// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "AwsCryptographyKeyStoreAdminOperations.dfy"
  // include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:extern "software.amazon.cryptography.keystoreadmin.internaldafny"} KeyStoreAdmin refines AbstractAwsCryptographyKeyStoreAdminService
{
  import opened AwsKmsUtils
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import Operations = AwsCryptographyKeyStoreAdminOperations
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes

  // There is no sensible default, so define something that passes verification but will fail at runtime
  function method DefaultKeyStoreAdminConfig(): KeyStoreAdminConfig
  {
    var ddb:= AwsCryptographyKeyStoreTypes.DynamoDBTable(
                ddbTableName := "None",
                ddbClient := None()
              );
    KeyStoreAdminConfig(
      logicalKeyStoreName := "None",
      storage := AwsCryptographyKeyStoreTypes.Storage.ddb(ddb)
    )
  }

  method {:vcs_split_on_every_assert} KeyStoreAdmin(config: KeyStoreAdminConfig)
    returns (res: Result<KeyStoreAdminClient, Error>)
    // Copying from KS/Index.dfy
    ensures
      && res.Success?
      && config.storage.custom? ==>
        && res.value.config.storage == config.storage.custom
    ensures
      && res.Success? ==>
        && match config.storage {
          case custom(custom) => res.value.config.storage == custom
          case ddb(ddb) =>
            && res.value.config.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
            && var storage: DefaultKeyStorageInterface.DynamoDBKeyStorageInterface := res.value.config.storage;
            && fresh(storage)
            && storage.logicalKeyStoreName == config.logicalKeyStoreName
            && (ddb.ddbClient.Some? ==> (storage.ddbClient == ddb.ddbClient.value))
            && fresh(storage.ddbClient)
        }
  {
    var storage: KeyStoreTypes.IKeyStorageInterface;
    match config.storage {
      case custom(custom) =>
        storage := custom;
        // If the custom storage is default DDBStorage, it's logical name must be correct
        :- Need(
          storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface ==>
            config.logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName,
          KeyStoreAdminException(message := "Storage's Logical Key Store Name does not match passed Logical Key Store Name")
        );
      case ddb(ddb) =>
        var physicalNameUTF8? := UTF8.Encode(ddb.ddbTableName);
        if (physicalNameUTF8?.Failure?) {
          return Failure(KeyStoreAdminException(message := "Could not UTF8 Encode DDB Table Name: " + physicalNameUTF8?.error));
        }
        var logicalNameUTF8? := UTF8.Encode(config.logicalKeyStoreName);
        if (logicalNameUTF8?.Failure?) {
          return Failure(KeyStoreAdminException(message := "Could not UTF8 Encode Logical Name: " + logicalNameUTF8?.error));
        }
        var ddbClient? := ProvideDDBClient(ddb.ddbClient);
        var ddbClient :- ddbClient?
        .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
        storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
          ddbTableName := ddb.ddbTableName,
          ddbClient := ddbClient,
          logicalKeyStoreName := config.logicalKeyStoreName,
          ddbTableNameUtf8 := physicalNameUTF8?.value,
          logicalKeyStoreNameUtf8 := logicalNameUTF8?.value
        );
    }
    // This just asserts that storage is assigned
    // Any assignment after this a mistake
    assert allocated(storage);

    var internalConfig := Operations.Config(
      logicalKeyStoreName := config.logicalKeyStoreName,
      storage := storage
    );
    assert Operations.ValidInternalConfig?(internalConfig);
    var client := new KeyStoreAdminClient(internalConfig);
    assert client.ValidState();
    res := Success(client);
    assert fresh(
        res.value.Modifies
        - ( if config.storage.custom? then
              config.storage.custom.Modifies
            else {}
        ) - ( if config.storage.ddb? then
                if config.storage.ddb.ddbClient.Some? then
                  config.storage.ddb.ddbClient.value.Modifies
                else {}
              else {}
        ) ) by
    {
      assert res.value.Modifies == Operations.ModifiesInternalConfig(internalConfig) + {res.value.History};
      assert fresh(res.value.History);
      assert Operations.ModifiesInternalConfig(internalConfig) == internalConfig.storage.Modifies + Operations.MutationLie();
      reveal Operations.MutationLie();
    }
  }

  class KeyStoreAdminClient... {

    predicate {:vcs_split_on_every_assert} {:rlimit 3000} ValidState() {
      && Operations.ValidInternalConfig?(config)
      && History !in Operations.ModifiesInternalConfig(config)
      && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    }

    constructor(config: Operations.InternalConfig)
    {
      this.config := config;
      History := new IKeyStoreAdminClientCallHistory();
      Modifies := Operations.ModifiesInternalConfig(config) + {History};
      // It is OK to reveal this value because there is no history,
      // and therefore revealing the lie will NOT make you prove false
      reveal Operations.MutationLie();
    }
  }

  method ProvideDDBClient(
    ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    returns (output: Result<DDB.Types.IDynamoDBClient, DDB.Types.Error>)
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
              && (ddbClient?.Some? ==> output.value == ddbClient?.value)
  {
    var ddbClient: DDB.Types.IDynamoDBClient;
    if (ddbClient?.None?) {
      ddbClient :- DDB.DynamoDBClient();
    } else {
      ddbClient := ddbClient?.value;
    }
    // If the customer gave us the DDB Client, it is fresh
    // If we create the DDB Client, it is fresh
    assume {:axiom} fresh(ddbClient) && fresh(ddbClient.Modifies);
    return Success(ddbClient);
  }
}
