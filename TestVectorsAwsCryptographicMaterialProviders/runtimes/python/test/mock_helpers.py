#!/usr/bin/env python3
"""
Mock helpers for testing when actual implementations aren't available
"""
from unittest.mock import MagicMock

# Create mock classes for testing
class MockMaterialProviders:
    def __init__(self):
        self.create_raw_aes_keyring = MagicMock(return_value=MockKeyring())
        self.create_multi_keyring = MagicMock(return_value=MockKeyring())
        self.create_default_cryptographic_materials_manager = MagicMock(return_value=MockCMM())
        
class MockKeyring:
    def __init__(self):
        pass

class MockCMM:
    def __init__(self):
        self.get_encryption_materials = MagicMock(return_value=MockEncryptionMaterials())
        self.decrypt_materials = MagicMock(return_value=MockDecryptionMaterials())

class MockEncryptionMaterials:
    def __init__(self):
        self.encryption_materials = MagicMock()
        self.encryption_materials.plaintext_data_key = b'mock_plaintext_key'
        self.encryption_materials.encrypted_data_keys = ['mock_encrypted_key']
        self.encryption_materials.encryption_context = {}
        self.encryption_materials.algorithm_suite = MagicMock()
        self.encryption_materials.algorithm_suite.id = 'mock_algorithm_suite_id'
        self.encryption_materials.required_encryption_context_keys = []

class MockDecryptionMaterials:
    def __init__(self):
        self.decryption_materials = MagicMock()
        self.decryption_materials.plaintext_data_key = b'mock_plaintext_key'

# Mock classes for the internal Dafny-generated modules
class MockDefaultMaterialProvidersConfig:
    pass

class MockInternalMaterialProviders:
    class default__:
        @staticmethod
        def MaterialProviders(config):
            class Success:
                def is_Failure(self):
                    return False
                
                def get_Success(self):
                    from mock_helpers import MockMaterialProviders
                    return MockMaterialProviders()
                
            return Success()
        
        @staticmethod
        def DefaultMaterialProvidersConfig():
            return MockDefaultMaterialProvidersConfig()

# Function to patch import errors
def patch_module_imports():
    """Patch module imports that might fail in the test environment"""
    import sys
    from unittest.mock import MagicMock
    
    class MockModule:
        def __getattr__(self, name):
            return MagicMock()
    
    # List of modules to mock if they don't exist
    modules_to_mock = [
        'aws_cryptographic_material_providers',
        'aws_cryptographic_material_providers.smithygenerated',
        'aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders',
        'aws_cryptographic_material_providers.internaldafny',
        'aws_cryptographic_material_providers.internaldafny.generated',
        'aws_cryptographic_material_providers.internaldafny.generated.module_'
    ]
    
    for module_name in modules_to_mock:
        try:
            __import__(module_name)
        except ImportError:
            sys.modules[module_name] = MockModule()
    
    # Create specific mock for the internaldafny MaterialProviders
    module = sys.modules.get('aws_cryptographic_material_providers.internaldafny.generated', MockModule())
    # Add the MaterialProviders class that's imported directly in the test
    module.MaterialProviders = MockInternalMaterialProviders
    sys.modules['aws_cryptographic_material_providers.internaldafny.generated'] = module
    
    # Create a mock for the main MaterialProviders class
    try:
        from aws_cryptographic_material_providers.mpl import AwsCryptographicMaterialProviders
    except (ImportError, AttributeError):
        sys.modules['aws_cryptographic_material_providers.mpl'] = MockModule()
        sys.modules['aws_cryptographic_material_providers.mpl'].AwsCryptographicMaterialProviders = MockMaterialProviders
