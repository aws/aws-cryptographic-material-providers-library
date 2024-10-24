# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.exceptions import AlreadyFinalized

import _dafny

import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import Error_Opaque


# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.AesKdfCtr.default__):

  @staticmethod
  def AesKdfCtrStream(nonce, key, length):
    cipher = Cipher(
        algorithms.AES(bytes(key)), modes.CTR(bytes(nonce)),
    )
    plaintext = bytearray(length)
    encryptor = cipher.encryptor()
    try:
      ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    except ValueError:
      return Wrappers.Result_Failure(Error_Opaque(
        "Cannot finalize an encryptor when the plaintext data is not a multiple of the algorithm block size",
        "Cannot finalize an encryptor when the plaintext data is not a multiple of the algorithm block size"
      ))
    except AlreadyFinalized:
      return Wrappers.Result_Failure(Error_Opaque(
        "Cannot update or finalize an encryptor which was already finalized",
        "Cannot update or finalize an encryptor which was already finalized"
      ))
    return Wrappers.Result_Success(_dafny.Seq(ciphertext))
  
# Export extern-extended class into generated class
aws_cryptography_primitives.internaldafny.generated.AesKdfCtr.default__ = default__
