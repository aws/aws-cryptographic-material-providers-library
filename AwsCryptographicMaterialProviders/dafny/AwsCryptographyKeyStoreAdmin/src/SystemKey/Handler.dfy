// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../AwsCryptographyKeyStore/src/HierarchicalVersionUtils.dfy"
include "../../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../KmsUtils.dfy"
include "ContentHandler.dfy"
include "../../../AwsCryptographyKeyStore/src/Utf8Constants.dfy"
include "../CommitmentAndIndex.dfy"

/* Public methods for Signing and Verifying Mutation Items */
module {:options "/functionSyntax:4" } SystemKey.Handler {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened StandardLibrary.NeedError
  import UTF8
  import KMS = Com.Amazonaws.Kms
  import AtomicPrimitives
  import MPL = MaterialProviders
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KSTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KmsUtils
  import ContentHandler // = SystemKey.ContentHandler
  import HVUtils = HierarchicalVersionUtils
  import Structure
  import Utf8Constants
  import CommitmentAndIndex

  // type SystemKeyError = e: Types.Error | e.MutationVerificationException? witness *

  // TODO : Move type *ToSHA along with other constants to SystemKey.Constants
  type CommitmentContentToSHA =
    m: MPL.Types.EncryptionContext
    | m.Keys == {
                  Utf8Constants.CREATE_TIME_UTF8_BYTES,
                  Utf8Constants.ORIGINAL_UTF8_BYTES,
                  Utf8Constants.TERMINAL_UTF8_BYTES,
                  Utf8Constants.INPUT_UTF8_BYTES,
                  Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES
                } witness *

  type IndexContentToSHA =
    m: MPL.Types.EncryptionContext
    | m.Keys == {
                  Utf8Constants.CREATE_TIME_UTF8_BYTES,
                  Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES,
                  Utf8Constants.PAGE_INDEX_UTF8_BYTES
                } witness *

  function CommitmentWithSignature(
    MutationCommitment: KSTypes.MutationCommitment,
    Signature: seq<uint8>
  ): (output: KSTypes.MutationCommitment)
  {
    KSTypes.MutationCommitment(
      Identifier := MutationCommitment.Identifier,
      CreateTime := MutationCommitment.CreateTime,
      UUID := MutationCommitment.UUID,
      Original := MutationCommitment.Original,
      Terminal := MutationCommitment.Terminal,
      Input := MutationCommitment.Input,
      CiphertextBlob := Signature)
  }

  function IndexWithSignature(
    MutationIndex: KSTypes.MutationIndex,
    Signature: seq<uint8>
  ): (output: KSTypes.MutationIndex)
  {
    KSTypes.MutationIndex(
      Identifier := MutationIndex.Identifier,
      CreateTime := MutationIndex.CreateTime,
      UUID := MutationIndex.UUID,
      PageIndex := MutationIndex.PageIndex,
      CiphertextBlob := Signature)
  }

  // TODO: Abstract and consolidate these 4 methods
  method SignCommitment(
    MutationCommitment: KSTypes.MutationCommitment,
    InternalSystemKey: KmsUtils.InternalSystemKey
  ) returns (output: Result<KSTypes.MutationCommitment, Types.Error>)
    requires
      && InternalSystemKey.ValidState()
         // -= To be Signed, the binary fields must be the UTF8 bytes of their JSON rep
      && CommitmentAndIndex.ValidCommitment?(MutationCommitment)
    ensures InternalSystemKey.ValidState()
    modifies InternalSystemKey.Modifies
    ensures
      && output.Success?
      ==>
        && CommitmentAndIndex.ValidCommitment?(output.value)
        && 0 < |output.value.CiphertextBlob|
  {
    if (InternalSystemKey.TrustStorage?) {
      return Success(CommitmentWithSignature(MutationCommitment, Utf8Constants.TRUST_STORAGE_UTF8_BYTES));
    }

    if (!InternalSystemKey.KmsSymEnc?) {
      // This is impossible, but I want to make sure this logic is always sound
      return Failure(Types.UnsupportedFeatureException(message:="Only TrustStorage and KMS Symmetric Encryption are supported."));
    }
    var timeBytes? := UTF8.Encode(MutationCommitment.CreateTime);
    if (timeBytes?.Failure?) {
      var e := Types.MutationVerificationException(
        message:=
          "Could not sign Mutation Commitment due to Serialization error: "
          + timeBytes?.error);
      return Failure(e);
    }
    var contentToSHA: CommitmentContentToSHA := map[
      Utf8Constants.CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      Utf8Constants.ORIGINAL_UTF8_BYTES := MutationCommitment.Original,
      Utf8Constants.TERMINAL_UTF8_BYTES := MutationCommitment.Terminal,
      Utf8Constants.INPUT_UTF8_BYTES := MutationCommitment.Input,
      Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES := Utf8Constants.HIERARCHY_VERSION_VALUE_UTF8_BYTES
    ];
    var content := ContentHandler.Content(
      ContentToSHA := contentToSHA,
      PartitionValue := MutationCommitment.Identifier,
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := MutationCommitment.UUID);

    var crypto? := HVUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.MutationVerificationException(
        message :=
          "Could not sign Mutation Commitment due to local Cryptography error: "
          + AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error));
      return Failure(e);
    }

    var signInput := ContentHandler.SignInput(
      MaterialIdentifier := InternalSystemKey.KeyId,
      Content := content,
      KmsTuple := InternalSystemKey.Tuple,
      Crypto := crypto?.value);
    assert signInput.ValidState();

    var signature :- ContentHandler.SignContent(signInput);
    return Success(CommitmentWithSignature(MutationCommitment, signature));
  }

  method SignIndex(
    MutationIndex: KSTypes.MutationIndex,
    InternalSystemKey: KmsUtils.InternalSystemKey
  )
    returns (output: Result<KSTypes.MutationIndex, Types.Error>)
    requires
      && InternalSystemKey.ValidState()
         // -= To be Signed, the binary fields must be the UTF8 bytes of their JSON rep
      && CommitmentAndIndex.ValidIndex?(MutationIndex)
    modifies InternalSystemKey.Modifies
    ensures InternalSystemKey.ValidState()
    ensures
      && output.Success?
      ==>
        && CommitmentAndIndex.ValidIndex?(output.value)
        && 0 < |output.value.CiphertextBlob|
  {
    if (InternalSystemKey.TrustStorage?) {
      return Success(IndexWithSignature(MutationIndex, Utf8Constants.TRUST_STORAGE_UTF8_BYTES));
    }

    if (!InternalSystemKey.KmsSymEnc?) {
      // This is impossible, but I want to make sure this logic is always sound
      return Failure(Types.UnsupportedFeatureException(message:="Only TrustStorage and KMS Symmetric Encryption are supported."));
    }
    var timeBytes? := UTF8.Encode(MutationIndex.CreateTime);
    if (timeBytes?.Failure?) {
      var e := Types.MutationVerificationException(
        message:=
          "Could not sign Mutation Index due to Serialization error: "
          + timeBytes?.error);
      return Failure(e);
    }
    var contentToSHA: IndexContentToSHA := map[
      Utf8Constants.CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      Utf8Constants.PAGE_INDEX_UTF8_BYTES := MutationIndex.PageIndex,
      Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES := Utf8Constants.HIERARCHY_VERSION_VALUE_UTF8_BYTES
    ];
    var content := ContentHandler.Content(
      ContentToSHA := contentToSHA,
      PartitionValue := MutationIndex.Identifier,
      SortValue := Structure.MUTATION_INDEX_TYPE,
      UUIDValue := MutationIndex.UUID);

    var crypto? := HVUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.MutationVerificationException(
        message :=
          "Could not sign Mutation Index due to local Cryptography error: "
          + AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error));
      return Failure(e);
    }

    var signInput := ContentHandler.SignInput(
      MaterialIdentifier := InternalSystemKey.KeyId,
      Content := content,
      KmsTuple := InternalSystemKey.Tuple,
      Crypto := crypto?.value);

    var signature :- ContentHandler.SignContent(signInput);
    return Success(IndexWithSignature(MutationIndex, signature));
  }

  method VerifyCommitment(
    MutationCommitment: KSTypes.MutationCommitment,
    InternalSystemKey: KmsUtils.InternalSystemKey
  ) returns (output: Result<bool, Types.Error>)
    requires
      && InternalSystemKey.ValidState()
         // -= To be Verified, the binary fields must be the UTF8 bytes of their JSON rep
      && CommitmentAndIndex.ValidCommitment?(MutationCommitment)
    modifies InternalSystemKey.Modifies
    ensures InternalSystemKey.ValidState()
  {
    if (InternalSystemKey.TrustStorage?) {
      if (MutationCommitment.CiphertextBlob == Utf8Constants.TRUST_STORAGE_UTF8_BYTES) {
        return Success(true);
      }
      return Success(false);
    }

    if (!InternalSystemKey.KmsSymEnc?) {
      // This is impossible, but I want to make sure this logic is always sound
      return Failure(Types.UnsupportedFeatureException(message:="Only TrustStorage and KMS Symmetric Encryption are supported."));
    }
    :- Need(
      KMS.Types.IsValid_CiphertextType(MutationCommitment.CiphertextBlob),
      Types.KeyStoreAdminException(message:="Mutation Commitment's Signature (enc) is not a valid KMS Ciphertext.")
    );
    var signature: KMS.Types.CiphertextType := MutationCommitment.CiphertextBlob;
    var timeBytes? := UTF8.Encode(MutationCommitment.CreateTime);
    if (timeBytes?.Failure?) {
      var e := Types.MutationVerificationException(
        message:=
          "Could not sign Mutation Commitment due to Serialization error: "
          + timeBytes?.error);
      return Failure(e);
    }
    var contentToSHA: CommitmentContentToSHA := map[
      Utf8Constants.CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      Utf8Constants.ORIGINAL_UTF8_BYTES := MutationCommitment.Original,
      Utf8Constants.TERMINAL_UTF8_BYTES := MutationCommitment.Terminal,
      Utf8Constants.INPUT_UTF8_BYTES := MutationCommitment.Input,
      Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES := Utf8Constants.HIERARCHY_VERSION_VALUE_UTF8_BYTES
    ];
    var content := ContentHandler.Content(
      ContentToSHA := contentToSHA,
      PartitionValue := MutationCommitment.Identifier,
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := MutationCommitment.UUID);

    var crypto? := HVUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.MutationVerificationException(
        message :=
          "Could not Verify Mutation Commitment Signature due to local Cryptography error: "
          + AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error));
      return Failure(e);
    }

    var verifyInput := ContentHandler.VerifyInput(
      MaterialIdentifier := InternalSystemKey.KeyId,
      Content := content,
      CiphertextBlob := signature,
      KmsTuple := InternalSystemKey.Tuple,
      Crypto := crypto?.value);

    var valid :- ContentHandler.VerifyContent(verifyInput);
    return Success(valid);
  }

  method VerifyIndex(
    MutationIndex: KSTypes.MutationIndex,
    InternalSystemKey: KmsUtils.InternalSystemKey
  ) returns (output: Result<bool, Types.Error>)
    requires
      && InternalSystemKey.ValidState()
         // -= To be Verified, the binary fields must be the UTF8 bytes of their JSON rep
      && CommitmentAndIndex.ValidIndex?(MutationIndex)
    modifies InternalSystemKey.Modifies
    ensures InternalSystemKey.ValidState()
  {
    if (InternalSystemKey.TrustStorage?) {
      if (MutationIndex.CiphertextBlob == Utf8Constants.TRUST_STORAGE_UTF8_BYTES) {
        return Success(true);
      }
      return Success(false);
    }

    if (!InternalSystemKey.KmsSymEnc?) {
      // print "\n WARNING :: DID NOT VALIDATE SIGNAUTRE of MUTATION.\n";
      // return Success(true);
      // This is impossible, but I want to make sure this logic is always sound
      return Failure(Types.UnsupportedFeatureException(message:="Only TrustStorage and KMS Symmetric Encryption are supported."));
    }
    :- Need(
      KMS.Types.IsValid_CiphertextType(MutationIndex.CiphertextBlob),
      Types.KeyStoreAdminException(message:="Mutation Index's Signature (enc) is not a valid KMS Ciphertext.")
    );
    var signature: KMS.Types.CiphertextType := MutationIndex.CiphertextBlob;
    var timeBytes? := UTF8.Encode(MutationIndex.CreateTime);
    if (timeBytes?.Failure?) {
      var e := Types.MutationVerificationException(
        message:=
          "Could not sign Mutation Index due to Serialization error: "
          + timeBytes?.error);
      return Failure(e);
    }
    var contentToSHA: IndexContentToSHA := map[
      Utf8Constants.CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      Utf8Constants.PAGE_INDEX_UTF8_BYTES := MutationIndex.PageIndex,
      Utf8Constants.HIERARCHY_VERSION_UTF8_BYTES := Utf8Constants.HIERARCHY_VERSION_VALUE_UTF8_BYTES
    ];
    var content := ContentHandler.Content(
      ContentToSHA := contentToSHA,
      PartitionValue := MutationIndex.Identifier,
      SortValue := Structure.MUTATION_INDEX_TYPE,
      UUIDValue := MutationIndex.UUID);

    var crypto? := HVUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.MutationVerificationException(
        message :=
          "Could not verify Mutation Index Signature due to local Cryptography error: "
          + AtomicPrimitives.ErrorUtils.MessageOrUnknown(crypto?.error));
      return Failure(e);
    }

    var verifyInput := ContentHandler.VerifyInput(
      MaterialIdentifier := InternalSystemKey.KeyId,
      Content := content,
      CiphertextBlob := signature,
      KmsTuple := InternalSystemKey.Tuple,
      Crypto := crypto?.value);
    var valid :- ContentHandler.VerifyContent(verifyInput);
    return Success(valid);
  }
}
