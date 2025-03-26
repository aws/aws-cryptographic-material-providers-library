// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Materials.dfy"
include "MaterialWrapping.dfy"
include "IntermediateKeyWrapping.dfy"
include "../Keyrings/AwsKms/Constants.dfy"

// Helpers for implementing EDK wrapping for the ECDH Keyrings
module {:options "/functionSyntax:4" } EcdhEdkWrapping {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened Actions
  import opened Wrappers
  import opened MaterialWrapping
  import opened IntermediateKeyWrapping
  import opened Constants
  import opened Seq
  import opened AlgorithmSuites
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import Types = AwsCryptographyMaterialProvidersTypes
  import AtomicPrimitives
  import Materials

  datatype EcdhUnwrapInfo = EcdhUnwrapInfo()
  datatype EcdhWrapInfo = EcdhWrapInfo()

  class EcdhUnwrap
    extends MaterialWrapping.UnwrapMaterial<EcdhUnwrapInfo>
  {
    const senderPublicKey: seq<uint8>
    const recipientPublicKey: seq<uint8>
    const sharedSecret: seq<uint8>
    const keyringVersion: seq<uint8>
    const curveSpec: PrimitiveTypes.ECDHCurveSpec
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      senderPublicKey: seq<uint8>,
      recipientPublicKey: seq<uint8>,
      sharedSecret: seq<uint8>,
      keyringVersion: seq<uint8>,
      curveSpec: PrimitiveTypes.ECDHCurveSpec,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.senderPublicKey == senderPublicKey
        && this.recipientPublicKey == recipientPublicKey
        && this.sharedSecret == sharedSecret
        && this.keyringVersion == keyringVersion
        && this.curveSpec == curveSpec
        && this.crypto == crypto
      ensures Invariant()
    {
      this.senderPublicKey := senderPublicKey;
      this.recipientPublicKey := recipientPublicKey;
      this.sharedSecret := sharedSecret;
      this.keyringVersion := keyringVersion;
      this.curveSpec := curveSpec;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    ghost predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    ghost predicate Ensures(
      input: MaterialWrapping.UnwrapInput,
      res: Result<MaterialWrapping.UnwrapOutput<EcdhUnwrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<EcdhUnwrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
    }

    method {:vcs_split_on_every_assert} Invoke(
      input: MaterialWrapping.UnwrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.UnwrapInput, Result<MaterialWrapping.UnwrapOutput<EcdhUnwrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.UnwrapOutput<EcdhUnwrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==>
                |res.value.unwrappedMaterial| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //= type=implication
      //# If the keyring cannot
      //# serialize the encryption context, OnDecrypt MUST fail.
      ensures CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext).Failure? ==> res.Failure?
    {
      var suite := input.algorithmSuite;
      var wrappedMaterial := input.wrappedMaterial;
      var aad := input.encryptionContext;

      :- Need(
        |wrappedMaterial| > CIPHERTEXT_WRAPPED_MATERIAL_INDEX,
        E("Recieved ciphertext is shorter than expected.")
      );

      var KeyLength := AlgorithmSuites.GetEncryptKeyLength(suite) as int;

      :- Need (
        |wrappedMaterial| > ECDH_WRAPPED_KEY_MATERIAL_INDEX + KeyLength,
        Types.AwsCryptographicMaterialProvidersException(message := "Received EDK Ciphertext of incorrect length.")
      );

      var kdfNonce := wrappedMaterial[0..ECDH_COMMITMENT_KEY_INDEX];
      var iv := seq(ECDH_AES_256_ENC_ALG.ivLength as nat, _ => 0); // IV is zero
      var commitmentKey := wrappedMaterial[ECDH_COMMITMENT_KEY_INDEX..ECDH_WRAPPED_KEY_MATERIAL_INDEX];
      var wrappedKey := wrappedMaterial[ECDH_WRAPPED_KEY_MATERIAL_INDEX..ECDH_WRAPPED_KEY_MATERIAL_INDEX+KeyLength];
      var authTag := wrappedMaterial[ECDH_WRAPPED_KEY_MATERIAL_INDEX+KeyLength..];

      var curveSpecUtf8 :- UTF8.Encode(
        CurveSpecTypeToString(this.curveSpec)
      ).MapFailure(E);
      var canonicalizedEC :- CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext);

      var fixedInfo := SerializeFixedInfo(
        ECDH_KDF_UTF8,
        curveSpecUtf8,
        senderPublicKey,
        recipientPublicKey,
        canonicalizedEC,
        keyringVersion
      );


      var derivedKeyingMaterial :- DeriveSharedKeyingMaterial(
        this.sharedSecret,
        fixedInfo,
        kdfNonce,
        crypto
      );

      var calculatedCommitmentKey: seq<uint8> := derivedKeyingMaterial[0..32];
      var sharedKeyingMaterial: seq<uint8> := derivedKeyingMaterial[32..];

      :- Need(
        |calculatedCommitmentKey| == |commitmentKey|,
        E("Calculated commitment key length does NOT match expected commitment key length")
      );

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#ondecrypt
      //# The keyring MUST check that the calculated Commitment Key
      //# from the key derivation step is equal to the deserialized commitment key
      //# found in the encrypted data key.
      var check?, _ := commitmentKeyCheck(calculatedCommitmentKey, commitmentKey);
      :- Need(
        check?,
        E("Commitment keys do not match")
      );

      var maybeUnwrappedPdk :=  crypto.AESDecrypt(
        PrimitiveTypes.AESDecryptInput(
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# The keyring MUST decrypt the encrypted data key with the shared wrapping key using `AES-GCM-256` with the following inputs:
          encAlg := ECDH_AES_256_ENC_ALG,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# - It MUST use the shared wrapping key as the AES-GCM cipher key.
          key := sharedKeyingMaterial,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# - It MUST use the `encrypted key` obtained from deserialization as the AES-GCM input ciphertext.
          cipherTxt := wrappedKey,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# - It MUST use the `authentication tag` obtained from deserialization as the AES-GCM input authentication tag.
          authTag := authTag,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# - It MUST use a zeroed out 12 byte IV
          iv := iv,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-unwrapping
          //# - MUST use the serialized [AAD](#branch-key-wrapping-and-unwrapping-aad) concatenated
          //#   with the `FixedInfo` used as part of the key derivation step concatenated with the keyring version found
          //#   in the key provider information.
          aad := fixedInfo
        )
      );
      var unwrappedPdk :- maybeUnwrappedPdk.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      :- Need(
        |unwrappedPdk| == AlgorithmSuites.GetEncryptKeyLength(input.algorithmSuite) as nat,
        E("Invalid Key Length")
      );

      var output := MaterialWrapping.UnwrapOutput(
        unwrappedMaterial := unwrappedPdk,
        unwrapInfo := EcdhUnwrapInfo()
      );

      return Success(output);
    }

    method commitmentKeyCheck(
      calculatedCommitmentKey: seq<uint8>, serializedCommitmentKey: seq<uint8>
    ) returns (res: bool, ghost collectedCommitmentKey: seq<bv8>)
      requires |calculatedCommitmentKey| == |serializedCommitmentKey|
      ensures |collectedCommitmentKey| == |serializedCommitmentKey|
      ensures forall j | 0 <= j < |collectedCommitmentKey| :: collectedCommitmentKey[j] == calculatedCommitmentKey[j] as bv8 ^ serializedCommitmentKey[j] as bv8
    {
      collectedCommitmentKey := [];
      var diff? := 0;
      for i := 0 to |serializedCommitmentKey|
        invariant |collectedCommitmentKey| == i
        invariant forall j | 0 <= j < i :: collectedCommitmentKey[j] == calculatedCommitmentKey[j] as bv8 ^ serializedCommitmentKey[j] as bv8
      {
        diff? := diff? | (calculatedCommitmentKey[i] as bv8 ^ serializedCommitmentKey[i] as bv8);
        collectedCommitmentKey := collectedCommitmentKey + [calculatedCommitmentKey[i] as bv8 ^ serializedCommitmentKey[i] as bv8];
      }

      res := diff? == 0;
    }
  }

  class EcdhGenerateAndWrapKeyMaterial
    extends MaterialWrapping.GenerateAndWrapMaterial<EcdhWrapInfo>
  {
    const sharedSecret: seq<uint8>
    const fixedInfo: seq<uint8>
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      sharedSecret: seq<uint8>,
      fixedInfo: seq<uint8>,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.sharedSecret == sharedSecret
        && this.fixedInfo == fixedInfo
        && this.crypto == crypto
      ensures Invariant()
    {
      this.sharedSecret := sharedSecret;
      this.fixedInfo := fixedInfo;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    ghost predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    ghost predicate Ensures(
      input: MaterialWrapping.GenerateAndWrapInput,
      res: Result<MaterialWrapping.GenerateAndWrapOutput<EcdhWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<EcdhWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
    }

    method {:vcs_split_on_every_assert} Invoke(
      input: MaterialWrapping.GenerateAndWrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.GenerateAndWrapInput, Result<MaterialWrapping.GenerateAndWrapOutput<EcdhWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.GenerateAndWrapOutput<EcdhWrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
      ensures res.Success? ==> |res.value.plaintextMaterial| == input.algorithmSuite.encrypt.AES_GCM.keyLength as nat
    {
      var suite := input.algorithmSuite;
      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
      //= type=implication
      //# If the [encryption materials](structures.md#encryption-materials) do not contain a plaintext data key,
      //# OnEncrypt MUST generate a random plaintext data key.
      var pdkResult := crypto
      .GenerateRandomBytes(PrimitiveTypes.GenerateRandomBytesInput(length := GetEncryptKeyLength(suite)));
      var pdk :- pdkResult.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      var wrap := new EcdhWrapKeyMaterial(
        sharedSecret,
        fixedInfo,
        crypto
      );

      var wrapOutput: MaterialWrapping.WrapOutput<EcdhWrapInfo> :- wrap.Invoke(
        MaterialWrapping.WrapInput(
          plaintextMaterial := pdk,
          algorithmSuite := input.algorithmSuite,
          encryptionContext := input.encryptionContext
        ), []);

      var output := MaterialWrapping.GenerateAndWrapOutput(
        plaintextMaterial := pdk,
        wrappedMaterial := wrapOutput.wrappedMaterial,
        wrapInfo := wrapOutput.wrapInfo
      );
      return Success(output);
    }
  }

  class EcdhWrapKeyMaterial
    extends MaterialWrapping.WrapMaterial<EcdhWrapInfo>
  {
    const sharedSecret: seq<uint8>
    const fixedInfo: seq<uint8>
    const crypto: AtomicPrimitives.AtomicPrimitivesClient

    constructor(
      sharedSecret: seq<uint8>,
      fixedInfo: seq<uint8>,
      crypto: AtomicPrimitives.AtomicPrimitivesClient
    )
      requires crypto.ValidState()
      ensures
        && this.sharedSecret == sharedSecret
        && this.fixedInfo == fixedInfo
        && this.crypto == crypto
      ensures Invariant()
    {
      this.sharedSecret := sharedSecret;
      this.fixedInfo := fixedInfo;
      this.crypto := crypto;
      Modifies := crypto.Modifies;
    }

    ghost predicate Invariant()
      reads Modifies
      decreases Modifies
    {
      && crypto.ValidState()
      && crypto.Modifies == Modifies
    }

    ghost predicate Ensures(
      input: MaterialWrapping.WrapInput,
      res: Result<MaterialWrapping.WrapOutput<EcdhWrapInfo>, Types.Error>,
      attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<EcdhWrapInfo>, Types.Error>>>
    )
      reads Modifies
      decreases Modifies
    {
      res.Success?
      ==>
        && Invariant()
        && 0 < |crypto.History.AESEncrypt|
           //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
           //= type=implication
           //# The keyring MUST encrypt the plaintext data key
           //# using AES-GCM and use the shared wrapping key as the wrapping key.
        && Seq.Last(crypto.History.AESEncrypt).output.Success?
        && var AESEncryptInput := Seq.Last(crypto.History.AESEncrypt).input;
        && var AESEncryptOutput := Seq.Last(crypto.History.AESEncrypt).output.value;
        && var iv := seq(ECDH_AES_256_ENC_ALG.ivLength as nat, _ => 0);
        && AESEncryptInput.encAlg == ECDH_AES_256_ENC_ALG
        && AESEncryptInput.msg == input.plaintextMaterial
           //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
           //= type=implication
           //# - It MUST use a zeroed out 12 byte IV
        && AESEncryptInput.iv == iv
           //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
           //= type=implication
           // - It MUST use the serialized [encryption context](structures.md#encryption-context-1) as the additional authenticated data (AAD).
        && AESEncryptInput.aad == fixedInfo
        && |res.value.wrappedMaterial| > |AESEncryptOutput.cipherText| + |AESEncryptOutput.authTag|
    }

    method {:vcs_split_on_every_assert} Invoke(
      input: MaterialWrapping.WrapInput,
      ghost attemptsState: seq<ActionInvoke<MaterialWrapping.WrapInput, Result<MaterialWrapping.WrapOutput<EcdhWrapInfo>, Types.Error>>>
    ) returns (res: Result<MaterialWrapping.WrapOutput<EcdhWrapInfo>, Types.Error>)
      requires Invariant()
      modifies Modifies
      decreases Modifies
      ensures Invariant()
      ensures Ensures(input, res, attemptsState)
    {
      var suite := input.algorithmSuite;
      var canonicalizedEC :- CanonicalEncryptionContext.EncryptionContextToAAD(input.encryptionContext);
      //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
      //# Before deriving a shared wrapping key, the keyring MUST generate a 32 byte random salt value.
      var maybeSalt := crypto.GenerateRandomBytes(
        PrimitiveTypes.GenerateRandomBytesInput(length := KDF_SALT_LEN)
      );

      //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
      //# If the keyring fails to generate a random value, the operation MUST fail.
      var salt :- maybeSalt.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#onencrypt
      //# The keyring MUST derive a data key according to the construction
      //# #outlined by the [key agreement schemas](./key-agreement-schemas.md#key-derivation)
      // (blank line for duvet)
      //# #If the Key Derivation step fails, the keyring MUST fail.
      var derivedKeyingMaterial :- DeriveSharedKeyingMaterial(
        sharedSecret,
        fixedInfo,
        salt,
        crypto
      );

      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //# The keyring MUST use the first 32 bytes as the Commitment Key.
      var commitmentKey: seq<uint8> := derivedKeyingMaterial[0..32];
      //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
      //# The keyring MUST use the last 32 bytes as the Shared Wrapping Key.
      var sharedKeyingMaterial: seq<uint8> := derivedKeyingMaterial[32..];

      var iv := seq(ECDH_AES_256_ENC_ALG.ivLength as nat, _ => 0); // IV is zero

      var maybeWrappedPdk := crypto.AESEncrypt(
        PrimitiveTypes.AESEncryptInput(
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# The keyring MUST encrypt a plaintext data key
          //# using `AES-GCM-256` with the following inputs:
          encAlg := ECDH_AES_256_ENC_ALG,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# - It MUST use a zeroed out 12 byte IV
          iv := iv,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# - MUST use the shared wrapping key as the AES-GCM cipher key.
          key := sharedKeyingMaterial,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# - MUST use the plain text data key that will be wrapped by the shared wrapping key as the AES-GCM message.
          msg := input.plaintextMaterial,
          //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
          //# - MUST use the serialized [AAD](#branch-key-wrapping-and-unwrapping-aad) concatenated
          //#   with the `FixedInfo` used as part of the key derivation step concatenated with the keyring version found
          //#   in the key provider information.
          aad := fixedInfo
        )
      );

      var wrappedPdk :- maybeWrappedPdk.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));

      var output := MaterialWrapping.WrapOutput(
        wrappedMaterial := salt + commitmentKey + wrappedPdk.cipherText + wrappedPdk.authTag,
        wrapInfo := EcdhWrapInfo()
      );
      return Success(output);
    }
  }

  //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
  //= type=implication
  //# The keyring MUST derive a shared wrapping key according to the construction
  //# outlined by the [key agreement schemes](./key-agreement-schemas.md#key-derivation)
  method {:vcs_split_on_every_assert} DeriveSharedKeyingMaterial(
    sharedSecret: seq<uint8>,
    fixedInfo: seq<uint8>,
    salt: seq<uint8>,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (res :Result<seq<uint8>, Types.Error>)
    requires crypto.ValidState()
    modifies crypto.Modifies
    ensures crypto.ValidState()
    ensures |crypto.History.KdfCounterMode| > 0
    ensures Last(crypto.History.KdfCounterMode).input
         == PrimitiveTypes.KdfCtrInput(
              digestAlgorithm := PrimitiveTypes.DigestAlgorithm.SHA_384,
              //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
              //= type=implication
              //# - MUST use the derived shared secret, Z
              ikm := sharedSecret,
              //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
              //= type=implication
              //# - L: MUST be a length of 512 bits
              expectedLength := KDF_EXPECTED_LEN,
              purpose := Some(fixedInfo),
              //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
              //= type=implication
              //# - salt: MUST be a random 32 byte string
              nonce := Some(salt)
            )
    ensures res.Success? ==>
              && Last(crypto.History.KdfCounterMode).output.Success?
                 //= aws-encryption-sdk-specification/framework/aws-kms/aws-kms-ecdh-keyring.md#onencrypt
                 //= type=implication
                 //# If they Key Derivation step succeeds it MUST produce
                 //# keying material with a length of 64 bytes.
              && |Last(crypto.History.KdfCounterMode).output.value| == KDF_EXPECTED_LEN as int
              && |res.value| == |Last(crypto.History.KdfCounterMode).output.value|
  {
    var maybeDerivedKeyingMaterial := crypto.KdfCounterMode(
      PrimitiveTypes.KdfCtrInput(
        digestAlgorithm := PrimitiveTypes.DigestAlgorithm.SHA_384,
        ikm := sharedSecret,
        expectedLength := KDF_EXPECTED_LEN,
        purpose := Some(fixedInfo),
        nonce := Some(salt)
      )
    );
    var derivedKeyingMaterial :- maybeDerivedKeyingMaterial.MapFailure(e => Types.AwsCryptographyPrimitives(AwsCryptographyPrimitives := e));
    res := Success(derivedKeyingMaterial);
  }

  function SerializeFixedInfo(
    ecdhKeyDerivationUtf8: UTF8.ValidUTF8Bytes,
    curveSpecUtf8: UTF8.ValidUTF8Bytes,
    senderPublicKey: seq<uint8>,
    recipientPublicKey: seq<uint8>,
    canonicalizedEC: seq<uint8>,
    keyringVersion: seq<uint8>
  ): (res: seq<uint8>)
    //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
    //= type=implication
    //# The FixedInfo field MUST be serialized in the following order:
    ensures res ==
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST be the UTF8 encoded string "ecdh-key-derivation"
            ecdhKeyDerivationUtf8 +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST use a null byte concatenating all the fixed info fields.
            ECDH_KDF_DELIMETER +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST be the UTF8 encoded string of the configured curve specification
            curveSpecUtf8 +
            ECDH_KDF_DELIMETER +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST be the UTF8 encoded string of the configured Key Derivation Method used
            ECDH_KDF_PRF_NAME +
            ECDH_KDF_DELIMETER +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST be A concatenation of the static public keys used by the parties
            //#  in the format of sender followed by receiver
            senderPublicKey +
            recipientPublicKey +
            ECDH_KDF_DELIMETER +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST use the keyring version found in the key provider information.
            keyringVersion +
            ECDH_KDF_DELIMETER +
            //= aws-encryption-sdk-specification/framework/key-agreement-schemas.md#key-derivation
            //= type=implication
            //# - MUST be The canonicalized encryption context found in the [encryption materials](structures.md#encryption-materials)
            canonicalizedEC
  {
    ecdhKeyDerivationUtf8 +
    ECDH_KDF_DELIMETER +
    curveSpecUtf8 +
    ECDH_KDF_DELIMETER +
    ECDH_KDF_PRF_NAME +
    ECDH_KDF_DELIMETER +
    senderPublicKey +
    recipientPublicKey +
    ECDH_KDF_DELIMETER +
    keyringVersion +
    ECDH_KDF_DELIMETER +
    canonicalizedEC
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
