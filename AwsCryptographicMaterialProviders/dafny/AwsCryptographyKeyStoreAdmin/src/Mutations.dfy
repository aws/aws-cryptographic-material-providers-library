// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "PrefixUtils.dfy"
include "MutationValidation.dfy"

module {:options "/functionSyntax:4" } Mutations {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq

  import Structure
  import DefaultKeyStorageInterface
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

  import PrefixUtils
  import MutationValidation

  const DEFAULT_APPLY_PAGE_SIZE := 3 as StandardLibrary.UInt.int32

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
      // Never describe itemNeither to customers as such.
      // Always use the `UnExecptedStateException`.
    | itemNeither(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)

  type OriginalOrTerminal = s:seq<CheckedItem>
    | forall i <- s :: !i.itemNeither?
    witness *

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function {:vcs_split_on_every_assert} ValidateInitializeMutationInput(
    input: Types.InitializeMutationInput,
    logicalKeyStoreName: string
  ): (output: Result<Types.InitializeMutationInput, Types.Error>)
    ensures
      output.Success?
      ==>
        && StateStrucs.ValidMutations?(input.mutations)
        && input.mutations.terminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.mutations.terminalKmsArn.value)

  {
    :- Need(|input.branchKeyIdentifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));
    var terminalEC := input.mutations.terminalEncryptionContext.UnwrapOr(map[]);
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
         && (input.mutations.terminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.mutations.terminalKmsArn.value)),
         Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
       );
    :- Need(StateStrucs.ValidMutations?(input.mutations),
            Types.KeyStoreAdminException(
              message := "Mutations parameter is invalid; If Encryption Context is given, it cannot be empty or have empty values."));
    Success(input)
  }

  method {:vcs_split_on_every_assert} InitializeMutation(
    input: Types.InitializeMutationInput,
    logicalKeyStoreName: string,
    keyManagerStrategy: keyManagerStrat,
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires ValidateInitializeMutationInput(input, logicalKeyStoreName).Success?
    requires StateStrucs.ValidMutations?(input.mutations) // may not need this
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
    var keyManager := keyManagerStrategy.reEncrypt;

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
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.activeItem.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricKey?(readItems.activeItem)
           && readItems.activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
           && KmsArn.ValidKmsArn?(activeItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Active Branch Key Item read from storage is malformed!")
    );

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.beaconItem.Identifier == input.branchKeyIdentifier
           && Structure.ActiveHierarchicalSymmetricBeaconKey?(readItems.beaconItem)
           && readItems.beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
           && KmsArn.ValidKmsArn?(readItems.beaconItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Beacon Branch Key Item read from storage is malformed!")
    );

      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
    :- Need(
      && (input.mutations.terminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.mutations.terminalKmsArn.value)),
      Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
    );

    // timestamp is for the new Active & Decrypt Only AND for the Mutation Lock
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate a timestamp: " + e));

    var mutationLockUUID? := UUID.GenerateUUID();
    var mutationLockUUID :- mutationLockUUID?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for Mutation Lock. " + e));

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
    if (input.mutations.terminalEncryptionContext.Some?) {

      var terminalEC := PrefixUtils.AddingPrefixToKeysOfMapDoesNotCreateCollisions(
        prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
        aMap := input.mutations.terminalEncryptionContext.value
      ) + unexpectedEC;
      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
      :- Need(
        terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
        Types.KeyStoreAdminException(message:="Terminal Encryption Context contains a reserved word!")
      );
      terminalEC? := Some(terminalEC);
      assert terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    }

    assert KmsArn.ValidKmsArn?(activeItem.KmsArn);
    var MutationToApply := StateStrucs.MutationToApply(
      Identifier := input.branchKeyIdentifier,
      Original := StateStrucs.MutableProperties(
        kmsArn := activeItem.KmsArn,
        customEncryptionContext := inferredOriginalEC
      ),
      Terminal := StateStrucs.MutableProperties(
        kmsArn := input.mutations.terminalKmsArn.UnwrapOr(activeItem.KmsArn),
        customEncryptionContext := terminalEC?.UnwrapOr(inferredOriginalEC)
      ),
      ExclusiveStartKey := None,
      UUID := Some(mutationLockUUID),
      CreateTime := timestamp
    );

    assert MutationToApply.Original.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.Terminal.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    // -= BEGIN Version Active Branch Key
    // --= Validate Active Branch Key
    :- VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := keyManagerStrategy
    );

      // -= Assert Beacon Key is in Original
    :- Need(
      readItems.beaconItem.KmsArn == MutationToApply.Original.kmsArn,
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not encrypted with the same KMS Key as ACTIVE!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST be in the same, original state."
      ));
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

    // --= Generate New Decrypt Only Branch Key with terminal properties
    var maybeNewVersion := UUID.GenerateUUID();
    var newVersion :- maybeNewVersion
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for new Decrypt Only. " + e));


    var decryptOnlyEncryptionContext := MutationValidation.DecryptOnlyBranchKeyEncryptionContextForMutation(
      input.branchKeyIdentifier,
      newVersion,
      timestamp,
      logicalKeyStoreName,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
      encryptionContext := decryptOnlyEncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(MutationToApply.Terminal.kmsArn),
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
      originalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := ActiveEncryptionContext,
      keyManagerStrategy := keyManagerStrategy
    );

    // -= Mutate Beacon Key
    var BeaconEncryptionContext := Structure.ReplaceMutableContext(
      readItems.beaconItem.EncryptionContext,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    assert readItems.beaconItem.KmsArn == MutationToApply.Original.kmsArn;
    var newBeaconKey :- ReEncryptHierarchicalKey(
      item := readItems.beaconItem,
      originalKmsArn := MutationToApply.Original.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := BeaconEncryptionContext,
      keyManagerStrategy := keyManagerStrategy
    );

    // -= Create Mutation Lock
    var MutationToken :- StateStrucs.SerializeMutableBranchKeyProperties(MutationToApply);

    // -= Write Mutation Lock, new branch key version, mutated beacon key
    var throwAway2? := storage.WriteInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.WriteInitializeMutationInput(
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
    // TODO Mutations FastFollow? :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Lock get written?
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
    logicalKeyStoreName: string,
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  ): (output: Result<Types.ApplyMutationInput, Types.Error>)
    ensures output.Success? ==>
              && |logicalKeyStoreName| > 0
              && ValidateMutationToken(input.mutationToken).Success?
              && input.pageSize.Some? ==> 0 < input.pageSize.value
                                          && (storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface && input.pageSize.Some? ==> input.pageSize.value <= 99)
  {
    var _ :- ValidateMutationToken(input.mutationToken);
    :- Need(|logicalKeyStoreName| > 0,
            Types.KeyStoreAdminException(message := "LogicalKeyStoreName cannot be empty!"));
    :- Need(
         // If the Storage is DDB && a page Size was given
         (storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface && input.pageSize.Some?)
         ==>
           // then the pageSize MUST be less than or equal to 99
           input.pageSize.value <= 99,
         Types.KeyStoreAdminException(message := "The DynamoDB Key Storage supports a max page size of 99"));
    :- Need(
         // If page Size was given then the pageSize MUST be greater than 0
         input.pageSize.Some? ==> 0 < input.pageSize.value,
         Types.KeyStoreAdminException(message := "The page size MUST be greater than 0."));
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
            Types.KeyStoreAdminException(message := "Mutation Token's Branch Key Identifier cannot be empty!"));
    :- Need(|input.Original| > 0,
            Types.KeyStoreAdminException(message := "Mutation Token's Original cannot be empty!"));
    :- Need(|input.Terminal| > 0,
            Types.KeyStoreAdminException(message := "Mutation Token's Terminal cannot be empty!"));
    Success(input)
  }

  method {:vcs_split_on_every_assert} ApplyMutation(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string,
    keyManagerStrategy: keyManagerStrat,
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires ValidateApplyMutationInput(input, logicalKeyStoreName, storage).Success?
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

    // -= Query for page Size Branch Key Items
    var queryOut? := storage.QueryForVersions(
      Types.AwsCryptographyKeyStoreTypes.QueryForVersionsInput(
        exclusiveStartKey := input.mutationToken.ExclusiveStartKey,
        Identifier := input.mutationToken.Identifier,
        pageSize := input.pageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)));

    var queryOut :- queryOut?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           forall item <- queryOut.items ::
             && item.Identifier == input.mutationToken.Identifier
             && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
             && item.Type.HierarchicalSymmetricVersion?
             && item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      // TODO-Mutations-FF: Replace this Need with something that can return an ID
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

      // TODO-Mutations-FF: Replace this Need with something that can return an ID
    :- Need(
      forall item <- queryOut.items :: KmsArn.ValidKmsArn?(item.KmsArn),
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

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
    , Types.UnexpectedStateException(
        message := if 0 < |neitherState?| then
          "Item(s) found in an unexpected state: "
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
            MutationToApply.Terminal.kmsArn,
            MutationToApply.Terminal.customEncryptionContext
          );

          var mutatedItem :- ReEncryptHierarchicalKey(
            item := item,
            originalKmsArn := MutationToApply.Original.kmsArn,
            terminalKmsArn := MutationToApply.Terminal.kmsArn,
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
      CompleteMutation := (|queryOut.exclusiveStartKey| == 0)
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


  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
  ): (output: CheckedItem)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires StateStrucs.MutationToApply?(MutationToApply)
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

  method {:isolate_assertions} ReEncryptHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly originalKmsArn: string,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: keyManagerStrat
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires keyManagerStrategy.reEncrypt?
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
    var wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := terminalEncryptionContext,
      sourceKmsArn := originalKmsArn,
      destinationKmsArn := terminalKmsArn,
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

  lemma FilterIsEmpty?<T>(f: (T ~> bool), xs: seq<T>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    ensures forall i | 0 <= i < |xs| :: f(xs[i]) ==> xs[i] in Seq.Filter(f, xs)
    ensures |Seq.Filter(f, xs)| == 0 ==> forall i | 0 <= i < |xs| :: !f(xs[i])
  {
    reveal Seq.Filter();
  }
}
