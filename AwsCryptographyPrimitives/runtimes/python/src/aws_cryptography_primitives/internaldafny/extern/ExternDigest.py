# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives import hashes

import _dafny

import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.Digest
import aws_cryptography_primitives.internaldafny.generated.ExternDigest
from aws_cryptography_primitives.internaldafny.generated.Digest import *


# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.ExternDigest.default__):

  @staticmethod
  def get_hash(digest_algorithm):
    if digest_algorithm.is_SHA__256:
      return hashes.Hash(hashes.SHA256())
    elif digest_algorithm.is_SHA__384:
      return hashes.Hash(hashes.SHA384())
    elif digest_algorithm.is_SHA__512:
      return hashes.Hash(hashes.SHA512())
    else:
      raise ValueError(f"Unsupported digest algorithm: {digest_algorithm}")

  @staticmethod
  def internal_digest(digest_algorithm, message):
    try:
      hash = default__.get_hash(digest_algorithm)
      message_bytes = bytes(message)
      hash.update(message_bytes)
      digest = hash.finalize()
      return Wrappers.Result_Success(digest)
    except ValueError as e:
      error = aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(
          message="Requested digest Algorithm is not supported."
      )
      return Wrappers.Result_Failure(error=error)


  @staticmethod
  def Digest(digest_algorithm, message):
    maybe_digest = default__.internal_digest(digest_algorithm, message)
    if maybe_digest.is_Failure:
      return maybe_digest.PropagateFailure()
    else:
      return Wrappers.Result_Success(_dafny.Seq(maybe_digest.value))

# Export extern-extended class into generated class
aws_cryptography_primitives.internaldafny.generated.ExternDigest.default__ = default__
