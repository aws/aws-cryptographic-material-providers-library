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
    // import KMS = KeyStoreTypes.ComAmazonawsKmsTypes

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
  function {:opaque} MutationLie(): set<object>
  {{}}

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    config.storage.Modifies + MutationLie()
  }

  method resolveKmsStratgety(
    kmsStratgey?: Option<KeyManagementStrategy>,
    config: InternalConfig
  )
    returns (output: Result<Mutations.keyManagerStrat, Error>)
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
      var kmsClient? := KMS.KMSClient();
      var kmsClient :- kmsClient?
      .MapFailure(e => Types.Error.ComAmazonawsKms(e));
      var kms := KeyStoreTypes.AwsKms(
        grantTokens := None(),
        kmsClient := Some(kmsClient)
      );
      input := KeyManagementStrategy.AwsKmsReEncrypt(kms);
    } else {
      input := kmsStratgey?.value;
    }
    match input {
      case AwsKmsReEncrypt(kms) =>
        var tuple :- kmsInputLies(kms, config);
        return Success(Mutations.keyManagerStrat.reEncrypt(tuple));
      case AwsKmsDecryptEncrypt(kmsDecryptEncrypt) =>
        // var decrypt :- kmsInputLies(kmsDecryptEncrypt.decrypt, config);
        // var encrypt :- kmsInputLies(kmsDecryptEncrypt.encrypt, config);
        // return Success(Mutations.keyManagerStrat.decryptEncrypt(decrypt, encrypt));
        return Failure(Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!"));
    }
  }

  function method {:opaque} kmsInputLies(
    kms: KeyStoreTypes.AwsKms,
    config: InternalConfig
  ): (output: Result<Mutations.KMSTuple, Error>)
    requires ValidInternalConfig?(config)
    // TODO: Support No KMS Client
    ensures output.Success?
            ==>
              && kms.kmsClient.Some?
              && (config.storage.Modifies !! output.value.kmsClient.Modifies)
              && output.value.kmsClient.ValidState()
              && GetValidGrantTokens(Some(output.value.grantTokens)).Success?
  {
    :- Need(
         kms.kmsClient.Some?,
         Types.KeyStoreAdminException(
           message := "KMS Client MUST be set!"
         )
       );
    var grantTokens := GetValidGrantTokens(kms.grantTokens);
    :- Need(
         && grantTokens.Success?,
         Types.KeyStoreAdminException(
           message := "Grant Tokens passed to Key Store Admin are invalid.")
       );
    assume {:axiom} config.storage.Modifies !! kms.kmsClient.value.Modifies;
    assume {:axiom} kms.kmsClient.value.ValidState();
    Success(Mutations.KMSTuple(kms.kmsClient.value, grantTokens.value))
  }

  function method kmsInputsToLegacyConfig(
    keyManagerStrat: Mutations.keyManagerStrat,
    kmsArn: Types.KMSIdentifier,
    config: InternalConfig
  ): (output: Result<KeyStoreOperations.Config, Error>)
    requires ValidInternalConfig?(config)
    // TODO :: Support Decrypt/Encrypt
    requires
      && keyManagerStrat.reEncrypt?
         // && keyManagerStrat.reEncrypt.kmsClient.ValidState()
      && GetValidGrantTokens(Some(keyManagerStrat.reEncrypt.grantTokens)).Success?
    // && (config.storage.Modifies !! keyManagerStrat.reEncrypt.kmsClient.Modifies)
    // ensures output.Success?
    //         ==>
    //           && keyManagerStrat.reEncrypt.kmsClient.ValidState()
    // && (config.storage.Modifies !! keyManagerStrat.reEncrypt.kmsClient.Modifies)
    ensures output.Success? ==> KeyStoreOperations.ValidInternalConfig?(output.value)
  {
    var _ :- KmsArn.IsValidKeyArn(match kmsArn
                                  case kmsKeyArn(kmsKeyArn) => kmsKeyArn
                                  case kmsMRKeyArn(kmsMRKeyArn) => kmsMRKeyArn)
             .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    var legacyConfig := KeyStoreOperations.Config(
                          id := "",
                          ddbTableName := None,
                          logicalKeyStoreName := config.logicalKeyStoreName,
                          kmsConfiguration := match kmsArn
                          case kmsKeyArn(kmsKeyArn) => KeyStoreOperations.Types.kmsKeyArn(kmsKeyArn)
                          case kmsMRKeyArn(kmsMRKeyArn) => KeyStoreOperations.Types.kmsMRKeyArn(kmsMRKeyArn),
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
    // return Failure(Types.KeyStoreAdminException(message := "Implement me"));
    var keyManagerStrat :- resolveKmsStratgety(input.strategy, config);
    :- Need(
      // Remove before Prod
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!")
    );

    var legacyConfig :- kmsInputsToLegacyConfig(keyManagerStrat, input.kmsArn, config);

    assume {:axiom} legacyConfig.kmsClient.Modifies < MutationLie();

    var output? := KeyStoreOperations.CreateKey(
      config := legacyConfig,
      input := KeyStoreOperations.Types.CreateKeyInput(
        branchKeyIdentifier := input.branchKeyIdentifier,
        encryptionContext := input.encryptionContext
      )
    );
    var value :- output?
    .MapFailure(e => Types.AwsCryptographyKeyStore(e));

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := value.branchKeyIdentifier
      ));
  }

  predicate VersionKeyEnsuresPublicly(input: VersionKeyInput, output: Result<VersionKeyOutput, Error>)
  {true}

  method VersionKey(config: InternalConfig, input: VersionKeyInput)
    returns (output: Result<VersionKeyOutput, Error>)
  {

    var keyManagerStrat :- resolveKmsStratgety(input.strategy, config);
    :- Need(
      // Remove before Prod
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!")
    );
    assert
      && keyManagerStrat.reEncrypt?
      && keyManagerStrat.reEncrypt.kmsClient.ValidState()
      && GetValidGrantTokens(Some(keyManagerStrat.reEncrypt.grantTokens)).Success?
      && (config.storage.Modifies !! keyManagerStrat.reEncrypt.kmsClient.Modifies);

    var legacyConfig :- kmsInputsToLegacyConfig(keyManagerStrat, input.kmsArn, config);

    assume {:axiom} legacyConfig.kmsClient.Modifies < MutationLie();

    var output? := KeyStoreOperations.VersionKey(
      config := legacyConfig,
      input := KeyStoreOperations.Types.VersionKeyInput(
        branchKeyIdentifier := input.branchKeyIdentifier
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
    var keyManagerStrat :- resolveKmsStratgety(input.strategy, config);
    :- Need(
      // Remove before Prod
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!")
    );
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
    var keyManagerStrat :- resolveKmsStratgety(input.strategy, config);
    :- Need(
      // Remove before Prod
      keyManagerStrat.reEncrypt?,
      Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!")
    );
    assume {:axiom} keyManagerStrat.reEncrypt.kmsClient.Modifies < MutationLie();

    var _ :- Mutations.ValidateApplyMutationInput(input, config.logicalKeyStoreName, config.storage);
    output := Mutations.ApplyMutation(input, config.logicalKeyStoreName, keyManagerStrat, config.storage);
    return output;
  }

  predicate ResumeMutationEnsuresPublicly(input: ResumeMutationInput , output: Result<ResumeMutationOutput, Error>)
  {true}

  method ResumeMutation ( config: InternalConfig , input: ResumeMutationInput )
    returns (output: Result<ResumeMutationOutput, Error>)
  {
    return Failure(Types.KeyStoreAdminException(message := "Implement me"));
  }
}
