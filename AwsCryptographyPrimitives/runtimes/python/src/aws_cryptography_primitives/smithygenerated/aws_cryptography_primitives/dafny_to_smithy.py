# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    DigestAlgorithm_SHA__256,
    DigestAlgorithm_SHA__384,
    DigestAlgorithm_SHA__512,
    ECDHCurveSpec_ECC__NIST__P256,
    ECDHCurveSpec_ECC__NIST__P384,
    ECDHCurveSpec_ECC__NIST__P521,
    ECDHCurveSpec_SM2,
    ECDSASignatureAlgorithm_ECDSA__P256,
    ECDSASignatureAlgorithm_ECDSA__P384,
    RSAPaddingMode_OAEP__SHA1,
    RSAPaddingMode_OAEP__SHA256,
    RSAPaddingMode_OAEP__SHA384,
    RSAPaddingMode_OAEP__SHA512,
    RSAPaddingMode_PKCS1,
)
import aws_cryptography_primitives.internaldafny.generated.module_
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models


def aws_cryptography_primitives_GenerateRandomBytesInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateRandomBytesInput(
        length=dafny_input.length,
    )


def aws_cryptography_primitives_DigestAlgorithm(dafny_input):
    if isinstance(dafny_input, DigestAlgorithm_SHA__512):
        return "SHA_512"

    elif isinstance(dafny_input, DigestAlgorithm_SHA__384):
        return "SHA_384"

    elif isinstance(dafny_input, DigestAlgorithm_SHA__256):
        return "SHA_256"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_primitives_DigestInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.DigestInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        message=bytes(dafny_input.message),
    )


def aws_cryptography_primitives_HMacInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.HMacInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        key=bytes(dafny_input.key),
        message=bytes(dafny_input.message),
    )


def aws_cryptography_primitives_HkdfExtractInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.HkdfExtractInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        salt=(bytes(dafny_input.salt.value)) if (dafny_input.salt.is_Some) else None,
        ikm=bytes(dafny_input.ikm),
    )


def aws_cryptography_primitives_HkdfExpandInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.HkdfExpandInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        prk=bytes(dafny_input.prk),
        info=bytes(dafny_input.info),
        expected_length=dafny_input.expectedLength,
    )


def aws_cryptography_primitives_HkdfInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.HkdfInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        salt=(bytes(dafny_input.salt.value)) if (dafny_input.salt.is_Some) else None,
        ikm=bytes(dafny_input.ikm),
        info=bytes(dafny_input.info),
        expected_length=dafny_input.expectedLength,
    )


def aws_cryptography_primitives_KdfCtrInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.KdfCtrInput(
        digest_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestAlgorithm(
            dafny_input.digestAlgorithm
        ),
        ikm=bytes(dafny_input.ikm),
        expected_length=dafny_input.expectedLength,
        purpose=(
            (bytes(dafny_input.purpose.value))
            if (dafny_input.purpose.is_Some)
            else None
        ),
        nonce=(bytes(dafny_input.nonce.value)) if (dafny_input.nonce.is_Some) else None,
    )


def aws_cryptography_primitives_AesKdfCtrInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.AesKdfCtrInput(
        ikm=bytes(dafny_input.ikm),
        expected_length=dafny_input.expectedLength,
        nonce=(bytes(dafny_input.nonce.value)) if (dafny_input.nonce.is_Some) else None,
    )


def aws_cryptography_primitives_AES_GCM(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.AES_GCM(
        key_length=dafny_input.keyLength,
        tag_length=dafny_input.tagLength,
        iv_length=dafny_input.ivLength,
    )


def aws_cryptography_primitives_AESEncryptInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.AESEncryptInput(
        enc_alg=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AES_GCM(
            dafny_input.encAlg
        ),
        iv=bytes(dafny_input.iv),
        key=bytes(dafny_input.key),
        msg=bytes(dafny_input.msg),
        aad=bytes(dafny_input.aad),
    )


def aws_cryptography_primitives_AESDecryptInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.AESDecryptInput(
        enc_alg=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AES_GCM(
            dafny_input.encAlg
        ),
        key=bytes(dafny_input.key),
        cipher_txt=bytes(dafny_input.cipherTxt),
        auth_tag=bytes(dafny_input.authTag),
        iv=bytes(dafny_input.iv),
        aad=bytes(dafny_input.aad),
    )


def aws_cryptography_primitives_GenerateRSAKeyPairInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateRSAKeyPairInput(
        length_bits=dafny_input.lengthBits,
    )


def aws_cryptography_primitives_GetRSAKeyModulusLengthInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GetRSAKeyModulusLengthInput(
        public_key=bytes(dafny_input.publicKey),
    )


def aws_cryptography_primitives_RSAPaddingMode(dafny_input):
    if isinstance(dafny_input, RSAPaddingMode_PKCS1):
        return "PKCS1"

    elif isinstance(dafny_input, RSAPaddingMode_OAEP__SHA1):
        return "OAEP_SHA1"

    elif isinstance(dafny_input, RSAPaddingMode_OAEP__SHA256):
        return "OAEP_SHA256"

    elif isinstance(dafny_input, RSAPaddingMode_OAEP__SHA384):
        return "OAEP_SHA384"

    elif isinstance(dafny_input, RSAPaddingMode_OAEP__SHA512):
        return "OAEP_SHA512"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_primitives_RSADecryptInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.RSADecryptInput(
        padding=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAPaddingMode(
            dafny_input.padding
        ),
        private_key=bytes(dafny_input.privateKey),
        cipher_text=bytes(dafny_input.cipherText),
    )


def aws_cryptography_primitives_RSAEncryptInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.RSAEncryptInput(
        padding=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAPaddingMode(
            dafny_input.padding
        ),
        public_key=bytes(dafny_input.publicKey),
        plaintext=bytes(dafny_input.plaintext),
    )


def aws_cryptography_primitives_ECDSASignatureAlgorithm(dafny_input):
    if isinstance(dafny_input, ECDSASignatureAlgorithm_ECDSA__P384):
        return "ECDSA_P384"

    elif isinstance(dafny_input, ECDSASignatureAlgorithm_ECDSA__P256):
        return "ECDSA_P256"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_primitives_GenerateECDSASignatureKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateECDSASignatureKeyInput(
        signature_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            dafny_input.signatureAlgorithm
        ),
    )


def aws_cryptography_primitives_ECDSASignInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ECDSASignInput(
        signature_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            dafny_input.signatureAlgorithm
        ),
        signing_key=bytes(dafny_input.signingKey),
        message=bytes(dafny_input.message),
    )


def aws_cryptography_primitives_ECDSAVerifyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ECDSAVerifyInput(
        signature_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            dafny_input.signatureAlgorithm
        ),
        verification_key=bytes(dafny_input.verificationKey),
        message=bytes(dafny_input.message),
        signature=bytes(dafny_input.signature),
    )


def aws_cryptography_primitives_ECDHCurveSpec(dafny_input):
    if isinstance(dafny_input, ECDHCurveSpec_ECC__NIST__P256):
        return "ECC_NIST_P256"

    elif isinstance(dafny_input, ECDHCurveSpec_ECC__NIST__P384):
        return "ECC_NIST_P384"

    elif isinstance(dafny_input, ECDHCurveSpec_ECC__NIST__P521):
        return "ECC_NIST_P521"

    elif isinstance(dafny_input, ECDHCurveSpec_SM2):
        return "SM2"

    else:
        raise ValueError(f"No recognized enum value in enum type: {dafny_input=}")


def aws_cryptography_primitives_GenerateECCKeyPairInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateECCKeyPairInput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
    )


def aws_cryptography_primitives_ECCPrivateKey(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ECCPrivateKey(
        pem=bytes(dafny_input.pem),
    )


def aws_cryptography_primitives_GetPublicKeyFromPrivateKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GetPublicKeyFromPrivateKeyInput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
        private_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPrivateKey(
            dafny_input.privateKey
        ),
    )


def aws_cryptography_primitives_ValidatePublicKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ValidatePublicKeyInput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
        public_key=bytes(dafny_input.publicKey),
    )


def aws_cryptography_primitives_ECCPublicKey(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ECCPublicKey(
        der=bytes(dafny_input.der),
    )


def aws_cryptography_primitives_DeriveSharedSecretInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.DeriveSharedSecretInput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
        private_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPrivateKey(
            dafny_input.privateKey
        ),
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPublicKey(
            dafny_input.publicKey
        ),
    )


def aws_cryptography_primitives_CompressPublicKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.CompressPublicKeyInput(
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPublicKey(
            dafny_input.publicKey
        ),
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
    )


def aws_cryptography_primitives_DecompressPublicKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.DecompressPublicKeyInput(
        compressed_public_key=bytes(dafny_input.compressedPublicKey),
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
    )


def aws_cryptography_primitives_ParsePublicKeyInput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ParsePublicKeyInput(
        public_key=bytes(dafny_input.publicKey),
    )


def aws_cryptography_primitives_GenerateRandomBytesOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_DigestOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_HMacOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_HkdfExtractOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_HkdfExpandOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_HkdfOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_KdfCtrOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_AesKdfCtrOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_AESEncryptOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.AESEncryptOutput(
        cipher_text=bytes(dafny_input.cipherText),
        auth_tag=bytes(dafny_input.authTag),
    )


def aws_cryptography_primitives_AESDecryptOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_RSAPublicKey(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.RSAPublicKey(
        length_bits=dafny_input.lengthBits,
        pem=bytes(dafny_input.pem),
    )


def aws_cryptography_primitives_RSAPrivateKey(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.RSAPrivateKey(
        length_bits=dafny_input.lengthBits,
        pem=bytes(dafny_input.pem),
    )


def aws_cryptography_primitives_GenerateRSAKeyPairOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateRSAKeyPairOutput(
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAPublicKey(
            dafny_input.publicKey
        ),
        private_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAPrivateKey(
            dafny_input.privateKey
        ),
    )


def aws_cryptography_primitives_GetRSAKeyModulusLengthOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GetRSAKeyModulusLengthOutput(
        length=dafny_input.length,
    )


def aws_cryptography_primitives_RSADecryptOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_RSAEncryptOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_GenerateECDSASignatureKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateECDSASignatureKeyOutput(
        signature_algorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            dafny_input.signatureAlgorithm
        ),
        verification_key=bytes(dafny_input.verificationKey),
        signing_key=bytes(dafny_input.signingKey),
    )


def aws_cryptography_primitives_ECDSASignOutput(dafny_input):
    return bytes(dafny_input)


def aws_cryptography_primitives_ECDSAVerifyOutput(dafny_input):
    return dafny_input


def aws_cryptography_primitives_GenerateECCKeyPairOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GenerateECCKeyPairOutput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
        private_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPrivateKey(
            dafny_input.privateKey
        ),
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPublicKey(
            dafny_input.publicKey
        ),
    )


def aws_cryptography_primitives_GetPublicKeyFromPrivateKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.GetPublicKeyFromPrivateKeyOutput(
        ecc_curve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDHCurveSpec(
            dafny_input.eccCurve
        ),
        private_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPrivateKey(
            dafny_input.privateKey
        ),
        public_key=bytes(dafny_input.publicKey),
    )


def aws_cryptography_primitives_ValidatePublicKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ValidatePublicKeyOutput(
        success=dafny_input.success,
    )


def aws_cryptography_primitives_DeriveSharedSecretOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.DeriveSharedSecretOutput(
        shared_secret=bytes(dafny_input.sharedSecret),
    )


def aws_cryptography_primitives_CompressPublicKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.CompressPublicKeyOutput(
        compressed_public_key=bytes(dafny_input.compressedPublicKey),
    )


def aws_cryptography_primitives_DecompressPublicKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.DecompressPublicKeyOutput(
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPublicKey(
            dafny_input.publicKey
        ),
    )


def aws_cryptography_primitives_ParsePublicKeyOutput(dafny_input):
    return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.models.ParsePublicKeyOutput(
        public_key=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECCPublicKey(
            dafny_input.publicKey
        ),
    )


def aws_cryptography_primitives_CryptoConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.config

    return (
        aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.config.CryptoConfig()
    )
