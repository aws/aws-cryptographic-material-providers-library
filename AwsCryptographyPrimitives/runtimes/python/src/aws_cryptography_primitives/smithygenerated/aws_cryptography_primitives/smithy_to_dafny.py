# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Seq
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    AESDecryptInput_AESDecryptInput as DafnyAESDecryptInput,
    AESEncryptInput_AESEncryptInput as DafnyAESEncryptInput,
    AESEncryptOutput_AESEncryptOutput as DafnyAESEncryptOutput,
    AES__GCM_AES__GCM as DafnyAES_GCM,
    AesKdfCtrInput_AesKdfCtrInput as DafnyAesKdfCtrInput,
    CompressPublicKeyInput_CompressPublicKeyInput as DafnyCompressPublicKeyInput,
    CompressPublicKeyOutput_CompressPublicKeyOutput as DafnyCompressPublicKeyOutput,
    CryptoConfig_CryptoConfig as DafnyCryptoConfig,
    DecompressPublicKeyInput_DecompressPublicKeyInput as DafnyDecompressPublicKeyInput,
    DecompressPublicKeyOutput_DecompressPublicKeyOutput as DafnyDecompressPublicKeyOutput,
    DeriveSharedSecretInput_DeriveSharedSecretInput as DafnyDeriveSharedSecretInput,
    DeriveSharedSecretOutput_DeriveSharedSecretOutput as DafnyDeriveSharedSecretOutput,
    DigestAlgorithm_SHA__256,
    DigestAlgorithm_SHA__384,
    DigestAlgorithm_SHA__512,
    DigestInput_DigestInput as DafnyDigestInput,
    ECCPrivateKey_ECCPrivateKey as DafnyECCPrivateKey,
    ECCPublicKey_ECCPublicKey as DafnyECCPublicKey,
    ECDHCurveSpec_ECC__NIST__P256,
    ECDHCurveSpec_ECC__NIST__P384,
    ECDHCurveSpec_ECC__NIST__P521,
    ECDHCurveSpec_SM2,
    ECDSASignInput_ECDSASignInput as DafnyECDSASignInput,
    ECDSASignatureAlgorithm_ECDSA__P256,
    ECDSASignatureAlgorithm_ECDSA__P384,
    ECDSAVerifyInput_ECDSAVerifyInput as DafnyECDSAVerifyInput,
    GenerateECCKeyPairInput_GenerateECCKeyPairInput as DafnyGenerateECCKeyPairInput,
    GenerateECCKeyPairOutput_GenerateECCKeyPairOutput as DafnyGenerateECCKeyPairOutput,
    GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput as DafnyGenerateECDSASignatureKeyInput,
    GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput as DafnyGenerateECDSASignatureKeyOutput,
    GenerateRSAKeyPairInput_GenerateRSAKeyPairInput as DafnyGenerateRSAKeyPairInput,
    GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput as DafnyGenerateRSAKeyPairOutput,
    GenerateRandomBytesInput_GenerateRandomBytesInput as DafnyGenerateRandomBytesInput,
    GetPublicKeyFromPrivateKeyInput_GetPublicKeyFromPrivateKeyInput as DafnyGetPublicKeyFromPrivateKeyInput,
    GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput as DafnyGetPublicKeyFromPrivateKeyOutput,
    GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput as DafnyGetRSAKeyModulusLengthInput,
    GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput as DafnyGetRSAKeyModulusLengthOutput,
    HMacInput_HMacInput as DafnyHMacInput,
    HkdfExpandInput_HkdfExpandInput as DafnyHkdfExpandInput,
    HkdfExtractInput_HkdfExtractInput as DafnyHkdfExtractInput,
    HkdfInput_HkdfInput as DafnyHkdfInput,
    KdfCtrInput_KdfCtrInput as DafnyKdfCtrInput,
    ParsePublicKeyInput_ParsePublicKeyInput as DafnyParsePublicKeyInput,
    ParsePublicKeyOutput_ParsePublicKeyOutput as DafnyParsePublicKeyOutput,
    RSADecryptInput_RSADecryptInput as DafnyRSADecryptInput,
    RSAEncryptInput_RSAEncryptInput as DafnyRSAEncryptInput,
    RSAPaddingMode_OAEP__SHA1,
    RSAPaddingMode_OAEP__SHA256,
    RSAPaddingMode_OAEP__SHA384,
    RSAPaddingMode_OAEP__SHA512,
    RSAPaddingMode_PKCS1,
    RSAPrivateKey_RSAPrivateKey as DafnyRSAPrivateKey,
    RSAPublicKey_RSAPublicKey as DafnyRSAPublicKey,
    ValidatePublicKeyInput_ValidatePublicKeyInput as DafnyValidatePublicKeyInput,
    ValidatePublicKeyOutput_ValidatePublicKeyOutput as DafnyValidatePublicKeyOutput,
)
import aws_cryptography_primitives.internaldafny.generated.module_
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def aws_cryptography_primitives_GenerateRandomBytesInput(native_input):
    return DafnyGenerateRandomBytesInput(
        length=native_input.length,
    )


def aws_cryptography_primitives_DigestInput(native_input):
    return DafnyDigestInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        message=Seq(native_input.message),
    )


def aws_cryptography_primitives_DigestAlgorithm(native_input):
    if native_input == "SHA_512":
        return DigestAlgorithm_SHA__512()

    elif native_input == "SHA_384":
        return DigestAlgorithm_SHA__384()

    elif native_input == "SHA_256":
        return DigestAlgorithm_SHA__256()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_primitives_HMacInput(native_input):
    return DafnyHMacInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        key=Seq(native_input.key),
        message=Seq(native_input.message),
    )


def aws_cryptography_primitives_HkdfExtractInput(native_input):
    return DafnyHkdfExtractInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        salt=(
            (Option_Some(Seq(native_input.salt)))
            if (native_input.salt is not None)
            else (Option_None())
        ),
        ikm=Seq(native_input.ikm),
    )


def aws_cryptography_primitives_HkdfExpandInput(native_input):
    return DafnyHkdfExpandInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        prk=Seq(native_input.prk),
        info=Seq(native_input.info),
        expectedLength=native_input.expected_length,
    )


def aws_cryptography_primitives_HkdfInput(native_input):
    return DafnyHkdfInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        salt=(
            (Option_Some(Seq(native_input.salt)))
            if (native_input.salt is not None)
            else (Option_None())
        ),
        ikm=Seq(native_input.ikm),
        info=Seq(native_input.info),
        expectedLength=native_input.expected_length,
    )


def aws_cryptography_primitives_KdfCtrInput(native_input):
    return DafnyKdfCtrInput(
        digestAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_DigestAlgorithm(
            native_input.digest_algorithm
        ),
        ikm=Seq(native_input.ikm),
        expectedLength=native_input.expected_length,
        purpose=(
            (Option_Some(Seq(native_input.purpose)))
            if (native_input.purpose is not None)
            else (Option_None())
        ),
        nonce=(
            (Option_Some(Seq(native_input.nonce)))
            if (native_input.nonce is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_primitives_AesKdfCtrInput(native_input):
    return DafnyAesKdfCtrInput(
        ikm=Seq(native_input.ikm),
        expectedLength=native_input.expected_length,
        nonce=(
            (Option_Some(Seq(native_input.nonce)))
            if (native_input.nonce is not None)
            else (Option_None())
        ),
    )


def aws_cryptography_primitives_AESEncryptInput(native_input):
    return DafnyAESEncryptInput(
        encAlg=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AES_GCM(
            native_input.enc_alg
        ),
        iv=Seq(native_input.iv),
        key=Seq(native_input.key),
        msg=Seq(native_input.msg),
        aad=Seq(native_input.aad),
    )


def aws_cryptography_primitives_AES_GCM(native_input):
    return DafnyAES_GCM(
        keyLength=native_input.key_length,
        tagLength=native_input.tag_length,
        ivLength=native_input.iv_length,
    )


def aws_cryptography_primitives_AESDecryptInput(native_input):
    return DafnyAESDecryptInput(
        encAlg=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_AES_GCM(
            native_input.enc_alg
        ),
        key=Seq(native_input.key),
        cipherTxt=Seq(native_input.cipher_txt),
        authTag=Seq(native_input.auth_tag),
        iv=Seq(native_input.iv),
        aad=Seq(native_input.aad),
    )


def aws_cryptography_primitives_GenerateRSAKeyPairInput(native_input):
    return DafnyGenerateRSAKeyPairInput(
        lengthBits=native_input.length_bits,
    )


def aws_cryptography_primitives_GetRSAKeyModulusLengthInput(native_input):
    return DafnyGetRSAKeyModulusLengthInput(
        publicKey=Seq(native_input.public_key),
    )


def aws_cryptography_primitives_RSADecryptInput(native_input):
    return DafnyRSADecryptInput(
        padding=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSAPaddingMode(
            native_input.padding
        ),
        privateKey=Seq(native_input.private_key),
        cipherText=Seq(native_input.cipher_text),
    )


def aws_cryptography_primitives_RSAPaddingMode(native_input):
    if native_input == "PKCS1":
        return RSAPaddingMode_PKCS1()

    elif native_input == "OAEP_SHA1":
        return RSAPaddingMode_OAEP__SHA1()

    elif native_input == "OAEP_SHA256":
        return RSAPaddingMode_OAEP__SHA256()

    elif native_input == "OAEP_SHA384":
        return RSAPaddingMode_OAEP__SHA384()

    elif native_input == "OAEP_SHA512":
        return RSAPaddingMode_OAEP__SHA512()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_primitives_RSAEncryptInput(native_input):
    return DafnyRSAEncryptInput(
        padding=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSAPaddingMode(
            native_input.padding
        ),
        publicKey=Seq(native_input.public_key),
        plaintext=Seq(native_input.plaintext),
    )


def aws_cryptography_primitives_GenerateECDSASignatureKeyInput(native_input):
    return DafnyGenerateECDSASignatureKeyInput(
        signatureAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            native_input.signature_algorithm
        ),
    )


def aws_cryptography_primitives_ECDSASignatureAlgorithm(native_input):
    if native_input == "ECDSA_P384":
        return ECDSASignatureAlgorithm_ECDSA__P384()

    elif native_input == "ECDSA_P256":
        return ECDSASignatureAlgorithm_ECDSA__P256()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_primitives_ECDSASignInput(native_input):
    return DafnyECDSASignInput(
        signatureAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            native_input.signature_algorithm
        ),
        signingKey=Seq(native_input.signing_key),
        message=Seq(native_input.message),
    )


def aws_cryptography_primitives_ECDSAVerifyInput(native_input):
    return DafnyECDSAVerifyInput(
        signatureAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            native_input.signature_algorithm
        ),
        verificationKey=Seq(native_input.verification_key),
        message=Seq(native_input.message),
        signature=Seq(native_input.signature),
    )


def aws_cryptography_primitives_GenerateECCKeyPairInput(native_input):
    return DafnyGenerateECCKeyPairInput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
    )


def aws_cryptography_primitives_ECDHCurveSpec(native_input):
    if native_input == "ECC_NIST_P256":
        return ECDHCurveSpec_ECC__NIST__P256()

    elif native_input == "ECC_NIST_P384":
        return ECDHCurveSpec_ECC__NIST__P384()

    elif native_input == "ECC_NIST_P521":
        return ECDHCurveSpec_ECC__NIST__P521()

    elif native_input == "SM2":
        return ECDHCurveSpec_SM2()

    else:
        raise ValueError(f"No recognized enum value in enum type: {native_input=}")


def aws_cryptography_primitives_GetPublicKeyFromPrivateKeyInput(native_input):
    return DafnyGetPublicKeyFromPrivateKeyInput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
        privateKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPrivateKey(
            native_input.private_key
        ),
    )


def aws_cryptography_primitives_ECCPrivateKey(native_input):
    return DafnyECCPrivateKey(
        pem=Seq(native_input.pem),
    )


def aws_cryptography_primitives_ValidatePublicKeyInput(native_input):
    return DafnyValidatePublicKeyInput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
        publicKey=Seq(native_input.public_key),
    )


def aws_cryptography_primitives_DeriveSharedSecretInput(native_input):
    return DafnyDeriveSharedSecretInput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
        privateKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPrivateKey(
            native_input.private_key
        ),
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPublicKey(
            native_input.public_key
        ),
    )


def aws_cryptography_primitives_ECCPublicKey(native_input):
    return DafnyECCPublicKey(
        der=Seq(native_input.der),
    )


def aws_cryptography_primitives_CompressPublicKeyInput(native_input):
    return DafnyCompressPublicKeyInput(
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPublicKey(
            native_input.public_key
        ),
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
    )


def aws_cryptography_primitives_DecompressPublicKeyInput(native_input):
    return DafnyDecompressPublicKeyInput(
        compressedPublicKey=Seq(native_input.compressed_public_key),
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
    )


def aws_cryptography_primitives_ParsePublicKeyInput(native_input):
    return DafnyParsePublicKeyInput(
        publicKey=Seq(native_input.public_key),
    )


def aws_cryptography_primitives_GenerateRandomBytesOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_DigestOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_HMacOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_HkdfExtractOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_HkdfExpandOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_HkdfOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_KdfCtrOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_AesKdfCtrOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_AESEncryptOutput(native_input):
    return DafnyAESEncryptOutput(
        cipherText=Seq(native_input.cipher_text),
        authTag=Seq(native_input.auth_tag),
    )


def aws_cryptography_primitives_AESDecryptOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_GenerateRSAKeyPairOutput(native_input):
    return DafnyGenerateRSAKeyPairOutput(
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSAPublicKey(
            native_input.public_key
        ),
        privateKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_RSAPrivateKey(
            native_input.private_key
        ),
    )


def aws_cryptography_primitives_RSAPublicKey(native_input):
    return DafnyRSAPublicKey(
        lengthBits=native_input.length_bits,
        pem=Seq(native_input.pem),
    )


def aws_cryptography_primitives_RSAPrivateKey(native_input):
    return DafnyRSAPrivateKey(
        lengthBits=native_input.length_bits,
        pem=Seq(native_input.pem),
    )


def aws_cryptography_primitives_GetRSAKeyModulusLengthOutput(native_input):
    return DafnyGetRSAKeyModulusLengthOutput(
        length=native_input.length,
    )


def aws_cryptography_primitives_RSADecryptOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_RSAEncryptOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_GenerateECDSASignatureKeyOutput(native_input):
    return DafnyGenerateECDSASignatureKeyOutput(
        signatureAlgorithm=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDSASignatureAlgorithm(
            native_input.signature_algorithm
        ),
        verificationKey=Seq(native_input.verification_key),
        signingKey=Seq(native_input.signing_key),
    )


def aws_cryptography_primitives_ECDSASignOutput(native_input):
    return Seq(native_input)


def aws_cryptography_primitives_ECDSAVerifyOutput(native_input):
    return native_input


def aws_cryptography_primitives_GenerateECCKeyPairOutput(native_input):
    return DafnyGenerateECCKeyPairOutput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
        privateKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPrivateKey(
            native_input.private_key
        ),
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPublicKey(
            native_input.public_key
        ),
    )


def aws_cryptography_primitives_GetPublicKeyFromPrivateKeyOutput(native_input):
    return DafnyGetPublicKeyFromPrivateKeyOutput(
        eccCurve=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECDHCurveSpec(
            native_input.ecc_curve
        ),
        privateKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPrivateKey(
            native_input.private_key
        ),
        publicKey=Seq(native_input.public_key),
    )


def aws_cryptography_primitives_ValidatePublicKeyOutput(native_input):
    return DafnyValidatePublicKeyOutput(
        success=native_input.success,
    )


def aws_cryptography_primitives_DeriveSharedSecretOutput(native_input):
    return DafnyDeriveSharedSecretOutput(
        sharedSecret=Seq(native_input.shared_secret),
    )


def aws_cryptography_primitives_CompressPublicKeyOutput(native_input):
    return DafnyCompressPublicKeyOutput(
        compressedPublicKey=Seq(native_input.compressed_public_key),
    )


def aws_cryptography_primitives_DecompressPublicKeyOutput(native_input):
    return DafnyDecompressPublicKeyOutput(
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPublicKey(
            native_input.public_key
        ),
    )


def aws_cryptography_primitives_ParsePublicKeyOutput(native_input):
    return DafnyParsePublicKeyOutput(
        publicKey=aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.smithy_to_dafny.aws_cryptography_primitives_ECCPublicKey(
            native_input.public_key
        ),
    )


def aws_cryptography_primitives_CryptoConfig(native_input):
    return DafnyCryptoConfig()
