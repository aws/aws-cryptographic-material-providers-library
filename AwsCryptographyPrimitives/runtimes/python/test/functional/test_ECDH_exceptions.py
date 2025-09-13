# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This file asserts properties about the exceptions
pyca raises for different public keys.

These assertions provide evidence
that pyca (in particular, OpenSSL backend)
raises a particular exception for one "infinity" public key
that it does not raise for other public keys.

These demonstrate that the "infinity" exception is not raised
for neither noncanonical infinity public keys
nor for other "short" keys.

These findings validate that the MPL
will correctly detect an "infinity" public key
and will fail to load an "infinity" public key
from a DER encoding.

This test suite is solely intended
to document and validate the expected behavior from pyca
in a particularly sensitive failure case
where the MPL should understand failure modes.

This test suite is NOT intended to require
that pyca should continue to raise these exceptions.
If the behavior from pyca changes,
we should first understand why the behavior changed,
then update the test suite if needed.
"""
import pytest
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import SECP256R1
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    load_der_public_key,
)
from pyasn1.codec.der.decoder import decode as der_decode
from pyasn1.codec.der.encoder import encode as der_encode
from pyasn1.type.univ import BitString, Sequence

# This exception string is raised when pyca cannot load the DER-encoded public key.
GENERIC_EXCEPTION_STRING = "Invalid key"
# This exception string appears to be raised ONLY for the invalid public key for the point at infinity.
INF_EXCEPTION_STRING = "Cannot load an EC public key where the point is at infinity"

def get_valid_der_components():
    """
    Generates a random valid public key,
    DER-encodes it,
    decodes it into an ASN.1 sequence,
    and returns the two items in the ASN.1 sequence as a tuple.
    The two items are (the ASN.1 encoded algorithm info, the ASN.1 encoded public key point).
    """
    private_key = ec.generate_private_key(
        SECP256R1
    )
    public_key_der = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
    alg_info_seq, _ = der_decode(public_key_der, asn1Spec=Sequence())
    return alg_info_seq.getComponentByPosition(0), alg_info_seq.getComponentByPosition(1)

def test_GIVEN_valid_seq_WHEN_load_der_public_key_THEN_no_exception():
    """Asserts that our ASN.1 sequence construction procedure CAN produce a valid DER public key."""
    # Given: Valid DER-encoded ASN.1 sequence represesenting a valid public key
    valid_alg_info, valid_point = get_valid_der_components()
    seq = Sequence()
    seq.setComponentByPosition(0, valid_alg_info)
    seq.setComponentByPosition(1, valid_point)
    der_seq = der_encode(seq)

    # When: load_der_public_key
    load_der_public_key(der_seq)
    # Then: No exception

def test_GIVEN_invalid_key_WHEN_load_der_public_key_THEN_generic_exception():
    """
    Asserts that our ASN.1 sequence construction procedure CAN produce an invalid DER public key,
    and that a "generic" invalid DER public key raises the "generic" exception.
    """
    # Given: Valid DER-encoded ASN.1 sequence representing an invalid public key
    valid_alg_info, valid_point = get_valid_der_components()
    # This isn't a valid point for a number of reasons
    invalid_point = BitString.fromOctetString(b"\xbe" * len(valid_point))
    seq = Sequence()
    seq.setComponentByPosition(0, valid_alg_info)
    seq.setComponentByPosition(1, invalid_point)
    der_seq = der_encode(seq)

    # Then: raises ValueError
    with pytest.raises(ValueError) as e:
        # When: load_der_public_key
        load_der_public_key(der_seq)

    # Then: exception is the generic exception and not the infinity key exception
    assert GENERIC_EXCEPTION_STRING in str(e.value)
    assert INF_EXCEPTION_STRING not in str(e.value)

def test_GIVEN_canonical_infinity_key_WHEN_load_der_public_key_THEN_special_exception():
    """
    Asserts that for the canonical "infinity" public key,
    defined as one byte of 0s,
    pyca raises a special exception type.
    """
    # Given: Valid DER-encoded ASN.1 sequence representing the canonical "infinity" invalid public key
    valid_alg_info, _ = get_valid_der_components()
    # Canonical invalid point is 1 byte of 0s
    invalid_point = BitString.fromOctetString(b"\x00")
    seq = Sequence()
    seq.setComponentByPosition(0, valid_alg_info)
    seq.setComponentByPosition(1, invalid_point)
    der_seq = der_encode(seq)

    # Then: raises ValueError
    with pytest.raises(ValueError) as e:
        # When: load_der_public_key
        load_der_public_key(der_seq)

     # Then: exception is the infinity key exception and not the generic key exception
    assert GENERIC_EXCEPTION_STRING not in str(e.value)
    assert INF_EXCEPTION_STRING in str(e.value)

def test_GIVEN_noncanonical_infinity_key_WHEN_load_der_public_key_THEN_generic_exception():
    """
    Asserts that for non-canonical "infinity" public key,
    defined as >1 byte of 0s,
    pyca raises the generic exception type.

    These are still invalid "infinity" public keys
    because the encoded point is still 0,
    but the exception message is different
    than the one for the canonical key.

    This validates that the "infinity" exception is only raised
    for the canonical infinity public key.
    """
    # Given: Valid DER-encoded ASN.1 sequence representing a non-canonical "infinity" invalid public key
    valid_alg_info, _ = get_valid_der_components()
    # Noncanonical, but still invalid points are >=2 bytes of 0s
    for i in range(2, 10):
        invalid_point = BitString.fromOctetString(b"\x00" * i)
        seq = Sequence()
        seq.setComponentByPosition(0, valid_alg_info)
        seq.setComponentByPosition(1, invalid_point)
        der_seq = der_encode(seq)

        # Then: raises ValueError
        with pytest.raises(ValueError) as e:
            # When: load_der_public_key
            load_der_public_key(der_seq)

    # Then: exception is the generic exception and not the infinity key exception
    assert GENERIC_EXCEPTION_STRING in str(e.value)
    assert INF_EXCEPTION_STRING not in str(e.value)

def test_GIVEN_some_short_non_infinity_keys_WHEN_load_der_public_key_THEN_generic_exception():
    """
    Asserts that points from 0x01 - 0xFF also fail with a generic exception,
    and not the "infinity" exception.
    
    This validates that the "infinity" exception
    is not raised for other "short" public keys,
    and is thus not a "short"/"decoding failure" exception.
    """
    # Given: Valid DER-encoded ASN.1 sequence representing invalid public keys
    valid_alg_info, _ = get_valid_der_components()
    # Given: "short" invalid public keys from 0x01 - 0xFF
    bytes_to_test = [bytes([num]) for num in range(1, 256)]
    for bytes_under_test in bytes_to_test:
        invalid_point = BitString.fromOctetString(bytes_under_test)
        seq = Sequence()
        seq.setComponentByPosition(0, valid_alg_info)
        seq.setComponentByPosition(1, invalid_point)
        der_seq = der_encode(seq)

        # Then: raises ValueError
        with pytest.raises(ValueError) as e:
            # When: load_der_public_key
            load_der_public_key(der_seq)

    # Then: exception is the generic exception and not the infinity key exception
    assert GENERIC_EXCEPTION_STRING in str(e.value)
    assert INF_EXCEPTION_STRING not in str(e.value)
