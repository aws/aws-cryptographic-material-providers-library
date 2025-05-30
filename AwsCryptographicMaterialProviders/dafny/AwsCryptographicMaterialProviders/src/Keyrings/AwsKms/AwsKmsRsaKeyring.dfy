// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../Keyring.dfy"
include "../../Materials.dfy"
include "../../CanonicalEncryptionContext.dfy"
include "../../AlgorithmSuites.dfy"
include "../../AwsArnParsing.dfy"
include "Constants.dfy"
include "AwsKmsUtils.dfy"
include "../../KeyWrapping/MaterialWrapping.dfy"
include "../../KeyWrapping/EdkWrapping.dfy"
include "../../ErrorMessages.dfy"

include "../../../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module AwsKmsRsaKeyring {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import opened Actions
  import UTF8
  import UUID
  import AtomicPrimitives
  import Crypto = AwsCryptographyPrimitivesTypes
  import Keyring
  import Materials
  import Types = AwsCryptographyMaterialProvidersTypes
  import KMS = ComAmazonawsKmsTypes
  import CanonicalEncryptionContext
  import AwsArnParsing
  import opened Constants
  import AlgorithmSuites
  import Seq
  import MaterialWrapping
  import EdkWrapping
  import AwsKmsUtils
  import ErrorMessages

  const MIN_KMS_RSA_KEY_LEN: Crypto.RSAModulusLengthBits := 2048

  class AwsKmsRsaKeyring
    extends Keyring.VerifiableInterface
  {
    const client: Option<KMS.IKMSClient>
    const grantTokens: KMS.GrantTokenList
    const awsKmsKey: AwsArnParsing.AwsKmsIdentifierString
    const awsKmsArn: AwsArnParsing.AwsKmsIdentifier
    const paddingScheme: KMS.EncryptionAlgorithmSpec
    const publicKey: Option<seq<uint8>>
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient

    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && cryptoPrimitives.Modifies <= Modifies
      && History !in cryptoPrimitives.Modifies
      && cryptoPrimitives.ValidState()
      && (client.Some? ==>
            && client.value.ValidState()
            && client.value.Modifies <= Modifies
            && History !in client.value.Modifies)
      && (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
      && UTF8.Encode(awsKmsKey).Success?
      && (publicKey.Some? ==> ValidRSAKeyLength(publicKey.value))
    }

    predicate ValidRSAKeyLength(publicKey: seq<uint8>) {
      var rsaKeyLengthRes := cryptoPrimitives.GetRSAKeyModulusLength(
                               Crypto.GetRSAKeyModulusLengthInput(publicKey := publicKey));
      && rsaKeyLengthRes.Success?
      && rsaKeyLengthRes.value.length >= MIN_KMS_RSA_KEY_LEN
    }

    constructor (
      publicKey: Option<seq<uint8>>,
      awsKmsKey: AwsArnParsing.AwsKmsIdentifierString,
      paddingScheme: KMS.EncryptionAlgorithmSpec,
      client: Option<KMS.IKMSClient>,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient,
      grantTokens: KMS.GrantTokenList
    )
      requires cryptoPrimitives.ValidState()
      requires client.Some? ==> client.value.ValidState()
      requires publicKey.Some? ==>
                 && var rsaKeyLengthRes := cryptoPrimitives.GetRSAKeyModulusLength(
                                             Crypto.GetRSAKeyModulusLengthInput(publicKey := publicKey.value));
                 && rsaKeyLengthRes.Success?
                 && rsaKeyLengthRes.value.length >= MIN_KMS_RSA_KEY_LEN
      requires (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
      ensures ValidState() && fresh(this) && fresh(History)
              && fresh(Modifies - (if client.Some? then client.value.Modifies else {}) - cryptoPrimitives.Modifies)
    {
      History := new Types.IKeyringCallHistory();
      Modifies := {History};
      if client.Some? {
        Modifies := Modifies + client.value.Modifies;
      }
      Modifies := Modifies + cryptoPrimitives.Modifies;

      var parsedAwsKmsId  := AwsArnParsing.ParseAwsKmsIdentifier(awsKmsKey);
      this.publicKey := publicKey;
      this.awsKmsKey := awsKmsKey;
      this.awsKmsArn      := parsedAwsKmsId.value;
      this.paddingScheme := paddingScheme;
      this.client := client;
      this.cryptoPrimitives := cryptoPrimitives;
      this.grantTokens := grantTokens;
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


    method OnEncrypt'(input: Types.OnEncryptInput)
      returns (res: Result<Types.OnEncryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnEncryptEnsuresPublicly(input, res)
      ensures unchanged(History)
      ensures res.Success?
              ==>
                && Materials.ValidEncryptionMaterialsTransition(
                  input.materials,
                  res.value.materials
                )
      ensures (publicKey.None? || |publicKey.Extract()| == 0)
              ==> res.Failure?

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#onencrypt
      //= type=implication
      //# OnEncrypt MUST fail if the input [encryption materials](../structures.md#encryption-materials)
      //# contains an [algorithm suite](../algorithm-suites.md) containing an
      //# [asymmetric signature](../algorithm-suites.md#asymmetric-signature-algorithm).
      ensures !(input.materials.algorithmSuite.signature.None?)
              ==> res.Failure?
    {
      OptionalSequenceIsSafeBecauseItIsInMemory(this.publicKey);
      :- Need(
        this.publicKey.Some? && |this.publicKey.Extract()|  as uint64 > 0,
        Types.AwsCryptographicMaterialProvidersException(
          message := "A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt"));

      :- Need(
        input.materials.algorithmSuite.signature.None?,
        Types.AwsCryptographicMaterialProvidersException(
          message := "AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing." +
          " Please specify an algorithm suite without asymmetric signing."));

      var wrap := new KmsRsaWrapKeyMaterial(
        publicKey.value,
        paddingScheme,
        cryptoPrimitives
      );
      var generateAndWrap := new KmsRsaGenerateAndWrapKeyMaterial(
        publicKey.value,
        paddingScheme,
        cryptoPrimitives
      );

      var wrapOutput :- EdkWrapping.WrapEdkMaterial<KmsRsaWrapInfo>(
        encryptionMaterials := input.materials,
        wrap := wrap,
        generateAndWrap := generateAndWrap
      );
      var symmetricSigningKeyList :=
        if wrapOutput.symmetricSigningKey.Some? then
          Some([wrapOutput.symmetricSigningKey.value])
        else
          None;

      var edk: Types.EncryptedDataKey := Types.EncryptedDataKey(
        keyProviderId := RSA_PROVIDER_ID,
        keyProviderInfo := UTF8.Encode(awsKmsKey).value,
        ciphertext := wrapOutput.wrappedMaterial
      );

      var returnMaterials;
      if (wrapOutput.GenerateAndWrapEdkMaterialOutput?) {
        returnMaterials :- Materials.EncryptionMaterialAddDataKey(input.materials, wrapOutput.plaintextDataKey, [edk], symmetricSigningKeyList);
      } else if (wrapOutput.WrapOnlyEdkMaterialOutput?) {
        returnMaterials :- Materials.EncryptionMaterialAddEncryptedDataKeys(input.materials, [edk], symmetricSigningKeyList);
      }
      return Success(Types.OnEncryptOutput(materials := returnMaterials));
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

      ensures res.Success?
              ==>
                && Materials.DecryptionMaterialsTransitionIsValid(
                  input.materials,
                  res.value.materials)
      ensures client.None? ==> res.Failure?

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#ondecrypt
      //= type=implication
      //# OnDecrypt MUST fail if the input [decryption materials](../structures.md#decryption-materials)
      //# contains an [algorithm suite](../algorithm-suites.md) containing an
      //# [asymmetric signature](../algorithm-suites.md#asymmetric-signature-algorithm).
      ensures !(input.materials.algorithmSuite.signature.None?)
              ==> res.Failure?
    {

      :- Need(
        client.Some?,
        Types.AwsCryptographicMaterialProvidersException(
          message := "An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt"));

      var materials := input.materials;
      :- Need(
        Materials.DecryptionMaterialsWithoutPlaintextDataKey(materials),
        Types.AwsCryptographicMaterialProvidersException(
          message := "Keyring received decryption materials that already contain a plaintext data key."));

      :- AwsKmsUtils.OkForDecrypt(awsKmsArn, awsKmsKey);

      :- Need(
        input.materials.algorithmSuite.signature.None?,
        Types.AwsCryptographicMaterialProvidersException(
          message := "AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing." +
          " Please specify an algorithm suite without asymmetric signing."));

      var filter := new AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter(awsKmsArn, RSA_PROVIDER_ID);
      var edksToAttempt :- FilterWithResult(filter, input.encryptedDataKeys);

      SequenceIsSafeBecauseItIsInMemory(edksToAttempt);
      if (0 == |edksToAttempt| as uint64) {
        var errorMessage :- ErrorMessages.IncorrectDataKeys(input.encryptedDataKeys, input.materials.algorithmSuite);
        return Failure(
            Types.AwsCryptographicMaterialProvidersException(
              message := errorMessage
            ));
      }

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-rsa-keyring.md#onencrypt
      //# OnEncrypt MUST calculate a Encryption Context Digest by:
      //  1. Serializing The [encryption context](structures.md#encryption-context-1) from the input
      //     [encryption materials](../structures.md#encryption-materials) according to the [encryption context serialization specification](../structures.md#serialization).
      //  2. Taking the SHA-384 Digest of this concatenation.
      var encryptionContextDigest :- EncryptionContextDigest(cryptoPrimitives, materials.encryptionContext);

      var decryptClosure := new DecryptSingleAWSRSAEncryptedDataKey(
        materials,
        client.value,
        awsKmsKey,
        paddingScheme,
        encryptionContextDigest,
        grantTokens
      );

      var outcome, attempts := ReduceToSuccess(
        decryptClosure,
        edksToAttempt
      );

      var SealedDecryptionMaterials :- outcome
      .MapFailure(errors => Types.CollectionOfErrors(list := errors,
                                                                   message := "No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."));

      assert decryptClosure.Ensures(Seq.Last(attempts).input, Success(SealedDecryptionMaterials), Seq.DropLast(attempts));
      return Success(Types.OnDecryptOutput(
                       materials := SealedDecryptionMaterials
                     ));
    }
  }

  method EncryptionContextDigest(cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient, encryptionContext: Types.EncryptionContext)
    returns (output: Result<seq<uint8>, Types.Error>)
    requires cryptoPrimitives.ValidState()
    modifies cryptoPrimitives.Modifies
    ensures cryptoPrimitives.ValidState()
  {
    var canonicalEC :- CanonicalEncryptionContext.EncryptionContextToAAD(encryptionContext);

    var DigestInput := Crypto.DigestInput(
      digestAlgorithm := Crypto.SHA_384,
      message := canonicalEC
    );
    var maybeDigest := cryptoPrimitives.Digest(DigestInput);
    var digest :- maybeDigest.MapFailure(e => Types.AwsCryptographyPrimitives(e));

    // The digest is not truncated.
    // There is an impact on the key size.
    // See: https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html
    // This is not safe to do for 1024 keys,
    // but AWS KMS does not support these keys.
    // Further we use SHA_384 to save a little on size
    // and avoid even the possibility of length extension.
    // Though length extension does not matter in this situation,
    // because a decryptor already has access to the key.
    return Success(digest);
  }

  class DecryptSingleAWSRSAEncryptedDataKey
    extends ActionWithResult<
      Types.EncryptedDataKey,
      Materials.SealedDecryptionMaterials,
      Types.Error>
  {
    const materials: Materials.DecryptionMaterialsPendingPlaintextDataKey
    const client: KMS.IKMSClient
    const awsKmsKey: AwsArnParsing.AwsKmsIdentifierString
    const paddingScheme: KMS.EncryptionAlgorithmSpec
    const encryptionContextDigest: seq<uint8>
    const grantTokens: KMS.GrantTokenList

    constructor(
      materials: Materials.DecryptionMaterialsPendingPlaintextDataKey,
      client: KMS.IKMSClient,
      awsKmsKey: AwsArnParsing.AwsKmsIdentifierString,
      paddingScheme: KMS.EncryptionAlgorithmSpec,
      encryptionContextDigest: seq<uint8>,
      grantTokens: KMS.GrantTokenList
    )
      requires client.ValidState()
      ensures
        && this.materials == materials
        && this.client == client
        && this.awsKmsKey == awsKmsKey
        && this.paddingScheme == paddingScheme
        && this.encryptionContextDigest == encryptionContextDigest
        && this.grantTokens == grantTokens
      ensures Invariant()
    {
      this.materials := materials;
      this.client := client;
      this.awsKmsKey := awsKmsKey;
      this.paddingScheme := paddingScheme;
      this.encryptionContextDigest := encryptionContextDigest;
      this.grantTokens := grantTokens;
      Modifies := client.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && client.ValidState()
      && client.Modifies == Modifies
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
        && var maybeWrappedMaterial :=
             EdkWrapping.GetProviderWrappedMaterial(edk.ciphertext, materials.algorithmSuite);
        && maybeWrappedMaterial.Success?
        && KMS.IsValid_CiphertextType(maybeWrappedMaterial.value)
        && Materials.DecryptionMaterialsTransitionIsValid(materials, res.value)
        && 0 < |client.History.Decrypt|
        && KMS.DecryptRequest(
             KeyId := Some(awsKmsKey),
             CiphertextBlob := maybeWrappedMaterial.value,
             EncryptionContext := None,
             GrantTokens := Some(grantTokens),
             EncryptionAlgorithm := Some(paddingScheme)
           ) == Seq.Last(client.History.Decrypt).input
        && Seq.Last(client.History.Decrypt).output.Success?
        && Seq.Last(client.History.Decrypt).output.value.Plaintext.Some?
        && (
             materials.algorithmSuite.edkWrapping.DIRECT_KEY_WRAPPING? ==>
               Seq.Last(client.History.Decrypt).output.value.Plaintext.value
               == encryptionContextDigest + res.value.plaintextDataKey.value)
        && Seq.Last(client.History.Decrypt).output.value.KeyId == Some(awsKmsKey)
    }

    predicate Requires(edk: Types.EncryptedDataKey){
      true
    }

    method Invoke(
      edk: Types.EncryptedDataKey,
      ghost attemptsState: seq<ActionInvoke<Types.EncryptedDataKey, Result<Materials.SealedDecryptionMaterials, Types.Error>>>
    ) returns (res: Result<Materials.SealedDecryptionMaterials, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(edk, res, attemptsState)
    {
      var unwrap := new KmsRsaUnwrapKeyMaterial(
        client,
        awsKmsKey,
        paddingScheme,
        encryptionContextDigest,
        grantTokens
      );
      var unwrapOutput :- EdkWrapping.UnwrapEdkMaterial(
        edk.ciphertext,
        materials,
        unwrap
      );

      var result :- Materials.DecryptionMaterialsAddDataKey(materials, unwrapOutput.plaintextDataKey, unwrapOutput.symmetricSigningKey);
      return Success(result);
    }
  }

  datatype KmsRsaUnwrapInfo = KmsRsaUnwrapInfo()

  datatype KmsRsaWrapInfo = KmsRsaWrapInfo()

  class KmsRsaGenerateAndWrapKeyMaterial
    extends MaterialWrapping.GenerateAndWrapMaterial<KmsRsaWrapInfo>
  {
    const publicKey: seq<uint8>
    const paddingScheme: KMS.EncryptionAlgorithmSpec
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      publicKey: seq<uint8>,
      paddingScheme: KMS.EncryptionAlgorithmSpec,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires cryptoPrimitives.ValidState()
      requires (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
      ensures
        && this.publicKey == publicKey
        && this.cryptoPrimitives == cryptoPrimitives
        && this.paddingScheme == paddingScheme
      ensures Invariant()
    {
      this.publicKey := publicKey;
      this.cryptoPrimitives := cryptoPrimitives;
      this.paddingScheme := paddingScheme;
      Modifies := cryptoPrimitives.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && cryptoPrimitives.ValidState()
      && Modifies == cryptoPrimitives.Modifies
      && (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
    }

    predicate Ensures(
      input: MaterialWrapping.GenerateAndWrapInput,
      res: Result<MaterialWrapping.GenerateAndWrapOutput<KmsRsaWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<KmsRsaWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {true}

    method Invoke(
      input: MaterialWrapping.GenerateAndWrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<KmsRsaWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.GenerateAndWrapOutput<KmsRsaWrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==> |res.value.plaintextMaterial| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat
    {
      var generateBytesResult := cryptoPrimitives
      .GenerateRandomBytes(Crypto.GenerateRandomBytesInput(length := AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite)));
      var plaintextMaterial :- generateBytesResult.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      var wrap := new KmsRsaWrapKeyMaterial(
        publicKey,
        paddingScheme,
        cryptoPrimitives
      );
      var wrapOutput: MaterialWrapping.WrapOutput<KmsRsaWrapInfo> :- wrap.Invoke(
        MaterialWrapping.WrapInput(
          plaintextMaterial := plaintextMaterial,
          algorithmSuite := input.algorithmSuite,
          encryptionContext := input.encryptionContext,
          serializedEC := input.serializedEC
        ), []);

      var output := MaterialWrapping.GenerateAndWrapOutput(
        plaintextMaterial := plaintextMaterial,
        wrappedMaterial := wrapOutput.wrappedMaterial,
        wrapInfo := KmsRsaWrapInfo()
      );

      return Success(output);
    }
  }

  class KmsRsaWrapKeyMaterial
    extends MaterialWrapping.WrapMaterial<KmsRsaWrapInfo>
  {
    const publicKey: seq<uint8>
    const paddingScheme: KMS.EncryptionAlgorithmSpec
    const cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      publicKey: seq<uint8>,
      paddingScheme: KMS.EncryptionAlgorithmSpec,
      cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires cryptoPrimitives.ValidState()
      requires (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
      ensures
        && this.publicKey == publicKey
        && this.cryptoPrimitives == cryptoPrimitives
        && this.paddingScheme == paddingScheme
      ensures Invariant()
    {
      this.publicKey := publicKey;
      this.cryptoPrimitives := cryptoPrimitives;
      this.paddingScheme := paddingScheme;
      Modifies := cryptoPrimitives.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && cryptoPrimitives.ValidState()
      && Modifies == cryptoPrimitives.Modifies
      && (paddingScheme.RSAES_OAEP_SHA_1? || paddingScheme.RSAES_OAEP_SHA_256?)
    }

    predicate Ensures(
      input: MaterialWrapping.WrapInput,
      res: Result<MaterialWrapping.WrapOutput<KmsRsaWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<KmsRsaWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {true}

    method Invoke(
      input: MaterialWrapping.WrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<KmsRsaWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.WrapOutput<KmsRsaWrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
    {
      var encryptionContextDigest :- EncryptionContextDigest(cryptoPrimitives, input.encryptionContext);
      var padding := match paddingScheme
        case RSAES_OAEP_SHA_1() => Crypto.OAEP_SHA1
        case RSAES_OAEP_SHA_256() => Crypto.OAEP_SHA256;

      var RSAEncryptOutput := cryptoPrimitives.RSAEncrypt(
        Crypto.RSAEncryptInput(
          padding := padding,
          publicKey := publicKey,
          plaintext := encryptionContextDigest + input.plaintextMaterial
        )
      );

      var ciphertext :- RSAEncryptOutput.MapFailure(e => Types.AwsCryptographyPrimitives(e));

      var output := MaterialWrapping.WrapOutput(
        wrappedMaterial := ciphertext,
        wrapInfo := KmsRsaWrapInfo()
      );

      return Success(output);
    }
  }

  class KmsRsaUnwrapKeyMaterial
    extends MaterialWrapping.UnwrapMaterial<KmsRsaUnwrapInfo>
  {
    const client: KMS.IKMSClient
    const awsKmsKey: AwsArnParsing.AwsKmsIdentifierString
    const paddingScheme: KMS.EncryptionAlgorithmSpec
    const encryptionContextDigest: seq<uint8>
    const grantTokens: KMS.GrantTokenList

    constructor(
      client: KMS.IKMSClient,
      awsKmsKey: AwsArnParsing.AwsKmsIdentifierString,
      paddingScheme: KMS.EncryptionAlgorithmSpec,
      encryptionContextDigest: seq<uint8>,
      grantTokens: KMS.GrantTokenList
    )
      requires client.ValidState()
      ensures
        && this.client == client
        && this.awsKmsKey == awsKmsKey
        && this.paddingScheme == paddingScheme
        && this.encryptionContextDigest == encryptionContextDigest
        && this.grantTokens == grantTokens
      ensures Invariant()
    {
      this.client := client;
      this.awsKmsKey := awsKmsKey;
      this.paddingScheme := paddingScheme;
      this.encryptionContextDigest := encryptionContextDigest;
      this.grantTokens := grantTokens;
      Modifies := client.Modifies;
    }

    predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && client.ValidState()
      && client.Modifies == Modifies
    }

    predicate Ensures(
      input: MaterialWrapping.UnwrapInput,
      res: Result<MaterialWrapping.UnwrapOutput<KmsRsaUnwrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<KmsRsaUnwrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
        && KMS.IsValid_CiphertextType(input.wrappedMaterial)
        && 0 < |client.History.Decrypt|
        && KMS.DecryptRequest(
             KeyId := Some(awsKmsKey),
             CiphertextBlob := input.wrappedMaterial,
             EncryptionContext := None,
             GrantTokens := Some(grantTokens),
             EncryptionAlgorithm := Some(paddingScheme)
           ) == Seq.Last(client.History.Decrypt).input
        && Seq.Last(client.History.Decrypt).output.Success?
        && Seq.Last(client.History.Decrypt).output.value.Plaintext.Some?
        && Seq.Last(client.History.Decrypt).output.value.Plaintext.value
           == encryptionContextDigest + res.value.unwrappedMaterial
        && Seq.Last(client.History.Decrypt).output.value.KeyId == Some(awsKmsKey)
    }

    method Invoke(
      input: MaterialWrapping.UnwrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<KmsRsaUnwrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.UnwrapOutput<KmsRsaUnwrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==> |res.value.unwrappedMaterial| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat
    {
      :- Need(KMS.IsValid_CiphertextType(input.wrappedMaterial),
              Types.AwsCryptographicMaterialProvidersException(message := "Ciphertext length invalid"));

      var decryptRequest := KMS.DecryptRequest(
        KeyId := Some(awsKmsKey),
        CiphertextBlob := input.wrappedMaterial,
        // Asymmetric keys do not support Encryption Context.
        // This is checked by verifying the encryption context digest.
        EncryptionContext := None,
        GrantTokens := Some(grantTokens),
        EncryptionAlgorithm := Some(paddingScheme)
      );

      var maybeDecryptResponse := client.Decrypt(decryptRequest);
      var decryptResponse :- maybeDecryptResponse
      .MapFailure(e => Types.ComAmazonawsKms( ComAmazonawsKms := e ));

      :- Need(
        && decryptResponse.KeyId.Some?
        && decryptResponse.KeyId.value == awsKmsKey
        && decryptResponse.Plaintext.Some?
      , Types.AwsCryptographicMaterialProvidersException(
          message := "Invalid response from KMS Decrypt"));

      OptionalSequenceIsSafeBecauseItIsInMemory(decryptResponse.Plaintext);
      SequenceIsSafeBecauseItIsInMemory(encryptionContextDigest);
      :- Need(
        && encryptionContextDigest <= decryptResponse.Plaintext.value
        && AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as uint64 + |encryptionContextDigest| as uint64 == |decryptResponse.Plaintext.value| as uint64
      , Types.AwsCryptographicMaterialProvidersException(
          message := "Encryption context digest does not match expected value."));

      var output := MaterialWrapping.UnwrapOutput(
        unwrappedMaterial := decryptResponse.Plaintext.value[|encryptionContextDigest| as uint64..],
        unwrapInfo := KmsRsaUnwrapInfo());

      return Success(output);
    }
  }
}
