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

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import KMS = ComAmazonawsKmsTypes
  import KmsArn
  import KMSKeystoreOperations

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

  method {:isolate_assertions} ReEncryptHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly originalKmsArn: string,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "ApplyMutation"
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires KMS.IsValid_KeyIdType(terminalKmsArn)
    requires KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
    requires KmsArn.ValidKmsArn?(originalKmsArn) && KmsArn.ValidKmsArn?(terminalKmsArn)
    requires item.KmsArn == originalKmsArn
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var wrappedKey?;
    var kmsOperation: string;
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        kmsOperation := "ReEncrypt";
        wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := terminalEncryptionContext,
          sourceKmsArn := originalKmsArn,
          destinationKmsArn := terminalKmsArn,
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );
      case decryptEncrypt(kmsD, kmsE) =>
        kmsOperation := "Decrypt/Encrypt";
        wrappedKey? := KMSKeystoreOperations.MutateViaDecryptEncrypt(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := terminalEncryptionContext,
          sourceKmsArn := originalKmsArn,
          destinationKmsArn := terminalKmsArn,
          decryptGrantTokens := kmsD.grantTokens,
          decryptKmsClient := kmsD.kmsClient,
          encryptGrantTokens := kmsE.grantTokens,
          encryptKmsClient := kmsE.kmsClient
        );
    }
    assert kmsOperation == "ReEncrypt" || kmsOperation == "Decrypt/Encrypt";
    // We call this method to create the new Active from the new Decrypt Only
    if (wrappedKey?.Failure? && item.Type.ActiveHierarchicalSymmetricVersion?) {
      var error := MutationErrorRefinement.CreateActiveException(
        branchKeyItem := item,
        error := wrappedKey?.error,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Failure(error);
    }
    // We call this method to mutate decryptOnly and the Becon
    if (
        && wrappedKey?.Failure?
        && (item.Type.HierarchicalSymmetricVersion? || item.Type.ActiveHierarchicalSymmetricBeacon?)) {
      var error := MutationErrorRefinement.MutateExceptionParse(
        item := item,
        error := wrappedKey?.error,
        terminalKmsArn := terminalKmsArn,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Failure(error);
    }
    // TODO-Mutations-DoNotVersion :: ActiveHierarchicalSymmetricVersion will need to be handled

    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalEncryptionContext,
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
}
