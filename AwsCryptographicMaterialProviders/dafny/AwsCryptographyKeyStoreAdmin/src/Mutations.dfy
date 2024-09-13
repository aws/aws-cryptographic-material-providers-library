// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"

module {:options "/functionSyntax:4" } Mutations {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq

  import Structure
  import DefaultEncryptedKeyStore
  import ErrorMessages = KeyStoreErrorMessages

  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import KmsArn
  import KMSKeystoreOperations

  import StateStrucs = MutationStateStructures
  import AwsKmsUtils
  import Time
  import UUID

  datatype KMSTuple = | KMSTuple(
    kmsClient: KMS.IKMSClient,
    grantTokens: KMS.GrantTokenList)

  datatype keyManagerStrat =
    | reEncrypt(reEncrypt: KMSTuple)
    | decryptEncrypt(decrypt: KMSTuple, encrypt: KMSTuple)
  {
    ghost predicate ValidState()
    {
      match this
      case reEncrypt(km) => km.kmsClient.ValidState()
      case decryptEncrypt(kmD, kmE) =>
        && kmD.kmsClient.ValidState()
        && kmE.kmsClient.ValidState()
    }
  }

  datatype CheckedItem =
    | itemOriginal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
    | itemTerminal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
    | itemNeither(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)

  type OriginalOrTerminal = s:seq<CheckedItem>
    | forall i <- s :: !i.itemNeither?
    witness *

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function ValidateInitializeMutationInput(
    input: Types.InitializeMutationInput,
    logicalKeyStoreName: string
  ): (output: Result<Types.InitializeMutationInput, Types.Error>)
    ensures output.Success? ==> StateStrucs.ValidMutations?(input.mutations)
    ensures output.Success? && input.mutations.finalEncryptionContext.Some?
            ==>
              && |Structure.SelectCustomEncryptionContextAsString(input.mutations.finalEncryptionContext.value)| == 0
  {
    :- Need(|input.branchKeyIdentifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));
    :- Need(StateStrucs.ValidMutations?(input.mutations),
            Types.KeyStoreAdminException(
              message := "Mutations parameter is invalid; If Encryption Context is given, it cannot be empty or have empty values."));
    :- Need(
         input.mutations.finalEncryptionContext.Some?
         ==>
           input.mutations.finalEncryptionContext.value.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
         Types.KeyStoreAdminException(message := "WIP"));

    // var inputIndex := 0;
    // while inputIndex < |inputEC|
    // {
    //   k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    //   inputIndex := inputIndex + 1;
    // }
    Success(input)
  }

  method {:vcs_split_on_every_assert} InitializeMutation(
    input: Types.InitializeMutationInput,
    logicalKeyStoreName: string,
    keyManagerStrategy: keyManagerStrat,
    storage: Types.AwsCryptographyKeyStoreTypes.IEncryptedKeyStore
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires ValidateInitializeMutationInput(input, logicalKeyStoreName).Success?
    requires StateStrucs.ValidMutations?(input.mutations) // made not need this
    requires storage.ValidState() &&
             match keyManagerStrategy
             case reEncrypt(km) => km.kmsClient.ValidState() && AwsKmsUtils.GetValidGrantTokens(Some(km.grantTokens)).Success?
             case decryptEncrypt(kmD, kmE) =>
               && kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
               && AwsKmsUtils.GetValidGrantTokens(Some(kmD.grantTokens)).Success?
               && AwsKmsUtils.GetValidGrantTokens(Some(kmE.grantTokens)).Success?
    ensures storage.ValidState() &&
            match keyManagerStrategy
            case reEncrypt(km) => km.kmsClient.ValidState()
            case decryptEncrypt(kmD, kmE) => kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
    modifies
      storage.Modifies,
            match keyManagerStrategy
            case reEncrypt(km) => km.kmsClient.Modifies
            case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    requires keyManagerStrategy.reEncrypt?
  {
    :- Need(
      // Remove before Prod
      keyManagerStrategy.reEncrypt?,
      Types.KeyStoreAdminException(message :="BETA :: Only Re Encrypt is supported!!")
    );
    var keyManager := keyManagerStrategy.reEncrypt;
    assert keyManager.kmsClient.ValidState();
    // TODO : REMOVE THIS AXIOM, or at least encapsulate it in opaque
    // assume {:axiom} storage.Modifies !! keyManager.kmsClient.Modifies;

    // Fetch Active Branch Key & Beacon Key & Mutation Lock
    var readItems? := storage.GetItemsForInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.GetItemsForInitializeMutationInput(Identifier := input.branchKeyIdentifier));
    var readItems :- readItems?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    // If Mutation Lock exists, fail

    :- Need(readItems.mutationLock.None?,
            Types.MutationConflictException(
              message :=
                if readItems.mutationLock.Some? then
                  "A Mutation is already in-flight! It's UUID is "
                  + readItems.mutationLock.value.UUID
                  + ". It was created on: " + readItems.mutationLock.value.CreateTime
                else
                  "Should not happen because this conflicts with the Need condition."
            )
    );

    var activeItem := readItems.activeItem;

    :- Need(
      || storage is DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore
      || (
           && activeItem.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricKey?(activeItem)
           && activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
           && readItems.beaconItem.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricBeaconKey?(readItems.beaconItem)
           && readItems.beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreAdminException(
        message := "Active Branch Key Item read from storage is malformed!")
    );

    :- Need(
      && KmsArn.ValidKmsArn?(activeItem.KmsArn)
      && (input.mutations.finalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.mutations.finalKmsArn.value))
    , Types.KeyStoreAdminException(message := "WIP: ")
    );

    // timestamp is for the new Active & Decrypt Only AND for the Mutation Lock
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(message := e));

    var mutationLockUUID? := UUID.GenerateUUID();
    var mutationLockUUID :- mutationLockUUID?
    .MapFailure(e => Types.KeyStoreAdminException(message := "Could not generate UUID for Mutation Lock. " + e));

    var customEncryptionContext
      := map k <- activeItem.EncryptionContext
                  // This pull everything that is not in our restricted list.
             | k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
      :: k := activeItem.EncryptionContext[k];

    var prefixedTerminalCustomEC?: Option<KeyStoreTypes.EncryptionContextString> := None;
    var defixedTerminalCustomEC?: Option<KeyStoreTypes.EncryptionContextString> := None;
    if (input.mutations.finalEncryptionContext.Some?) {
      var prefixedTerminalCustomEC := map k <- input.mutations.finalEncryptionContext.value
        :: Structure.ENCRYPTION_CONTEXT_PREFIX + k := input.mutations.finalEncryptionContext.value[k];
      prefixedTerminalCustomEC? := Some(prefixedTerminalCustomEC);
      defixedTerminalCustomEC? := Some(input.mutations.finalEncryptionContext.value);
    }

    var MutationToApply := StateStrucs.MutationToApply(
      Identifier := input.branchKeyIdentifier,
      Original := StateStrucs.MutableProperties(
        kmsArn := KeyStoreTypes.kmsKeyArn(activeItem.KmsArn),
        customEncryptionContext := customEncryptionContext
      ),
      Terminal := StateStrucs.MutableProperties(
        kmsArn := KeyStoreTypes.kmsKeyArn(input.mutations.finalKmsArn.UnwrapOr(activeItem.KmsArn)),
        customEncryptionContext := prefixedTerminalCustomEC?.UnwrapOr(customEncryptionContext)
        // customEncryptionContext := input.mutations.finalEncryptionContext.UnwrapOr(customEncryptionContext)
      ),
      ExclusiveStartKey := None,
      UUID := Some(mutationLockUUID),
      CreateTime := timestamp
    );

      // -= BEGIN Version Active Branch Key
      // --= Validate Active Branch Key
    :- VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := keyManagerStrategy
    );

      // -= Assert Beacon Key is in Original
    :- Need(
      readItems.beaconItem.EncryptionContext
      ==
      Structure.ReplaceMutableContext(
        readItems.beaconItem.EncryptionContext,
        readItems.beaconItem.KmsArn,
        MutationToApply.Original.customEncryptionContext),
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not in the Original State!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST be in the original state."
      ));
    // -= Validate Beacon Key
    :- VerifyEncryptedHierarchicalKey(
      item := readItems.beaconItem,
      keyManagerStrategy := keyManagerStrategy
    );

    // --= Generate New Decrypt Only Branch Key with terminal properties
    var maybeNewVersion := UUID.GenerateUUID();
    var newVersion :- maybeNewVersion
    .MapFailure(e => Types.KeyStoreAdminException(message := e));

    var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      input.branchKeyIdentifier,
      newVersion,
      timestamp,
      logicalKeyStoreName,
      MutationToApply.Terminal.kmsArn.kmsKeyArn,
      // MutationToApply.Terminal.customEncryptionContext
      defixedTerminalCustomEC?.UnwrapOr(customEncryptionContext)
    );

    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
      encryptionContext := decryptOnlyEncryptionContext,
      kmsConfiguration := MutationToApply.Terminal.kmsArn,
      grantTokens := keyManager.grantTokens,
      kmsClient := keyManager.kmsClient
    );
    var wrappedDecryptOnlyBranchKey :- wrappedDecryptOnlyBranchKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    var newDecryptOnly := Structure.ConstructEncryptedHierarchicalKey(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );

    var ActiveEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(newDecryptOnly.EncryptionContext);
    var newActive :- ReEncryptHierarchicalKey(
      item := newDecryptOnly,
      terminalKmsArn := MutationToApply.Terminal.kmsArn.kmsKeyArn,
      terminalEncryptionContext := ActiveEncryptionContext,
      keyManagerStrategy := keyManagerStrategy
    );

    // -= Mutate Beacon Key
    var BeaconEncryptionContext := Structure.ReplaceMutableContext(
      readItems.beaconItem.EncryptionContext,
      MutationToApply.Terminal.kmsArn.kmsKeyArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    var newBeaconKey :- ReEncryptHierarchicalKey(
      item := readItems.beaconItem,
      terminalKmsArn := MutationToApply.Terminal.kmsArn.kmsKeyArn,
      terminalEncryptionContext := BeaconEncryptionContext,
      keyManagerStrategy := keyManagerStrategy
    );

    // -= Create Mutation Lock
    var MutationToken :- StateStrucs.SerializeMutableBranchKeyProperties(MutationToApply);

    // -= Write Mutation Lock, new branch key version, mutated beacon key
    var throwAway2? := storage.WriteItemsForInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.WriteItemsForInitializeMutationInput(
        active := newActive,
        oldActive := activeItem,
        version := newDecryptOnly,
        beacon := newBeaconKey,
        mutationLock := KeyStoreTypes.MutationLock(
          Identifier := MutationToken.Identifier,
          CreateTime := MutationToken.CreateTime,
          UUID := MutationToken.UUID.value,
          Original := MutationToken.Original,
          Terminal := MutationToken.Terminal
        )
      ));
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var mutatedBranchKeyItems := [
      Types.MutatedBranchKeyItem(itemType := "Mutation Lock: " + mutationLockUUID, description := "Created"),
      Types.MutatedBranchKeyItem(itemType := "Active: " + newVersion, description := "Created"),
      Types.MutatedBranchKeyItem(itemType := "Decrypt Only: " + newVersion, description := "Created"),
      Types.MutatedBranchKeyItem(itemType := "Beacon", description := "Mutated")
    ];

    return Success(Types.InitializeMutationOutput(
                     mutationToken := MutationToken,
                     mutatedBranchKeyItems := mutatedBranchKeyItems));
  }

  // Ensures:
  // Mutations Token is valid
  // logicalKeyStoreName is valid
  function ValidateApplyMutationInput(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string
  ): (output: Result<Types.ApplyMutationInput, Types.Error>)
    ensures output.Success? ==> |logicalKeyStoreName| > 0 && ValidateMutationToken(input.mutationToken).Success?
  {
    var _ :- ValidateMutationToken(input.mutationToken);
    :- Need(|logicalKeyStoreName| > 0,
            Types.KeyStoreAdminException(message := "LogicalKeyStoreName cannot be empty!"));
    Success(input)
  }

  // Ensures:
  // Branch Key ID is set
  // Original is set (not going to deseriazlize yet)
  // Terminal is Valid (not going to deseriazlize yet)
  function ValidateMutationToken(
    input: Types.MutationToken
  ): (output: Result<Types.MutationToken, Types.Error>)
    ensures output.Success?
            ==>
              && |input.Identifier| > 0
              && |input.Original| > 0
              && |input.Terminal| > 0
  {
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));
    :- Need(|input.Original| > 0,
            Types.KeyStoreAdminException(message := "Original cannot be empty!"));
    :- Need(|input.Terminal| > 0,
            Types.KeyStoreAdminException(message := "Terminal cannot be empty!"));
    Success(input)
  }

  method {:vcs_split_on_every_assert} ApplyMutation(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string,
    keyManagerStrategy: keyManagerStrat,
    storage: Types.AwsCryptographyKeyStoreTypes.IEncryptedKeyStore
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires ValidateApplyMutationInput(input, logicalKeyStoreName).Success?
    requires
      && storage.ValidState()
      && keyManagerStrategy.ValidState()
    ensures
      && storage.ValidState()
      && keyManagerStrategy.ValidState()
    modifies
      storage.Modifies,
             match keyManagerStrategy
             case reEncrypt(km) => km.kmsClient.Modifies
             case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    requires keyManagerStrategy.reEncrypt?
  {

    var keyManager := keyManagerStrategy.reEncrypt;
    // assume {:axiom} storage.Modifies !! keyManager.kmsClient.Modifies;

    // -= Query for page Size Branch Key Items
    var queryOut? := storage.QueryForVersions(
      Types.AwsCryptographyKeyStoreTypes.QueryForVersionsInput(
        exclusiveStartKey := input.mutationToken.ExclusiveStartKey,
        Identifier := input.mutationToken.Identifier,
        // DDB TransactWrite takes a max of 25
        // with the mutation lock, 24 items is the maximum we could write
        // TODO this size should be optional
        // DDB is best when you write slow and steady, not as fast as possible :)
        pageSize := input.pageSize.UnwrapOr(24)));

    var queryOut :- queryOut?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    :- Need(
      || storage is DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore
      || (
           forall item <- queryOut.items ::
             && item.Identifier == input.mutationToken.Identifier
             && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
             && item.Type.HierarchicalSymmetricVersion?
             && item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreAdminException(
        message := "WIP:")
    );

    :- Need(
      forall item <- queryOut.items :: KmsArn.ValidKmsArn?(item.KmsArn),
      Types.KeyStoreAdminException(
        message := "WIP:")
    );

    // TODO: Consider adding a short circuit if there are no Items.
    // The while loop will safely skip,
    // but there are few extra deserialization that are not needed.

    var MutationToApply :- StateStrucs.DeserializeMutationToken(input.mutationToken);

    var queryOutItems := Seq.Map(
      item
      requires Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
      =>
        MatchItemToState(item, MutationToApply),
      queryOut.items
    );

    var ItemNeither? := (item: CheckedItem) => item.itemNeither?;

    var neitherState? := Seq.Filter(ItemNeither?, queryOutItems);

    :- Need(
      |neitherState?| == 0
    , Types.KeyStoreAdminException(
        message := if 0 < |neitherState?| then
          "WIP:"
          + Join(Seq.Map((i:CheckedItem) => i.item.Identifier, neitherState?), ",")
        else
          "Can't happen"
      ));

    FilterIsEmpty?(ItemNeither?, queryOutItems);
    var itemsToProcess: OriginalOrTerminal := queryOutItems;

    //TODO: In order to get the logging, we will have to refactor itemsEvaluated to have both cases.
    //For BETA, we will live with out
    var itemsEvaluated := [];
    for versionIndex := 0 to |itemsToProcess|
      // invariant forall item <- itemsToProcess :: item.itemTerminal? || item.itemOriginal?
    {
      var item := itemsToProcess[versionIndex];
      match item {
        case itemTerminal(item) =>
          :- VerifyEncryptedHierarchicalKey(
            item := item,
            keyManagerStrategy:= keyManagerStrategy
          );
        // if item is original, mutate with Failure
        case itemOriginal(item) =>

          var terminalEncryptionContext := Structure.ReplaceMutableContext(
            item.EncryptionContext,
            MutationToApply.Terminal.kmsArn.kmsKeyArn,
            MutationToApply.Terminal.customEncryptionContext
          );

          var mutatedItem :- ReEncryptHierarchicalKey(
            item := item,
            terminalKmsArn := MutationToApply.Terminal.kmsArn.kmsKeyArn,
            terminalEncryptionContext := terminalEncryptionContext,
            keyManagerStrategy := keyManagerStrategy
          );
          itemsEvaluated := itemsEvaluated + [mutatedItem];
      }
    }

    // Add conditional check on Mutation Lock & Mutation Token agreement to Write Request
    var writeReq := KeyStoreTypes.WriteMutatedVersionsInput(
      items := itemsEvaluated,
      Identifier := input.mutationToken.Identifier,
      Original := input.mutationToken.Original,
      Terminal := input.mutationToken.Terminal,
      CompleteMutation := if (|queryOut.exclusiveStartKey| == 0) then Some(true) else None
    );

    // print "\nApply Mutations for ID: " + input.mutationToken.Identifier;
    //  if (|queryOut.exclusiveStartKey| == 0) {
    //    print " Should Delete M-lock ";
    //  } else {
    //    print " Should not Delete M-lock ";
    //  }
    //  print " with mutated item size of : " + String.Base10Int2String(|itemsEvaluated|);
    //  print "\n";

    // -= write to storage ;; MUST write to storage to ensure Terminal in M-Lock and M-Token agree
    var throwAway2? := storage.WriteMutatedVersions(writeReq);
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    output := Success(
      Types.ApplyMutationOutput(
        result := if 0 < |queryOut.exclusiveStartKey| then
          Types.continueMutation(
            input.mutationToken.(
            ExclusiveStartKey := Some(queryOut.exclusiveStartKey)
            )
          )
        else
          Types.ApplyMutationResult.completeMutation(Types.MutationComplete()),
        mutatedBranchKeyItems := []
      ));
  }

  predicate itemMatchesMutableProperities?(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    KmsArn: string,
    CustomEC: Types.AwsCryptographyKeyStoreTypes.EncryptionContextString,
    ECKeysPrefixedToDefixed: set<(string, string)>
  ): (output: bool)
  {
    // Does the Custom Encryption Context match?
    && forall ecKeys :: ecKeys in ECKeysPrefixedToDefixed ==>
                          && (ecKeys.0 in item.EncryptionContext)
                          && (ecKeys.1 in CustomEC)
                          && (item.EncryptionContext[ecKeys.0] == CustomEC[ecKeys.1])
                             // Does the KMS ARN Match?
                          && item.KmsArn == KmsArn
  }

  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
    // KmsArn: string,
    // OriginalEncryptionContext: Types.AwsCryptographyKeyStoreTypes.EncryptionContextString,
    // TerminalEncryptionContext: Types.AwsCryptographyKeyStoreTypes.EncryptionContextString
  ): (output: CheckedItem)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires StateStrucs.MutationToApply?(MutationToApply)
  {
    if item.EncryptionContext
       == Structure.ReplaceMutableContext(
            item.EncryptionContext,
            item.KmsArn,
            MutationToApply.Original.customEncryptionContext
          ) then
      itemOriginal(item)
    else if item.EncryptionContext
            == Structure.ReplaceMutableContext(
                 item.EncryptionContext,
                 MutationToApply.Terminal.kmsArn.kmsKeyArn,
                 MutationToApply.Terminal.customEncryptionContext
               ) then
      itemTerminal(item)
    else
      itemNeither(item)
  }

  function matchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    originalKmsArn: string,
    originalCustomEC: Types.AwsCryptographyKeyStoreTypes.EncryptionContextString,
    originalECKeysPrefixedToDefixed: set<(string, string)>,
    terminalKmsArn: string,
    terminalCustomEC: Types.AwsCryptographyKeyStoreTypes.EncryptionContextString,
    terminalECKeysPrefixedToDefixed: set<(string, string)>
  ): (output: CheckedItem)
  {
    if itemMatchesMutableProperities?(item, originalKmsArn, originalCustomEC, originalECKeysPrefixedToDefixed) then itemOriginal(item)
    else if itemMatchesMutableProperities?(item, terminalKmsArn, terminalCustomEC, terminalECKeysPrefixedToDefixed) then itemTerminal(item)
    else itemNeither(item)
  }

  method VerifyEncryptedHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: keyManagerStrat
  )
    returns (output: Outcome<Types.Error>)
    requires keyManagerStrategy.reEncrypt?

    requires Structure.EncryptedHierarchicalKey?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var throwAway? := KMSKeystoreOperations.ReEncryptKey(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := item.EncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
      grantTokens := keyManagerStrategy.reEncrypt.grantTokens,
      kmsClient := keyManagerStrategy.reEncrypt.kmsClient
    );

    output := if throwAway?.Success? then
      Pass
    else
      Fail(Types.Error.AwsCryptographyKeyStore(throwAway?.error));
  }

  method ReEncryptHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: keyManagerStrat
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires keyManagerStrategy.reEncrypt?

    requires Structure.EncryptedHierarchicalKey?(item)
    requires KMS.IsValid_KeyIdType(terminalKmsArn)
    requires KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
    requires KMSKeystoreOperations.AttemptKmsOperation?(KeyStoreTypes.kmsKeyArn(terminalKmsArn), terminalEncryptionContext)
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var wrappedKey? := KMSKeystoreOperations.ReEncryptKey(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := terminalEncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(terminalKmsArn),
      grantTokens := keyManagerStrategy.reEncrypt.grantTokens,
      kmsClient := keyManagerStrategy.reEncrypt.kmsClient
    );
    var wrappedKey :- wrappedKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalEncryptionContext,
                        wrappedKey.CiphertextBlob.value
                      ));
  }

  // Note: This Method MUST NOT be public, it is internal only
  method CompleteMutation(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string,
    storage: Types.AwsCryptographyKeyStoreTypes.IEncryptedKeyStore
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires storage.ValidState()
    modifies storage.Modifies
    ensures storage.ValidState()
    // requires Query for items returned none
  {
    // Create Write request to delete Mutation Lock
    // Add contional check on Mutation Lock & Mutation Token aggreement to Write Request
    // -= write to storage
    // return MutationComplete
    return Failure(Types.KeyStoreAdminException(message := "Implement me"));
  }


  lemma FilterIsEmpty?<T>(f: (T ~> bool), xs: seq<T>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    ensures forall i | 0 <= i < |xs| :: f(xs[i]) ==> xs[i] in Seq.Filter(f, xs)
    ensures |Seq.Filter(f, xs)| == 0 ==> forall i | 0 <= i < |xs| :: !f(xs[i])
  {
    reveal Seq.Filter();
  }
}
