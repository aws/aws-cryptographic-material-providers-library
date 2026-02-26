// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Keyring.dfy"
include "../Materials.dfy"
include "../AlgorithmSuites.dfy"
include "../Materials.dfy"
include "../KeyWrapping/MaterialWrapping.dfy"
include "../KeyWrapping/EdkWrapping.dfy"
include "../KeyWrapping/EcdhEdkWrapping.dfy"
include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../ErrorMessages.dfy"
include "../CanonicalEncryptionContext.dfy"
include "./AwsKms/Constants.dfy"

module {:options "/functionSyntax:4" } RawECDHKeyring {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import opened String = StandardLibrary.String
  import opened Actions
  import opened Wrappers
  import opened Constants
  import Types = AwsCryptographyMaterialProvidersTypes
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import AtomicPrimitives
  import Keyring
  import Materials
  import opened AlgorithmSuites
  import Random
  import ECDH
  import UTF8
  import opened Seq
  import MaterialWrapping
  import EdkWrapping
  import EcdhEdkWrapping
  import ErrorMessages
  import CanonicalEncryptionContext

  const RAW_ECDH_KEYRING_VERSION: seq<uint8> := [0x01]

  predicate ValidPublicKeyLength(p: seq<uint8>)
  {
    SequenceIsSafeBecauseItIsInMemory(p);
    var len := |p| as uint64;
    && (len == ECDH_PUBLIC_KEY_LEN_ECC_NIST_256 ||
        len == ECDH_PUBLIC_KEY_LEN_ECC_NIST_384 ||
        len == ECDH_PUBLIC_KEY_LEN_ECC_NIST_521)
  }

  predicate ValidCompressedPublicKeyLength(p: seq<uint8>)
  {
    SequenceIsSafeBecauseItIsInMemory(p);
    var len := |p| as uint64;
    && (len == ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_256 ||
        len == ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_384 ||
        len == ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_521)
  }

  predicate ValidProviderInfoLength(p: seq<uint8>)
  {
    SequenceIsSafeBecauseItIsInMemory(p);
    var len := |p| as uint64;
    (len == ECDH_PROVIDER_INFO_256_LEN as uint64 ||
     len == ECDH_PROVIDER_INFO_384_LEN as uint64 ||
     len == ECDH_PROVIDER_INFO_521_LEN as uint64
    )
  }

  //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#interface
  //= type=implication
  //# MUST implement the [AWS Encryption SDK Keyring interface](../keyring-interface.md#interface)
  class RawEcdhKeyring
    extends Keyring.VerifiableInterface
  {
    const senderPrivateKey: PrimitiveTypes.ECCPrivateKey
    const senderPublicKey: PrimitiveTypes.ECCPublicKey
    const recipientPublicKey: PrimitiveTypes.ECCPublicKey
    const compressedSenderPublicKey: seq<uint8>
    const compressedRecipientPublicKey: seq<uint8>
    const keyAgreementScheme: Types.RawEcdhStaticConfigurations
    const curveSpec: PrimitiveTypes.ECDHCurveSpec
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient

    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && cryptoPrimitives.ValidState()
      && cryptoPrimitives.Modifies <= Modifies
      && History !in cryptoPrimitives.Modifies
    }

    constructor(
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#initialization
      //= type=implication
      //# - MUST provide a [Key Agreement Schema](#key-agreement-schema)
      keyAgreementScheme: Types.RawEcdhStaticConfigurations,
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#initialization
      //= type=implication
      //# - MUST provide a [Curve Specification](#curve-specification)
      curveSpec: PrimitiveTypes.ECDHCurveSpec,

      senderPrivateKey: Option<seq<uint8>>,
      senderPublicKey: Option<seq<uint8>>,
      recipientPublicKey: seq<uint8>,
      compressedSenderPublicKey: Option<seq<uint8>>,
      compressedRecipientPublicKey: seq<uint8>,
      cryptoPrimitives : AtomicPrimitives.AtomicPrimitivesClient
    )
      requires cryptoPrimitives.ValidState()
      requires senderPublicKey.Some? ==> ValidPublicKeyLength(senderPublicKey.value)
      requires ValidPublicKeyLength(recipientPublicKey)
      ensures ValidState() && fresh(this) && fresh(History)
              && fresh(Modifies - cryptoPrimitives.Modifies)
    {
      this.keyAgreementScheme := keyAgreementScheme;
      this.curveSpec := curveSpec;
      this.cryptoPrimitives := cryptoPrimitives;

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#initialization
      //= type=implication
      //# The keyring MUST set the sender's public key
      //# and the recipient's public key on the keyring.
      this.recipientPublicKey := PrimitiveTypes.ECCPublicKey(der := recipientPublicKey);
      this.compressedRecipientPublicKey := compressedRecipientPublicKey;
      if senderPublicKey.Some? && senderPrivateKey.Some? && compressedSenderPublicKey.Some? {
        this.senderPublicKey := PrimitiveTypes.ECCPublicKey(der := senderPublicKey.value);
        this.senderPrivateKey := PrimitiveTypes.ECCPrivateKey(pem := senderPrivateKey.value);
        this.compressedSenderPublicKey := compressedSenderPublicKey.value;
      } else {
        this.senderPublicKey := PrimitiveTypes.ECCPublicKey(der := []);
        this.senderPrivateKey := PrimitiveTypes.ECCPrivateKey(pem := []);
        this.compressedSenderPublicKey := [];
      }

      History := new Types.IKeyringCallHistory();
      Modifies := {History};
      Modifies := Modifies + cryptoPrimitives.Modifies;
    }


    ghost     predicate OnEncryptEnsuresPublicly (
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

    //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
    //= type=implication
    //# OnEncrypt MUST take [encryption materials](structures.md#encryption-materials) as input.
    method {:vcs_split_on_every_assert} OnEncrypt'(input: Types.OnEncryptInput)
      returns (res: Result<Types.OnEncryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnEncryptEnsuresPublicly(input, res)
      ensures unchanged(History)
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
      //= type=implication
      //# OnEncrypt MUST fail if configured with a
      //# [PublicKeyDiscovery Key Agreement Configuration](./key-agreement-schemas.md#publickeydiscovery)
      ensures this.keyAgreementScheme.PublicKeyDiscovery? ==> res.Failure?
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
      //= type=implication
      //# If the keyring cannot serialize
      //# the encryption context, OnEncrypt MUST fail.
      ensures CanonicalEncryptionContext.EncryptionContextToAAD(input.materials.encryptionContext).Failure? ==> res.Failure?
    {
      if this.keyAgreementScheme.PublicKeyDiscovery? {
        return  Failure(Types.AwsCryptographicMaterialProvidersException(
                          message := "PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt."));
      }

      var operationSenderPrivateKey: PrimitiveTypes.ECCPrivateKey;
      var operationSenderPublicKey: PrimitiveTypes.ECCPublicKey;
      var operationCompressedSenderPublicKey: seq<uint8>;

      if this.keyAgreementScheme.EphemeralPrivateKeyToStaticPublicKey? {
        var ephemeralKeyPair :- GenerateEphemeralEccKeyPair(this.curveSpec, this.cryptoPrimitives);
        operationSenderPrivateKey := ephemeralKeyPair.privateKey;
        operationSenderPublicKey := ephemeralKeyPair.publicKey;
        var operationCompressedSenderPublicKey? :- CompressPublicKey(
          PrimitiveTypes.ECCPublicKey(der := operationSenderPublicKey.der),
          this.curveSpec,
          this.cryptoPrimitives
        );
        operationCompressedSenderPublicKey := operationCompressedSenderPublicKey?;
      } else {
        operationSenderPrivateKey := this.senderPrivateKey;
        operationSenderPublicKey := this.senderPublicKey;
        operationCompressedSenderPublicKey := this.compressedSenderPublicKey;
      }

      var materials := input.materials;
      var suite := input.materials.algorithmSuite;

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
      //# The keyring MUST derive the shared secret
      //# according to the configured [Key Agreement Schema](#key-agreement-procedure).
      // (blank line for duvet)
      //# If the keyring fails to compute the shared secret, the keyring MUST fail.
      var sharedSecret :- LocalDeriveSharedSecret(
        operationSenderPrivateKey,
        recipientPublicKey,
        this.curveSpec,
        this.cryptoPrimitives
      );

      var curveSpecUtf8 :- UTF8.Encode(
        CurveSpecTypeToString(this.curveSpec)
      ).MapFailure(E);

      var canonicalizedEC :- CanonicalEncryptionContext.EncryptionContextToAAD(input.materials.encryptionContext);

      var fixedInfo := EcdhEdkWrapping.SerializeFixedInfo(
        ECDH_KDF_UTF8,
        curveSpecUtf8,
        operationCompressedSenderPublicKey,
        this.compressedRecipientPublicKey,
        canonicalizedEC,
        RAW_ECDH_KEYRING_VERSION
      );

      var ecdhGenerateAndWrap := new EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial(
        sharedSecret,
        fixedInfo,
        cryptoPrimitives
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
      //# The keyring MUST perform data key wrapping according to the [Data Key Wrapping section](#data-key-wrapping).
      var ecdhWrap := new EcdhEdkWrapping.EcdhWrapKeyMaterial(
        sharedSecret,
        fixedInfo,
        cryptoPrimitives
      );

      var wrapOutput :- EdkWrapping.WrapEdkMaterial<EcdhEdkWrapping.EcdhWrapInfo>(
        encryptionMaterials := materials,
        wrap := ecdhWrap,
        generateAndWrap := ecdhGenerateAndWrap
      );

      var symmetricSigningKeyList :=
        if wrapOutput.symmetricSigningKey.Some? then
          Some([wrapOutput.symmetricSigningKey.value])
        else
          None;

        // Impossible to hit but needed for verification. Come back and prove properly.
      :- Need(
        && ValidCompressedPublicKeyLength(operationCompressedSenderPublicKey)
        && ValidCompressedPublicKeyLength(this.compressedRecipientPublicKey),
        E("Invalid compressed public key length.")
      );

      var edk := Types.EncryptedDataKey(
        //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
        //# - The [key provider id](../structures.md#key-provider-id) MUST be the UTF8 encoded string "raw-ecdh".
        keyProviderId := RAW_ECDH_PROVIDER_ID,
        //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#key-provider-information
        //# Both the recipient and the sender public keys MUST be in their compressed formats.
        keyProviderInfo := SerializeProviderInfo(operationCompressedSenderPublicKey, this.compressedRecipientPublicKey),
        ciphertext := wrapOutput.wrappedMaterial
      );

      if (wrapOutput.GenerateAndWrapEdkMaterialOutput?) {
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
        //# OnEncrypt MUST append a new [encrypted data key](../structures.md#encrypted-data-key)
        //# to the encrypted data key list in the [encryption materials](../structures.md#encryption-materials)
        var result :- Materials.EncryptionMaterialAddDataKey(
          materials,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# If the keyring successfully wraps the plaintext data key it MUST set it on the [encryption materials](structures.md#encryption-materials).
          wrapOutput.plaintextDataKey,
          [edk],
          symmetricSigningKeyList
        );
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

    ghost predicate OnDecryptEnsuresPublicly ( input: Types.OnDecryptInput , output: Result<Types.OnDecryptOutput, Types.Error> )
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

    method {:vcs_split_on_every_assert} OnDecrypt'(input: Types.OnDecryptInput)
      returns (res: Result<Types.OnDecryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnDecryptEnsuresPublicly(input, res)
      ensures unchanged(History)
      ensures res.Success?
              ==>
                && Materials.DecryptionMaterialsTransitionIsValid(
                  input.materials,
                  res.value.materials
                )
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //= type=implication
      //# OnDecrypt MUST fail if configured with a
      //# [EphemeralPrivateKeyToStaticPublicKey Key Agreement Configuration](./key-agreement-schemas.md#ephemeralprivatekeytostaticpublickey)
      ensures this.keyAgreementScheme.EphemeralPrivateKeyToStaticPublicKey? ==> res.Failure?
    {
      if this.keyAgreementScheme.EphemeralPrivateKeyToStaticPublicKey? {
        return  Failure(Types.AwsCryptographicMaterialProvidersException(
                          message := "EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt."));
      }

      var materials := input.materials;
      var suite := input.materials.algorithmSuite;

        //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
        //# If the decryption materials already contain a plaintext data key,
        //# the keyring MUST fail
        //# and MUST NOT modify the [decryption materials](structures.md#decryption-materials).
      :- Need(
        Materials.DecryptionMaterialsWithoutPlaintextDataKey(materials),
        E("Keyring received decryption materials that already contain a plaintext data key.")
      );

      var operationCompressedSenderPublicKey := if this.compressedSenderPublicKey  == [] then Option.None()
      else Some(this.compressedSenderPublicKey);

      var filter := new OnDecryptEcdhDataKeyFilter(keyAgreementScheme, this.compressedRecipientPublicKey, operationCompressedSenderPublicKey);

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# The set of encrypted data keys MUST first be filtered to match this keyring’s configuration.
      //# For the encrypted data key to match:
      var edksToAttempt :- FilterWithResult(filter, input.encryptedDataKeys);

      SequenceIsSafeBecauseItIsInMemory(edksToAttempt);
      if (0 == |edksToAttempt| as uint64) {
        var errorMessage :- ErrorMessages.IncorrectDataKeys(input.encryptedDataKeys, input.materials.algorithmSuite);
        return Failure(E(errorMessage));
      }

      var decryptClosure := new DecryptSingleEncryptedDataKey(
        materials,
        cryptoPrimitives,
        this.compressedSenderPublicKey,
        this.compressedRecipientPublicKey,
        keyAgreementScheme,
        curveSpec
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# For each encrypted data key in the filtered set, one at a time, the OnDecrypt MUST attempt to decrypt the data key.
      //# If this attempt results in an error, then these errors MUST be collected.
      var outcome, attempts := ReduceToSuccess(
        decryptClosure,
        edksToAttempt
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# If OnDecrypt fails to successfully decrypt any encrypted data key,
      //# then it MUST yield an error that includes all the collected errors.
      var SealedDecryptionMaterials :- outcome
      .MapFailure(errors => Types.CollectionOfErrors(
                      list := errors,
                      message := "No Configured Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."
                    )
      );

      assert decryptClosure.Ensures(Last(attempts).input, Success(SealedDecryptionMaterials), DropLast(attempts));
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# If the response does satisfy these requirements then OnDecrypt:
      // (blank line for duvet)
      //# - MUST set the plaintext data key on the [decryption materials](./structures.md#decryption-materials)
      //# - MUST immediately return the modified [decryption materials](../structures.md#decryption-materials).
      return Success(Types.OnDecryptOutput(
                       materials := SealedDecryptionMaterials
                     ));
    }
  }

  class OnDecryptEcdhDataKeyFilter
    extends DeterministicActionWithResult<Types.EncryptedDataKey, bool, Types.Error>
  {
    const keyAgreementScheme: Types.RawEcdhStaticConfigurations
    const compressedRecipientPublicKey: seq<uint8>
    const compressedSenderPublicKey: seq<uint8>

    constructor(
      keyAgreementScheme: Types.RawEcdhStaticConfigurations,
      compressedRecipientPublicKey: seq<uint8>,
      compressedSenderPublicKey: Option<seq<uint8>>
    )
    {
      this.keyAgreementScheme := keyAgreementScheme;
      this.compressedRecipientPublicKey := compressedRecipientPublicKey;
      if compressedSenderPublicKey.Some? {
        this.compressedSenderPublicKey := compressedSenderPublicKey.value;
      } else {
        this.compressedSenderPublicKey := [];
      }
    }

    ghost predicate Ensures(
      edk: Types.EncryptedDataKey,
      res: Result<bool, Types.Error>
    ) {
      && (
        && res.Success?
        && res.value
        ==>
          (edk.keyProviderId == KMS_ECDH_PROVIDER_ID ||
           edk.keyProviderId == RAW_ECDH_PROVIDER_ID)
          && UTF8.ValidUTF8Seq(edk.keyProviderId)
      )
    }

    method {:vcs_split_on_every_assert} Invoke(edk: Types.EncryptedDataKey)
      returns (res: Result<bool, Types.Error>)
      ensures Ensures(edk, res)
    {
      var providerInfo := edk.keyProviderInfo;
      var providerId := edk.keyProviderId;

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# - The key provider ID of the encrypted data key MUST have a value equal to the UTF8 encoded strings `raw-ecdh` OR `aws-kms-ecdh`.
      if ((providerId != RAW_ECDH_PROVIDER_ID) && (providerId != KMS_ECDH_PROVIDER_ID)) {
        return Success(false);
      }

      SequenceIsSafeBecauseItIsInMemory(providerInfo);
      :- Need(
        && |providerInfo| as uint64 <= ECDH_PROVIDER_INFO_521_LEN as uint64
        && ValidProviderInfoLength(providerInfo),
        E("EDK ProviderInfo longer than expected")
      );

      var keyringVersion := providerInfo[0 as uint32];
      :- Need(
        //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
        //# - The deserialized version value in the [key provider information](#key-provider-information) MUST match `0x01`.
        [keyringVersion] == RAW_ECDH_KEYRING_VERSION,
        E("Incorrect Keyring version found in provider info.")
      );

      var recipientPublicKeyLength := SeqToUInt32(providerInfo[ECDH_PROVIDER_INFO_RPL_INDEX..ECDH_PROVIDER_INFO_RPK_INDEX]);
      var recipientPublicKeyLengthIndex := ECDH_PROVIDER_INFO_RPK_INDEX as uint64 + recipientPublicKeyLength as uint64;
      var senderPublicKeyIndex := recipientPublicKeyLengthIndex + ECDH_PROVIDER_INFO_PUBLIC_KEY_LEN;
      :- Need(
        recipientPublicKeyLengthIndex + 4 < |providerInfo| as uint64,
        E("Key Provider Info Serialization Error. Serialized length less than expected.")
      );
      var providerInfoRecipientPublicKey := providerInfo[ECDH_PROVIDER_INFO_RPK_INDEX..recipientPublicKeyLengthIndex];
      var providerInfoSenderPublicKey := providerInfo[senderPublicKeyIndex..];

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# - MUST first verify that the uncompressed deserialized sender public key
      //#   and the uncompressed deserialized recipient public key match the public
      //#   keys configured on the keyring.
      if this.keyAgreementScheme.PublicKeyDiscovery? {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#publickeydiscovery
        //# - MUST verify that the recipient public key stored on
        //# the message ciphertext matches the configured recipient's
        //# public key.
        return Success(this.compressedRecipientPublicKey == providerInfoRecipientPublicKey);
      } else {
        return Success(
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#rawprivatekeytostaticpublickey
            //# - MUST verify that both the configured sender's and recipient's
            //#   public keys match the public keys stored on the message ciphertext.
            (this.compressedSenderPublicKey == providerInfoSenderPublicKey && this.compressedRecipientPublicKey == providerInfoRecipientPublicKey) ||
            (this.compressedSenderPublicKey == providerInfoRecipientPublicKey && this.compressedRecipientPublicKey == providerInfoSenderPublicKey)
          );
      }
    }
  }

  class DecryptSingleEncryptedDataKey
    extends ActionWithResult<
      Types.EncryptedDataKey,
      Materials.SealedDecryptionMaterials,
      Types.Error>
  {
    const materials: Materials.DecryptionMaterialsPendingPlaintextDataKey
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    const senderPublicKey: seq<uint8>
    const recipientPublicKey: seq<uint8>
    const keyAgreementScheme: Types.RawEcdhStaticConfigurations
    const curveSpec: PrimitiveTypes.ECDHCurveSpec

    constructor(
      materials: Materials.DecryptionMaterialsPendingPlaintextDataKey,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient,
      senderPublicKey: seq<uint8>,
      recipientPublicKey: seq<uint8>,
      keyAgreementScheme: Types.RawEcdhStaticConfigurations,
      curveSpec: PrimitiveTypes.ECDHCurveSpec
    )
      requires cryptoPrimitives.ValidState()
      requires
        && (keyAgreementScheme.PublicKeyDiscovery? || keyAgreementScheme.RawPrivateKeyToStaticPublicKey?)
      ensures
        && this.materials == materials
        && this.cryptoPrimitives == cryptoPrimitives
        && this.recipientPublicKey == recipientPublicKey
        && this.senderPublicKey == senderPublicKey
        && this.keyAgreementScheme == keyAgreementScheme
        && this.curveSpec == curveSpec
      ensures && (this.keyAgreementScheme.PublicKeyDiscovery? || this.keyAgreementScheme.RawPrivateKeyToStaticPublicKey?)
      ensures Invariant()
    {
      this.materials := materials;
      this.cryptoPrimitives := cryptoPrimitives;
      this.recipientPublicKey := recipientPublicKey;
      this.senderPublicKey := senderPublicKey;
      this.keyAgreementScheme := keyAgreementScheme;
      this.curveSpec := curveSpec;
      Modifies := cryptoPrimitives.Modifies;
    }

    ghost predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && cryptoPrimitives.ValidState()
      && cryptoPrimitives.Modifies == Modifies
    }

    ghost predicate Ensures(
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

    ghost predicate Requires(edk: Types.EncryptedDataKey){
      && UTF8.ValidUTF8Seq(edk.keyProviderId)
    }

    method {:vcs_split_on_every_assert} Invoke(
      edk: Types.EncryptedDataKey,
      ghost attemptsState: seq<ActionInvoke<Types.EncryptedDataKey, Result<Materials.SealedDecryptionMaterials, Types.Error>>>
    ) returns (res: Result<Materials.SealedDecryptionMaterials, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(edk, res, attemptsState)
    {
      assert UTF8.ValidUTF8Seq(edk.keyProviderId);

      var suite := materials.algorithmSuite;
      var keyProviderId := edk.keyProviderId;
      var providerInfo := edk.keyProviderInfo;
      var ciphertext := edk.ciphertext;

      var providerWrappedMaterial :- EdkWrapping.GetProviderWrappedMaterial(ciphertext, suite);

      SequenceIsSafeBecauseItIsInMemory(providerInfo);
      :- Need(
        && |providerInfo| as uint64 <= ECDH_PROVIDER_INFO_521_LEN as uint64
        && ValidProviderInfoLength(providerInfo),
        E("EDK ProviderInfo longer than expected")
      );

      var keyringVersion := providerInfo[0 as uint32];
      :- Need(
        [keyringVersion] == RAW_ECDH_KEYRING_VERSION,
        E("Incorrect Keyring version found in provider info.")
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# - The [ciphertext](#ciphertext) and [key provider information](#key-provider-information) MUST be successfully deserialized.
      var recipientPublicKeyLength := SeqToUInt32(providerInfo[ECDH_PROVIDER_INFO_RPL_INDEX..ECDH_PROVIDER_INFO_RPK_INDEX]);
      var recipientPublicKeyLengthIndex := ECDH_PROVIDER_INFO_RPK_INDEX as uint64 + recipientPublicKeyLength as uint64;
      var senderPublicKeyIndex := recipientPublicKeyLengthIndex + ECDH_PROVIDER_INFO_PUBLIC_KEY_LEN;
      :- Need(
        recipientPublicKeyLengthIndex + 4 < |providerInfo| as uint64,
        E("Key Provider Info Serialization Error. Serialized length less than expected.")
      );
      var providerInfoRecipientPublicKey := providerInfo[ECDH_PROVIDER_INFO_RPK_INDEX..recipientPublicKeyLengthIndex];
      var providerInfoSenderPublicKey := providerInfo[senderPublicKeyIndex..];

      var senderPublicKey :- DecompressPublicKey(providerInfoSenderPublicKey, this.curveSpec, this.cryptoPrimitives);
      var recipientPublicKey :- DecompressPublicKey(providerInfoRecipientPublicKey, this.curveSpec, this.cryptoPrimitives);

      var _ :- ValidatePublicKey(
        this.cryptoPrimitives,
        this.curveSpec,
        senderPublicKey
      );

      var _ :- ValidatePublicKey(
        this.cryptoPrimitives,
        this.curveSpec,
        recipientPublicKey
      );

      var sharedSecretPublicKey: seq<uint8>;
      var sharedSecretPrivateKey: seq<uint8>;
      match this.keyAgreementScheme {
        case PublicKeyDiscovery(publicKeyDiscovery) => {
          sharedSecretPublicKey := senderPublicKey;
          sharedSecretPrivateKey := publicKeyDiscovery.recipientStaticPrivateKey;
        }
        case RawPrivateKeyToStaticPublicKey(rawPrivateKeyToStaticPublicKey) => {
          sharedSecretPrivateKey := rawPrivateKeyToStaticPublicKey.senderStaticPrivateKey;
          if rawPrivateKeyToStaticPublicKey.recipientPublicKey == recipientPublicKey {
            sharedSecretPublicKey := recipientPublicKey;
          } else {
            sharedSecretPublicKey := senderPublicKey;
          }
        }
        case EphemeralPrivateKeyToStaticPublicKey(_) => {
          //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#ephemeralprivatekeytostaticpublickey
          //# On decrypt, the keyring MUST fail.
          return Failure(E("EphemeralPrivateKeyToStaticPublicKey Not allowed on decrypt"));
        }
      }

      var _ :- ValidatePublicKey(
        this.cryptoPrimitives,
        this.curveSpec,
        sharedSecretPublicKey
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# The keyring MUST derive the shared secret
      //# according to the configured [Key Agreement Schema](#key-agreement-procedure).
      // (blank line for duvet)
      //# If the Key Agreement step fails, then an error MUST be collected
      //# and the next encrypted data key in the filtered set MUST be attempted.
      var sharedSecret :- LocalDeriveSharedSecret(
        PrimitiveTypes.ECCPrivateKey(pem := sharedSecretPrivateKey),
        PrimitiveTypes.ECCPublicKey(der := sharedSecretPublicKey),
        this.curveSpec,
        this.cryptoPrimitives
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# The keyring MUST perform data key unwrapping according to the [Data Key Unwrapping section](#data-key-unwrapping).
      var ecdhUnwrap := new EcdhEdkWrapping.EcdhUnwrap(
        providerInfoSenderPublicKey,
        providerInfoRecipientPublicKey,
        sharedSecret,
        RAW_ECDH_KEYRING_VERSION,
        curveSpec,
        cryptoPrimitives
      );

      var unwrapOutputRes := EdkWrapping.UnwrapEdkMaterial(
        edk.ciphertext,
        materials,
        ecdhUnwrap
      );

      var unwrapOutput :- unwrapOutputRes;

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# If the response does satisfy these requirements then OnDecrypt:
      // (blank line for duvet)
      //# - MUST set the plaintext data key on the [decryption materials](./structures.md#decryption-materials)
      //# - MUST immediately return the modified [decryption materials](../structures.md#decryption-materials).
      var result :- Materials.DecryptionMaterialsAddDataKey(materials, unwrapOutput.plaintextDataKey, unwrapOutput.symmetricSigningKey);
      return Success(result);
    }
  }

  method {:vcs_split_on_every_assert} LocalDeriveSharedSecret(
    senderPrivateKey: PrimitiveTypes.ECCPrivateKey,
    recipientPublicKey: PrimitiveTypes.ECCPublicKey,
    curveSpec: PrimitiveTypes.ECDHCurveSpec,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res: Result<seq<uint8>, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.DeriveSharedSecret| > 0
              && Last(crypto.History.DeriveSharedSecret).output.Success?
              && Last(crypto.History.DeriveSharedSecret).input
                 == PrimitiveTypes.DeriveSharedSecretInput(
                      eccCurve := curveSpec,
                      privateKey := senderPrivateKey,
                      publicKey := recipientPublicKey
                    )
              && Last(crypto.History.DeriveSharedSecret).output.value.sharedSecret == res.value
  {
    var maybeSharedSecret := crypto.DeriveSharedSecret(
      PrimitiveTypes.DeriveSharedSecretInput(
        eccCurve := curveSpec,
        privateKey := senderPrivateKey,
        publicKey := recipientPublicKey
      )
    );

    var sharedSecretOutput :- maybeSharedSecret
    .MapFailure(e => Types.AwsCryptographyPrimitives( AwsCryptographyPrimitives := e));

    return Success(sharedSecretOutput.sharedSecret);
  }

  method {:vcs_split_on_every_assert} CompressPublicKey(
    publicKey: PrimitiveTypes.ECCPublicKey,
    curveSpec: PrimitiveTypes.ECDHCurveSpec,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res: Result<seq<uint8>, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.CompressPublicKey| > 0
              && Last(crypto.History.CompressPublicKey).output.Success?
              && Last(crypto.History.CompressPublicKey).input
                 == PrimitiveTypes.CompressPublicKeyInput(
                      eccCurve := curveSpec,
                      publicKey := publicKey
                    )
              && Last(crypto.History.CompressPublicKey).output.value.compressedPublicKey == res.value
  {
    var maybeCompressedPublicKey := crypto.CompressPublicKey(
      PrimitiveTypes.CompressPublicKeyInput(
        publicKey := publicKey,
        eccCurve := curveSpec
      )
    );

    var compressedPublicKey :- maybeCompressedPublicKey
    .MapFailure(e => Types.AwsCryptographyPrimitives( AwsCryptographyPrimitives := e));

    return Success(compressedPublicKey.compressedPublicKey);
  }

  method {:vcs_split_on_every_assert} DecompressPublicKey(
    publicKey: seq<uint8>,
    curveSpec: PrimitiveTypes.ECDHCurveSpec,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res: Result<seq<uint8>, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.DecompressPublicKey| > 0
              && Last(crypto.History.DecompressPublicKey).output.Success?
              && Last(crypto.History.DecompressPublicKey).input
                 == PrimitiveTypes.DecompressPublicKeyInput(
                      eccCurve := curveSpec,
                      compressedPublicKey := publicKey
                    )
              && Last(crypto.History.DecompressPublicKey).output.value.publicKey.der == res.value
  {
    var maybePublicKey := crypto.DecompressPublicKey(
      PrimitiveTypes.DecompressPublicKeyInput(
        compressedPublicKey := publicKey,
        eccCurve := curveSpec
      )
    );

    var publicKey :- maybePublicKey
    .MapFailure(e => Types.AwsCryptographyPrimitives( AwsCryptographyPrimitives := e));

    return Success(publicKey.publicKey.der);
  }

  function SerializeProviderInfo(
    senderPublicKey: seq<uint8>,
    recipientPublicKey: seq<uint8>
  ): (res: seq<uint8>)
    requires ValidCompressedPublicKeyLength(recipientPublicKey)
    requires ValidCompressedPublicKeyLength(senderPublicKey)
    ensures |res| ==
            |RAW_ECDH_KEYRING_VERSION| +
            |UInt32ToSeq(|recipientPublicKey| as uint32)| +
            |recipientPublicKey| +
            |UInt32ToSeq(|senderPublicKey| as uint32)| +
            |senderPublicKey|
  {
    RAW_ECDH_KEYRING_VERSION +
    UInt32ToSeq(|recipientPublicKey| as uint32) +
    recipientPublicKey +
    UInt32ToSeq(|senderPublicKey| as uint32) +
    senderPublicKey
  }

  method {:vcs_split_on_every_assert} GenerateEphemeralEccKeyPair(
    curveSpec: PrimitiveTypes.ECDHCurveSpec,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res: Result<PrimitiveTypes.GenerateECCKeyPairOutput, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.GenerateECCKeyPair| > 0
              && Last(crypto.History.GenerateECCKeyPair).output.Success?
              && Last(crypto.History.GenerateECCKeyPair).input
                 == PrimitiveTypes.GenerateECCKeyPairInput(
                      eccCurve := curveSpec
                    )
  {
    var maybeKeyPair := crypto.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := curveSpec
      )
    );

    var keyPair :- maybeKeyPair.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));
    res := Success(keyPair);
  }

  method ValidatePublicKey(
    crypto: AtomicPrimitives.AtomicPrimitivesClient,
    curveSpec: PrimitiveTypes.ECDHCurveSpec,
    publicKey: seq<uint8>
  ) returns (res: Result<bool, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures res.Success? ==>
              && |crypto.History.ValidatePublicKey| > 0
              && Last(crypto.History.ValidatePublicKey).output.Success?
              && Last(crypto.History.ValidatePublicKey).input
                 == PrimitiveTypes.ValidatePublicKeyInput(
                      eccCurve := curveSpec,
                      publicKey := publicKey
                    )
  {
    var maybeValidate := crypto.ValidatePublicKey(
      PrimitiveTypes.ValidatePublicKeyInput(
        eccCurve := curveSpec,
        publicKey := publicKey
      )
    );

    var validate :- maybeValidate.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));
    res := Success(validate.success);
  }

  function CurveSpecTypeToString(c: PrimitiveTypes.ECDHCurveSpec): string
  {
    match c {
      case ECC_NIST_P256 => "p256"
      case ECC_NIST_P384 => "p384"
      case ECC_NIST_P521 => "p521"
      case SM2 => "sm2"
    }
  }

  function E(s : string) : Types.Error {
    Types.AwsCryptographicMaterialProvidersException(message := s)
  }
}
