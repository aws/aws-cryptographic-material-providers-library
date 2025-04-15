// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "MutationErrorRefinement.dfy"
include "KmsUtils.dfy"

/** Common Functions/Methods for Mutations. */
module {:options "/functionSyntax:4" } Mutations {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import KMS = ComAmazonawsKmsTypes

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import KmsArn
  import KMSKeystoreOperations
  import DefaultKeyStorageInterface
  import AtomicPrimitives
  import GetKeys

  import ErrorMessages = KeyStoreErrorMessages
  import HvUtils = HierarchicalVersionUtils
  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import MutationErrorRefinement
  import KmsUtils

  datatype ActiveVerificationHolder =
    | NotDecrypt()
    | KmsDecrypt(kmsRes: KMS.PlaintextType)

  method ValidateCommitmentAndIndexStructures(
    token: Types.MutationToken,
    commitment: KeyStoreTypes.MutationCommitment,
    index: KeyStoreTypes.MutationIndex
  )
    returns (output: Result<StateStrucs.CommitmentAndIndex, Types.Error>)
    ensures
      output.Success? ==>
        && commitment.Identifier == index.Identifier == token.Identifier
        && commitment.UUID == index.UUID == token.UUID
    ensures
      && output.Success?
      ==>
        && output.value.ValidState()
        && output.value.ValidUTF8()

  {
    if (commitment.Identifier != index.Identifier || token.Identifier != index.Identifier) {
      return
        Failure(Types.MutationInvalidException(
                  message := "The Token and the Mutation Commitment read from storage disagree."
                  + " This indicates that the Token is for a different Mutation than the one in-flight."
                  + " A possible cause is this token is from an earlier Mutation that already finished?"
                  + " Branch Key ID: " + token.Identifier + ";"
                  + " Mutation Commitment UUID: " + commitment.UUID + ";"
                  + " Token UUID: " + token.UUID + ";"
                ));
    }
    if (commitment.UUID != index.UUID || token.UUID != index.UUID) {
      return
        Failure(Types.MutationInvalidException(
                  message := "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
                  + " Branch Key ID: " + token.Identifier + ";"
                  + " Mutation Commitment UUID: " + commitment.UUID + ";"
                  + " Mutation Index UUID: " + index.UUID + ";"
                ));
    }
    var commitmentAndIndex := StateStrucs.CommitmentAndIndex(commitment, index);
    if (!commitmentAndIndex.ValidUTF8()) {
      return Failure(
          Types.MutationInvalidException(
            message :=
              "The Mutation Commitment and Mutation Index read from storage do not contain valid UTF8 sequences."
              + " Branch Key ID: " + token.Identifier + ";"
              + " Mutation Commitment UUID: " + commitment.UUID + ";"));
    }
    return Success(commitmentAndIndex);
  }

  method {:isolate_assertions} VerifyEncryptedHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "ApplyMutation",
    nameonly isTerminalHv2?: bool := false
  )
    returns (output: Result<ActiveVerificationHolder,Types.Error>)

    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires keyManagerStrategy.SupportHV1()
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
  {

    var success?: bool := false;
    var throwAwayError;
    // TODO-HV-2-M3: Support mutations on HV-2 item (mutation starting with hv-2 item)
    :- Need(
      item.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1,
      Types.KeyStoreAdminException(
        message := "At this time, Mutations ONLY support HV-1; BK's Active Item is HV-2.")
    );
    if (isTerminalHv2?) {
      // TODO-HV-2-M2: Add test to cover the if condition of this code path
      // TODO-HV-2-M4: Support other key manager strategy
      :- Need(keyManagerStrategy.kmsSimple?, Types.KeyStoreAdminException(message:="only KMS Simple allow when mutating to hv-2."));
      var decryptRes := GetKeys.DecryptBranchKeyItem(
        item,
        KmsUtils.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
        keyManagerStrategy.kmsSimple.grantTokens,
        keyManagerStrategy.kmsSimple.kmsClient
      );
      if decryptRes.Success? {
        return Success(ActiveVerificationHolder.KmsDecrypt(decryptRes.value));
      } else {
        var error := BuildErrorForFailure(
          item,
          decryptRes.error,
          localOperation,
          "Decrypt"
        );
        return Failure(error);
      }
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

      case decryptEncrypt(kmsD, kmsE) =>
        kmsOperation := "Decrypt/Encrypt";
        var decryptKmsClient;
        var decryptGrantTokens;
        if localOperation == "ApplyMutation" {
          decryptGrantTokens := kmsE.grantTokens;
          decryptKmsClient := kmsE.kmsClient;
        } else {
          decryptGrantTokens := kmsD.grantTokens;
          decryptKmsClient := kmsD.kmsClient;
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
      var error := BuildErrorForFailure(
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

  method BuildErrorForFailure(
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

    assert false;
  }

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
    requires input.keyManagerStrategy.decryptEncrypt? || input.keyManagerStrategy.reEncrypt?
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
    // hierachyVersion: HierarchyVersion,
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
      Structure.HIERARCHY_VERSION := Structure.HIERARCHY_VERSION_VALUE
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
            MutationToApply.Original.customEncryptionContext
          ) then
      itemOriginal(item)
    else if item.EncryptionContext
            == Structure.ReplaceMutableContext(
                 item.EncryptionContext,
                 MutationToApply.Terminal.kmsArn,
                 MutationToApply.Terminal.customEncryptionContext
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

    requires mutationToApply.Terminal.hierarchyVersion.v1? ==> keyManagerStrategy.SupportHV1()
    requires mutationToApply.Terminal.hierarchyVersion.v2? ==> keyManagerStrategy.SupportHV2()
  {
    var mutatedItem: KeyStoreTypes.EncryptedHierarchicalKey;
    if (mutationToApply.Terminal.hierarchyVersion.v1?) {
      // TODO-HV-2-M2: Wire up MutateToHV2 once hierarchyVersion is added to MutableProperties
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
                       message := ErrorMessages.INVALID_HIERARCHY_VERSION
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
  {
    var terminalEncryptionContext := Structure.ReplaceMutableContext(
      item.EncryptionContext,
      mutationToApply.Terminal.kmsArn,
      mutationToApply.Terminal.customEncryptionContext
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
  {
    :- Need(
      keyManagerStrategy.kmsSimple?,
      Types.KeyStoreAdminException(message :="Only KMS Simple is supported at this time for HV-2 to Create Keys")
    );
    var terminalBKC := Structure.ReplaceMutableContext(
      item.EncryptionContext,
      mutationToApply.Terminal.kmsArn,
      mutationToApply.Terminal.customEncryptionContext
    );
    :- Need(
      HvUtils.HasUniqueTransformedKeys?(terminalBKC),
      Types.KeyStoreAdminException(
        message := ErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
      )
    );
    var crypto? := HvUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.KeyStoreAdminException(
        message := "Local Cryptography error: " +
        AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error)
      );
      return Failure(e);
    }
    var aes256Key: KMS.PlaintextType;
    if (aes256Key?.Some?) {
      aes256Key := aes256Key?.value;
    } else {
      aes256Key :- decryptOrBuildMutateException(item, keyManagerStrategy, localOperation);
    }
    var bkcDigest? := HvUtils.CreateBKCDigest(
      terminalBKC,
      crypto?.value
    );
    var bkcDigest :- bkcDigest?.MapFailure(e => Types.AwsCryptographyKeyStore(
                                               AwsCryptographyKeyStore:= e
                                             ));
    var plainTextTuple := HvUtils.PackPlainTextTuple(bkcDigest, aes256Key);
    var encryptRes :- expect KMSKeystoreOperations.EncryptKey(
      plainTextTuple,
      HvUtils.SelectKmsEncryptionContextForHv2(terminalBKC),
      item.EncryptionContext[Structure.KMS_FIELD],
      KmsUtils.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
      keyManagerStrategy.kmsSimple.grantTokens,
      keyManagerStrategy.kmsSimple.kmsClient
    );
    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalBKC,
                        encryptRes
                      ));
  }

  method decryptOrBuildMutateException(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    localOperation: string
  ) returns (output: Result<KMS.PlaintextType, Types.Error>)
    requires keyManagerStrategy.ValidState()
    modifies keyManagerStrategy.ModifiesMultiSet
    ensures keyManagerStrategy.ValidState()

    requires Structure.EncryptedHierarchicalKeyFromStorage?(item)
    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
    requires KmsArn.ValidKmsArn?(item.KmsArn)

    requires keyManagerStrategy.kmsSimple?

    ensures output.Success?
            ==>
              && |keyManagerStrategy.kmsSimple.kmsClient.History.Decrypt| == |old(keyManagerStrategy.kmsSimple.kmsClient.History.Decrypt)| + 1
              && var hv := item.EncryptionContext[Structure.HIERARCHY_VERSION];
              && GetKeys.ValidateKmsDecryption(
                   item,
                   KmsUtils.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
                   keyManagerStrategy.kmsSimple.grantTokens,
                   keyManagerStrategy.kmsSimple.kmsClient,
                   hv)
              && var decryptResponse := Seq.Last(keyManagerStrategy.kmsSimple.kmsClient.History.Decrypt).output.value;
              && |output.value| == Structure.AES_256_LENGTH as int
              && if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && HvUtils.HasUniqueTransformedKeys?(item.EncryptionContext)
                   && output.value == decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..]
                 else
                   && output.value == decryptResponse.Plaintext.value
  {
    var decryptRes := GetKeys.DecryptBranchKeyItem(
      item,
      KmsUtils.KmsSymmetricKeyArnToKMSConfiguration(Types.KmsSymmetricKeyArn.KmsKeyArn(item.KmsArn)),
      keyManagerStrategy.kmsSimple.grantTokens,
      keyManagerStrategy.kmsSimple.kmsClient
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
