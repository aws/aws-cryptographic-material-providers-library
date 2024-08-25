// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
  // include "../../AwsCryptographyKeyStore/src/AwsCryptographyKeyStoreOperations.dfy"
  // include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsUtils.dfy"

// include "GetKeys.dfy"
// include "CreateKeyStoreTable.dfy"
// include "CreateKeys.dfy"
// include "Structure2.dfy"
// include "ErrorMessages.dfy"
// include "KmsArn.dfy"
// include "DefaultEncryptedKeyStore.dfy"

module AwsCryptographyKeyStoreAdminOperations refines AbstractAwsCryptographyKeyStoreAdminOperations {
  import opened AwsKmsUtils
  import KO = KMSKeystoreOperations
  import KMS = ComAmazonawsKmsTypes
  import DDB = ComAmazonawsDynamodbTypes
  import MPL = AwsCryptographyMaterialProvidersTypes
  import CreateKeys
  import CreateKeyStoreTable
  import GetKeys
  import UUID
  import Time
    // import Structure2
  import ErrorMessages = KeyStoreErrorMessages
  import KmsArn
  import DefaultEncryptedKeyStore

  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = KeyStoreOperations.Types

  datatype Config = Config(
    // nameonly id: string,
    // nameonly ddbTableName: Option<DDB.TableName>,
    nameonly logicalKeyStoreName: string,
    // nameonly kmsConfiguration: KMSConfiguration,
    // nameonly grantTokens: KMS.GrantTokenList,
    // nameonly kmsClient: ComAmazonawsKmsTypes.IKMSClient,
    // nameonly ddbClient: Option<ComAmazonawsDynamodbTypes.IDynamoDBClient>,
    nameonly storage: KeyStoreTypes.IEncryptedKeyStore,
    nameonly ghost kmsConstructedRegion: Option<string>,
    nameonly ghost ddbConstructedRegion: Option<string>
  )

  type InternalConfig = Config

  predicate ValidInternalConfig?(config: InternalConfig)
  {
    && true

    // && (config.kmsConfiguration.kmsKeyArn? ==> KmsArn.ValidKmsArn?(config.kmsConfiguration.kmsKeyArn))
    // && (config.kmsConfiguration.kmsMRKeyArn? ==> KmsArn.ValidKmsArn?(config.kmsConfiguration.kmsMRKeyArn))
    // && config.kmsClient.ValidState()
    && config.storage.ValidState()
       // && config.storage.Modifies !! config.kmsClient.Modifies
    && (config.storage is DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore
        ==>
          config.logicalKeyStoreName == (config.storage as DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore).logicalKeyStoreName)
  }

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    config.storage.Modifies
  }


  predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
  {true}

  method CreateKey ( config: InternalConfig , input: CreateKeyInput )
    returns (output: Result<CreateKeyOutput, Error>)
  {

    :- Need(
      KmsArn.ValidKmsArn?(match input.kmsArn
                          case kmsKeyArn(kmsKeyArn) => kmsKeyArn
                          case kmsMRKeyArn(kmsMRKeyArn) => kmsMRKeyArn),
      Types.KeyStoreAdminException(
        message := ErrorMessages.CREATE_KEY_STORE_DEPRECATED
      )
    );

    match input.kms
    case ReEncrypt(kmsClient) =>

      assume {:axiom} config.storage.Modifies !! kmsClient.Modifies;
      assume kmsClient.ValidState();

      var legacyConfig := KeyStoreOperations.Config(
        id := "",
        ddbTableName := None,
        logicalKeyStoreName := config.logicalKeyStoreName,
        kmsConfiguration := match input.kmsArn
        case kmsKeyArn(kmsKeyArn) => KeyStoreOperations.Types.kmsKeyArn(kmsKeyArn)
        case kmsMRKeyArn(kmsMRKeyArn) => KeyStoreOperations.Types.kmsMRKeyArn(kmsMRKeyArn),
        grantTokens := [],
        kmsClient := kmsClient,
        ddbClient := None,
        storage := config.storage,
        kmsConstructedRegion := None,
        ddbConstructedRegion := None
      );

      assert KeyStoreOperations.ValidInternalConfig?(legacyConfig);

      var output? := KeyStoreOperations.CreateKey(
        config := legacyConfig,
        input := KeyStoreOperations.Types.CreateKeyInput(
          branchKeyIdentifier := input.branchKeyIdentifier,
          encryptionContext := input.encryptionContext
        )
      );

      var value :- output?
      .MapFailure(e => Types.AwsCryptographyKeyStore(e));

      output := Success(Types.CreateKeyOutput(
                          branchKeyIdentifier := value.branchKeyIdentifier
                        ));
  }


  // predicate VersionKeyEnsuresPublicly(input: VersionKeyInput, output: Result<VersionKeyOutput, Error>)
  // {true}

  // method VersionKey(config: InternalConfig, input: VersionKeyInput)
  //   returns (output: Result<VersionKeyOutput, Error>)

}
