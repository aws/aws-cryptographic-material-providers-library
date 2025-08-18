# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Fuzz Testing Generator for AWS Cryptographic Material Providers Library

This script generates fuzzed test vectors with a focused approach:
1. Fuzz encryption context fields and key-related fields (strings; since there a variety of Unicode characters that can be tested)
2. Randomly choosing and testing the "representative values" -> https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/test-vectors/test-vector-enumeration.md#selecting-a-representative-input-value
"""

import json
import uuid
import unicodedata
import warnings
import argparse
from typing import Dict, Any, List, Tuple
import hypothesis
from hypothesis import strategies as st
from hypothesis.strategies import composite
from hypothesis.errors import NonInteractiveExampleWarning

# Key identifier field names - constants to avoid magic strings
KEY_ID_FIELD = "fuzzed_key_id"
KEY_NAMESPACE_FIELD = "key_namespace"
KEY_ID_IN_MATERIAL_FIELD = "key_id_in_material"
INTERNAL_KEY_ID_FIELD = "_key_id_in_material"

# Description templates for test vectors
DESCRIPTION_TEMPLATES = {
    "raw": "Raw keyring test with Unicode fuzzing",
    "kms": "KMS keyring test with Unicode fuzzing"
}

# Key, Algorithm, Test-Type, Key-Material Definitions
KMS_KEYS = ["us-west-2-mrk", "us-east-1-mrk", "us-west-2-decryptable"] #us-west-2-rsa-mrk (already have rsa), us-west-2-256-ecc, us-west-2-384-ecc (and already have enough ecc)
RAW_KEY_TYPES = ["aes-128", "aes-192", "aes-256", "ecc-256", "ecc-384", "ecc-521"] #rsa-4096 not included because of complex interdependencies and structural requirements
KEYRING_TYPES = ["kms", "raw"]

# Key materials for raw keyrings
KEY_MATERIALS = {
    "aes-128": {"bits": 128, "material": "AAECAwQFBgcICRAREhMUFQ=="},
    "aes-192": {"bits": 192, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIj"},
    "aes-256": {"bits": 256, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIjJCUmJygpMDE="},

    # ECC key materials
    "ecc-256": {
        "bits": 256,
        "algorithm": "ecdh",
        "sender-material": "-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n-----END PRIVATE KEY-----",
        "recipient-material": "-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgYvB/1CVSgfQDrE6A\nDz7pdgxcOb+AHnsaI4LQMY6s8JChRANCAARYxf/AeERu2Z3VtDokplDs/atuGIbW\n7IGhknbK2MP+NV/mbcaxl8Xki9FegBslxCbM66KaoOZR1bCxPpGub2aS\n-----END PRIVATE KEY-----",
        "sender-public-key": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp1IMe0q5R4TyJ9zHGX3N3BCLPPlxX+yb4XLldcFhCxmfAI7sJyoxNInpRMEmOR2M1ghe+9xbyWlhmBmBoUm2vA==",
        "recipient-public-key": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWMX/wHhEbtmd1bQ6JKZQ7P2rbhiG1uyBoZJ2ytjD/jVf5m3GsZfF5IvRXoAbJcQmzOuimqDmUdWwsT6Rrm9mkg==",
        "curve": "ecc-256"
    },
    
    "ecc-384": {
        "bits": 384,
        "algorithm": "ecdh", 
        "sender-material": "-----BEGIN PRIVATE KEY-----\nMIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAx0jhFAVQX2zykSLO/\n3VvDDaQJspek3404TtDZupcxi2rThfnxh96u8CYD6XfHikehZANiAAR2W/Cc8slJ\ngYSGi3e+38UUW6dFi1mJBNEZEbJ4vljgEzBo7FecTsCOQH8Zu2nX3eQpuboD8Fb7\nARpqq7rug5jKBMQLUbvridjLBRLuFsfaLpZ07ih4/+VduqQom7D31ik=\n-----END PRIVATE KEY-----",
        "recipient-material": "-----BEGIN PRIVATE KEY-----\nMIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDALwMcT5K2IOUK5Ww5o\nqYrYLzKHuAvFs0VLuKvJOCmWa3NK2WXtUIJ2fPYzp2Y9oTShZANiAATXUn2WMiLB\nbf665ikArOEAOFgruhqAwlxy58BP42nodBZFFf4L7cy7vPLpasp3fFroN57tYfjy\nXL5Wc0vb+xJaTZLBTU/tRGvtjHH0hQgMib2ch6akUJAT6zuMgNNdd7A=\n-----END PRIVATE KEY-----",
        "sender-public-key": "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEdlvwnPLJSYGEhot3vt/FFFunRYtZiQTRGRGyeL5Y4BMwaOxXnE7AjkB/Gbtp193kKbm6A/BW+wEaaqu67oOYygTEC1G764nYywUS7hbH2i6WdO4oeP/lXbqkKJuw99Yp",
        "recipient-public-key": "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE11J9ljIiwW3+uuYpAKzhADhYK7oagMJccufAT+Np6HQWRRX+C+3Mu7zy6WrKd3xa6Dee7WH48ly+VnNL2/sSWk2SwU1P7URr7Yxx9IUIDIm9nIempFCQE+s7jIDTXXew",
        "curve": "ecc-384"
    },
    
    "ecc-521": {
        "bits": 521,
        "algorithm": "ecdh",
        "sender-material": "-----BEGIN PRIVATE KEY-----\nMIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIANn8j3pIu1wiwkz7z\niPKuqj2MEVWKe/UW/8NEtvD9tKQmMlAzwY/QN93k+0TNlXpvJTUvjI2NZDKNoQ2b\n0B44YfyhgYkDgYYABAHfgnF9LoYBRWwXKKEFQa+Xfg+ztDRdTVTqNZ8roUYmNvLL\nLz2F8oEOhDbMJZ5r1B1C9w5uJqeF6tE8a3yzm47R/wAs0k6dY3wfDKD013Wnn+6e\nNw1mtrvTi6+Pej/ukYOuCjCwm8B0AvxBzdHk8Q/nCcspO9pIsRl/I4qNz4tPaGjJ\nTA==\n-----END PRIVATE KEY-----",
        "recipient-material": "-----BEGIN PRIVATE KEY-----\nMIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIBjhdIxb49QXi4OsOH\n5PNWnp/KePiuICqC+fxJJ6ceUgPr5SMlLxhHcfHSVZBCkGLP0Rjd1D9gi7Va1oxe\nIHmWRu2hgYkDgYYABAAmg0dilFc6FiO9OE8t1el92KdPo9WYu1hXYnjGYT7OuGj3\nbD9lr0KMNCm3wTPCiLjPb4Iqnk+g0SgrsQ4NvU7nygFBlgz8xXLzIXPqVICthcHX\nRWRB8HnXmyzeF0iCs12F/6vYn/uZfxp3IV/KCR4LwSzbiFzxsV9GYoCoUE30LDVb\nXg==\n-----END PRIVATE KEY-----",
        "sender-public-key": "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB34JxfS6GAUVsFyihBUGvl34Ps7Q0XU1U6jWfK6FGJjbyyy89hfKBDoQ2zCWea9QdQvcObianherRPGt8s5uO0f8ALNJOnWN8Hwyg9Nd1p5/unjcNZra704uvj3o/7pGDrgowsJvAdAL8Qc3R5PEP5wnLKTvaSLEZfyOKjc+LT2hoyUw=",
        "recipient-public-key": "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAJoNHYpRXOhYjvThPLdXpfdinT6PVmLtYV2J4xmE+zrho92w/Za9CjDQpt8Ezwoi4z2+CKp5PoNEoK7EODb1O58oBQZYM/MVy8yFz6lSArYXB10VkQfB515ss3hdIgrNdhf+r2J/7mX8adyFfygkeC8Es24hc8bFfRmKAqFBN9Cw1W14=",
        "curve": "ecc-521"
    }
}

# Algorithm suites
ALGORITHM_SUITES = [
        # ESDK Algorithm Suites
        "0014",  # AES-128-GCM, no KDF
        "0046",  # AES-192-GCM, no KDF  
        "0078",  # AES-256-GCM, no KDF
        "0114",  # AES-128-GCM, HKDF-SHA256
        "0146",  # AES-192-GCM, HKDF-SHA256
        "0178",  # AES-256-GCM, HKDF-SHA256
        "0214",  # AES-128-GCM, HKDF-SHA256, ECDSA-P256
        "0346",  # AES-192-GCM, HKDF-SHA384, ECDSA-P384
        "0378",  # AES-256-GCM, HKDF-SHA384, ECDSA-P384
        "0478",  # AES-256-GCM, HKDF-SHA512, Key Commitment
        "0578",  # AES-256-GCM, HKDF-SHA512, Key Commitment, ECDSA-P256
        # DBE Algorithm Suites
        "6700",  # DBE AES-256-GCM with Key Commitment
        "6701",  # DBE AES-256-GCM with Key Commitment; ECDSA with P-384 and SHA-384
]

# Unicode strategies for maximum diversity
# Complete subcategories coverage for each Unicode category; refer to the documentation for category descriptions: https://www.unicode.org/reports/tr44/#General_Category_Values
unicode_strategies = [
    st.text(min_size=1, max_size=50),
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['So', 'Sc', 'Sk', 'Sm'])), #Symbols
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Lo', 'Ll', 'Lu', 'Lm', 'Lt'])), #Letters
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Nd', 'Nl', 'No'])), #Numbers
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Mn', 'Mc', 'Me'])), #Marks
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Zs', 'Zl', 'Zp'])), #Separators
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Cc', 'Cf', 'Cs', 'Co', 'Cn'])), #Control characters
    st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po'])), #Punctuation
    
    # Normalization cases
    st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFD', s)),  # Decomposed form
    st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFC', s)),  # Composed form

    #Incorrect handling of surrogate pairs, string truncation, character boundary issues; explicitly adding the lowest (U+0000) and highest (U+FFFF) 16-bit code points
    st.lists(st.integers(min_value=0x10000, max_value=0x10FFFF), min_size=1, max_size=25).map(lambda codepoints: ''.join(chr(cp) for cp in codepoints)).map(lambda s: s + '\u0000\uFFFF'),

    #Normalization + explicitly combining characters
    st.text(min_size=2, max_size=50).map(lambda s: unicodedata.normalize('NFD', s + '\u0300\u0301'))
]

# Below are the helper methods defined to assemble a test vector; a modular generation process for easy debugging.

def get_description_template(keyring_type: str) -> str:
    """Get description template for keyring type."""
    return DESCRIPTION_TEMPLATES.get(keyring_type, f"Fuzz test with {keyring_type} keyring")

@composite
def fuzz_key_identifiers(draw, base_key_id: str) -> Dict[str, Any]:
    """Generate completely independent fuzzed key identifiers for raw keyrings.
    
    Generates three independent Unicode strings:
    1. fuzzed_key_id: Lookup key for keys.json (not in encrypted message)
    2. key_namespace: Provider-id in encrypted message header (KEY PROVIDER ID)  
    3. key_id_in_material: Key-id in encrypted message header (KEY PROVIDER INFORMATION)
    
    Returns:
        Dictionary with fuzzed_key_id, key_namespace, and key_id_in_material
    """
    
    # Generate three completely independent Unicode strings
    fuzzed_key_id = draw(st.one_of(unicode_strategies))      # Lookup key for keys.json (not in message)
    key_namespace = draw(st.one_of(unicode_strategies))      # Provider-id (in message header)
    key_id_in_material = draw(st.one_of(unicode_strategies)) # Key-id (in message header)
    
    return {KEY_ID_FIELD: fuzzed_key_id, KEY_NAMESPACE_FIELD: key_namespace, KEY_ID_IN_MATERIAL_FIELD: key_id_in_material}

@composite
def fuzz_encryption_context(draw):
    """Generate diverse encryption contexts with Unicode characters.
    
    Avoids empty strings as they're invalid for KMS operations.
    """
    num_pairs = draw(st.integers(min_value=1, max_value=20))
    context = {}
    
    for _ in range(num_pairs):
        # Generate Unicode keys and values (min_size=1 to avoid empty strings)
        key = draw(st.one_of(unicode_strategies))
        value = draw(st.one_of(unicode_strategies))
        
        context[key] = value
    
    return context

def generate_required_keys(draw, encryption_context: Dict[str, str]) -> List[str]:
    """Generate requiredEncryptionContextKeys from existing context keys."""
    context_keys = list(encryption_context.keys())
    num_required = draw(st.integers(min_value=1, max_value=len(context_keys)))
    return draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=num_required, unique=True))

def create_key_description(draw, keyring_type: str, kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create key description based on keyring type."""
    if keyring_type == "raw":
        return create_raw_key_description(draw)
    elif keyring_type == "kms":
        return create_kms_key_description(kms_key, required_keys)
    else:
        raise ValueError(f"Unknown keyring type: {keyring_type}")

def create_raw_key_description(draw) -> Dict[str, Any]:
    """Create raw keyring description."""
    raw_key_id = draw(st.sampled_from(RAW_KEY_TYPES))
    key_identifiers = draw(fuzz_key_identifiers(raw_key_id))
    
    # Base description for all raw keyrings
    description = {
        "key": key_identifiers[KEY_ID_FIELD],  # Use fuzzed_key_id as the lookup key
        "provider-id": key_identifiers[KEY_NAMESPACE_FIELD],
        INTERNAL_KEY_ID_FIELD: key_identifiers[KEY_ID_IN_MATERIAL_FIELD]  # Store for later use in keys.json
    }
    
    # Handle different key types
    if raw_key_id.startswith("aes"):
        description.update({
            "type": "raw",
            "encryption-algorithm": "aes"
        })
    elif raw_key_id.startswith("ecc"):
        # ECC keys use a different type and structure
        description.update({
            "type": "raw-ecdh",
            "sender": key_identifiers[KEY_ID_FIELD],  # Same key for sender and recipient in static mode
            "recipient": key_identifiers[KEY_ID_FIELD],
            "sender-public-key": "sender-material-public-key",
            "recipient-public-key": "recipient-material-public-key", 
            "ecc-curve": raw_key_id,  # e.g., "ecc-256"
            "schema": "static"
        })
    
    return description

def create_kms_key_description(kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create KMS keyring description."""
    return {
        "type": "required-encryption-context-cmm",
        "underlying": {"type": "aws-kms", "key": kms_key},
        "requiredEncryptionContextKeys": required_keys
    }

# Assembling a test vector

@composite
def fuzz_test_vector(draw):
    """Generate a complete fuzzed test vector."""
    # Generate basic components
    encryption_context = draw(fuzz_encryption_context())
    algorithm_suite = draw(st.sampled_from(ALGORITHM_SUITES))
    keyring_type = draw(st.sampled_from(KEYRING_TYPES))

    if keyring_type == "kms":
        kms_key = draw(st.sampled_from(KMS_KEYS))
    else:
        kms_key = None  # Raw keyrings don't need this
    
    required_keys = generate_required_keys(draw, encryption_context)
    
    key_description = create_key_description(draw, keyring_type, kms_key, required_keys)
    
    # Create test vector
    test_vector = {
        "type": "positive-keyring",  # Only positive test cases
        "description": get_description_template(keyring_type),
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": encryption_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }
    
    return test_vector

def extract_new_keys(test_vectors: Dict[str, Any]) -> Dict[str, Any]:
    """Extract new keys from raw keyring test vectors.

    - Scans all generated test vectors
    - Finds raw keyring tests (type == "raw" or "raw-ecdh")
    - Extracts the fuzzed key lookups they reference
    - Creates corresponding key material entries for keys.json
    - Returns a dict of new keys to add to keys.json
    """
    new_keys = {}
    
    for test_vector in test_vectors.values():
        key_desc = test_vector.get("encryptKeyDescription", {})
        key_type = key_desc.get("type")
        
        # Handle both "raw" (AES) and "raw-ecdh" (ECC) types
        if key_type in ["raw", "raw-ecdh"]:
            # The lookup key is now the fuzzed_key_id (stored in "key" field)
            fuzzed_key_id = key_desc["key"]
            
            # Get the key-id that should go in the material (different from lookup key)
            key_id_in_material = key_desc.get(INTERNAL_KEY_ID_FIELD, fuzzed_key_id)
            
            if key_type == "raw":
                encryption_algorithm = key_desc.get("encryption-algorithm", "aes")
                base_key_id = "aes-256"  # default fallback
                for key_type_name in RAW_KEY_TYPES:
                    if key_type_name.startswith(encryption_algorithm):
                        base_key_id = key_type_name
                        break
            else:  # raw-ecdh
                # For ECC, use the curve name directly
                base_key_id = key_desc.get("ecc-curve", "ecc-256")
            
            key_info = KEY_MATERIALS.get(base_key_id, KEY_MATERIALS["aes-256"])
            
            # Create the key entry for keys.json based on algorithm type
            if base_key_id.startswith("aes"):
                new_keys[fuzzed_key_id] = {
                    "encrypt": True, 
                    "decrypt": True, 
                    "algorithm": "aes", 
                    "type": "symmetric",
                    "bits": key_info["bits"], 
                    "encoding": "base64",
                    "material": key_info["material"], 
                    "key-id": key_id_in_material
                }
            elif base_key_id.startswith("ecc"):
                new_keys[fuzzed_key_id] = {
                    "encrypt": True,
                    "decrypt": True,
                    "algorithm": "ecdh",
                    "type": "ecc-private",
                    "bits": key_info["bits"],
                    "encoding": "pem",
                    "sender-material": key_info["sender-material"],
                    "recipient-material": key_info["recipient-material"],
                    "public-key-encoding": "base64-der",
                    "sender-material-public-key": key_info["sender-public-key"],
                    "recipient-material-public-key": key_info["recipient-public-key"],
                    "key-id": key_id_in_material
                }
    
    return new_keys

def generate_fuzz_test_vectors(num_vectors) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Generate multiple fuzzed test vectors and collect new key generated."""
    test_vectors = {}
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=NonInteractiveExampleWarning)
        for i in range(num_vectors):
            # TODO: remove .example() usage.
            # Hypothesis is designed for property-based testing, so when using .example() it informs us that we should be using @given to actually test properties, not just generate examples.
            # But we're in a different use case, because we're essentially using Hypothesis as a sophisticated random data generator to create test vectors that will be evaluated by a different test system
            # Warning surpressed so that it doesn't fill the output with this message: https://github.com/aws/aws-cryptographic-material-providers-library/pull/1630/files#r2226909207; it will paste that message 2000 times for 2000 test vectors, for e.g.
            test_vector = fuzz_test_vector().example()
            test_id = str(uuid.uuid4())
            test_vectors[test_id] = test_vector
    
    new_keys = extract_new_keys(test_vectors)
    return test_vectors, new_keys

def main():
    """Main function to generate fuzzed test vectors."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate fuzzed test vectors')
    parser.add_argument('--num-vectors', type=int, default=20, help='Number of test vectors to generate')
    args = parser.parse_args()
    
    # Generate test vectors and new keys with specified number
    test_vectors, new_keys = generate_fuzz_test_vectors(num_vectors=args.num_vectors)
    
    # Load and update keys.json
    try:
        with open("keys.json", "r") as f:
            keys_data = json.load(f)
    except FileNotFoundError:
        print("Error: keys.json not found!")
        return
    
    keys_data["keys"].update(new_keys)
    
    with open("keys.json", "w") as f:
        json.dump(keys_data, f, indent=2, ensure_ascii=False)
    
    # Create and save manifest.json
    manifest_data = {
        "manifest": {"version": 4, "type": "awses-mpl-encrypt"},
        "keys": "file://keys.json",
        "tests": test_vectors
    }
    with open("manifest.json", "w") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(test_vectors)} test vectors with {len(new_keys)} new keys")

if __name__ == "__main__":
    main()