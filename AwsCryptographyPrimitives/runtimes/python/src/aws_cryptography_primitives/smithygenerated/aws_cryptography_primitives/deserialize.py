# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
    AESEncryptOutput_AESEncryptOutput as DafnyAESEncryptOutput,
    Error,
    Error_AwsCryptographicPrimitivesError,
    GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput as DafnyGenerateECDSASignatureKeyOutput,
    GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput as DafnyGenerateRSAKeyPairOutput,
    GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput as DafnyGetRSAKeyModulusLengthOutput,
)
import aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy
import module_
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    AwsCryptographicPrimitivesError,
    CollectionOfErrors,
    OpaqueError,
    ServiceError,
)

from .config import Config


async def _deserialize_generate_random_bytes(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateRandomBytesOutput(input.value)

async def _deserialize_digest(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_DigestOutput(input.value)

async def _deserialize_h_mac(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HMacOutput(input.value)

async def _deserialize_hkdf_extract(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfExtractOutput(input.value)

async def _deserialize_hkdf_expand(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfExpandOutput(input.value)

async def _deserialize_hkdf(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_HkdfOutput(input.value)

async def _deserialize_kdf_counter_mode(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_KdfCtrOutput(input.value)

async def _deserialize_aes_kdf_counter_mode(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AesKdfCtrOutput(input.value)

async def _deserialize_aes_encrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AESEncryptOutput(input.value)

async def _deserialize_aes_decrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_AESDecryptOutput(input.value)

async def _deserialize_generate_rsa_key_pair(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateRSAKeyPairOutput(input.value)

async def _deserialize_get_rsa_key_modulus_length(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GetRSAKeyModulusLengthOutput(input.value)

async def _deserialize_rsa_decrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSADecryptOutput(input.value)

async def _deserialize_rsa_encrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_RSAEncryptOutput(input.value)

async def _deserialize_generate_ecdsa_signature_key(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_GenerateECDSASignatureKeyOutput(input.value)

async def _deserialize_ecdsa_sign(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSASignOutput(input.value)

async def _deserialize_ecdsa_verify(input: DafnyResponse, config: Config):

  if input.IsFailure():
      return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.dafny_to_smithy.aws_cryptography_primitives_ECDSAVerifyOutput(input.value)

async def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
        return OpaqueError(obj=error.obj)
    elif error.is_CollectionOfErrors:
        return CollectionOfErrors(
            message=_dafny.string_of(error.message),
            list=[await _deserialize_error(dafny_e) for dafny_e in error.list],
        )
    elif error.is_AwsCryptographicPrimitivesError:
      return AwsCryptographicPrimitivesError(message=_dafny.string_of(error.message))
    else:
        return OpaqueError(obj=error)
