from aws_cryptography_primitives.internal_generated_dafny.AESEncryption import *
import aws_cryptography_primitives.internal_generated_dafny.AESEncryption
import Wrappers
import _dafny
from aws_cryptography_primitives.internal_generated_dafny.HMAC import *
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

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
            ct = aesgcm.encrypt(iv_bytes, plaintext_bytes, aad_bytes)

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
            plaintext = aesgcm.decrypt(iv_bytes, ct_and_tag, aad_bytes)

            return Wrappers.Result_Success(_dafny.Seq(plaintext))

aws_cryptography_primitives.internal_generated_dafny.AESEncryption.AESEncryption = AESEncryption
