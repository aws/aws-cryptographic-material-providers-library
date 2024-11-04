// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "Mutations.dfy"

module AwsCryptographyKeyStoreAdminOperations refines AbstractAwsCryptographyKeyStoreAdminOperations {
  import opened AwsKmsUtils
  import KmsArn
  import DefaultKeyStorageInterface
  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = KeyStoreOperations.Types
  import KMS = Com.Amazonaws.Kms
  import Mutations

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
    returns (output: Result<Mutations.keyManagerStrat, Error>)
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
        return Success(Mutations.keyManagerStrat.reEncrypt(tuple));
        // TODO-Mutations-FF :
        // case AwsKmsDecryptEncrypt(kmsDecryptEncrypt) =>
        //   // var decrypt :- ResolveKmsInput(kmsDecryptEncrypt.decrypt, config);
        //   // var encrypt :- ResolveKmsInput(kmsDecryptEncrypt.encrypt, config);
        //   // return Success(Mutations.keyManagerStrat.decryptEncrypt(decrypt, encrypt));
        //   return Failure(Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!"));
    }
  }

  method ResolveKmsInput(
    kms: KeyStoreTypes.AwsKms,
    config: InternalConfig
  )
    returns (output: Result<Mutations.KMSTuple, Error>)
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
    output := Success(Mutations.KMSTuple(kmsClient, grantTokens.value));
  }

  function method LegacyConfig(
    keyManagerStrat: Mutations.keyManagerStrat,
    kmsArn: Types.KmsAesIdentifier,
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
    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
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
    :- Need(
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="Only ReEncrypt is supported at this time.")
    );
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} keyManagerStrat.reEncrypt.kmsClient.Modifies < MutationLie();

    var _ :- Mutations.ValidateInitializeMutationInput(input, config.logicalKeyStoreName);
    output := Mutations.InitializeMutation(input, config.logicalKeyStoreName, keyManagerStrat, config.storage);
    return output;
  }

  predicate ApplyMutationEnsuresPublicly(input: ApplyMutationInput, output: Result<ApplyMutationOutput, Error>)
  {true}

  method ApplyMutation(config: InternalConfig, input: ApplyMutationInput)
    returns (output: Result<ApplyMutationOutput, Error>)
  {
    var keyManagerStrat :- ResolveStrategy(input.Strategy, config);
    :- Need(
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="Only ReEncrypt is supported at this time.")
    );
    // See Smithy-Dafny : https://github.com/smithy-lang/smithy-dafny/pull/543
    assume {:axiom} keyManagerStrat.reEncrypt.kmsClient.Modifies < MutationLie();

    var _ :- Mutations.ValidateApplyMutationInput(input, config.logicalKeyStoreName, config.storage);
    output := Mutations.ApplyMutation(input, config.logicalKeyStoreName, keyManagerStrat, config.storage);
    return output;
  }

  // predicate ResumeMutationEnsuresPublicly(input: ResumeMutationInput , output: Result<ResumeMutationOutput, Error>)
  // {true}

  // method ResumeMutation ( config: InternalConfig , input: ResumeMutationInput )
  //   returns (output: Result<ResumeMutationOutput, Error>)
  // {
  //   return Failure(Types.KeyStoreAdminException(message := "Implement me"));
  // }
}
