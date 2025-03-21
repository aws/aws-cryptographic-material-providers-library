// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "Mutations.dfy"
include "InitializeMutation.dfy"
include "ApplyMutation.dfy"
include "KmsUtils.dfy"
include "DescribeMutation.dfy"
include "CreateKeys.dfy"

module AwsCryptographyKeyStoreAdminOperations refines AbstractAwsCryptographyKeyStoreAdminOperations {
  import opened AwsKmsUtils
  import opened StandardLibrary
    // import opened Wrappers
  import KmsArn
  import DefaultKeyStorageInterface
  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KMS = Com.Amazonaws.Kms
  import Mutations
  import KSAInitializeMutation = InternalInitializeMutation
  import KSAApplyMutation = InternalApplyMutation
  import DM = DescribeMutation
  import KmsUtils
  import AtomicPrimitives
  import CanonicalEncryptionContext
  import UUID
  import ErrorMessages = KeyStoreErrorMessages
  import Structure
  import KMSKeystoreOperations
  import Time
  import KO = KMSKeystoreOperations
  import CreateKeysHV2

  datatype Config = Config(
    nameonly logicalKeyStoreName: string,
    nameonly storage: KeyStoreTypes.IKeyStorageInterface
  )

  type InternalConfig = Config

  predicate ValidInternalConfig?(config: InternalConfig)
  {
    && config.storage.ValidState()
    && (config.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
        ==>
          config.logicalKeyStoreName == (config.storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName)
  }

  // This function is the lie we will tell ourselves
  // about what the mutation scope is.
  // You MUST NOT reveal this value.
  // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
  function {:opaque} MutationLie(): set<object>
  {{}}

  function method DefaultInitializeMutationDoNotVersion(
    input: Option<bool> := None
  ): (output: bool)
  {
    if input.None? then false else input.value
  }

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    config.storage.Modifies + MutationLie()
  }

  method ProvideKMSClient(
    kmsClient?: Option<KMS.Types.IKMSClient> := None
  )
    returns (output: Result<KMS.Types.IKMSClient, KMS.Types.Error>)
    // Because Dafny is not able to parse
    // the code that Smithy-Dafny produces for reference types inside a union,
    // the requires kms.ValidState() and modifies kmsClient are commented out.
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    // requires kms.kmsClient.Some? ==> kms.kmsClient.value.ValidState()
    // modifies (if kms.kmsClient.Some? then kms.kmsClient.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var kmsClient: KMS.Types.IKMSClient;
    if (kmsClient?.None?) {
      kmsClient :- KMS.KMSClient();
    } else {
      kmsClient := kmsClient?.value;
    }
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} kmsClient.Modifies < MutationLie();
    // If the customer gave us the KMS Client, it is fresh
    // If we create the KMS Client, it is fresh
    assume {:axiom} fresh(kmsClient) && fresh(kmsClient.Modifies);
    return Success(kmsClient);
  }

  method ResolveStrategy(
    kmsStratgey?: Option<KeyManagementStrategy>,
    config: InternalConfig
  )
    returns (output: Result<KmsUtils.keyManagerStrat, Error>)
    // Because Dafny is not able to parse
    // the code that Smithy-Dafny produces for reference types inside a union,
    // the requires kms.ValidState() and modifies kmsClient are commented out.
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    // requires
    //   kmsStratgey?.Some? ==> match kmsStratgey?.value {
    //       case AwsKmsReEncrypt(kms) => kms.kmsClient.Some? ==> kms.kmsClient.value.ValidState()
    //   }
    // modifies (if
    //   && kmsStratgey?.Some?
    //   && kmsStratgey?.value.AwsKmsReEncrypt?
    //   && kmsStratgey?.value.AwsKmsReEncrypt.kmsClient.Some?
    //   then kmsStratgey?.value.AwsKmsReEncrypt.kmsClient.value.Modifies else {})
    requires ValidInternalConfig?(config)
    ensures output.Success?
            ==>
              && match output.value {
                   case reEncrypt(km) => km.kmsClient.ValidState()
                   case decryptEncrypt(kmD, kmE) => kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
                 }
              && match output.value {
                   case reEncrypt(km) => config.storage.Modifies !! km.kmsClient.Modifies
                   case decryptEncrypt(kmD, kmE) => config.storage.Modifies !! (kmD.kmsClient.Modifies + kmE.kmsClient.Modifies)
                 }
              && match output.value {
                   case reEncrypt(km) => GetValidGrantTokens(Some(km.grantTokens)).Success?
                   case decryptEncrypt(kmD, kmE) =>
                     && AwsKmsUtils.GetValidGrantTokens(Some(kmD.grantTokens)).Success?
                     && AwsKmsUtils.GetValidGrantTokens(Some(kmE.grantTokens)).Success?
                 }

  {
    var input: KeyManagementStrategy;
    if (kmsStratgey?.None?) {
      var kms := KeyStoreTypes.AwsKms();
      input := KeyManagementStrategy.AwsKmsReEncrypt(kms);
    } else {
      input := kmsStratgey?.value;
    }
    match input {
      case AwsKmsReEncrypt(kms) =>
        var tuple :- ResolveKmsInput(kms, config);
        return Success(KmsUtils.keyManagerStrat.reEncrypt(tuple));
      case AwsKmsDecryptEncrypt(kmsDecryptEncrypt) =>
        :- Need(
          && kmsDecryptEncrypt.decrypt.Some?
          && kmsDecryptEncrypt.encrypt.Some?,
          Types.KeyStoreAdminException(message :=
                                         "MUST supply KMS clients to both decrypt and encrypt fields in AwsKmsDecryptEncrypt strategy."
          ));
        var decrypt :- ResolveKmsInput(kmsDecryptEncrypt.decrypt.value, config);
        var encrypt :- ResolveKmsInput(kmsDecryptEncrypt.encrypt.value, config);
        return Success(KmsUtils.keyManagerStrat.decryptEncrypt(decrypt, encrypt));
      case AwsKmsForHierarchyVersionTwo(kmsForHV2) =>
        :- Need(
          && kmsForHV2.generateRandom.Some?
          && kmsForHV2.encrypt.Some?
          && kmsForHV2.decrypt.Some?,
          Types.KeyStoreAdminException(message :=
                                         "At this time, users MUST supply KMS clients for generateRandom, encrypt, and decrypt."
          ));
        var generateRandom :- ResolveKmsInput(kmsForHV2.generateRandom.value, config);
        var decrypt :- ResolveKmsInput(kmsForHV2.decrypt.value, config);
        var encrypt :- ResolveKmsInput(kmsForHV2.encrypt.value, config);
        return Success(KmsUtils.keyManagerStrat.kmsForHV2(generateRandom, decrypt, encrypt));
    }
  }

  method ResolveKmsInput(
    kms: KeyStoreTypes.AwsKms,
    config: InternalConfig
  )
    returns (output: Result<KmsUtils.KMSTuple, Error>)
    // Because Dafny is not able to parse
    // the code that Smithy-Dafny produces for reference types inside a union,
    // the requires kms.ValidState() and modifies kmsClient are commented out.
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    // requires kms.kmsClient.Some? ==> kms.kmsClient.value.ValidState()
    // modifies (if kms.kmsClient.Some? then kms.kmsClient.value.Modifies else {})
    requires ValidInternalConfig?(config)
    ensures output.Success?
            ==>
              && (config.storage.Modifies !! output.value.kmsClient.Modifies)
              && output.value.kmsClient.ValidState()
              && GetValidGrantTokens(Some(output.value.grantTokens)).Success?
              && fresh(output.value.kmsClient) && fresh(output.value.kmsClient.Modifies)
  {
    var kmsClient? := ProvideKMSClient(kms.kmsClient);
    var kmsClient :- kmsClient?
    .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
    var grantTokens := GetValidGrantTokens(kms.grantTokens);
    :- Need(
      && grantTokens.Success?,
      Types.KeyStoreAdminException(
        message := "Grant Tokens passed to Key Store Admin are invalid.")
    );
    assume {:axiom} config.storage.Modifies !! kmsClient.Modifies;
    output := Success(KmsUtils.KMSTuple(kmsClient, grantTokens.value));
  }

  method ResolveSystemKey(
    systemKey: SystemKey,
    config: InternalConfig
  ) returns (output: Result<KmsUtils.InternalSystemKey, Error>)
    requires ValidInternalConfig?(config)
    // We do not know why these statements cannot be proven,
    // but we do not have the time to address it
    // It could be if we apply the MutableState trait from
    // https://github.com/smithy-lang/smithy-dafny/pull/543
    // that would allow us to address these issues.
    // requires match systemKey
    //          case kmsSymmetricEncryption(kmsSym) =>
    //            if kmsSym.AwsKms.kmsClient.Some?
    //            then kmsSym.AwsKms.kmsClient.value.ValidState()
    //            else true
    //          case trustStorage => true
    // modifies match systemKey
    //          case kmsSymmetricEncryption(kmsSym) =>
    //            if kmsSym.AwsKms.kmsClient.Some?
    //            then kmsSym.AwsKms.kmsClient.value.Modifies
    //            else {}
    //          case trustStorage => {}
    ensures output.Success?
            ==>
              && (config.storage.Modifies !! output.value.Modifies)
              && output.value.ValidState()
              && fresh(output.value.Modifies)
  {
    if (systemKey.trustStorage?) {
      return Success(KmsUtils.TrustStorage());
    }
    var kmsSym := systemKey.kmsSymmetricEncryption;
    var tuple :- ResolveKmsInput(kmsSym.AwsKms, config);
    var internal := KmsUtils.KmsSymEnc(
      Tuple := tuple,
      KeyId := kmsSym.KmsArn);
    assert internal.ValidState();
    return Success(internal);
  }

  // TODO: Refactor Config to allow DecryptEncryptStrategy
  function method LegacyConfig(
    keyManagerStrat: KmsUtils.keyManagerStrat,
    kmsArn: Types.KmsSymmetricKeyArn,
    config: InternalConfig
  ): (output: Result<KeyStoreOperations.Config, Error>)
    requires ValidInternalConfig?(config)
    requires
      && keyManagerStrat.reEncrypt?
      && keyManagerStrat.reEncrypt.kmsClient.ValidState()
      && GetValidGrantTokens(Some(keyManagerStrat.reEncrypt.grantTokens)).Success?
    ensures output.Success?
            ==>
              && keyManagerStrat.reEncrypt.kmsClient.ValidState()
    ensures output.Success? ==> KeyStoreOperations.ValidInternalConfig?(output.value)
  {
    var _ :- KmsArn.IsValidKeyArn(match kmsArn
                                  case KmsKeyArn(kmsKeyArn) => kmsKeyArn
                                  case KmsMRKeyArn(kmsMRKeyArn) => kmsMRKeyArn)
             .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    var legacyConfig := KeyStoreOperations.Config(
                          id := "",
                          ddbTableName := None,
                          logicalKeyStoreName := config.logicalKeyStoreName,
                          kmsConfiguration := match kmsArn
                          case KmsKeyArn(kmsKeyArn) => KeyStoreOperations.Types.kmsKeyArn(kmsKeyArn)
                          case KmsMRKeyArn(kmsMRKeyArn) => KeyStoreOperations.Types.kmsMRKeyArn(kmsMRKeyArn),
                          grantTokens := keyManagerStrat.reEncrypt.grantTokens,
                          kmsClient := keyManagerStrat.reEncrypt.kmsClient,
                          ddbClient := None,
                          storage := config.storage,
                          kmsConstructedRegion := None,
                          ddbConstructedRegion := None
                        );

    // These are required to use the existing logic.
    // This is required because Dafny is not able to parse
    // the code that Smithy-Dafny produces for reference types inside a union
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} legacyConfig.kmsClient.ValidState();
    // This is for the legacy client. Again, this should follow from the code that smithy-dafny produces.
    assume {:axiom} legacyConfig.storage.Modifies !! legacyConfig.kmsClient.Modifies;

    Success(legacyConfig)
  }

  predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
  {true}

  method CreateKey ( config: InternalConfig , input: CreateKeyInput )
    returns (output: Result<CreateKeyOutput, Error>)
  {
    // If hierarchyVersion is not specified, default to v1
    var hierarchyVersion := if input.HierarchyVersion.Some? then
      input.HierarchyVersion.value
    else KeyStoreTypes.HierarchyVersion.v1;

    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);

    if (hierarchyVersion == KeyStoreTypes.HierarchyVersion.v2) {
      var encryptDecryptConfig :- EncryptDecryptConfig(keyManagerStrat, input.KmsArn, config);

      output := CreateKeyHV2(config, input, keyManagerStrat);
    }
    else {
      :- Need(
        keyManagerStrat.reEncrypt?,
        Types.KeyStoreAdminException(message :="Only ReEncrypt is supported at this time.")
      );

      var legacyConfig :- LegacyConfig(keyManagerStrat, input.KmsArn, config);

      // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
      assume {:axiom} legacyConfig.kmsClient.Modifies < MutationLie();

      var output? := KeyStoreOperations.CreateKey(
        config := legacyConfig,
        input := KeyStoreOperations.Types.CreateKeyInput(
          branchKeyIdentifier := input.Identifier,
          encryptionContext := input.EncryptionContext
        )
      );
      var value :- output?
      .MapFailure(e => Types.AwsCryptographyKeyStore(e));

      output := Success(
        Types.CreateKeyOutput(
          Identifier := value.branchKeyIdentifier
        ));
    }
  }

  // TODO-HV-2: Add Pre & Post Conditions -> Maybe copy from KeyStore
  // TODO-HV-2: Should handle KeyManagerStrat for HV2
  method CreateKeyHV2(config: InternalConfig, input: CreateKeyInput, keyManagerStrat: KmsUtils.keyManagerStrat)
    returns (output: Result<Types.CreateKeyOutput, Error>)
  {

    :- Need(input.Identifier.Some? ==>
              && input.EncryptionContext.Some?
              && 0 < |input.EncryptionContext.value|,
            Types.KeyStoreAdminException(message := ErrorMessages.CUSTOM_BRANCH_KEY_ID_NEED_EC));

    :- Need(
      KO.HasKeyId(config.kmsConfiguration),
      Types.KeyStoreAdminException(
        message := ErrorMessages.DISCOVERY_CREATE_KEY_NOT_SUPPORTED
      )
    );

    var branchKeyIdentifier: string;

    if input.Identifier.None? {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
      //# If no branch key id is provided,
      //# then this operation MUST create a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
      //# to be used as the branch key id.
      var maybeBranchKeyId := UUID.GenerateUUID();
      branchKeyIdentifier :- maybeBranchKeyId
      .MapFailure(e => Types.KeyStoreAdminException(message := e));
    } else {
      :- Need(0 < |input.Identifier.value|, Types.KeyStoreAdminException(message := "Custom branch key id can not be an empty string."));
      branchKeyIdentifier := input.Identifier.value;
    }

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //# - `timestamp`: a timestamp for the current time.
    //# This timestamp MUST be in ISO8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(message := e));

    var maybeBranchKeyVersion := UUID.GenerateUUID();
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //# - `version`: a new guid. This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var branchKeyVersion :- maybeBranchKeyVersion
    .MapFailure(e => Types.KeyStoreAdminException(message := e));

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
            Types.KeyStoreAdminException( message := ErrorMessages.UTF8_ENCODING_ENCRYPTION_CONTEXT_ERROR));


    output := CreateKeysHV2.CreateBranchAndBeaconKeys(
      branchKeyIdentifier,
      map i <- encodedEncryptionContext :: i.0.value := i.1.value,
      timestamp,
      branchKeyVersion,
      config.logicalKeyStoreName,
      config.kmsConfiguration,
      config.grantTokens,
      config.kmsClient,
      config.storage
    );
  }

  predicate VersionKeyEnsuresPublicly(input: VersionKeyInput, output: Result<VersionKeyOutput, Error>)
  {true}

  method VersionKey(config: InternalConfig, input: VersionKeyInput)
    returns (output: Result<VersionKeyOutput, Error>)
  {

    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
    :- Need(
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="Only ReEncrypt is supported at this time.")
    );

    var legacyConfig :- LegacyConfig(keyManagerStrat, input.KmsArn, config);

    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} legacyConfig.kmsClient.Modifies < MutationLie();

    var output? := KeyStoreOperations.VersionKey(
      config := legacyConfig,
      input := KeyStoreOperations.Types.VersionKeyInput(
        branchKeyIdentifier := input.Identifier
      )
    );
    var value :- output?
    .MapFailure(e => Types.AwsCryptographyKeyStore(e));
    output := Success(Types.VersionKeyOutput());
  }

  predicate InitializeMutationEnsuresPublicly(input: InitializeMutationInput, output: Result<InitializeMutationOutput, Error>)
  {true}

  method InitializeMutation(config: InternalConfig, input: InitializeMutationInput )
    returns (output: Result<InitializeMutationOutput, Error>)
  {
    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
    var systemKey :- ResolveSystemKey(input.SystemKey, config);
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    if keyManagerStrat.reEncrypt? {
      assume {:axiom} keyManagerStrat.reEncrypt.kmsClient.Modifies < MutationLie();
    }

    if keyManagerStrat.decryptEncrypt? {
      assume {:axiom} keyManagerStrat.decrypt.kmsClient.Modifies < MutationLie();
      assume {:axiom} keyManagerStrat.encrypt.kmsClient.Modifies < MutationLie();
      assume {:axiom} keyManagerStrat.decrypt.kmsClient.Modifies !! keyManagerStrat.encrypt.kmsClient.Modifies;
    }
    assume {:axiom} keyManagerStrat.Modifies !! systemKey.Modifies;

    var internalInput := KSAInitializeMutation.InternalInitializeMutationInput(
      Identifier := input.Identifier,
      Mutations := input.Mutations,
      SystemKey := systemKey,
      DoNotVersion := DefaultInitializeMutationDoNotVersion(input.DoNotVersion),
      logicalKeyStoreName := config.logicalKeyStoreName,
      keyManagerStrategy := keyManagerStrat,
      storage := config.storage
    );

    internalInput :- KSAInitializeMutation.ValidateInitializeMutationInput(internalInput);
    output := KSAInitializeMutation.InitializeMutation(internalInput);
    return output;
  }

  predicate ApplyMutationEnsuresPublicly(input: ApplyMutationInput, output: Result<ApplyMutationOutput, Error>)
  {true}

  method ApplyMutation(config: InternalConfig, input: ApplyMutationInput)
    returns (output: Result<ApplyMutationOutput, Error>)
  {
    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
    var systemKey :- ResolveSystemKey(input.SystemKey, config);
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    if keyManagerStrat.reEncrypt? {
      assume {:axiom} keyManagerStrat.reEncrypt.kmsClient.Modifies < MutationLie();
    }
    if keyManagerStrat.decryptEncrypt? {
      assume {:axiom} keyManagerStrat.decrypt.kmsClient.Modifies < MutationLie();
      assume {:axiom} keyManagerStrat.encrypt.kmsClient.Modifies < MutationLie();
      assume {:axiom} keyManagerStrat.decrypt.kmsClient.Modifies !! keyManagerStrat.encrypt.kmsClient.Modifies;
    }
    assume {:axiom} keyManagerStrat.Modifies !! systemKey.Modifies;

    var internalInput := KSAApplyMutation.InternalApplyMutationInput(
      MutationToken := input.MutationToken,
      PageSize := input.PageSize,
      SystemKey := systemKey,
      logicalKeyStoreName := config.logicalKeyStoreName,
      keyManagerStrategy := keyManagerStrat,
      storage := config.storage);

    var _ :- KSAApplyMutation.ValidateApplyMutationInput(internalInput);
    output := KSAApplyMutation.ApplyMutation(internalInput);
    return output;
  }

  predicate DescribeMutationEnsuresPublicly(
    input: DescribeMutationInput,
    output: Result<DescribeMutationOutput, Error>
  )
  {true}

  method DescribeMutation(
    config: InternalConfig,
    input: DescribeMutationInput
  )
    returns (output: Result<DescribeMutationOutput, Error>)
  {
    var input := DM.InternalDescribeMutationInput(
      Identifier := input.Identifier,
      storage := config.storage);
    output := DM.DescribeMutation(input);
    return output;
  }
}
