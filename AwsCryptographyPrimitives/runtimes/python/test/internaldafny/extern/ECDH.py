# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from aws_cryptography_primitives.internaldafny.extern.ECDH import (
    ECCAlgorithms,
    ECCUtils as src_ECCUtils,
)

from aws_cryptography_primitives.internaldafny.generated.ECDH import default__

CreateGetInfinityPublicKeyError = default__.CreateGetInfinityPublicKeyError
CreateGetInfinityPublicKeySuccess = default__.CreateGetInfinityPublicKeySuccess
CreateGetOutOfBoundsPublicKeyError = default__.CreateGetOutOfBoundsPublicKeyError
CreateGetOutOfBoundsPublicKeySuccess = default__.CreateGetOutOfBoundsPublicKeySuccess

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (Encoding,PublicFormat)
import _dafny
from aws_cryptography_primitives.smithygenerated.aws_cryptography_primitives.errors import (
    AwsCryptographicPrimitivesError,
    _smithy_error_to_dafny_error
)

# Extend src extern with test utilities
class ECCUtils(src_ECCUtils):

    def GetInfinityPublicKey(dafny_eccAlgorithm):
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateGetInfinityPublicKeyError(
                maybe_ecc_algorithm.error
            )
        
        try:
            # manually create the ASN.1 encoded public key
            from pyasn1.codec.der.decoder import decode as der_decode
            from pyasn1.codec.der.encoder import encode as der_encode
            from pyasn1.type.univ import BitString, Sequence

            # generate a random public/private key to get valid alg_info
            private_key = ec.generate_private_key(
                maybe_ecc_algorithm.value.value
            )
            public_key_der = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

            alg_info_seq, _ = der_decode(public_key_der, asn1Spec=Sequence())
            alg_info = alg_info_seq.getComponentByPosition(0)
            
            # inf point defined as 1 byte of 0s
            point_at_infinity = BitString.fromOctetString(b'\x00')

            seq = Sequence()
            seq.setComponentByPosition(0, alg_info)
            seq.setComponentByPosition(1, point_at_infinity)

            return CreateGetInfinityPublicKeySuccess(
                _dafny.Seq(
                    der_encode(seq)
                )
            )
        except Exception as e:
            return CreateGetInfinityPublicKeyError(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message=str(e)
                    )
                )
            )
    
    def GetOutOfBoundsPublicKey(dafny_eccAlgorithm):
        maybe_ecc_algorithm = ECCAlgorithms.eccAlgorithm(dafny_eccAlgorithm)
        if maybe_ecc_algorithm.is_Failure:
            return CreateGetInfinityPublicKeyError(
                maybe_ecc_algorithm.error
            )
        
        try:
            curve = maybe_ecc_algorithm.value
            
            # Manually create the ASN.1 encoded public key
            from pyasn1.codec.der.decoder import decode as der_decode
            from pyasn1.codec.der.encoder import encode as der_encode
            from pyasn1.type.univ import BitString, ObjectIdentifier, Sequence

            # generate a random public/private key to get valid alg_info
            private_key = ec.generate_private_key(
                maybe_ecc_algorithm.value.value
            )
            public_key_der = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

            alg_info_seq, _ = der_decode(public_key_der, asn1Spec=Sequence())
            alg_info = alg_info_seq.getComponentByPosition(0)

            length = src_ECCUtils.CURVE_TO_ECC_SECRET_LENGTH_MAP[curve.name]

            # one possible out of bounds point
            out_of_bounds_point = b'\x04' + (b'\xFF' * (2 * length))
            
            point_at_infinity = BitString.fromOctetString(out_of_bounds_point)

            seq = Sequence()
            seq.setComponentByPosition(0, alg_info)
            seq.setComponentByPosition(1, point_at_infinity)

            return CreateGetOutOfBoundsPublicKeySuccess(
                _dafny.Seq(
                    der_encode(seq)
                )
            )
        except Exception as e:
            return CreateGetOutOfBoundsPublicKeyError(
                _smithy_error_to_dafny_error(
                    AwsCryptographicPrimitivesError(
                        message=str(e)
                    )
                )
            )
    
import aws_cryptography_primitives
# Export extended extern to the src extern.
# This will ONLY be exported if the test is loaded,
# which does not happen as part of regular operation.
aws_cryptography_primitives.internaldafny.extern.ECDH.ECCUtils = ECCUtils
aws_cryptography_primitives.internaldafny.generated.ECDH.ECCUtils = ECCUtils
