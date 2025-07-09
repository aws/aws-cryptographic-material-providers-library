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
    
    # Generate key descriptions based on test type (NORMAL ASCII)
    test_type = draw(st.sampled_from(["positive-keyring", "negative-encrypt-keyring", "negative-decrypt-keyring"]))
    
    if test_type == "positive-keyring":
        # For positive tests, use required-encryption-context-cmm with underlying aws-kms
        key_description = {
            "type": "required-encryption-context-cmm",
            "underlying": {
                "type": "aws-kms",
                "key": kms_key
            },
            "requiredEncryptionContextKeys": required_keys
        }
    else:
        # For negative tests, use raw key with existing symmetric key from keys.json
        raw_key_id = draw(st.sampled_from(["aes-128", "aes-192", "aes-256"]))
        key_description = {
            "type": "raw",
            "key": raw_key_id,
            "provider-id": f"aws-raw-vectors-persistent-{raw_key_id}",
            "encryption-algorithm": "aes"
        }
    
    # Create the test vector in the correct format
    test_vector = {
        "type": test_type,
        "description": draw(st.text(min_size=10, max_size=200, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ')),  # Normal ASCII
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": reproduced_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }
    
    # Add error descriptions for negative tests (NORMAL ASCII)
    if test_type == "negative-encrypt-keyring":
        test_vector["errorDescription"] = draw(st.text(min_size=10, max_size=200, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '))
    elif test_type == "negative-decrypt-keyring":
        test_vector["decryptErrorDescription"] = draw(st.text(min_size=10, max_size=200, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '))
    
    return test_vector


def generate_fuzz_test_vectors(num_vectors: int = 2) -> Dict[str, Any]:
    """
    Generate multiple fuzzed test vectors.
    
    Args:
        num_vectors: Number of test vectors to generate
        
    Returns:
        Dictionary containing the test vectors
    """
    test_vectors = {}
    
    print(f"Generating {num_vectors} fuzzed test vectors...")
    print("Focus: encryptionContext, requiredEncryptionContextKeys, reproducedEncryptionContext")
    
    for i in range(num_vectors):
        # Use Hypothesis to generate a test vector
        test_vector = fuzz_test_vector().example()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
        
        if (i + 1) % 10 == 0:
            print(f"Generated {i + 1}/{num_vectors} vectors...")
    
    return test_vectors


def main():
    """Main function to generate fuzzed test vectors."""
    print("=== AWS Cryptographic Material Providers Fuzz Testing Generator ===")
    print("Strategy: Focus on encryption context UTF-8 vulnerabilities")
    
    # Generate test vectors
    test_vectors = generate_fuzz_test_vectors(num_vectors=2)
    
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


if __name__ == "__main__":
    main() 