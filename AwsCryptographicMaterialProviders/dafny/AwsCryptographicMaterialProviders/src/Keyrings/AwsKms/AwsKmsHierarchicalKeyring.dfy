// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../Keyring.dfy"
include "../../Materials.dfy"
include "../../AlgorithmSuites.dfy"
include "../../CanonicalEncryptionContext.dfy"
include "../../KeyWrapping/EdkWrapping.dfy"
include "Constants.dfy"
include "AwsKmsMrkMatchForDecrypt.dfy"
include "../../AwsArnParsing.dfy"
include "AwsKmsUtils.dfy"
include "../../CMCs/StormTracker.dfy"
include "../../CMCs/StormTrackingCMC.dfy"
include "../../CMCs/LocalCMC.dfy"
include "../../CMCs/SynchronizedLocalCMC.dfy"
include "../../CMCs/CacheConstants.dfy"
include "../../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../../ErrorMessages.dfy"

module AwsKmsHierarchicalKeyring {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import opened AwsArnParsing
  import opened AwsKmsUtils
  import opened Seq
  import opened Actions
  import opened Constants
  import opened A = AwsKmsMrkMatchForDecrypt
  import LocalCMC
  import SynchronizedLocalCMC
  import StormTracker
  import StormTrackingCMC
  import opened CacheConstants
  import opened AlgorithmSuites
  import EdkWrapping
  import MaterialWrapping
  import CanonicalEncryptionContext
  import Keyring
  import Materials
  import Time
  import Random
  import Digest
  import Types = AwsCryptographyMaterialProvidersTypes
  import Crypto = AwsCryptographyPrimitivesTypes
  import KMS = ComAmazonawsKmsTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KeyStore = AwsCryptographyKeyStoreTypes
  import UTF8
  import UUID
  import HKDF
  import HMAC
  import opened AESEncryption
  import AtomicPrimitives
  import ErrorMessages

  const BRANCH_KEY_STORE_GSI := "Active-Keys"
  const BRANCH_KEY_FIELD := "enc"
  const VERSION_FIELD := "version"
  const BRANCH_KEY_IDENTIFIER_FIELD := "branch-key-id"

  const KEY_CONDITION_EXPRESSION := "#status = :status and #branch_key_id = :branch_key_id"
  const EXPRESSION_ATTRIBUTE_NAMES := map[
                                        "#status"       := "status",
                                        "#branch_key_id" := "branch-key-id"
                                      ]
  const EXPRESSION_ATTRIBUTE_VALUE_STATUS_KEY := ":status"
  const EXPRESSION_ATTRIBUTE_VALUE_STATUS_VALUE := "ACTIVE"
  const EXPRESSION_ATTRIBUTE_VALUE_BRANCH_KEY := ":branch_key_id"

  const H_WRAP_SALT_LEN: Types.PositiveInteger := 16
  const H_WRAP_NONCE_LEN: Types.PositiveInteger := 12
  const DERIVED_BRANCH_KEY_EXPECTED_LENGTH: Types.PositiveInteger := 32
  const AES_256_ENC_KEY_LENGTH: int32 := 32
  const AES_256_ENC_TAG_LENGTH: int32 := 16
  const AES_256_ENC_IV_LENGTH: int32 := 12
  const AES_256_ENC_ALG := Crypto.AES_GCM(
                             keyLength := AES_256_ENC_KEY_LENGTH,
                             //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
                             //= type=implication
                             //# MUST use an authentication tag byte of length 16.
                             tagLength := AES_256_ENC_TAG_LENGTH,
                             ivLength := AES_256_ENC_IV_LENGTH
                           )

  const EDK_CIPHERTEXT_VERSION_LENGTH: int32 := 16
  const EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX := H_WRAP_SALT_LEN + H_WRAP_NONCE_LEN
  const EDK_CIPHERTEXT_VERSION_INDEX := EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX + EDK_CIPHERTEXT_VERSION_LENGTH
  // Salt = 16, IV = 12, Version = 16, Authentication Tag = 16
  const EXPECTED_EDK_CIPHERTEXT_OVERHEAD := EDK_CIPHERTEXT_VERSION_INDEX + AES_256_ENC_TAG_LENGTH

  // Checks if (time_now - cache creation time of the extracted cache entry) is less than the allowed
  // TTL of the current Hierarchical Keyring calling the getEntry method from the cache.
  // Mitigates risk if another Material Provider wrote the entry with a longer TTL.
  predicate method cacheEntryWithinLimits(
    creationTime: Types.PositiveLong,
    now: Types.PositiveLong,
    ttlSeconds: Types.PositiveLong
  ): (output: bool)
  {
    now - creationTime <= ttlSeconds as Types.PositiveLong
  }

  //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#interface
  //= type=implication
  //# MUST implement the [AWS Encryption SDK Keyring interface](../keyring-interface.md#interface)
  class AwsKmsHierarchicalKeyring
    extends Keyring.VerifiableInterface
  {
    const branchKeyId: Option<string>
    const branchKeyIdSupplier: Option<Types.IBranchKeyIdSupplier>
    const keyStore: KeyStore.IKeyStoreClient
    const ttlSeconds: Types.PositiveLong
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    const cache: Types.ICryptographicMaterialsCache
    const partitionIdBytes: seq<uint8>
    const logicalKeyStoreNameBytes: seq<uint8>

    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && keyStore.ValidState()
      && cryptoPrimitives.ValidState()
      && cache.ValidState()
      && (branchKeyIdSupplier.Some? ==> branchKeyIdSupplier.value.ValidState())
      && keyStore.Modifies <= Modifies
      && cryptoPrimitives.Modifies <= Modifies
      && cache.Modifies <= Modifies
      && (branchKeyIdSupplier.Some? ==> branchKeyIdSupplier.value.Modifies <= Modifies)
      && History !in keyStore.Modifies
      && History !in cryptoPrimitives.Modifies
      && History !in cache.Modifies
      && (branchKeyIdSupplier.Some? ==> History !in branchKeyIdSupplier.value.Modifies)
      && (branchKeyIdSupplier.Some? || branchKeyId.Some?)
      && (branchKeyIdSupplier.None? || branchKeyId.None?)
    }

    constructor (
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#initialization
      //= type=implication
      //# - MUST provide a [KeyStore](../branch-key-store.md)
      keyStore: KeyStore.IKeyStoreClient,
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#initialization
      //= type=implication
      //# - MUST provide either a Branch Key Identifier or a [Branch Key Supplier](#branch-key-supplier)
      branchKeyId: Option<string>,
      branchKeyIdSupplier: Option<Types.IBranchKeyIdSupplier>,
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#initialization
      //= type=implication
      //# - MUST provide a cache limit TTL
      ttlSeconds: Types.PositiveLong,

      cmc: Types.ICryptographicMaterialsCache,
      partitionIdBytes: seq<uint8>,
      logicalKeyStoreNameBytes: seq<uint8>,
      cryptoPrimitives : AtomicPrimitives.AtomicPrimitivesClient
    )
      requires ttlSeconds >= 0
      requires keyStore.ValidState() && cryptoPrimitives.ValidState() && cmc.ValidState()
      requires branchKeyIdSupplier.Some? ==> branchKeyIdSupplier.value.ValidState()
      requires (branchKeyIdSupplier.Some? || branchKeyId.Some?)
      requires (branchKeyIdSupplier.None? || branchKeyId.None?)
      ensures
        && this.keyStore     == keyStore
        && this.branchKeyIdSupplier  == branchKeyIdSupplier
        && this.ttlSeconds   == ttlSeconds
        && this.partitionIdBytes   == partitionIdBytes
        && this.logicalKeyStoreNameBytes == logicalKeyStoreNameBytes
        && this.cache == cmc
      ensures
        && ValidState()
        && fresh(this)
        && fresh(History)
        && var maybeSupplierModifies := if branchKeyIdSupplier.Some? then branchKeyIdSupplier.value.Modifies else {};
        && fresh(Modifies - keyStore.Modifies - cryptoPrimitives.Modifies - maybeSupplierModifies - cmc.Modifies)
    {
      this.keyStore                 := keyStore;
      this.branchKeyId              := branchKeyId;
      this.branchKeyIdSupplier      := branchKeyIdSupplier;
      this.ttlSeconds               := ttlSeconds;
      this.cryptoPrimitives         := cryptoPrimitives;
      this.cache                    := cmc;
      this.partitionIdBytes         := partitionIdBytes;
      this.logicalKeyStoreNameBytes := logicalKeyStoreNameBytes;

      History := new Types.IKeyringCallHistory();
      var maybeSupplierModifies := if branchKeyIdSupplier.Some? then branchKeyIdSupplier.value.Modifies else {};
      Modifies := {History} + keyStore.Modifies + cryptoPrimitives.Modifies + maybeSupplierModifies + cmc.Modifies;
    }

    method GetBranchKeyId(context: Types.EncryptionContext) returns (ret: Result<string, Types.Error>)
      requires ValidState()
      modifies if branchKeyIdSupplier.Some? then branchKeyIdSupplier.value.Modifies else {}
      ensures ValidState()
      ensures branchKeyId.Some? ==> ret.Success? && ret.value == branchKeyId.value
    {
      if branchKeyId.Some? {
        return Success(branchKeyId.value);
      } else {
        var GetBranchKeyIdOut :- branchKeyIdSupplier.value.GetBranchKeyId(
          Types.GetBranchKeyIdInput(
            encryptionContext := context
          ));
        return Success(GetBranchKeyIdOut.branchKeyId);
      }
    }

    predicate OnEncryptEnsuresPublicly (
      input: Types.OnEncryptInput ,
      output: Result<Types.OnEncryptOutput, Types.Error> )
      : (outcome: bool)
      ensures
        outcome ==>
          output.Success?
          ==>
            && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.materials)
            && Materials.ValidEncryptionMaterialsTransition(
                 input.materials,
                 output.value.materials
               )
    {
      output.Success?
      ==>
        && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.materials)
        && Materials.ValidEncryptionMaterialsTransition(
             input.materials,
             output.value.materials
           )
    }

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
    //= type=implication
    //# OnEncrypt MUST take [encryption materials]
    //# (../structures.md#encryption-materials) as input.
    method {:vcs_split_on_every_assert} OnEncrypt'(input: Types.OnEncryptInput)
      returns (res: Result<Types.OnEncryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnEncryptEnsuresPublicly(input, res)
      ensures unchanged(History)
    {
      var materials := input.materials;
      var suite := materials.algorithmSuite;

      var branchKeyIdForEncrypt :- GetBranchKeyId(materials.encryptionContext);
      var branchKeyIdUtf8 :- UTF8.Encode(branchKeyIdForEncrypt)
      .MapFailure(WrapStringToError);

      var cacheId :- GetActiveCacheId(branchKeyIdForEncrypt, branchKeyIdUtf8, cryptoPrimitives);

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
      //# the hierarchical keyring MUST attempt to obtain the branch key materials
      //# by querying the backing branch keystore specified in
      //# the [retrieve OnEncrypt branch key materials](#query-branch-keystore-onencrypt) section.
      var hierarchicalMaterials :- GetActiveHierarchicalMaterials(
        branchKeyIdForEncrypt,
        cacheId,
        keyStore
      );

      var branchKey := hierarchicalMaterials.branchKey;
      var branchKeyVersion := hierarchicalMaterials.branchKeyVersion;
      var branchKeyVersionAsString :- UTF8.Decode(branchKeyVersion).MapFailure(WrapStringToError);
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ciphertext
      //#concatenated with the byte representation of the UUID branch key version from the [branch key materials](../structures.md#branch-key-materials)
      :- Need(
        // A UUID string is 36 characters long,
        // this is the string representation of the UUIDs 16 bytes.
        |branchKeyVersionAsString| == 36,
        Types.AwsCryptographicMaterialProvidersException(
          message := "Branch key version string is not a UUID: " + branchKeyVersionAsString
        )
      );
      var branchKeyVersionAsBytes :- UUID.ToByteArray(branchKeyVersionAsString).MapFailure(WrapStringToError);

      var kmsHierarchyGenerateAndWrap := new KmsHierarchyGenerateAndWrapKeyMaterial(
        hierarchicalMaterials.branchKey,
        branchKeyIdUtf8,
        branchKeyVersionAsBytes,
        cryptoPrimitives
      );
      var kmsHierarchyWrap := new KmsHierarchyWrapKeyMaterial(
        hierarchicalMaterials.branchKey,
        branchKeyIdUtf8,
        branchKeyVersionAsBytes,
        cryptoPrimitives
      );

      var wrapOutput :- EdkWrapping.WrapEdkMaterial<HierarchyWrapInfo>(
        encryptionMaterials := materials,
        wrap := kmsHierarchyWrap,
        generateAndWrap := kmsHierarchyGenerateAndWrap
      );

      var symmetricSigningKeyList :=
        if wrapOutput.symmetricSigningKey.Some? then
          Some([wrapOutput.symmetricSigningKey.value])
        else
          None;

      var edk := Types.EncryptedDataKey(
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
        //# [key provider id](../structures.md#key-provider-id): MUST be UTF8 Encoded "aws-kms-hierarchy"
        keyProviderId := PROVIDER_ID_HIERARCHY,
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
        //# [key provider info](../structures.md#key-provider-information): MUST be the UTF8 Encoded AWS DDB response `branch-key-id`
        keyProviderInfo := branchKeyIdUtf8,
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
        //# [ciphertext](../structures.md#ciphertext): MUST be serialized as the [hierarchical keyring ciphertext](#ciphertext)
        ciphertext := wrapOutput.wrappedMaterial
      );

      if (wrapOutput.GenerateAndWrapEdkMaterialOutput?) {
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
        //# OnEncrypt MUST append a new [encrypted data key](../structures.md#encrypted-data-key)
        //# to the encrypted data key list in the [encryption materials](../structures.md#encryption-materials)
        var result :- Materials.EncryptionMaterialAddDataKey(materials, wrapOutput.plaintextDataKey, [edk], symmetricSigningKeyList);
        return Success(Types.OnEncryptOutput(
                         materials := result
                       ));
      } else if (wrapOutput.WrapOnlyEdkMaterialOutput?) {
        var result :- Materials.EncryptionMaterialAddEncryptedDataKeys(
          materials,
          [edk],
          symmetricSigningKeyList
        );
        return Success(Types.OnEncryptOutput(
                         materials := result
                       ));
      }
    }

    predicate OnDecryptEnsuresPublicly ( input: Types.OnDecryptInput , output: Result<Types.OnDecryptOutput, Types.Error> )
      : (outcome: bool)
      ensures
        outcome ==>
          output.Success?
          ==>
            && Materials.DecryptionMaterialsTransitionIsValid(
              input.materials,
              output.value.materials
            )
    {
      output.Success?
      ==>
        && Materials.DecryptionMaterialsTransitionIsValid(
          input.materials,
          output.value.materials
        )
    }
    method OnDecrypt'(input: Types.OnDecryptInput)
      returns (res: Result<Types.OnDecryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnDecryptEnsuresPublicly(input, res)
      ensures unchanged(History)

    {
      var materials := input.materials;
      var suite := input.materials.algorithmSuite;

      :- Need(
        Materials.DecryptionMaterialsWithoutPlaintextDataKey(materials),
        E("Keyring received decryption materials that already contain a plaintext data key.")
      );

      // Determine branch key ID
      var branchKeyIdForDecrypt :- GetBranchKeyId(materials.encryptionContext);

      var filter := new OnDecryptHierarchyEncryptedDataKeyFilter(branchKeyIdForDecrypt);
      var edksToAttempt :- FilterWithResult(filter, input.encryptedDataKeys);

      SequenceIsSafeBecauseItIsInMemory(edksToAttempt);
      if (0 == |edksToAttempt| as uint64) {
        var errorMessage :- ErrorMessages.IncorrectDataKeys(input.encryptedDataKeys, input.materials.algorithmSuite);
        return Failure(
            Types.AwsCryptographicMaterialProvidersException(
              message := errorMessage
            ));
      }

      var decryptClosure := new DecryptSingleEncryptedDataKey(
        materials := materials,
        keyStore := keyStore,
        cryptoPrimitives := cryptoPrimitives,
        branchKeyId := branchKeyIdForDecrypt,
        ttlSeconds := ttlSeconds,
        cache := cache,
        partitionIdBytes := partitionIdBytes,
        logicalKeyStoreNameBytes := logicalKeyStoreNameBytes
      );

      var outcome, attempts := ReduceToSuccess(
        decryptClosure,
        edksToAttempt
      );

      var SealedDecryptionMaterials :- outcome
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-keyring.md#ondecrypt
      //# If OnDecrypt fails to successfully decrypt any [encrypted data key]
      //# (../structures.md#encrypted-data-key), then it MUST yield an error
      //# that includes all the collected errors.
      .MapFailure(errors => Types.CollectionOfErrors(
                      list := errors,
                      message := "No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."
                    )
      );

      assert decryptClosure.Ensures(Last(attempts).input, Success(SealedDecryptionMaterials), DropLast(attempts));
      return Success(Types.OnDecryptOutput(
                       materials := SealedDecryptionMaterials
                     ));
    }

    method GetActiveCacheId(
      branchKeyId: string,
      branchKeyIdUtf8: seq<uint8>,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    )
      returns (cacheId: Result<seq<uint8>, Types.Error>)

      requires cryptoPrimitives.ValidState()
      modifies cryptoPrimitives.Modifies
      ensures cryptoPrimitives.ValidState()
      ensures cacheId.Success? ==> |cacheId.value| == 48
    {
      SequenceIsSafeBecauseItIsInMemory(branchKeyId);
      :- Need(
        && var branchKeyId := UTF8.Decode(branchKeyIdUtf8);
        && branchKeyId.Success?
        && (SequenceIsSafeBecauseItIsInMemory(branchKeyId.value); 0 <= |branchKeyId.value| as uint64 < UINT32_LIMIT as uint64),
        E("Invalid Branch Key ID Length")
      );
      // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#encryption-materials
      //# When the hierarchical keyring receives an OnEncrypt request,
      //# the cache entry identifier MUST be calculated as the
      //# SHA-384 hash of the following byte strings, in the order listed:
      // (blank line for duvet)
      //# - MUST be the Resource ID for the Hierarchical Keyring (0x02)
      //# - MUST be the Scope ID for Encrypt (0x01)
      //# - MUST be the Partition ID for the Hierarchical Keyring
      //# - Resource Suffix
      //#   - MUST be the UTF8 encoded Logical Key Store Name of the keystore for the Hierarchical Keyring
      //#   - MUST be the UTF8 encoded branch-key-id
      // (blank line for duvet)
      //# All the above fields must be separated by a single NULL_BYTE `0x00`.

      var hashAlgorithm := Crypto.DigestAlgorithm.SHA_384;

      // Resource ID: Hierarchical Keyring [0x02]
      var resourceId : seq<uint8> := RESOURCE_ID_HIERARCHICAL_KEYRING;

      // Scope ID: Encryption [0x01]
      var scopeId : seq<uint8> := SCOPE_ID_ENCRYPT;

      // Create the Suffix
      var suffix : seq<uint8> := logicalKeyStoreNameBytes + NULL_BYTE + branchKeyIdUtf8;

      // Append Resource Id, Scope Id, Partition Id, and Suffix to create the cache identifier
      var identifier := resourceId + NULL_BYTE + scopeId + NULL_BYTE + partitionIdBytes + NULL_BYTE + suffix;

      var maybeCacheIdDigest := cryptoPrimitives
      .Digest(Crypto.DigestInput(digestAlgorithm := hashAlgorithm, message := identifier));
      var cacheDigest :- maybeCacheIdDigest
      .MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      SequenceIsSafeBecauseItIsInMemory(cacheDigest);
      :- Need(
        |cacheDigest| as uint64 == Digest.Length(hashAlgorithm) as uint64,
        Types.AwsCryptographicMaterialProvidersException(
          message := "Digest generated a message not equal to the expected length.")
      );

      return Success(cacheDigest);
    }

    method GetActiveHierarchicalMaterials(
      branchKeyId: string,
      cacheId: seq<uint8>,
      keyStore: KeyStore.IKeyStoreClient
    )
      returns (material: Result<KeyStore.BranchKeyMaterials, Types.Error>)
      requires ValidState()
      requires keyStore.ValidState() && cache.ValidState()
      modifies keyStore.Modifies, cache.Modifies
      ensures ValidState()
      ensures keyStore.ValidState() && cache.ValidState()
    {
      // call cache
      var getCacheInput := Types.GetCacheEntryInput(identifier := cacheId, bytesUsed := None);
      var getCacheOutput := cache.GetCacheEntry(getCacheInput);

      // If error is not EntryDoesNotExist, return Failure
      if (getCacheOutput.Failure? && !getCacheOutput.error.EntryDoesNotExist?) {
        return Failure(getCacheOutput.error);
      }

      var now := Time.GetCurrent();

      // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#onencrypt
      //# If using a `Shared` cache across multiple Hierarchical Keyrings,
      //# different keyrings having the same `branchKey` can have different TTLs.
      //# In such a case, the expiry time in the cache is set according to the Keyring that populated the cache.
      //# There MUST be a check (cacheEntryWithinLimits) to make sure that for the cache entry found, who's TTL has NOT expired,
      //# `time.now() - cacheEntryCreationTime <= ttlSeconds` is true and
      //# valid for TTL of the Hierarchical Keyring getting the cache entry.
      //# If this is NOT true, then we MUST treat the cache entry as expired.
      if getCacheOutput.Failure? || !cacheEntryWithinLimits(
           creationTime := getCacheOutput.value.creationTime,
           now := now,
           ttlSeconds := ttlSeconds
         )
      {
        var maybeGetActiveBranchKeyOutput := keyStore.GetActiveBranchKey(
          KeyStore.GetActiveBranchKeyInput(
            branchKeyIdentifier := branchKeyId
          )
        );
        var getActiveBranchKeyOutput :- maybeGetActiveBranchKeyOutput
        .MapFailure(e => Types.AwsCryptographyKeyStore(AwsCryptographyKeyStore := e));

        var branchKeyMaterials := getActiveBranchKeyOutput.branchKeyMaterials;

        var now := Time.GetCurrent();
        :- Need(
          (now as int + ttlSeconds as int) < UInt.INT64_MAX_LIMIT,
          Types.AwsCryptographicMaterialProvidersException(message := "INT64 Overflow when putting cache entry.")
        );

        var putCacheEntryInput:= Types.PutCacheEntryInput(
          identifier := cacheId,
          materials := Types.Materials.BranchKey(branchKeyMaterials),
          creationTime := now,
          expiryTime := ttlSeconds + now,
          messagesUsed := None,
          bytesUsed := None
        );

        var putResult := cache.PutCacheEntry(putCacheEntryInput);
        if (putResult.Failure? && !putResult.error.EntryAlreadyExists?) {
          return Failure(putResult.error);
        }

        return Success(branchKeyMaterials);
      } else {
        :- Need(getCacheOutput.value.materials.BranchKey?, E("Invalid Material Type."));
        return Success(getCacheOutput.value.materials.BranchKey);
      }
    }
  }

  method DeriveEncryptionKeyFromBranchKey(
    branchKey: seq<uint8>,
    salt: seq<uint8>,
    purpose: Option<seq<uint8>>,
    cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
  )
    returns (output: Result<seq<uint8>, Types.Error>)

    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()
    ensures output.Success? ==> |output.value| == 32
    ensures |cryptoPrimitives.History.GenerateRandomBytes| == old(|cryptoPrimitives.History.GenerateRandomBytes|)
    ensures |cryptoPrimitives.History.KdfCounterMode| > 0
  {
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
    //# 3. Use a [KDF in Counter Mode with a Pseudo Random Function with HMAC SHA 256]
    //# (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1.pdf)
    var maybeDerivedBranchKey := cryptoPrimitives.KdfCounterMode(
      Crypto.KdfCtrInput(
        digestAlgorithm := Crypto.DigestAlgorithm.SHA_256,
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
        //# - Use the branch key as the `key`.
        ikm := branchKey,
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
        //# to derive a 32 byte `derivedBranchKey`
        expectedLength := DERIVED_BRANCH_KEY_EXPECTED_LENGTH,
        purpose := purpose,
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
        //# - Use the `salt` as the salt.
        nonce := Some(salt)
      )
    );
    var derivedBranchKey :- maybeDerivedBranchKey.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));
    output := Success(derivedBranchKey);
  }

  function method {:opaque} WrappingAad(
    branchKeyId: seq<uint8>,
    branchKeyVersion: seq<uint8>,
    aad: seq<uint8>
  ): (res : seq<uint8>)
    requires UTF8.ValidUTF8Seq(branchKeyId)
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping-and-unwrapping-aad
    //= type=implication
    //# To construct the AAD, the keyring MUST concatenate the following values
    //  1. "aws-kms-hierarchy" as UTF8 Bytes
    //  1. Value of `branch-key-id` as UTF8 Bytes
    //  1. [version](../structures.md#branch-key-version) as Bytes
    //  1. [encryption context](structures.md#encryption-context-1) from the input
    //     [encryption materials](../structures.md#encryption-materials) according to the [encryption context serialization specification](../structures.md#serialization).
    ensures res == PROVIDER_ID_HIERARCHY + branchKeyId + branchKeyVersion + aad
    // branchKeyVersion is stored as UTF8 Bytes in the materials.
    // Store it as raw bytes in the materials so that we can encode it once per call.
  {
    PROVIDER_ID_HIERARCHY + branchKeyId + branchKeyVersion + aad
  }

  class OnDecryptHierarchyEncryptedDataKeyFilter
    extends DeterministicActionWithResult<Types.EncryptedDataKey, bool, Types.Error>
  {
    const branchKeyId: string

    constructor(
      branchKeyId: string
    )
    {
      this.branchKeyId := branchKeyId;
    }

    predicate Ensures(
      edk: Types.EncryptedDataKey,
      res: Result<bool, Types.Error>
    ) {
      && (
        && res.Success?
        && res.value
        ==>
          && edk.keyProviderId == PROVIDER_ID_HIERARCHY
          && UTF8.ValidUTF8Seq(edk.keyProviderInfo)
      )
    }

    method Invoke(edk: Types.EncryptedDataKey)
      returns (res: Result<bool, Types.Error>)
      ensures Ensures(edk, res)
    {
      var providerInfo := edk.keyProviderInfo;
      var providerId := edk.keyProviderId;

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ondecrypt
      //# - Its provider ID MUST match the UTF8 Encoded value of “aws-kms-hierarchy”.
      if providerId != PROVIDER_ID_HIERARCHY {
        return Success(false);
      }

      // We filter out values that do not match,
      // Therefore we know that this provider ID is UTF8 encoded
      assert UTF8.ValidUTF8Seq(PROVIDER_ID_HIERARCHY);
      assert providerId == PROVIDER_ID_HIERARCHY;

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ondecrypt
      //# -- The deserialized key provider info MUST be UTF8 Decoded
      var branchKeyId :- UTF8.Decode(providerInfo).MapFailure(e => E("Invalid encoding, provider info is not UTF8."));

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ondecrypt
      //#  MUST match this keyring's configured `Branch Key Identifier`.
      return Success(this.branchKeyId == branchKeyId);
    }
  }

  class DecryptSingleEncryptedDataKey
    extends ActionWithResult<
      Types.EncryptedDataKey,
      Materials.SealedDecryptionMaterials,
      Types.Error>
  {
    const materials: Materials.DecryptionMaterialsPendingPlaintextDataKey
    const keyStore: KeyStore.IKeyStoreClient
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    const branchKeyId: string
    const ttlSeconds: Types.PositiveLong
    const cache: Types.ICryptographicMaterialsCache
    const partitionIdBytes: seq<uint8>
    const logicalKeyStoreNameBytes: seq<uint8>

    constructor(
      materials: Materials.DecryptionMaterialsPendingPlaintextDataKey,
      keyStore: KeyStore.IKeyStoreClient,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient,
      branchKeyId: string,
      ttlSeconds: Types.PositiveLong,
      cache: Types.ICryptographicMaterialsCache,
      partitionIdBytes: seq<uint8>,
      logicalKeyStoreNameBytes: seq<uint8>
    )
      requires keyStore.ValidState() && cryptoPrimitives.ValidState() && cache.ValidState()
      ensures
        && this.materials == materials
        && this.keyStore == keyStore
        && this.cryptoPrimitives == cryptoPrimitives
        && this.branchKeyId == branchKeyId
        && this.ttlSeconds == ttlSeconds
        && this.cache == cache
        && this.partitionIdBytes == partitionIdBytes
        && this.logicalKeyStoreNameBytes == logicalKeyStoreNameBytes
      ensures Invariant()
    {
      this.materials := materials;
      this.keyStore := keyStore;
      this.cryptoPrimitives := cryptoPrimitives;
      this.branchKeyId := branchKeyId;
      this.ttlSeconds := ttlSeconds;
      this.cache := cache;
      this.partitionIdBytes := partitionIdBytes;
      this.logicalKeyStoreNameBytes := logicalKeyStoreNameBytes;
      Modifies := keyStore.Modifies + cryptoPrimitives.Modifies + cache.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && keyStore.ValidState()
      && cryptoPrimitives.ValidState()
      && cache.ValidState()
      && keyStore.Modifies + cryptoPrimitives.Modifies + cache.Modifies == Modifies
    }

    predicate Ensures(
      edk: Types.EncryptedDataKey,
      res: Result<Materials.SealedDecryptionMaterials, Types.Error>,
      attemptsState: seq<ActionInvoke<Types.EncryptedDataKey, Result<Materials.SealedDecryptionMaterials, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
        && Materials.DecryptionMaterialsTransitionIsValid(materials, res.value)

    }

    predicate Requires(edk: Types.EncryptedDataKey){
      && UTF8.ValidUTF8Seq(edk.keyProviderInfo)
    }
    method Invoke(
      edk: Types.EncryptedDataKey,
      ghost attemptsState: seq<ActionInvoke<Types.EncryptedDataKey, Result<Materials.SealedDecryptionMaterials, Types.Error>>>
    ) returns (res: Result<Materials.SealedDecryptionMaterials, Types.Error>)
      requires Invariant()
      requires Requires(edk)
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(edk, res, attemptsState)
    {

      assert UTF8.ValidUTF8Seq(edk.keyProviderId);

      var suite := materials.algorithmSuite;
      var keyProviderId := edk.keyProviderId;
      var branchKeyIdUtf8 := edk.keyProviderInfo;
      var ciphertext := edk.ciphertext;

      var providerWrappedMaterial :- EdkWrapping.GetProviderWrappedMaterial(ciphertext, suite);
      SequenceIsSafeBecauseItIsInMemory(providerWrappedMaterial);
      :- Need (
        |providerWrappedMaterial| as uint64 >= EDK_CIPHERTEXT_VERSION_INDEX as uint64,
        Types.AwsCryptographicMaterialProvidersException(message := "Received EDK Ciphertext of incorrect length.")
      );
      var branchKeyVersionUuid := providerWrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX..EDK_CIPHERTEXT_VERSION_INDEX];
      var version :- UUID.FromByteArray(branchKeyVersionUuid).MapFailure(WrapStringToError);

      var cacheId :- GetVersionCacheId(branchKeyIdUtf8, version, cryptoPrimitives);
      var hierarchicalMaterials :- GetHierarchicalMaterialsVersion(branchKeyId, branchKeyIdUtf8, version, cacheId);
      var branchKey := hierarchicalMaterials.branchKey;
      var branchKeyVersion := hierarchicalMaterials.branchKeyVersion;
      var branchKeyVersionAsString :- UTF8.Decode(branchKeyVersion).MapFailure(WrapStringToError);
      var branchKeyVersionAsBytes :- UUID.ToByteArray(branchKeyVersionAsString).MapFailure(WrapStringToError);

      // We need to create a new client here so that we can reason about the state of the client
      // down the line. This is ok because the only state tracked is the client's history.
      var maybeCrypto := AtomicPrimitives.AtomicPrimitives();
      var cryptoPrimitivesX : Crypto.IAwsCryptographicPrimitivesClient :- maybeCrypto
      .MapFailure(e => Types.AwsCryptographyPrimitives(e));
      assert cryptoPrimitivesX is AtomicPrimitives.AtomicPrimitivesClient;
      var cryptoPrimitives := cryptoPrimitivesX as AtomicPrimitives.AtomicPrimitivesClient;

      var kmsHierarchyUnwrap := new KmsHierarchyUnwrapKeyMaterial(
        branchKey,
        branchKeyIdUtf8,
        branchKeyVersionAsBytes,
        cryptoPrimitives
      );

      var unwrapOutputRes := EdkWrapping.UnwrapEdkMaterial(
        edk.ciphertext,
        materials,
        kmsHierarchyUnwrap
      );

      var unwrapOutput :- unwrapOutputRes;

      var result :- Materials.DecryptionMaterialsAddDataKey(materials, unwrapOutput.plaintextDataKey, unwrapOutput.symmetricSigningKey);
      return Success(result);
    }

    method GetVersionCacheId(
      branchKeyIdUtf8: seq<uint8>, // The branch key as Bytes
      branchKeyVersion: string,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    )
      returns (cacheId: Result<seq<uint8>, Types.Error>)
      ensures cacheId.Success? ==> |cacheId.value| == 48
    {
      SequenceIsSafeBecauseItIsInMemory(branchKeyId);
      :- Need(
        && var branchKeyId := UTF8.Decode(branchKeyIdUtf8);
        && branchKeyId.Success?
        && (SequenceIsSafeBecauseItIsInMemory(branchKeyId.value); 0 <= |branchKeyId.value| as uint64 < UINT32_LIMIT as uint64),
        E("Invalid Branch Key ID Length")
      );
      // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#decryption-materials
      //# When the hierarchical keyring receives an OnDecrypt request,
      //# it MUST calculate the cache entry identifier as the
      //# SHA-384 hash of the following byte strings, in the order listed:
      // (blank line for duvet)
      //# - MUST be the Resource ID for the Hierarchical Keyring (0x02)
      //# - MUST be the Scope ID for Decrypt (0x02)
      //# - MUST be the Partition ID for the Hierarchical Keyring
      //# - Resource Suffix
      //#   - MUST be the UTF8 encoded Logical Key Store Name of the keystore for the Hierarchical Keyring
      //#   - MUST be the UTF8 encoded branch-key-id
      //#   - MUST be the UTF8 encoded branch-key-version
      // (blank line for duvet)
      //# All the above fields must be separated by a single NULL_BYTE `0x00`.

      var hashAlgorithm := Crypto.DigestAlgorithm.SHA_384;

      // Resource ID: Hierarchical Keyring [0x02]
      var resourceId : seq<uint8> := RESOURCE_ID_HIERARCHICAL_KEYRING;

      // Scope ID: Decryption [0x02]
      var scopeId : seq<uint8> := SCOPE_ID_DECRYPT;

        // Convert branch key version into UTF8 bytes
      :- Need(
        UTF8.IsASCIIString(branchKeyVersion),
        E("Unable to represent as an ASCII string.")
      );
      var versionBytes :- UTF8.Encode(branchKeyVersion).MapFailure(e => Types.AwsCryptographicMaterialProvidersException(message := e));

      // Create the suffix
      var suffix : seq<uint8> := logicalKeyStoreNameBytes + NULL_BYTE + branchKeyIdUtf8 + NULL_BYTE + versionBytes;

      // Append Resource Id, Scope Id, Partition Id, and Suffix to create the cache identifier
      var identifier := resourceId + NULL_BYTE + scopeId + NULL_BYTE + partitionIdBytes + NULL_BYTE + suffix;

      var identifierDigestInput := Crypto.DigestInput(
        digestAlgorithm := hashAlgorithm, message := identifier
      );
      var maybeCacheDigest := Digest.Digest(identifierDigestInput);
      var cacheDigest :- maybeCacheDigest.MapFailure(e => Types.AwsCryptographyPrimitives(e));

      assert |cacheDigest| == Digest.Length(hashAlgorithm) as nat;

      return Success(cacheDigest);
    }

    method GetHierarchicalMaterialsVersion(
      branchKeyId: string,
      branchKeyIdUtf8: seq<uint8>,
      version: string,
      cacheId: seq<uint8>
    )
      returns (material: Result<KeyStore.BranchKeyMaterials, Types.Error>)
      requires Invariant()
      requires keyStore.ValidState() && cache.ValidState()
      modifies keyStore.Modifies, cache.Modifies
      ensures keyStore.ValidState() && cache.ValidState()
    {
      // call cache
      var getCacheInput := Types.GetCacheEntryInput(identifier := cacheId, bytesUsed := None);
      var getCacheOutput := cache.GetCacheEntry(getCacheInput);
      if (getCacheOutput.Failure? && !getCacheOutput.error.EntryDoesNotExist?) {
        return Failure(getCacheOutput.error);
      }

      var now := Time.GetCurrent();

      // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#ondecrypt
      //# If using a `Shared` cache across multiple Hierarchical Keyrings,
      //# different keyrings having the same `branchKey` can have different TTLs.
      //# In such a case, the expiry time in the cache is set according to the Keyring that populated the cache.
      //# There MUST be a check (cacheEntryWithinLimits) to make sure that for the cache entry found, who's TTL has NOT expired,
      //# `time.now() - cacheEntryCreationTime <= ttlSeconds` is true and
      //# valid for TTL of the Hierarchical Keyring getting the cache entry.
      //# If this is NOT true, then we MUST treat the cache entry as expired.
      if getCacheOutput.Failure? || !cacheEntryWithinLimits(
           creationTime := getCacheOutput.value.creationTime,
           now := now,
           ttlSeconds := ttlSeconds
         )
      {
        var maybeGetBranchKeyVersionOutput := keyStore.GetBranchKeyVersion(
          KeyStore.GetBranchKeyVersionInput(
            branchKeyIdentifier := branchKeyId,
            branchKeyVersion := version
          )
        );

        var getBranchKeyVersionOutput :- maybeGetBranchKeyVersionOutput
        .MapFailure(e => Types.AwsCryptographyKeyStore(AwsCryptographyKeyStore := e));

        var branchKeyMaterials := getBranchKeyVersionOutput.branchKeyMaterials;

        var now := Time.GetCurrent();
        :- Need(
          (now as int + ttlSeconds as int) < UInt.INT64_MAX_LIMIT,
          Types.AwsCryptographicMaterialProvidersException(message := "INT64 Overflow when putting cache entry.")
        );

        var putCacheEntryInput:= Types.PutCacheEntryInput(
          identifier := cacheId,
          materials := Types.Materials.BranchKey(branchKeyMaterials),
          creationTime := now,
          expiryTime := ttlSeconds + now,
          messagesUsed := None,
          bytesUsed := None
        );

        var putResult := cache.PutCacheEntry(putCacheEntryInput);
        if (putResult.Failure? && !putResult.error.EntryAlreadyExists?) {
          return Failure(putResult.error);
        }

        return Success(branchKeyMaterials);
      } else {
        :- Need(getCacheOutput.value.materials.BranchKey?, E("Invalid Material Type."));
        return Success(getCacheOutput.value.materials.BranchKey);
      }
    }
  }

  datatype HierarchyUnwrapInfo = HierarchyUnwrapInfo()
  datatype HierarchyWrapInfo = HierarchyWrapInfo()

  class KmsHierarchyUnwrapKeyMaterial
    extends MaterialWrapping.UnwrapMaterial<HierarchyUnwrapInfo>
  {
    const branchKey: seq<uint8>
    const branchKeyIdUtf8 : UTF8.ValidUTF8Bytes
    const branchKeyVersionAsBytes: seq<uint8>
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      branchKey: seq<uint8>,
      branchKeyIdUtf8: UTF8.ValidUTF8Bytes,
      branchKeyVersionAsBytes: seq<uint8>,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.branchKey == branchKey
        && this.branchKeyIdUtf8 == branchKeyIdUtf8
        && this.branchKeyVersionAsBytes == branchKeyVersionAsBytes
        && this.crypto == crypto
      ensures Invariant()
    {
      this.branchKey := branchKey;
      this.branchKeyIdUtf8 := branchKeyIdUtf8;
      this.branchKeyVersionAsBytes := branchKeyVersionAsBytes;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    predicate Ensures(
      input: MaterialWrapping.UnwrapInput,
      res: Result<MaterialWrapping.UnwrapOutput<HierarchyUnwrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<HierarchyUnwrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
        && var KeyLength := AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite);
        && |input.wrappedMaterial| == EXPECTED_EDK_CIPHERTEXT_OVERHEAD as int + KeyLength as int
        && |crypto.History.AESDecrypt| > 0
        && Seq.Last(crypto.History.AESDecrypt).output.Success?
        && var AESDecryptInput := Seq.Last(crypto.History.AESDecrypt).input;
        && var AESDecryptOutput := Seq.Last(crypto.History.AESDecrypt).output.value;
        && var wrappedMaterial := input.wrappedMaterial;
        && var aad := input.encryptionContext;
        && var salt := wrappedMaterial[..H_WRAP_SALT_LEN];
        && var iv := wrappedMaterial[H_WRAP_SALT_LEN..EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX];
        && var branchKeyVersionUuid := wrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX..EDK_CIPHERTEXT_VERSION_INDEX];
        && var wrappedKey := wrappedMaterial[EDK_CIPHERTEXT_VERSION_INDEX..EDK_CIPHERTEXT_VERSION_INDEX + KeyLength];
        && var authTag := wrappedMaterial[EDK_CIPHERTEXT_VERSION_INDEX + KeyLength..];
        && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
        && var serializedEC := CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).value;
        && var wrappingAad := WrappingAad(branchKeyIdUtf8, branchKeyVersionAsBytes, serializedEC);
        // Since we can't call a method here in the predicate we can't derive the key here
        // but we can make sure that the rest of the construction is correct.
        && AESDecryptInput.encAlg == AES_256_ENC_ALG
        && AESDecryptInput.cipherTxt == wrappedKey
        && AESDecryptInput.authTag == authTag
        && AESDecryptInput.iv == iv
        && AESDecryptInput.aad == wrappingAad
        && AESDecryptOutput == res.value.unwrappedMaterial
    }

    method Invoke(
      input: MaterialWrapping.UnwrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<HierarchyUnwrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.UnwrapOutput<HierarchyUnwrapInfo>, Types.Error>)
      requires Invariant()
      requires Requires(input)
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==>
                |res.value.unwrappedMaterial| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat
    {
      var suite := input.algorithmSuite;
      var wrappedMaterial := input.wrappedMaterial;
      var aad := input.encryptionContext;

      var KeyLength := AlgorithmSuites.GetEncryptKeyLength(suite);

      SequenceIsSafeBecauseItIsInMemory(wrappedMaterial);
      :- Need (
        // Salt = 16, IV = 12, Version = 16, Authentication Tag = 16 + Encrypted Key Length
        |wrappedMaterial| as uint64 == EXPECTED_EDK_CIPHERTEXT_OVERHEAD as uint64 + KeyLength as uint64,
        Types.AwsCryptographicMaterialProvidersException(message := "Received EDK Ciphertext of incorrect length2.")
      );

      var salt := wrappedMaterial[..H_WRAP_SALT_LEN];
      var iv := wrappedMaterial[H_WRAP_SALT_LEN..EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX];
      var branchKeyVersionUuid := wrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX..EDK_CIPHERTEXT_VERSION_INDEX];
      var wrappedKey := wrappedMaterial[EDK_CIPHERTEXT_VERSION_INDEX.. EDK_CIPHERTEXT_VERSION_INDEX + KeyLength];
      var authTag := wrappedMaterial[EDK_CIPHERTEXT_VERSION_INDEX + KeyLength..];

      var serializedEC :- input.serializedEC;
      var wrappingAad := WrappingAad(branchKeyIdUtf8, branchKeyVersionAsBytes, serializedEC);
      var derivedBranchKey :- DeriveEncryptionKeyFromBranchKey(
        branchKey,
        salt,
        Some(PROVIDER_ID_HIERARCHY),
        crypto
      );

      var maybeUnwrappedPdk :=  crypto.AESDecrypt(
        Crypto.AESDecryptInput(
          encAlg := AES_256_ENC_ALG,
          key := derivedBranchKey,
          cipherTxt := wrappedKey,
          authTag := authTag,
          iv := iv,
          aad := wrappingAad
        )
      );
      var unwrappedPdk :- maybeUnwrappedPdk.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      assert |unwrappedPdk| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat;

      var output := MaterialWrapping.UnwrapOutput(
        unwrappedMaterial := unwrappedPdk,
        unwrapInfo := HierarchyUnwrapInfo()
      );

      return Success(output);
    }
  }

  class KmsHierarchyGenerateAndWrapKeyMaterial
    extends MaterialWrapping.GenerateAndWrapMaterial<HierarchyWrapInfo>
  {
    const branchKey: seq<uint8>
    const branchKeyIdUtf8 : UTF8.ValidUTF8Bytes
    const branchKeyVersionAsBytes: seq<uint8>
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      branchKey: seq<uint8>,
      branchKeyIdUtf8 : UTF8.ValidUTF8Bytes,
      branchKeyVersionAsBytes: seq<uint8>,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.branchKey == branchKey
        && this.branchKeyIdUtf8 == branchKeyIdUtf8
        && this.branchKeyVersionAsBytes == branchKeyVersionAsBytes
        && this.crypto == crypto
      ensures Invariant()
    {
      this.branchKey := branchKey;
      this.branchKeyIdUtf8 := branchKeyIdUtf8;
      this.branchKeyVersionAsBytes := branchKeyVersionAsBytes;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    predicate Ensures(
      input: MaterialWrapping.GenerateAndWrapInput,
      res: Result<MaterialWrapping.GenerateAndWrapOutput<HierarchyWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<HierarchyWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
    }

    method Invoke(
      input: MaterialWrapping.GenerateAndWrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<HierarchyWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.GenerateAndWrapOutput<HierarchyWrapInfo>, Types.Error>)
      requires Invariant()
      requires Requires(input)
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==> |res.value.plaintextMaterial| == input.algorithmSuite.encrypt.AES_GCM.keyLength as nat
    {
      var suite := input.algorithmSuite;
      var pdkResult := crypto
      .GenerateRandomBytes(Crypto.GenerateRandomBytesInput(length := GetEncryptKeyLength(suite)));
      var pdk :- pdkResult.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      var wrap := new KmsHierarchyWrapKeyMaterial(
        branchKey,
        branchKeyIdUtf8,
        branchKeyVersionAsBytes,
        crypto
      );

      var wrapOutput: MaterialWrapping.WrapOutput<HierarchyWrapInfo> :- wrap.Invoke(
        MaterialWrapping.WrapInput(
          plaintextMaterial := pdk,
          algorithmSuite := input.algorithmSuite,
          encryptionContext := input.encryptionContext,
          serializedEC := input.serializedEC
        ), []);

      var output := MaterialWrapping.GenerateAndWrapOutput(
        plaintextMaterial := pdk,
        wrappedMaterial := wrapOutput.wrappedMaterial,
        wrapInfo := HierarchyWrapInfo()
      );
      return Success(output);
    }

  }

  class KmsHierarchyWrapKeyMaterial
    extends MaterialWrapping.WrapMaterial<HierarchyWrapInfo>
  {
    const branchKey: seq<uint8>
    const branchKeyIdUtf8 : UTF8.ValidUTF8Bytes
    const branchKeyVersionAsBytes: seq<uint8>
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      branchKey: seq<uint8>,
      branchKeyIdUtf8 : UTF8.ValidUTF8Bytes,
      branchKeyVersionAsBytes: seq<uint8>,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.branchKey == branchKey
        && this.branchKeyIdUtf8 == branchKeyIdUtf8
        && this.branchKeyVersionAsBytes == branchKeyVersionAsBytes
        && this.crypto == crypto
      ensures Invariant()
    {
      this.branchKey := branchKey;
      this.branchKeyIdUtf8 := branchKeyIdUtf8;
      this.branchKeyVersionAsBytes := branchKeyVersionAsBytes;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    predicate Ensures(
      input: MaterialWrapping.WrapInput,
      res: Result<MaterialWrapping.WrapOutput<HierarchyWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<HierarchyWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      && (
        res.Success?
        ==>
          && Invariant()
          && 0 < |crypto.History.AESEncrypt|
          && Seq.Last(crypto.History.AESEncrypt).output.Success?
          && var AESEncryptInput := Seq.Last(crypto.History.AESEncrypt).input;
          && var AESEncryptOutput := Seq.Last(crypto.History.AESEncrypt).output.value;
          && CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Success?
          && var serializedEC := CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext);
          && var wrappingAad := WrappingAad(branchKeyIdUtf8, branchKeyVersionAsBytes, serializedEC.value);
          && AESEncryptInput.encAlg == AES_256_ENC_ALG
          && AESEncryptInput.msg == input.plaintextMaterial
          && AESEncryptInput.aad == wrappingAad
          && |res.value.wrappedMaterial| > |AESEncryptOutput.cipherText| + |AESEncryptOutput.authTag|
          && res.value.wrapInfo == HierarchyWrapInfo()
      )
    }

    method Invoke(
      input: MaterialWrapping.WrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<HierarchyWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.WrapOutput<HierarchyWrapInfo>, Types.Error>)
      requires Invariant()
      requires Requires(input)
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
    {
      var suite := input.algorithmSuite;

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
      //# The hierarchical keyring MUST:
      // (blank line for duvet)
      //# 1. Generate a 16 byte random salt using a secure source of randomness
      //# 1. Generate a 12 byte random iv using a secure source of randomness
      var maybeNonceSalt := crypto.GenerateRandomBytes(
        Crypto.GenerateRandomBytesInput(length := H_WRAP_SALT_LEN + H_WRAP_NONCE_LEN)
      );
      var saltAndNonce :- maybeNonceSalt.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      assert |crypto.History.GenerateRandomBytes| == old(|crypto.History.GenerateRandomBytes|) + 1;
      assert |saltAndNonce| == (H_WRAP_NONCE_LEN + H_WRAP_SALT_LEN) as int;

      var salt := saltAndNonce[..H_WRAP_SALT_LEN];
      var nonce := saltAndNonce[H_WRAP_SALT_LEN..];

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping-and-unwrapping-aad
      //# To Encrypt and Decrypt the `wrappedDerivedBranchKey` the keyring MUST include the following values as part of the AAD for
      //# the AES Encrypt/Decrypt calls.
      //  1. "aws-kms-hierarchy" as UTF8 Bytes
      //  1. Value of `branch-key-id` as UTF8 Bytes
      //  1. [version](../structures.md#branch-key-version) as Bytes
      //  1. [encryption context](structures.md#encryption-context-1) from the input
      //     [encryption materials](../structures.md#encryption-materials) according to the [encryption context serialization specification](../structures.md#serialization).
      var serializedEC :- input.serializedEC;
      var wrappingAad := WrappingAad(branchKeyIdUtf8, branchKeyVersionAsBytes, serializedEC);

      var derivedBranchKey :- DeriveEncryptionKeyFromBranchKey(
        branchKey,
        salt,
        Some(PROVIDER_ID_HIERARCHY),
        crypto
      );

      var maybeWrappedPdk := crypto.AESEncrypt(
        Crypto.AESEncryptInput(
          //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
          //# 1. Encrypt a plaintext data key with the `derivedBranchKey` using
          //# `AES-GCM-256` with the following inputs:
          encAlg := AES_256_ENC_ALG,
          //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
          //# MUST use the derived `IV` as the AES-GCM IV.
          iv := nonce,
          //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
          //# MUST use the `derivedBranchKey` as the AES-GCM cipher key.
          key := derivedBranchKey,
          //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
          //# MUST use the plain text data key that will be wrapped by the `derivedBranchKey` as the AES-GCM message.
          msg := input.plaintextMaterial,
          //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#branch-key-wrapping
          //# - MUST use the serialized [AAD](#branch-key-wrapping-and-unwrapping-aad) as the AES-GCM AAD.
          aad := wrappingAad
        )
      );
      var wrappedPdk :- maybeWrappedPdk.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      var output := MaterialWrapping.WrapOutput(
        wrappedMaterial := salt + nonce +  branchKeyVersionAsBytes + wrappedPdk.cipherText + wrappedPdk.authTag,
        wrapInfo := HierarchyWrapInfo()
      );
      return Success(output);
    }
  }

  function method SerializeEDKCiphertext(encOutput: Crypto.AESEncryptOutput): (ciphertext: seq<uint8>) {
    encOutput.cipherText + encOutput.authTag
  }

  function method E(s : string) : Types.Error {
    Types.AwsCryptographicMaterialProvidersException(message := s)
  }

}
