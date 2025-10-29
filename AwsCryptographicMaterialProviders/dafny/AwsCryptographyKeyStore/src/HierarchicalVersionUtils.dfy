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

  function HasPrefix(key: string): bool {
    |key| >= |Structure.ENCRYPTION_CONTEXT_PREFIX| &&
    key[..|Structure.ENCRYPTION_CONTEXT_PREFIX|] == Structure.ENCRYPTION_CONTEXT_PREFIX
  }

  function RemovePrefix(key: string): string
    requires HasPrefix(key)
  {
    key[|Structure.ENCRYPTION_CONTEXT_PREFIX|..]
  }

  // checks that when we transform keys in the encryption context by removing the aws-crypto-ec: prefix (if present),
  // we don't end up with duplicate keys.
  predicate HasUniqueTransformedKeys?(branchKeyContext: Structure.EncryptionContextString)
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

  // Logically, HasUniqueTransformedKeys?(branchKeyContext) could be removed but verification does not understand that when
  // Structure.PrefixedEncryptionContext?(branchKeyContext - Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES) is true,
  // HasUniqueTransformedKeys?(branchKeyContext) should be true and verification fails on SelectKmsEncryptionContextForHv2 function
  // with "key expressions might be referring to the same value" on `map entry <- transformedContext :: entry.0 := entry.1`
  predicate IsValidHV2EC?(branchKeyContext: Structure.EncryptionContextString) {
    && Structure.PrefixedEncryptionContext?(branchKeyContext - Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES)
    && HasUniqueTransformedKeys?(branchKeyContext)
  }

  // HV-2 only sends the Branch Key's Encryption Context to KMS, as compared to the Branch Key Context
  // the Branch Key's Encryption Context can be divided into two groups
  // 1. those created by MPL consumers via the library, which are prefixed with aws-crypto-ec:
  // 2. those created by MPL consumers OUTSIDE of the library, which are not prefixed
  function SelectKmsEncryptionContextForHv2(
    branchKeyContext: Structure.EncryptionContextString
  ): (output: Structure.EncryptionContextString)
    requires Structure.BranchKeyContext?(branchKeyContext)
    requires IsValidHV2EC?(branchKeyContext)
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-encryption-context
    //= type=implication
    //# If the `hierarchy-version` is v2, AWS KMS encryption context MUST be the [encryption context from authenticated branch key context](#encryption-context-from-authenticated-branch-key-context) without any transformation.
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

  method CreateBKCDigest (
    branchKeyContext: map<string, string>,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (output: Result<seq<uint8>, BKCDigestError>)
    requires crypto.ValidState() && Structure.BranchKeyContext?(branchKeyContext)
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures Structure.EncodeEncryptionContext(branchKeyContext).Failure? ==> output.Failure?
    ensures output.Success? ==>
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
