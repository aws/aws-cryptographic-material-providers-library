# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Fuzz Testing Generator for AWS Cryptographic Material Providers Library

This script generates fuzzed test vectors with a focused approach:
1. Fuzz encryption context fields and key-related fields (strings; since there a variety of Unicode characters that can be tested)
2. Randomly choosing and testing the "representative values" -> https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/test-vectors/test-vector-enumeration.md#selecting-a-representative-input-value

#TODO-Fuzztesting:
- "negative-encrypt-keyring" fuzzing functionality: currently, we implement tests with missing required keys (for KMS keyrings) or invalid key material (raw keryings)
    - Invalid key material (like "no-plaintext-data-key" for raw keyrings)
    - Insufficient permissions (encrypt-only keys trying to decrypt)
    - Malformed key configurations
    - Algorithm mismatches
    - Invalid encryption context formats
- Strengthening encryption context fuzzing with specific edge cases, structured patterns
- Add key name and key name space fuzz testing (any unicode character)
- add RSA as well for "raw" key fuzzing
- Remove extraneous logging/printing statements to simplify output on CI
- Increase the number of test vectors
"""

import json
import uuid
from typing import Dict, Any, List, Tuple
import hypothesis
from hypothesis import strategies as st
from hypothesis.strategies import composite

# Description templates for test vectors
DESCRIPTION_TEMPLATES = {
    ("positive-keyring", "raw"): "Raw keyring test with Unicode fuzzing",
    ("positive-keyring", "kms"): "KMS keyring test with Unicode fuzzing", 
    ("positive-keyring", "aws-kms-mrk-aware"): "MRK-aware keyring test with Unicode fuzzing",
    ("positive-keyring", "aws-kms-rsa"): "RSA keyring test with Unicode fuzzing",
    ("positive-keyring", "caching-cmm"): "Caching CMM test with Unicode fuzzing",
    ("negative-encrypt-keyring", "raw"): "Raw keyring encryption failure test",
    ("negative-encrypt-keyring", "kms"): "KMS keyring encryption failure test",
    ("negative-encrypt-keyring", "aws-kms-mrk-aware"): "MRK-aware keyring encryption failure test",
    ("negative-encrypt-keyring", "aws-kms-rsa"): "RSA keyring encryption failure test", 
    ("negative-encrypt-keyring", "caching-cmm"): "Caching CMM encryption failure test",
    ("negative-decrypt-keyring", "raw"): "Raw keyring decryption failure test",
    ("negative-decrypt-keyring", "kms"): "KMS keyring decryption failure test",
    ("negative-decrypt-keyring", "aws-kms-mrk-aware"): "MRK-aware keyring decryption failure test",
    ("negative-decrypt-keyring", "aws-kms-rsa"): "RSA keyring decryption failure test",
    ("negative-decrypt-keyring", "caching-cmm"): "Caching CMM decryption failure test",
}

# Key, Algorithm, Test-Type, Key-Material Definitions
KMS_KEYS = ["us-west-2-mrk", "us-east-1-mrk", "us-west-2-decryptable", "us-west-2-encrypt-only"]
MRK_KEYS = ["us-west-2-mrk", "us-east-1-mrk"]

RAW_KEY_TYPES = ["aes-128", "aes-192", "aes-256"]
KEYRING_TYPES = ["kms", "raw", "aws-kms-mrk-aware", "aws-kms-rsa", "caching-cmm"]

TEST_TYPES = ["positive-keyring", "negative-encrypt-keyring", "negative-decrypt-keyring"]

KEY_MATERIALS = {
    "aes-128": {"bits": 128, "material": "AAECAwQFBgcICRAREhMUFQ=="},
    "aes-192": {"bits": 192, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIj"},
    "aes-256": {"bits": 256, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIjJCUmJygpMDE="}
}

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

# Below are the helper methods defined to assemble a test vector; a modular generation process for easy debugging

def get_description_template(test_type: str, keyring_type: str) -> str:
    """Get description template for test type and keyring type combination."""
    return DESCRIPTION_TEMPLATES.get((test_type, keyring_type), f"Fuzz test: {test_type} with {keyring_type} keyring")

@composite
def fuzz_encryption_context(draw):
    """Generate diverse encryption contexts with Unicode characters.
    
    Avoids empty strings as they're invalid for KMS operations.
    """
    num_pairs = draw(st.integers(min_value=1, max_value=20))
    context = {}
    
    for _ in range(num_pairs):
        # Generate Unicode keys and values (min_size=1 to avoid empty strings)

        key = draw(st.one_of(
            # Basic categories
            st.text(min_size=1, max_size=50),  # Normal text
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['So', 'Sc', 'Sk', 'Sm'])), #Symbols
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Lo', 'Ll', 'Lu', 'Lm', 'Lt'])), #Letters
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Nd', 'Nl', 'No'])), #Numbers
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Mn', 'Mc', 'Me'])), #Marks
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Zs', 'Zl', 'Zp'])), #Separators
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Cc', 'Cf', 'Cs', 'Co', 'Cn'])), #Control characters
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po'])), #Punctuation
            
            # Specific edge cases
            st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFD', s)),  # Decomposed form
            st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFC', s)),  # Composed form
            
            # Bidirectional text
            st.text(min_size=1, max_size=25, alphabet=st.characters(script='Arabic')) + 
                st.text(min_size=1, max_size=25, alphabet=st.characters(script='Latin')),
            
            # Emoji
            st.text(min_size=1, max_size=50, alphabet=st.characters(block='Emoticons'))
        ))
        
        value = draw(st.one_of(
            st.text(min_size=1, max_size=50),  # Normal text
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['So', 'Sc', 'Sk', 'Sm'])), #Symbols
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Lo', 'Ll', 'Lu', 'Lm', 'Lt'])), #Letters
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Nd', 'Nl', 'No'])), #Numbers
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Mn', 'Mc', 'Me'])), #Marks
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Zs', 'Zl', 'Zp'])), #Separators
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Cc', 'Cf', 'Cs', 'Co', 'Cn'])), #Control characters
            st.text(min_size=1, max_size=50, alphabet=st.characters(categories=['Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po'])), #Punctuation
            
            # Specific edge cases
            st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFD', s)),  # Decomposed form
            st.text(min_size=1, max_size=50).map(lambda s: unicodedata.normalize('NFC', s)),  # Composed form
            
            # Bidirectional text
            st.text(min_size=1, max_size=25, alphabet=st.characters(script='Arabic')) + 
                st.text(min_size=1, max_size=25, alphabet=st.characters(script='Latin')),
            
            # Emoji
            st.text(min_size=1, max_size=50, alphabet=st.characters(block='Emoticons'))
        ))
        
        context[key] = value
    
    return context

def generate_required_keys(draw, test_type: str, encryption_context: Dict[str, str]) -> List[str]:
    """Generate requiredEncryptionContextKeys based on test type."""
    if test_type == "negative-encrypt-keyring":
        # Generate keys that don't exist in encryption context; encryption fails as a result
        context_keys = set(encryption_context.keys())
        required_keys = []
        for _ in range(draw(st.integers(min_value=1, max_value=3))):
            while True:
                candidate_key = draw(st.text(min_size=1, max_size=20))
                if candidate_key not in context_keys:
                    required_keys.append(candidate_key)
                    context_keys.add(candidate_key)
                    break
        return required_keys
    else:
        # Use subset of existing context keys
        context_keys = list(encryption_context.keys())
        num_required = draw(st.integers(min_value=1, max_value=min(len(context_keys), 5)))
        return draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=num_required, unique=True))

def create_key_description(draw, keyring_type: str, test_type: str, kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create key description based on keyring and test type."""
    if keyring_type == "raw":
        return create_raw_key_description(draw, test_type)
    elif keyring_type == "caching-cmm":
        return create_caching_cmm_description(kms_key, required_keys)
    elif keyring_type in ["kms", "aws-kms-mrk-aware", "aws-kms-rsa"]:
        return create_kms_based_key_description(draw, keyring_type, kms_key, required_keys)
    else:
        raise ValueError(f"Unknown keyring type: {keyring_type}")

#TODO-Fuzztesting: add RSA as well for "raw" key fuzzing
def create_raw_key_description(draw, test_type: str) -> Dict[str, Any]:
    """Create raw keyring description."""
    if test_type == "negative-encrypt-keyring":
        return {"type": "static-material-keyring", "key": "no-plaintext-data-key"}
    
    raw_key_id = draw(st.sampled_from(RAW_KEY_TYPES))
    key_identifiers = draw(fuzz_key_identifiers(raw_key_id))
    return {
        "type": "raw",
        "key": key_identifiers["key_name"],
        "provider-id": key_identifiers["key_namespace"],
        "encryption-algorithm": "aes"
    }

def create_kms_based_key_description(draw, keyring_type: str, kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create KMS-based keyring description (handles kms, mrk-aware, rsa)."""
    # Map keyring types to their underlying types and keys
    keyring_config = {
        "kms": {"type": "aws-kms", "key": kms_key},
        "aws-kms-mrk-aware": {"type": "aws-kms-mrk-aware", "key": draw(st.sampled_from(MRK_KEYS))},
        "aws-kms-rsa": {"type": "aws-kms-rsa", "key": "us-west-2-rsa-mrk"}
    }
    
    underlying_config = keyring_config.get(keyring_type, {"type": "aws-kms", "key": kms_key})
    
    return {
        "type": "required-encryption-context-cmm",
        "underlying": underlying_config,
        "requiredEncryptionContextKeys": required_keys
    }

def create_caching_cmm_description(kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create caching CMM description."""
    return {
        "type": "caching-cmm",
        "underlying": {
            "type": "required-encryption-context-cmm",
            "underlying": {"type": "aws-kms", "key": kms_key},
            "requiredEncryptionContextKeys": required_keys
        },
        "maxAge": 600,
        "maxBytesEncrypted": 1000,
        "maxMessagesEncrypted": 10
    }

def generate_reproduced_context(draw, encryption_context: Dict[str, str]) -> Dict[str, str]:
    """Generate reproducedEncryptionContext with various strategies."""
    strategy = draw(st.sampled_from(['exact', 'partial', 'one', 'mismatch']))
    context_keys = list(encryption_context.keys())
    
    if strategy == 'exact':
        return encryption_context.copy()
    elif strategy == 'partial':
        subset_keys = draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=len(context_keys), unique=True))
        return {k: encryption_context[k] for k in subset_keys if k in encryption_context}
    elif strategy == 'one':
        return {context_keys[0]: encryption_context[context_keys[0]]}
    else:  # mismatch
        reproduced_context = {}
        for key in draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=len(context_keys), unique=True)):
            if draw(st.booleans()):
                reproduced_context[key] = draw(st.text(min_size=1, max_size=50))
            else:
                reproduced_context[key] = encryption_context[key]
        return reproduced_context

def add_error_descriptions(test_vector: Dict[str, Any], test_type: str, keyring_type: str) -> None:
    """Add error descriptions for negative tests."""
    if test_type == "negative-encrypt-keyring":
        test_vector["errorDescription"] = "Expected encryption failure"
    elif test_type == "negative-decrypt-keyring":
        test_vector["decryptErrorDescription"] = "Expected decryption failure"

# Assembling a test vector

@composite
def fuzz_test_vector(draw):
    """Generate a complete fuzzed test vector."""
    # Generate basic components
    encryption_context = draw(fuzz_encryption_context())
    algorithm_suite = draw(st.sampled_from(ALGORITHM_SUITES))
    test_type = draw(st.sampled_from(TEST_TYPES))
    keyring_type = draw(st.sampled_from(KEYRING_TYPES))

    if keyring_type in ["kms", "aws-kms-mrk-aware", "caching-cmm"]:
        kms_key = draw(st.sampled_from(KMS_KEYS))
    else:
        kms_key = None  # Raw keyrings don't need this
    
    # Generate required keys based on test type
    required_keys = generate_required_keys(draw, test_type, encryption_context)
    
    # Create key descriptions
    key_description = create_key_description(draw, keyring_type, test_type, kms_key, required_keys)
    
    # Generate reproduced context
    reproduced_context = generate_reproduced_context(draw, encryption_context)
    
    # Create test vector
    test_vector = {
        "type": test_type,
        "description": get_description_template(test_type, keyring_type),
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": reproduced_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }
    
    # Add error descriptions for negative tests
    add_error_descriptions(test_vector, test_type, keyring_type)
    
    return test_vector

def extract_new_keys(test_vectors: Dict[str, Any]) -> Dict[str, Any]:
    """Extract new keys from raw keyring test vectors.

    - Scans all generated test vectors
    - Finds raw keyring tests (type == "raw")
    - Extracts the fuzzed key names they reference
    - Creates corresponding key material entries for keys.json
    - Returns a dict of new keys to add to keys.json
    """
    new_keys = {}
    
    for test_vector in test_vectors.values():
        if test_vector.get("encryptKeyDescription", {}).get("type") == "raw":
            key_name = test_vector["encryptKeyDescription"]["key"]
            
            # Determine base key type from key name
            base_key_id = "aes-256"  # default
            for key_type in RAW_KEY_TYPES:
                if key_type in key_name:
                    base_key_id = key_type
                    break
            
            key_info = KEY_MATERIALS.get(base_key_id, KEY_MATERIALS["aes-256"])
            new_keys[key_name] = {
                "encrypt": True, "decrypt": True, "algorithm": "aes", "type": "symmetric",
                "bits": key_info["bits"], "encoding": "base64",
                "material": key_info["material"], "key-id": base_key_id
            }
    
    return new_keys

def generate_fuzz_test_vectors(num_vectors: int = 5) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Generate multiple fuzzed test vectors and collect new key generated."""
    test_vectors = {}
    
    for i in range(num_vectors):
        test_vector = fuzz_test_vector().example()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
    
    new_keys = extract_new_keys(test_vectors)
    return test_vectors, new_keys

def main():
    """Main function to generate fuzzed test vectors."""
    # Generate test vectors and new keys
    test_vectors, new_keys = generate_fuzz_test_vectors(num_vectors=5)
    
    # Load and update keys.json
    try:
        with open("keys.json", "r") as f:
            keys_data = json.load(f)
    except FileNotFoundError:
        print("Error: keys.json not found!")
        return
    
    original_key_count = len(keys_data["keys"])
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