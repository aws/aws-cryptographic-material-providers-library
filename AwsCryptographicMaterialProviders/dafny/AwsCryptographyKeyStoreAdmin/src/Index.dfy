// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "AwsCryptographyKeyStoreAdminOperations.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:extern "software.amazon.cryptography.keystoreadmin.internaldafny"}
  KeyStoreAdmin refines AbstractAwsCryptographyKeyStoreAdminService
{
  import opened AwsKmsUtils
  import DDB = ComAmazonawsDynamodbTypes
  import DefaultEncryptedKeyStore
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

  method KeyStoreAdmin(config: KeyStoreAdminConfig)
    returns (res: Result<KeyStoreAdminClient, Error>)
  {
    // These values are not assigned on purpose.
    // Since Dafny will prove definite assignment when these values
    // are used the MUST have values.
    // This helps bind their assignment to the correctness
    // that they are used when referencing them in the specification.
    // By looking at the value
    // TODO: Parse TableName for Region, in case it is a full arn
    //var inferredRegion: Option<string>;
    //var ddbConstructedRegion: Option<string>;

    // TODO: allow for None DDB Client
    if (config.storage.ddb?) {
      :- Need(&& config.storage.ddb? && config.storage.ddb.ddbClient.Some?,
              KeyStoreAdminException(message := "Key Store Admin Client requires a constructed DDB Client.")
      );
    }
    assert config.storage.ddb? ==> config.storage.ddb.ddbClient.Some?;

    var storage: KeyStoreTypes.IEncryptedKeyStore;
    if config.storage.custom? {
      storage := config.storage.custom;
      :- Need(
        && storage is DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore
        && config.logicalKeyStoreName == (storage as DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore).logicalKeyStoreName,
        KeyStoreAdminException(message := "Storage's Logical Key Store Name does not match passed Logical Key Store Name")
      );
    } else {
      storage := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
        ddbTableName := config.storage.ddb.ddbTableName,
        ddbClient := config.storage.ddb.ddbClient.value,
        logicalKeyStoreName := config.logicalKeyStoreName
      );
    }
    var internalConfig := Operations.Config(
      logicalKeyStoreName := config.logicalKeyStoreName,
      storage := storage,
      kmsConstructedRegion := None(),
      ddbConstructedRegion := None()
    );
    assert Operations.ValidInternalConfig?(internalConfig);
    var client := new KeyStoreAdminClient(internalConfig);
    return Success(client);
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
    }
  }
}
