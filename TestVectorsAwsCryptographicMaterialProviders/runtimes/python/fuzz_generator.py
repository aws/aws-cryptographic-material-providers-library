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
from typing import Dict, Any, List, Tuple
import hypothesis
from hypothesis import strategies as st
from hypothesis.strategies import composite

# Description templates for test vectors
DESCRIPTION_TEMPLATES = {
    "raw": "Raw keyring test with Unicode fuzzing",
    "kms": "KMS keyring test with Unicode fuzzing"
}

#TODO-Fuzztesting: #include the other KMS keys and rsa for raw keyrings (2 KMS keys, AES raw keys now); other keyring types (only positive-keyring now); other algo suites
# Key, Algorithm, Test-Type, Key-Material Definitions
KMS_KEYS = ["us-west-2-mrk", "us-east-1-mrk"]  # Just 2 KMS keys
RAW_KEY_TYPES = ["aes-128", "aes-192", "aes-256"]
KEYRING_TYPES = ["kms", "raw"]  # Only KMS and raw aes keyrings


# Key materials for raw keyrings
KEY_MATERIALS = {
    "aes-128": {"bits": 128, "material": "AAECAwQFBgcICRAREhMUFQ=="},
    "aes-192": {"bits": 192, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIj"},
    "aes-256": {"bits": 256, "material": "AAECAwQFBgcICRAREhMUFRYXGBkgISIjJCUmJygpMDE="}
}

# Algorithm suites
ALGORITHM_SUITES = [
    "0014",  # AES-128-GCM, no KDF
    "0078",  # AES-256-GCM, no KDF
    "0114",  # AES-128-GCM, HKDF-SHA256
    "0178",  # AES-256-GCM, HKDF-SHA256
]

# Below are the helper methods defined to assemble a test vector; a modular generation process for easy debugging.

def get_description_template(keyring_type: str) -> str:
    """Get description template for keyring type."""
    return DESCRIPTION_TEMPLATES.get(keyring_type, f"Fuzz test with {keyring_type} keyring")

@composite
def fuzz_key_identifiers(draw, base_key_id: str) -> Dict[str, Any]:
    """Generate fuzzed key name, namespace, and key material for raw keyrings
    Returns:
        Dictionary with key_name, key_namespace, and key_material
    """
    # Generate Unicode prefix and suffix for key name
    unicode_strategies = [
        st.text(min_size=1, max_size=10),  # Normal text
        st.text(min_size=1, max_size=10, alphabet=st.characters(categories=['So', 'Sc', 'Sk', 'Sm'])),  # Symbols
        st.text(min_size=1, max_size=10, alphabet=st.characters(categories=['Lo', 'Ll', 'Lu', 'Lm', 'Lt'])),  # Letters
        st.text(min_size=1, max_size=10, alphabet=st.characters(categories=['Nd', 'Nl', 'No'])),  # Numbers
        
        # Specific edge cases
        st.text(min_size=1, max_size=10).map(lambda s: unicodedata.normalize('NFD', s)),  # Decomposed form
        st.text(min_size=1, max_size=10).map(lambda s: unicodedata.normalize('NFC', s)),  # Composed form
    ]
    
    unicode_prefix = draw(st.one_of(unicode_strategies))
    unicode_suffix = draw(st.one_of(unicode_strategies))
    
    # Create key name with Unicode elements
    key_name = f"{unicode_prefix}-{base_key_id}-{unicode_suffix}"
    
    # Create namespace with Unicode elements
    namespace_part = draw(st.text(min_size=1, max_size=5))
    key_namespace = f"aws-raw-vectors-persistent-{unicode_prefix}-{base_key_id}-{namespace_part}"
    
    # Generate fuzzed key-id
    key_id_suffix = draw(st.one_of(unicode_strategies))
    fuzzed_key_id = f"{base_key_id}-{key_id_suffix}"
    
    # Get key material information based on the base key ID
    key_info = KEY_MATERIALS.get(base_key_id, KEY_MATERIALS["aes-256"])
    key_material = {
        "encrypt": True, 
        "decrypt": True, 
        "algorithm": "aes", 
        "type": "symmetric",
        "bits": key_info["bits"], 
        "encoding": "base64",
        "material": key_info["material"], 
        "key-id": fuzzed_key_id  # Using the fuzzed key-id
    }
    
    return {"key_name": key_name, "key_namespace": key_namespace, "key_material": key_material}

#TODO-Fuzztesting: Strengthening encryption context fuzzing with specific edge cases (close to the character limitation for encryption context (8,192)), structured patterns
@composite
def fuzz_encryption_context(draw):
    """Generate diverse encryption contexts with Unicode characters.
    
    Avoids empty strings as they're invalid for KMS operations.
    """
    num_pairs = draw(st.integers(min_value=3, max_value=10))  # Increased number of pairs
    context = {}
    
    for _ in range(num_pairs):
        # Generate Unicode keys and values (min_size=1 to avoid empty strings)
        key = draw(st.one_of(
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
        ))
        
        context[key] = value
    
    return context

#TODO-Fuzztesting: "negative-encrypt-keyring" fuzzing functionality: in fuzzToDos version, implemented tests with missing required keys (for KMS keyrings) or invalid key material (raw keryings)
# but it could also fail because of algo mismatches or invalid encryption context formats
# currently, only testing for positive-keyring
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

#TODO-Fuzztesting: ensure use of other algorithm types for raw keyrings (not just aes)
def create_raw_key_description(draw) -> Dict[str, Any]:
    """Create raw keyring description."""
    raw_key_id = draw(st.sampled_from(RAW_KEY_TYPES))
    key_identifiers = draw(fuzz_key_identifiers(raw_key_id))
    return {
        "type": "raw",
        "key": key_identifiers["key_name"],
        "provider-id": key_identifiers["key_namespace"],
        "encryption-algorithm": "aes"
    }

def create_kms_key_description(kms_key: str, required_keys: List[str]) -> Dict[str, Any]:
    """Create KMS keyring description."""
    return {
        #TODO-Fuzztesting: only considering one "type": required-encryption-context-cmm; could consider aws-kms, symmetric, rsa, etc (refer to keys.json)
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
    
    # Generate required keys
    required_keys = generate_required_keys(draw, encryption_context)
    
    # Create key descriptions
    key_description = create_key_description(draw, keyring_type, kms_key, required_keys)
    
    # Create test vector
    test_vector = {
        "type": "positive-keyring",  # Only positive test cases
        "description": get_description_template(keyring_type),
        "algorithmSuiteId": algorithm_suite,
        "encryptKeyDescription": key_description,
        "decryptKeyDescription": key_description,
        "reproducedEncryptionContext": encryption_context,  # Same as original for positive tests
        "requiredEncryptionContextKeys": required_keys,
        "encryptionContext": encryption_context
    }
    
    return test_vector

def extract_new_keys(test_vectors: Dict[str, Any]) -> Dict[str, Any]:
    """Extract new keys from raw keyring test vectors.

    - Scans all generated test vectors
    - Finds raw keyring tests (type == "raw")
    - Extracts the fuzzed key lookups they reference
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
            
            #TODO-Fuzztesting: note: currently not testing every case for type, algorithm, encoding
            key_info = KEY_MATERIALS.get(base_key_id, KEY_MATERIALS["aes-256"])
            new_keys[key_name] = {
                "encrypt": True, "decrypt": True, "algorithm": "aes", "type": "symmetric",
                "bits": key_info["bits"], "encoding": "base64",
                "material": key_info["material"], "key-id": key_name  # Using key_name as key-id for maximum fuzzing
            }
    
    return new_keys

def generate_fuzz_test_vectors(num_vectors: int = 20) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Generate multiple fuzzed test vectors and collect new key generated."""
    test_vectors = {}
    
    for i in range(num_vectors):
        test_vector = fuzz_test_vector().example()
        test_id = str(uuid.uuid4())
        test_vectors[test_id] = test_vector
    
    new_keys = extract_new_keys(test_vectors)
    return test_vectors, new_keys

#TODO-Fuzztesting: create CI and add necessary Makefile commands
#TODO-Fuzztesting: increase the number of test vectors (for CI)
#TODO-Fuzztesting: remove extraneous logging/printing statements to simplify output (for CI)
def main():
    """Main function to generate fuzzed test vectors."""
    # Generate test vectors and new keys
    test_vectors, new_keys = generate_fuzz_test_vectors(num_vectors=20)
    
    # Load and update keys.json
    try:
        with open("keys.json", "r") as f:
            keys_data = json.load(f)
    except FileNotFoundError:
        print("Error: keys.json not found!")
        return
    
    keys_data["keys"].update(new_keys)
    
    #TODO-Fuzztesting: this works for python runtime; however, this probably will not dump the JSON in the right place for all runtimes. Figure this out.
    with open("keys.json", "w") as f:
        json.dump(keys_data, f, indent=2, ensure_ascii=False)
    
    # Create and save manifest.json
    manifest_data = {
        "manifest": {"version": 4, "type": "awses-mpl-encrypt"},
        "keys": "file://keys.json",
        "tests": test_vectors
    }
    #TODO-Fuzztesting; same potential JSON directory issue as above ^^
    with open("manifest.json", "w") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(test_vectors)} test vectors with {len(new_keys)} new keys")

if __name__ == "__main__":
    main()