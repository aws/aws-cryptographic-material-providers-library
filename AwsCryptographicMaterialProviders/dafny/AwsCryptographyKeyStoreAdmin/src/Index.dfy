// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "AwsCryptographyKeyStoreAdminOperations.dfy"
  // include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:extern "software.amazon.cryptography.keystoreadmin.internaldafny"}
  KeyStoreAdmin refines AbstractAwsCryptographyKeyStoreAdminService
{
  import opened AwsKmsUtils
  import DDB = ComAmazonawsDynamodbTypes
  import DefaultEncryptedKeyStore
  import Operations = AwsCryptographyKeyStoreAdminOperations

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
  {
    return Failure(KeyStoreAdminException(message := "Implement me!"));
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
