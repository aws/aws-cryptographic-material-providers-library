# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
  NoEncryption,
  Encoding,
  PrivateFormat,
  PublicFormat,
  load_pem_public_key,
  load_pem_private_key,
)
from cryptography.hazmat.primitives import hashes

import _dafny

from aws_cryptography_primitives.internaldafny.generated.RSAEncryption import *
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import _smithy_error_to_dafny_error

# No generated class to extend
class RSA:

  RSA_KEY_LEN_MAX = 4096
  RSA_PUBLIC_EXPONENT = 65537
  RSA_ERROR_MSG = "AWS Crypto will not generate an RSA Key with length greater than " + str(RSA_KEY_LEN_MAX)

  @classmethod
  def GenerateKeyPairExtern(cls, length_bits):
    if length_bits > cls.RSA_KEY_LEN_MAX:
      raise Exception(cls.RSA_ERROR_MSG)
    private_key = rsa.generate_private_key(
        public_exponent=cls.RSA_PUBLIC_EXPONENT,
        key_size=length_bits,
    )
    private_key_pem_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
    public_key = private_key.public_key()
    public_key_pem_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    return _dafny.Seq(public_key_pem_bytes), _dafny.Seq(private_key_pem_bytes)

  @staticmethod
  def GetPaddingForPaddingMode(padding_mode):
    if padding_mode.is_OAEP__SHA1:
      return padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA1()),
          algorithm=hashes.SHA1(),
          label=None
      )
    elif padding_mode.is_OAEP__SHA256:
      return padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
          label=None
      )
    elif padding_mode.is_OAEP__SHA384:
      return padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA384()),
          algorithm=hashes.SHA384(),
          label=None
      )
    elif padding_mode.is_OAEP__SHA512:
      return padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA512()),
          algorithm=hashes.SHA512(),
          label=None
      )
    elif padding_mode.is_PKCS1:
      return padding.PKCS1v15()

  @staticmethod
  def EncryptExtern(padding_mode, public_key_der, plaintext):
    try:
      plaintext_bytes = bytes(plaintext)
      public_key = load_pem_public_key(bytes(public_key_der))

      ct = public_key.encrypt(
        plaintext_bytes,
        RSA.GetPaddingForPaddingMode(padding_mode)
      )

      return Wrappers.Result_Success(_dafny.Seq(ct))
    except Exception as e:
      return Wrappers.Result_Failure(
        _smithy_error_to_dafny_error(
          e
        )
      )

  @staticmethod
  def DecryptExtern(padding_mode, private_key_der, ciphertext):
    ciphertext_bytes = bytes(ciphertext)
    private_key = load_pem_private_key(bytes(private_key_der), None)

    try:
      pt = private_key.decrypt(
        ciphertext_bytes,
        RSA.GetPaddingForPaddingMode(padding_mode)
      )

      return Wrappers.Result_Success(_dafny.Seq(pt))
    except Exception as e:
      return Wrappers.Result_Failure(
        _smithy_error_to_dafny_error(
          e
        )
      )

  @staticmethod
  def GetRSAKeyModulusLengthExtern(public_key_pem):
    try:
      public_key = load_pem_public_key(bytes(public_key_pem))
      modulus_bit_length = public_key.key_size
      return Wrappers.Result_Success(modulus_bit_length)
    except Exception as e:
      return Wrappers.Result_Failure(
        _smithy_error_to_dafny_error(
          e
        )
      )

class EmptyClass:
  pass
# Export extern class into the generated module
aws_cryptography_primitives.internaldafny.generated.RSAEncryption.RSA = RSA
aws_cryptography_primitives.internaldafny.generated.RSAEncryption.RSAEncryption = EmptyClass
aws_cryptography_primitives.internaldafny.generated.RSAEncryption.RSAEncryption.RSA = RSA
# Remove following lines after https://github.com/dafny-lang/dafny/issues/4853 is resolved
aws_cryptography_primitives.internaldafny.generated.RSAEncryption.RSA_GetRSAKeyModulusLengthExtern = RSA.GetRSAKeyModulusLengthExtern
aws_cryptography_primitives.internaldafny.generated.RSAEncryption.RSAEncryption.RSA_GetRSAKeyModulusLengthExtern = RSA.GetRSAKeyModulusLengthExtern
RSA_GetRSAKeyModulusLengthExtern = RSA.GetRSAKeyModulusLengthExtern