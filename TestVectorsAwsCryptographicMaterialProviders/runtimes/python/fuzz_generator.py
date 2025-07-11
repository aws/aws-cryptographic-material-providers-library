fuzz_generator.py


# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


# #!/usr/bin/env python3


"""
Fuzz Testing Generator for AWS Cryptographic Material Providers Library

This script generates fuzzed test vectors with a focused approach:
1. Fuzz encryption context fields and key-related fields (strings; since there a variery of UTF-8 characters that can be tested)
2. Randomly choosing and testing the "representative values" -> https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/test-vectors/test-vector-enumeration.md#selecting-a-representative-input-value

#TO DO:
- Add key name and key name space fuzz testing (any unicode character)
"""



import json
import uuid
import base64
import random
from typing import Dict, Any, List
import hypothesis
from hypothesis import given, strategies as st
from hypothesis.strategies import composite


# Fixed description templates mapping test types and keyring types to descriptions
DESCRIPTION_TEMPLATES = {
    ("positive-keyring", "raw"): "UTF-8 key identifier cross-runtime test with raw keyring",
    ("positive-keyring", "kms"): "KMS keyring baseline test with encryption context fuzzing",
    ("negative-encrypt-keyring", "raw"): "Raw keyring encryption failure test with UTF-8 key identifiers",
    ("negative-encrypt-keyring", "kms"): "KMS keyring encryption failure test with encryption context fuzzing",
    ("negative-decrypt-keyring", "raw"): "Raw keyring decryption failure test with UTF-8 key identifiers",
    ("negative-decrypt-keyring", "kms"): "KMS keyring decryption failure test with encryption context fuzzing",
}


def get_description_template(test_type: str, keyring_type: str) -> str:
    """
    Get fixed description template for test type and keyring type combination.
    
    Args:
        test_type: Type of test (positive-keyring, negative-encrypt-keyring, negative-decrypt-keyring)
        keyring_type: Type of keyring (kms, raw)
        
    Returns:
        Fixed description string for debugging purposes
    """
    return DESCRIPTION_TEMPLATES.get((test_type, keyring_type), f"Fuzz test: {test_type} with {keyring_type} keyring")



@composite
def fuzz_encryption_context(draw):
    """
    Generate diverse encryption contexts for fuzzing.
    
    This strategy creates encryption contexts with:
    - Normal ASCII strings
    - Unicode characters (including the problematic ones from the UTF-8 vulnerability)
    - Emojis and special characters
    - Null bytes and control characters
    - Surrogate pairs and replacement characters
    
    IMPORTANT: No empty strings for keys or values (invalid for KMS)
    """
    # Generate 1-20 key-value pairs (minimum 1 to ensure context exists)
    num_pairs = draw(st.integers(min_value=1, max_value=20))
    
    context = {}
    for _ in range(num_pairs):
        # Generate diverse key names (minimum size 1 to avoid empty strings)
        key = draw(st.one_of(
            st.text(min_size=1, max_size=50),  # Normal text
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['So', 'Sc', 'Sk'])),  # Symbols
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Lo', 'Ll', 'Lu'])),  # Letters
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Nd', 'Nl', 'No'])),  # Numbers
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Mn', 'Mc', 'Me'])),  # Marks
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Zs', 'Zl', 'Zp'])),  # Separators
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Cc', 'Cf', 'Cs', 'Co', 'Cn'])),  # Control chars
        ))
        
        # Generate diverse values (minimum size 1 to avoid empty strings)
        value = draw(st.one_of(
            st.text(min_size=1, max_size=100),  # Normal text
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['So', 'Sc', 'Sk'])),  # Symbols
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['Lo', 'Ll', 'Lu'])),  # Letters
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['Nd', 'Nl', 'No'])),  # Numbers
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['Mn', 'Mc', 'Me'])),  # Marks
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['Zs', 'Zl', 'Zp'])),  # Separators
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['Cc', 'Cf', 'Cs', 'Co', 'Cn'])),  # Control chars
            st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=['So'])),  # Emojis and symbols
        ))
        
        context[key] = value
    
    return context


@composite
def fuzz_test_vector(draw):
    """
    Generate a complete fuzzed test vector.
    
    This creates test vectors with:
    - Fuzzed encryption contexts - UTF-8 fuzzing
    - Normal ASCII for descriptions and other fields
    """
    # Use existing AWS KMS keys from keys.json
    kms_keys = [
        "us-west-2-mrk",
        "us-east-1-mrk", 
        "us-west-2-decryptable",
        "us-west-2-encrypt-only"
    ]
    
    # All available algorithm suites (11 ESDK + 2 DBE) as of date 07/9/2025
    algorithm_suites = [
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
        "6701",  # DBE AES-256-GCM
        "6702",  # DBE AES-256-GCM with Key Commitment
    ]
    
    # Generate fuzzed encryption context (UTF-8 fuzzing)
    encryption_context = draw(fuzz_encryption_context())
    
    # Generate fuzzed required encryption context keys (subset of context keys)
    context_keys = list(encryption_context.keys())
    # Since we always have at least 1 context key, we always have required keys
    num_required = draw(st.integers(min_value=1, max_value=min(len(context_keys), 5)))
    required_keys = draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=num_required, unique=True))
    
    #  Generate fuzzed reproduced encryption context
    # Sometimes match exactly, sometimes partially, sometimes completely different
    reproduced_strategy = draw(st.sampled_from(['exact', 'partial', 'empty', 'mismatch']))
    
    if reproduced_strategy == 'exact':
        reproduced_context = encryption_context.copy()
    elif reproduced_strategy == 'partial':
        # Take a subset of the original context (minimum 1 key to avoid empty)
        subset_keys = draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=len(context_keys), unique=True))
        reproduced_context = {k: encryption_context[k] for k in subset_keys if k in encryption_context}
    elif reproduced_strategy == 'empty':
        # For empty strategy, use a single key to avoid completely empty context
        reproduced_context = {context_keys[0]: encryption_context[context_keys[0]]}
    else:  # mismatch
        # Create a context with some matching keys but different values (minimum 1 key)
        reproduced_context = {}
        for key in draw(st.lists(st.sampled_from(context_keys), min_size=1, max_size=len(context_keys), unique=True)):
            if draw(st.booleans()):
                # Same key, different value (minimum size 1 to avoid empty)
                reproduced_context[key] = draw(st.text(min_size=1, max_size=50))
            else:
                # Same key, same value
                reproduced_context[key] = encryption_context[key]
    
    # FIXED VARIABLES: Choose algorithm suite and KMS key (randomly from valid options)
    algorithm_suite = draw(st.sampled_from(algorithm_suites))
    kms_key = draw(st.sampled_from(kms_keys))
    
    # Generate test type and keyring type independently (removing artificial restrictions)
    test_type = draw(st.sampled_from(["positive-keyring", "negative-encrypt-keyring", "negative-decrypt-keyring"]))
    keyring_type = draw(st.sampled_from(["kms", "raw"]))
    
    # Generate key descriptions based on keyring type AND test type
    if keyring_type == "kms":
        if test_type == "negative-encrypt-keyring":
            # For negative encrypt tests, use configurations that will cause encryption to fail
            # Strategy: Use required keys that don't exist in the encryption context
            missing_required_keys = [draw(st.text(min_size=1, max_size=20)) for _ in range(draw(st.integers(min_value=1, max_value=3)))]
            # Ensure these keys are NOT in the encryption context
            while any(key in encryption_context for key in missing_required_keys):
                missing_required_keys = [draw(st.text(min_size=1, max_size=20)) for _ in range(draw(st.integers(min_value=1, max_value=3)))]
            
            key_description = {
                "type": "required-encryption-context-cmm",
                "underlying": {
                    "type": "aws-kms",
                    "key": kms_key
                },
                "requiredEncryptionContextKeys": missing_required_keys  # Keys that don't exist in context
            }
        elif test_type == "negative-decrypt-keyring":
            # For negative decrypt tests, use mismatched required keys between encrypt and decrypt
            key_description = {
                "type": "required-encryption-context-cmm",
                "underlying": {
                    "type": "aws-kms",
                    "key": kms_key
                },
                "requiredEncryptionContextKeys": required_keys
            }
        else:  # positive-keyring
            # For positive tests, use normal configuration
            key_description = {
                "type": "required-encryption-context-cmm",
                "underlying": {
                    "type": "aws-kms",
                    "key": kms_key
                },
                "requiredEncryptionContextKeys": required_keys
            }
    else:  # raw keyring
        if test_type == "negative-encrypt-keyring":
            # For negative encrypt tests with raw keyrings, use the special failing key
            key_description = {
                "type": "static-material-keyring",
                "key": "no-plaintext-data-key"  # This key is designed to fail encryption
            }
        elif test_type == "negative-decrypt-keyring":
            # For negative decrypt tests, use fuzzed keys but with mismatched configurations
            raw_key_id = draw(st.sampled_from(["aes-128", "aes-192", "aes-256"]))
            
            
            key_description = {
                "type": "raw",
                "key": key_identifiers["key_name"],
                "provider-id": key_identifiers["key_namespace"],
                "encryption-algorithm": "aes"
            }
        else:  # positive-keyring
            # For positive tests, use normal fuzzed raw keyring
            raw_key_id = draw(st.sampled_from(["aes-128", "aes-192", "aes-256"]))
            
            
            key_description = {
                "type": "raw",
                "key": key_identifiers["key_name"],  # Use fuzzed key name (will be added to keys.json)
                "provider-id": key_identifiers["key_namespace"],  # Apply fuzzed key namespaces to the "provider-id" field
                "encryption-algorithm": "aes"
            }
    
    # Create the test vector in the correct format
    test_vector = {
        "type": test_type,
        "description": get_description_template(test_type, keyring_type),  # Use fixed description templates
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": reproduced_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }
    
    # Add error descriptions for negative tests using fixed templates
    if test_type == "negative-encrypt-keyring":
        if keyring_type == "raw":
            test_vector["errorDescription"] = "Expected encryption failure due to UTF-8 key identifier handling"
        else:
            test_vector["errorDescription"] = "Expected encryption failure with KMS keyring and fuzzed encryption context"
    elif test_type == "negative-decrypt-keyring":
        if keyring_type == "raw":
            test_vector["decryptErrorDescription"] = "Expected decryption failure due to UTF-8 key identifier handling"
        else:
            test_vector["decryptErrorDescription"] = "Expected decryption failure with KMS keyring and fuzzed encryption context"
    
    return test_vector


def generate_fuzz_test_vectors(num_vectors: int = 5) -> tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Generate multiple fuzzed test vectors and collect new keys.
    
    Args:
        num_vectors: Number of test vectors to generate
        
    Returns:
        Tuple containing:
        - Dictionary containing the test vectors
        - Dictionary containing new keys to add to keys.json
    """
    test_vectors = {}
    new_keys = {}
    
    print(f"Generating {num_vectors} fuzzed test vectors...")
    print("Focus: encryptionContext, requiredEncryptionContextKeys, reproducedEncryptionContext, and key identifiers")
    
    for i in range(num_vectors):
        # Use Hypothesis to generate a test vector
        test_vector = fuzz_test_vector().example()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
        
        # Extract new keys from raw keyring test vectors
        if (test_vector.get("encryptKeyDescription", {}).get("type") == "raw"):
            key_name = test_vector["encryptKeyDescription"]["key"]
            
            # Generate the key material for this fuzzed key name
            # Determine the base key type from the key name pattern
            if "aes-128" in key_name:
                base_key_id = "aes-128"
            elif "aes-192" in key_name:
                base_key_id = "aes-192"
            elif "aes-256" in key_name:
                base_key_id = "aes-256"
            else:
                base_key_id = "aes-256"  # Default fallback
            
            
            key_bits_map = {
                "aes-128": 128,
                "aes-192": 192,
                "aes-256": 256
            }
            
            base_materials = {
                "aes-128": "AAECAwQFBgcICRAREhMUFQ==",  # 16 bytes for AES-128
                "aes-192": "AAECAwQFBgcICRAREhMUFRYXGBkgISIj",  # 24 bytes for AES-192
                "aes-256": "AAECAwQFBgcICRAREhMUFRYXGBkgISIjJCUmJygpMDE="  # 32 bytes for AES-256
            }
            
            new_keys[key_name] = {
                "encrypt": True,
                "decrypt": True,
                "algorithm": "aes",
                "type": "symmetric",
                "bits": key_bits_map.get(base_key_id, 256),
                "encoding": "base64",
                "material": base_materials.get(base_key_id, base_materials["aes-256"]),
                "key-id": base_key_id
            }
        
        if (i + 1) % 10 == 0:
            print(f"Generated {i + 1}/{num_vectors} vectors...")
    
    print(f"Generated {len(new_keys)} new fuzzed keys for keys.json")
    return test_vectors, new_keys


def main():
    """Main function to generate fuzzed test vectors."""
    print("=== AWS Cryptographic Material Providers Fuzz Testing Generator ===")
    print("Strategy: Focus on encryption context UTF-8 vulnerabilities and key identifier fuzzing")
    
    # Generate test vectors and new keys
    test_vectors, new_keys = generate_fuzz_test_vectors(num_vectors=5)
    
    # Load existing keys.json
    try:
        with open("keys.json", "r") as f:
            keys_data = json.load(f)
    except FileNotFoundError:
        print("Error: keys.json not found!")
        return
    
    # Add new fuzzed keys to the existing keys
    original_key_count = len(keys_data["keys"])
    keys_data["keys"].update(new_keys)
    new_key_count = len(keys_data["keys"])
    
    # Save updated keys.json
    with open("keys.json", "w") as f:
        json.dump(keys_data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated keys.json: {original_key_count} -> {new_key_count} keys (+{new_key_count - original_key_count} new)")
    
    # Create manifest.json with the correct format
    manifest_data = {
        "manifest": {
            "version": 4,
            "type": "awses-mpl-encrypt"
        },
        "keys": "file://keys.json",
        "tests": test_vectors
    }
    
    # Save to file as manifest.json
    with open("manifest.json", "w") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(test_vectors)} fuzzed test vectors")
    print("Saved to manifest.json")
    
    # Show a sample of what was generated
    print("\nSample test vector:")
    sample_id = list(test_vectors.keys())[0]
    sample_vector = test_vectors[sample_id]
    print(f"Test ID: {sample_id}")
    print(f"Type: {sample_vector['type']}")
    print(f"Algorithm Suite: {sample_vector['algorithmSuiteId']}")
    print(f"Description: {sample_vector['description']}")
    print(f"Encryption Context Keys: {list(sample_vector['encryptionContext'].keys())}")
    print(f"Required Keys: {sample_vector['requiredEncryptionContextKeys']}")
    print(f"Reproduced Context Keys: {list(sample_vector['reproducedEncryptionContext'].keys())}")
    
    # Show sample of new keys added
    if new_keys:
        print(f"\nSample new key added to keys.json:")
        sample_key_name = list(new_keys.keys())[0]
        sample_key_data = new_keys[sample_key_name]
        print(f"Key Name: {sample_key_name}")
        print(f"Algorithm: {sample_key_data['algorithm']}")
        print(f"Type: {sample_key_data['type']}")
        print(f"Bits: {sample_key_data['bits']}")
        print(f"Key ID: {sample_key_data['key-id']}")


if __name__ == "__main__":
    main() 
