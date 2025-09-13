# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from enum import Enum

import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from aws_cryptography_primitives.internaldafny.generated.ECDH import default__
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import (
    AwsCryptographicPrimitivesError,
    _smithy_error_to_dafny_error
)

import _dafny
import cryptography.hazmat.primitives.asymmetric.ec
from aws_cryptography_primitives.internaldafny.extern.Signature import (
    _ecc_decode_compressed_point,
    _ecc_encode_compressed_point_public_key,
)

from aws_cryptography_primitives.internaldafny.generated.ECDH import \
    EccKeyPair_EccKeyPair
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.serialization import (Encoding,
                                                          NoEncryption,
                                                          PrivateFormat,
                                                          PublicFormat,
                                                          load_der_public_key,
                                                          load_pem_private_key)

from aws_cryptography_primitives.internaldafny.extern.Signature import \
    _ECC_CURVE_PARAMETERS


curve_mapping = {
    "secp256r1": _ECC_CURVE_PARAMETERS["secp256r1"],
    "secp384r1": _ECC_CURVE_PARAMETERS["secp384r1"],
    "secp521r1": _ECC_CURVE_PARAMETERS["secp521r1"],
}

def _validate_point(curve, x, y):
    """
    Validate that the coordinates x, y:
    - lie within the elliptic curve field
    - satisfy the elliptic curve equation
    """
    # Get curve parameters
    a = curve.a
    b = curve.b
    p = curve.p

    # Check if point is within the field range
    if not (0 <= x < p and 0 <= y < p):
        return False

    # Check if the point satisfies the elliptic curve equation
    left = (y * y) % p
    right = (x * x * x + a * x + b) % p
    return left == right


class DeriveSharedSecret:
    def CalculateSharedSecret(
        dafny_eccAlgorithm,
        dafny_privateKey,
        dafny_publicKey,
    ) -> Wrappers.Result:
        public_key_der_bytes = bytes(dafny_publicKey.der)
        private_key_pem_bytes = bytes(dafny_privateKey.pem)

        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return default__.CreateExternDerivesharedSecretError(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value
        
        if curve.name != "SM2":
            try:
                private_key = load_pem_private_key(private_key_pem_bytes, None)
                public_key = load_der_public_key(public_key_der_bytes)

                shared_key = private_key.exchange(
                    ec.ECDH(),
                    public_key
                )

                return default__.CreateExternDerivesharedSecretSuccess(
                    _dafny.Seq(
                        shared_key
                    )
                )
            except Exception as e:
                return default__.CreateExternDerivesharedSecretError(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            message=str(e)
                        )
                    )
                )
        else:
            return default__.CreateExternDerivesharedSecretError(
                _smithy_error_to_dafny_error(
                    ValueError(
                        "SM2 not yet supported."
                    )
                )
            )

class KeyGeneration:
    
    @staticmethod
    def GenerateKeyPair(dafny_eccAlgorithm) -> Wrappers.Result:
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return default__.CreateExternEccKeyGenFailure(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value

        if curve.name != "SM2":
            try:
                private_key = ec.generate_private_key(
                    maybe_ecc_algorithm.value.value
                )

                private_key_pem_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
                public_key_der_bytes = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

                return default__.CreateExternEccKeyGenSuccess(EccKeyPair_EccKeyPair(
                    publicKey=_dafny.Seq(public_key_der_bytes),
                    privateKey=_dafny.Seq(private_key_pem_bytes)
                ))
            except Exception as e:
                return default__.CreateExternEccKeyGenFailure(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            message=str(e)
                        )
                    )
                )
        else:
            return default__.CreateExternEccKeyGenFailure(
                    _smithy_error_to_dafny_error(
                        ValueError(
                            "SM2 not supported."
                        )
                    )
                )


class ECCUtils:

    CURVE_TO_ECC_SECRET_LENGTH_MAP = {
        "secp256r1": int(256 / 8),
        "secp384r1": int(384 / 8),
        "secp521r1": int(521 / 8 + 1) # 521/8 is not a whole number
    }
    
    def ParsePublicKey(dafny_publicKey: _dafny.Seq) -> Wrappers.Result:
        try:
            public_key_bytes = bytes(dafny_publicKey)
            public_key = load_der_public_key(public_key_bytes)
            public_bytes = public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

            return default__.CreateExternParsePublicKeySuccess(
                _dafny.Seq(
                    public_bytes
                )
            )
        except Exception as e:
            return default__.CreateExternParsePublicKeyError(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message=str(e)
                    )
                )
            )
    
    def GetPublicKey(dafny_eccAlgorithm, dafny_privateKey):
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return default__.CreateExternGetPublicKeyFromPrivateError(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value

        if curve.name != "SM2": 
            try:
                # get order for parsed private key
                private_key_pem = bytes(dafny_privateKey.pem)
                private_key = load_pem_private_key(private_key_pem, None)
                private_key_curve = curve_mapping[private_key.curve.name]
                private_key_order = private_key_curve.order

                # get expected curve order
                ecdh_curve = curve_mapping[curve.name]
                curve_order = ecdh_curve.order

                if private_key_order != curve_order:
                    return default__.CreateExternGetPublicKeyFromPrivateError(
                        _smithy_error_to_dafny_error(
                            AwsCryptographicPrimitivesError(
                                message="Private Key NOT on configured curve spec."
                            )
                        )
                    )

                public_key = private_key.public_key()
                public_key_der = public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

                return Wrappers.Result_Success(
                    _dafny.Seq(
                        public_key_der
                    )
                )
            except Exception as e:
                return default__.CreateExternGetPublicKeyFromPrivateError(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            message=str(e)
                        )
                    )
                )
        else:
            return default__.CreateExternEccKeyGenFailure(
                    _smithy_error_to_dafny_error(
                        ValueError(
                            "SM2 not supported."
                        )
                    )
                )

        
    def ValidatePublicKey(dafny_eccAlgorithm, dafny_publicKey):
        public_key_bytes = bytes(dafny_publicKey)

        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return default__.CreateExternValidatePublicKeyError(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value
        
        if curve.name != "SM2":
            try:
                public_key = load_der_public_key(public_key_bytes)
                public_key_curve_name = public_key.curve.name
                if not (public_key_curve_name == curve.name):
                    return default__.CreateExternValidatePublicKeyError(
                        _smithy_error_to_dafny_error(
                            AwsCryptographicPrimitivesError(
                                message="Provided public key is not on configured curve."
                            )
                        )
                    )

                valid_public_key = ECCUtils.NistPublicKeyValidationCriteria(public_key)
                
                return default__.CreateExternValidatePublicKeySuccess(
                    valid_public_key
                )
            except Exception as e:
                return default__.CreateExternValidatePublicKeyError(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            message=str(e)
                        )
                    )
                )
        else:
            return default__.CreateExternValidatePublicKeyError(
                _smithy_error_to_dafny_error(
                    ValueError(
                        "SM2 Not yet Supported."
                    )
                )
            )
        
    def NistPublicKeyValidationCriteria(public_key):
        public_numbers = public_key.public_numbers()
        pyca_curve_name = public_key.curve.name
        ecdsa_curve = curve_mapping[pyca_curve_name]

        _validate_point(ecdsa_curve, public_numbers.x, public_numbers.y)
        
        return (
            ECCUtils.ValidatePublicKeyIsNotInfinity(public_numbers) and
            ECCUtils.CoordinateBetween0AndP(public_numbers.x, ecdsa_curve) and
            ECCUtils.CoordinateBetween0AndP(public_numbers.y, ecdsa_curve)
        )
    
    def ValidatePublicKeyIsNotInfinity(point):
        return not (point.x == 0 and point.y == 0)
    
    def CoordinateBetween0AndP(coordinate, curve):
        return (
            coordinate > 0 and
            coordinate < curve.p
        )
    
    def CompressPublicKey(dafny_publicKeyDerBytes, dafny_eccAlgorithm):
        try:
            public_key_bytes = bytes(dafny_publicKeyDerBytes)
            public_key = load_der_public_key(public_key_bytes)
            compressed_public_key = _ecc_encode_compressed_point_public_key(public_key)
            return default__.CreateExternCompressPublicKeySuccess(
                _dafny.Seq(
                    compressed_public_key
                )
            )
        except Exception as e:
            return default__.CreateExternCompressPublicKeyError(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message=str(e)
                    )
                )
            )

    def DecompressPublicKey(dafny_compressedPublicKey, dafny_eccAlgorithm):
        try:
            maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
            if maybe_ecc_algorithm.is_Failure:
                return default__.CreateExternDecompressPublicKeyError(
                    maybe_ecc_algorithm.error
                )

            compressed_public_key_bytes = bytes(dafny_compressedPublicKey)
            curve = maybe_ecc_algorithm.value

            x, y = _ecc_decode_compressed_point(curve, compressed_public_key_bytes)
            public_numbers = ec.EllipticCurvePublicNumbers(x=x, y=y, curve=curve.value)
            public_key = public_numbers.public_key(backend=default_backend())

            return default__.CreateExternDecompressPublicKeySuccess(
                _dafny.Seq(
                    public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
                )
            )
        except Exception as e:
            return default__.CreateExternDecompressPublicKeyError(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message=str(e)
                    )
                )
            )

class ECCAlgorithms(Enum):
    """Enum for supported ECC algorithms."""
    secp256r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP256R1()
    secp384r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP384R1()
    secp521r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP521R1()

    @staticmethod
    def eccAlgorithm(dafny_eccAlgorithm) -> Wrappers.Result:
        if dafny_eccAlgorithm.is_ECC__NIST__P256:
            named_curve_algorithm = ECCAlgorithms.secp256r1
        elif dafny_eccAlgorithm.is_ECC__NIST__P384:
            named_curve_algorithm = ECCAlgorithms.secp384r1
        elif dafny_eccAlgorithm.is_ECC__NIST__P521:
            named_curve_algorithm = ECCAlgorithms.secp521r1
        else:
            return Wrappers.Result_Failure(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message = f"Requested Curve is not supported. Requested {dafny_eccAlgorithm}"
                    )
                )
            )
        return Wrappers.Result_Success(named_curve_algorithm)


# Empty class to hold extern functions.
# This is exported to the generated class
# in a way that the generated code
# expects to access extern methods.
class ECDH_externs:
    pass

import aws_cryptography_primitives.internaldafny.generated.ECDH
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH = ECDH_externs
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.DeriveSharedSecret = DeriveSharedSecret
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.KeyGeneration = KeyGeneration
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.ECCUtils = ECCUtils
