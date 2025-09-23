// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../Keyring.dfy"
include "../../Materials.dfy"
include "../../AlgorithmSuites.dfy"
include "../../KeyWrapping/EdkWrapping.dfy"
include "../../KeyWrapping/EcdhEdkWrapping.dfy"
include "Constants.dfy"
include "../../CanonicalEncryptionContext.dfy"
include "AwsKmsMrkMatchForDecrypt.dfy"
include "../../AwsArnParsing.dfy"
include "AwsKmsUtils.dfy"
include "../../ErrorMessages.dfy"
include "../RawECDHKeyring.dfy"

include "../../../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module {:options "/functionSyntax:4" } AwsKmsEcdhKeyring {
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
  import opened AlgorithmSuites
  import RawECDHKeyring
  import Keyring
  import Materials
  import Types = AwsCryptographyMaterialProvidersTypes
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import UUID
  import EdkWrapping
  import MaterialWrapping
  import EcdhEdkWrapping
  import ErrorMessages
  import AtomicPrimitives
  import CanonicalEncryptionContext

  const AWS_KMS_ECDH_KEYRING_VERSION := RawECDHKeyring.RAW_ECDH_KEYRING_VERSION

  //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#interface
  //= type=implication
  //# MUST implement the [AWS Encryption SDK Keyring interface](../keyring-interface.md#interface)
  class AwsKmsEcdhKeyring
    extends Keyring.VerifiableInterface
  {
    const client: KMS.IKMSClient
    const senderKmsKeyId: Option<AwsKmsIdentifierString>
    const senderPublicKey: Option<KMS.PublicKeyType>
    const recipientPublicKey: KMS.PublicKeyType
    const compressedSenderPublicKey: Option<seq<uint8>>
    const compressedRecipientPublicKey: seq<uint8>
    const keyAgreementScheme: Types.KmsEcdhStaticConfigurations
    const curveSpec: PrimitiveTypes.ECDHCurveSpec
    const grantTokens: KMS.GrantTokenList
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient

    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && client.ValidState()
      && client.Modifies <= Modifies
      && History !in client.Modifies
      && cryptoPrimitives.ValidState()
      && cryptoPrimitives.Modifies <= Modifies
      && History !in cryptoPrimitives.Modifies
    }

    constructor (
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#initialization
      //= type=implication
      //# - MUST provide a [Key Agreement Schema](#key-agreement-schema)
      KeyAgreementScheme: Types.KmsEcdhStaticConfigurations,
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#initialization
      //= type=implication
      //# - MUST provide a [Curve Specification](#curve-specification)
      curveSpec: PrimitiveTypes.ECDHCurveSpec,
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#initialization
      //= type=implication
      //# - MUST provide an AWS KMS SDK client
      client: KMS.IKMSClient,
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#initialization
      //= type=implication
      //# - MAY provide a list of Grant Tokens
      grantTokens: KMS.GrantTokenList,

      senderKmsKeyId: Option<AwsKmsIdentifierString>,
      senderPublicKey: Option<KMS.PublicKeyType>,
      recipientPublicKey: KMS.PublicKeyType,
      compressedSenderPublicKey: Option<seq<uint8>>,
      compressedRecipientPublicKey: seq<uint8>,
      cryptoPrimitives : AtomicPrimitives.AtomicPrimitivesClient
    )
      requires client.ValidState()
      requires cryptoPrimitives.ValidState()
      requires KMS.IsValid_PublicKeyType(recipientPublicKey)
      requires senderPublicKey.Some? ==> KMS.IsValid_PublicKeyType(senderPublicKey.value)
      requires |recipientPublicKey| < UINT32_LIMIT
      ensures ValidState() && fresh(this) && fresh(History)
              && fresh(Modifies - client.Modifies - cryptoPrimitives.Modifies)
    {
      this.keyAgreementScheme  := KeyAgreementScheme;
      this.curveSpec   := curveSpec;

      this.client      := client;
      this.grantTokens := grantTokens;
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#initialization
      //= type=implication
      //# the keyring MUST set the recipient's public key on the keyring.
      this.recipientPublicKey := recipientPublicKey;
      this.senderPublicKey := senderPublicKey;
      this.compressedSenderPublicKey := compressedSenderPublicKey;
      this.compressedRecipientPublicKey := compressedRecipientPublicKey;
      this.senderKmsKeyId := senderKmsKeyId;
      this.cryptoPrimitives := cryptoPrimitives;

      History := new Types.IKeyringCallHistory();
      Modifies := {History};
      Modifies := Modifies + client.Modifies + cryptoPrimitives.Modifies;
    }

    ghost predicate OnEncryptEnsuresPublicly (
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

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
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

      ensures StringifyEncryptionContext(input.materials.encryptionContext).Failure?
              ==>
                res.Failure?
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //= type=implication
      //# OnEncrypt MUST fail if configured with a
      //# [KmsPublicKeyDiscovery Key Agreement Configuration](../key-agreement-schemas.md#kmspublickeydiscovery)
      ensures this.keyAgreementScheme.KmsPublicKeyDiscovery? ==> res.Failure?
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //= type=implication
      //# If the keyring cannot serialize
      //# the encryption context, OnEncrypt MUST fail.
      ensures CanonicalEncryptionContext.EncryptionContextToAAD(input.materials.encryptionContext).Failure? ==> res.Failure?
    {
      :- Need(
        !keyAgreementScheme.KmsPublicKeyDiscovery?,
        E("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")
      );

        // Impossible to hit on encrypt, but dafny has a hard time inferring that if we are not discovery we
        // will have senderKmsKeyId.
      :- Need(
        this.senderKmsKeyId.Some?,
        E("Keyring MUST be configured with a sender KMS Key ID")
      );
        // Impossible to hit on encrypt, but dafny has a hard time inferring that if we are not discovery we
        // will have senderKmsKeyId.
      :- Need(
        this.senderPublicKey.Some?,
        E("Keyring MUST be configured with a senderPublicKey")
      );

      var senderKmsKeyId := this.senderKmsKeyId.value;

      var materials := input.materials;
      var suite := input.materials.algorithmSuite;
      var stringifiedEncCtx :- StringifyEncryptionContext(input.materials.encryptionContext);

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //# If the call to KMS DeriveSharedSecret fails, the keyring MUST fail.
      var sharedSecret :- DeriveSharedSecret(
        client,
        senderKmsKeyId,
        recipientPublicKey,
        grantTokens
      );

      var operationCompressedSenderPublicKey := if this.compressedSenderPublicKey.None? then []
      else this.compressedSenderPublicKey.value;

      var curveSpecUtf8 :- UTF8.Encode(
        RawECDHKeyring.CurveSpecTypeToString(this.curveSpec)
      ).MapFailure(WrapStringToError);
      var canonicalizedEC :- CanonicalEncryptionContext.EncryptionContextToAAD(input.materials.encryptionContext);

      var fixedInfo := EcdhEdkWrapping.SerializeFixedInfo(
        ECDH_KDF_UTF8,
        curveSpecUtf8,
        operationCompressedSenderPublicKey,
        this.compressedRecipientPublicKey,
        canonicalizedEC,
        AWS_KMS_ECDH_KEYRING_VERSION
      );

      var ecdhGenerateAndWrap := new EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial(
        sharedSecret,
        fixedInfo,
        cryptoPrimitives
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //# The keyring MUST perform data key wrapping according to the [Data Key Wrapping section](../raw-ecdh-keyring.md#data-key-wrapping).
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
        && RawECDHKeyring.ValidCompressedPublicKeyLength(operationCompressedSenderPublicKey)
        && RawECDHKeyring.ValidCompressedPublicKeyLength(compressedRecipientPublicKey),
        E("Invalid compressed public key length.")
      );

      var edk := Types.EncryptedDataKey(
        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
        //# - The [key provider id](../structures.md#key-provider-id) MUST be the UTF8 encoded string "aws-kms-ecdh".
        keyProviderId := KMS_ECDH_PROVIDER_ID,
        keyProviderInfo := RawECDHKeyring.SerializeProviderInfo(operationCompressedSenderPublicKey, compressedRecipientPublicKey),
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

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-keyring.md#ondecrypt
    //= type=implication
    //# OnDecrypt MUST take [decryption materials]
    //# (../structures.md#decryption-materials) and a list of [encrypted data
    //# keys](../structures.md#encrypted-data-key) as input.
    method {:vcs_split_on_every_assert} OnDecrypt'(
      input: Types.OnDecryptInput
    )
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
    {
      var materials := input.materials;
      var suite := input.materials.algorithmSuite;

        //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
        //# If the decryption materials already contain a plaintext data key,
        //# OnDecrypt MUST fail
        //# and MUST NOT modify the [decryption materials](structures.md#decryption-materials).
      :- Need(
        Materials.DecryptionMaterialsWithoutPlaintextDataKey(materials),
        E("Keyring received decryption materials that already contain a plaintext data key.")
      );

      var filter := new OnDecryptEcdhDataKeyFilter(
        keyAgreementScheme, this.compressedRecipientPublicKey, this.compressedSenderPublicKey
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
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
        this.compressedRecipientPublicKey,
        client,
        grantTokens,
        keyAgreementScheme,
        curveSpec
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# For each encrypted data key in the filtered set, one at a time, the OnDecrypt MUST attempt to decrypt the data key.
      //# If this attempt results in an error, then these errors MUST be collected.
      var outcome, attempts := ReduceToSuccess(
        decryptClosure,
        edksToAttempt
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# If OnDecrypt fails to successfully decrypt any encrypted data key,
      //# then it MUST yield an error that includes all the collected errors.
      var SealedDecryptionMaterials :- outcome
      .MapFailure(errors => Types.CollectionOfErrors(
                      list := errors,
                      message := "No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."
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

  method {:vcs_split_on_every_assert} DeriveSharedSecret(
    client: KMS.IKMSClient,
    senderAwsKmsKey: AwsKmsIdentifierString,
    recipientPublicKey: seq<uint8>,
    grantTokens: KMS.GrantTokenList
  )
    returns (res :Result<seq<uint8>, Types.Error>)
    requires client.ValidState()
    requires KMS.IsValid_PublicKeyType(recipientPublicKey)
    modifies client.Modifies
    ensures client.ValidState()
    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
    //= type=implication
    //# To attempt to generate a shared secret,
    //# OnEncrypt MUST call [AWS KMS DeriveSharedSecret]()
    //# the keyring MUST call with a request constructed as follows:
    ensures res.Success? ==>
              && 0 < |client.History.DeriveSharedSecret|
              && Last(client.History.DeriveSharedSecret).input
                 == KMS.DeriveSharedSecretRequest(
                      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
                      //= type=implication
                      //# - `KeyId` MUST be the configured AWS KMS key identifier in the schema
                      KeyId := senderAwsKmsKey,
                      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
                      //= type=implication
                      //# - `KeyAgreementAlgorithm` MUST be "ECDH"
                      KeyAgreementAlgorithm := KMS.KeyAgreementAlgorithmSpec.ECDH,
                      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
                      //= type=implication
                      //# - `PublicKey` MUST be the configured Recipient Public Key on the schema
                      PublicKey := recipientPublicKey,
                      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
                      //= type=implication
                      //# - `GrantTokens` MUST be this keyring's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
                      GrantTokens := Some(grantTokens)
                    )
  {
    var deriveSharedSecretRequest := KMS.DeriveSharedSecretRequest(
      KeyId := senderAwsKmsKey,
      KeyAgreementAlgorithm := KMS.KeyAgreementAlgorithmSpec.ECDH,
      PublicKey := recipientPublicKey,
      GrantTokens := Some(grantTokens)
    );

    var maybeDeriveSharedSecret := client.DeriveSharedSecret(deriveSharedSecretRequest);

    //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
    //= type=implication
    //# If the call to KMS DeriveSharedSecret fails, the keyring MUST fail.
    var deriveSharedSecretResponse :- maybeDeriveSharedSecret
    .MapFailure(e => Types.ComAmazonawsKms( ComAmazonawsKms := e ));

    :- Need(
      && deriveSharedSecretResponse.KeyId.Some?
      && deriveSharedSecretResponse.SharedSecret.Some?
      && deriveSharedSecretResponse.KeyAgreementAlgorithm.Some?
      && deriveSharedSecretResponse.KeyId.value == senderAwsKmsKey
      && deriveSharedSecretResponse.KeyAgreementAlgorithm.value == KMS.KeyAgreementAlgorithmSpec.ECDH,
      E(s := "Invalid response from KMS DeriveSharedSecret")
    );

    return Success(deriveSharedSecretResponse.SharedSecret.value);
  }

  class DecryptSingleEncryptedDataKey
    extends ActionWithResult<
      Types.EncryptedDataKey,
      Materials.SealedDecryptionMaterials,
      Types.Error>
  {
    const materials: Materials.DecryptionMaterialsPendingPlaintextDataKey
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    const recipientPublicKey: seq<uint8>
    const client: KMS.IKMSClient
    const grantTokens: KMS.GrantTokenList
    const keyAgreementScheme: Types.KmsEcdhStaticConfigurations
    const curveSpec: PrimitiveTypes.ECDHCurveSpec

    constructor(
      materials: Materials.DecryptionMaterialsPendingPlaintextDataKey,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient,
      recipientPublicKey: seq<uint8>,
      client: KMS.IKMSClient,
      grantTokens: KMS.GrantTokenList,
      keyAgreementScheme: Types.KmsEcdhStaticConfigurations,
      curveSpec: PrimitiveTypes.ECDHCurveSpec
    )
      requires cryptoPrimitives.ValidState() && client.ValidState()
      ensures
        && this.materials == materials
        && this.cryptoPrimitives == cryptoPrimitives
        && this.recipientPublicKey == recipientPublicKey
        && this.keyAgreementScheme == keyAgreementScheme
        && this.client == client
        && this.curveSpec == curveSpec
        && this.grantTokens == grantTokens
      ensures Invariant()
    {
      this.materials := materials;
      this.cryptoPrimitives := cryptoPrimitives;
      this.recipientPublicKey := recipientPublicKey;
      this.keyAgreementScheme := keyAgreementScheme;
      this.client := client;
      this.curveSpec := curveSpec;
      this.grantTokens := grantTokens;
      Modifies := cryptoPrimitives.Modifies + client.Modifies;
    }

    ghost predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && cryptoPrimitives.ValidState() && client.ValidState()
      && cryptoPrimitives.Modifies + client.Modifies == Modifies
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

    method {:vcs_split_on_every_assert}  Invoke(
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
      var providerInfo := edk.keyProviderInfo;
      var ciphertext := edk.ciphertext;

      var providerWrappedMaterial :- EdkWrapping.GetProviderWrappedMaterial(ciphertext, suite);

      SequenceIsSafeBecauseItIsInMemory(providerInfo);
      :- Need(
        && |providerInfo| as uint64 <= ECDH_PROVIDER_INFO_521_LEN as uint64
        && RawECDHKeyring.ValidProviderInfoLength(providerInfo),
        E("EDK ProviderInfo longer than expected")
      );

      var keyringVersion := providerInfo[0 as uint32];
      :- Need(
        [keyringVersion] == AWS_KMS_ECDH_KEYRING_VERSION,
        E("Incorrect Keyring version found in provider info.")
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# - The [ciphertext](#ciphertext) and [key provider information](#key-provider-information) MUST be successfully deserialized.
      var recipientPublicKeyLength := SeqToUInt32(providerInfo[ECDH_PROVIDER_INFO_RPL_INDEX..ECDH_PROVIDER_INFO_RPK_INDEX]);
      var recipientPublicKeyLengthIndex := ECDH_PROVIDER_INFO_RPK_INDEX as uint64 + recipientPublicKeyLength as uint64;
      var senderPublicKeyIndex := recipientPublicKeyLengthIndex + ECDH_PROVIDER_INFO_PUBLIC_KEY_LEN;
      SequenceIsSafeBecauseItIsInMemory(providerInfo);
      :- Need(
        recipientPublicKeyLengthIndex + 4 < |providerInfo| as uint64,
        E("Key Provider Info Serialization Error. Serialized length less than expected.")
      );
      var providerInfoRecipientPublicKey := providerInfo[ECDH_PROVIDER_INFO_RPK_INDEX..recipientPublicKeyLengthIndex];
      var providerInfoSenderPublicKey := providerInfo[senderPublicKeyIndex..];

      var senderPublicKey :- RawECDHKeyring.DecompressPublicKey(providerInfoSenderPublicKey, this.curveSpec, this.cryptoPrimitives);
      var recipientPublicKey :- RawECDHKeyring.DecompressPublicKey(providerInfoRecipientPublicKey, this.curveSpec, this.cryptoPrimitives);

      var _ :- RawECDHKeyring.ValidatePublicKey(
        this.cryptoPrimitives,
        this.curveSpec,
        senderPublicKey
      );

      var _ :- RawECDHKeyring.ValidatePublicKey(
        this.cryptoPrimitives,
        this.curveSpec,
        recipientPublicKey
      );

      :- Need(
        && KMS.IsValid_PublicKeyType(senderPublicKey)
        && KMS.IsValid_PublicKeyType(this.recipientPublicKey),
        E("Received serialized sender public key of incorrect length")
      );

      var sharedSecretPublicKey: seq<uint8>;
      var sharedSecretKmsKeyId;
      match this.keyAgreementScheme {
        case KmsPublicKeyDiscovery(kmsPublicKeyDiscovery) => {
          var _ :- ValidateKmsKeyId(kmsPublicKeyDiscovery.recipientKmsIdentifier);
          sharedSecretPublicKey := senderPublicKey;
          sharedSecretKmsKeyId := kmsPublicKeyDiscovery.recipientKmsIdentifier;
        }
        case KmsPrivateKeyToStaticPublicKey(kmsPrivateKeyToStaticPublicKey) => {
          var _ :- ValidateKmsKeyId(kmsPrivateKeyToStaticPublicKey.senderKmsIdentifier);
          sharedSecretKmsKeyId := kmsPrivateKeyToStaticPublicKey.senderKmsIdentifier;
          if kmsPrivateKeyToStaticPublicKey.recipientPublicKey == recipientPublicKey {
            sharedSecretPublicKey := recipientPublicKey;
          } else {
            sharedSecretPublicKey := senderPublicKey;
          }
        }
      }

      :- Need(
        KMS.IsValid_PublicKeyType(sharedSecretPublicKey),
        E("Received Recipient Public Key of incorrect expected length")
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# The keyring MUST derive the shared secret
      //# by calling [AWS KMS DeriveSharedSecret]()
      var sharedSecret :- DeriveSharedSecret(
        client, sharedSecretKmsKeyId, sharedSecretPublicKey, grantTokens
      );

      var ecdhUnwrap := new EcdhEdkWrapping.EcdhUnwrap(
        providerInfoSenderPublicKey,
        providerInfoRecipientPublicKey,
        sharedSecret,
        AWS_KMS_ECDH_KEYRING_VERSION,
        curveSpec,
        cryptoPrimitives
      );

      var unwrapOutputRes := RawECDHKeyring.EdkWrapping.UnwrapEdkMaterial(
        edk.ciphertext,
        materials,
        ecdhUnwrap
      );

      var unwrapOutput :- unwrapOutputRes;

      var result :- Materials.DecryptionMaterialsAddDataKey(materials, unwrapOutput.plaintextDataKey, unwrapOutput.symmetricSigningKey);
      return Success(result);
    }
  }

  class OnDecryptEcdhDataKeyFilter
    extends DeterministicActionWithResult<Types.EncryptedDataKey, bool, Types.Error>
  {
    const keyAgreementScheme: Types.KmsEcdhStaticConfigurations
    const compressedRecipientPublicKey: seq<uint8>
    const compressedSenderPublicKey: seq<uint8>

    constructor(
      keyAgreementScheme: Types.KmsEcdhStaticConfigurations,
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

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#ondecrypt
      //# - The key provider ID of the encrypted data key MUST have a value equal to the UTF8 encoded strings `raw-ecdh` OR `aws-kms-ecdh`.
      if ((providerId != RAW_ECDH_PROVIDER_ID) && (providerId != KMS_ECDH_PROVIDER_ID)) {
        return Success(false);
      }
      SequenceIsSafeBecauseItIsInMemory(providerInfo);
      :- Need(
        && |providerInfo| as uint64 <= ECDH_PROVIDER_INFO_521_LEN as uint64
        && RawECDHKeyring.ValidProviderInfoLength(providerInfo),
        E("EDK ProviderInfo longer than expected")
      );

      var keyringVersion := providerInfo[0 as uint32];
      :- Need(
        [keyringVersion] == AWS_KMS_ECDH_KEYRING_VERSION,
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

      if this.keyAgreementScheme.KmsPublicKeyDiscovery? {
        //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmspublickeydiscovery
        //# - MUST verify that the configured recipient's public key
        //#   matches the public key stored on the message ciphertext.
        return Success(this.compressedRecipientPublicKey == providerInfoRecipientPublicKey);
      } else {
        return Success(
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#kmsprivatekeytostaticpublickey
            //# - MUST verify that both the configured sender's and recipient's
            //#   public keys match the public keys stored on the message ciphertext.
            (this.compressedSenderPublicKey == providerInfoSenderPublicKey && this.compressedRecipientPublicKey == providerInfoRecipientPublicKey) ||
            (this.compressedSenderPublicKey == providerInfoRecipientPublicKey && this.compressedRecipientPublicKey == providerInfoSenderPublicKey)
          );
      }
    }
  }

  function E(s : string) : Types.Error {
    Types.AwsCryptographicMaterialProvidersException(message := s)
  }
}
