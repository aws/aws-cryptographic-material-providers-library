// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

include "Keyrings/AwsKms/StrictMultiKeyring.dfy"
include "Keyrings/MultiKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsEcdhKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsHierarchicalKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsUtils.dfy"
include "Keyrings/AwsKms/AwsKmsDiscoveryKeyring.dfy"
include "Keyrings/AwsKms/DiscoveryMultiKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsMrkKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsUtils.dfy"
include "Keyrings/AwsKms/MrkAwareStrictMultiKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsMrkDiscoveryKeyring.dfy"
include "Keyrings/AwsKms/MrkAwareDiscoveryMultiKeyring.dfy"
include "Keyrings/AwsKms/AwsKmsRsaKeyring.dfy"
include "Keyrings/RawAESKeyring.dfy"
include "Keyrings/RawRSAKeyring.dfy"
include "Keyrings/RawECDHKeyring.dfy"
include "CMMs/DefaultCMM.dfy"
include "CMCs/LocalCMC.dfy"
include "CMCs/SynchronizedLocalCMC.dfy"
include "CMCs/StormTracker.dfy"
include "CMCs/StormTrackingCMC.dfy"
include "DefaultClientSupplier.dfy"
include "Materials.dfy"
include "Commitment.dfy"
include "AwsArnParsing.dfy"
include "AlgorithmSuites.dfy"
include "CMMs/RequiredEncryptionContextCMM.dfy"
include "Utils.dfy"

module AwsCryptographyMaterialProvidersOperations refines AbstractAwsCryptographyMaterialProvidersOperations {

  import MultiKeyring
  import opened S = StrictMultiKeyring
  import opened D = DiscoveryMultiKeyring
  import opened MD = MrkAwareDiscoveryMultiKeyring
  import opened M = MrkAwareStrictMultiKeyring
  import opened StandardLibrary.MemoryMath
  import AwsKmsKeyring
  import AwsKmsHierarchicalKeyring
  import AwsKmsMrkKeyring
  import AwsKmsDiscoveryKeyring
  import AwsKmsMrkDiscoveryKeyring
  import AwsKmsRsaKeyring
  import AwsKmsEcdhKeyring
  import RawAESKeyring
  import RawRSAKeyring
  import RawECDHKeyring
  import opened C = DefaultCMM
  import LocalCMC
  import SynchronizedLocalCMC
  import StormTracker
  import StormTrackingCMC
  import Crypto = AwsCryptographyPrimitivesTypes
  import AtomicPrimitives
  import opened AwsKmsUtils
  import DefaultClientSupplier
  import Materials
  import Commitment
  import AlgorithmSuites
  import opened AwsArnParsing
  import opened Utils
  import Kms = Com.Amazonaws.Kms
  import Ddb = ComAmazonawsDynamodbTypes
  import RequiredEncryptionContextCMM
  import UUID
  import StandardLibrary.String

  datatype Config = Config(
    nameonly crypto: AtomicPrimitives.AtomicPrimitivesClient
  )

  type InternalConfig = Config

  predicate ValidInternalConfig?(config: InternalConfig)
  {
    && config.crypto.ValidState()
  }

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {
    config.crypto.Modifies
  }

  predicate CreateAwsKmsKeyringEnsuresPublicly(input: CreateAwsKmsKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsKeyring(config: InternalConfig, input: CreateAwsKmsKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    var _ :- ValidateKmsKeyId(input.kmsKeyId);
    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var keyring := new AwsKmsKeyring.AwsKmsKeyring(input.kmsClient, input.kmsKeyId, grantTokens);
    return Success(keyring);
  }

  predicate CreateAwsKmsDiscoveryKeyringEnsuresPublicly(input: CreateAwsKmsDiscoveryKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsDiscoveryKeyring(config: InternalConfig, input: CreateAwsKmsDiscoveryKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    if input.discoveryFilter.Some? {
      var _ :- ValidateDiscoveryFilter(input.discoveryFilter.value);
    }
    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var keyring := new AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring(input.kmsClient, input.discoveryFilter, grantTokens);
    return Success(keyring);
  }

  predicate CreateAwsKmsMultiKeyringEnsuresPublicly(input: CreateAwsKmsMultiKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsMultiKeyring(config: InternalConfig, input: CreateAwsKmsMultiKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    var grantTokens :- GetValidGrantTokens(input.grantTokens);

    if input.clientSupplier.Some? {
      output := StrictMultiKeyring(
        input.generator,
        input.kmsKeyIds,
        input.clientSupplier.value,
        Option.Some(grantTokens)
      );
    } else {
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-multi-keyrings.md#aws-kms-multi-keyring
      //# If a regional client supplier is not passed, then a default MUST be
      //# created that takes a region string and generates a default AWS SDK
      //# client for the given region.
      var clientSupplier :- CreateDefaultClientSupplier(config, Types.CreateDefaultClientSupplierInput());
      output := StrictMultiKeyring(
        input.generator,
        input.kmsKeyIds,
        clientSupplier,
        Option.Some(grantTokens)
      );
    }
  }

  predicate CreateAwsKmsDiscoveryMultiKeyringEnsuresPublicly(input: CreateAwsKmsDiscoveryMultiKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsDiscoveryMultiKeyring ( config: InternalConfig,  input: CreateAwsKmsDiscoveryMultiKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    var grantTokens :- GetValidGrantTokens(input.grantTokens);

    var clientSupplier: Types.IClientSupplier;

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-multi-keyrings.md#aws-kms-discovery-multi-keyring
    //# If a regional client supplier is not passed, then a default MUST be created that takes a region string and generates a default AWS SDK client for the given region.
    if input.clientSupplier.None? {
      clientSupplier :- CreateDefaultClientSupplier(config, Types.CreateDefaultClientSupplierInput());
    } else {
      clientSupplier := input.clientSupplier.value;
    }
    output := DiscoveryMultiKeyring(
      input.regions,
      input.discoveryFilter,
      clientSupplier,
      Option.Some(grantTokens)
    );
  }

  predicate CreateAwsKmsMrkKeyringEnsuresPublicly(input: CreateAwsKmsMrkKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsMrkKeyring ( config: InternalConfig,  input: CreateAwsKmsMrkKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    var _ :- ValidateKmsKeyId(input.kmsKeyId);
    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var keyring := new AwsKmsMrkKeyring.AwsKmsMrkKeyring(input.kmsClient, input.kmsKeyId, grantTokens);
    return Success(keyring);
  }


  predicate CreateAwsKmsMrkMultiKeyringEnsuresPublicly(input: CreateAwsKmsMrkMultiKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsMrkMultiKeyring ( config: InternalConfig,  input: CreateAwsKmsMrkMultiKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    var grantTokens :- GetValidGrantTokens(input.grantTokens);

    var clientSupplier: Types.IClientSupplier;

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-mrk-multi-keyrings.md#aws-kms-mrk-multi-keyring
    //# If a regional client supplier is not passed, then a default MUST be created that takes a region string and generates a default AWS SDK client for the given region.
    if input.clientSupplier.None? {
      clientSupplier :- CreateDefaultClientSupplier(config, Types.CreateDefaultClientSupplierInput());
    } else {
      clientSupplier := input.clientSupplier.value;
    }
    output := MrkAwareStrictMultiKeyring(
      input.generator,
      input.kmsKeyIds,
      clientSupplier,
      Option.Some(grantTokens)
    );
  }

  predicate CreateAwsKmsMrkDiscoveryKeyringEnsuresPublicly(input: CreateAwsKmsMrkDiscoveryKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsMrkDiscoveryKeyring ( config: InternalConfig,  input: CreateAwsKmsMrkDiscoveryKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    if input.discoveryFilter.Some? {
      var _ :- ValidateDiscoveryFilter(input.discoveryFilter.value);
    }

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-mrk-discovery-keyring.md#initialization
    //= type=implication
    //# The keyring SHOULD fail initialization if the provided region does not match the
    //# region of the KMS client.
    var regionMatch := Kms.RegionMatch(input.kmsClient, input.region);
    :- Need(regionMatch != Some(false),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Provided client and region do not match"));

    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var keyring := new AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring(input.kmsClient, input.region, input.discoveryFilter, grantTokens);
    return Success(keyring);
  }


  predicate CreateAwsKmsMrkDiscoveryMultiKeyringEnsuresPublicly(input: CreateAwsKmsMrkDiscoveryMultiKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsMrkDiscoveryMultiKeyring ( config: InternalConfig,  input: CreateAwsKmsMrkDiscoveryMultiKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    var grantTokens :- GetValidGrantTokens(input.grantTokens);

    var clientSupplier: Types.IClientSupplier;

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-mrk-multi-keyrings.md#aws-kms-mrk-multi-keyring
    //# If a regional client supplier is not passed,
    //# then a default MUST be created that takes a region string and
    //# generates a default AWS SDK client for the given region.
    if input.clientSupplier.None? {
      clientSupplier :- CreateDefaultClientSupplier(config, Types.CreateDefaultClientSupplierInput());
    } else {
      clientSupplier := input.clientSupplier.value;
    }
    output := MrkAwareDiscoveryMultiKeyring(
      input.regions,
      input.discoveryFilter,
      clientSupplier,
      Option.Some(grantTokens)
    );
  }

  predicate CreateAwsKmsHierarchicalKeyringEnsuresPublicly(input: CreateAwsKmsHierarchicalKeyringInput, output: Result<IKeyring, Error>)
  {true}

  function method N(n : PositiveLong) : string {
    String.Base10Int2String(n as int)
  }

  // = aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#initialization
  // # If the cache to initialize is a [Storm Tracking Cryptographic Materials Cache](../storm-tracking-cryptographic-materials-cache.md#overview)
  // # then the [Grace Period](../storm-tracking-cryptographic-materials-cache.md#grace-period) MUST be less than the [cache limit TTL](#cache-limit-ttl).
  method CheckCache(cache : CacheType, ttlSeconds: PositiveLong) returns (output : Outcome<Error>)
  {
    if cache.StormTracking? {
      var gracePeriod := if cache.StormTracking.timeUnits.UnwrapOr(Types.Seconds).Seconds? then
        cache.StormTracking.gracePeriod as PositiveLong
      else
        cache.StormTracking.gracePeriod as PositiveLong / 1000;
      var storm := cache.StormTracking;
      if ttlSeconds <= gracePeriod {
        var msg := "When creating an AwsKmsHierarchicalKeyring with a StormCache, " +
        "the ttlSeconds of the KeyRing must be greater than the gracePeriod of the StormCache " +
        "yet the ttlSeconds is " + N(ttlSeconds) + " and the gracePeriod is " + N(gracePeriod) + ".";
        return Fail(Types.AwsCryptographicMaterialProvidersException(message := msg));
      }
      return Pass;
    } else {
      return Pass;
    }
  }

  method CreateAwsKmsHierarchicalKeyring (config: InternalConfig, input: CreateAwsKmsHierarchicalKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#initialization
    // //= type=implication
    //# If the Hierarchical Keyring does NOT get a `Shared` cache on initialization,
    //# it MUST initialize a [cryptographic-materials-cache](../local-cryptographic-materials-cache.md)
    //# with the user provided cache limit TTL and the entry capacity.
    //# If no `cache` is provided, a `DefaultCache` MUST be configured with entry capacity of 1000.
    var cmc;

    if input.cache.Some? {
      :- CheckCache(input.cache.value, input.ttlSeconds);
      match input.cache.value {
        case Shared(c) =>
          cmc := c;
        case _ =>
          cmc :- CreateCryptographicMaterialsCache(
            config,
            CreateCryptographicMaterialsCacheInput(cache := input.cache.value)
          );
      }
    }
    else {
      :- CheckCache(CacheType.StormTracking(StormTracker.DefaultStorm()), input.ttlSeconds);
      cmc :- CreateCryptographicMaterialsCache(
        config,
        CreateCryptographicMaterialsCacheInput(
          cache := Types.Default(
            Types.DefaultCache(entryCapacity := 1000)
          )
        )
      );
    }

    // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#partition-id
    // //= type=implication
    //# PartitionId can be a string provided by the user. If provided, it MUST be interpreted as UTF8 bytes.
    //# If the PartitionId is NOT provided by the user, it MUST be set to the 16 byte representation of a v4 UUID.
    var partitionIdBytes : seq<uint8>;

    if input.partitionId.Some? {
      partitionIdBytes :- UTF8.Encode(input.partitionId.value)
      .MapFailure(
        e => Types.AwsCryptographicMaterialProvidersException(
            message := "Could not UTF-8 Encode Partition ID: " + e
          )
      );
    } else {
      var uuid? := UUID.GenerateUUID();

      var uuid :- uuid?
      .MapFailure(e => Types.AwsCryptographicMaterialProvidersException(message := e));

      partitionIdBytes :- UUID.ToByteArray(uuid)
      .MapFailure(e => Types.AwsCryptographicMaterialProvidersException(message := e));
    }

    // //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-hierarchical-keyring.md#logical-key-store-name
    // //= type=implication
    //# Logical Key Store Name is set by the user when configuring the Key Store for
    //# the Hierarchical Keyring. This is a logical name for the key store.
    //# Logical Key Store Name MUST be converted to UTF8 Bytes to be used in
    //# the cache identifiers.
    var getKeyStoreInfoOutput? := input.keyStore.GetKeyStoreInfo();
    var getKeyStoreInfoOutput :- getKeyStoreInfoOutput?
    .MapFailure(e => Types.AwsCryptographyKeyStore(AwsCryptographyKeyStore := e));
    var logicalKeyStoreName := getKeyStoreInfoOutput.logicalKeyStoreName;

    var logicalKeyStoreNameBytes : seq<uint8> :- UTF8.Encode(logicalKeyStoreName)
    .MapFailure(
      e => Types.AwsCryptographicMaterialProvidersException(
          message := "Could not UTF-8 Encode Logical Key Store Name: " + e
        )
    );

    :- Need(input.branchKeyId.None? || input.branchKeyIdSupplier.None?,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier."));

    :- Need(input.branchKeyId.Some? || input.branchKeyIdSupplier.Some?,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Must initialize keyring with either branchKeyId or BranchKeyIdSupplier."));

    var keyring := new AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring(
      keyStore := input.keyStore,
      branchKeyId := input.branchKeyId,
      branchKeyIdSupplier := input.branchKeyIdSupplier,
      ttlSeconds := input.ttlSeconds,
      cmc := cmc,
      partitionIdBytes := partitionIdBytes,
      logicalKeyStoreNameBytes := logicalKeyStoreNameBytes,
      cryptoPrimitives := config.crypto
    );
    return Success(keyring);
  }

  predicate CreateAwsKmsEcdhKeyringEnsuresPublicly(input: CreateAwsKmsEcdhKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsEcdhKeyring(config: InternalConfig, input: CreateAwsKmsEcdhKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var recipientPublicKey: KMS.PublicKeyType;
    var senderPublicKey: Option<KMS.PublicKeyType>;
    var compressedSenderPublicKey: Option<seq<uint8>>;

    match input.KeyAgreementScheme {
      case KmsPublicKeyDiscovery(kmsPublicKeyDiscovery) => {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmspublickeydiscovery
        //# - MUST provide the recipient's AWS KMS key identifier
        var _ :- ValidateKmsKeyId(kmsPublicKeyDiscovery.recipientKmsIdentifier);
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmspublickeydiscovery
        //# the keyring MUST call
        //# `kms:GetPublicKey` on the recipient's configured KMS key ID.
        // (blank line for duvet)
        //# If the keyring fails to retrieve the public key, the keyring MUST fail.
        recipientPublicKey :- GetEcdhPublicKey(input.kmsClient, kmsPublicKeyDiscovery.recipientKmsIdentifier);
        senderPublicKey := Option.None();
        compressedSenderPublicKey := Option.None();
      }
      case KmsPrivateKeyToStaticPublicKey(kmsPrivateKeyToStaticPublicKey) => {
        if kmsPrivateKeyToStaticPublicKey.senderPublicKey.Some? {
          :- Need(
            KMS.IsValid_PublicKeyType(
              kmsPrivateKeyToStaticPublicKey.senderPublicKey.value
            ),
            Types.AwsCryptographicMaterialProvidersException(message := "Invalid SenderPublicKey length."));
          //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmsprivatekeytostaticpublickey
          //# - MAY provide the sender's public key
          //#   - Public key MUST be DER-encoded [X.509 SubjectPublicKeyInfo](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1)
          senderPublicKey := Some(kmsPrivateKeyToStaticPublicKey.senderPublicKey.value);
          var compressedPKU :- RawECDHKeyring.CompressPublicKey(Crypto.ECCPublicKey(der := senderPublicKey.value), input.curveSpec, config.crypto);
          compressedSenderPublicKey := Some(compressedPKU);
        } else {
          var _ :- ValidateKmsKeyId(kmsPrivateKeyToStaticPublicKey.senderKmsIdentifier);
          //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmsprivatekeytostaticpublickey
          //# On initialization, if the keyring is not configured with
          //# a sender public key, the keyring MUST call
          //# `kms:GetPublicKey` on the sender's configured KMS key ID.
          // (blank line for duvet)
          //# If the keyring fails to retrieve the public key, the keyring MUST fail.
          var senderPublicKeyResponse :- GetEcdhPublicKey(input.kmsClient, kmsPrivateKeyToStaticPublicKey.senderKmsIdentifier);
          var compressedPKU :- RawECDHKeyring.CompressPublicKey(Crypto.ECCPublicKey(der := senderPublicKeyResponse), input.curveSpec, config.crypto);
          senderPublicKey := Some(senderPublicKeyResponse);
          compressedSenderPublicKey := Some(compressedPKU);
        }

        :- Need(
          KMS.IsValid_PublicKeyType(
            kmsPrivateKeyToStaticPublicKey.recipientPublicKey
          ),
          Types.AwsCryptographicMaterialProvidersException(message := "Invalid RecipientPublicKey length."));
        recipientPublicKey := kmsPrivateKeyToStaticPublicKey.recipientPublicKey;
      }
    }

    var _ :- RawECDHKeyring.ValidatePublicKey(
      config.crypto,
      input.curveSpec,
      recipientPublicKey
    );

    var compressedRecipientPublicKey :- RawECDHKeyring.CompressPublicKey(
      Crypto.ECCPublicKey(der := recipientPublicKey),
      input.curveSpec,
      config.crypto
    );

    var senderKmsKeyId := if input.KeyAgreementScheme.KmsPublicKeyDiscovery? then Option.None()
    else Some(input.KeyAgreementScheme.KmsPrivateKeyToStaticPublicKey.senderKmsIdentifier);

    if senderKmsKeyId.Some? {
      var _ :- ValidateKmsKeyId(senderKmsKeyId.value);
    }

    if senderPublicKey.Some? {
      var _ :- RawECDHKeyring.ValidatePublicKey(
        config.crypto,
        input.curveSpec,
        senderPublicKey.value
      );
    }

    var keyring := new AwsKmsEcdhKeyring.AwsKmsEcdhKeyring(
      input.KeyAgreementScheme,
      input.curveSpec,
      input.kmsClient,
      grantTokens,
      senderKmsKeyId,
      senderPublicKey,
      recipientPublicKey,
      compressedSenderPublicKey,
      compressedRecipientPublicKey,
      config.crypto
    );

    return Success(keyring);
  }

  predicate CreateMultiKeyringEnsuresPublicly(input: CreateMultiKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateMultiKeyring ( config: InternalConfig,  input: CreateMultiKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    SequenceIsSafeBecauseItIsInMemory(input.childKeyrings);
    :- Need(input.generator.Some? || |input.childKeyrings| as uint64 > 0,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Must include a generator keyring and/or at least one child keyring"));

    var keyring := new MultiKeyring.MultiKeyring(input.generator, input.childKeyrings);
    return Success(keyring);
  }


  predicate CreateRawAesKeyringEnsuresPublicly(input: CreateRawAesKeyringInput, output: Result<IKeyring, Error>)
  {
    //= aws-encryption-sdk-specification/framework/raw-aes-keyring.md#changelog
    //= type=implication
    //# Raw AES keyring MUST NOT accept a key namespace of "aws-kms".
    input.keyNamespace == "aws-kms"
    ==>
      output.Failure?
  }

  method CreateRawAesKeyring ( config: InternalConfig,  input: CreateRawAesKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    :- Need(input.keyNamespace != "aws-kms",
            Types.AwsCryptographicMaterialProvidersException(
              message := "keyNamespace must not be `aws-kms`"));

    var wrappingAlg:Crypto.AES_GCM := match input.wrappingAlg
      case ALG_AES128_GCM_IV12_TAG16() => Crypto.AES_GCM(
        keyLength := 16,
        tagLength := 16,
        ivLength := 12
      )
      case ALG_AES192_GCM_IV12_TAG16() => Crypto.AES_GCM(
        keyLength := 24,
        tagLength := 16,
        ivLength := 12
      )
      case ALG_AES256_GCM_IV12_TAG16() => Crypto.AES_GCM(
        keyLength := 32,
        tagLength := 16,
        ivLength := 12
      );

    var namespaceAndName :- ParseKeyNamespaceAndName(input.keyNamespace, input.keyName);
    var (namespace, name) := namespaceAndName;

    SequenceIsSafeBecauseItIsInMemory(input.wrappingKey);
    var wrapping_key_size := |input.wrappingKey| as uint64;
    :- Need(wrapping_key_size == 16 || wrapping_key_size == 24 || wrapping_key_size == 32,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Invalid wrapping key length"));
    :- Need(wrapping_key_size == wrappingAlg.keyLength as uint64,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Wrapping key length does not match specified wrapping algorithm"));

    var keyring := new RawAESKeyring
    .RawAESKeyring(
      namespace := namespace,
      name := name,
      key := input.wrappingKey,
      wrappingAlgorithm := wrappingAlg,
      cryptoPrimitives := config.crypto
    );
    return Success(keyring);
  }


  predicate CreateRawRsaKeyringEnsuresPublicly(input: CreateRawRsaKeyringInput, output: Result<IKeyring, Error>)
  {
    //= aws-encryption-sdk-specification/framework/raw-rsa-keyring.md#changelog
    //= type=implication
    //# Raw RSA keyring MUST NOT accept a key namespace of "aws-kms".
    && (input.keyNamespace == "aws-kms"
        ==>
          output.Failure?)
    && (input.publicKey.None? && input.privateKey.None?
        ==>
          output.Failure?)
  }

  method CreateRawRsaKeyring ( config: InternalConfig,  input: CreateRawRsaKeyringInput )
    returns (output: Result<IKeyring, Error>)
  {
    :- Need(input.keyNamespace != "aws-kms",
            Types.AwsCryptographicMaterialProvidersException(
              message := "keyNamespace must not be `aws-kms`"));
    :- Need(input.publicKey.Some? || input.privateKey.Some?,
            Types.AwsCryptographicMaterialProvidersException(
              message := "A publicKey or a privateKey is required"));

    var padding: Crypto.RSAPaddingMode := match input.paddingScheme
      case PKCS1() => Crypto.RSAPaddingMode.PKCS1
      case OAEP_SHA1_MGF1() => Crypto.RSAPaddingMode.OAEP_SHA1
      case OAEP_SHA256_MGF1() => Crypto.RSAPaddingMode.OAEP_SHA256
      case OAEP_SHA384_MGF1() => Crypto.RSAPaddingMode.OAEP_SHA384
      case OAEP_SHA512_MGF1() => Crypto.RSAPaddingMode.OAEP_SHA512
      ;

    var namespaceAndName :- ParseKeyNamespaceAndName(input.keyNamespace, input.keyName);
    var (namespace, name) := namespaceAndName;

    var keyring := new RawRSAKeyring.RawRSAKeyring(
      namespace := namespace,
      name := name,
      publicKey := input.publicKey,
      privateKey := input.privateKey,
      paddingScheme := padding,
      cryptoPrimitives := config.crypto
    );
    return Success(keyring);
  }

  predicate CreateRawEcdhKeyringEnsuresPublicly(input: CreateRawEcdhKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateRawEcdhKeyring(config: InternalConfig, input: CreateRawEcdhKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    var recipientPublicKey: seq<uint8>;
    var senderPrivateKey: Option<seq<uint8>>;
    var senderPublicKey: Option<seq<uint8>>;
    var compressedSenderPublicKey: Option<seq<uint8>>;

    match input.KeyAgreementScheme {
      case RawPrivateKeyToStaticPublicKey(rawPrivateKeyToStaticPublicKey) => {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#rawprivatekeytostaticpublickey
        //# - MUST provide the recipient's public key
        recipientPublicKey := rawPrivateKeyToStaticPublicKey.recipientPublicKey;
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#rawprivatekeytostaticpublickey
        //# - MUST provide the sender's static private key
        senderPrivateKey := Option.Some(rawPrivateKeyToStaticPublicKey.senderStaticPrivateKey);
        var reproducedPublicKey :- GetPublicKey(input.curveSpec, Crypto.ECCPrivateKey(pem := senderPrivateKey.value), config.crypto);
        var _ :- RawECDHKeyring.ValidatePublicKey(
          config.crypto,
          input.curveSpec,
          reproducedPublicKey
        );
        senderPublicKey := Some(reproducedPublicKey);
        var compressedSenderPublicKey? :- RawECDHKeyring.CompressPublicKey(
          Crypto.ECCPublicKey(der := reproducedPublicKey),
          input.curveSpec,
          config.crypto
        );
        compressedSenderPublicKey := Some(compressedSenderPublicKey?);
      }
      case EphemeralPrivateKeyToStaticPublicKey(ephemeralPrivateKeyToStaticPublicKey) => {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#ephemeralprivatekeytostaticpublickey
        //# - MUST provide the recipient's public key
        recipientPublicKey := ephemeralPrivateKeyToStaticPublicKey.recipientPublicKey;
        senderPrivateKey := Option.None();
        senderPublicKey := Option.None();
        compressedSenderPublicKey := Option.None();
      }
      case PublicKeyDiscovery(publicKeyDiscovery) => {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#publickeydiscovery
        //# - MUST provide the recipient's static private key
        var reproducedPublicKey :- GetPublicKey(input.curveSpec, Crypto.ECCPrivateKey(pem := publicKeyDiscovery.recipientStaticPrivateKey), config.crypto);
        recipientPublicKey := reproducedPublicKey;
        senderPrivateKey := Option.None();
        senderPublicKey := Option.None();
        compressedSenderPublicKey := Option.None();
      }
    }

    var compressedRecipientPublicKey :- RawECDHKeyring.CompressPublicKey(
      Crypto.ECCPublicKey(der := recipientPublicKey),
      input.curveSpec,
      config.crypto
    );

    //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#initialization
    //# On initialization, the keyring MUST assert that the recipient's public key
    //# and the sender's private key belong to the same ECC Curve, and that
    //# the public key's ECC points are not the "points at infinity".
    var _ :- RawECDHKeyring.ValidatePublicKey(
      config.crypto,
      input.curveSpec,
      recipientPublicKey
    );

    if senderPublicKey.Some? {
      var _ :- RawECDHKeyring.ValidatePublicKey(
        config.crypto,
        input.curveSpec,
        senderPublicKey.value
      );
      :- Need(
        RawECDHKeyring.ValidPublicKeyLength(senderPublicKey.value),
        Types.AwsCryptographicMaterialProvidersException(message := "Invalid sender public key length")
      );
    }

    :- Need(
      RawECDHKeyring.ValidPublicKeyLength(recipientPublicKey),
      Types.AwsCryptographicMaterialProvidersException(message := "Invalid recipient public key length")
    );

    var keyring := new RawECDHKeyring.RawEcdhKeyring(
      keyAgreementScheme := input.KeyAgreementScheme,
      curveSpec := input.curveSpec,
      senderPrivateKey := senderPrivateKey,
      senderPublicKey := senderPublicKey,
      recipientPublicKey := recipientPublicKey,
      compressedSenderPublicKey := compressedSenderPublicKey,
      compressedRecipientPublicKey := compressedRecipientPublicKey,
      cryptoPrimitives := config.crypto
    );

    return Success(keyring);
  }

  predicate CreateAwsKmsRsaKeyringEnsuresPublicly(input: CreateAwsKmsRsaKeyringInput, output: Result<IKeyring, Error>)
  {true}

  method CreateAwsKmsRsaKeyring(config: InternalConfig, input: CreateAwsKmsRsaKeyringInput)
    returns (output: Result<IKeyring, Error>)
  {
    :- Need(input.publicKey.Some? || input.kmsClient.Some?,
            Types.AwsCryptographicMaterialProvidersException(
              message := "A publicKey or a kmsClient is required"));
    :- Need(input.encryptionAlgorithm.RSAES_OAEP_SHA_1? || input.encryptionAlgorithm.RSAES_OAEP_SHA_256?,
            Types.AwsCryptographicMaterialProvidersException(
              message := "Unsupported EncryptionAlgorithmSpec"));

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#initialization
      //= type=implication
      //# The AWS KMS key identifier MUST NOT be null or empty.

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#initialization
      //= type=implication
      //# The AWS KMS key identifier MUST be [a valid identifier](../../framework/aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-identifier).

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#initialization
      //= type=implication
      //# The AWS KMS key identifier MUST NOT be an AWS KMS alias.
    :- Need(
      && KMS.IsValid_KeyIdType(input.kmsKeyId)
      && ParseAwsKmsArn(input.kmsKeyId).Success?,
      Types.AwsCryptographicMaterialProvidersException(
        message := "Kms Key ID must be a KMS Key ARN")
    );

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#initialization
    //= type=implication
    //# If provided the Public Key
    //# MUST have an RSA modulus bit length greater than or equal to 2048.
    if (input.publicKey.Some?) {
      var lengthOutputRes := config.crypto.GetRSAKeyModulusLength(
        Crypto.GetRSAKeyModulusLengthInput(publicKey := input.publicKey.value));
      var lengthOutput :- lengthOutputRes.MapFailure(e => Types.AwsCryptographyPrimitives(e));
      :- Need(lengthOutput.length >= AwsKmsRsaKeyring.MIN_KMS_RSA_KEY_LEN,
              Types.AwsCryptographicMaterialProvidersException(
                message := "Invalid public key length"));
    }

    var _ :- ValidateKmsKeyId(input.kmsKeyId);
    var grantTokens :- GetValidGrantTokens(input.grantTokens);
    var keyring := new AwsKmsRsaKeyring.AwsKmsRsaKeyring(
      publicKey := input.publicKey,
      awsKmsKey := input.kmsKeyId,
      paddingScheme := input.encryptionAlgorithm,
      client := input.kmsClient,
      cryptoPrimitives := config.crypto,
      grantTokens := grantTokens
    );
    return Success(keyring);
  }

  predicate CreateDefaultCryptographicMaterialsManagerEnsuresPublicly(input: CreateDefaultCryptographicMaterialsManagerInput, output: Result<ICryptographicMaterialsManager, Error>)
  {true}

  method CreateDefaultCryptographicMaterialsManager(config: InternalConfig, input: CreateDefaultCryptographicMaterialsManagerInput)
    returns (output: Result<ICryptographicMaterialsManager, Error>)
  {
    var cmm := new DefaultCMM.OfKeyring(input.keyring, config.crypto);
    return Success(cmm);
  }

  function method CmpError(s : string) : Error
  {
    Types.AwsCryptographicMaterialProvidersException(
      message := s)
  }
  predicate CreateRequiredEncryptionContextCMMEnsuresPublicly(input: CreateRequiredEncryptionContextCMMInput, output: Result<ICryptographicMaterialsManager, Error>)
  {true}

  method CreateRequiredEncryptionContextCMM(config: InternalConfig, input: CreateRequiredEncryptionContextCMMInput)
    returns (output: Result<ICryptographicMaterialsManager, Error>)
    ensures output.Success? ==> output.value.ValidState()
  {
    :- Need(input.underlyingCMM.Some? && input.keyring.None?, CmpError("CreateRequiredEncryptionContextCMM currently only supports cmm."));
    var keySet : set<UTF8.ValidUTF8Bytes> := set k <- input.requiredEncryptionContextKeys;
    SetIsSafeBecauseItIsInMemory(keySet);
    :- Need(0 < |keySet| as uint64, CmpError("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey."));
    var cmm := new RequiredEncryptionContextCMM.RequiredEncryptionContextCMM(
      input.underlyingCMM.value,
      keySet);

    return Success(cmm);
  }

  predicate CreateCryptographicMaterialsCacheEnsuresPublicly(input: CreateCryptographicMaterialsCacheInput , output: Result<ICryptographicMaterialsCache, Error>)
  {true}

  method CreateCryptographicMaterialsCache(config: InternalConfig, input: CreateCryptographicMaterialsCacheInput)
    returns (output: Result<ICryptographicMaterialsCache, Error>)
  {
    match input.cache {
      case Default(c) =>
        var cache := StormTracker.DefaultStorm().(entryCapacity := c.entryCapacity);
        :- StormTracker.CheckSettings(cache);
        var cmc := new StormTracker.StormTracker(cache);
        var synCmc := new StormTrackingCMC.StormTrackingCMC(cmc);
        return Success(synCmc);
      case No(_) =>
        var cmc := new LocalCMC.LocalCMC(0, 1);
        return Success(cmc);
      case SingleThreaded(c) =>
        var cmc := new LocalCMC.LocalCMC(
          c.entryCapacity as uint64,
          OptionalCountingNumber(c.entryPruningTailSize).UnwrapOr(1) as uint64
        );
        return Success(cmc);
      case MultiThreaded(c) =>
        var cmc := new LocalCMC.LocalCMC(
          c.entryCapacity as uint64,
          OptionalCountingNumber(c.entryPruningTailSize).UnwrapOr(1) as uint64
        );
        var synCmc := new SynchronizedLocalCMC.SynchronizedLocalCMC(cmc);
        return Success(synCmc);
      case StormTracking(c) =>
        var cache := c.( entryPruningTailSize := OptionalCountingNumber(c.entryPruningTailSize));
        :- StormTracker.CheckSettings(cache);


        var cmc := new StormTracker.StormTracker(cache);
        var synCmc := new StormTrackingCMC.StormTrackingCMC(cmc);
        return Success(synCmc);
      case Shared(c) =>
        var exception := Types.AwsCryptographicMaterialProvidersException(
          message := "CreateCryptographicMaterialsCache should never be called with Shared CacheType.");
        return Failure(exception);
    }
  }

  // Smithy-Dafny currently uses `int` in Java to represent
  // a `integer` in Smithy.
  // This is problematic because in Java `int` can not be `null`.
  // This means that an unset `int` will be `0`.
  // When crossing back and forth between Dafny and Java then
  // an optional integer will never be `None`.
  // For `CountingNumber` this can be identified by checking for `0`
  function method OptionalCountingNumber(c: Option<int32>)
    : Option<CountingNumber>
  {
    if c.Some? && c.value <= 0 then
      Wrappers.None
    else
      c
  }

  lemma OptionalCountingNumberCorrect(c: int32)
    ensures 1 <= c ==> OptionalCountingNumber(Some(c)) == Some(c)
    ensures c <= 0 ==> OptionalCountingNumber(Some(c)) == Wrappers.None
  {}

  predicate CreateDefaultClientSupplierEnsuresPublicly(input: CreateDefaultClientSupplierInput, output: Result<IClientSupplier, Error>)
  {true}

  method CreateDefaultClientSupplier ( config: InternalConfig,  input: CreateDefaultClientSupplierInput )
    returns (output: Result<IClientSupplier, Error>)
  {
    var clientSupplier := new DefaultClientSupplier.DefaultClientSupplier();
    return Success(clientSupplier);
  }

  function method InitializeEncryptionMaterials ( config: InternalConfig,  input: InitializeEncryptionMaterialsInput )
    : (output: Result<EncryptionMaterials, Error>)
  {
    Materials.InitializeEncryptionMaterials(input)
  }

  function method InitializeDecryptionMaterials ( config: InternalConfig,  input: InitializeDecryptionMaterialsInput )
    : (output: Result<DecryptionMaterials, Error>)
  {
    Materials.InitializeDecryptionMaterials(input)
  }

  function method ValidEncryptionMaterialsTransition ( config: InternalConfig,  input: ValidEncryptionMaterialsTransitionInput )
    : (output: Result<(), Error>)
  {
    :- Need(
         Materials.ValidEncryptionMaterialsTransition(input.start, input.stop),
         InvalidEncryptionMaterialsTransition( message := "Invalid Encryption Materials Transition" )
       );

    Success(())
  }

  function method ValidDecryptionMaterialsTransition ( config: InternalConfig,  input: ValidDecryptionMaterialsTransitionInput )
    : (output: Result<(), Error>)
  {
    :- Need(
         Materials.DecryptionMaterialsTransitionIsValid(input.start, input.stop),
         InvalidDecryptionMaterialsTransition( message := "Invalid Decryption Materials Transition")
       );

    Success(())
  }

  function method EncryptionMaterialsHasPlaintextDataKey ( config: InternalConfig,  input: EncryptionMaterials )
    : (output: Result<(), Error>)
  {
    :- Need(
         Materials.EncryptionMaterialsHasPlaintextDataKey(input),
         InvalidDecryptionMaterials( message := "Invalid Encryption Materials")
       );

    Success(())
  }
  function method DecryptionMaterialsWithPlaintextDataKey ( config: InternalConfig,  input: DecryptionMaterials )
    : (output: Result<(), Error>)
  {
    :- Need(
         Materials.DecryptionMaterialsWithPlaintextDataKey(input),
         InvalidDecryptionMaterials( message := "Invalid Decryption Materials")
       );

    Success(())
  }

  function method GetAlgorithmSuiteInfo ( config: InternalConfig,  input: seq<uint8> )
    : (output: Result<AlgorithmSuiteInfo, Error>)
  {
    AlgorithmSuites.GetAlgorithmSuiteInfo(input)
  }

  function method ValidAlgorithmSuiteInfo ( config: InternalConfig,  input: AlgorithmSuiteInfo )
    : (output: Result<(), Error>)
  {
    :- Need(AlgorithmSuites.AlgorithmSuite?(input),
            InvalidAlgorithmSuiteInfo( message := "Invalid AlgorithmSuiteInfo" )
       );

    Success(())
  }

  function method ValidateCommitmentPolicyOnEncrypt ( config: InternalConfig,  input: ValidateCommitmentPolicyOnEncryptInput )
    : (output: Result<(), Error>)
  {
    :- Commitment.ValidateCommitmentPolicyOnEncrypt(input.algorithm, input.commitmentPolicy);

    Success(())
  }

  function method ValidateCommitmentPolicyOnDecrypt ( config: InternalConfig,  input: ValidateCommitmentPolicyOnDecryptInput )
    : (output: Result<(), Error>)
  {
    :- Commitment.ValidateCommitmentPolicyOnDecrypt(input.algorithm, input.commitmentPolicy);

    Success(())
  }

}
