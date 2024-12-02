// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "PrefixUtils.dfy"
include "KmsUtils.dfy"
include "MutationIndexUtils.dfy"
include "SystemKey/Handler.dfy"
include "Mutations.dfy"

module {:options "/functionSyntax:4" } InternalInitializeMutation {
  // StandardLibrary Imports
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import Time
  import UUID
  import UTF8
    // KMS & MPL Imports
  import KMS = ComAmazonawsKmsTypes
  import AwsKmsUtils
    // KeyStore Imports
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import DefaultKeyStorageInterface
  import KmsArn
  import KMSKeystoreOperations
    // KeyStoreAdmin Imports
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KmsUtils
  import StateStrucs = MutationStateStructures
  import PrefixUtils
  import MutationIndexUtils
  import SystemKeyHandler = SystemKey.Handler
  import Mutations

  datatype InternalInitializeMutationInput = | InternalInitializeMutationInput (
    nameonly Identifier: string ,
    nameonly Mutations: Types.Mutations ,
    nameonly SystemKey: KmsUtils.InternalSystemKey ,
    nameonly DoNotVersion: bool,
    nameonly logicalKeyStoreName: string,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
  {
    ghost predicate ValidState()
    {
      && SystemKey.ValidState()
      && keyManagerStrategy.ValidState()
      && storage.ValidState()
      && SystemKey.Modifies !! keyManagerStrategy.Modifies !! storage.Modifies
    }
  }

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function {:isolate_assertions} ValidateInitializeMutationInput(
    input: InternalInitializeMutationInput
  ): (output: Result<InternalInitializeMutationInput, Types.Error>)
    ensures
      output.Success?
      ==>
        && StateStrucs.ValidMutations?(input.Mutations)
    ensures
      && output.Success?
      && input.Mutations.TerminalKmsArn.Some?
      ==>
        && KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)
    ensures
      && output.Success?
      ==>
        input.DoNotVersion == false
  {
    :- Need(
         input.DoNotVersion == false,
         Types.UnsupportedFeatureException(message := "At this time, DoNotVersion MUST be false.")
       );
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));
    var terminalEC := input.Mutations.TerminalEncryptionContext.UnwrapOr(map[]);
    :- Need(
         terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
         Types.KeyStoreAdminException(
           message := "The terminal encryption context provided includes a key that is reserved for Crypto Tools library."));

    // Dafny struggles with Map operations; but Dafny will filter the keys of a map by a condition.
    // Thus, to ensure that there are no keys in the input that are already prefixed,
    // we count the number of keys that are NOT prefixed,
    // and assert that the number of keys that are NOT prefixed
    // is equal to the total number of keys.
    var filterByPrefix := PrefixUtils.FilterMapForKeysThatDoNotBeginWithPrefix(
                            prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
                            aMap := terminalEC);
    :- Need(
         |filterByPrefix| == |terminalEC|,
         Types.KeyStoreAdminException(
           message :=
             "The terminal encryption context provided includes one or more keys that start with `"
             + Structure.ENCRYPTION_CONTEXT_PREFIX + "`."
             + " The Key Store will always add this prefix to provided encryption context."
             + " To avoid unintended double prefixing,"
             + " the Key Store forbids custom Encryption Context keys from starting with this prefix."
             + " Ensure the encryption context provided does not include these values."));

    :- Need(
         && (input.Mutations.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)),
         Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
       );
    :- Need(StateStrucs.ValidMutations?(input.Mutations),
            Types.KeyStoreAdminException(
              message := "Mutations parameter is invalid; If Encryption Context is given, it cannot be empty or have empty values."));
    Success(input)
  }

  method {:isolate_assertions} InitializeMutation(
    input: InternalInitializeMutationInput
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires ValidateInitializeMutationInput(input).Success?
    requires StateStrucs.ValidMutations?(input.Mutations) // may not need this
    requires
      && input.storage.ValidState()
      && match input.keyManagerStrategy {
           case reEncrypt(km) => km.kmsClient.ValidState() && AwsKmsUtils.GetValidGrantTokens(Some(km.grantTokens)).Success?
           case decryptEncrypt(kmD, kmE) =>
             && kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
             && AwsKmsUtils.GetValidGrantTokens(Some(kmD.grantTokens)).Success?
             && AwsKmsUtils.GetValidGrantTokens(Some(kmE.grantTokens)).Success?
         }
      && input.SystemKey.ValidState()
      && input.ValidState()
    ensures
      && input.storage.ValidState()
      && input.SystemKey.ValidState()
      &&
         match input.keyManagerStrategy {
           case reEncrypt(km) => km.kmsClient.ValidState()
           case decryptEncrypt(kmD, kmE) => kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
         }
      && input.ValidState()
    modifies
      input.storage.Modifies,
             match input.keyManagerStrategy {
               case reEncrypt(km) => km.kmsClient.Modifies
               case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
             },
             input.SystemKey.Modifies
  {
    var resumeMutation? := false;

    // Fetch Active Branch Key & Beacon Key & Mutation Lock
    var readItems? := input.storage.GetItemsForInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.GetItemsForInitializeMutationInput(Identifier := input.Identifier));
    var readItems :- readItems?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    if (readItems.MutationCommitment.None? && readItems.MutationIndex.Some?) {
      var indexUUID := readItems.MutationIndex.value.UUID;
      return Failure(
          Types.MutationInvalidException(
            message := "Found a Mutation Index but no Mutation Commitment."
            + " The Key Store's Storage, for this Branch Key, has become corrupted."
            + " Recommend auditing the Branch Key's items for tampering."
            + " Recommend auditing access to the storage."
            + " To successfully start a new mutation, delete the Mutation Index."
            + " But know that the new mutation will fail if any corrupt items are encountered."
            + "\nBranch Key ID: " + input.Identifier + ";"
            + " Mutation Index UUID: " + indexUUID));
    }

    if (readItems.MutationCommitment.Some?) {
      resumeMutation? :- CommitmentAndInputMatch(
        internalInput := input,
        commitment := readItems.MutationCommitment.value);
      if (resumeMutation?) {
        // TODO-SystemKey :: ResumeMutation will validate SystemKey
        output := ResumeMutation(
          commitment := readItems.MutationCommitment.value,
          index := readItems.MutationIndex,
          logicalKeyStoreName := input.logicalKeyStoreName,
          storage := input.storage, // );//,
          SystemKey := input.SystemKey);
        return output;
      }
      return Failure(
          Types.MutationConflictException(
            message :=
              "A Mutation is already in-flight!"
              + " The in-flight Mutation was created with a different Input."
              + " Complete the in-flight before starting a new one. "
              + " If you need to resume the in-flight Mutation,"
              + " provide identical input to InitializeMutation."
              + " DescribeMutation can be used to retrieve the verbatim input."
              + " MutationCommitment UUID: " + readItems.MutationCommitment.value.UUID
              + " CreatedOn: " + readItems.MutationCommitment.value.CreateTime
              + " BranchKeyID: " + input.Identifier
          ));
    }

    var activeItem := readItems.ActiveItem;

    :- Need(
      || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.ActiveItem.Identifier == input.Identifier
           && Structure.ActiveHierarchicalSymmetricKey?(readItems.ActiveItem)
           && readItems.ActiveItem.EncryptionContext[Structure.TABLE_FIELD] == input.logicalKeyStoreName
           && KmsArn.ValidKmsArn?(activeItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Active Branch Key Item read from storage is malformed!")
    );

    :- Need(
      || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.BeaconItem.Identifier == input.Identifier
           && Structure.ActiveHierarchicalSymmetricBeaconKey?(readItems.BeaconItem)
           && readItems.BeaconItem.EncryptionContext[Structure.TABLE_FIELD] == input.logicalKeyStoreName
           && KmsArn.ValidKmsArn?(readItems.BeaconItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Beacon Branch Key Item read from storage is malformed!")
    );

      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
    :- Need(
      && (input.Mutations.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)),
      Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
    );

    // timestamp is for the new Active & Decrypt Only AND for the Mutation Commitment
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate a timestamp: " + e));

    var mutationCommitmentUUID? := UUID.GenerateUUID();
    var mutationCommitmentUUID :- mutationCommitmentUUID?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for Mutation Commitment. " + e));

    var inferredOriginalEC
      := map k <- activeItem.EncryptionContext
                  // This pull everything that is not in our restricted list.
             | k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
      :: k := activeItem.EncryptionContext[k];

    // To Preserve Unexpected/un-modeled Attributes.
    // We need to copy them from inferredOriginalEC to terminalEC.
    // Which means we need to select those members without a prefix,
    // and copy them over to terminal.
    var unexpectedEC := PrefixUtils.FilterMapForKeysThatDoNotBeginWithPrefix(
      prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
      aMap := inferredOriginalEC
    );
    assert unexpectedEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;

    var terminalEC?: Option<KeyStoreTypes.EncryptionContextString> := None;
    if (input.Mutations.TerminalEncryptionContext.Some?) {

      var terminalEC := PrefixUtils.AddingPrefixToKeysOfMapDoesNotCreateCollisions(
        prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
        aMap := input.Mutations.TerminalEncryptionContext.value
      ) + unexpectedEC;
      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
      // TODO-Mutations-FF : Replace runtime check with Lemma.
      // See https://github.com/aws/aws-cryptographic-material-providers-library/pull/750#discussion_r1777654751
      :- Need(
        terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
        Types.KeyStoreAdminException(message:="Terminal Encryption Context contains a reserved word!")
      );
      terminalEC? := Some(terminalEC);
      assert terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    }

    assert KmsArn.ValidKmsArn?(activeItem.KmsArn);
    var MutationToApply := StateStrucs.MutationToApply(
      Identifier := input.Identifier,
      Original := StateStrucs.MutableProperties(
        kmsArn := activeItem.KmsArn,
        customEncryptionContext := inferredOriginalEC
      ),
      Terminal := StateStrucs.MutableProperties(
        kmsArn := input.Mutations.TerminalKmsArn.UnwrapOr(activeItem.KmsArn),
        customEncryptionContext := terminalEC?.UnwrapOr(inferredOriginalEC)
      ),
      ExclusiveStartKey := None,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp,
      Input := input.Mutations,
      CommitmentCiphertext := [0], // TODO-Mutations-GA Create Commitment Ciphertext
      IndexCiphertext := [0] // TODO-Mutations-GA Create Index Ciphertext
    );

    assert MutationToApply.Original.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.Terminal.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.ValidState();
    // -= BEGIN Version Active Branch Key
    // --= Validate Active Branch Key
    var verifyActive? := Mutations.VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );
    if (verifyActive?.Fail?) {
      return Failure(verifyActive?.error);
    }

      // -= Assert Beacon Key is in Original
    :- Need(
      readItems.BeaconItem.KmsArn == MutationToApply.Original.kmsArn,
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not encrypted with the same KMS Key as ACTIVE!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST have the same KMS-ARN and Custom Encryption Context!"
      ));
    :- Need(
      readItems.BeaconItem.EncryptionContext
      ==
      Structure.ReplaceMutableContext(
        readItems.BeaconItem.EncryptionContext,
        readItems.BeaconItem.KmsArn,
        MutationToApply.Original.customEncryptionContext),
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not in the Original State!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST be in the original state."
      ));

    // --= Generate New Decrypt Only Branch Key with terminal properties
    var maybeNewVersion := UUID.GenerateUUID();
    var newVersion :- maybeNewVersion
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for new Decrypt Only. " + e));


    var decryptOnlyEncryptionContext := Mutations.DecryptOnlyBranchKeyEncryptionContextForMutation(
      input.Identifier,
      newVersion,
      timestamp,
      input.logicalKeyStoreName,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    // TODO-Mutations-GA? :: If the KMS Call fails with access denied,
    // it indicates that the MPL Consumer does not have access to
    // GenerateDataKeyWithoutPlaintext on the terminal key.
    var newDecryptOnly :- CreateNewTerminalDecryptOnlyBranchKey(
      decryptOnlyEncryptionContext,
      MutationToApply,
      input.keyManagerStrategy
    );

    var ActiveEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(newDecryptOnly.EncryptionContext);

    var newActive :- Mutations.ReEncryptHierarchicalKey(
      item := newDecryptOnly,
      originalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := ActiveEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );

    // -= Mutate Beacon Key
    var BeaconEncryptionContext := Structure.ReplaceMutableContext(
      readItems.BeaconItem.EncryptionContext,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    assert readItems.BeaconItem.KmsArn == MutationToApply.Original.kmsArn;

    var newBeaconKey :- Mutations.ReEncryptHierarchicalKey(
      item := readItems.BeaconItem,
      originalKmsArn := MutationToApply.Original.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := BeaconEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );

    // -= Create Mutation Commitment & Mutation Index
    var MutationCommitment :- StateStrucs.SerializeMutationCommitment(MutationToApply);
    var MutationIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, None);

    // -= Apply System Key to Commitment & Mutation Index
    var SignedMutationCommitment :- SystemKeyHandler.SignCommitment(MutationCommitment, input.SystemKey);
    var SignedMutationIndex :- SystemKeyHandler.SignIndex(MutationIndex, input.SystemKey);

    // -= Write Mutation Commitment, new branch key version, mutated beacon key
    var throwAway2? := input.storage.WriteInitializeMutation(
      KeyStoreTypes.WriteInitializeMutationInput(
        Active := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newActive, Old:=activeItem),
        Version := KeyStoreTypes.WriteInitializeMutationVersion.rotate(rotate:=newDecryptOnly),
        Beacon := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newBeaconKey, Old:=readItems.BeaconItem),
        MutationCommitment :=  SignedMutationCommitment, // MutationCommitment,
        MutationIndex := SignedMutationIndex // MutationIndex
      ));
    // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Commitment get written?
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var mutatedBranchKeyItems := GetMutatedBranchKeyItems(mutationCommitmentUUID, newVersion);

    var Token := Types.MutationToken(
      Identifier := input.Identifier,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp);

    var Flag: Types.InitializeMutationFlag := Types.Created();

    return Success(Types.InitializeMutationOutput(
                     MutationToken := Token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));
  }

  function GetMutatedBranchKeyItems(mutationCommitmentUUID: seq<char>, newVersion: seq<char>)
    : (output: seq<Types.MutatedBranchKeyItem>)
  {
    [Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + mutationCommitmentUUID, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + mutationCommitmentUUID, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Active: " + newVersion, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Decrypt Only: " + newVersion, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Beacon", Description := "Mutated")
    ]
  }

  method {:isolate_assertions} CreateNewTerminalDecryptOnlyBranchKey(
    decryptOnlyEncryptionContext: Structure.BranchKeyContext,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat
  )
    returns (res: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires KmsArn.ValidKmsArn?(mutationToApply.Terminal.kmsArn)
    requires KMSKeystoreOperations.AttemptKmsOperation?(
               KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn), decryptOnlyEncryptionContext
             )
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(kms) => kms.kmsClient.Modifies
      case decryptEncrypt(kmsD, kmsE) => kmsD.kmsClient.Modifies + kmsE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
    ensures res.Success? ==>
              && Structure.BranchKeyContext?(res.value.EncryptionContext)
              && Structure.EncryptedHierarchicalKey?(res.value)
              && res.value.KmsArn == KMSKeystoreOperations.GetKeyId(KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn))
              && Structure.BRANCH_KEY_TYPE_PREFIX < res.value.EncryptionContext[Structure.TYPE_FIELD]
              && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext
  {
    var grantTokens: KMS.GrantTokenList;
    var kmsClient: KMS.IKMSClient;
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        grantTokens := kms.grantTokens;
        kmsClient := kms.kmsClient;
      case decryptEncrypt(kmsD, kmsE) =>
        grantTokens := kmsE.grantTokens;
        kmsClient := kmsE.kmsClient;
    }

    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
      encryptionContext := decryptOnlyEncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn),
      grantTokens := grantTokens,
      kmsClient := kmsClient
    );
    var wrappedDecryptOnlyBranchKey :- wrappedDecryptOnlyBranchKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var newDecryptOnly := Structure.ConstructEncryptedHierarchicalKey(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );

    :- Need(
      Structure.BRANCH_KEY_TYPE_PREFIX < newDecryptOnly.EncryptionContext[Structure.TYPE_FIELD],
      Types.KeyStoreAdminException(message := "Invalid Branch Key prefix.")
    );

    return Success(newDecryptOnly);
  }

  function CommitmentAndInputMatch(
    nameonly internalInput: InternalInitializeMutationInput,
    nameonly commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<bool, Types.Error>)
  {
    var readMutations :- StateStrucs.DeserializeMutationInput(commitment);
    var givenMutations := internalInput.Mutations;
    Success(readMutations == givenMutations)
  }


  method {:isolate_assertions} ResumeMutation(
    nameonly commitment: KeyStoreTypes.MutationCommitment,
    nameonly index: Option<KeyStoreTypes.MutationIndex>,
    nameonly logicalKeyStoreName: string,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface,
    nameonly SystemKey: KmsUtils.InternalSystemKey
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires storage.ValidState() && SystemKey.ValidState()
    ensures storage.ValidState() && SystemKey.ValidState()
    modifies storage.Modifies, SystemKey.Modifies
    ensures
      output.Success? && index.Some?
      ==>
        index.value.UUID == commitment.UUID
  {
    var mutatedBranchKeyItems := [
      Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + commitment.UUID, Description := "Matched Input")
    ];
    var Flag: Types.InitializeMutationFlag := Types.Resumed();
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Original),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Original is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Terminal),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Terminal is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Input),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Input is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && 0 < |commitment.Identifier|,
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Identifier cannot be empty."));
    :- Need(
      && 0 < |commitment.UUID|,
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's UUID cannot be empty."));
    var commitmentIsVerified :- SystemKeyHandler.VerifyCommitment(commitment, SystemKey);
    :- Need(
      commitmentIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Commitment's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));
    var Token := Types.MutationToken(
      Identifier := commitment.Identifier,
      UUID := commitment.UUID,
      CreateTime := commitment.CreateTime);

    if (index.None?) {
      Flag := Types.ResumedWithoutIndex();
      var timestamp? := Time.GetCurrentTimeStamp();
      var timestamp :- timestamp?
      .MapFailure(e => Types.KeyStoreAdminException(
                      message := "Could not generate a timestamp: " + e));
      var newIndex := KeyStoreTypes.MutationIndex(
        Identifier := commitment.Identifier,
        PageIndex := MutationIndexUtils.ExclusiveStartKeyToPageIndex(None),
        UUID := commitment.UUID,
        CreateTime := timestamp,
        CiphertextBlob := [0] // [0] is a temporary place holder, but we should fix this by creating an internal type
      );
      var SignedMutationIndex :- SystemKeyHandler.SignIndex(newIndex, SystemKey);
      // -= Write Mutation Index, conditioned on Mutation Commitment
      var throwAway2? := storage.WriteMutationIndex(
        KeyStoreTypes.WriteMutationIndexInput(
          MutationCommitment := commitment,
          MutationIndex := SignedMutationIndex
        ));
      // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
      // What Condition Check failed?
      var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
      mutatedBranchKeyItems := mutatedBranchKeyItems
      + [Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + commitment.UUID, Description := "Created")];
    } else {
      var commitmentAndIndex :- Mutations.ValidateCommitmentAndIndexStructures(
        Token,
        commitment,
        index.value);
      var indexIsVerified :- SystemKeyHandler.VerifyIndex(commitmentAndIndex.Index, SystemKey);
      :- Need(
        indexIsVerified,
        Types.MutationVerificationException(
          message:=
            "Mutation Index's failed the System Key's Signature Verification."
            + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
            + " Mutation cannot continue. Audit Key Store's Storage's access."
            + " The Mutation will need to be manually restarted."));
    }

    return Success(Types.InitializeMutationOutput(
                     MutationToken := Token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));

  }
}
