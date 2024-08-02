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
            # Remember when we did a performance test,
            # and realized that our Dafny implementation
            # requires the extern to turn PEM bytes
            # into a private key on every invocation
            # for the raw RSA private key?
            # Same issue here.
            # TODO: Refactor Dafny impl.
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
        # would be cool if this cached public key

        # TODO: check crypto provider?
        public_key_bytes = bytes(dafny_publicKey)
        public_key = load_der_public_key(public_key_bytes)
        public_bytes = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)

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
        

        if maybe_ecc_algorithm.value.name != "SM2PKE": # ?? magic string? what?
            # try:
            private_key_pem = bytes(dafny_privateKey.pem)
            private_key = load_pem_private_key(private_key_pem, None)
            public_key = private_key.public_key()
            public_key_der = public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)


            return Wrappers.Result_Success(
                _dafny.Seq(
                    public_key_der
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
        
        if maybe_ecc_algorithm.value.name != "SM2": # ?? magic string? what?
            # try:
            valid_public_key = ECCUtils.NistPublicKeyValidationCriteria(public_key_bytes)
            
            return CreateExternValidatePublicKeySuccess(
                valid_public_key
            )
        
    def NistPublicKeyValidationCriteria(public_key_bytes):
        # todo
        return True
    
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
        
        public_key_bytes = bytes(dafny_publicKeyDerBytes)
        public_key = load_pem_public_key(public_key_bytes)
        compressed_public_key = _ecc_encode_compressed_point_public_key(public_key)
        return CreateExternCompressPublicKeySuccess(
            _dafny.Seq(
                compressed_public_key
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
        
        # Manually create the ASN.1 encoded public key
        import binascii
        public_key_bitstring = univ.BitString("'00000000'H")

        # Define the OID for the EC public key
        oid_ec_public_key = univ.ObjectIdentifier('1.2.840.10045.2.1')

        asn1_public_key = ECPublicKey()
        asn1_public_key.setComponentByName('algorithm', oid_ec_public_key)
        asn1_public_key.setComponentByName('publicKey', univ.BitString(public_key_bitstring))
                
        # Encode the ASN.1 structure to DER
        encoded_public_key = der_encoder(asn1_public_key)      
          
        return CreateGetInfinityPublicKeySuccess(
            _dafny.Seq(
                encoded_public_key
            )
        )





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