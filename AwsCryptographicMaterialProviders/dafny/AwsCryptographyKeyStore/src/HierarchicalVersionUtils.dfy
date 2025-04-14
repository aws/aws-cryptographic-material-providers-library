// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"
include "KeyStoreErrorMessages.dfy"

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

  method ProvideCryptoClient(
    Crypto?: Option<AtomicPrimitives.AtomicPrimitivesClient> := None
  )
    returns (output: Result<AtomicPrimitives.AtomicPrimitivesClient, AtomicPrimitives.Types.Error>)
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
      Crypto :- AtomicPrimitives.AtomicPrimitives();
    } else {
      Crypto := Crypto?.value;
    }
    // If the customer gave us the Crypto Client, it is fresh
    // If we create the Crypto Client, it is fresh
    assume {:axiom} fresh(Crypto) && fresh(Crypto.Modifies);
    return Success(Crypto);
  }

  // TODO-HV2: Create a known answer test for CreateBKCDigest. See https://github.com/aws/aws-cryptographic-material-providers-library/commit/09a84e15b5d7311b0418180ddda69dc7314b320e
  method CreateBKCDigest (
    branchKeyContext: map<string, string>,
    cryptoClient: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (output: Result<seq<uint8>, BKCDigestError>)
    requires Structure.BranchKeyContext?(branchKeyContext)
    requires cryptoClient.ValidState()
    modifies cryptoClient.Modifies
    ensures cryptoClient.ValidState()
    ensures output.Success? ==>
              && 0 < |cryptoClient.History.Digest|
              && Seq.Last(cryptoClient.History.Digest).output.Success?
              && var DigestInput := Seq.Last(cryptoClient.History.Digest).input;
              && var DigestOutput := Seq.Last(cryptoClient.History.Digest).output;
              && DigestInput.digestAlgorithm == AtomicPrimitives.Types.SHA_384
              && DigestOutput.value == output.value
              && |output.value| == Structure.BKC_DIGEST_LENGTH as int
  {
    var utf8BKContext :- EncodeEncryptionContext(branchKeyContext).MapFailure(WrapStringToError);
    var digestResult := CanonicalEncryptionContext.EncryptionContextDigest(cryptoClient, utf8BKContext);
    if (digestResult.Failure?) {
      var error: Types.Error;
      error := match digestResult.error {
        case AwsCryptographyPrimitives(e) =>
          // we cannot reliably serialize a Primitive error without work
          Types.KeyStoreException(message:="Could not SHA-384 Content.")
        case AwsCryptographicMaterialProvidersException(e) =>
          Types.KeyStoreException(message:="Could not SHA-384 Content. " + e)
      };
      return Failure(error);
    }
    return Success(digestResult.value);
  }

  function WrapStringToError(e: string)
    :(ret: Types.Error)
  {
    Types.KeyStoreException( message := e )
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

  // HV-2 only sends the Branch Key's Encryption Context to KMS, as compared to the Branch Key Context
  // the Branch Key's Encryption Context can be divided into two groups
  // 1. those created by MPL consumers via the library, which are prefixed with aws-crypto-ec:
  // 2. those created by MPL consumers OUTSIDE of the library, which are not prefixed
  function SelectKmsEncryptionContextForHv2(
    branchKeyContext: Types.EncryptionContextString
  ): (output: Types.EncryptionContextString)
    requires Structure.BranchKeyContext?(branchKeyContext)
    // TODO-HV-2-M2: Revisit this implementation to handle scenarios where removing prefix results in conflicting keys.
    requires HasUniqueTransformedKeys?(branchKeyContext)
    ensures forall k <- output ::
              exists originalKey ::
                && originalKey in branchKeyContext
                && (HasPrefix(originalKey) ==> k == RemovePrefix(originalKey))
                && (!HasPrefix(originalKey) ==> k == originalKey)
                && originalKey !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
  {
    var transformedContext :=
      set k <- branchKeyContext.Keys
          | k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
        :: (
             if HasPrefix(k) then RemovePrefix(k) else k,  // transformed key
             branchKeyContext[k]                           // original value
           );
    map entry <- transformedContext :: entry.0 := entry.1
  }

  predicate HasUniqueTransformedKeys?(branchKeyContext: Types.EncryptionContextString)
  {
    forall k1, k2 :: k1 in branchKeyContext && k2 in branchKeyContext ==>
                       (
                         // If transformed keys are equal
                         (if HasPrefix(k1) then RemovePrefix(k1) else k1) ==
                         (if HasPrefix(k2) then RemovePrefix(k2) else k2)
                         ==>
                           // Then original keys must be equal
                           k1 == k2
                       )
  }

  function HasPrefix(key: string): bool {
    |key| > |Structure.ENCRYPTION_CONTEXT_PREFIX| &&
    key[..|Structure.ENCRYPTION_CONTEXT_PREFIX|] == Structure.ENCRYPTION_CONTEXT_PREFIX
  }

  function RemovePrefix(key: string): string
    requires HasPrefix(key)
  {
    key[|Structure.ENCRYPTION_CONTEXT_PREFIX|..]
  }

  // Helper function to encode encryption context from string map to UTF8 bytes map
  function EncodeEncryptionContext(
    input: Types.EncryptionContextString
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
  ): (output: Result<Types.EncryptionContextString, string>)
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
