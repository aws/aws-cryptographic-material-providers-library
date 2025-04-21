// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../AwsCryptographyKeyStore/src/HierarchicalVersionUtils.dfy"
include "../../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../KmsUtils.dfy"
include "ContentHandler.dfy"
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
  import CommitmentAndIndex

  // type SystemKeyError = e: Types.Error | e.MutationVerificationException? witness *

  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=Y3JlYXRlLXRpbWU&oenc=65001&oeol=CR
  const CREATE_TIME_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.KEY_CREATE_TIME)
  // var s := [99,114,101,97,116,101,45,116,105,109,101]
  // assert UTF8.ValidUTF8Range
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=b3JpZ2luYWw&oenc=65001&oeol=CR
  const ORIGINAL_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.M_ORIGINAL) // [111,114,105,103,105,110,97,108]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=dGVybWluYWw&oenc=65001&oeol=CR
  const TERMINAL_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.M_TERMINAL) //[116,101,114,109,105,110,97,108]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=aW5wdXQ&oenc=65001&oeol=CR
  const INPUT_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.M_INPUT) // [105,110,112,117,116]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=cGFnZUluZGV4&oenc=65001&oeol=CR
  const PAGE_INDEX_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.M_PAGE_INDEX) //[112,97,103,101,73,110,100,101,120]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=YnJhbmNoOk1VVEFUSU9OX0NPTU1JVE1FTlQ&oenc=65001&oeol=CR
  const COMMITMENT_TYPE_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.MUTATION_COMMITMENT_TYPE) // [98,114,97,110,99,104,58,77,85,84,65,84,73,79,78,95,67,79,77,77,73,84,77,69,78,84]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=YnJhbmNoOk1VVEFUSU9OX0lOREVY&oenc=65001&oeol=CR
  const INDEX_TYPE_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.MUTATION_INDEX_TYPE) //[98,114,97,110,99,104,58,77,85,84,65,84,73,79,78,95,73,78,68,69,88]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=dHJ1c3RTdG9yYWdl&oenc=65001&oeol=CR
  const TRUST_STORAGE_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii("trustStorage") // [116,114,117,115,116,83,116,111,114,97,103,101]
  const HIERARCHY_VERSION_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.HIERARCHY_VERSION) // [116,114,117,115,116,83,116,111,114,97,103,101]
  const HIERARCHY_VERSION_VALUE_UTF8_BYTES: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii(Structure.HIERARCHY_VERSION_VALUE)

  // TODO : Move type *ToSHA along with other constants to SystemKey.Constants
  type CommitmentContentToSHA =
    m: MPL.Types.EncryptionContext
    | m.Keys == {
                  CREATE_TIME_UTF8_BYTES,
                  ORIGINAL_UTF8_BYTES,
                  TERMINAL_UTF8_BYTES,
                  INPUT_UTF8_BYTES,
                  HIERARCHY_VERSION_UTF8_BYTES
                } witness *

  type IndexContentToSHA =
    m: MPL.Types.EncryptionContext
    | m.Keys == {
                  CREATE_TIME_UTF8_BYTES,
                  HIERARCHY_VERSION_UTF8_BYTES,
                  PAGE_INDEX_UTF8_BYTES
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
      return Success(CommitmentWithSignature(MutationCommitment, TRUST_STORAGE_UTF8_BYTES));
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
      CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      ORIGINAL_UTF8_BYTES := MutationCommitment.Original,
      TERMINAL_UTF8_BYTES := MutationCommitment.Terminal,
      INPUT_UTF8_BYTES := MutationCommitment.Input,
      HIERARCHY_VERSION_UTF8_BYTES := HIERARCHY_VERSION_VALUE_UTF8_BYTES
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
      return Success(IndexWithSignature(MutationIndex, TRUST_STORAGE_UTF8_BYTES));
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
      CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      PAGE_INDEX_UTF8_BYTES := MutationIndex.PageIndex,
      HIERARCHY_VERSION_UTF8_BYTES := HIERARCHY_VERSION_VALUE_UTF8_BYTES
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
      if (MutationCommitment.CiphertextBlob == TRUST_STORAGE_UTF8_BYTES) {
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
      CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      ORIGINAL_UTF8_BYTES := MutationCommitment.Original,
      TERMINAL_UTF8_BYTES := MutationCommitment.Terminal,
      INPUT_UTF8_BYTES := MutationCommitment.Input,
      HIERARCHY_VERSION_UTF8_BYTES := HIERARCHY_VERSION_VALUE_UTF8_BYTES
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
      if (MutationIndex.CiphertextBlob == TRUST_STORAGE_UTF8_BYTES) {
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
      CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      PAGE_INDEX_UTF8_BYTES := MutationIndex.PageIndex,
      HIERARCHY_VERSION_UTF8_BYTES := HIERARCHY_VERSION_VALUE_UTF8_BYTES
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
