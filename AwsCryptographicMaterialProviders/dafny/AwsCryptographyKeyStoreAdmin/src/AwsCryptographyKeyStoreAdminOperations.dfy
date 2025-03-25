// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "Mutations.dfy"
include "InitializeMutation.dfy"
include "ApplyMutation.dfy"
include "KmsUtils.dfy"
include "DescribeMutation.dfy"

module AwsCryptographyKeyStoreAdminOperations refines AbstractAwsCryptographyKeyStoreAdminOperations {
  import opened AwsKmsUtils
  import KmsArn
  import DefaultKeyStorageInterface
  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = KeyStoreOperations.Types
  import KMS = Com.Amazonaws.Kms
  import Mutations
  import KSAInitializeMutation = InternalInitializeMutation
  import KSAApplyMutation = InternalApplyMutation
  import DM = DescribeMutation
  import KmsUtils

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
    ensures output.Success? ==> output.value.ValidState() && config.storage.Modifies !! output.value.Modifies
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
      case AwsKmsSimple(kms) =>
        var tuple :- ResolveKmsInput(kms, config);
        return Success(KmsUtils.keyManagerStrat.kmsSimple(tuple));
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

  method ResolveHierarchyVersionForCreateKey(
    hierarchyVersion?: Option<KeyStoreTypes.HierarchyVersion>,
    config: InternalConfig
  )
    returns (output: Result<KeyStoreTypes.HierarchyVersion, Error>)
  {
    if (hierarchyVersion?.None?) {
      return Success(KeyStoreTypes.HierarchyVersion.v1);
    }
    return Success(hierarchyVersion?.value);
  }


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
                                  case KmsKeyArn(kmsKeyArn) => kmsKeyArn)
             .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    var legacyConfig := KeyStoreOperations.Config(
                          id := "",
                          ddbTableName := None,
                          logicalKeyStoreName := config.logicalKeyStoreName,
                          kmsConfiguration := match kmsArn
                          case KmsKeyArn(kmsKeyArn) => KeyStoreOperations.Types.kmsKeyArn(kmsKeyArn),
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
    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
    :- Need(
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="Only ReEncrypt is supported at this time.")
    );

    var legacyConfig :- LegacyConfig(keyManagerStrat, input.KmsArn, config);

    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} legacyConfig.kmsClient.Modifies < MutationLie();

    var hvInput :- ResolveHierarchyVersionForCreateKey(input.HierarchyVersion, config);
    :- Need(
      hvInput.v1?,
      Types.KeyStoreAdminException(message :="Only hierarchy-version-1 is supported at this time.")
    );

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
        Identifier := value.branchKeyIdentifier,
        // TODO-HV-2-M1: this will need to be properly wired
        HierarchyVersion := hvInput
      ));
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
    assume {:axiom} keyManagerStrat.Modifies < MutationLie();
    assume {:axiom} keyManagerStrat.Modifies !! systemKey.Modifies;

    :- Need(
      keyManagerStrat.SupportHV1(),
      Types.KeyStoreAdminException(message := "At this time, Mutations do not support KeyManagementStrategy#AwsKmsSimple.")
    );

    if (
        && input.Mutations.TerminalHierarchyVersion.Some?
        && input.Mutations.TerminalHierarchyVersion.value.v2?
      ) {
      return Failure(Types.KeyStoreAdminException(message :="At this time, Mutations do not support mutations to hierarchy-version-2."));
    }
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
    assume {:axiom} keyManagerStrat.Modifies < MutationLie();
    assume {:axiom} keyManagerStrat.Modifies !! systemKey.Modifies;

    :- Need(
      keyManagerStrat.SupportHV1(),
      Types.KeyStoreAdminException(message := "At this time, Mutations do not support KeyManagementStrategy#AwsKmsSimple.")
    );
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
