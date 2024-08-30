# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from cryptography.exceptions import (
  InvalidSignature,
  UnsupportedAlgorithm
)
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
  NoEncryption,
  Encoding,
  PrivateFormat,
  load_pem_private_key,
)
import cryptography.hazmat.primitives.asymmetric.ec as ec
from cryptography.hazmat.primitives.asymmetric.ec import (
  SECP256R1,
  SECP384R1,
)
from cryptography.hazmat.primitives.asymmetric.utils import (
  decode_dss_signature,
  encode_dss_signature
)

from collections import namedtuple
import _dafny
from enum import Enum

import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
from aws_cryptography_primitives.internaldafny.generated.Signature import *
import aws_cryptography_primitives.internaldafny.generated.Signature
from aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes import (
  DigestAlgorithm_SHA__256,
  DigestAlgorithm_SHA__384,
  Error_AwsCryptographicPrimitivesError
)


# Extend generated class
class default__(aws_cryptography_primitives.internaldafny.generated.Signature.default__):
  class ECDSA:

    @staticmethod
    def ExternKeyGen(signature_algorithm):
      maybe_signature_algorithm = SignatureAlgorithms.signatureAlgorithm(signature_algorithm)
      if maybe_signature_algorithm.is_Failure:
        return Wrappers.Result_Failure(maybe_signature_algorithm.error)
      
      private_key = ec.generate_private_key(
        maybe_signature_algorithm.value.value.curve
      )

      private_key_pem_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
      public_key_pem_bytes = _ecc_encode_compressed_point(private_key)

      return Wrappers.Result_Success(SignatureKeyPair_SignatureKeyPair(
          verificationKey=_dafny.Seq(public_key_pem_bytes),
          signingKey=_dafny.Seq(private_key_pem_bytes)
      ))

    @staticmethod
    def Sign(signature_algorithm, signing_key, message):
      maybe_signature_algorithm = SignatureAlgorithms.signatureAlgorithm(signature_algorithm)
      if maybe_signature_algorithm.is_Failure:
        return Wrappers.Result_Failure(maybe_signature_algorithm.error)
      
      try:
        private_key = load_pem_private_key(bytes(signing_key), None)
      except ValueError:
        return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
          message="Could not decode signing_key"
        ))
      except TypeError:
        return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
          message="Provided signing_key is encrypted, but encrypted signing_keys are not supported"
        ))
      except UnsupportedAlgorithm:
        return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
          message="Serialized key type is not supported by cryptography provider"
        ))

      maybe_digest = ExternDigest.default__.internal_digest(
          maybe_signature_algorithm.value.value.message_digest_algorithm,
          message
      )
      if maybe_digest.is_Failure:
        return Wrappers.Result_Failure(maybe_digest.error)
      digest = maybe_digest.value

      signature_algorithm = maybe_signature_algorithm.value.value
      signature = _ecc_static_length_signature(private_key, signature_algorithm, digest)

      return Wrappers.Result_Success(_dafny.Seq(signature))

    @staticmethod
    def Verify(signature_algorithm, verification_key, message, signature):
      maybe_signature_algorithm = SignatureAlgorithms.signatureAlgorithm(signature_algorithm)
      if maybe_signature_algorithm.is_Failure:
        return Wrappers.Result_Failure(maybe_signature_algorithm.error)
      
      message_digest_algorithm = maybe_signature_algorithm.value.value.message_digest_algorithm
      if message_digest_algorithm.is_SHA__256:
        sign_algo = ec.ECDSA(hashes.SHA256())
      elif message_digest_algorithm.is_SHA__384:
        sign_algo = ec.ECDSA(hashes.SHA384())
      else:
        return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
          message=f"Requested Digest Algorithm is not supported. Requested {message_digest_algorithm}"
        ))

      curve = maybe_signature_algorithm.value.value.curve()

      try:
        public_key = _ecc_public_numbers_from_compressed_point(curve, verification_key).public_key()
      except (TypeError, NotImplementedError) as e:
        return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
          message=str(e)
        ))

      maybe_digest = ExternDigest.default__.internal_digest(
          maybe_signature_algorithm.value.value.message_digest_algorithm,
          message
      )
      if maybe_digest.is_Failure:
        return Wrappers.Result_Failure(maybe_digest.error)
      digest = maybe_digest.value

      try:
        public_key.verify(bytes(signature),
                          digest,
                          sign_algo)
      except InvalidSignature:
        # If signature fails to validate, return Success(False)
        return Wrappers.Result_Success(False)
      
      # If signature validates, return Success(True)
      return Wrappers.Result_Success(True)

# Export extern-extended class into generated class
aws_cryptography_primitives.internaldafny.generated.Signature.default__ = default__

class SignatureAlgorithm:
  def __init__(self, curve, message_digest_algorithm, raw_signature_algorithm, expected_signature_length):
    self.curve = curve
    self.message_digest_algorithm = message_digest_algorithm
    self.raw_signature_algorithm = raw_signature_algorithm
    self.expected_signature_length = expected_signature_length

class SignatureAlgorithms(Enum):
  P256 = SignatureAlgorithm(
            SECP256R1,
            DigestAlgorithm_SHA__256(),
            "NONEwithECDSA",
            71
          )
  P384 = SignatureAlgorithm(
            SECP384R1,
            DigestAlgorithm_SHA__384(),
            "NONEwithECDSA",
            103
          )

  @classmethod
  def signatureAlgorithm(self, sig_alg):
    #= aws-encryption-sdk-specification/framework/transitive-requirements.md#ecdsa
    ## If specified to use ECDSA, the AWS Encryption SDK MUST use ECDSA with the following specifics:
    ## - The elliptic curve is specified by the algorithm suite.
    ##   The specific curves are defined in
    ##   [Digital Signature Standard (DSS) (FIPS PUB 186-4)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf).
    if sig_alg.is_ECDSA__P256:
      signature_algorithm = SignatureAlgorithms.P256
    elif sig_alg.is_ECDSA__P384:
      signature_algorithm = SignatureAlgorithms.P384
    else:
      return Wrappers.Result_Failure(Error_AwsCryptographicPrimitivesError(
        message=f"Requested Curve is not supported. Requested {sig_alg}"
      ))
    return Wrappers.Result_Success(signature_algorithm)

# Export extern class
aws_cryptography_primitives.internaldafny.generated.Signature.ECDSA = default__.ECDSA
# Weirdness with how we've named the extern in Dafny...
aws_cryptography_primitives.internaldafny.generated.Signature.Signature = aws_cryptography_primitives.internaldafny.generated.Signature
aws_cryptography_primitives.internaldafny.generated.Signature.Signature.ECDSA = default__.ECDSA
# Remove after https://github.com/dafny-lang/dafny/issues/4853
aws_cryptography_primitives.internaldafny.generated.Signature.ECDSA_Verify = default__.ECDSA.Verify
ECDSA_Verify = default__.ECDSA.Verify

### Following are copied, lightly modified, and pasted util functions/constant definitions
### from the AWS Encryption SDK for Python.
### Reference: https://github.com/aws/aws-encryption-sdk-python/blob/ad6b02c69523d71181734ee42cc9a1debefb8631/src/aws_encryption_sdk/internal/crypto/elliptic_curve.py

def _to_bytes(data):
  """Takes an input str or bytes object and returns an equivalent bytes object.

  :param data: Input data
  :type data: str or bytes
  :returns: Data normalized to bytes
  :rtype: bytes
  """
  if isinstance(data, str) and not isinstance(data, bytes):
    return str.encode(data)
  return data

def _int_to_bytes(integer, length = None):
  return integer.to_bytes(
      length or (integer.bit_length() + 7) // 8 or 1, "big"
  )

_ECCCurveParameters = namedtuple("_ECCCurveParameters", ["p", "a", "b", "order"])
_ECC_CURVE_PARAMETERS = {
  "secp256r1": _ECCCurveParameters(
      p=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF,
      a=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC,
      b=0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B,
      order=0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551,
  ),
  "secp384r1": _ECCCurveParameters(
      p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFF0000000000000000FFFFFFFF,
      a=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFF0000000000000000FFFFFFFC,
      b=0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF,
      order=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC7634D81F4372DDF581A0DB248B0A77AECEC196ACCC52973,
  ),
  "secp521r1": _ECCCurveParameters(
      p=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, # noqa pylint: disable=line-too-long
      a=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC, # noqa pylint: disable=line-too-long
      b=0x0051953EB9618E1C9A1F929A21A0B68540EEA2DA725B99B315F3B8B489918EF109E156193951EC7E937B1652C0BD3BB1BF073573DF883D2C34F1EF451FD46B503F00, # noqa pylint: disable=line-too-long
      order=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA51868783BF2F966B7FCC0148F709A5D03BB5C9B8899C47AEBB6FB71E91386409, # noqa pylint: disable=line-too-long
  ),
}

def _ecc_static_length_signature(key, algorithm, digest):
  """Calculates an elliptic curve signature with a static length using pre-calculated hash.

  :param key: Elliptic curve private key
  :type key: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey
  :param algorithm: Master algorithm to use
  :type algorithm: aws_encryption_sdk.identifiers.Algorithm
  :param bytes digest: Pre-calculated hash digest
  :returns: Signature with required length
  :rtype: bytes
  """
  if algorithm.message_digest_algorithm.is_SHA__256:
    sign_algo = ec.ECDSA(hashes.SHA256())
  elif algorithm.message_digest_algorithm.is_SHA__384:
    sign_algo = ec.ECDSA(hashes.SHA384())
  pre_hashed_algorithm = sign_algo
  signature = b""
  while len(signature) != algorithm.expected_signature_length:
    signature = key.sign(digest, pre_hashed_algorithm)
    if len(signature) != algorithm.expected_signature_length:
      # Most of the time, a signature of the wrong length can be fixed
      # by negating s in the signature relative to the group order.
      r, s = decode_dss_signature(signature)
      s = _ECC_CURVE_PARAMETERS[algorithm.curve.name].order - s
      signature = encode_dss_signature(r, s)
  return signature

def _ecc_encode_compressed_point_public_key(public_key: EllipticCurvePublicKey):
  """Encodes a compressed elliptic curve point
      as described in SEC-1 v2 section 2.3.3
      http://www.secg.org/sec1-v2.pdf

  :param private_key: Private key from which to extract point data
  :type private_key: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey
  :returns: Encoded compressed elliptic curve point
  :rtype: bytes
  :raises NotImplementedError: for non-prime curves
  """
  public_numbers = public_key.public_numbers()
  # key_size is in bits. Convert to bytes and round up
  byte_length = (public_key.curve.key_size + 7) // 8
  y_map = [b"\x02", b"\x03"]
  # If curve in prime field.
  if public_key.curve.name.startswith("secp"):
    y_order = public_numbers.y % 2
    y = y_map[y_order]
  else:
    raise NotImplementedError("Non-prime curves are not supported at this time")
  return y + _int_to_bytes(public_numbers.x, byte_length)

def _ecc_encode_compressed_point(private_key):
  """Encodes a compressed elliptic curve point
      as described in SEC-1 v2 section 2.3.3
      http://www.secg.org/sec1-v2.pdf

  :param private_key: Private key from which to extract point data
  :type private_key: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey
  :returns: Encoded compressed elliptic curve point
  :rtype: bytes
  :raises NotImplementedError: for non-prime curves
  """
  public_key = private_key.public_key()
  return _ecc_encode_compressed_point_public_key(public_key)

def _ecc_decode_compressed_point(curve, compressed_point):
  """Decodes a compressed elliptic curve point
      as described in SEC-1 v2 section 2.3.4
      http://www.secg.org/sec1-v2.pdf

  :param curve: Elliptic curve type to generate
  :type curve: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurve
  :param bytes compressed_point: Encoded compressed elliptic curve point
  :returns: X and Y coordinates from compressed point
  :rtype: tuple of longs
  :raises NotImplementedError: for non-prime curves and unsupported prime curves
  :raises TypeError: for points at infinity
  """
  if not compressed_point:
    raise TypeError("Points at infinity are not allowed")
  y_order_map = {b"\x02": 0, b"\x03": 1}
  raw_x = compressed_point[1:]
  raw_x = _to_bytes(raw_x)
  x = int.from_bytes(raw_x, "big")
  raw_y = compressed_point[0]
  # In Python3, bytes index calls return int values rather than strings
  if isinstance(raw_y, int):
    raw_y = str.encode(chr(raw_y))
  elif isinstance(raw_y, str):
    raw_y = str.encode(raw_y)
  y_order = y_order_map[raw_y]
  # If curve in prime field.
  if curve.name.startswith("secp"):
    try:
      params = _ECC_CURVE_PARAMETERS[curve.name]
    except KeyError:
      raise NotImplementedError("Curve {name} is not supported at this time".format(name=curve.name))
    alpha = (pow(x, 3, params.p) + (params.a * x % params.p) + params.b) % params.p
    # Only works for p % 4 == 3 at this time.
    # This is the case for all currently supported algorithms.
    # This will need to be expanded if curves which do not match this are added.
    #  Python-ecdsa has these algorithms implemented.  Copy or reference?
    #  https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
    #  Handbook of Applied Cryptography, algorithms 3.34 - 3.39
    if params.p % 4 == 3:
      beta = pow(alpha, (params.p + 1) // 4, params.p)
    else:
      raise NotImplementedError("S not 1 :: Curve not supported at this time")
    if beta % 2 == y_order:
      y = beta
    else:
      y = params.p - beta
  else:
    raise NotImplementedError("Non-prime curves are not supported at this time")
  return x, y

def _ecc_public_numbers_from_compressed_point(curve, compressed_point):
  """Decodes a compressed elliptic curve point
      as described in SEC-1 v2 section 2.3.3
      and returns a PublicNumbers instance
      based on the decoded point.
      http://www.secg.org/sec1-v2.pdf

  :param curve: Elliptic curve type to generate
  :type curve: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurve
  :param bytes compressed_point: Encoded compressed elliptic curve point
  :returns: EllipticCurvePublicNumbers instance generated from compressed point and curve
  :rtype: cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicNumbers
  """
  x, y = _ecc_decode_compressed_point(curve, compressed_point)
  return ec.EllipticCurvePublicNumbers(x=x, y=y, curve=curve)