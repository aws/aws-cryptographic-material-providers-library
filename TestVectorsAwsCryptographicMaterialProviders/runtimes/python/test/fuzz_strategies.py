"""
Shared fuzzing strategies for AWS Cryptographic Material Providers Library

This module provides Hypothesis strategies for generating test inputs that can be
used by both the main fuzzing tests and CI-friendly tests.
"""
import logging
from typing import Dict, List, Optional, Tuple, Union
from hypothesis import strategies as st
from hypothesis.strategies import composite

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mpl_fuzz_strategies")

# Constants for test configuration
MAX_PLAINTEXT_SIZE = 1024 * 10  # 10KB max plaintext for performance
TEST_ALGORITHMS = [
    "ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY",  # Default committed algorithm
    "ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384" # Algorithm with signature
]

#########################
# Strategy Generators
#########################

@composite
def encryption_contexts(draw, min_pairs=0, max_pairs=20):
    """Generate random encryption contexts with different characteristics"""
    num_pairs = draw(st.integers(min_value=min_pairs, max_value=max_pairs))
    
    # Define strategies for keys and values
    key_strategies = {
        "normal": st.text(min_size=1, max_size=20, alphabet=st.characters(blacklist_categories=('Cs',))),
        "empty": st.just(""),
        "long": st.text(min_size=50, max_size=100),
        "special": st.text(alphabet="!@#$%^&*()_+-=[]{}|;':\",./<>?", min_size=1, max_size=20),
        "unicode": st.text(alphabet=st.characters(categories=('L',)), min_size=1, max_size=10),
        "numeric": st.text(alphabet="0123456789", min_size=1, max_size=10),
    }
    
    value_strategies = {
        "normal": st.text(min_size=1, max_size=50),
        "empty": st.just(""),
        "long": st.text(min_size=50, max_size=100),
        "binary_safe": st.text(alphabet=st.characters(blacklist_categories=('Cc', 'Cs'))),
        "numeric": st.text(alphabet="0123456789", min_size=1, max_size=20),
    }
    
    context = {}
    for _ in range(num_pairs):
        key_type = draw(st.sampled_from(list(key_strategies.keys())))
        key = draw(key_strategies[key_type])
        
        value_type = draw(st.sampled_from(list(value_strategies.keys())))
        value = draw(value_strategies[value_type])
        
        if key and key not in context:  # Only add non-empty keys to avoid dict errors
            context[key] = value
    
    return context

@composite
def algorithm_suites(draw):
    """Generate valid algorithm suite IDs with varying properties"""
    algorithm_id = draw(st.sampled_from(TEST_ALGORITHMS))
    
    # For MPL, algorithm suite IDs are typically passed as strings
    return algorithm_id

@composite
def plaintexts(draw, min_size=0, max_size=MAX_PLAINTEXT_SIZE):
    """Generate random plaintexts of varying sizes and patterns"""
    size_strategy = st.integers(min_value=min_size, max_value=max_size)
    content_type = draw(st.sampled_from(["random", "pattern", "zeros", "ones"]))
    size = draw(size_strategy)
    
    if content_type == "random":
        return draw(st.binary(min_size=size, max_size=size))
    elif content_type == "pattern":
        pattern = draw(st.binary(min_size=1, max_size=10))
        repeats = size // len(pattern) + 1
        return (pattern * repeats)[:size]
    elif content_type == "zeros":
        return bytes([0] * size)
    else:  # ones
        return bytes([255] * size)
