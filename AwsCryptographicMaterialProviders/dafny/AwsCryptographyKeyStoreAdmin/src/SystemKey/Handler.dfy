// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../KmsUtils.dfy"
include "ContentHandler.dfy"

/* Public methods for Signing and Verifying Mutation Items */
module {:options "/functionSyntax:4" } SystemKey.Handler {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened StandardLibrary.NeedError
  import UTF8
  import KMS = Com.Amazonaws.Kms
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KSTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KmsUtils
  import AtomicPrimitives
  import ContentHandler // = SystemKey.ContentHandler
  import Structure
  import MPL = MaterialProviders

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

  lemma UTF8BytesAreValid()
    ensures
      && UTF8.IsASCIIString(Structure.KEY_CREATE_TIME)
      && UTF8.EncodeAscii(Structure.KEY_CREATE_TIME) == CREATE_TIME_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(CREATE_TIME_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.M_ORIGINAL)
      && UTF8.EncodeAscii(Structure.M_ORIGINAL) == ORIGINAL_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(ORIGINAL_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.M_TERMINAL)
      && UTF8.EncodeAscii(Structure.M_TERMINAL) == TERMINAL_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(TERMINAL_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.M_INPUT)
      && UTF8.EncodeAscii(Structure.M_INPUT) == INPUT_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(INPUT_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.M_PAGE_INDEX)
      && UTF8.EncodeAscii(Structure.M_PAGE_INDEX) == PAGE_INDEX_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(PAGE_INDEX_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.MUTATION_COMMITMENT_TYPE)
      && UTF8.EncodeAscii(Structure.MUTATION_COMMITMENT_TYPE) == COMMITMENT_TYPE_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(COMMITMENT_TYPE_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString(Structure.MUTATION_INDEX_TYPE)
      && UTF8.EncodeAscii(Structure.MUTATION_INDEX_TYPE) == INDEX_TYPE_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(INDEX_TYPE_UTF8_BYTES)
    ensures
      && UTF8.IsASCIIString("trustStorage")
      && UTF8.EncodeAscii("trustStorage") == TRUST_STORAGE_UTF8_BYTES
      ==> UTF8.ValidUTF8Seq(TRUST_STORAGE_UTF8_BYTES)
  {}

  method SignCommitment(
    MutationCommitment: KSTypes.MutationCommitment,
    InternalSystemKey: KmsUtils.InternalSystemKey
  )
    returns (output: Result<KSTypes.MutationCommitment, Types.Error>)
    requires InternalSystemKey.ValidState()
    ensures InternalSystemKey.ValidState()
    modifies InternalSystemKey.Modifies
    // -= To be Signed, the binary fields must be the UTF8 bytes of their JSON rep
    requires
      && UTF8.ValidUTF8Seq(MutationCommitment.Original)
      && UTF8.ValidUTF8Seq(MutationCommitment.Terminal)
      && UTF8.ValidUTF8Seq(MutationCommitment.Input)
      && 0 < |MutationCommitment.UUID|
      && 0 < |MutationCommitment.Identifier|
    // && 0 < |MutationCommitment.UUID|
    // ensures output.Failure? ==> output.error.MutationVerificationException?
  {
    if (InternalSystemKey.TrustStorage?) {
      return Success(CommitmentWithSignature(MutationCommitment, TRUST_STORAGE_UTF8_BYTES));
    }

    var timeBytes? := UTF8.Encode(MutationCommitment.CreateTime);
    if (timeBytes?.Failure?) {
      var e := Types.MutationVerificationException(
        message:=
          "Could not sign Mutation Commitment due to Serialization error: "
          + timeBytes?.error);
      return Failure(e);
    }
    var contentToSHA: MPL.Types.EncryptionContext := map[
      CREATE_TIME_UTF8_BYTES := timeBytes?.value,
      ORIGINAL_UTF8_BYTES := MutationCommitment.Original,
      TERMINAL_UTF8_BYTES := MutationCommitment.Terminal,
      INPUT_UTF8_BYTES := MutationCommitment.Input
    ];
    assert forall item | item in contentToSHA.Items ::
        && UTF8.ValidUTF8Seq(item.0) && UTF8.ValidUTF8Seq(item.1)
    by {
      assert
        && UTF8.IsASCIIString(Structure.KEY_CREATE_TIME)
        && UTF8.EncodeAscii(Structure.KEY_CREATE_TIME) == CREATE_TIME_UTF8_BYTES
        && UTF8.IsASCIIString(Structure.M_ORIGINAL)
        && UTF8.EncodeAscii(Structure.M_ORIGINAL) == ORIGINAL_UTF8_BYTES
        && UTF8.IsASCIIString(Structure.M_TERMINAL)
        && UTF8.EncodeAscii(Structure.M_TERMINAL) == TERMINAL_UTF8_BYTES
        && UTF8.IsASCIIString(Structure.M_INPUT)
        && UTF8.EncodeAscii(Structure.M_INPUT) == INPUT_UTF8_BYTES;
    }
    var content := ContentHandler.Content(
      ContentToSHA := contentToSHA,
      PartitionValue := MutationCommitment.Identifier,
      SortValue := Structure.MUTATION_COMMITMENT_TYPE,
      UUIDValue := MutationCommitment.UUID);
    assert content.ValidState();

    var crypto? := ContentHandler.ProvideCryptoClient();
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
}
