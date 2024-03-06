from aws_cryptography_primitives.internaldafny.generated.AESEncryption import *
import aws_cryptography_primitives.internaldafny.generated.AESEncryption
import Wrappers
import _dafny
from aws_cryptography_primitives.internaldafny.generated.HMAC import *
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from software_amazon_cryptography_primitives_internaldafny_types import Error_AwsCryptographicPrimitivesError
from cryptography.exceptions import InvalidTag

default__ = aws_cryptography_primitives.internaldafny.generated.AESEncryption.default__

class AESEncryption:

    class AES_GCM:

        @staticmethod
        def AESEncryptExtern(
            enc_alg,
            iv,
            key,
            message,
            aad
        ) -> Wrappers.Result:
            key_bytes = bytes(key)
            iv_bytes = bytes(iv)
            plaintext_bytes = bytes(message)
            aad_bytes = bytes(aad)

            aesgcm = AESGCM(key_bytes)
            try:
                ct = aesgcm.encrypt(iv_bytes, plaintext_bytes, aad_bytes)
            except OverflowError:
                return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
                    message="AES-GCM cannot encrypt plaintext data larger than 2^31-1 bytes"
                ))

            return Wrappers.Result_Success(
                default__.EncryptionOutputFromByteSeq(_dafny.Seq(ct), enc_alg)
            )

        @staticmethod
        def AESDecryptExtern(
            enc_alg,
            key,
            ciphertext,
            auth_tag,
            iv,
            aad
        ) -> Wrappers.Result:
            key_bytes = bytes(key)
            iv_bytes = bytes(iv)
            ciphertext_bytes = bytes(ciphertext)
            tag_bytes = bytes(auth_tag)
            aad_bytes = bytes(aad)

            ct_and_tag = ciphertext_bytes + tag_bytes
            aesgcm = AESGCM(key_bytes)
            try:
                plaintext = aesgcm.decrypt(iv_bytes, ct_and_tag, aad_bytes)
            except InvalidTag:
                return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
                    message="AES-GCM decrypt failed to validate authentication tag for ciphertext"
                ))

            return Wrappers.Result_Success(_dafny.Seq(plaintext))

aws_cryptography_primitives.internaldafny.generated.AESEncryption.AESEncryption = AESEncryption
