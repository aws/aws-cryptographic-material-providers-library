// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "MutationsConstants.dfy"
include "SystemKey/Handler.dfy"

module {:options "/functionSyntax:4" } DescribeMutation {
  import opened StandardLibrary
  import opened Wrappers

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import M_ErrorMessages = MutationsConstants.ErrorMessages
  import SystemKeyHandler = SystemKey.Handler
  import KMS = Com.Amazonaws.Kms
  import CommitmentAndIndex

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
      Commitment.Identifier == Index.Identifier && 0 < |Commitment.Identifier|,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Branch Key IDs."
        + " The Storage implementation is wrong, or something terrible has happened to storage."
        + " Branch Key ID: " + input.Identifier + ";"
        + " Mutation Commitment Branch Key ID: " + Commitment.Identifier + ";"
        + " Mutation Index Branch Key ID: " + Index.Identifier + ";"
      ));
    :- Need(
      Commitment.UUID == Index.UUID && 0 < |Commitment.UUID| ,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
        + " Branch Key ID: " + input.Identifier + ";"
        + " Mutation Commitment UUID: " + Commitment.UUID + ";"
        + " Mutation Index UUID: " + Index.UUID + ";"
      ));
    :- Need(
      CommitmentAndIndex.ValidCommitment?(Commitment),
      Types.MutationInvalidException(
        message := "Mutation Commitment read from Storage is invalid or corrupted."
        + " Recommend auditing the Branch Key's items for tampering."
        + " Recommend auditing access to the storage."
        + "\nBranch Key ID: " + input.Identifier + ";"
        + " Mutation Commitment UUID: " + Commitment.UUID));
    :- Need(
      CommitmentAndIndex.ValidIndex?(Index),
      Types.MutationInvalidException(
        message := "Mutation Index read from Storage is invalid or corrupted."
        + " Recommend auditing the Branch Key's items for tampering."
        + " Recommend auditing access to the storage."
        + "\nBranch Key ID: " + input.Identifier + ";"
        + " Mutation Index UUID: " + Index.UUID));
    var commitmentAndIndex := CommitmentAndIndex.CommitmentAndIndex(
      commitment := Commitment,
      index := Index);
    assert commitmentAndIndex.ValidIDs() && commitmentAndIndex.ValidUTF8();
    var MutationToApply :- StateStrucs.DeserializeMutation(commitmentAndIndex);
    var original := Types.MutableBranchKeyContext(
      KmsArn := MutationToApply.Original.kmsArn,
      EncryptionContext := MutationToApply.Original.customEncryptionContext,
      HierarchyVersion := MutationToApply.Original.hierarchyVersion
    );
    var terminal := Types.MutableBranchKeyContext(
      KmsArn := MutationToApply.Terminal.kmsArn,
      EncryptionContext := MutationToApply.Terminal.customEncryptionContext,
      HierarchyVersion := MutationToApply.Terminal.hierarchyVersion
    );
    var details := Types.MutationDetails(
      Original := original,
      Terminal := terminal,
      Input := MutationToApply.Input,
      SystemKey := SystemKeyDescription(Commitment),
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

  const TRUST_STORAGE_str := "Trust Storage"
  const KMS_SYM_ENC_str := "KMS Symmetric Encryption"
  const UNKOWN_str := "Unknown"

  function SystemKeyDescription(
    MutationCommitment: KeyStoreTypes.MutationCommitment
  ): (output: string)
    ensures
      && MutationCommitment.CiphertextBlob == SystemKeyHandler.TRUST_STORAGE_UTF8_BYTES
      ==>
        output == TRUST_STORAGE_str
    ensures
      && MutationCommitment.CiphertextBlob != SystemKeyHandler.TRUST_STORAGE_UTF8_BYTES
      && KMS.Types.IsValid_CiphertextType(MutationCommitment.CiphertextBlob)
      ==>
        output == KMS_SYM_ENC_str
    ensures
      && MutationCommitment.CiphertextBlob != SystemKeyHandler.TRUST_STORAGE_UTF8_BYTES
      && !KMS.Types.IsValid_CiphertextType(MutationCommitment.CiphertextBlob)
      ==>
        output == UNKOWN_str
  {
    if MutationCommitment.CiphertextBlob == SystemKeyHandler.TRUST_STORAGE_UTF8_BYTES
    then TRUST_STORAGE_str
    else
      if KMS.Types.IsValid_CiphertextType(MutationCommitment.CiphertextBlob)
      then KMS_SYM_ENC_str
      else UNKOWN_str
  }
}
