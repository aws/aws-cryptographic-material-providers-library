// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Materials.dfy"
include "../AlgorithmSuites.dfy"
include "../CMM.dfy"
include "../Defaults.dfy"
include "../Commitment.dfy"
include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../CanonicalEncryptionContext.dfy"

module {:options "/functionSyntax:4" } CachingCMM  {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Materials
  import CMM
  import UTF8
  import Types = AwsCryptographyMaterialProvidersTypes
  import Seq

  import Time
  import Seq.MergeSort
  import Sorting
  import CanonicalEncryptionContext
  import AlgorithmSuites
  import BoundedInts
  import Aws.Cryptography.Primitives

  class CachingCMM
    extends CMM.VerifiableInterface
  {
    const underlyingCMM: Types.ICryptographicMaterialsManager
    const cache: Types.ICryptographicMaterialsCache
    const cryptoPrimitives: Primitives.AtomicPrimitivesClient
    //= aws-encryption-sdk-specification/framework/caching-cmm.md#partition-id
    //= type=implication
    //# The Partition ID MUST NOT be changed after initialization.
    const partitionKeyDigest: seq<uint8>
    //= aws-encryption-sdk-specification/framework/caching-cmm.md#cache-limit-ttl
    //= type=implication
    //# The Caching CMM MUST set a time-to-live (TTL) for data keys in the CMC.
    const ttlSeconds: Types.PositiveInteger
    //= aws-encryption-sdk-specification/framework/caching-cmm.md#limit-bytes
    //= type=implication
    //# The maximum number of bytes that MAY be encrypted by a single data key.
    const limitBytes: Types.PositiveLong
    //= aws-encryption-sdk-specification/framework/caching-cmm.md#limit-messages
    //= type=implication
    //# The maximum number of messages that MAY be encrypted by a single data key.
    const limitMessages: BoundedInts.uint32

    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && underlyingCMM.ValidState()
      && cryptoPrimitives.ValidState()
      && underlyingCMM.Modifies <= Modifies
      && cryptoPrimitives.Modifies <= Modifies
      && underlyingCMM.Modifies
      !! cryptoPrimitives.Modifies
      !! {History}
      && limitBytes as int <  0x8000_0000_0000_0000 // 2^63-1
      && limitMessages as int < BoundedInts.TWO_TO_THE_32
    }

    constructor (
      nameonly inputCMM: Types.ICryptographicMaterialsManager,
      nameonly inputCryptoPrimitives: Primitives.AtomicPrimitivesClient,
      nameonly inputCache: Types.ICryptographicMaterialsCache,
      nameonly inputPartitionKeyDigest: seq<uint8>,
      nameonly ghost inputPartitionKey: seq<uint8>,
      nameonly inputTtlSeconds: Types.PositiveInteger,
      nameonly inputLimitBytes: Types.PositiveLong,
      nameonly inputLimitMessages: Types.PositiveInteger
    )
      requires inputCMM.ValidState()
      requires inputCryptoPrimitives.ValidState()
      requires inputCMM.Modifies !! inputCryptoPrimitives.Modifies
      requires inputLimitBytes <=  (0x8000_0000_0000_0000 - 1) as int64

      // This is an optimization.
      // Here we prove that the value we store in partitionKeyDigest
      // is the required digest.

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#decryption-materials
      //= type=implication
      //# 1.  The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#encryption-materials-with-algorithm-suite
      //= type=implication
      //# 1.  The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#encryption-materials-without-algorithm-suite
      //= type=implication
      //# 1. The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID
      requires
        && 0 < |inputCryptoPrimitives.History.Digest|
        && var digest := Seq.Last(inputCryptoPrimitives.History.Digest);
        && digest.input
           == Primitives.Types.DigestInput(
                digestAlgorithm := Primitives.Types.SHA_512,
                message := inputPartitionKey
              )
        && digest.output.Success?
        && digest.output.value == inputPartitionKeyDigest
      ensures partitionKeyDigest == inputPartitionKeyDigest

      ensures
        && ValidState()
        && fresh(this)
        && fresh(History)
        && fresh(Modifies - underlyingCMM.Modifies - cryptoPrimitives.Modifies - cache.Modifies)
      ensures Modifies == { History } + underlyingCMM.Modifies + cryptoPrimitives.Modifies + cache.Modifies
      ensures
        && underlyingCMM == inputCMM
        && cache == inputCache
        && cryptoPrimitives == inputCryptoPrimitives
        && partitionKeyDigest == inputPartitionKeyDigest
        && ttlSeconds == inputTtlSeconds
        && limitBytes == inputLimitBytes
        && limitMessages == inputLimitMessages as BoundedInts.uint32
    {
      underlyingCMM := inputCMM;
      cache := inputCache;
      cryptoPrimitives := inputCryptoPrimitives;
      partitionKeyDigest := inputPartitionKeyDigest;
      ttlSeconds := inputTtlSeconds;
      limitBytes := inputLimitBytes;
      limitMessages := inputLimitMessages as BoundedInts.uint32;

      History := new Types.ICryptographicMaterialsManagerCallHistory();
      Modifies := { History } + inputCMM.Modifies + inputCryptoPrimitives.Modifies + inputCache.Modifies;
    }

    ghost predicate GetEncryptionMaterialsEnsuresPublicly(input: Types.GetEncryptionMaterialsInput, output: Result<Types.GetEncryptionMaterialsOutput, Types.Error>)
    {true}

    method GetEncryptionMaterials'(
      input: Types.GetEncryptionMaterialsInput
    )
      returns (output: Result<Types.GetEncryptionMaterialsOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures ValidState()
      ensures GetEncryptionMaterialsEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures output.Success?
              ==>
                && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.encryptionMaterials)
      ensures output.Success?
              ==>
                && CMM.RequiredEncryptionContextKeys?(input.requiredEncryptionContextKeys, output.value.encryptionMaterials)

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
      //= type=implication
      //# If the [Max Plaintext Length on the encryption materials request](./cmm-interface.md#encryption-materials-request) is not set
      //# the caching CMM MUST obtain the encryption materials
      //# by making a call to the underlying CMM's [Get Encryption Materials](cmm-interface.md#get-encryption-materials) function.
      ensures
        output.Success? ==>
          || input.maxPlaintextLength.None?
          || (input.maxPlaintextLength.value < 0)
          || (limitBytes < input.maxPlaintextLength.value)
          ==>
            && |old(underlyingCMM.History.GetEncryptionMaterials)| + 1 == |underlyingCMM.History.GetEncryptionMaterials|
            && input == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).input
            && output == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).output

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
      //= type=implication
      //# If the [algorithm suite](algorithm-suites.md) requested contains a [Identity KDF](algorithm-suites.md#identity-kdf),
      //# the caching CMM MUST obtain the encryption materials
      //# by making a call to the underlying CMM's [Get Encryption Materials](cmm-interface.md#get-encryption-materials) function.
      ensures
        && output.Success?
        && (input.algorithmSuiteId.Some? && AlgorithmSuites.GetSuite(input.algorithmSuiteId.value).kdf.IDENTITY?)
        ==>
          && |old(underlyingCMM.History.GetEncryptionMaterials)| + 1 == |underlyingCMM.History.GetEncryptionMaterials|
          && input == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).input
          && output == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).output

      ensures
        && !BypassCache(input, limitBytes)
        && output.Success?
        ==>
          && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + 2
          && var ecDigestRequest := Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest));
          && var cacheEntryIdentifierRequest := Seq.Last(cryptoPrimitives.History.Digest);
          && ecDigestRequest.output.Success?
          && cacheEntryIdentifierRequest.output.Success?
          && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
          && ecDigestRequest.input
             == Primitives.Types.DigestInput(
                  digestAlgorithm := Primitives.Types.SHA_512,
                  message := CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).value
                )

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#appendix-a-cache-entry-identifier-formulas
          //= type=implication
          //# When accessing the underlying CMC,
          //# the caching CMM MUST use the formulas specified in this appendix
          //# in order to compute the [cache entry identifier](cryptographic-materials-cache.md#cache-identifier).
          && (if input.algorithmSuiteId.Some? then
                //= aws-encryption-sdk-specification/framework/caching-cmm.md#encryption-materials-with-algorithm-suite
                //= type=implication
                //# If the Get Encryption Materials request does specify an algorithm suite,
                //# then the cache entry identifier MUST be calculated
                //# as the SHA-512 hash of the concatenation of the following byte strings,
                //# in the order listed:
                cacheEntryIdentifierRequest.input
                == Primitives.Types.DigestInput(
                  digestAlgorithm := Primitives.Types.SHA_512,
                  message :=
                    //# 1.  The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID
                    partitionKeyDigest
                    //# 2.  One byte with value 1 (`0x01`)
                    + [0x01]
                    //# 3.  The two-byte algorithm suite ID corresponding to the algorithm suite in the request
                    + AlgorithmSuites.GetSuite(input.algorithmSuiteId.value).binaryId
                    //# 4.  The SHA-512 hash of the serialized encryption context
                    + ecDigestRequest.output.value
                )
              else
                //= aws-encryption-sdk-specification/framework/caching-cmm.md#encryption-materials-without-algorithm-suite
                //= type=implication
                //# If the Get Encryption Materials request does not specify an algorithm suite,
                //# then the cache entry identifier MUST be calculated
                //# as the SHA-512 hash of the concatenation of the following byte strings,
                //# in the order listed:
                cacheEntryIdentifierRequest.input
                == Primitives.Types.DigestInput(
                  digestAlgorithm := Primitives.Types.SHA_512,
                  message :=
                    //# 1. The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID
                    partitionKeyDigest
                    //# 2. One null byte (`0x00`)
                    + [0x00]
                    //# 3. The SHA-512 hash of the serialized encryption context
                    + ecDigestRequest.output.value
                )
             )
          && var cacheEntryIdentifier := cacheEntryIdentifierRequest.output.value;

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
          //= type=implication
          //# Otherwise, the caching CMM MUST attempt to find the [encryption materials](structures.md#encryption-materials)
          //# from the underlying [cryptographic materials cache (CMC)](#underlying-cryptographic-materials-cache).
          && |cache.History.GetCacheEntry| == |old(cache.History.GetCacheEntry)| + 1

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
          //= type=implication
          //# The caching CMM MUST use the formulas specified in [Appendix A](#appendix-a-cache-entry-identifier-formulas)
          //# in order to compute the [cache entry identifier](cryptographic-materials-cache.md#cache-identifier).
          && Seq.Last(cache.History.GetCacheEntry).input
             == Types.GetCacheEntryInput(
                  identifier := cacheEntryIdentifier,
                  //= aws-encryption-sdk-specification/framework/caching-cmm.md#usage-stats
                  //= type=implication
                  //# When the caching CMM obtains encryption materials from the cryptographic materials cache,
                  //# the caching CMM MUST update the usage stats for the cache entry retrieved.
                  bytesUsed := Some(input.maxPlaintextLength.value)
                )

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
          //= type=implication
          //# If an encryption materials cache entry is found,
          //# and the [cache entry is within limits](#cache-entry-within-limits)
          //# the caching CMM MUST return the encryption materials retrieved.
          && (
               && Seq.Last(cache.History.GetCacheEntry).output.Success?
               && var entry := Seq.Last(cache.History.GetCacheEntry).output;
               && entry.value.materials.Encryption?
               && (exists now
                     :: cacheEntryWithinLimits(
                          creationTime := entry.value.creationTime,
                          bytesUsed    := entry.value.bytesUsed,
                          messagesUsed := entry.value.messagesUsed,
                          now          := now
                        ))
               ==>
                 && entry.value.materials.Encryption == output.value.encryptionMaterials
             )

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
          //= type=implication
          //# If a cache entry is not found or the cache entry is expired
          //# or the [cache entry is not within limits](#cache-entry-within-limits),
          //# the caching CMM MUST then attempt to obtain the encryption materials
          //# by making a call to the underlying CMM's [Get Encryption Materials](cmm-interface.md#get-encryption-materials).
          && (
               || Seq.Last(cache.History.GetCacheEntry).output.Failure?
               || (
                    && Seq.Last(cache.History.GetCacheEntry).output.Success?
                    && var entry := Seq.Last(cache.History.GetCacheEntry).output;
                    && entry.value.materials.Encryption?
                    && (exists now
                          :: !cacheEntryWithinLimits(
                               creationTime := entry.value.creationTime,
                               bytesUsed    := entry.value.bytesUsed,
                               messagesUsed := entry.value.messagesUsed,
                               now          := now
                             )))
               ==>
                 && |old(underlyingCMM.History.GetEncryptionMaterials)| + 1 == |underlyingCMM.History.GetEncryptionMaterials|
                 && input == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).input
                 && output == Seq.Last(underlyingCMM.History.GetEncryptionMaterials).output

                 //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
                 //= type=implication
                 //# If the [algorithm suite](algorithm-suites.md) on the returned encryption material
                 //# does not contain an [Identity KDF](algorithm-suites.md#identity-kdf),
                 //# and the newly constructed [cache entry is within limits](#cache-entry-within-limits),
                 //# the caching CMM MUST add the encryption materials obtained from the underlying CMM into the underlying CMC.
                 && var encryptionMaterials := output.value.encryptionMaterials;
                 (
                   && !encryptionMaterials.algorithmSuite.kdf.IDENTITY?
                   && (exists now
                         :: cacheEntryWithinLimits(
                              creationTime := now,
                              bytesUsed    := input.maxPlaintextLength.value,
                              messagesUsed := 1,
                              now          := now
                            ))
                   ==>
                     && |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)| + 1
                     && var PutCacheEntryInput := Seq.Last(cache.History.PutCacheEntry).input;
                     && PutCacheEntryInput.materials == Types.Encryption(output.value.encryptionMaterials)
                     && PutCacheEntryInput.identifier == Seq.Last(cache.History.GetCacheEntry).input.identifier
                        //= aws-encryption-sdk-specification/framework/caching-cmm.md#usage-stats
                        //= type=implication
                        //# When the caching CMM stores encryption materials into the cryptographic materials cache,
                        //# the caching CMM MUST set the initial usage stats for the cache entry.
                     && PutCacheEntryInput.bytesUsed == input.maxPlaintextLength
                 )
                 //= aws-encryption-sdk-specification/framework/caching-cmm.md#get-encryption-materials
                 //= type=implication
                 //# If the [algorithm suite](algorithm-suites.md) on the returned encryption material
                 //# contains an an [Identity KDF](algorithm-suites.md#identity-kdf),
                 //# or the newly constructed [cache entry is not within limits](#cache-entry-within-limits),
                 //# the caching CMM MUST NOT store the encryption materials in the underlying CMC.
                 && (
                   || encryptionMaterials.algorithmSuite.kdf.IDENTITY?
                   || (exists now
                         :: !cacheEntryWithinLimits(
                              creationTime := now,
                              bytesUsed    := input.maxPlaintextLength.value,
                              messagesUsed := 1,
                              now          := now
                            ))
                   ==>
                     && |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)|
                 )
             )
    {
      if BypassCache(input, limitBytes) {
        output := underlyingCMM.GetEncryptionMaterials(input);
      } else {
        var cacheEntryIdentifier :- GetEncryptMaterialsCacheIdentifier(partitionKeyDigest, input, cryptoPrimitives);
        verifyValidStateCache(cache);
        var entry := getEntry(
          cache,
          Types.GetCacheEntryInput(
            identifier := cacheEntryIdentifier,
            bytesUsed := Some(input.maxPlaintextLength.value)
          )
        );
        var now := Time.GetCurrent();
        if
          && entry.Success?
          && entry.value.materials.Encryption?
          && cacheEntryWithinLimits(
               creationTime := entry.value.creationTime,
               bytesUsed    := entry.value.bytesUsed,
               messagesUsed := entry.value.messagesUsed,
               now          := now
             )
        {
          output := Success(
            Types.GetEncryptionMaterialsOutput(
              encryptionMaterials := entry.value.materials.Encryption
            ));
        } else {
          output := underlyingCMM.GetEncryptionMaterials(input);
          if output.Success? {
            MaybePut(
              cacheEntryIdentifier,
              Types.Encryption(output.value.encryptionMaterials),
              input.maxPlaintextLength.value
            );
          }
        }
      }

        // For Dafny keyrings this is a trivial statement
        // because they implement a trait that ensures this.
        // However not all keyrings are Dafny keyrings.
        // Customers can create custom keyrings.
      :- Need(
        output.Success? ==> Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.encryptionMaterials),
        Types.AwsCryptographicMaterialProvidersException(
          message := "Could not retrieve materials required for encryption"));
      :- Need(
        output.Success? ==> CMM.RequiredEncryptionContextKeys?(input.requiredEncryptionContextKeys, output.value.encryptionMaterials),
        Types.AwsCryptographicMaterialProvidersException(
          message := "Keyring returned an invalid response"));

    }

    predicate cacheEntryWithinLimits(
      nameonly creationTime: Types.PositiveLong,
      nameonly bytesUsed: Types.PositiveLong,
      nameonly messagesUsed: Types.PositiveInteger,
      nameonly now: Types.PositiveLong
    )
    {
      //= aws-encryption-sdk-specification/framework/caching-cmm.md#cache-entry-within-limits
      //= type=implication
      //# * Current time minus the [entry's creation time](./cryptographic-materials-cache.md#creation-time)
      //# MUST be less than or equal to the configured [Cache Limit TTL](#cache-limit-ttl)
      && now - creationTime <= ttlSeconds as Types.PositiveLong

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#cache-entry-within-limits
      //= type=implication
      //# * The [entry's bytes used](./cryptographic-materials-cache.md#bytes-usage)
      //# MUST be less than or equal to the configured [Limit Bytes](#limit-bytes)
      && bytesUsed as int64 <= limitBytes

      //= aws-encryption-sdk-specification/framework/caching-cmm.md#cache-entry-within-limits
      //= type=implication
      //# * The [entry's messages used](./cryptographic-materials-cache.md#message-usage)
      //# MUST be less than or equal to the configured [Limit Messages](#limit-messages)
      && messagesUsed as uint32 <= limitMessages
    }

    method MaybePut(
      identifier: seq<uint8>,
      cacheEntryMartials: Types.Materials,
      bytesUsed: Types.PositiveLong
    )
      requires cacheEntryMartials.Decryption? || cacheEntryMartials.Encryption?

      ensures
        var algorithmSuite := match cacheEntryMartials
          case Decryption(m) => m.algorithmSuite
          case Encryption(m) => m.algorithmSuite;
        && !algorithmSuite.kdf.IDENTITY?
        && (exists now
              :: cacheEntryWithinLimits(
                   creationTime := now,
                   bytesUsed    := bytesUsed,
                   messagesUsed := 1,
                   now          := now
                 ))
        ==>
          && |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)| + 1
          && Seq.Last(cache.History.PutCacheEntry).input.identifier == identifier
          && Seq.Last(cache.History.PutCacheEntry).input.materials == cacheEntryMartials
          && Seq.Last(cache.History.PutCacheEntry).input.bytesUsed == Some(bytesUsed)
          && Seq.Last(cache.History.PutCacheEntry).input.messagesUsed == Some(1)
      ensures
        var algorithmSuite := match cacheEntryMartials
          case Decryption(m) => m.algorithmSuite
          case Encryption(m) => m.algorithmSuite;
        || algorithmSuite.kdf.IDENTITY?
        || !(exists now
               :: cacheEntryWithinLimits(
                    creationTime := now,
                    bytesUsed    := bytesUsed,
                    messagesUsed := 1,
                    now          := now
                  ))
        ==>
          |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)|
    {
      var now: int64 := Time.GetCurrent();
      // This is true for any correct implementation for any reasonable timescale.
      // We control the time implementation but Dafny knows that it is still possible.
      expect now  < UInt.INT64_MAX_LIMIT as int64 - ttlSeconds as int64;
      var expiryTime := now + ttlSeconds as int64;
      var algorithmSuite := match cacheEntryMartials
        case Decryption(m) => m.algorithmSuite
        case Encryption(m) => m.algorithmSuite;
      if
        && !algorithmSuite.kdf.IDENTITY?
        && cacheEntryWithinLimits(
             creationTime := now,
             bytesUsed    := bytesUsed,
             messagesUsed := 1,
             now          := now
           )
      {
        verifyValidStateCache(cache);
        var _ := putEntry(
          cache,
          Types.PutCacheEntryInput(
            identifier := identifier,
            materials := cacheEntryMartials,
            creationTime := now,
            expiryTime := expiryTime,
            messagesUsed := Some(1),
            bytesUsed := None
          )
        );
      }
    }

    ghost predicate DecryptMaterialsEnsuresPublicly(input: Types.DecryptMaterialsInput, output: Result<Types.DecryptMaterialsOutput, Types.Error>)
    {true}

    method DecryptMaterials'(
      input: Types.DecryptMaterialsInput
    )
      returns (output: Result<Types.DecryptMaterialsOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DecryptMaterialsEnsuresPublicly(input, output)
      ensures unchanged(History)

      ensures output.Success?
              ==>
                && Materials.DecryptionMaterialsWithPlaintextDataKey(output.value.decryptionMaterials)
      ensures
        && (output.Success? ==> CMM.ReproducedEncryptionContext?(input))
        && (!CMM.ReproducedEncryptionContext?(input) ==> output.Failure?)
      ensures output.Success? ==> CMM.EncryptionContextComplete(input, output.value.decryptionMaterials)


      //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
      //= type=implication
      //# If the [algorithm suite](algorithm-suites.md) requested contains a [Identity KDF](algorithm-suites.md#identity-kdf),
      //# the caching CMM MUST obtain the decryption materials
      //# by making a call to the underlying CMM's [Decrypt Materials](cmm-interface.md#decrypt-materials) function.
      ensures
        && output.Success?
        && AlgorithmSuites.GetSuite(input.algorithmSuiteId).kdf.IDENTITY?
        ==>
          && |old(underlyingCMM.History.DecryptMaterials)| + 1 == |underlyingCMM.History.DecryptMaterials|
          && input == Seq.Last(underlyingCMM.History.DecryptMaterials).input
          && output == Seq.Last(underlyingCMM.History.DecryptMaterials).output


      ensures
        && !AlgorithmSuites.GetSuite(input.algorithmSuiteId).kdf.IDENTITY?
        && output.Success?
        ==>
          && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + |input.encryptedDataKeys| + 2
          && var cacheEntryIdentifierRequest := Seq.Last(cryptoPrimitives.History.Digest);
          && cacheEntryIdentifierRequest.output.Success?
          && var edkDigestRequests
               := cryptoPrimitives.History.Digest[
                  |old(cryptoPrimitives.History.Digest)| .. |old(cryptoPrimitives.History.Digest)| + |input.encryptedDataKeys|
                  ];
          && (forall e <- edkDigestRequests :: e.output.Success?)
          && var ecDigestRequest := Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest));
          && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
          && ecDigestRequest.output.Success?
          && ecDigestRequest.input.digestAlgorithm == Primitives.Types.SHA_512
          && ecDigestRequest.input.message == CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).value

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#appendix-a-cache-entry-identifier-formulas
          //= type=implication
          //# When accessing the underlying CMC,
          //# the caching CMM MUST use the formulas specified in this appendix
          //# in order to compute the [cache entry identifier](cryptographic-materials-cache.md#cache-identifier).

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#decryption-materials
          //= type=implication
          //# When the caching CMM receives a Decrypt Materials request,
          //# it MUST calculate the cache entry identifier as
          //# the SHA-512 hash of the concatenation of the following byte strings,
          //# in the order listed:
          && cacheEntryIdentifierRequest.input.digestAlgorithm == Primitives.Types.SHA_512
          && cacheEntryIdentifierRequest.input.message ==
             //# 1.  The SHA-512 hash of a UTF-8 encoding of the caching CMM’s Partition ID
             partitionKeyDigest
             //# 2.  The two-byte algorithm suite ID corresponding to the algorithm suite in the request
             + AlgorithmSuites.GetSuite(input.algorithmSuiteId).binaryId
             //# 3.  The concatenation of the lexicographically-sorted SHA-512 hashes of the serialized encrypted data keys,
             //#     where serialization is as defined in the [Encrypted Data Key Entries specification](../data-format/message-header.md#encrypted-data-key-entries).
             + SortEdkDigests(PluckDigestValue(edkDigestRequests))
             //# 4.  A sentinel field of 512 zero bits (or equivalently, 64 null bytes), indicating the end of the key hashes
             + PADDING_OF_512_ZERO_BITS
             //# 5.  The SHA-512 hash of the serialized encryption context
             + ecDigestRequest.output.value
          && var cacheEntryIdentifier := cacheEntryIdentifierRequest.output.value;

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
          //= type=implication
          //# Otherwise, the caching CMM MUST attempt to find the [decryption materials](structures.md#decryption-materials)
          //# from the [underlying CMC](#underlying-cryptographic-materials-cache).
          && |cache.History.GetCacheEntry| == |old(cache.History.GetCacheEntry)| + 1

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
          //= type=implication
          //# The caching CMM MUST use the formulas specified in [Appendix A](#appendix-a-cache-entry-identifier-formulas)
          //# in order to compute the [cache entry identifier](cryptographic-materials-cache.md#cache-identifier).
          && Seq.Last(cache.History.GetCacheEntry).input
             == Types.GetCacheEntryInput(
                  identifier := cacheEntryIdentifier,
                  bytesUsed := None()
                )

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
          //= type=implication
          //# If a decryption materials cache entry is found,
          //# and the [cache entry is within limits](#cache-entry-within-limits)
          //# the caching CMM MUST return the decryption materials retrieved.
          && (
               && Seq.Last(cache.History.GetCacheEntry).output.Success?
               && var entry := Seq.Last(cache.History.GetCacheEntry).output;
               && entry.value.materials.Decryption?
               && (exists now
                     :: cacheEntryWithinLimits(
                          creationTime := entry.value.creationTime,
                          bytesUsed    := entry.value.bytesUsed,
                          messagesUsed := entry.value.messagesUsed,
                          now          := now
                        ))
               ==>
                 && entry.value.materials.Decryption == output.value.decryptionMaterials
             )

          //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
          //= type=implication
          //# If a cache entry is not found or the cache entry is expired
          //# or the [cache entry is not within limits](#cache-entry-within-limits),
          //# the caching CMM MUST attempt to obtain the decryption materials
          //# by making a call to the underlying CMM's [Decrypt Materials](cmm-interface.md#decrypt-materials).
          && (
               || Seq.Last(cache.History.GetCacheEntry).output.Failure?
               || (
                    && Seq.Last(cache.History.GetCacheEntry).output.Success?
                    && var entry := Seq.Last(cache.History.GetCacheEntry).output;
                    && entry.value.materials.Encryption?
                    && (exists now
                          :: !cacheEntryWithinLimits(
                               creationTime := entry.value.creationTime,
                               bytesUsed    := entry.value.bytesUsed,
                               messagesUsed := entry.value.messagesUsed,
                               now          := now
                             )))
               ==>
                 && |old(underlyingCMM.History.DecryptMaterials)| + 1 == |underlyingCMM.History.DecryptMaterials|
                 && input == Seq.Last(underlyingCMM.History.DecryptMaterials).input
                 && output == Seq.Last(underlyingCMM.History.DecryptMaterials).output

                 //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
                 //= type=implication
                 //# For decrypt limits bytes MUST be 0.
                 && var bytesUsed := 0;

                 //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
                 //= type=implication
                 //# If the [algorithm suite](algorithm-suites.md) on the returned decryption material
                 //# does not contain an [Identity KDF](algorithm-suites.md#identity-kdf),
                 //# and the newly constructed [cache entry is within limits](#cache-entry-within-limits),
                 //# the caching CMM MUST add the decryption materials obtained from the underlying CMM into the underlying CMC.
                 && var decryptionMaterials := output.value.decryptionMaterials;
                 (
                   && !decryptionMaterials.algorithmSuite.kdf.IDENTITY?
                   && (exists now
                         :: cacheEntryWithinLimits(
                              creationTime := now,
                              bytesUsed    := bytesUsed,
                              messagesUsed := 1,
                              now          := now
                            ))
                   ==>
                     && |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)| + 1
                     && var PutCacheEntryInput := Seq.Last(cache.History.PutCacheEntry).input;
                     && PutCacheEntryInput.materials == Types.Decryption(output.value.decryptionMaterials)
                     && PutCacheEntryInput.identifier == Seq.Last(cache.History.GetCacheEntry).input.identifier
                     && PutCacheEntryInput.bytesUsed == Some(bytesUsed)
                 )

                 //= aws-encryption-sdk-specification/framework/caching-cmm.md#decrypt-materials
                 //= type=implication
                 //# If the [algorithm suite](algorithm-suites.md) on the returned decryption material
                 //# contains an an [Identity KDF](algorithm-suites.md#identity-kdf),
                 //# or the newly constructed [cache entry is not within limits](#cache-entry-within-limits),
                 //# the caching CMM MUST NOT store the decryption materials in the underlying CMC.
                 && (
                   || decryptionMaterials.algorithmSuite.kdf.IDENTITY?
                   || (exists now
                         :: !cacheEntryWithinLimits(
                              creationTime := now,
                              bytesUsed    := bytesUsed,
                              messagesUsed := 1,
                              now          := now
                            ))
                   ==>
                     && |cache.History.PutCacheEntry| == |old(cache.History.PutCacheEntry)|
                 )
             )
    {
      :- Need(CMM.ReproducedEncryptionContext?(input),
              Types.AwsCryptographicMaterialProvidersException(
                message := "Encryption context does not match reproduced encryption context.")
      );
      if AlgorithmSuites.GetSuite(input.algorithmSuiteId).kdf.IDENTITY?
      {
        output := underlyingCMM.DecryptMaterials(input);
      } else {
        var identifier :- GetDecryptMaterialsCacheIdentifier(partitionKeyDigest, input, cryptoPrimitives);
        verifyValidStateCache(cache);
        var entry := getEntry(
          cache,
          Types.GetCacheEntryInput(
            identifier := identifier,
            bytesUsed := None
          )
        );
        var now := Time.GetCurrent();

        if
          && entry.Success?
          && entry.value.materials.Decryption?
          && cacheEntryWithinLimits(
               creationTime := entry.value.creationTime,
               bytesUsed    := entry.value.bytesUsed,
               messagesUsed := entry.value.messagesUsed,
               now          := now
             )
        {
          output := Success(
            Types.DecryptMaterialsOutput(
              decryptionMaterials := entry.value.materials.Decryption
            ));
        } else {
          output := underlyingCMM.DecryptMaterials(input);
          if output.Success? {
            MaybePut(
              identifier,
              Types.Decryption(output.value.decryptionMaterials),
              0
            );
          }
        }
      }

      :- Need(
        output.Success? ==> Materials.DecryptionMaterialsWithPlaintextDataKey(output.value.decryptionMaterials),
        Types.AwsCryptographicMaterialProvidersException(
          message := "Keyring.OnDecrypt failed to decrypt the plaintext data key."));
      :- Need(
        output.Success? ==> CMM.EncryptionContextComplete(input, output.value.decryptionMaterials),
        Types.AwsCryptographicMaterialProvidersException(
          message := "Reproduced encryption context missing from encryption context."));
    }
  }

  predicate BypassCache(
    input: Types.GetEncryptionMaterialsInput,
    limitBytes: Types.PositiveLong
  ) {
    || input.maxPlaintextLength.None?
    || (input.maxPlaintextLength.value < 0)
    || (limitBytes < input.maxPlaintextLength.value)
    || (input.algorithmSuiteId.Some? && AlgorithmSuites.GetSuite(input.algorithmSuiteId.value).kdf.IDENTITY?)
  }

  // We add this axiom here because verifying the mutability of the share state of the
  // cache. Dafny does not support concurrency and proving the state of mutable frames
  // is complicated.
  lemma {:axiom} verifyValidStateCache (cmc: Types.ICryptographicMaterialsCache)
    ensures cmc.ValidState()

  method getEntry(cache: Types.ICryptographicMaterialsCache, input: Types.GetCacheEntryInput)
    returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
    requires cache.ValidState()
    ensures cache.ValidState()
    ensures cache.GetCacheEntryEnsuresPublicly(input, output)
    ensures cache.History.GetCacheEntry == old(cache.History.GetCacheEntry) + [Types.DafnyCallEvent(input, output)]
  {
    // Because of the mutable state of the cache you may not know if you have an entry in cache
    // at this point in execution; assuming we have not modified it allows dafny to verify that it can get an entry.
    assume {:axiom} cache.Modifies == {};
    output := cache.GetCacheEntry(input);
  }

  method putEntry(cache: Types.ICryptographicMaterialsCache, input: Types.PutCacheEntryInput)
    returns (output: Result<(), Types.Error>)
    requires cache.ValidState()
    ensures cache.ValidState()
    ensures cache.PutCacheEntryEnsuresPublicly(input, output)
    ensures cache.History.PutCacheEntry == old(cache.History.PutCacheEntry) + [Types.DafnyCallEvent(input, output)]
  {
    // Because of the mutable state of the cache you may not know if you have an entry in cache
    // at this point in execution; assuming we have not modified it allows dafny to verify that it can put an entry.
    assume {:axiom} cache.Modifies == {};
    output := cache.PutCacheEntry(input);
  }

  method GetEncryptMaterialsCacheIdentifier (
    partitionKeyDigest: seq<uint8>,
    input: Types.GetEncryptionMaterialsInput,
    cryptoPrimitives: Primitives.AtomicPrimitivesClient
  )
    returns (output: Result<seq<uint8>, Types.Error>)
    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()

    ensures
      output.Success?
      ==>
        && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + 2
        && Seq.Last(cryptoPrimitives.History.Digest).output.Success?
        && var ecDigestRequest := Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest));
        && ecDigestRequest.output.Success?
        && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
        && ecDigestRequest.input
           == Primitives.Types.DigestInput(
                digestAlgorithm := Primitives.Types.SHA_512,
                message := CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).value
              )
        && (if input.algorithmSuiteId.Some? then
              Seq.Last(cryptoPrimitives.History.Digest).input
              == Primitives.Types.DigestInput(
                digestAlgorithm := Primitives.Types.SHA_512,
                message :=
                  partitionKeyDigest
                  + [0x01]
                  + AlgorithmSuites.GetSuite(input.algorithmSuiteId.value).binaryId
                  + ecDigestRequest.output.value
              )
            else
              Seq.Last(cryptoPrimitives.History.Digest).input
              == Primitives.Types.DigestInput(
                digestAlgorithm := Primitives.Types.SHA_512,
                message :=
                  partitionKeyDigest
                  + [0x00]
                  + ecDigestRequest.output.value
              )
           )
        && Seq.Last(cryptoPrimitives.History.Digest).output.value == output.value
  {
    var ecDigest :- Sha512EncryptionContext(input.encryptionContext, cryptoPrimitives);

    var output';

    if input.algorithmSuiteId.Some? {
      var algorithmSuiteBinaryId := AlgorithmSuites.GetSuite(input.algorithmSuiteId.value).binaryId;
      output' := cryptoPrimitives.Digest(
        Primitives.Types.DigestInput(
          digestAlgorithm := Primitives.Types.SHA_512,
          message :=
            partitionKeyDigest
            + [0x01]
            + algorithmSuiteBinaryId
            + ecDigest
        ));
    } else {
      output' := cryptoPrimitives.Digest(
        Primitives.Types.DigestInput(
          digestAlgorithm := Primitives.Types.SHA_512,
          message :=
            partitionKeyDigest
            + [0x00]
            + ecDigest
        ));
    }
    output := output'.MapFailure(e => Types.AwsCryptographyPrimitives(e));
  }

  const PADDING_OF_512_ZERO_BITS: seq<uint8> := [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0
  ]

  lemma PaddingIsCorrect()
    ensures |PADDING_OF_512_ZERO_BITS| == 64
    ensures 64 * 8 == 512
    ensures forall b <- PADDING_OF_512_ZERO_BITS :: b == 0
  {}

  method {:vcs_split_on_every_assert} GetDecryptMaterialsCacheIdentifier(
    partitionKeyDigest: seq<uint8>,
    input: Types.DecryptMaterialsInput,
    cryptoPrimitives: Primitives.AtomicPrimitivesClient
  )
    returns (output: Result<seq<uint8>, Types.Error>)
    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()

    ensures
      output.Success?
      ==>
        && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + |input.encryptedDataKeys| + 2
        && var outputRequest := Seq.Last(cryptoPrimitives.History.Digest);
        && var edkDigestRequests
          := cryptoPrimitives.History.Digest[
             |old(cryptoPrimitives.History.Digest)| .. |old(cryptoPrimitives.History.Digest)| + |input.encryptedDataKeys|
             ];
        && (forall e <- edkDigestRequests :: e.output.Success?)
        && var ecDigestRequest := Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest));
        && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
        && ecDigestRequest.output.Success?
        && ecDigestRequest.input.digestAlgorithm == Primitives.Types.SHA_512
        && ecDigestRequest.input.message == CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).value

        && outputRequest.input.digestAlgorithm == Primitives.Types.SHA_512
        && outputRequest.input.message
           ==  partitionKeyDigest
               + AlgorithmSuites.GetSuite(input.algorithmSuiteId).binaryId
               + SortEdkDigests(PluckDigestValue(edkDigestRequests))
               + PADDING_OF_512_ZERO_BITS
               + ecDigestRequest.output.value
        && outputRequest.output.Success?
        && output.value == outputRequest.output.value
  {
    ghost var oldDigest := cryptoPrimitives.History.Digest;

    var digests :- EdkDigests(input.encryptedDataKeys, cryptoPrimitives);

    label AFTER_EDK_DIGESTS:
    var edkDigestRequests := cryptoPrimitives.History.Digest[|oldDigest|..];
    assert cryptoPrimitives.History.Digest == oldDigest + edkDigestRequests;

    var sortedEdkHashes : seq<uint8> := SortEdkDigests(digests);
    var algorithmSuiteBinaryId := AlgorithmSuites.GetSuite(input.algorithmSuiteId).binaryId;

    var ecDigest :- Sha512EncryptionContext(input.encryptionContext, cryptoPrimitives);

    label AFTER_ENCRYPTION_CONTEXT:
    var ecDigestRequest := Seq.Last(cryptoPrimitives.History.Digest);
    assert cryptoPrimitives.History.Digest == old@AFTER_EDK_DIGESTS(cryptoPrimitives.History.Digest) + [ecDigestRequest];

    var message := partitionKeyDigest
    + algorithmSuiteBinaryId
    + sortedEdkHashes
    + PADDING_OF_512_ZERO_BITS
    + ecDigest;

    var output' := cryptoPrimitives.Digest(
      Primitives.Types.DigestInput(
        digestAlgorithm := Primitives.Types.SHA_512,
        message := message
      ));
    output := output'.MapFailure(e => Types.AwsCryptographyPrimitives(e));

    var outputDigestRequest := Seq.Last(cryptoPrimitives.History.Digest);
    assert cryptoPrimitives.History.Digest == old@AFTER_ENCRYPTION_CONTEXT(cryptoPrimitives.History.Digest) + [outputDigestRequest];
    assert edkDigestRequests
        == cryptoPrimitives.History.Digest[
           |oldDigest| .. |oldDigest| + |input.encryptedDataKeys|
           ]
    by {
      assert |edkDigestRequests| == |input.encryptedDataKeys|;
      assert old@AFTER_EDK_DIGESTS(cryptoPrimitives.History.Digest) < cryptoPrimitives.History.Digest;
      assert edkDigestRequests == old@AFTER_EDK_DIGESTS(cryptoPrimitives.History.Digest[|oldDigest|..]);
    }
    assert ecDigestRequest == Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest));
    assert (forall e <- edkDigestRequests :: e.output.Success?);
    assert PluckDigestValue(edkDigestRequests) == digests;
    assert Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest)).output.Success?;
    assert Seq.Last(cryptoPrimitives.History.Digest).input.digestAlgorithm == Primitives.Types.SHA_512;
    assert Seq.Last(cryptoPrimitives.History.Digest).input.message
        ==  partitionKeyDigest
            + AlgorithmSuites.GetSuite(input.algorithmSuiteId).binaryId
            + SortEdkDigests(PluckDigestValue(edkDigestRequests))
            + PADDING_OF_512_ZERO_BITS
            + Seq.Last(Seq.DropLast(cryptoPrimitives.History.Digest)).output.value;
  }

  method Sha512EncryptionContext(
    encryptionContext: Types.EncryptionContext,
    cryptoPrimitives: Primitives.AtomicPrimitivesClient
  )
    returns (output: Result<seq<uint8>, Types.Error>)
    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()

    ensures
      output.Success?
      ==>
        && CanonicalEncryptionContext.EncryptionContextToAAD(encryptionContext).Success?
        && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + 1
        && old(cryptoPrimitives.History.Digest) < cryptoPrimitives.History.Digest
        && Seq.Last(cryptoPrimitives.History.Digest).input
           == Primitives.Types.DigestInput(
                digestAlgorithm := Primitives.Types.SHA_512,
                message := CanonicalEncryptionContext.EncryptionContextToAAD(encryptionContext).value
              )
        && Seq.Last(cryptoPrimitives.History.Digest).output.Success?
        && Seq.Last(cryptoPrimitives.History.Digest).output.value == output.value
  {
    var message :- CanonicalEncryptionContext.EncryptionContextToAAD(encryptionContext);

    var output' := cryptoPrimitives.Digest(
      Primitives.Types.DigestInput(
        digestAlgorithm := Primitives.Types.SHA_512,
        message := message
      ));

    output := output'.MapFailure(e => Types.AwsCryptographyPrimitives(e));
  }

  method EdkDigests(
    encryptedDataKeys: Types.EncryptedDataKeyList,
    cryptoPrimitives: Primitives.AtomicPrimitivesClient
  )
    returns (output: Result<seq<seq<uint8>>, Types.Error>)
    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()
    ensures output.Success?
            ==>
              && |output.value| == |encryptedDataKeys|
              && (forall edk <- encryptedDataKeys :: EncryptedDataKeyIntoBytes(edk).Success?)
              && |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + |encryptedDataKeys|
              && old(cryptoPrimitives.History.Digest) <= cryptoPrimitives.History.Digest
              && var digestRequests := cryptoPrimitives.History.Digest[|old(cryptoPrimitives.History.Digest)|..];
              && (forall r <- digestRequests :: r.output.Success?)
              && (forall k, request
                    |
                    && 0 <= k < |encryptedDataKeys|
                    && request == digestRequests[k]
                    ::
                      && request.input
                         == Primitives.Types.DigestInput(
                              digestAlgorithm := Primitives.Types.SHA_512,
                              message := EncryptedDataKeyIntoBytes(encryptedDataKeys[k]).value
                            )
                      && request.output.Success?
                      && output.value[k] == request.output.value
                 )
              && PluckDigestValue(digestRequests) == output.value
  {
    reveal PluckDigestValue();
    var digests := [];
    for i := 0 to |encryptedDataKeys|
      invariant cryptoPrimitives.ValidState()
      invariant |digests| == i
      invariant |cryptoPrimitives.History.Digest| == |old(cryptoPrimitives.History.Digest)| + i
      invariant old(cryptoPrimitives.History.Digest) <= cryptoPrimitives.History.Digest
      invariant |cryptoPrimitives.History.Digest[|old(cryptoPrimitives.History.Digest)|..]| == i
      invariant forall edk <- encryptedDataKeys[..i] :: EncryptedDataKeyIntoBytes(edk).Success?
      invariant forall
          request <- cryptoPrimitives.History.Digest[|old(cryptoPrimitives.History.Digest)|..]
          :: request.output.Success?

      invariant
        digests
        == PluckDigestValue(cryptoPrimitives.History.Digest[|old(cryptoPrimitives.History.Digest)|..])
      invariant forall
          k, request
          |
          && 0 <= k < i
          && request == cryptoPrimitives.History.Digest[|old(cryptoPrimitives.History.Digest)| + k]
          ::
            && request.input
               == Primitives.Types.DigestInput(
                    digestAlgorithm := Primitives.Types.SHA_512,
                    message := EncryptedDataKeyIntoBytes(encryptedDataKeys[k]).value
                  )
            && request.output.Success?
            && request.output.value == digests[k]
    {
      var message :- EncryptedDataKeyIntoBytes(encryptedDataKeys[i]);
      var digest' := cryptoPrimitives.Digest(
        Primitives.Types.DigestInput(
          digestAlgorithm := Primitives.Types.SHA_512,
          message := message
        ));
      var digest :- digest'.MapFailure(e => Types.AwsCryptographyPrimitives(e));
      digests := digests + [digest];
    }

    output := Success(digests);
  }

  opaque ghost function PluckDigestValue(
    digestRequests: seq<Primitives.Types.DafnyCallEvent<Primitives.Types.DigestInput, Result<seq<uint8>, Primitives.Types.Error>>>
  )
    :seq<seq<uint8>>
    requires forall c <- digestRequests :: c.output.Success?
  {
    seq(|digestRequests|, k requires 0 <= k < |digestRequests| => digestRequests[k].output.value)
  }

  function SortEdkDigests(
    digests: seq<seq<uint8>>
  )
    : (output: seq<uint8>)
  {
    Sorting.AboutLexicographicByteSeqBelow();
    var sortedDigests := MergeSort.MergeSortBy(digests, Sorting.LexicographicByteSeqBelow);
    Seq.Flatten(sortedDigests)
  }

  function EncryptedDataKeyIntoBytes(edk: Types.EncryptedDataKey)
    : (output: Result<seq<uint8>, Types.Error>)

  {
    :- Need(HasUint16Len(edk.keyProviderId) && HasUint16Len(edk.keyProviderInfo) && HasUint16Len(edk.ciphertext),
            Types.AwsCryptographicMaterialProvidersException( message := "Unable to serialize encrypted data key"));
    Success(
      UInt16ToSeq(|edk.keyProviderId| as uint16) + edk.keyProviderId
      + UInt16ToSeq(|edk.keyProviderInfo| as uint16) + edk.keyProviderInfo
      + UInt16ToSeq(|edk.ciphertext| as uint16) + edk.ciphertext)
  }

}
