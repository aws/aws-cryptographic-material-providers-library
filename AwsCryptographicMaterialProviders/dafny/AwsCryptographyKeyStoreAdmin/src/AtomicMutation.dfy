// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "PrefixUtils.dfy"
include "KmsUtils.dfy"
include "MutationIndexUtils.dfy"
include "SystemKey/Handler.dfy"
include "Mutations.dfy"
include "ApplyMutation.dfy"
include "InitializeMutation.dfy"

module {:options "/functionSyntax:4" } InternalAtomicMutation {
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
    // TODO-Atomic: Reuse some of the functions, Need Refactoring
  import InternalInitializeMutation
  import InternalApplyMutation

  // TODO: Confirm Back
  predicate ValidateQueryOutResults?(
    input: InternalAtomicMutationInput,
    queryItems: KeyStoreTypes.QueryForVersionsOutput
  )
  {
    || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
    || (
         forall item <- queryItems.Items ::
           && Mutations.ValidateItemFromStorage?(
                input.storage,
                item,
                identifier := input.Identifier,
                logicalName := input.logicalKeyStoreName)
           && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
           && item.Type.HierarchicalSymmetricVersion?
       )
  }

  datatype InternalAtomicMutationInput = | InternalAtomicMutationInput (
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
  function {:isolate_assertions} ValidateAtomicMutationInput(
    input: InternalAtomicMutationInput
  ): (output: Result<InternalAtomicMutationInput, Types.Error>)
    ensures
      output.Success?
      ==>
        && StateStrucs.ValidMutations?(input.Mutations)
        && 0 < |input.Identifier|
    ensures
      && output.Success?
      && input.Mutations.TerminalKmsArn.Some?
      ==>
        && KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)
  {
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));

    // TODO-Atomic: If the Storage is DDB, then total no of items should be less than 99


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

  method {:isolate_assertions} AtomicMutation(
    input: InternalAtomicMutationInput
  )
    returns (output: Result<Types.AtomicMutationOutput, Types.Error>)
    requires ValidateAtomicMutationInput(input).Success?
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
    // var resumeMutation? := false;

    // Fetch Active Branch Key & Beacon Key & Mutation Lock
    var readItems? := input.storage.GetItemsForInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.GetItemsForInitializeMutationInput(Identifier := input.Identifier));
    var readItems :- readItems?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    // TODO-Atomic: Should we error out for cases;
    //  case 1: MLock -> None & MIndex -> Some then Error (Corruption)
    //  case 2: MLock -> Some? then Error ()
    // Check for any existing mutation state
    // TODO-Atomic: Question? We may need support deleting existing mutation,
    //  As in-flight does not allow users to leverage atomic mutation.
    if (readItems.MutationCommitment.Some? || readItems.MutationIndex.Some?) {
      var message := if readItems.MutationCommitment.Some? && readItems.MutationIndex.Some? then
        "Found both Mutation Commitment and Mutation Index."
        + " An active mutation is in progress for this Branch Key."
        + " To proceed with Atomic Mutation, first complete the existing mutation using ApplyMutation"
        + " or check the current mutation state using DescribeMutation."
        + "\nBranch Key ID: " + input.Identifier
        + "\nMutation UUID: " + readItems.MutationCommitment.value.UUID
        + "\nMutation Created On: " + readItems.MutationCommitment.value.CreateTime
      else if readItems.MutationCommitment.Some? then
        "Found Mutation Commitment without Mutation Index."
        + " An active mutation is in progress for this Branch Key."
        + " To proceed with Atomic Mutation, first complete the existing mutation using ApplyMutation"
        + " or check the current mutation state using DescribeMutation."
        + "\nBranch Key ID: " + input.Identifier
        + "\nMutation UUID: " + readItems.MutationCommitment.value.UUID
        + "\nMutation Created On: " + readItems.MutationCommitment.value.CreateTime
      else
        "Found a Mutation Index but no Mutation Commitment."
        + " The Key Store's Storage, for this Branch Key, has become corrupted."
        + " Recommend auditing the Branch Key's items for tampering."
        + " Recommend auditing access to the storage."
        + " To successfully start a new mutation, delete the Mutation Index."
        + " But know that the new mutation will fail if any corrupt items are encountered."
        + "\nBranch Key ID: " + input.Identifier
        + "\nMutation Index UUID: " + readItems.MutationIndex.value.UUID;

      return Failure(
          Types.MutationConflictException(message := message)
        );
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

      // ValidateAtomicMutationInput SHOULD take care of this Need, but Dafny is struggling
    :- Need(
      && (input.Mutations.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)),
      Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
    );

    // timestamp is for the new Active & Decrypt Only AND for the Mutation Commitment
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate a timestamp: " + e));

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
      // ValidateAtomicMutationInput SHOULD take care of this Need, but Dafny is struggling
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
      UUID := "Atomic-Mutation-Place-Holder-UUID",
      CreateTime := timestamp,
      Input := input.Mutations,
      CommitmentCiphertext := [0], // TODO-Mutations-GA Create Commitment Ciphertext
      IndexCiphertext := [0] // TODO-Mutations-GA Create Index Ciphertext
    );

    assert MutationToApply.Original.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.Terminal.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    // TODO-Atomic: May not hold true, since we don't require UUID/maybe a placeholder
    assert MutationToApply.ValidState();


    // --= Validate Active Branch Key
    var verifyActive? := Mutations.VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "AtomicMutation"
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
          + " For Atomic Mutation to succeed, the ACTIVE & Beacon Key MUST have the same KMS-ARN and Custom Encryption Context!"
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
          + " For Atomic Mutation to succeed, the ACTIVE & Beacon Key MUST be in the original state."
      ));

    var initializeMutationActiveInput := InternalInitializeMutation.InitializeMutationActiveInput(
      input :=   InternalInitializeMutation.InternalInitializeMutationInput(
        Identifier := input.Identifier,
        Mutations := input.Mutations,
        SystemKey := input.SystemKey,
        DoNotVersion := input.DoNotVersion,
        logicalKeyStoreName := input.logicalKeyStoreName,
        keyManagerStrategy := input.keyManagerStrategy,
        storage := input.storage
      ),
      activeItem := activeItem,
      mutationToApply := MutationToApply,
      timestamp := timestamp);
    assert initializeMutationActiveInput.ValidState();
    var initializeMutationActiveOutput :- InternalInitializeMutation.InitializeMutationActive(initializeMutationActiveInput);

    // -= Mutate Beacon Key
    var newBeaconKey :- Mutations.MutateItem(readItems.BeaconItem, MutationToApply, input.keyManagerStrategy, "AtomicMutation", false);

    // TODO-Atomic: Query for Versions
    var queryOut :- QueryForVersionsAndValidate(input, MutationToApply);
    var queryOutItems := Seq.Map(
      item
      requires Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
      =>
        Mutations.MatchItemToState(item, MutationToApply),
      queryOut.Items
    );

    var ItemNeither? := (item: Mutations.CheckedItem) => item.itemNeither?;

    var neitherState? := Seq.Filter(ItemNeither?, queryOutItems);

    :- Need(
      |neitherState?| == 0
    , Types.UnexpectedStateException(
        message := if 0 < |neitherState?| then
          "Item(s) found in an unexpected state: "
          + Join(Seq.Map((i: Mutations.CheckedItem) => i.item.Identifier, neitherState?), ",")
        else
          "Can't happen"
      ));

    Mutations.FilterIsEmpty?(ItemNeither?, queryOutItems);
    var itemsToProcess: Mutations.OriginalOrTerminal := queryOutItems;

    assert forall item <- itemsToProcess ::
        && item.item is KeyStoreTypes.EncryptedHierarchicalKey
        && Structure.EncryptedHierarchicalKey?(item.item)
        && item.item.Type.HierarchicalSymmetricVersion?
        && (item.itemOriginal? ==> item.item.KmsArn == MutationToApply.Original.kmsArn);

    // Process Branch Keys that need to be mutated
    var processedItems? :- InternalApplyMutation.ProcessBranchKeysInApplyMutation(itemsToProcess, input.keyManagerStrategy, MutationToApply);
    var itemsEvaluated := processedItems?.0;
    var versionlogStatements := processedItems?.1;

    // -= Write new branch key version, mutated beacon key,
    var throwAway2? := input.storage.WriteAtomicMutation(
      KeyStoreTypes.WriteAtomicMutationInput(
        Active := initializeMutationActiveOutput.writeActive,
        Version := initializeMutationActiveOutput.writeVersion,
        Beacon := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newBeaconKey, Old:=readItems.BeaconItem),
        // TODO-Atomic: Validate Versions.
        Items := itemsEvaluated
      ));
    // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Commitment get written?
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var logStatements :=
      initializeMutationActiveOutput.logStatements
      + [Types.MutatedBranchKeyItem(ItemType := "Beacon", Description := "Mutated")]
      + versionlogStatements;

    return Success(Types.AtomicMutationOutput(
                     MutatedBranchKeyItems := logStatements
                   ));
  }

  // TODO-Atomic: Leverage IniliazeMutation & AtomicMutation
  // TODO-Mutations-FF: Refactor all common functions into a new module maybe?
  // TODO-Atomic: Refactor with ApplyMutation
  method QueryForVersionsAndValidate(
    input: InternalAtomicMutationInput,
    mutationToApply: StateStrucs.MutationToApply
  ) returns (output: Result<KeyStoreTypes.QueryForVersionsOutput, Types.Error>)
    requires input.ValidState()
    modifies input.storage.Modifies
    ensures input.ValidState()
    ensures output.Success? ==>
              && |input.storage.History.QueryForVersions| == |old(input.storage.History.QueryForVersions)| + 1
              && Seq.Last(input.storage.History.QueryForVersions).output.Success?
              && var queryOutInput := Seq.Last(input.storage.History.QueryForVersions).input;
              && KeyStoreTypes.QueryForVersionsInput(
                ExclusiveStartKey := mutationToApply.ExclusiveStartKey,
                Identifier := mutationToApply.Identifier,
                PageSize := 97
              ) == queryOutInput
    ensures output.Success? ==>
              && Seq.Last(input.storage.History.QueryForVersions).output.Success?
              && var queryOutOutput := Seq.Last(input.storage.History.QueryForVersions).output.value;
              && output.value == queryOutOutput
              && ValidateQueryOutResults?(input, output.value)
              && forall item <- output.value.Items :: Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
                                                      && forall item <- output.value.Items :: item.Type.HierarchicalSymmetricVersion?
  {
    var queryOut? := input.storage.QueryForVersions(
      Types.AwsCryptographyKeyStoreTypes.QueryForVersionsInput(
        ExclusiveStartKey := mutationToApply.ExclusiveStartKey,
        Identifier := mutationToApply.Identifier,
        PageSize := 97));

    var queryOut :- queryOut?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    :- Need(
      ValidateQueryOutResults?(input, queryOut),
      // TODO-Mutations-FF: Replace this Need with something that can return an ID
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

    return Success(queryOut);
  }
}
