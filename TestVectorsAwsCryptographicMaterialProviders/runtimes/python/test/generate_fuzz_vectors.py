#!/usr/bin/env python3

"""
Generate fuzzed test vectors for the AWS Cryptographic Material Providers Library.

This script uses Hypothesis to generate a large number of test vectors with
diverse inputs for encryption contexts, plaintexts, and algorithm suites.
The vectors are saved in a JSON manifest format that can be used with the
existing test commands.
"""

import argparse
import base64
import json
import os
import sys
import unicodedata
from dataclasses import dataclass
from typing import Dict, List, Optional

import hypothesis
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy


@st.composite
def encryption_contexts(draw, min_pairs=0, max_pairs=20):
    """Generate random encryption contexts with different characteristics."""
    num_pairs = draw(st.integers(min_value=min_pairs, max_value=max_pairs))
    
    # Define strategies for keys and values
    key_strategies = {
        "normal": st.text(min_size=1, max_size=20),
        "empty": st.just(""),
        "long": st.text(min_size=50, max_size=100),
        "special": st.text(alphabet="!@#$%^&*()_+-=[]{}|;':\",./<>?", min_size=1, max_size=20),
        "unicode": st.text(alphabet=st.characters(categories=('L',)), min_size=1, max_size=10),
        "numeric": st.text(alphabet="0123456789", min_size=1, max_size=10),
    }
    
    value_strategies = {
        "normal": st.text(min_size=1, max_size=20),
        "empty": st.just(""),
        "long": st.text(min_size=50, max_size=100),
        "binary": st.binary(min_size=1, max_size=20).map(lambda b: base64.b64encode(b).decode('ascii')),
        "unicode": st.text(alphabet=st.characters(categories=('L',)), min_size=1, max_size=10),
    }
    
    context = {}
    for _ in range(num_pairs):
        key_type = draw(st.sampled_from(list(key_strategies.keys())))
        value_type = draw(st.sampled_from(list(value_strategies.keys())))
        
        key = draw(key_strategies[key_type])
        value = draw(value_strategies[value_type])
        
        # Ensure keys don't collide
        unique_key = f"{key}_{_}" if key in context else key
        context[unique_key] = value
    
    return context


@st.composite
def unicode_encryption_contexts(draw):
    """Generate encryption contexts specifically focused on Unicode edge cases."""
    num_pairs = draw(st.integers(min_value=1, max_value=10))
    context = {}
    
    # Unicode character categories to test
    categories = [
        ('L',),  # Letters
        ('Mn',), # Non-spacing marks
        ('Zs',), # Spaces
        # ('Cs',), # Surrogates - removed as they cause JSON serialization issues
        ('Co',), # Private use
        ('Cf',), # Format characters
    ]
    
    # Characters known to cause normalization issues
    problematic_chars = [
        '\u2028',  # Line separator
        '\u2029',  # Paragraph separator
        '\u200B',  # Zero-width space
        '\u200D',  # Zero-width joiner
        '\u200E',  # Left-to-right mark
        '\u0000',  # Null character
        '\uFEFF',  # Byte order mark
        '\uFFFF',  # Highest BMP code point
        '\U0001F600',  # Emoji (outside BMP)
    ]
    
    for _ in range(num_pairs):
        # Decide what kind of test case to generate
        case_type = draw(st.sampled_from([
            "normal_unicode",
            "problematic_char",
            "normalized_pair",
            "combining_chars",
            "emoji_sequences"
        ]))
        
        if case_type == "normal_unicode":
            category = draw(st.sampled_from(categories))
            key = draw(st.text(alphabet=st.characters(categories=category), min_size=1, max_size=10))
            value = draw(st.text(alphabet=st.characters(categories=category), min_size=1, max_size=20))
        elif case_type == "problematic_char":
            key = draw(st.text(min_size=0, max_size=5)) + draw(st.sampled_from(problematic_chars))
            value = draw(st.text(min_size=0, max_size=5)) + draw(st.sampled_from(problematic_chars))
        elif case_type == "normalized_pair":
            # Generate pre-composed/decomposed pairs (NFC/NFD normalization forms)
            base = draw(st.sampled_from(["a", "e", "i", "o", "u"]))
            # e.g. "á" (U+00E1) vs "a" + combining acute (U+0061 + U+0301)
            key1 = base + '\u0301'  # Adding combining acute accent
            key2 = unicodedata.normalize('NFC', key1)  # Pre-composed form
            key = draw(st.sampled_from([key1, key2]))
            value = draw(st.text(min_size=1, max_size=10))
        elif case_type == "combining_chars":
            # Generate strings with multiple combining characters
            base_char = draw(st.sampled_from(["a", "e", "i", "o", "u"]))
            num_combining = draw(st.integers(min_value=1, max_value=5))
            combining_chars = ['\u0301', '\u0302', '\u0303', '\u0304', '\u0305']
            key = base_char + ''.join(draw(st.sampled_from(combining_chars)) for _ in range(num_combining))
            value = draw(st.text(min_size=1, max_size=10))
        else:  # emoji_sequences
            # Generate emoji sequences including ZWJ sequences
            emojis = ['\U0001F600', '\U0001F601', '\U0001F602', '\U0001F923']
            zwj = '\u200D'
            key = draw(st.sampled_from(emojis))
            if draw(st.booleans()):
                key += zwj + draw(st.sampled_from(emojis))
            value = draw(st.text(min_size=1, max_size=10))
            
        # Ensure keys don't collide
        unique_key = f"{key}_{_}" if key in context else key
        context[unique_key] = value
        
    return context


@st.composite
def plaintexts(draw, min_size=0, max_size=1024):
    """Generate random plaintexts with different characteristics."""
    pattern = draw(st.sampled_from([
        "empty",
        "random",
        "repeating",
        "zeros"
    ]))
    
    if pattern == "empty":
        return b""
    elif pattern == "random":
        return draw(st.binary(min_size=min_size, max_size=max_size))
    elif pattern == "repeating":
        base = draw(st.binary(min_size=1, max_size=10))
        repeat = draw(st.integers(1, 100))
        return base * repeat
    else:  # zeros
        length = draw(st.integers(1, max_size))
        return b"\x00" * length


def algorithm_suites() -> SearchStrategy:
    """Generate valid algorithm suite identifiers."""
    return st.sampled_from([
        "ALG_AES_128_GCM_IV12_TAG16_NO_KDF",
        "ALG_AES_192_GCM_IV12_TAG16_NO_KDF",
        "ALG_AES_256_GCM_IV12_TAG16_NO_KDF",
        "ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256",
        "ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256",
        "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256",
        "ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256",
        "ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384",
        "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384",
    ])


@dataclass
class TestVector:
    """Represents a test vector for encryption/decryption testing."""
    id: str
    encryption_context: Dict[str, str]
    plaintext: bytes
    algorithm_suite: str

    def to_json(self) -> dict:
        """Convert the test vector to a JSON-serializable dictionary."""
        return {
            "id": self.id,
            "encryption_context": self.encryption_context,
            "plaintext": base64.b64encode(self.plaintext).decode('ascii'),
            "algorithm_suite": self.algorithm_suite
        }


def generate_test_vectors(num_vectors: int, include_unicode_tests: bool = True) -> List[TestVector]:
    """Generate test vectors using Hypothesis strategies."""
    vectors = []
    
    # Use Hypothesis to generate test vectors
    @hypothesis.settings(max_examples=num_vectors, deadline=None)
    @hypothesis.given(
        encryption_context=encryption_contexts(),
        plaintext=plaintexts(),
        algorithm_suite=algorithm_suites()
    )
    def add_vector(encryption_context, plaintext, algorithm_suite):
        nonlocal vectors
        vector_id = f"vector_{len(vectors):06d}"
        vectors.append(TestVector(
            id=vector_id,
            encryption_context=encryption_context,
            plaintext=plaintext,
            algorithm_suite=algorithm_suite
        ))
    
    # Generate regular test vectors
    add_vector()
    
    # Optionally add specialized Unicode test vectors
    if include_unicode_tests:
        unicode_vectors = []
        
        # Ensure at least 1 Unicode vector, but no more than 20% of total
        unicode_count = max(1, num_vectors // 5)  
        @hypothesis.settings(max_examples=unicode_count, deadline=None)
        @hypothesis.given(
            encryption_context=unicode_encryption_contexts(),
            plaintext=st.binary(min_size=1, max_size=100),
            algorithm_suite=algorithm_suites()
        )
        def add_unicode_vector(encryption_context, plaintext, algorithm_suite):
            nonlocal unicode_vectors
            vector_id = f"unicode_vector_{len(unicode_vectors):06d}"
            unicode_vectors.append(TestVector(
                id=vector_id,
                encryption_context=encryption_context,
                plaintext=plaintext,
                algorithm_suite=algorithm_suite
            ))
        
        add_unicode_vector()
        vectors.extend(unicode_vectors)
    
    return vectors


def create_manifest(vectors: List[TestVector], output_dir: str, filename: str = "manifest.json") -> str:
    """Create a manifest file from test vectors."""
    manifest = {
        "type": "awses-decrypt-verify",
        "version": 1,
        "tests": [v.to_json() for v in vectors]
    }
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write manifest to file
    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    return output_path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate fuzzed test vectors.')
    parser.add_argument('--num-vectors', type=int, default=1000,
                      help='Number of test vectors to generate')
    parser.add_argument('--output-dir', type=str, default='.',
                      help='Directory to write test vectors to')
    parser.add_argument('--filename', type=str, default='manifest.json',
                      help='Filename for the manifest')
    parser.add_argument('--no-unicode', action='store_true',
                      help='Disable Unicode-specific test vectors')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    
    print(f"Generating {args.num_vectors} test vectors...")
    vectors = generate_test_vectors(args.num_vectors, not args.no_unicode)
    
    manifest_path = create_manifest(vectors, args.output_dir, args.filename)
    print(f"Successfully wrote {len(vectors)} test vectors to {manifest_path}")
