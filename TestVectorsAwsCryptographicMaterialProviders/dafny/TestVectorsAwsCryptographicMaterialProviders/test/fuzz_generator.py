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
import random
import argparse
from typing import Dict, Any, List, Tuple

# Description templates for test vectors
DESCRIPTION_TEMPLATES = {
    "raw": "Raw keyring test with Unicode fuzzing",
    "kms": "KMS keyring test with Unicode fuzzing"
}

#TODO-Fuzztesting: #include the other keys: KMS keys, rsa for raw keys, (right now: 2 KMS keys, AES raw keys now); other keyring types; other test types (only positive-keyring now)
# Key, Algorithm, Test-Type, Key-Material Definitions
KMS_KEYS = ["us-west-2-mrk", "us-east-1-mrk", "us-west-2-decryptable"] #us-west-2-rsa-mrk (alr have rsa), us-west-2-256-ecc, us-west-2-384-ecc (and alr have enough ecc)
RAW_KEY_TYPES = ["aes-128", "aes-192", "aes-256", "ecc-256", "ecc-384", "ecc-521"] #"rsa-4096",
KEYRING_TYPES = ["kms", "raw"]

# Key materials for raw keyrings
KEY_MATERIALS = {
    "aes-128": {"bits": 128, "material": "AAECAwQFBgcICRAREhMUFQ=="},
    "aes-192": {"bits": 192, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIj"},
    "aes-256": {"bits": 256, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIjJCUmJygpMDE="},

        # RSA key material
    # "rsa-4096": {
    #     "bits": 4096,
    #     "algorithm": "rsa",
    #     "material": "-----BEGIN PRIVATE KEY-----\n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\ndzxtGxpeTBi+KhKlca8SlCdCqYwG6Q==\n-----END PRIVATE KEY-----",
    #     "padding-algorithm": "oaep-mgf1",
    #     "padding-hash": "sha512"
    # },
    
    # # RSA public key material (needed for RawRSAKeyring encryption)
    # "rsa-4096-public": {
    #     "bits": 4096,
    #     "algorithm": "rsa",
    #     "material": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAs7RoNYEPAIws89VV+kra\nrVv/4wbdmUAaAKWgWuxZi5na9GJSmnhCkqyLRm7wPbQY4LCoa5/IMUxkHLsYDPdu\nudY0Qm0GcoxOlvJKHYo4RjF7HyiS34D6dvyO4Gd3aq0mZHoxSGCxW/7hf03wEMzc\niVJXWHXhaI0lD6nrzIEgLrE4L+3V2LeAQjvZsTKd+bYMqeZOL2syiVVIAU8POwAG\nGVBroJoveFm/SUp6lCiN0M2kTeyQA2ax3QTtZSAa8nwrI7U52XOzVmdMicJsy2Pg\nuW98te3MuODdK24yNkHIkYameP/Umf/SJshUJQd5a/TUp3XE+HhOWAumx22tIDlC\nvZS11cuk2fp0WeHUnXaC19N5qWKfvHEKSugzty/z3lGP7ItFhrF2X1qJHeAAsL11\nkjo6Lc48KsE1vKvbnW4VLyB3wdNiVvmUNO29tPXwaR0Q5Gbr3jk3nUzdkEHouHWQ\n41lubOHCCBN3V13mh/MgtNhESHjfmmOnh54ErD9saA1d7CjTf8g2wqmjEqvGSW6N\nq7zhcWR2tp1olflS7oHzul4/I3hnkfL6Kb2xAWWaQKvg3mtsY2OPlzFEP0tR5UcH\nPfp5CeS1Xzg7hN6vRICW6m4l3u2HJFld2akDMm1vnSz8RCbPW7jp7YBxUkWJmypM\ntG7Yv2aGZXGbUtM8o1cZarECAwEAAQ==\n-----END PUBLIC KEY-----"
    # },
    
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

def generate_unicode_string() -> str:
    """Generate a Unicode string with diverse characters."""
    # Define all Unicode categories we want to include
    all_categories = [
        'So', 'Sc', 'Sk', 'Sm',
        'Lo', 'Ll', 'Lu', 'Lm', 'Lt',
        'Nd', 'Nl', 'No',
        'Mn', 'Mc', 'Me',
        'Zs', 'Zl', 'Zp',
        'Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po'
    ]
    
    # Generate a string with characters from random categories
    length = random.randint(1, 50)
    chars = []
    for _ in range(length):
        category = random.choice(all_categories)
        char = chr(random.randint(0x0020, 0x10FFFF))
        while unicodedata.category(char) != category:
            char = chr(random.randint(0x0020, 0x10FFFF))
        chars.append(char)
    
    basic_string = ''.join(chars)
    
    # Randomly apply normalization
    normalizations = ['NFC', 'NFD', 'NFKC', 'NFKD']
    normalized_string = unicodedata.normalize(random.choice(normalizations), basic_string)
    
    # Randomly add some special cases
    special_cases = [
        lambda s: s,  # No change
        lambda s: s + '\u0000\uFFFF',  # Add BMP boundaries
        lambda s: s + '\u0300\u0301',  # Add combining characters
        lambda s: ''.join(chr(random.randint(0x10000, 0x10FFFF)) for _ in range(5)) + s  # Add non-BMP characters
    ]
    
    return random.choice(special_cases)(normalized_string)

# Below are the helper methods defined to assemble a test vector; a modular generation process for easy debugging.

def get_description_template(keyring_type: str) -> str:
    """Get description template for keyring type."""
    return DESCRIPTION_TEMPLATES.get(keyring_type, f"Fuzz test with {keyring_type} keyring")

#TODO-Fuzztesting: Strengthening encryption context fuzzing with specific edge cases (close to the character limitation for encryption context (8,192)), structured patterns
def fuzz_encryption_context():
    """Generate diverse encryption contexts with Unicode characters.
    Avoids empty strings as they're invalid for KMS operations.
    """
    num_pairs = random.randint(3, 10)
    context = {}
    for _ in range(num_pairs):
        key = generate_unicode_string()
        value = generate_unicode_string()
        context[key] = value
    return context

#TODO-Fuzztesting: "negative-encrypt-keyring" fuzzing functionality: in fuzzToDos branch, implemented tests with missing required keys (for KMS keyrings) or invalid key material (raw keryings)
#but it could also fail because of algo mismatches or invalid encryption context formats
#currently, only testing for positive-keyring

def create_key_description(keyring_type: str, kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create key description based on keyring type."""
    if keyring_type == "raw":
        return create_raw_key_description()
    elif keyring_type == "kms":
        return create_kms_key_description(kms_key, required_keys)
    else:
        raise ValueError(f"Unknown keyring type: {keyring_type}")

#TODO-Fuzztesting: ensure use of other algorithm types for raw keyrings (not just aes)
def create_raw_key_description() -> Dict[str, Any]:
    """Create raw keyring description without using Hypothesis."""
    import random
    
    raw_key_id = random.choice(RAW_KEY_TYPES)
    
    # Generate key identifiers
    fuzzed_key_id = generate_unicode_string()
    key_namespace = generate_unicode_string()
    key_id_in_material = generate_unicode_string()
    
    # Base description
    description = {
        "key": fuzzed_key_id,
        "provider-id": key_namespace,
        "_key_id_in_material": key_id_in_material
    }
    
    # Handle different key types
    if raw_key_id.startswith("aes"):
        description.update({
            "type": "raw",
            "encryption-algorithm": "aes"
        })
    elif raw_key_id.startswith("ecc"):
        description.update({
            "type": "raw-ecdh",
            "sender": fuzzed_key_id,
            "recipient": fuzzed_key_id,
            "sender-public-key": "sender-material-public-key",
            "recipient-public-key": "recipient-material-public-key",
            "ecc-curve": raw_key_id,
            "schema": "static"
        })
    
    return description

#TODO-Fuzztesting: add aws-kms-ecdh and aws-kms-hierarchy when more KMS keys are added
def create_kms_key_description(kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create KMS keyring description."""
    return {
        #TODO-Fuzztesting: only considering one "type": required-encryption-context-cmm; could consider aws-kms, symmetric, rsa, etc (refer to keys.json)
        "type": "required-encryption-context-cmm",
        "underlying": {"type": "aws-kms", "key": kms_key},
        "requiredEncryptionContextKeys": required_keys
    }

# Assembling a test vector

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
        
        # Handle both "raw" (AES/RSA) and "raw-ecdh" (ECC) types
        if key_type in ["raw", "raw-ecdh"]:
            # The lookup key is now the fuzzed_key_id (stored in "key" field)
            fuzzed_key_id = key_desc["key"]
            
            # Get the key-id that should go in the material (different from lookup key)
            key_id_in_material = key_desc.get("_key_id_in_material", fuzzed_key_id)
            
            # Determine base key type from the encryption algorithm or ECC curve
            if key_type == "raw":
                encryption_algorithm = key_desc.get("encryption-algorithm", "aes")
                # Find matching key type based on algorithm
                base_key_id = "aes-256"  # default fallback
                for key_type_name in RAW_KEY_TYPES:
                    if key_type_name.startswith(encryption_algorithm):
                        base_key_id = key_type_name
                        break
            else:  # raw-ecdh
                # For ECC, use the curve name directly
                base_key_id = key_desc.get("ecc-curve", "ecc-256")
            
            # Get key material information
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
            elif base_key_id.startswith("rsa"):
                # Create RSA private key entry
                new_keys[fuzzed_key_id] = {
                    "encrypt": True,
                    "decrypt": True,
                    "algorithm": "rsa",
                    "type": "private",
                    "bits": key_info["bits"],
                    "encoding": "pem",
                    "material": key_info["material"],
                    "key-id": key_id_in_material
                }
                
                # Also create a corresponding public key entry (needed for RawRSAKeyring encryption)
                public_key_id = fuzzed_key_id + "-public"
                public_key_info = KEY_MATERIALS["rsa-4096-public"]
                new_keys[public_key_id] = {
                    "encrypt": True,
                    "decrypt": False,
                    "algorithm": "rsa", 
                    "type": "public",
                    "bits": public_key_info["bits"],
                    "encoding": "pem",
                    "material": public_key_info["material"],  # Use the public key material
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

def generate_single_test_vector() -> Dict[str, Any]:
    """Generate a single test vector without using Hypothesis."""
    # Generate encryption context
    encryption_context = fuzz_encryption_context()
    
    # Select random values from available options
    algorithm_suite = random.choice(ALGORITHM_SUITES)
    keyring_type = random.choice(KEYRING_TYPES)
    
    # Generate required keys
    context_keys = list(encryption_context.keys())
    num_required = random.randint(1, len(context_keys))
    required_keys = random.sample(context_keys, num_required)
    
    # Handle key description based on keyring type
    if keyring_type == "kms":
        kms_key = random.choice(KMS_KEYS)
        key_description = create_kms_key_description(kms_key, required_keys)
    else:  # raw
        key_description = create_raw_key_description()
    
    # Create test vector
    return {
        "type": "positive-keyring",
        "description": get_description_template(keyring_type),
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": encryption_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }

def generate_fuzz_test_vectors(num_vectors) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Generate multiple fuzzed test vectors and collect new key generated."""
    test_vectors = {}
    
    for _ in range(num_vectors):
        test_vector = generate_single_test_vector()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
    
    new_keys = extract_new_keys(test_vectors)
    return test_vectors, new_keys

#TODO-Fuzztesting: increase the number of test vectors (for CI), need to increase the stack perhaps?
#TODO-Fuzztesting: remove extraneous logging/printing statements to simplify output (for CI)
#TODO-Fuzztesting: Add a logging mechanism to log erros/vulnerabilities we run into
def main():
    """Main function to generate fuzzed test vectors."""
    parser = argparse.ArgumentParser(description='Generate fuzzed test vectors')
    parser.add_argument('--num-vectors', type=int, default=5)
    args = parser.parse_args()
    
    try:
        # Generate vectors and update keys
        test_vectors, new_keys = generate_fuzz_test_vectors(args.num_vectors)
        
        # Update keys.json
        with open("keys.json", "r+") as f:
            keys_data = json.load(f)
            keys_data["keys"].update(new_keys)
            f.seek(0)
            json.dump(keys_data, f, indent=2, ensure_ascii=False)
            f.truncate()
        
        # Save manifest.json
        with open("manifest.json", "w") as f:
            json.dump({
                "manifest": {"version": 4, "type": "awses-mpl-encrypt"},
                "keys": "file://keys.json",
                "tests": test_vectors
            }, f, indent=2, ensure_ascii=False)
        
        print(f"Generated {len(test_vectors)} test vectors with {len(new_keys)} new keys")
    
    except FileNotFoundError:
        print("Error: keys.json not found!")

if __name__ == "__main__":
    main()