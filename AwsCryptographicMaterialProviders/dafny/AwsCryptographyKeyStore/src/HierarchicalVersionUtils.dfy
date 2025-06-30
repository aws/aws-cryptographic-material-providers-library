// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"
  // include "KeyStoreErrorMessages.dfy"

module {:options "/functionSyntax:4" } HierarchicalVersionUtils {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened Seq
  import AtomicPrimitives
  import Structure
  import UTF8
  import CanonicalEncryptionContext
  import Types = AwsCryptographyKeyStoreTypes
  import KeyStoreErrorMessages

  type PlainTextTuple = s: seq<uint8> | |s| == 80 witness *
  type BKCDigestError = e: Types.Error | (e.KeyStoreException? ) witness *

  function WrapStringToError(e: string)
    :(ret: Types.Error)
  {
    Types.KeyStoreException( message := e )
  }

  method ProvideCryptoClient(
    Crypto?: Option<AtomicPrimitives.AtomicPrimitivesClient> := None
  )
    returns (output: Result<AtomicPrimitives.AtomicPrimitivesClient, Types.Error>)
    requires Crypto?.Some? ==> Crypto?.value.ValidState()
    modifies (if Crypto?.Some? then Crypto?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var Crypto: AtomicPrimitives.AtomicPrimitivesClient;
    if (Crypto?.None?) {
      var Crypto? := AtomicPrimitives.AtomicPrimitives();
      Crypto :- Crypto?.MapFailure(e => Types.KeyStoreException(message := "Failed to create primitives client"));
    } else {
      Crypto := Crypto?.value;
    }
    // If the customer gave us the Crypto Client, it is fresh
    // If we create the Crypto Client, it is fresh
    assume {:axiom} fresh(Crypto) && fresh(Crypto.Modifies);
    return Success(Crypto);
  }

  method CreateBKCDigest (
    branchKeyContext: map<string, string>,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (output: Result<seq<uint8>, BKCDigestError>)
    requires crypto.ValidState() && Structure.BranchKeyContext?(branchKeyContext)
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures Structure.EncodeEncryptionContext(branchKeyContext).Failure? ==> output.Failure?
    ensures
      && output.Success?
      ==>
        // Note there is no proof that the input to the digest
        // is utf8BKContext; dafny could not handle that
        && |crypto.History.Digest| == |old(crypto.History.Digest)| + 1
        && old(crypto.History.Digest) < crypto.History.Digest
        && var digestEvent := Seq.Last(crypto.History.Digest);
        && digestEvent.output.Success?
        && digestEvent.output.value == output.value
        && |output.value| == Structure.BKC_DIGEST_LENGTH as int
        && Structure.EncodeEncryptionContext(branchKeyContext).Success?
        && var utf8BKContext := Structure.EncodeEncryptionContext(branchKeyContext).value;
        && CanonicalEncryptionContext.EncryptionContextToAAD(utf8BKContext).Success?
        && var canonicalEC := CanonicalEncryptionContext.EncryptionContextToAAD(utf8BKContext).value;
        && AtomicPrimitives.Types.DigestInput(
          digestAlgorithm := AtomicPrimitives.Types.SHA_384,
          message := canonicalEC
        ) == digestEvent.input
  {
    var utf8BKContext :- Structure.EncodeEncryptionContext(branchKeyContext).MapFailure(WrapStringToError);
    var digestResult? := CanonicalEncryptionContext.EncryptionContextDigest(crypto, utf8BKContext);
    var digestResult :- digestResult?.MapFailure(e => Types.KeyStoreException(message:=e));
    return Success(digestResult);
  }

  // unpacks PlainTextTuple (i.e (BKC_DIGEST + AES_256 key)) to return BKC_DIGEST, AES_256 key
  function UnpackPlainTextTuple (
    plainTextTuple: PlainTextTuple
  ) : (Result:(seq<uint8>, seq<uint8>))
    requires |plainTextTuple| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    ensures |Result.0| == Structure.BKC_DIGEST_LENGTH as int
    ensures |Result.1| == Structure.AES_256_LENGTH as int
    ensures Result.0 == plainTextTuple[..Structure.BKC_DIGEST_LENGTH]
    ensures Result.1 == plainTextTuple[Structure.BKC_DIGEST_LENGTH..]
  {
    (plainTextTuple[..Structure.BKC_DIGEST_LENGTH], plainTextTuple[Structure.BKC_DIGEST_LENGTH..])
  }

  // packs BKCDigest and AES 256 Key into (bkcDigest + aes256Key)
  function PackPlainTextTuple (
    bkcDigest: seq<uint8>, aes256Key: seq<uint8>
  ) : (Result:(PlainTextTuple))
    requires |bkcDigest| == Structure.BKC_DIGEST_LENGTH as int
    requires |aes256Key| == Structure.AES_256_LENGTH as int
    ensures |Result| as uint8 == |bkcDigest| as uint8 + |aes256Key| as uint8
    ensures Result[..Structure.BKC_DIGEST_LENGTH] == bkcDigest
    ensures Result[Structure.BKC_DIGEST_LENGTH..] == aes256Key
    ensures Result == bkcDigest + aes256Key
  {
    (bkcDigest + aes256Key)
  }

  // Helper function to encode encryption context from string map to UTF8 bytes map
  function EncodeEncryptionContext(
    input: Structure.EncryptionContextString
  ): (output: Result<Types.EncryptionContext, string>)
    ensures output.Success? ==> |output.value| == |input| // Output map size equals input map size
    ensures output.Failure? ==> output.error == "Unable to encode string"
  {
    var encodedEncryptionContext
      := set k <- input
           ::
             (UTF8.Encode(k), UTF8.Encode(input[k]), k);

    if (forall i <- encodedEncryptionContext
          ::
            && i.0.Success?
            && i.1.Success?)
    then
      var resultMap := map i <- encodedEncryptionContext :: i.0.value := i.1.value;
      if |resultMap| == |input| then
        Success(resultMap)
      else
        Failure("Unable to encode string")
    else
      Failure("Unable to encode string")
  }

  // Helper function to decode encryption context from UTF8 bytes map to string map
  function DecodeEncryptionContext(
    input: Types.EncryptionContext
  ): (output: Result<Structure.EncryptionContextString, string>)
    ensures output.Success? ==> |output.value| == |input| // Output map size equals input map size
    ensures output.Failure? ==> output.error == "Unable to decode string"
  {
    var decodedEncryptionContext
      := set k <- input
           ::
             (UTF8.Decode(k), UTF8.Decode(input[k]), k);

    if (forall i <- decodedEncryptionContext
          ::
            && i.0.Success?
            && i.1.Success?
               // TODO-UTF8-OPTIMIZATION :: It is silly to Decode and then Encode
            && var decoded := UTF8.Encode(i.0.value);
            && decoded.Success?
            && i.2 == decoded.value)
    then
      var resultMap := map i <- decodedEncryptionContext :: i.0.value := i.1.value;
      if |resultMap| == |input| then
        Success(resultMap)
      else
        Failure("Unable to decode string")
    else
      Failure("Unable to decode string")
  }

}
