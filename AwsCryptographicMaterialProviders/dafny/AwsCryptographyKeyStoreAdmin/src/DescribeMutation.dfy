// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "MutationsConstants.dfy"

module {:options "/functionSyntax:4" } DescribeMutation {
  import opened StandardLibrary
  import opened Wrappers

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import M_ErrorMessages = MutationsConstants.ErrorMessages

  datatype InternalDescribeMutationInput = | InternalDescribeMutationInput (
    nameonly Identifier: string ,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )

  method DescribeMutation(
    input: InternalDescribeMutationInput
  )
    returns (output: Result<Types.DescribeMutationOutput, Types.Error>)
    requires input.storage.ValidState()
    ensures input.storage.ValidState()
    modifies input.storage.Modifies
  {
    // TODO-Mutations-GA :: Consolidate the Index and Commitment validation here with ApplyMutation's
    var storageReq := KeyStoreTypes.GetMutationInput(
      Identifier := input.Identifier
    );
    var fetchMutation? := input.storage.GetMutation(storageReq);
    if (fetchMutation?.Failure?) {
      return Failure(Types.Error.AwsCryptographyKeyStore(AwsCryptographyKeyStore := fetchMutation?.error));
    }
    var fetchMutation := fetchMutation?.value;
    if (fetchMutation.MutationCommitment.None? && fetchMutation.MutationIndex.Some?) {
      return Failure(
          Types.MutationInvalidException(
            message := "Found a Mutation Index but no Mutation Commitment."
            + " The Key Store's Storage, for this Branch Key, has become corrupted."
            + " Recommend auditing the Branch Key's items for tampering."
            + " Recommend auditing access to the storage."
            + " To successfully start a new mutation, delete the Mutation Index."
            + " But know that the new mutation will fail if any corrupt items are encountered."
            + "\nBranch Key ID: " + input.Identifier + ";"
            + " Mutation Index UUID: " + fetchMutation.MutationIndex.value.UUID));
    }
    if (fetchMutation.MutationCommitment.None? && fetchMutation.MutationIndex.None?) {
      var no := Types.MutationInFlight.No(No := "No Mutation in-flight for " + input.Identifier + ".");
      return Success(Types.DescribeMutationOutput(MutationInFlight := no));
    }
    var Commitment := fetchMutation.MutationCommitment.value;
    var token := Types.MutationToken(
      Identifier := Commitment.Identifier,
      UUID := Commitment.UUID,
      CreateTime := Commitment.CreateTime);
    :- Need(
      fetchMutation.MutationIndex.Some?,
      Types.MutationInvalidException(
        message := "No Mutation Index exsists for this in-flight mutation of Branch Key ID " + input.Identifier + " ."
        // TODO-Mutations-GA :: More details on this error
      ));
    var Index := fetchMutation.MutationIndex.value;
    :- Need(
      // If custom storage is really bad
      Commitment.Identifier == Index.Identifier,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Branch Key IDs."
        + " The Storage implementation is wrong, or something terrible has happened to storage."
        + " Branch Key ID: " + input.Identifier + ";"
        + " Mutation Commitment Branch Key ID: " + Commitment.Identifier + ";"
        + " Mutation Index Branch Key ID: " + Index.Identifier + ";"
      ));
    :- Need(
      Commitment.UUID == Index.UUID,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
        + " Branch Key ID: " + input.Identifier + ";"
        + " Mutation Commitment UUID: " + Commitment.UUID + ";"
        + " Mutation Index UUID: " + Index.UUID + ";"
      ));
    var CommitmentAndIndex := StateStrucs.CommitmentAndIndex(
      Commitment := Commitment,
      Index := Index);
    assert CommitmentAndIndex.ValidState();
    // TODO-Mutations-GA :: Use System Key to Verify Commitment and Index
    var MutationToApply :- StateStrucs.DeserializeMutation(CommitmentAndIndex);
    var original := Types.MutableBranchKeyProperties(
      KmsArn := MutationToApply.Original.kmsArn,
      CustomEncryptionContext := MutationToApply.Original.customEncryptionContext
    );
    var terminal := Types.MutableBranchKeyProperties(
      KmsArn := MutationToApply.Terminal.kmsArn,
      CustomEncryptionContext := MutationToApply.Terminal.customEncryptionContext
    );
    var details := Types.MutationDetails(
      Original := original,
      Terminal := terminal,
      Input := MutationToApply.Input,
      SystemKey := "TrustStorage",
      CreateTime := MutationToApply.CreateTime,
      UUID := MutationToApply.UUID
    );
    var description := Types.MutationDescription(
      MutationDetails := details,
      MutationToken := token);
    var inFlight := Types.MutationInFlight.Yes(
      Yes := description);
    return Success(Types.DescribeMutationOutput(MutationInFlight := inFlight));
  }
}
