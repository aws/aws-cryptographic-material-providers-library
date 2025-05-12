// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../AwsCryptographyKeyStore/src/KeyStoreErrorMessages.dfy"
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "MutationErrorRefinement.dfy"
include "../../../dafny/AwsCryptographyKeyStore/src/KmsUtils.dfy"
include "KeyStoreAdminHelpers.dfy"
include "KeyStoreAdminErrorMessages.dfy"

/** Common Functions/Methods for Mutations. */
module {:options "/functionSyntax:4" } Mutations {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import opened UInt = StandardLibrary.UInt

  import KMS = ComAmazonawsKmsTypes
  import AtomicPrimitives

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import KmsArn
  import KMSKeystoreOperations
  import DefaultKeyStorageInterface
  import GetKeys
  import KeyStoreErrorMessages
  import HVUtils = HierarchicalVersionUtils
  import KmsUtils

  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import KeyStoreAdminErrorMessages
  import MutationErrorRefinement
  import KeyStoreAdminHelpers

  const StringToHierarchyVersion := Structure.StringToHierarchyVersion
  const HierarchyVersionToString := Structure.HierarchyVersionToString

  // ActiveVerificationHolder stores the decrypted branch key after verification (KMS decryption for hv1, KMS decryption + SHA validation for hv2)
  // With ActiveVerificationHolder, we can avoid redundant decryption during mutations
  datatype ActiveVerificationHolder =
    | NotDecrypt()
    | KmsDecrypt(kmsRes: KMS.PlaintextType)

  method {:isolate_assertions} VerifyEncryptedHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "ApplyMutation",
    nameonly mutationToApply: StateStrucs.MutationToApply
  )
    returns (output: Result<ActiveVerificationHolder,Types.Error>)

    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires mutationToApply.ValidState()
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, keyManagerStrategy)
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    if (mutationToApply.Terminal.hierarchyVersion.v2?) {
      var res := VerifyEncryptedHierarchicalKeyForHV2(
        item := item,
        keyManagerStrategy := keyManagerStrategy,
        localOperation := localOperation,
        mutationToApply := mutationToApply
      );
      return res;
    } else if (mutationToApply.Terminal.hierarchyVersion.v1?) {
      var res := VerifyEncryptedHierarchicalKeyForHV1(
        item := item,
        keyManagerStrategy := keyManagerStrategy,
        localOperation := localOperation,
        mutationToApply := mutationToApply
      );
      return res;
    } else {
      return Failure(Types.AwsCryptographyKeyStore(
                       KeyStoreTypes.HierarchyVersionException(
                         message := KeyStoreErrorMessages.INVALID_HIERARCHY_VERSION
                       )));
    }
  }

  method VerifyEncryptedHierarchicalKeyForHV1(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string,
    nameonly mutationToApply: StateStrucs.MutationToApply
  )
    returns (output: Result<ActiveVerificationHolder,Types.Error>)

    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires mutationToApply.ValidState()
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, keyManagerStrategy)
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    requires mutationToApply.Terminal.hierarchyVersion.v1?
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var success?: bool := false;
    var throwAwayError;
    if (mutationToApply.Terminal.hierarchyVersion.v2?) {
      // TODO-HV-2-M4: Support other key manager strategy
      :- Need(keyManagerStrategy.kmsSimple? || keyManagerStrategy.decryptEncrypt?, Types.UnsupportedFeatureException(message:=KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_MUTATIONS_HV_2));
      var kmsTupleToDecrypt := getDecryptKMSTuple(keyManagerStrategy);
      var decryptRes := GetKeys.DecryptBranchKeyItem(
        item,
        KeyStoreAdminHelpers.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
        kmsTupleToDecrypt.grantTokens,
        kmsTupleToDecrypt.kmsClient
      );
      if decryptRes.Success? {
        return Success(ActiveVerificationHolder.KmsDecrypt(decryptRes.value));
      }
      if decryptRes.error.ComAmazonawsKms? || decryptRes.error.KeyManagementException? || decryptRes.error.BranchKeyCiphertextException? {
        var error := BuildVerificationError(
          item,
          decryptRes.error,
          localOperation,
          "Decrypt"
        );
        return Failure(error);
      }
      return Failure(Types.AwsCryptographyKeyStore(
                       AwsCryptographyKeyStore := decryptRes.error
                     ));
    }
    var kmsOperation: string;
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        kmsOperation := "ReEncrypt";
        var throwAway? := KMSKeystoreOperations.ReEncryptKey(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := item.EncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );

        if throwAway?.Success? {
          success? := true;
        } else {
          throwAwayError := throwAway?.error;
        }
      case kmsSimple(kms) =>
        kmsOperation := "ReEncrypt";
        var throwAway? := KMSKeystoreOperations.ReEncryptKey(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := item.EncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );

        if throwAway?.Success? {
          success? := true;
        } else {
          throwAwayError := throwAway?.error;
        }
      case decryptEncrypt(kmsD, kmsE) =>
        kmsOperation := "Decrypt/Encrypt";
        var decryptKmsClient;
        var decryptGrantTokens;
        if localOperation == "ApplyMutation" {
          decryptGrantTokens := kmsE.grantTokens;
          decryptKmsClient := kmsE.kmsClient;
        } else if localOperation == "InitializeMutation" {
          decryptGrantTokens := kmsD.grantTokens;
          decryptKmsClient := kmsD.kmsClient;
        } else {
          return Failure(Types.KeyStoreAdminException(
                           message := KeyStoreAdminErrorMessages.UnsupportedLocalOperation(localOperation)
                         ));
        }

        var throwAway? := KMSKeystoreOperations.VerifyViaDecryptEncryptKey(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := item.EncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
          decryptGrantTokens := decryptGrantTokens,
          decryptKmsClient := decryptKmsClient
        );

        if throwAway?.Success? {
          success? := true;
        } else {
          throwAwayError := throwAway?.error;
        }
    }

    if (!success?) {
      var error := BuildVerificationError(
        item,
        throwAwayError,
        localOperation,
        kmsOperation
      );
      return Failure(error);
    }

    assert success?;
    return Success(ActiveVerificationHolder.NotDecrypt());
  }

  method VerifyEncryptedHierarchicalKeyForHV2(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string,
    nameonly mutationToApply: StateStrucs.MutationToApply
  )
    returns (output: Result<ActiveVerificationHolder,Types.Error>)

    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires mutationToApply.ValidState()
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, keyManagerStrategy)
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    requires mutationToApply.Terminal.hierarchyVersion.v2?
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var KMSTuple;
    if localOperation == "ApplyMutation" {
      KMSTuple := KmsUtils.getEncryptKMSTuple(keyManagerStrategy);
    } else if localOperation == "InitializeMutation" {
      KMSTuple := KmsUtils.getDecryptKMSTuple(keyManagerStrategy);
    } else {
      return Failure(Types.KeyStoreAdminException(
                       message := KeyStoreAdminErrorMessages.UnsupportedLocalOperation(localOperation)
                     ));
    }

    var decryptRes := GetKeys.DecryptBranchKeyItem(
      item,
      KeyStoreAdminHelpers.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
      KMSTuple.grantTokens,
      KMSTuple.kmsClient
    );

    if decryptRes.Success? {
      return Success(ActiveVerificationHolder.KmsDecrypt(decryptRes.value));
    }

    if decryptRes.error.ComAmazonawsKms? || decryptRes.error.KeyManagementException? || decryptRes.error.BranchKeyCiphertextException? {
      var error := BuildVerificationError(
        item,
        decryptRes.error,
        localOperation,
        "Decrypt"
      );
      return Failure(error);
    }

    return Failure(Types.AwsCryptographyKeyStore(
                     AwsCryptographyKeyStore := decryptRes.error
                   ));
  }

  // TODO-HV-2-M2: Add precondition  that the ActiveHierarchicalSymmetricVersion Item's have the original context,
  // and the HierarchicalSymmetricVersion have the terminal context.
  method BuildVerificationError(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    throwAwayError: KMSKeystoreOperations.KmsError,
    localOperation: string,
    kmsOperation: string
  ) returns (error: Types.Error)
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
  {
    if item.Type.ActiveHierarchicalSymmetricVersion? {
      error := MutationErrorRefinement.VerifyActiveException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation
      );
      return error;
    }

    if item.Type.HierarchicalSymmetricVersion? {
      error := MutationErrorRefinement.VerifyTerminalException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation
      );
      return error;
    }
  }

  // TODO-HV-2-Mutate-Version: Can be removed in favor of Mutations.ReEncryptHierarchicalKey()
  // or refactor Mutations.ReEncryptHierarchicalKey to use this Method.
  method {:isolate_asserations} NewActiveItemForDecryptEncrypt(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "InitializeMutation"
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires KMS.IsValid_KeyIdType(terminalKmsArn)
    requires KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
    requires KmsArn.ValidKmsArn?(terminalKmsArn)
    requires item.KmsArn == terminalKmsArn
    requires keyManagerStrategy.ValidState()
    requires keyManagerStrategy.decryptEncrypt?
    requires item.Type.HierarchicalSymmetricVersion? // the input is a Version
    requires Structure.ActiveHierarchicalSymmetricVersionEncryptionContext?(terminalEncryptionContext)
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
    ensures output.Success? ==> output.value.Type.ActiveHierarchicalSymmetricVersion? // the output is an ACTIVE
  {
    var wrappedKey?;
    // When using the decrypt encrypt strategy, we created the new DecryptOnly with the encrypt client.
    // If we want to reencrypt it for the new active we must do so with only the encrypt client. This means
    // that the encrypt client will perform both the decrypt and encrypt operations. Otherwise we assume that
    // the decrypt client has permissions to decrypt the kms key that we are moving to. This is a wrong assumption.
    wrappedKey? := KMSKeystoreOperations.MutateViaDecryptEncryptOnInitializeMutation(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := terminalEncryptionContext,
      sourceKmsArn := terminalKmsArn,
      destinationKmsArn := terminalKmsArn,
      grantTokens := keyManagerStrategy.encrypt.grantTokens,
      kmsClient := keyManagerStrategy.encrypt.kmsClient
    );
    // We call this method to create the new Active from the new Decrypt Only
    if (wrappedKey?.Failure?) {
      var error := MutationErrorRefinement.CreateActiveException(
        branchKeyItem := Structure.ConstructEncryptedHierarchicalKey(
          terminalEncryptionContext,
          item.CiphertextBlob),
        error := wrappedKey?.error,
        localOperation := localOperation,
        kmsOperation := "Decrypt/Encrypt");
      return Failure(error);
    }
    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalEncryptionContext,
                        wrappedKey?.value
                      ));
  }

  // TODO: decide if I want to do this or leave the params
  datatype ReEncryptHierarchicalKeyInput = ReEncryptHierarchicalKeyInput(
    nameonly item: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly originalKmsArn: string,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat
  )
  {
    ghost predicate Pre()
    {
      && Structure.EncryptedHierarchicalKeyFromStorage?(item)
      && KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
      && KmsArn.ValidKmsArn?(originalKmsArn) && KmsArn.ValidKmsArn?(terminalKmsArn)
      && item.KmsArn == originalKmsArn
      && keyManagerStrategy.ValidState()
    }
    ghost const Modifies := keyManagerStrategy.ModifiesMultiSet
    ghost predicate Post()
    {
      && keyManagerStrategy.ValidState()
    }
  }

  // Re-encrypts branch key items when Terminal Hierarchy Version is 1.
  // Does not support Terminal Hierarchy Version 2 operations.
  method {:isolate_assertions} ReEncryptHierarchicalKey(
    nameonly input: ReEncryptHierarchicalKeyInput,
    nameonly localOperation: string := "ApplyMutation",
    nameonly createNewActive: bool := false
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires input.Pre()
    ensures input.Post()
    modifies input.Modifies
    requires localOperation == "InitializeMutation" || localOperation == "ApplyMutation"
    requires input.keyManagerStrategy.decryptEncrypt? || input.keyManagerStrategy.reEncrypt? || input.keyManagerStrategy.kmsSimple?
    requires input.item.EncryptionContext[Structure.KMS_FIELD] == input.originalKmsArn
    requires input.terminalEncryptionContext[Structure.KMS_FIELD] == input.terminalKmsArn
  {
    var wrappedKey?;
    var kmsOperation: string;
    match input.keyManagerStrategy {
      case reEncrypt(kms) =>
        kmsOperation := "ReEncrypt";
        wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
          ciphertext := input.item.CiphertextBlob,
          sourceEncryptionContext := input.item.EncryptionContext,
          destinationEncryptionContext := input.terminalEncryptionContext,
          sourceKmsArn := input.originalKmsArn,
          destinationKmsArn := input.terminalKmsArn,
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );
      case kmsSimple(kms) =>
        kmsOperation := "ReEncrypt";
        wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
          ciphertext := input.item.CiphertextBlob,
          sourceEncryptionContext := input.item.EncryptionContext,
          destinationEncryptionContext := input.terminalEncryptionContext,
          sourceKmsArn := input.originalKmsArn,
          destinationKmsArn := input.terminalKmsArn,
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );
      case decryptEncrypt(kmsD, kmsE) =>
        var decryptedKey? := KMSKeystoreOperations.DecryptKeyForHv1(
          encryptedKey := input.item,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(input.originalKmsArn),
          grantTokens := kmsD.grantTokens,
          kmsClient := kmsD.kmsClient);
        if (decryptedKey?.Failure?) {
          var error := MutationErrorRefinement.MutateExceptionParse(
            item := input.item,
            error := decryptedKey?.error,
            terminalKmsArn := input.terminalKmsArn,
            localOperation := localOperation,
            kmsOperation := "Decrypt");
          return Failure(error);
        }
        kmsOperation := "Encrypt";
        wrappedKey? := KMSKeystoreOperations.EncryptKey(
          plaintext := decryptedKey?.value.Plaintext.value,
          encryptionContext := input.terminalEncryptionContext,
          kmsArnToStorage := input.terminalEncryptionContext[Structure.KMS_FIELD],
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(input.terminalKmsArn),
          grantTokens := kmsE.grantTokens,
          kmsClient := kmsE.kmsClient
        );
    }
    assert kmsOperation == "ReEncrypt" || kmsOperation == "Encrypt";
    // We call this method to create the new Active from the new Decrypt Only
    if (wrappedKey?.Failure? && input.item.Type.ActiveHierarchicalSymmetricVersion? && createNewActive) {
      var error := MutationErrorRefinement.CreateActiveException(
        branchKeyItem := input.item,
        error := wrappedKey?.error,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Failure(error);
    }
    if (wrappedKey?.Failure?) {
      var error := MutationErrorRefinement.MutateExceptionParse(
        item := input.item,
        error := wrappedKey?.error,
        terminalKmsArn := input.terminalKmsArn,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Failure(error);
    }
    // TODO-Mutations-DoNotVersion :: ActiveHierarchicalSymmetricVersion will need to be handled

    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        input.terminalEncryptionContext,
                        wrappedKey?.value
                      ));
  }

  lemma FilterIsEmpty?<T>(f: (T ~> bool), xs: seq<T>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    ensures forall i | 0 <= i < |xs| :: f(xs[i]) ==> xs[i] in Seq.Filter(f, xs)
    ensures |Seq.Filter(f, xs)| == 0 ==> forall i | 0 <= i < |xs| :: !f(xs[i])
  {
    reveal Seq.Filter();
  }

  // TODO-HV-2-M2: Refactor to allow HV-2 for Mutations
  /** This function is largely identical to Structure.DecryptOnlyBranchKeyEncryptionContext, **/
  /** except the "custom Encryption Context" has already been prefixed. **/
  function DecryptOnlyBranchKeyEncryptionContextForMutation(
    branchKeyId: string,
    branchKeyVersion: string,
    timestamp: string,
    logicalKeyStoreName: string,
    kmsKeyArn: string,
    hierarchyVersion: KeyStoreTypes.HierarchyVersion,
    prefixedCustomEncryptionContext: map<string, string>
  ): (output: map<string, string>)
    requires 0 < |branchKeyId|
    requires 0 < |branchKeyVersion|
    requires prefixedCustomEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    ensures Structure.BranchKeyContext?(output)
    ensures Structure.BRANCH_KEY_TYPE_PREFIX < output[Structure.TYPE_FIELD]
    ensures Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in output
    ensures output[Structure.KMS_FIELD] == kmsKeyArn
    ensures output[Structure.TABLE_FIELD] == logicalKeyStoreName
    ensures output[Structure.HIERARCHY_VERSION] == HierarchyVersionToString(hierarchyVersion)
    ensures forall k <- prefixedCustomEncryptionContext
              ::
                && k in output
                && output[k] == prefixedCustomEncryptionContext[k]
  {
    map[
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := branchKeyId,
      Structure.TYPE_FIELD := Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion,
      Structure.KEY_CREATE_TIME := timestamp,
      Structure.TABLE_FIELD := logicalKeyStoreName,
      Structure.KMS_FIELD := kmsKeyArn,
      Structure.HIERARCHY_VERSION := HierarchyVersionToString(hierarchyVersion)
    ] + prefixedCustomEncryptionContext
  }

  datatype CheckedItem =
    | itemOriginal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
    | itemTerminal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
      // Never describe itemNeither to customers as such.
      // Always use the `UnExecptedStateException`.
    | itemNeither(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)

  type OriginalOrTerminal = s:seq<CheckedItem>
    | forall i <- s :: !i.itemNeither?
    witness *

  lemma OriginalOrTerminalIsEncryptedHierarchicalKeyFromStorage?(items: OriginalOrTerminal)
    ensures forall item <- items ::
              && (item.itemOriginal? || item.itemTerminal?)
              && item.item is KeyStoreTypes.EncryptedHierarchicalKey
  {}

  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
  ): (output: CheckedItem)
    requires item.Type.HierarchicalSymmetricVersion?
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires MutationToApply.ValidState()
    ensures Structure.EncryptedHierarchicalKeyFromStorage?(output.item)
    ensures
      && output.itemOriginal?
      ==>
        && output.item.KmsArn == MutationToApply.Original.kmsArn
    ensures output.item.Type.HierarchicalSymmetricVersion?
  {
    if item.EncryptionContext
       == Structure.ReplaceMutableContext(
            item.EncryptionContext,
            MutationToApply.Original.kmsArn,
            MutationToApply.Original.customEncryptionContext,
            MutationToApply.Original.hierarchyVersion
          ) then
      itemOriginal(item)
    else if item.EncryptionContext
            == Structure.ReplaceMutableContext(
                 item.EncryptionContext,
                 MutationToApply.Terminal.kmsArn,
                 MutationToApply.Terminal.customEncryptionContext,
                 MutationToApply.Terminal.hierarchyVersion
               ) then
      itemTerminal(item)
    else
      itemNeither(item)
  }

  predicate ValidateItemFromStorage?(
    storage: KeyStoreTypes.IKeyStorageInterface,
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly identifier: string,
    nameonly logicalName: string
  )
  {
    || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
    || (
         && item.Identifier == identifier
         && Structure.TABLE_FIELD in item.EncryptionContext
         && item.EncryptionContext[Structure.TABLE_FIELD] == logicalName
         && KmsArn.ValidKmsArn?(item.KmsArn)
       )
  }

  method MutateItem(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    localOperation: string,
    doNotVersion: bool,
    nameonly aes256Key?: Option<KMS.PlaintextType> := None
  ) returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    modifies keyManagerStrategy.ModifiesMultiSet
    ensures mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    requires item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires localOperation == "InitializeMutation" || localOperation == "ApplyMutation"
    requires aes256Key?.Some? ==> |aes256Key?.value| == Structure.AES_256_LENGTH as int

    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, keyManagerStrategy)
  {
    var mutatedItem: KeyStoreTypes.EncryptedHierarchicalKey;
    if (mutationToApply.Terminal.hierarchyVersion.v1?) {
      :- Need(
        item.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1,
        Types.UnsupportedFeatureException(
          message := KeyStoreAdminErrorMessages.UNSUPPORTED_DOWNGRADE_HV
        )
      );
      mutatedItem :- MutateToHV1(
        item,
        mutationToApply,
        keyManagerStrategy,
        localOperation,
        doNotVersion
      );
    } else if (mutationToApply.Terminal.hierarchyVersion.v2?) {
      mutatedItem :- MutateToHV2(
        item,
        mutationToApply,
        keyManagerStrategy,
        localOperation,
        aes256Key?
      );
    } else {
      return Failure(Types.KeyStoreAdminException(
                       message := KeyStoreErrorMessages.INVALID_HIERARCHY_VERSION
                     ));
    }
    return Success(mutatedItem);
  }

  method MutateToHV1(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    localOperation: string,
    doNotVersion: bool
  ) returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    modifies keyManagerStrategy.ModifiesMultiSet
    ensures mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    requires item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires localOperation == "InitializeMutation" || localOperation == "ApplyMutation"
    requires keyManagerStrategy.SupportHV1()
    requires mutationToApply.Terminal.hierarchyVersion.v1?
    requires HierarchyVersionToString(mutationToApply.Terminal.hierarchyVersion) == Structure.HIERARCHY_VERSION_VALUE_1 == item.EncryptionContext[Structure.HIERARCHY_VERSION]
  {
    var terminalEncryptionContext := Structure.ReplaceMutableContext(
      item.EncryptionContext,
      mutationToApply.Terminal.kmsArn,
      mutationToApply.Terminal.customEncryptionContext,
      mutationToApply.Terminal.hierarchyVersion
    );
    assert KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext);
    var input := ReEncryptHierarchicalKeyInput(
      item := item,
      originalKmsArn := mutationToApply.Original.kmsArn,
      terminalKmsArn := mutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := terminalEncryptionContext,
      keyManagerStrategy := keyManagerStrategy
    );
    var mutatedItem :- ReEncryptHierarchicalKey(
      input := input,
      localOperation := localOperation
    );
    return Success(mutatedItem);
  }

  method MutateToHV2(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    localOperation: string,
    aes256Key?: Option<KMS.PlaintextType>
  ) returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    modifies keyManagerStrategy.ModifiesMultiSet
    ensures mutationToApply.ValidState() && keyManagerStrategy.ValidState()

    requires item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires aes256Key?.Some? ==> |aes256Key?.value| == Structure.AES_256_LENGTH as int
    requires keyManagerStrategy.SupportHV2()
    requires HierarchyVersionToString(mutationToApply.Terminal.hierarchyVersion) == Structure.HIERARCHY_VERSION_VALUE_2
  {
    var decryptKMSTuple := KmsUtils.getDecryptKMSTuple(keyManagerStrategy);
    var encryptKMSTuple := KmsUtils.getEncryptKMSTuple(keyManagerStrategy);
    var terminalBKC := Structure.ReplaceMutableContext(
      item.EncryptionContext,
      mutationToApply.Terminal.kmsArn,
      mutationToApply.Terminal.customEncryptionContext,
      mutationToApply.Terminal.hierarchyVersion
    );
    :- Need(
      HVUtils.HasUniqueTransformedKeys?(terminalBKC),
      Types.KeyStoreAdminException(
        message := KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
      )
    );
    var crypto? := HVUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.KeyStoreAdminException(
        message := "Failed to create internal AtomicPrimitivesClient:" +
        AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error)
      );
      return Failure(e);
    }
    var aes256Key: KMS.PlaintextType;
    if (aes256Key?.Some?) {
      aes256Key := aes256Key?.value;
    } else {
      aes256Key :- decryptOrBuildMutateException(item, localOperation, decryptKMSTuple.grantTokens, decryptKMSTuple.kmsClient);
    }
    var bkcDigest? := HVUtils.CreateBKCDigest(
      terminalBKC,
      crypto?.value
    );
    var bkcDigest :- bkcDigest?.MapFailure(e => Types.AwsCryptographyKeyStore(
                                               AwsCryptographyKeyStore:= e
                                             ));
    var plainTextTuple := HVUtils.PackPlainTextTuple(bkcDigest, aes256Key);
    var encryptRes := KMSKeystoreOperations.EncryptKey(
      plainTextTuple,
      HVUtils.SelectKmsEncryptionContextForHv2(terminalBKC),
      terminalBKC[Structure.KMS_FIELD],
      KeyStoreAdminHelpers.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(terminalBKC[Structure.KMS_FIELD])),
      encryptKMSTuple.grantTokens,
      encryptKMSTuple.kmsClient
    );
    if (encryptRes.Failure?) {
      var error := MutationErrorRefinement.MutateExceptionParse(
        item := item,
        error := encryptRes.error,
        terminalKmsArn := mutationToApply.Terminal.kmsArn,
        localOperation := localOperation,
        kmsOperation := "Encrypt");
      return Failure(error);
    }
    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalBKC,
                        encryptRes.value
                      ));
  }

  method decryptOrBuildMutateException(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    localOperation: string,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  ) returns (output: Result<KMS.PlaintextType, Types.Error>)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires KmsArn.ValidKmsArn?(item.KmsArn)

    ensures output.Success?
            ==>
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && var hv := item.EncryptionContext[Structure.HIERARCHY_VERSION];
              && GetKeys.ValidateKmsDecryption(
                   item,
                   KeyStoreAdminHelpers.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
                   grantTokens,
                   kmsClient,
                   hv)
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;
              && |output.value| == Structure.AES_256_LENGTH as int
              && if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && HVUtils.HasUniqueTransformedKeys?(item.EncryptionContext)
                   && output.value == decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..]
                 else
                   && output.value == decryptResponse.Plaintext.value
  {
    var decryptRes := GetKeys.DecryptBranchKeyItem(
      item,
      KeyStoreAdminHelpers.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
      grantTokens,
      kmsClient
    );
    if decryptRes.Failure? {
      var err := decryptRes.error;
      if err.ComAmazonawsKms? || err.KeyManagementException? || err.BranchKeyCiphertextException? {
        var error := MutationErrorRefinement.MutateExceptionParse(
          item := item,
          error := err,
          terminalKmsArn := Structure.HIERARCHY_VERSION_VALUE_2,
          localOperation := localOperation,
          kmsOperation := "Decrypt");
        return Failure(error);
      } else {
        return Failure(Types.AwsCryptographyKeyStore(
                         AwsCryptographyKeyStore := err
                       ));
      }
    }
    return Success(decryptRes.value);
  }
}
