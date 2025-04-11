// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module CanonicalEncryptionContext {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
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
    :- Need(|encryptionContext| < UINT16_LIMIT,
            Types.AwsCryptographicMaterialProvidersException( message := "Encryption Context is too large" ));
    var keys := SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, UInt.UInt8Less);

    if |keys| == 0 then
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

  method EncryptionContextDigest(
    Crypto: AtomicPrimitives.AtomicPrimitivesClient,
    encryptionContext: Types.EncryptionContext
  )
    returns (output: Result<seq<uint8>, CanonizeDigestError>)
    requires Crypto.ValidState()
    modifies Crypto.Modifies
    ensures Crypto.ValidState()
    ensures output.Success? ==>
              && 0 < |Crypto.History.Digest|
              && Seq.Last(Crypto.History.Digest).output.Success?
              && var DigestInput := Seq.Last(Crypto.History.Digest).input;
              && var DigestOutput := Seq.Last(Crypto.History.Digest).output;
              && DigestInput.digestAlgorithm == AtomicPrimitives.Types.SHA_384
              && DigestOutput.value == output.value
              && |output.value| == 48 // 384 bits / 8 bits per byte == 48 bytes
  {
    var canonicalEC :- EncryptionContextToAAD(encryptionContext);

    var DigestInput := AtomicPrimitives.Types.DigestInput(
      digestAlgorithm := AtomicPrimitives.Types.SHA_384,
      message := canonicalEC
    );
    var maybeDigest := Crypto.Digest(DigestInput);
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
