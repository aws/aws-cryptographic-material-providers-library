
# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Coverage-guided fuzzing runner using hypofuzz for AWS Cryptographic Material Providers Library

This script uses hypofuzz to perform coverage-guided fuzzing, which tracks code coverage
and uses that information to guide the generation of new test inputs.
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any

import hypothesis
from hypothesis import strategies as st, given, settings, HealthCheck
from hypothesis.errors import NonInteractiveExampleWarning
import warnings

# Import our existing fuzz generator components
from fuzz_generator import (
    fuzz_test_vector, 
    extract_new_keys,
    generate_fuzz_test_vectors
)

@given(test_vector=fuzz_test_vector())
@settings(
    max_examples=1000,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow, HealthCheck.data_too_large]
)
def test_coverage_guided_vector_generation(test_vector: Dict[str, Any]):
    """
    Hypothesis test for coverage-guided fuzzing.
    
    This function is designed to be run by hypofuzz, which will use coverage
    information to guide the generation of test_vector inputs to explore
    different code paths in the validation and processing logic.
    """
    # Validate the test vector structure - this creates different code paths
    # that hypofuzz will try to explore
    required_fields = ["type", "description", "algorithmSuiteId", 
                      "encryptKeyDescription", "decryptKeyDescription", "encryptionContext"]
    
    for field in required_fields:
        if field not in test_vector:
            raise ValueError(f"Missing required field: {field}")
    
    # Process different keyring types - more code paths for coverage
    key_desc = test_vector["encryptKeyDescription"]
    keyring_type = key_desc.get("type", "unknown")
    
    if keyring_type == "required-encryption-context-cmm":
        # CMM keyring path
        underlying = key_desc.get("underlying", {})
        required_keys = key_desc.get("requiredEncryptionContextKeys", [])
        enc_context = test_vector.get("encryptionContext", {})
        
        # Validate required keys are present
        for req_key in required_keys:
            if req_key not in enc_context:
                raise ValueError(f"Missing required encryption context key: {req_key}")
                
    elif keyring_type in ["raw", "raw-ecdh"]:
        # Raw keyring path
        key_id = key_desc.get("key", "")
        provider_id = key_desc.get("provider-id", "")
        
        # Different validation paths based on key characteristics
        if len(provider_id) > 200:
            raise ValueError("Provider ID too long")
        if not key_id:
            raise ValueError("Key ID cannot be empty")
            
    # Algorithm suite validation - another code path
    algorithm_suite = test_vector.get("algorithmSuiteId", "")
    if not algorithm_suite:
        raise ValueError("Algorithm suite cannot be empty")
    
    # Encryption context validation
    enc_context = test_vector.get("encryptionContext", {})
    if len(enc_context) > 100:
        raise ValueError("Too many encryption context pairs")
    
    # If we get here, the test vector is valid
    return True


def run_hypofuzz_coverage_guided(duration_seconds: int = 300, num_vectors: int = 1000):
    """
    Run coverage-guided fuzzing using hypofuzz CLI.
    
    Falls back to regular fuzzing if hypofuzz is not available.
    """
    print(f"Starting coverage-guided fuzzing for {duration_seconds} seconds...")
    
    try:
        # Try to run hypofuzz
        result = subprocess.run([
            "hypofuzz", "run",
            "--timeout", str(duration_seconds),
            "--target", "hypofuzz_runner:test_coverage_guided_vector_generation",
            "--database", "./hypofuzz_db"
        ], capture_output=True, text=True, timeout=duration_seconds + 60)
        
        if result.returncode == 0:
            print("Coverage-guided fuzzing completed successfully!")
            print("Hypofuzz output:", result.stdout)
        else:
            print("Hypofuzz failed, falling back to regular fuzzing...")
            print("Error:", result.stderr)
            raise subprocess.CalledProcessError(result.returncode, "hypofuzz")
            
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        print("Hypofuzz not available or failed, using regular fuzzing with coverage simulation...")
        
        # Fallback: use our regular fuzz generator but with more vectors
        # to simulate the broader exploration that coverage-guided fuzzing would provide
        test_vectors, new_keys = generate_fuzz_test_vectors(num_vectors)
        
        # Save results
        try:
            with open("keys.json", "r") as f:
                keys_data = json.load(f)
        except FileNotFoundError:
            print("Error: keys.json not found!")
            return
        
        keys_data["keys"].update(new_keys)
        
        with open("keys.json", "w") as f:
            json.dump(keys_data, f, indent=2, ensure_ascii=False)
        
        manifest_data = {
            "manifest": {"version": 4, "type": "awses-mpl-encrypt"},
            "keys": "file://keys.json",
            "tests": test_vectors
        }
        with open("manifest.json", "w") as f:
            json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        
        print(f"Generated {len(test_vectors)} test vectors with {len(new_keys)} new keys")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run coverage-guided fuzzing with hypofuzz')
    parser.add_argument('--duration', type=int, default=300, help='Fuzzing duration in seconds')
    parser.add_argument('--num-vectors', type=int, default=1000, help='Number of vectors for fallback mode')
    
    args = parser.parse_args()
    
    run_hypofuzz_coverage_guided(args.duration, args.num_vectors)
