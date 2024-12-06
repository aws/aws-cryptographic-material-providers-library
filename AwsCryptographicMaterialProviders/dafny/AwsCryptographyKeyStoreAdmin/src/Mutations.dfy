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

  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import MutationErrorRefinement
  import KmsUtils

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
    nameonly localOperation: string := "ApplyMutation"
  )
    returns (output: Outcome<Types.Error>)

    requires Structure.EncryptedHierarchicalKey?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var kmsOperation: string;
    var success?: bool := false;
    var throwAwayError;

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

    if (
        && !success?
        && item.Type.ActiveHierarchicalSymmetricVersion?
      ) {
      var error := MutationErrorRefinement.VerifyActiveException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Fail(error);
    }

    if (
        && !success?
        && item.Type.HierarchicalSymmetricVersion?
      ) {
      var error := MutationErrorRefinement.VerifyTerminalException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Fail(error);
    }

    assert success?;
    return Pass;
  }

  method {:isolate_asserations} NewActiveItemForDecryptEncrypt(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "InitializeMutation"
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires KMS.IsValid_KeyIdType(terminalKmsArn)
    requires KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
    requires KmsArn.ValidKmsArn?(terminalKmsArn)
    requires item.KmsArn == terminalKmsArn
    requires keyManagerStrategy.ValidState()
    requires keyManagerStrategy.decryptEncrypt?
    requires item.Type.HierarchicalSymmetricVersion? // the input is a Version
    requires Structure.ActiveHierarchicalSymmetricVersionEncryptionContext?(terminalEncryptionContext)
    modifies keyManagerStrategy.encrypt.Modifies
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
      && Structure.EncryptedHierarchicalKey?(item)
      && KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
      && KmsArn.ValidKmsArn?(originalKmsArn) && KmsArn.ValidKmsArn?(terminalKmsArn)
      && item.KmsArn == originalKmsArn
      && keyManagerStrategy.ValidState()
    }
    // TODO-Mutations-FF : Refactor KmsUtils.KeyMang Modifies to be like below and replace all copies
    ghost const Modifies :=
      match keyManagerStrategy {
        case reEncrypt(km) => multiset(km.kmsClient.Modifies)
        case decryptEncrypt(kmD, kmE) => multiset(kmD.kmsClient.Modifies) + multiset(kmE.kmsClient.Modifies)
      }
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
        kmsOperation := "Decrypt/Encrypt";
        wrappedKey? := KMSKeystoreOperations.MutateViaDecryptEncrypt(
          ciphertext := input.item.CiphertextBlob,
          sourceEncryptionContext := input.item.EncryptionContext,
          destinationEncryptionContext := input.terminalEncryptionContext,
          sourceKmsArn := input.originalKmsArn,
          destinationKmsArn := input.terminalKmsArn,
          decryptGrantTokens := kmsD.grantTokens,
          decryptKmsClient := kmsD.kmsClient,
          encryptGrantTokens := kmsE.grantTokens,
          encryptKmsClient := kmsE.kmsClient
        );
    }
    assert kmsOperation == "ReEncrypt" || kmsOperation == "Decrypt/Encrypt";
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

  /** This function is largely identical to Structure.DecryptOnlyBranchKeyEncryptionContext, **/
  /** except the "custom Encryption Context" has already been prefixed. **/
  function DecryptOnlyBranchKeyEncryptionContextForMutation(
    branchKeyId: string,
    branchKeyVersion: string,
    timestamp: string,
    logicalKeyStoreName: string,
    kmsKeyArn: string,
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

  lemma OriginalOrTerminalIsEncryptedHierarchicalKey?(items: OriginalOrTerminal)
    ensures forall item <- items ::
              && (item.itemOriginal? || item.itemTerminal?)
              && item.item is KeyStoreTypes.EncryptedHierarchicalKey
  {}

  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
  ): (output: CheckedItem)
    requires item.Type.HierarchicalSymmetricVersion?
    requires Structure.EncryptedHierarchicalKey?(item)
    requires MutationToApply.ValidState()
    ensures Structure.EncryptedHierarchicalKey?(output.item)
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
    doNotVersion: bool
  ) returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    modifies match keyManagerStrategy {
               case reEncrypt(km) => multiset(km.kmsClient.Modifies)
               case decryptEncrypt(kmD, kmE) => multiset(kmD.kmsClient.Modifies) + multiset(kmE.kmsClient.Modifies)
             }
    ensures mutationToApply.ValidState() && keyManagerStrategy.ValidState()
    requires item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.EncryptedHierarchicalKey?(item)
    requires localOperation == "InitializeMutation" || localOperation == "ApplyMutation"
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
}
