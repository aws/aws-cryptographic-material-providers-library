// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module CanonicalEncryptionContext {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened Wrappers
  import Seq
  import SortedSets
  import AtomicPrimitives

  // Let's us refine the error across modules
  type CanonizeError = e: Types.Error | e.AwsCryptographicMaterialProvidersException? witness *
  type CanonizeDigestError = e: Types.Error | (e.AwsCryptographicMaterialProvidersException? || e.AwsCryptographyPrimitives?) witness *

  //= aws-encryption-sdk-specification/framework/raw-aes-keyring.md#onencrypt
  //# The keyring MUST attempt to serialize the [encryption materials']
  //# (structures.md#encryption-materials) [encryption context]
  //# (structures.md#encryption-context-1) according to the
  //# [encryption context serialization specification](structures.md#serialization).

  // This implements the canonical Encryption Context serialization
  // (i.e. the serialization without the prepended total length)
  function method {:vcs_split_on_every_assert} EncryptionContextToAAD(
    encryptionContext: Types.EncryptionContext
  ):
    (res: Result<seq<uint8>, CanonizeError>)
  {
    MapIsSafeBecauseItIsInMemory(encryptionContext);
    :- Need(|encryptionContext| as uint64 < UINT16_LIMIT as uint64,
            Types.AwsCryptographicMaterialProvidersException( message := "Encryption Context is too large" ));
    var keys := SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, UInt.UInt8Less);

    if |keys| as uint16 == 0 then
      Success([])
    else
      var KeyIntoPairBytes := k
                              requires k in encryptionContext
                              =>
                                var v := encryptionContext[k];
                                IntoPairBytes(k, v);
      var pairsBytesResult := Seq.MapWithResult(KeyIntoPairBytes, keys);
      if pairsBytesResult.Failure? then
        assert pairsBytesResult.error.AwsCryptographicMaterialProvidersException?;
        Failure(pairsBytesResult.error)
      else
        // The final return should be the bytes of the pairs, prepended with the number of pairs
        var allBytes := UInt16ToSeq(|keys| as uint16) + Seq.Flatten(pairsBytesResult.value);
        Success(allBytes)
  }

  function method IntoPairBytes(
    k: seq<uint8>,
    v: seq<uint8>
  ): (output: Result<seq<uint8>, CanonizeError>)
    ensures output.Success? ==> HasUint16Len(k) && HasUint16Len(v)
    ensures (!HasUint16Len(k) || !HasUint16Len(v)) ==> output.Failure?
  {
    if HasUint16Len(k) && HasUint16Len(v)
    then Success(UInt16ToSeq(|k| as uint16) + k + UInt16ToSeq(|v| as uint16) + v)
    else Failure(Types.AwsCryptographicMaterialProvidersException( message := "Unable to serialize encryption context"))
  }

  // @texastony had a dream of using this predicates to
  // remove duplicate code in HVUtils
  // and CreateKeyHV2.dfy but has given up on the dream for now.
  // TODO-HV-2-FOLLOW : Complete Dream or Kill this
  // predicate digestSHA384ContextPostConditions(
  //   nameonly content: seq<uint8>,
  //   nameonly digest: seq<uint8>,
  //   nameonly digestEvent: AtomicPrimitives.Types.DafnyCallEvent<AtomicPrimitives.Types.DigestInput, Result<seq<uint8>, AtomicPrimitives.Types.Error>>
  // )
  // {
  //   var input := digestEvent.input;
  //   var output := digestEvent.output;
  //   && input.digestAlgorithm == AtomicPrimitives.Types.SHA_384
  //   && input.message == content
  //   && output.Success?
  //   ==>
  //     && |output.value| == 48 // 384 bits / 8 bits per byte == 48 bytes
  //     && output.value == digest
  // }

  // twostate predicate encryptionContextDigestPostConditions(
  //   crypto: AtomicPrimitives.AtomicPrimitivesClient,
  //   encryptionContext: Types.EncryptionContext,
  //   digest: seq<uint8>
  // )
  //   reads crypto.History
  // {
  //   && var content? := EncryptionContextToAAD(encryptionContext);
  //   && content?.Success?
  //   && |crypto.History.Digest| == |old(crypto.History.Digest)| + 1
  //   && var digestEvent := Seq.Last(crypto.History.Digest);
  //   && digestSHA384ContextPostConditions(
  //     content := content?.value,
  //     digest := digest,
  //     digestEvent := digestEvent)
  // }

  method EncryptionContextDigest(
    crypto: AtomicPrimitives.AtomicPrimitivesClient,
    encryptionContext: Types.EncryptionContext
  )
    returns (output: Result<seq<uint8>, CanonizeDigestError>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    // We tried to collapse all of this post condition into a common predicate.
    // We failed; we will have to copy and paste it.
    // @texastony thinks reason is that is very difficult to keep track of the input.
    ensures
      && output.Success?
      ==>
        && var content? := EncryptionContextToAAD(encryptionContext);
        && content?.Success?
        && |crypto.History.Digest| == |old(crypto.History.Digest)| + 1
        && var digestEvent := Seq.Last(crypto.History.Digest);
        && digestEvent.input.digestAlgorithm == AtomicPrimitives.Types.SHA_384
        && digestEvent.input.message == content?.value
        && digestEvent.output.Success?
        && |digestEvent.output.value| == 48 // 384 bits / 8 bits per byte == 48 bytes
        && digestEvent.output.value == output.value
  {
    var canonicalEC :- EncryptionContextToAAD(encryptionContext);

    var DigestInput := AtomicPrimitives.Types.DigestInput(
      digestAlgorithm := AtomicPrimitives.Types.SHA_384,
      message := canonicalEC
    );
    var maybeDigest := crypto.Digest(DigestInput);
    var digest :- maybeDigest.MapFailure(e => Types.AwsCryptographyPrimitives(e));

    // The digest is not truncated.
    // There is an impact on the key size.
    // See: https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html
    // This is not safe to do for 1024 keys,
    // but AWS KMS does not support these keys.
    // Further we use SHA_384 to save a little on size
    // and avoid even the possiblity of length extenstion.
    // Though length extension does not matter in this situation,
    // because a decryptor already has access to the key.
    return Success(digest);
  }
}
