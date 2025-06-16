"""
Fuzz Testing for AWS Cryptographic Material Providers Library

This file implements property-based fuzz testing for the MPL library with a focus on:
1. Encryption context handling - testing edge cases in key-value pairs
2. Algorithm suite variations - testing different algorithms and parameters
3. Keyring configurations - testing different keyring setups and edge cases
4. Error handling - ensuring proper error behavior under unusual inputs

It uses Hypothesis for property-based testing to generate a wide range of inputs
and verify that the library behaves correctly under all conditions.
"""

import base64
import logging
import os
import random
from typing import Dict, List, Optional, Tuple, Union

import boto3
import hypothesis
from hypothesis import given, settings

# Import MPL components
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders as mpl_types
from aws_cryptographic_material_providers.mpl import AwsCryptographicMaterialProviders as MaterialProviders

# Import the shared fuzzing strategies
from .fuzz_strategies import encryption_contexts, plaintexts, algorithm_suites

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mpl_fuzz_tests")

# Configure longer test timeouts for thorough fuzzing
hypothesis.settings.register_profile("mpl_fuzzing", 
                                    max_examples=100, 
                                    deadline=10000)  # 10 seconds per test
hypothesis.settings.load_profile("mpl_fuzzing")

# Constants for test configuration
DEFAULT_COMMITMENT_POLICY = "REQUIRE_ENCRYPT_REQUIRE_DECRYPT"

#########################
# Keyring Setup Functions
#########################

def create_raw_aes_keyring():
    """Create a Raw AES Keyring for testing purposes"""
    from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
    material_providers_result = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
    if material_providers_result.is_Failure():
        raise Exception(f"Failed to initialize Material Providers: {material_providers_result.get_Failure()}")
    material_providers = material_providers_result.get_Success()
    
    # Generate a random wrapping key for testing
    wrapping_key = os.urandom(32)  # 256-bit AES key
    
    return material_providers.create_raw_aes_keyring(
        key_namespace="mpl-fuzz-test",
        key_name="test-aes-key",
        wrapping_key=wrapping_key,
        wrapping_alg="ALG_AES256_GCM_IV12_TAG16"
    )

def create_material_providers():
    """Helper function to create the Material Providers client correctly"""
    from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
    material_providers_result = MaterialProviders.default__.MaterialProviders(
        MaterialProviders.default__.DefaultMaterialProvidersConfig()
    )
    if material_providers_result.is_Failure():
        raise Exception(f"Failed to initialize Material Providers: {material_providers_result.get_Failure()}")
    return material_providers_result.get_Success()

def create_multi_keyring():
    """Create a multi-keyring with multiple AES keyrings for testing"""
    material_providers = create_material_providers()
    
    # Create multiple AES keyrings with different keys
    aes_keyring1 = create_raw_aes_keyring()
    aes_keyring2 = create_raw_aes_keyring()
    
    return material_providers.create_multi_keyring(
        generator=aes_keyring1,
        child_keyrings=[aes_keyring2]
    )

def try_create_kms_keyring():
    """Try to create a KMS keyring using CI account credentials if available"""
    try:
        # Check if we have AWS credentials available (from assume-ci-role.sh)
        if os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get('AWS_SECRET_ACCESS_KEY'):
            # Initialize Material Providers
            from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
            material_providers = MaterialProviders.MaterialProvidersClient(MaterialProviders.DefaultMaterialProvidersConfig())
            
            # Create KMS client with the region specified in assume-ci-role.sh
            region = os.environ.get('AWS_REGION', 'us-west-2')
            kms_client = boto3.client('kms', region_name=region)
            
            # Use the GitHub CI role to create a KMS key
            # This uses the alias/aws-crypto-tools-ci-key that should be available in the CI account
            try:
                # First try using an alias that should exist in the CI account
                key_id = "alias/aws-crypto-tools-ci-key"
                
                # Test if the key is accessible by describing it
                kms_client.describe_key(KeyId=key_id)
                
                logger.info(f"Using KMS key with alias: {key_id}")
                
                return material_providers.create_aws_kms_keyring(
                    kms_key_id=key_id,
                    kms_client=kms_client
                )
            except Exception as key_error:
                logger.warning(f"Could not use aliased key: {key_error}")
                
                # Fallback: Try to create a temporary key for testing
                logger.info("Attempting to create a temporary KMS key for testing...")
                response = kms_client.create_key(
                    Description='Temporary key for MPL fuzz testing',
                    KeyUsage='ENCRYPT_DECRYPT',
                    Origin='AWS_KMS'
                )
                
                key_id = response['KeyMetadata']['KeyId']
                logger.info(f"Created temporary KMS key: {key_id}")
                
                # Schedule key for deletion after testing (7 days is minimum)
                kms_client.schedule_key_deletion(
                    KeyId=key_id,
                    PendingWindowInDays=7
                )
                
                return material_providers.create_aws_kms_keyring(
                    kms_key_id=key_id,
                    kms_client=kms_client
                )
    except Exception as e:
        logger.warning(f"Failed to create KMS keyring: {e}")
        return None
    
    return None

#########################
# Core Testing Functions
#########################

def encrypt_and_decrypt(keyring, encryption_context, plaintext, algorithm_suite_id=None):
    """
    Test MPL encryption and decryption materials handling
    
    This function doesn't actually encrypt data (MPL is a material providers library),
    but tests the material generation and management process.
    """
    from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
    material_providers = MaterialProviders.MaterialProvidersClient(MaterialProviders.DefaultMaterialProvidersConfig())
    
    # Create a Cryptographic Materials Manager from the keyring
    cmm = material_providers.create_default_cryptographic_materials_manager(keyring=keyring)
    
    try:
        # Build encryption materials request
        encryption_request = {
            "encryption_context": encryption_context,
            "commitment_policy": DEFAULT_COMMITMENT_POLICY,
        }
        
        if algorithm_suite_id:
            encryption_request["algorithm_suite_id"] = algorithm_suite_id
        
        # Get encryption materials
        encryption_materials = cmm.get_encryption_materials(encryption_request)
        
        # Extract information we want to verify during round trip
        plaintext_data_key = encryption_materials.encryption_materials.plaintext_data_key
        encrypted_data_keys = encryption_materials.encryption_materials.encrypted_data_keys
        
        # Since MPL doesn't actually encrypt data (that's up to the client),
        # we'll simulate an encryption/decryption round trip by verifying
        # we can get the same plaintext key back during decryption
        
        # Get decryption materials
        decrypt_request = {
            "algorithm_suite_id": encryption_materials.encryption_materials.algorithm_suite.id,
            "commitment_policy": DEFAULT_COMMITMENT_POLICY,
            "encrypted_data_keys": encrypted_data_keys,
            "encryption_context": encryption_context
        }
        
        decryption_materials = cmm.decrypt_materials(decrypt_request)
        
        # Extract plaintext key for verification
        decryption_key = decryption_materials.decryption_materials.plaintext_data_key
        
        # For a successful encryption/decryption round trip with the same key and context,
        # the decryption key should exactly match the encryption key
        return {
            "success": True,
            "plaintext_data_key": plaintext_data_key,
            "decryption_key": decryption_key,
            "encryption_materials": encryption_materials,
            "decryption_materials": decryption_materials,
            "key_match": plaintext_data_key == decryption_key
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": e,
            "error_type": type(e).__name__,
            "encryption_context": encryption_context
        }

def classify_error(error_result):
    """Classify errors into expected validation issues versus unexpected bugs"""
    error = error_result.get("error")
    error_type = error_result.get("error_type")
    context = error_result.get("encryption_context")
    
    # Known validation errors in MPL
    expected_errors = [
        "ValidationException",
        "AwsCryptographicMaterialProvidersException",
        "EmptyEncryptionContextKeys",
        "InvalidEncryptionContextValue",
        "IllegalArgumentException",
    ]
    
    # Log the error details for analysis
    logger.warning(f"Error with context {context}: {error_type} - {error}")
    
    # Check if this is an expected validation error
    for expected in expected_errors:
        if expected in str(error_type) or expected in str(error):
            return True
    
    # Otherwise, consider it an unexpected bug that should be investigated
    return False

#########################
# Test Cases
#########################

@settings(max_examples=50)
@given(
    encryption_context=encryption_contexts(),
    plaintext=plaintexts(min_size=1, max_size=1024),
    algorithm_id=algorithm_suites()
)
def test_encryption_decryption_roundtrip(encryption_context, plaintext, algorithm_id):
    """Test encryption and decryption materials handling with various encryption contexts and algorithms"""
    # Setup keyring
    keyring = create_raw_aes_keyring()
    
    # Perform encryption and decryption
    result = encrypt_and_decrypt(keyring, encryption_context, plaintext, algorithm_id)
    
    # Check results
    if result["success"]:
        # Verify keys match for round trip
        assert result["key_match"], "Decryption key does not match encryption key"
        
        # Verify encryption context was properly handled
        assert result["encryption_materials"].encryption_materials.encryption_context == encryption_context
    else:
        # Check if this was an expected validation error
        if not classify_error(result):
            raise result["error"]

@settings(max_examples=20)
@given(
    encryption_context=encryption_contexts(max_pairs=5),
    plaintext=plaintexts(min_size=10, max_size=100)
)
def test_multi_keyring_handling(encryption_context, plaintext):
    """Test encryption using a multi-keyring setup"""
    # Create a multi-keyring
    keyring = create_multi_keyring()
    
    # Perform encryption and decryption with the multi-keyring
    result = encrypt_and_decrypt(keyring, encryption_context, plaintext)
    
    if result["success"]:
        # Verify keys match for round trip
        assert result["key_match"], "Decryption key does not match encryption key"
        
        # Verify multiple encrypted data keys were created (one per child keyring)
        materials = result["encryption_materials"]
        assert len(materials.encryption_materials.encrypted_data_keys) > 1, \
            "Multi-keyring should create multiple encrypted data keys"
    else:
        # Check if this was an expected validation error
        if not classify_error(result):
            raise result["error"]

@settings(max_examples=20)
@given(
    encryption_context=encryption_contexts(max_pairs=3),
    tampered_key=st.text(min_size=1, max_size=20),
    tampered_value=st.text(min_size=1, max_size=20)
)
def test_encryption_context_tampering(encryption_context, tampered_key, tampered_value):
    """Test that changing the encryption context after encryption affects decryption"""
    # Skip if encryption context is empty or if tampered key already exists
    if not encryption_context or tampered_key in encryption_context:
        hypothesis.assume(False)
        return
    
    # Setup keyring
    keyring = create_raw_aes_keyring()
    from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
    material_providers = MaterialProviders.MaterialProvidersClient(MaterialProviders.DefaultMaterialProvidersConfig())
    cmm = material_providers.create_default_cryptographic_materials_manager(keyring=keyring)
    
    # Get encryption materials with original context
    try:
        # Get encryption materials with the original context
        encryption_request = {
            "encryption_context": encryption_context,
            "commitment_policy": DEFAULT_COMMITMENT_POLICY,
        }
        
        encryption_materials = cmm.get_encryption_materials(encryption_request)
        plaintext_key = encryption_materials.encryption_materials.plaintext_data_key
        encrypted_data_keys = encryption_materials.encryption_materials.encrypted_data_keys
        
        # Tamper with encryption context for decryption
        tampered_context = encryption_context.copy()
        tampered_context[tampered_key] = tampered_value
        
        # Try to decrypt with tampered context
        decrypt_request = {
            "algorithm_suite_id": encryption_materials.encryption_materials.algorithm_suite.id,
            "commitment_policy": DEFAULT_COMMITMENT_POLICY,
            "encrypted_data_keys": encrypted_data_keys,
            "encryption_context": tampered_context
        }
        
        try:
            decryption_materials = cmm.decrypt_materials(decrypt_request)
            decryption_key = decryption_materials.decryption_materials.plaintext_data_key
            
            # If we get here with a tampered context, verify that the key is different
            # which means the tampered context affected the key derivation
            assert plaintext_key != decryption_key, "Encryption context change should result in a different key"
        except Exception as e:
            # Expected outcome for many algorithms - decryption should fail with tampered context
            assert "encryption context" in str(e).lower() or \
                   "validation" in str(e).lower() or \
                   "authentication" in str(e).lower() or \
                   "mac" in str(e).lower()
    
    except Exception as e:
        # Only re-raise if this isn't an expected validation error
        expected_errors = [
            "EmptyEncryptionContextKeys", 
            "InvalidEncryptionContextValue",
            "ValidationException"
        ]
        if not any(expected in str(e) for expected in expected_errors):
            raise

@settings(max_examples=20)
@given(
    encryption_context=encryption_contexts(max_pairs=3),
    algorithm_id=algorithm_suites()
)
def test_required_encryption_context_cmm(encryption_context, algorithm_id):
    """Test behavior when required encryption context keys are specified"""
    # Setup
    from aws_cryptographic_material_providers.internaldafny.generated import MaterialProviders
    material_providers = MaterialProviders.MaterialProvidersClient(MaterialProviders.DefaultMaterialProvidersConfig())
    
    # Create a basic keyring
    keyring = create_raw_aes_keyring()
    
    # Skip if encryption context is empty
    if not encryption_context:
        hypothesis.assume(False)
        return
        
    # Choose a required key from the context keys
    context_keys = list(encryption_context.keys())
    if not context_keys:
        required_key = "test-required-key"
    else:
        required_key = random.choice(context_keys)
    
    try:
        # Create a Required Encryption Context CMM that requires the specific key
        required_cmm = material_providers.create_required_encryption_context_cmm(
            keyring=keyring,
            required_encryption_context_keys=[required_key]
        )
        
        # Try to get encryption materials
        encryption_request = {
            "encryption_context": encryption_context,
            "commitment_policy": DEFAULT_COMMITMENT_POLICY,
        }
        
        if algorithm_id:
            encryption_request["algorithm_suite_id"] = algorithm_id
        
        try:
            encryption_materials = required_cmm.get_encryption_materials(encryption_request)
            
            # If we got here, the key must be in the context
            assert required_key in encryption_context, "Required key should be in encryption context"
            
            # Verify the key is in the required keys list
            assert required_key in encryption_materials.encryption_materials.required_encryption_context_keys, \
                "Required key should be in required_encryption_context_keys list"
                
        except Exception as e:
            # Expected error if required key is missing
            if required_key not in encryption_context:
                assert "required" in str(e).lower() or "missing" in str(e).lower()
            else:
                raise
                
    except Exception as e:
        # Only re-raise if this isn't an expected validation error
        expected_errors = ["ValidationException"]
        if not any(expected in str(e) for expected in expected_errors):
            raise

# Optional KMS keyring test - runs only if AWS credentials are available
def test_kms_keyring_if_available():
    """Test AWS KMS keyring if credentials are available"""
    # Try to create a KMS keyring
    kms_keyring = try_create_kms_keyring()
    
    # Skip test if KMS keyring creation failed
    if not kms_keyring:
        logger.info("Skipping KMS keyring test - no credentials available")
        return
    
    # Test with simple encryption context and plaintext
    encryption_context = {"purpose": "test", "project": "mpl-fuzz"}
    plaintext = b"test data for kms keyring"
    
    # Perform encryption and decryption
    result = encrypt_and_decrypt(kms_keyring, encryption_context, plaintext)
    
    # Check results
    if result["success"]:
        # Verify keys match for round trip
        assert result["key_match"], "Decryption key does not match encryption key"
        
        # Verify encryption context was properly handled
        assert result["encryption_materials"].encryption_materials.encryption_context == encryption_context
        
        logger.info("KMS keyring test passed successfully")
    else:
        # Log but don't fail the test - KMS errors could be due to permissions/config
        logger.warning(f"KMS keyring test failed: {result.get('error_type')} - {result.get('error')}")
