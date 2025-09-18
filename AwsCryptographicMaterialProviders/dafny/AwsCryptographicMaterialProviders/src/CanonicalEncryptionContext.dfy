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

  //= aws-encryption-sdk-specification/framework/raw-aes-keyring.md#onencrypt
  //# The keyring MUST attempt to serialize the [encryption materials']
  //# (structures.md#encryption-materials) [encryption context]
  //# (structures.md#encryption-context-1) according to the
  //# [encryption context serialization specification](structures.md#serialization).

  // This implements the canonical Encryption Context serialization
  // (i.e. the serialization without the prepended total length)
  function method EncryptionContextToAAD(
    encryptionContext: Types.EncryptionContext
  ):
    (res: Result<seq<uint8>, Types.Error>)
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
                                :- Need(HasUint16Len(k) && HasUint16Len(v),
                                        Types.AwsCryptographicMaterialProvidersException( message := "Unable to serialize encryption context"));
                                Success(UInt16ToSeq(|k| as uint16) + k + UInt16ToSeq(|v| as uint16) + v);

      var pairsBytes :- Seq.MapWithResult(KeyIntoPairBytes, keys);

      // The final return should be the bytes of the pairs, prepended with the number of pairs
      var allBytes := UInt16ToSeq(|keys| as uint16) + Seq.Flatten(pairsBytes);
      Success(allBytes)
  }
}
