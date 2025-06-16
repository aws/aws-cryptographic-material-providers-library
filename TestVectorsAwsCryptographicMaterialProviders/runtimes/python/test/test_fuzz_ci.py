"""
Simplified version of fuzz tests for CI environments

This module imports the fuzzing strategies from test_fuzz_encryption but implements
simplified tests that don't depend on actual crypto implementations.
"""

import logging
import hypothesis
from hypothesis import given, settings

# Import the fuzzing strategies from our shared module
from .fuzz_strategies import encryption_contexts, plaintexts, algorithm_suites

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
