# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders import (
    MaterialProvidersClient,
)
from .dafny_protocol import DafnyRequest


class DafnyImplInterface:
    impl: MaterialProvidersClient | None = None

    # operation_map cannot be created at dafnyImplInterface create time,
    # as the map's values reference values inside `self.impl`,
    # and impl is only populated at runtime.
    # Accessing these before impl is populated results in an error.
    # At runtime, the map is populated once and cached.
    operation_map = None

    def handle_request(self, input: DafnyRequest):
        if self.operation_map is None:
            self.operation_map = {
                "CreateAwsKmsKeyring": self.impl.CreateAwsKmsKeyring,
                "CreateAwsKmsDiscoveryKeyring": self.impl.CreateAwsKmsDiscoveryKeyring,
                "CreateAwsKmsMultiKeyring": self.impl.CreateAwsKmsMultiKeyring,
                "CreateAwsKmsDiscoveryMultiKeyring": self.impl.CreateAwsKmsDiscoveryMultiKeyring,
                "CreateAwsKmsMrkKeyring": self.impl.CreateAwsKmsMrkKeyring,
                "CreateAwsKmsMrkMultiKeyring": self.impl.CreateAwsKmsMrkMultiKeyring,
                "CreateAwsKmsMrkDiscoveryKeyring": self.impl.CreateAwsKmsMrkDiscoveryKeyring,
                "CreateAwsKmsMrkDiscoveryMultiKeyring": self.impl.CreateAwsKmsMrkDiscoveryMultiKeyring,
                "CreateAwsKmsHierarchicalKeyring": self.impl.CreateAwsKmsHierarchicalKeyring,
                "CreateAwsKmsRsaKeyring": self.impl.CreateAwsKmsRsaKeyring,
                "CreateAwsKmsEcdhKeyring": self.impl.CreateAwsKmsEcdhKeyring,
                "CreateMultiKeyring": self.impl.CreateMultiKeyring,
                "CreateRawAesKeyring": self.impl.CreateRawAesKeyring,
                "CreateRawRsaKeyring": self.impl.CreateRawRsaKeyring,
                "CreateRawEcdhKeyring": self.impl.CreateRawEcdhKeyring,
                "CreateDefaultCryptographicMaterialsManager": self.impl.CreateDefaultCryptographicMaterialsManager,
                "CreateRequiredEncryptionContextCMM": self.impl.CreateRequiredEncryptionContextCMM,
                "CreateCryptographicMaterialsCache": self.impl.CreateCryptographicMaterialsCache,
                "CreateDefaultClientSupplier": self.impl.CreateDefaultClientSupplier,
                "InitializeEncryptionMaterials": self.impl.InitializeEncryptionMaterials,
                "InitializeDecryptionMaterials": self.impl.InitializeDecryptionMaterials,
                "ValidEncryptionMaterialsTransition": self.impl.ValidEncryptionMaterialsTransition,
                "ValidDecryptionMaterialsTransition": self.impl.ValidDecryptionMaterialsTransition,
                "EncryptionMaterialsHasPlaintextDataKey": self.impl.EncryptionMaterialsHasPlaintextDataKey,
                "DecryptionMaterialsWithPlaintextDataKey": self.impl.DecryptionMaterialsWithPlaintextDataKey,
                "GetAlgorithmSuiteInfo": self.impl.GetAlgorithmSuiteInfo,
                "ValidAlgorithmSuiteInfo": self.impl.ValidAlgorithmSuiteInfo,
                "ValidateCommitmentPolicyOnEncrypt": self.impl.ValidateCommitmentPolicyOnEncrypt,
                "ValidateCommitmentPolicyOnDecrypt": self.impl.ValidateCommitmentPolicyOnDecrypt,
            }

        # This logic is where a typical Smithy client would expect the "server" to be.
        # This code can be thought of as logic our Dafny "server" uses
        #   to route incoming client requests to the correct request handler code.
        if input.dafny_operation_input is None:
            return self.operation_map[input.operation_name]()
        else:
            return self.operation_map[input.operation_name](input.dafny_operation_input)
