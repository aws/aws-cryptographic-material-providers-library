// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "KeyStoreAdminErrorMessages.dfy"

/** Common Functions/Methods for Mutation Commitment And Index. */
module {:options "/functionSyntax:4" } CommitmentAndIndex {
  import opened Wrappers
  import opened StandardLibrary.NeedError
  import Seq
  import UTF8

  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdminErrorMessages

  import KeyStoreTypes = Types.AwsCryptographyKeyStoreTypes

  /**
     The Commitment & Index are persisted to the storage by Initialize.
     The Commitment & Index are read by Apply.
     The Index is updated by Apply.
     Both are deleted when the Mutation is completed by Apply.
   */
  datatype CommitmentAndIndex = CommitmentAndIndex (
    commitment: KeyStoreTypes.MutationCommitment,
    index: KeyStoreTypes.MutationIndex
  ) {
    /** 
      The Commitment & Index MUST always have the same Identifier & UUID. 
      They MAY NOT have the same CreateTime. 
    */
    ghost predicate ValidIDs()
    {
      && 0 < |commitment.Identifier|
      && commitment.Identifier == index.Identifier
      && 0 < |commitment.UUID |
      && commitment.UUID == index.UUID
    }
    ghost predicate ValidUTF8()
    {
      // TODO: Does the `enc` field need ValidUTF8Seq? Same for Index?
      // Dafny's JSON library needs ValidUTF8Seq, but the system key handler does not.
      && UTF8.ValidUTF8Seq(commitment.Original)
      && UTF8.ValidUTF8Seq(commitment.Terminal)
      && UTF8.ValidUTF8Seq(commitment.Input)
      && UTF8.ValidUTF8Seq(index.PageIndex)
    }
  }

  predicate ValidCommitment?(
    Commitment: KeyStoreTypes.MutationCommitment
  ) {
    && UTF8.ValidUTF8Seq(Commitment.Original)
    && UTF8.ValidUTF8Seq(Commitment.Terminal)
    && UTF8.ValidUTF8Seq(Commitment.Input)
    && 0 < |Commitment.Identifier|
    && 0 < |Commitment.UUID|
  }

  predicate ValidIndex?(
    Index: KeyStoreTypes.MutationIndex
  ) {
    && 0 < |Index.Identifier|
    && 0 < |Index.UUID|
    && UTF8.ValidUTF8Seq(Index.PageIndex)
  }

  method FetchMutationItems(
    storage: KeyStoreTypes.IKeyStorageInterface,
    bkid: string
  ) returns (output: Result<CommitmentAndIndex, Types.Error>)
    requires storage.ValidState() && 0 < |bkid|
    modifies storage.Modifies
    ensures storage.ValidState()
    ensures output.Success? ==>
              && |old(storage.History.GetMutation)| + 1 == |storage.History.GetMutation|
              && var storageEvent := Seq.Last(storage.History.GetMutation);
              && storageEvent.input.Identifier == bkid
              && storageEvent.output.Success?
              && storageEvent.output.value.MutationCommitment.Some?
              && storageEvent.output.value.MutationIndex.Some?
              && var commitment := storageEvent.output.value.MutationCommitment.value;
              && var index := storageEvent.output.value.MutationIndex.value;
              && output.value.ValidIDs()
              && output.value.commitment == commitment
              && output.value.index == index
              && output.value.commitment.Identifier == bkid
  {
    var fetchMutation? := storage.GetMutation(
      Types.AwsCryptographyKeyStoreTypes.GetMutationInput(
        Identifier := bkid));
    var fetchMutation :- fetchMutation?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    :- Need(
      fetchMutation.MutationCommitment.Some?,
      Types.MutationInvalidException(
        message := KeyStoreAdminErrorMessages.NoMutationInFlight(bkid)
      ));
    var commitment := fetchMutation.MutationCommitment.value;
    :- Need(
      fetchMutation.MutationIndex.Some?,
      Types.MutationInvalidException(
        message := KeyStoreAdminErrorMessages.NoMutationIndexExists(bkid)
      ));
    var index := fetchMutation.MutationIndex.value;
    :- Need(
      // @texastony tried to convince Dafny the post condition on GetMutationEnsuresPublicly
      // made this check redundant, but Dafny would not buy it
      // token.Identifier == commitment.Identifier == index.Identifier,
      bkid == commitment.Identifier,
      Types.MutationInvalidException(message := "Storage returned MUTATION_COMMITMENT and MUTATION_INDEX for a different branch key!"));
    var mutationItems := CommitmentAndIndex(commitment, index);
    :- MutationItemsValidIDs(mutationItems);
    return Success(mutationItems);
  }

  function MutationItemsValidIDs(
    mutationItems: CommitmentAndIndex
  ): (outcome: Outcome<Types.Error>)
    requires 0 < |mutationItems.commitment.Identifier|
    ensures outcome.Pass? ==> mutationItems.ValidIDs()
  {
    :- NeedOutcome(
         // @texastony tried to convince Dafny the post condition on GetMutationEnsuresPublicly
         // made this check redundant, but Dafny would not buy it
         mutationItems.commitment.Identifier == mutationItems.index.Identifier,
         () => Types.MutationInvalidException(
             message := KeyStoreAdminErrorMessages.IndexAndCommitmentBKIDDisagree(
               indexBKID := mutationItems.index.Identifier,
               commitmentBKID := mutationItems.commitment.Identifier
             )));
    :- NeedOutcome(
         // Just like with bkid, Dafny does not want to give us this.
         mutationItems.commitment.UUID == mutationItems.index.UUID,
         () => Types.MutationInvalidException(
             message := KeyStoreAdminErrorMessages.IndexAndCommitmentUUIDDisagree(
               indexUUID := mutationItems.index.UUID,
               commitmentUUID := mutationItems.commitment.UUID
             )));
    :- NeedOutcome(
         0 < |mutationItems.commitment.UUID|,
         () => Types.MutationInvalidException(
             message:=KeyStoreAdminErrorMessages.INVALID_COMMITMENT_UUID
           ));
    Outcome.Pass
  }

  function TokenAndMutationItemsAggree(
    mutationItems: CommitmentAndIndex,
    token: Types.MutationToken
  ): (outcome: Outcome<Types.Error>)
    requires mutationItems.ValidIDs()
    ensures mutationItems.ValidIDs()
    ensures
      outcome.Pass?
      ==>
        && mutationItems.commitment.UUID == token.UUID
        && mutationItems.index.UUID == token.UUID
  {
    :- NeedOutcome(
         mutationItems.commitment.UUID == token.UUID,
         () => Types.MutationInvalidException(
             message := KeyStoreAdminErrorMessages.TokenAndMutationCommitmentDisagree(
               token.Identifier,
               mutationItems.commitment.UUID,
               token.UUID
             )));
    Outcome.Pass
  }

  function MutationItemsValidUTF8(
    mutationItems: CommitmentAndIndex
  ): (outcome: Outcome<Types.Error>)
    requires mutationItems.ValidIDs()
    ensures
      outcome.Pass?
      ==>
        && mutationItems.ValidIDs()
        && mutationItems.ValidUTF8()
        && ValidCommitment?(mutationItems.commitment)
        && ValidIndex?(mutationItems.index)
  {
    :- NeedOutcome(
         ValidCommitment?(mutationItems.commitment),
         () => Types.MutationInvalidException(
             message := KeyStoreAdminErrorMessages.INVALID_COMMITMENT_UTF8
           ));
    :- NeedOutcome(
         ValidIndex?(mutationItems.index),
         () => Types.MutationInvalidException(
             message := KeyStoreAdminErrorMessages.INVALID_INDEX_UTF8
           ));
    Outcome.Pass
  }
}