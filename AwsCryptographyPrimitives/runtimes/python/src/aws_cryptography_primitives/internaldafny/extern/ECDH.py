import standard_library.internaldafny.generated.Wrappers as Wrappers
from enum import Enum

from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import AwsCryptographicPrimitivesError
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import _smithy_error_to_dafny_error
from aws_cryptography_primitives.internaldafny.generated.ECDH import default__
CreateExternDerivesharedSecretSuccess = default__.CreateExternDerivesharedSecretSuccess
CreateExternDerivesharedSecretError = default__.CreateExternDerivesharedSecretError
CreateExternEccKeyGenFailure = default__.CreateExternEccKeyGenFailure
CreateExternEccKeyGenSuccess = default__.CreateExternEccKeyGenSuccess
CreateExternParsePublicKeySuccess = default__.CreateExternParsePublicKeySuccess
CreateExternGetPublicKeyFromPrivateError = default__.CreateExternGetPublicKeyFromPrivateError
CreateExternValidatePublicKeyError = default__.CreateExternValidatePublicKeyError
CreateExternValidatePublicKeySuccess = default__.CreateExternValidatePublicKeySuccess
CreateExternCompressPublicKeySuccess = default__.CreateExternCompressPublicKeySuccess
CreateExternDecompressPublicKeyError = default__.CreateExternDecompressPublicKeyError
CreateExternDecompressPublicKeySuccess = default__.CreateExternDecompressPublicKeySuccess
CreateGetInfinityPublicKeyError = default__.CreateGetInfinityPublicKeyError
CreateGetInfinityPublicKeySuccess = default__.CreateGetInfinityPublicKeySuccess

import ecdsa

import cryptography.hazmat.primitives.asymmetric.ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import (
  NoEncryption,
  Encoding,
  PrivateFormat,
  PublicFormat,
  load_pem_private_key,
  load_der_public_key,
)
from cryptography.hazmat.primitives.asymmetric import ec
import _dafny

from cryptography.hazmat.primitives.asymmetric.ec import (
  SECP256R1,
  SECP384R1,
  EllipticCurvePublicNumbers,
)

from aws_cryptography_primitives.internaldafny.extern.Signature import (
    _ecc_encode_compressed_point,
    _ecc_decode_compressed_point,
    _int_to_bytes,
)


from aws_cryptography_primitives.internaldafny.generated.ECDH import (
    EccKeyPair_EccKeyPair,
)

from cryptography.hazmat.primitives.serialization import PublicFormat

from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey



        
from pyasn1.type import univ, namedtype
from pyasn1.codec.der.encoder import encode as der_encoder
from pyasn1.codec.der.decoder import decode as der_decoder

INF_PUBLIC_KEY_DER =  b"-----BEGIN PUBLIC KEY-----\n" \
                   b"MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n" \
                   b"AAAAAAAAAAAAAAAAAAAAAAAAAA==\n" \
                   b"-----END PUBLIC KEY-----\n" 

curve_mapping = {
    "secp256r1": ecdsa.curves.NIST256p,
    "secp384r1": ecdsa.curves.NIST384p,
    "secp521r1": ecdsa.curves.NIST521p
}

# Define the ASN.1 structure for an EC public key
class ECPublicKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('algorithm', univ.ObjectIdentifier()),
        namedtype.NamedType('publicKey', univ.BitString())
    )


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
  # key_size is in bits. Convert to bytes and round up
#   byte_length = (private_key.curve.key_size + 7) // 8
#   public_numbers = private_key.public_key().public_numbers()
  public_numbers = public_key.public_numbers()
  byte_length = (public_key.curve.key_size + 7) // 8
  y_map = [b"\x02", b"\x03"]
  # If curve in prime field.
  if public_key.curve.name.startswith("secp"):
    y_order = public_numbers.y % 2
    y = y_map[y_order]
  else:
    raise NotImplementedError("Non-prime curves are not supported at this time")
  return y + _int_to_bytes(public_numbers.x, byte_length)

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
            return CreateExternDerivesharedSecretError(
                maybe_ecc_algorithm.error
            )
        
        if maybe_ecc_algorithm.value.name != "SM2PKE": # ?? magic string? what?
            #try:
            private_key = load_pem_private_key(private_key_pem_bytes, None)
            public_key = load_der_public_key(public_key_der_bytes)

            shared_key = private_key.exchange(
                ec.ECDH(),
                public_key
            )

            return CreateExternDerivesharedSecretSuccess(
                _dafny.Seq(
                    shared_key
                )
            )
            # except Exception as e:
            #     return CreateExternDerivesharedSecretError(
            #         _smithy_error_to_dafny_error(
            #             AwsCryptographicPrimitivesError(
            #                 e
            #             )
            #         )
            #     )
        else:
            return CreateExternDerivesharedSecretError(
                _smithy_error_to_dafny_error(
                    ValueError(
                        "SM2 not yet supported."
                    )
                )
            )
        
def validate_point(curve, x, y):
    # Get curve parameters
    a = curve.a()
    b = curve.b()
    p = curve.p()

    # Check if point is within the field range
    if not (0 <= x < p and 0 <= y < p):
        return False

    # Check if the point satisfies the elliptic curve equation
    left = (y * y) % p
    right = (x * x * x + a * x + b) % p
    return left == right


class KeyGeneration:
    ELLIPTIC_CURVE_ALGORITHM = "EC"
    SEC_PRIME_FIELD_PREFIX = "secp"
    SEC_P256 = "256r1"
    SEC_P384 = "384r1"
    SEC_P521 = "521r1"
    SM2_KA = "SM2"

    @staticmethod
    def GenerateKeyPair(dafny_eccAlgorithm) -> Wrappers.Result:
        # TODO: any crypto provider checking? ala java `checkBCProvider`
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateExternEccKeyGenFailure(
                maybe_ecc_algorithm.error
            )
        
        try:
            private_key = ec.generate_private_key(
                maybe_ecc_algorithm.value.value
            )

            private_key_pem_bytes = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
            public_key_der_bytes = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

            return CreateExternEccKeyGenSuccess(EccKeyPair_EccKeyPair(
                publicKey=_dafny.Seq(public_key_der_bytes),
                privateKey=_dafny.Seq(private_key_pem_bytes)
            ))
        except Exception as e:
            return CreateExternEccKeyGenFailure(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        e
                    )
                )
            )


class ECCUtils:
    
    def ParsePublicKey(dafny_publicKey: _dafny.Seq) -> Wrappers.Result:
        # TODO: check crypto provider?
        public_key_bytes = bytes(dafny_publicKey)
        public_key = load_der_public_key(public_key_bytes)
        public_bytes = public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

        return CreateExternParsePublicKeySuccess(
            _dafny.Seq(
                public_bytes
            )
        )
    
    def GetPublicKey(dafny_eccAlgorithm, dafny_privateKey):
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateExternGetPublicKeyFromPrivateError(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value

        if curve.name != "SM2PKE": # magic string?
            try:
                # get order for parsed private key
                private_key_pem = bytes(dafny_privateKey.pem)
                private_key = load_pem_private_key(private_key_pem, None)
                private_key_curve = curve_mapping[private_key.curve.name]
                private_key_order = private_key_curve.order

                # get expected curve order
                ecdsa_curve = curve_mapping[curve.name]
                curve_order = ecdsa_curve.order

                if private_key_order != curve_order:
                    return CreateExternGetPublicKeyFromPrivateError(
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
                return CreateExternGetPublicKeyFromPrivateError(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            e
                        )
                    )
                )
        
    def ValidatePublicKey(dafny_eccAlgorithm, dafny_publicKey):
        # TODO: check crypto provider?
        public_key_bytes = bytes(dafny_publicKey)

        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateExternValidatePublicKeyError(
                maybe_ecc_algorithm.error
            )
        
        curve = maybe_ecc_algorithm.value
        
        if curve.name != "SM2": # ?? magic string? what?
            try:
                print(f"{public_key_bytes=}")
                if not ECCUtils.ValidatePublicKeyIsNotInfinityDER(public_key_bytes):
                # if not ECCUtils.ValidatePublicKeyIsNotInfinity(public_key.public_numbers()):
                    return CreateExternValidatePublicKeyError(
                        _smithy_error_to_dafny_error(
                            AwsCryptographicPrimitivesError(
                                message="Provided public key is the point at infinity."
                            )
                        )
                    )
        
                print("loading public key")
                public_key = load_der_public_key(public_key_bytes)
                public_key_curve_name = public_key.curve.name
                if not (public_key_curve_name == curve.name):
                    return CreateExternValidatePublicKeyError(
                        _smithy_error_to_dafny_error(
                            AwsCryptographicPrimitivesError(
                                message="Provided public key is not on configured curve."
                            )
                        )
                    )

                valid_public_key = ECCUtils.NistPublicKeyValidationCriteria(public_key)
                
                return CreateExternValidatePublicKeySuccess(
                    valid_public_key
                )
            except Exception as e:
                print(e)
                print(type(e))
                return CreateExternValidatePublicKeyError(
                    _smithy_error_to_dafny_error(
                        AwsCryptographicPrimitivesError(
                            message=str(e)
                        )
                    )
                )
        
    def NistPublicKeyValidationCriteria(public_key):
        public_numbers = public_key.public_numbers()
        pyca_curve_name = public_key.curve.name
        ecdsa_curve = curve_mapping[pyca_curve_name]
        validate_point(ecdsa_curve.curve, public_numbers.x, public_numbers.y)
        return (
            ECCUtils.ValidatePublicKeyIsNotInfinity(public_numbers) and
            ECCUtils.CoordinateBetween0AndP(public_numbers.x, ecdsa_curve) and
            ECCUtils.CoordinateBetween0AndP(public_numbers.y, ecdsa_curve)
        )
    
    def ValidatePublicKeyIsNotInfinity(point):
        return not (point.x == 0 and point.y == 0)
    
    def ValidatePublicKeyIsNotInfinityDER(key):
        return key != INF_PUBLIC_KEY_DER
    
    def CoordinateBetween0AndP(coordinate, curve):
        return (
            coordinate > 0 and
            coordinate < curve.curve.p()
        )
    
    def CompressPublicKey(dafny_publicKeyDerBytes, dafny_eccAlgorithm):
        public_key_bytes = bytes(dafny_publicKeyDerBytes)
        public_key = load_der_public_key(public_key_bytes)
        compressed_public_key = _ecc_encode_compressed_point_public_key(public_key)
        return CreateExternCompressPublicKeySuccess(
            _dafny.Seq(
                compressed_public_key
            )
        )
        

    def DecompressPublicKey(dafny_compressedPublicKey, dafny_eccAlgorithm):
        # todo: check crypto provider

        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateExternDecompressPublicKeyError(
                maybe_ecc_algorithm.error
            )
        compressed_public_key_bytes = bytes(dafny_compressedPublicKey)
        curve = maybe_ecc_algorithm.value

        x, y = _ecc_decode_compressed_point(curve, compressed_public_key_bytes)
        public_numbers = ec.EllipticCurvePublicNumbers(x=x, y=y, curve=curve.value)
        public_key = public_numbers.public_key(backend=default_backend())
        # public_key = EllipticCurvePublicKey.from_encoded_point(curve, compressed_public_key_bytes)

        return CreateExternDecompressPublicKeySuccess(
            _dafny.Seq(
                public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
            )
        )
    
    # We should've made this a test-only extern
    def GetInfinityPublicKey(dafny_eccAlgorithm):
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateGetInfinityPublicKeyError(
                maybe_ecc_algorithm.error
            )
        
        # curve = maybe_ecc_algorithm.value
        
        # public_key_der = ec.generate_private_key(
        #     curve.value
        # ).public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

        # asn1_public_key_der =


        inf_public_numbers = EllipticCurvePublicNumbers(x=0, y=0, curve=ec.SECP256R1())
        # public_key = inf_public_numbers.public_key(backend=default_backend())

        # Manually create the ASN.1 encoded public key
        from pyasn1.type.univ import Sequence, BitString, ObjectIdentifier
        from pyasn1.codec.der.encoder import encode as der_encode
        from pyasn1.codec.der.decoder import decode as der_decode

        # generate a random public/private key
        private_key = ec.generate_private_key(
            maybe_ecc_algorithm.value.value
        )
        public_key_der = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
        public_key_point_bytes = private_key.public_key().public_bytes(Encoding.X962, PublicFormat.UncompressedPoint)
        # input(f"{public_key_point_bytes=}")
        # input(f"{len(public_key_point_bytes)=}")
        inf_public_key_point_bytes = b"\x00"
        # input(f"{inf_public_key_point_bytes=}")
        # input(f"{len(inf_public_key_point_bytes)=}")
        alg_info_seq, _ = der_decode(public_key_der, asn1Spec=Sequence())
        # input(f"{alg_info_seq.getComponentByPosition(0)=}")
        # input(f"{alg_info_seq.getComponentByPosition(1)=}")
        alg_info = alg_info_seq.getComponentByPosition(0)
        input(f"{alg_info=}")
        # Build a pub key with the point at infinity defined as a 1 byte zero array

        # generate random point on curve
        import os
        curve = private_key.curve
        field_size = curve.key_size // 8
        random_x = int.from_bytes(os.urandom(field_size), byteorder='big')
        random_y = int.from_bytes(os.urandom(field_size), byteorder='big')
        random_x = random_x % (1 << field_size * 8)
        random_y = random_y % (1 << field_size * 8)
        random_point_bytes = b'\x04' + random_x.to_bytes(field_size, byteorder='big') + random_y.to_bytes(field_size, byteorder='big')
        random_point_bitstring = BitString.fromOctetString(inf_public_key_point_bytes)

        
        point_at_infinity = der_encode(BitString.fromOctetString(b'\x00'))
        enc_point = BitString.fromOctetString(point_at_infinity)
        input(f"{point_at_infinity=}")
        seq = Sequence()
        seq.setComponentByPosition(0, alg_info)
        seq.setComponentByPosition(1, enc_point)
        # input(f"{seq.getComponentByPosition(0)=}")
        # input(f"{seq.getComponentByPosition(1)=}")
        # input(f"{der_encode(seq)=}")
        # input(f"orig {public_key_der=}")
        # return der_encode(seq)

    

        # ec_public_key_info = Sequence()
        # ec_public_key_info.setComponentByPosition(0, ObjectIdentifier('1.2.840.10045.2.1'))  # id-ecPublicKey
        # # todo others?
        # ec_public_key_info.setComponentByPosition(1, ObjectIdentifier('1.2.840.10045.3.1.7'))  # prime256v1 (SECP256R1)
        # ec_point_bitstring = BitString.fromOctetString(b'\x01' * 32 + b'\x01' * 32)
        # ec_public_key_sequence = Sequence()
        # ec_public_key_sequence.setComponentByPosition(0, ec_public_key_info)
        # ec_public_key_sequence.setComponentByPosition(1, ec_point_bitstring)

        # import binascii
        # public_key_bitstring = univ.BitString("'00000000'H")

        # # Define the OID for the EC public key
        # oid_ec_public_key = univ.ObjectIdentifier('1.2.840.10045.2.1')

        # asn1_public_key = ECPublicKey()
        # asn1_public_key.setComponentByName('algorithm', oid_ec_public_key)
        # asn1_public_key.setComponentByName('publicKey', univ.BitString(public_key_bitstring))
                
        # # Encode the ASN.1 structure to DER
        # encoded_public_key = der_encoder(asn1_public_key)     

        # key = INF_PUBLIC_KEY_DER
        
        print("inf")
          
        return CreateGetInfinityPublicKeySuccess(
            _dafny.Seq(
                der_encode(seq)
            )
        )
    
    def GetOutOfBoundsPublicKey(dafny_curve):
        return Wrappers.Result_Success(b"todo")


class CustomECCAlgorithm(cryptography.hazmat.primitives.asymmetric.ec.EllipticCurve):
    def __init__(self, name, key_size):
        self.name = name
        self.key_size = key_size

    def name(self):
        return self.name
    
    def key_size(self):
        return self.key_size
        
class ECCAlgorithms(Enum):
    import cryptography.hazmat.primitives.asymmetric.ec
    secp256r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP256R1()
    secp384r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP384R1()
    secp521r1 = cryptography.hazmat.primitives.asymmetric.ec.SECP521R1()

    # secp256r1 = ECCAlgorithm(KeyGeneration.SEC_PRIME_FIELD_PREFIX + KeyGeneration.SEC_P256)
    # secp384r1 = ECCAlgorithm(KeyGeneration.SEC_PRIME_FIELD_PREFIX + KeyGeneration.SEC_P384)
    # secp521r1 = ECCAlgorithm(KeyGeneration.SEC_PRIME_FIELD_PREFIX + KeyGeneration.SEC_P521)
    SM2 = CustomECCAlgorithm(name=KeyGeneration.SM2_KA, key_size=-1)


    @staticmethod
    def eccAlgorithm(dafny_eccAlgorithm) -> Wrappers.Result:
        if dafny_eccAlgorithm.is_ECC__NIST__P256:
            named_curve_algorithm = ECCAlgorithms.secp256r1
        elif dafny_eccAlgorithm.is_ECC__NIST__P384:
            named_curve_algorithm = ECCAlgorithms.secp384r1
        elif dafny_eccAlgorithm.is_ECC__NIST__P521:
            named_curve_algorithm = ECCAlgorithms.secp521r1
        elif dafny_eccAlgorithm.is_SM2:
            named_curve_algorithm = ECCAlgorithms.SM2
        else:
            return Wrappers.Result_Failure(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message = f"Requested Curve is not supported. Requested {dafny_eccAlgorithm}"
                    )
                )
            )
        return Wrappers.Result_Success(named_curve_algorithm)

import aws_cryptography_primitives.internaldafny.generated.ECDH

class dummyclass:
    pass

aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH = dummyclass
# TODO; extern name bad
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.DeriveSharedSecret = DeriveSharedSecret
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.DeriveSharedSecret = DeriveSharedSecret
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.KeyGeneration = KeyGeneration
aws_cryptography_primitives.internaldafny.generated.ECDH.ECDH.ECCUtils = ECCUtils
aws_cryptography_primitives.internaldafny.generated.ECDH.ECCUtils = ECCUtils