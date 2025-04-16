// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "KmsUtils.dfy"
include "MutationIndexUtils.dfy"
include "SystemKey/Handler.dfy"
include "Mutations.dfy"

module {:options "/functionSyntax:4" } InternalApplyMutation {
  // StandardLibrary Imports
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import UTF8
    // KeyStore Imports
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import DefaultKeyStorageInterface
  import KmsArn
    // KeyStoreAdmin Imports
  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import KmsUtils
  import MutationIndexUtils
  import SystemKeyHandler = SystemKey.Handler
  import Mutations

  const DEFAULT_APPLY_PAGE_SIZE := 3 as StandardLibrary.UInt.int32

  predicate ValidateQueryOutResults?(
    input: InternalApplyMutationInput,
    queryItems: KeyStoreTypes.QueryForVersionsOutput
  )
  {
    || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
    || (
         forall item <- queryItems.Items ::
           && Mutations.ValidateItemFromStorage?(
                input.storage,
                item,
                identifier := input.MutationToken.Identifier,
                logicalName := input.logicalKeyStoreName)
           && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
           && item.Type.HierarchicalSymmetricVersion?
              // TODO-HV-2-M2 : allow for HV-2
           && item.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1
       )
  }

  datatype InternalApplyMutationInput = | InternalApplyMutationInput (
    nameonly MutationToken: Types.MutationToken ,
    nameonly PageSize: Option<StandardLibrary.UInt.int32> ,
    nameonly SystemKey: KmsUtils.InternalSystemKey ,
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
      && keyManagerStrategy.SupportHV1()
    }
  }

  // Ensures:
  //-= Mutations Token is valid
  //-= logicalKeyStoreName is valid
  //-= PageSize is valid
  function ValidateApplyMutationInput(
    input: InternalApplyMutationInput
  ): (output: Result<InternalApplyMutationInput, Types.Error>)
    ensures output.Success? ==>
              && |input.logicalKeyStoreName| > 0
              && ValidateMutationToken(input.MutationToken).Success?
              && input.PageSize.Some?
              ==>
                0 < input.PageSize.value
                && (
                  && (input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
                      && input.PageSize.Some?)
                  ==>
                    input.PageSize.value <= 99)
  {
    var _ :- ValidateMutationToken(input.MutationToken);
    :- Need(|input.logicalKeyStoreName| > 0,
            Types.KeyStoreAdminException(message := "LogicalKeyStoreName cannot be empty!"));
    :- Need(
         // If the Storage is DDB && a page Size was given
         (input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface && input.PageSize.Some?)
         ==>
           // then the pageSize MUST be less than or equal to 99
           input.PageSize.value <= 99,
         Types.KeyStoreAdminException(message := "The DynamoDB Key Storage supports a max page size of 99"));
    :- Need(
         // If page Size was given then the pageSize MUST be greater than 0
         input.PageSize.Some? ==> 0 < input.PageSize.value,
         Types.KeyStoreAdminException(message := "The page size MUST be greater than 0."));
    Success(input)
  }

  // Ensures:
  // Branch Key ID is set
  function ValidateMutationToken(
    input: Types.MutationToken
  ): (output: Result<Types.MutationToken, Types.Error>)
    ensures output.Success?
            ==>
              && |input.Identifier| > 0
  {
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Mutation Token's Branch Key Identifier cannot be empty!"));
    Success(input)
  }


  method {:isolate_assertions} ApplyMutation(
    input: InternalApplyMutationInput
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires ValidateApplyMutationInput(input).Success?
    requires input.ValidState()
    ensures input.ValidState()
    modifies
      input.storage.Modifies,
            input.keyManagerStrategy.Modifies,
            input.SystemKey.Modifies
  {
    // -= Fetch Commitment and Index
    var storage := input.storage;
    var keyManagerStrategy := input.keyManagerStrategy;
    var SystemKey := input.SystemKey;
    // var logicalKeyStoreName := input.logicalKeyStoreName;
    var fetchMutation? := storage.GetMutation(
      Types.AwsCryptographyKeyStoreTypes.GetMutationInput(
        Identifier := input.MutationToken.Identifier));
    var fetchMutation: KeyStoreTypes.GetMutationOutput :- fetchMutation?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

      // -= Validate Commitment and Index
    :- Need(
      fetchMutation.MutationCommitment.Some?,
      Types.MutationInvalidException(
        message := "No Mutation is in-flight for this Branch Key ID " + input.MutationToken.Identifier + " ."
      ));
    :- Need(
      input.MutationToken.UUID == fetchMutation.MutationCommitment.value.UUID,
      Types.MutationInvalidException(
        message := "The Token and the Mutation Commitment read from storage disagree."
        + " This indicates that the Token is for a different Mutation than the one in-flight."
        + " A possible cause is this token is from an earlier Mutation that already finished?"
        + " Branch Key ID: " + input.MutationToken.Identifier + ";"
        + " Mutation Commitment UUID: " + fetchMutation.MutationCommitment.value.UUID + ";"
        + " Token UUID: " + input.MutationToken.UUID + ";"
      ));
    :- Need(
      fetchMutation.MutationIndex.Some?,
      Types.MutationInvalidException(
        message := "No Mutation Index exsists for this in-flight mutation of Branch Key ID " + input.MutationToken.Identifier + " ."
      ));
    var CommitmentAndIndex :- Mutations.ValidateCommitmentAndIndexStructures(
      input.MutationToken,
      fetchMutation.MutationCommitment.value,
      fetchMutation.MutationIndex.value);

    var commitmentIsVerified :- SystemKeyHandler.VerifyCommitment(CommitmentAndIndex.Commitment, SystemKey);
    :- Need(
      commitmentIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Commitment's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));
    var indexIsVerified :- SystemKeyHandler.VerifyIndex(CommitmentAndIndex.Index, SystemKey);
    :- Need(
      indexIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Index's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));

    var MutationToApply :- StateStrucs.DeserializeMutation(CommitmentAndIndex);

    // -= Query for page Size Branch Key Items
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
        && Structure.EncryptedHierarchicalKeyFromStorage?(item.item)
        && item.item.Type.HierarchicalSymmetricVersion?
        && (item.itemOriginal? ==> item.item.KmsArn == MutationToApply.Original.kmsArn);

    // Process Branch Keys that need to be mutated
    var processedItems? :- ProcessBranchKeysInApplyMutation(itemsToProcess, keyManagerStrategy, MutationToApply);
    var itemsEvaluated := processedItems?.0;
    var logStatements := processedItems?.1;

      // Update Index
    :- Need(
      UTF8.ValidUTF8Seq(queryOut.ExclusiveStartKey),
      Types.KeyStoreAdminException(
        message:="ExclusiveStartKey returned by Key Store's Storage is not valid UTF-8 Byte Sequence."));
    var newIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, Some(queryOut.ExclusiveStartKey));
    var signedNewIndex :- SystemKeyHandler.SignIndex(newIndex, SystemKey);

    // TODO-Mutations-FF Log Index update or deletion of commitment and index
    var _ :- WriteMutations(
      storage,
      itemsEvaluated,
      CommitmentAndIndex.Commitment,
      newIndex := signedNewIndex,
      oldIndex := CommitmentAndIndex.Index,
      endMutationBool := (|queryOut.ExclusiveStartKey| == 0)
    );

    var Token := Types.MutationToken(
      Identifier := MutationToApply.Identifier,
      UUID := MutationToApply.UUID,
      CreateTime := MutationToApply.CreateTime);

    output := Success(
      Types.ApplyMutationOutput(
        MutationResult :=
          if 0 < |queryOut.ExclusiveStartKey|
          then
            Types.ContinueMutation(Token)
          else
            Types.ApplyMutationResult.CompleteMutation(Types.MutationComplete()),
        MutatedBranchKeyItems := logStatements
      ));
  }

  method WriteMutations(
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface,
    itemsEvaluated: seq<KeyStoreTypes.OverWriteEncryptedHierarchicalKey>,
    commitment: KeyStoreTypes.MutationCommitment,
    nameonly newIndex: KeyStoreTypes.MutationIndex,
    nameonly oldIndex: KeyStoreTypes.MutationIndex,
    nameonly endMutationBool: bool
  ) returns (output: Result<(), Types.Error>)
    requires storage.ValidState()
    modifies storage.Modifies
    ensures storage.ValidState()
    ensures output.Success? ==>
              && |storage.History.WriteMutatedVersions| == |old(storage.History.WriteMutatedVersions)| + 1
              && Seq.Last(storage.History.WriteMutatedVersions).output.Success?
              && var input := Seq.Last(storage.History.WriteMutatedVersions).input;
              && KeyStoreTypes.WriteMutatedVersionsInput(
                Items := itemsEvaluated,
                MutationCommitment := commitment,
                MutationIndex := KeyStoreTypes.OverWriteMutationIndex(Index:=newIndex, Old:=oldIndex),
                EndMutation := endMutationBool
              ) == input
  {
    // Add conditional check on Mutation Commitment & Mutation Token agreement to Write Request
    var writeReq := KeyStoreTypes.WriteMutatedVersionsInput(
      Items := itemsEvaluated,
      MutationCommitment := commitment,
      MutationIndex := KeyStoreTypes.OverWriteMutationIndex(Index:=newIndex, Old:=oldIndex),
      EndMutation := endMutationBool
    );

    // -= write to storage ;; MUST write to storage to ensure Terminal in M-Commitment and M-Token agree
    var throwAway2? := storage.WriteMutatedVersions(writeReq);
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    return Success(());
  }

  method QueryForVersionsAndValidate(
    input: InternalApplyMutationInput,
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
                PageSize := input.PageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)
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
        PageSize := input.PageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)));

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

  method ProcessBranchKeysInApplyMutation(
    items: Mutations.OriginalOrTerminal,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    mutationToApply: StateStrucs.MutationToApply
  ) returns (output: Result<(seq<KeyStoreTypes.OverWriteEncryptedHierarchicalKey>, seq<Types.MutatedBranchKeyItem>), Types.Error>)
    requires keyManagerStrategy.ValidState() && mutationToApply.ValidState()
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply, keyManagerStrategy)
    requires forall item <- items :: item.item is KeyStoreTypes.EncryptedHierarchicalKey
    requires forall item <- items :: item.item.Type.HierarchicalSymmetricVersion?
    requires forall item <- items :: KmsArn.ValidKmsArn?(item.item.KmsArn)
    requires forall item <- items :: Structure.EncryptedHierarchicalKeyFromStorage?(item.item)
    requires forall item <- items :: item.itemOriginal? ==> item.item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! mutationToApply.Terminal.customEncryptionContext.Keys
  {
    var logStatements: seq<Types.MutatedBranchKeyItem> := [];
    var itemsEvaluated := [];

    for versionIndex := 0 to |items|
    {
      var item := items[versionIndex];
      match item {
        case itemTerminal(item) =>
          var verify? := Mutations.VerifyEncryptedHierarchicalKey(
            item := item,
            keyManagerStrategy := keyManagerStrategy,
            localOperation := "ApplyMutation",
            mutationToApply := mutationToApply
          );
          if (verify?.Fail?) {
            return Failure(verify?.error);
          }
          logStatements := logStatements
          + [Types.MutatedBranchKeyItem(
               ItemType := "Version (Decrypt Only): " + item.Type.HierarchicalSymmetricVersion.Version,
               Description := " Validated in Terminal")];
        // if item is original, mutate with Failure
        case itemOriginal(item) =>
          var mutatedItem :- Mutations.MutateItem(item, mutationToApply, keyManagerStrategy, "ApplyMutation", false);
          itemsEvaluated := itemsEvaluated + [
            KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=mutatedItem, Old:=item)
          ];
          logStatements := logStatements
          + [Types.MutatedBranchKeyItem(
               ItemType := "Decrypt Only: " + item.Type.HierarchicalSymmetricVersion.Version,
               Description := " Mutated to Terminal")];
      }
    }
    return Success((itemsEvaluated, logStatements));
  }
}
