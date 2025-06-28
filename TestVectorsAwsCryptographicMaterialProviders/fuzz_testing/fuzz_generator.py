#!/usr/bin/env python3
"""
Fuzz Testing Generator for AWS Cryptographic Material Providers Library

This script generates fuzzed test vectors focusing on encryption context variations
while using AWS KMS keyrings. It creates test.json files that can be used with
the existing test infrastructure.
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
    - Unicode characters (including the problematic ones)
    - Empty strings
    - Special characters
    - Various sizes (0-20 key-value pairs)
    """
    # Define different types of keys and values
    normal_keys = st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Nd']))
    unicode_keys = st.text(min_size=1, max_size=10, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Lo', 'Mn', 'Mc']))
    special_keys = st.text(min_size=1, max_size=10, alphabet=st.characters(whitelist_categories=['P', 'S', 'Zs']))
    
    normal_values = st.text(min_size=0, max_size=50, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Nd', 'Zs']))
    unicode_values = st.text(min_size=0, max_size=30, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Lo', 'Mn', 'Mc', 'Zs']))
    special_values = st.text(min_size=0, max_size=30, alphabet=st.characters(whitelist_categories=['P', 'S', 'Zs']))
    
    # Create key-value pairs with different combinations
    key_strategies = [normal_keys, unicode_keys, special_keys]
    value_strategies = [normal_values, unicode_values, special_values]
    
    # Generate 0-20 key-value pairs
    num_pairs = draw(st.integers(min_value=0, max_value=20))
    
    context = {}
    for _ in range(num_pairs):
        key_strategy = draw(st.sampled_from(key_strategies))
        value_strategy = draw(st.sampled_from(value_strategies))
        
        key = draw(key_strategy)
        value = draw(value_strategy)
        
        # Avoid duplicate keys
        if key not in context:
            context[key] = value
    
    return context


@composite
def fuzz_test_vector(draw):
    """
    Generate a complete fuzzed test vector.
    
    This creates test vectors with:
    - Fuzzed encryption contexts
    - AWS KMS keyrings
    - Various algorithm suites
    - reproducedEncryptionContext for testing context handling
    """
    # Use existing AWS KMS keys from keys.json
    kms_keys = [
        "us-west-2-mrk",
        "us-east-1-mrk", 
        "us-west-2-decryptable",
        "us-west-2-encrypt-only"
    ]
    
    # All available algorithm suites (11 ESDK + 2 DBE)
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
        "0578",  # AES-256-GCM, HKDF-SHA512, Key Commitment, ECDSA-P384
        # DBE Algorithm Suites
        "6701",  # DBE AES-256-GCM
        "6702"   # DBE AES-256-GCM, Key Commitment
    ]
    
    # Generate encryption context
    encryption_context = draw(fuzz_encryption_context())
    
    # Generate reproduced encryption context (this is where the fuzzing magic happens!)
    # We want to test both correct and incorrect reproductions
    should_reproduce_correctly = draw(st.booleans())
    
    if should_reproduce_correctly:
        # Correct reproduction - should match exactly
        reproduced_context = encryption_context.copy()
    else:
        # Incorrect reproduction - introduce subtle differences
        reproduced_context = draw(st.one_of([
            # Case 1: Slightly modified values (UTF-8 edge cases)
            st.fixed_dictionaries({
                k: st.one_of([
                    st.just(v),  # Keep original
                    st.just(v + "🚀"),  # Add emoji
                    st.just(v + "\u0000"),  # Add null byte
                    st.just(v + "\uFFFD"),  # Add replacement char
                    st.just(v + "\uD800\uDC00"),  # Add surrogate pair
                ]) for k, v in encryption_context.items()
            }),
            # Case 2: Missing or extra keys
            st.dictionaries(
                keys=st.text(min_size=1, max_size=20),
                values=st.text(min_size=0, max_size=50),
                min_size=0, max_size=10
            ),
            # Case 3: Empty context when original has content
            st.just({}),
            # Case 4: Different key names but same values
            st.fixed_dictionaries({
                k + "_modified": st.just(v) for k, v in encryption_context.items()
            })
        ]))
    
    # Choose algorithm suite
    algorithm_suite = draw(st.sampled_from(algorithm_suites))
    
    # Choose KMS key
    kms_key = draw(st.sampled_from(kms_keys))
    
    # Generate required encryption context keys (subset of actual keys)
    all_keys = list(encryption_context.keys())
    required_keys = draw(st.lists(
        st.sampled_from(all_keys) if all_keys else st.just(""),
        min_size=0, 
        max_size=min(len(all_keys), 5)
    ))
    
    return {
        "type": "positive-keyring",
        "description": f"Fuzzed test vector with {algorithm_suite} and {len(encryption_context)} context keys",
        "algorithmSuiteId": algorithm_suite,
        "encryptionContext": encryption_context,
        "requiredEncryptionContextKeys": required_keys,
        "encryptKeyDescription": {
            "type": "aws-kms",
            "key": kms_key
        },
        "decryptKeyDescription": {
            "type": "aws-kms", 
            "key": kms_key
        },
        "reproducedEncryptionContext": reproduced_context
    }


def generate_fuzzed_test_vectors(num_vectors: int = 5) -> Dict[str, Any]:
    """
    Generate a set of fuzzed test vectors.
    
    Args:
        num_vectors: Number of test vectors to generate
        
    Returns:
        Dictionary containing the test vectors
    """
    print(f"Generating {num_vectors} fuzzed test vectors...")
    
    test_vectors = {}
    
    for i in range(num_vectors):
        # Use Hypothesis to generate a test vector
        test_vector = fuzz_test_vector().example()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
        
        if (i + 1) % 10 == 0:
            print(f"Generated {i + 1}/{num_vectors} vectors...")
    
    return {"tests": test_vectors}


def save_test_vectors(test_vectors: Dict[str, Any], filename: str = "fuzz_test.json"):
    """
    Save test vectors to a JSON file.
    
    Args:
        test_vectors: The test vectors to save
        filename: Output filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(test_vectors, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(test_vectors['tests'])} test vectors to {filename}")


def create_fuzzed_keys_json():
    """
    Create a fuzzed keys.json file based on the existing one.
    For now, we'll use the existing keys.json as-is.
    """
    # Copy the existing keys.json
    import shutil
    import os
    
    source_keys = "../dafny/TestVectorsAwsCryptographicMaterialProviders/test/keys.json"
    target_keys = "fuzz_keys.json"
    
    if os.path.exists(source_keys):
        shutil.copy2(source_keys, target_keys)
        print(f"Copied existing keys.json to {target_keys}")
    else:
        print(f"Warning: {source_keys} not found")


def main():
    """Main function to generate fuzzed test vectors."""
    print("=== AWS Cryptographic Material Providers Fuzz Testing ===")
    print("Generating fuzzed test vectors with AWS KMS keyrings...")
    
    # Create fuzzed keys.json
    create_fuzzed_keys_json()
    
    # Generate fuzzed test vectors
    test_vectors = generate_fuzzed_test_vectors(num_vectors=5)
    
    # Save to file
    save_test_vectors(test_vectors, "fuzz_test.json")
    
    # Print some statistics
    contexts = [v.get('encryptionContext', {}) for v in test_vectors['tests'].values()]
    empty_contexts = sum(1 for c in contexts if not c)
    unicode_contexts = sum(1 for c in contexts if any(ord(char) > 127 for char in str(c)))
    
    print(f"\n=== Fuzzing Statistics ===")
    print(f"Total test vectors: {len(test_vectors['tests'])}")
    print(f"Empty encryption contexts: {empty_contexts}")
    print(f"Unicode-containing contexts: {unicode_contexts}")
    print(f"Average context size: {sum(len(c) for c in contexts) / len(contexts):.1f} key-value pairs")
    
    print(f"\n=== Next Steps ===")
    print(f"1. Run: python3 fuzz_runner.py")
    print(f"2. Check fuzz_failures.log for any failures")
    print(f"3. Examine fuzz_test.json to see generated vectors")


if __name__ == "__main__":
    main() 