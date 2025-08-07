// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsUtils.dfy"

include "GetKeys.dfy"
include "CreateKeyStoreTable.dfy"
include "CreateKeys.dfy"
include "Structure.dfy"
include "ErrorMessages.dfy"
include "KmsArn.dfy"

module AwsCryptographyKeyStoreOperations refines AbstractAwsCryptographyKeyStoreOperations {
  import opened AwsKmsUtils
  import opened StandardLibrary.MemoryMath
  import KO = KMSKeystoreOperations
  import KMS = ComAmazonawsKmsTypes
  import DDB = ComAmazonawsDynamodbTypes
  import MPL = AwsCryptographyMaterialProvidersTypes
  import CreateKeys
  import CreateKeyStoreTable
  import GetKeys
  import UUID
  import Time
  import Structure
  import ErrorMessages = KeyStoreErrorMessages
  import KmsArn

  datatype Config = Config(
    nameonly id: string,
    nameonly ddbTableName: DDB.TableName,
    nameonly logicalKeyStoreName: string,
    nameonly kmsConfiguration: KMSConfiguration,
    nameonly grantTokens: KMS.GrantTokenList,
    nameonly kmsClient: ComAmazonawsKmsTypes.IKMSClient,
    nameonly ddbClient: ComAmazonawsDynamodbTypes.IDynamoDBClient
  )

  type InternalConfig = Config

  predicate ValidInternalConfig?(config: InternalConfig)
  {
    && DDB.IsValid_TableName(config.ddbTableName)
    && (config.kmsConfiguration.kmsKeyArn? ==> KmsArn.ValidKmsArn?(config.kmsConfiguration.kmsKeyArn))
    && (config.kmsConfiguration.kmsMRKeyArn? ==> KmsArn.ValidKmsArn?(config.kmsConfiguration.kmsMRKeyArn))
    && config.kmsClient.ValidState()
    && config.ddbClient.ValidState()
    && config.ddbClient.Modifies !! config.kmsClient.Modifies
  }

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    config.kmsClient.Modifies + config.ddbClient.Modifies
  }

  predicate GetKeyStoreInfoEnsuresPublicly(output: Result<GetKeyStoreInfoOutput, Error>)
  {true}

  method GetKeyStoreInfo(config: InternalConfig)
    returns (output: Result<GetKeyStoreInfoOutput, Error>)
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#getkeystoreinfo
    //= type=implication
    //# This operation MUST return the keystore information in this keystore configuration.
    ensures output.Success? ==>
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getkeystoreinfo
              //= type=implication
              //# This MUST include:
              && output.value.keyStoreId == config.id
              && output.value.keyStoreName == config.ddbTableName
              && output.value.logicalKeyStoreName == config.logicalKeyStoreName
              && output.value.grantTokens == config.grantTokens
              && output.value.kmsConfiguration == config.kmsConfiguration
  {
    output := Success(
      Types.GetKeyStoreInfoOutput(
        keyStoreId := config.id,
        keyStoreName := config.ddbTableName,
        logicalKeyStoreName := config.logicalKeyStoreName,
        grantTokens := config.grantTokens,
        kmsConfiguration := config.kmsConfiguration
      )
    );
  }

  predicate CreateKeyStoreEnsuresPublicly(input: CreateKeyStoreInput, output: Result<CreateKeyStoreOutput, Error>)
  {true}

  method CreateKeyStore ( config: InternalConfig, input: CreateKeyStoreInput )
    returns (output: Result<CreateKeyStoreOutput, Error>)
    ensures output.Success? ==>
              && AwsArnParsing.ParseAmazonDynamodbTableName(output.value.tableArn).Success?
              && AwsArnParsing.ParseAmazonDynamodbTableName(output.value.tableArn).value == config.ddbTableName
  {
    var ddbTableArn :- CreateKeyStoreTable.CreateKeyStoreTable(config.ddbTableName, config.ddbClient);
    var tableName := AwsArnParsing.ParseAmazonDynamodbTableName(ddbTableArn);
    :- Need(
      && tableName.Success?
      && tableName.value == config.ddbTableName,
      Types.KeyStoreException(message := "Configured DDB Table Name does not match parsed Table Name from DDB Table Arn.")
    );

    output := Success(Types.CreateKeyStoreOutput(tableArn := ddbTableArn));
  }

  predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
  {true}

  method CreateKey ( config: InternalConfig , input: CreateKeyInput )
    returns (output: Result<CreateKeyOutput, Error>)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If an optional branch key id is provided
    //# and no encryption context is provided this operation MUST fail.
    ensures
      && input.branchKeyIdentifier.Some?
      && input.encryptionContext.None?
      ==> output.Failure?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If the Keystore's KMS Configuration is `Discovery` or `MRDiscovery`,
    //# this operation MUST fail.
    ensures
      && !KO.HasKeyId(config.kmsConfiguration)
      ==> output.Failure?
  {
    OptionalMapIsSafeBecauseItIsInMemory(input.encryptionContext);
    :- Need(input.branchKeyIdentifier.Some? ==>
              && input.encryptionContext.Some?
              && 0 < |input.encryptionContext.value| as uint64,
            Types.KeyStoreException(message := ErrorMessages.CUSTOM_BRANCH_KEY_ID_NEED_EC));

    :- Need(
      KO.HasKeyId(config.kmsConfiguration),
      Types.KeyStoreException(
        message := ErrorMessages.DISCOVERY_CREATE_KEY_NOT_SUPPORTED
      )
    );

    var hierarchyVersion : HierarchyVersion;
    if input.hierarchyVersion.None? {
      hierarchyVersion := HierarchyVersion.v1;
    } else {
      hierarchyVersion := input.hierarchyVersion.value;
    }

    var branchKeyIdentifier: string;

    if input.branchKeyIdentifier.None? {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
      //# If no branch key id is provided,
      //# then this operation MUST create a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
      //# to be used as the branch key id.
      var maybeBranchKeyId := UUID.GenerateUUID();
      branchKeyIdentifier :- maybeBranchKeyId
      .MapFailure(e => Types.KeyStoreException(message := e));
    } else {
      SequenceIsSafeBecauseItIsInMemory(input.branchKeyIdentifier.value);
      :- Need(0 < |input.branchKeyIdentifier.value| as uint64, Types.KeyStoreException(message := "Custom branch key id can not be an empty string."));
      branchKeyIdentifier := input.branchKeyIdentifier.value;
    }

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //# - `timestamp`: a timestamp for the current time.
    //# This timestamp MUST be in ISO8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreException(message := e));

    var maybeBranchKeyVersion := UUID.GenerateUUID();
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //# - `version`: a new guid. This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var branchKeyVersion :- maybeBranchKeyVersion
    .MapFailure(e => Types.KeyStoreException(message := e));

    var unwrapEncryptionContext := input.encryptionContext.UnwrapOr(map[]);
    var encodedEncryptionContext
      := set k <- unwrapEncryptionContext
      ::
        (UTF8.Decode(k), UTF8.Decode(unwrapEncryptionContext[k]), k);

      // This SHOULD be impossible
      // A Dafny string SHOULD all be encodable
    :- Need(forall i <- encodedEncryptionContext
              ::
                && i.0.Success?
                && i.1.Success?
                && DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + i.0.value)
                   // Dafny requires that I *prove* that k == Encode(Decode(k))
                   // Since UTF8 can be lossy in some implementations
                   // this is the simplest...
                   // A prove that ValidUTF8Seq(i) ==> Decode(i).Success?
                   // would improve the situation
                && var encoded := UTF8.Encode(i.0.value);
                && encoded.Success?
                && i.2 == encoded.value
           ,
            Types.KeyStoreException( message := ErrorMessages.UTF8_ENCODING_ENCRYPTION_CONTEXT_ERROR));

    if hierarchyVersion == HierarchyVersion.v1 {
      output := CreateKeys.CreateBranchAndBeaconKeys(
        branchKeyIdentifier,
        map i <- encodedEncryptionContext :: i.0.value := i.1.value,
        timestamp,
        branchKeyVersion,
        config.ddbTableName,
        config.logicalKeyStoreName,
        config.kmsConfiguration,
        config.grantTokens,
        config.kmsClient,
        config.ddbClient
      );
    } else {
      output := CreateKeys.CreateBranchAndBeaconKeysVersion2(
        branchKeyIdentifier,
        map i <- encodedEncryptionContext :: i.0.value := i.1.value,
        timestamp,
        branchKeyVersion,
        config.ddbTableName,
        config.logicalKeyStoreName,
        config.kmsConfiguration,
        config.grantTokens,
        config.kmsClient,
        config.ddbClient,
        hierarchyVersion
      );
    }
  }

  predicate VersionKeyEnsuresPublicly(input: VersionKeyInput, output: Result<VersionKeyOutput, Error>)
  {true}

  method VersionKey(config: InternalConfig, input: VersionKeyInput)
    returns (output: Result<VersionKeyOutput, Error>)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    //= type=implication
    //# If the Keystore's KMS Configuration is `Discovery` or `MRDiscovery`,
    //# this operation MUST immediately fail.
    ensures
      && !KO.HasKeyId(config.kmsConfiguration)
      ==> output.Failure?
  {
    :- Need(
      KO.HasKeyId(config.kmsConfiguration),
      Types.KeyStoreException(
        message := ErrorMessages.DISCOVERY_VERSION_KEY_NOT_SUPPORTED
      )
    );

    SequenceIsSafeBecauseItIsInMemory(input.branchKeyIdentifier);
    :- Need(0 < |input.branchKeyIdentifier| as uint64, Types.KeyStoreException(message := ErrorMessages.BRANCH_KEY_ID_NEEDED));

    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreException(message := e));

    var maybeBranchKeyVersion := UUID.GenerateUUID();
    var branchKeyVersion :- maybeBranchKeyVersion
    .MapFailure(e => Types.KeyStoreException(message := e));

    output := CreateKeys.VersionActiveBranchKey(
      input,
      timestamp,
      branchKeyVersion,
      config.ddbTableName,
      config.logicalKeyStoreName,
      config.kmsConfiguration,
      config.grantTokens,
      config.kmsClient,
      config.ddbClient
    );
  }

  predicate GetActiveBranchKeyEnsuresPublicly(input: GetActiveBranchKeyInput, output: Result<GetActiveBranchKeyOutput, Error>)
  {true}

  method GetActiveBranchKey(config: InternalConfig, input: GetActiveBranchKeyInput)
    returns (output: Result<GetActiveBranchKeyOutput, Error>)
  {
    output := GetKeys.GetActiveKeyAndUnwrap(
      input,
      config.ddbTableName,
      config.logicalKeyStoreName,
      config.kmsConfiguration,
      config.grantTokens,
      config.kmsClient,
      config.ddbClient
    );
  }

  predicate GetBranchKeyVersionEnsuresPublicly(input: GetBranchKeyVersionInput, output: Result<GetBranchKeyVersionOutput, Error>)
  {true}

  method GetBranchKeyVersion(config: InternalConfig, input: GetBranchKeyVersionInput)
    returns (output: Result<GetBranchKeyVersionOutput, Error>)
  {
    output := GetKeys.GetBranchKeyVersion(
      input,
      config.ddbTableName,
      config.logicalKeyStoreName,
      config.kmsConfiguration,
      config.grantTokens,
      config.kmsClient,
      config.ddbClient
    );
  }

  predicate GetBeaconKeyEnsuresPublicly(input: GetBeaconKeyInput, output: Result<GetBeaconKeyOutput, Error>)
  {true}

  method GetBeaconKey(config: InternalConfig, input: GetBeaconKeyInput)
    returns (output: Result<GetBeaconKeyOutput, Error>)
  {
    output := GetKeys.GetBeaconKeyAndUnwrap(
      input,
      config.ddbTableName,
      config.logicalKeyStoreName,
      config.kmsConfiguration,
      config.grantTokens,
      config.kmsClient,
      config.ddbClient
    );
  }
}
