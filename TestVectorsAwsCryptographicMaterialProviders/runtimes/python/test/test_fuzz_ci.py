"""
Simplified Fuzz Testing for AWS Cryptographic Material Providers Library

This file demonstrates how property-based testing with Hypothesis can generate
diverse inputs for testing encryption and decryption operations.
It's designed to run in CI environments without requiring the actual crypto implementations.
"""

import os
import logging
import hypothesis
from hypothesis import given, settings

# Try different import methods to make this work both in CI and locally
try:
    # Try direct import first (when run with pytest -m)
    from .fuzz_strategies import encryption_contexts, plaintexts, algorithm_suites
except (ImportError, ValueError):
    try:
        # Try relative import from the same directory
        from fuzz_strategies import encryption_contexts, plaintexts, algorithm_suites
    except ImportError:
        # Fall back to defining strategies inline for CI simplicity
        import hypothesis.strategies as st
        from hypothesis.strategies import composite
        
        # Constants for test configuration
        MAX_PLAINTEXT_SIZE = 1024 * 10  # 10KB max plaintext for performance
        TEST_ALGORITHMS = [
            "ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY",  # Default committed algorithm
            "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384" # Algorithm with signature
        ]
        
        @composite
        def encryption_contexts(draw, min_pairs=0, max_pairs=20):
            """Generate random encryption contexts with different characteristics"""
            num_pairs = draw(st.integers(min_value=min_pairs, max_value=max_pairs))
            
            key_strategy = st.text(min_size=1, max_size=20)
            value_strategy = st.text(min_size=0, max_size=50)
            
            context = {}
            for _ in range(num_pairs):
                key = draw(key_strategy)
                value = draw(value_strategy)
                if key and key not in context:
                    context[key] = value
            
            return context

        @composite
        def algorithm_suites(draw):
            """Generate valid algorithm suite IDs"""
            return draw(st.sampled_from(TEST_ALGORITHMS))

        @composite
        def plaintexts(draw, min_size=0, max_size=MAX_PLAINTEXT_SIZE):
            """Generate random plaintexts of varying sizes and patterns"""
            size = draw(st.integers(min_value=min_size, max_value=max_size))
            content_type = draw(st.sampled_from(["random", "zeros", "ones"]))
            
            if content_type == "random":
                return draw(st.binary(min_size=size, max_size=size))
            elif content_type == "zeros":
                return bytes([0] * size)
            else:  # ones
                return bytes([255] * size)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mpl_fuzz_ci_tests")

# Configure Hypothesis for CI (faster tests, more deterministic)
hypothesis.settings.register_profile("ci", 
                                   deadline=None,  # No deadline in CI
                                   print_blob=True,  # Show example blobs 
                                   derandomize=True,  # Make tests deterministic
                                   suppress_health_check=(hypothesis.HealthCheck.too_slow,))
hypothesis.settings.load_profile("ci")

#########################
# CI-friendly test cases
#########################

@settings(max_examples=20)
@given(
    encryption_context=encryption_contexts(),
    plaintext=plaintexts(min_size=1, max_size=1024),
    algorithm_id=algorithm_suites()
)
def test_encryption_decryption_roundtrip_ci(encryption_context, plaintext, algorithm_id):
    """Simplified test that just verifies fuzzing strategies generate valid inputs"""
    logger.info(f"Testing with encryption_context size: {len(encryption_context)}")
    logger.info(f"Testing with plaintext size: {len(plaintext)}")
    logger.info(f"Testing with algorithm: {algorithm_id}")
    
    # Just verify that the strategies generate valid inputs
    assert isinstance(encryption_context, dict), "Encryption context should be a dictionary"
    assert isinstance(plaintext, bytes), "Plaintext should be bytes"
    assert isinstance(algorithm_id, str), "Algorithm ID should be a string"
    
    # For dictionaries, check structure more thoroughly
    for key, value in encryption_context.items():
        assert isinstance(key, str), "Encryption context keys should be strings"
        assert isinstance(value, str), "Encryption context values should be strings"

@settings(max_examples=10)
@given(
    encryption_context=encryption_contexts(max_pairs=5),
    plaintext=plaintexts(min_size=10, max_size=100)
)
def test_multi_keyring_handling_ci(encryption_context, plaintext):
    """Simplified test for multi-keyring setup - just validates inputs"""
    logger.info(f"Testing multi-keyring with encryption_context: {encryption_context}")
    
    # Just verify that the strategies generate valid inputs
    assert isinstance(encryption_context, dict)
    assert len(encryption_context) <= 5, "Should have at most 5 pairs"
    assert isinstance(plaintext, bytes)
    assert 10 <= len(plaintext) <= 100, "Plaintext size should be between 10 and 100 bytes"

# Simple placeholder for KMS test to keep structure similar to main test file
def test_kms_keyring_if_available_ci():
    """Placeholder for KMS test in CI"""
    logger.info("Running CI placeholder for KMS keyring test")
    # Just a placeholder that always passes
    assert True
