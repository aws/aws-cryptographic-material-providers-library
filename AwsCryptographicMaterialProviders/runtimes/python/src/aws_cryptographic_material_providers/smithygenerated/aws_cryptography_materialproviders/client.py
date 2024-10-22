# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    IAwsCryptographicMaterialProvidersClient,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references
from typing import Callable, TypeVar, cast

from .config import Config, MaterialProvidersConfig
from .dafny_protocol import DafnyRequest, DafnyResponse
from .plugin import set_config_impl
from smithy_python.exceptions import SmithyRetryException
from smithy_python.interfaces.interceptor import Interceptor, InterceptorContext
from smithy_python.interfaces.retries import RetryErrorInfo, RetryErrorType

from .config import Plugin
from .deserialize import (
    _deserialize_create_aws_kms_discovery_keyring,
    _deserialize_create_aws_kms_discovery_multi_keyring,
    _deserialize_create_aws_kms_ecdh_keyring,
    _deserialize_create_aws_kms_hierarchical_keyring,
    _deserialize_create_aws_kms_keyring,
    _deserialize_create_aws_kms_mrk_discovery_keyring,
    _deserialize_create_aws_kms_mrk_discovery_multi_keyring,
    _deserialize_create_aws_kms_mrk_keyring,
    _deserialize_create_aws_kms_mrk_multi_keyring,
    _deserialize_create_aws_kms_multi_keyring,
    _deserialize_create_aws_kms_rsa_keyring,
    _deserialize_create_cryptographic_materials_cache,
    _deserialize_create_default_client_supplier,
    _deserialize_create_default_cryptographic_materials_manager,
    _deserialize_create_multi_keyring,
    _deserialize_create_raw_aes_keyring,
    _deserialize_create_raw_ecdh_keyring,
    _deserialize_create_raw_rsa_keyring,
    _deserialize_create_required_encryption_context_cmm,
    _deserialize_decryption_materials_with_plaintext_data_key,
    _deserialize_encryption_materials_has_plaintext_data_key,
    _deserialize_get_algorithm_suite_info,
    _deserialize_initialize_decryption_materials,
    _deserialize_initialize_encryption_materials,
    _deserialize_valid_algorithm_suite_info,
    _deserialize_valid_decryption_materials_transition,
    _deserialize_valid_encryption_materials_transition,
    _deserialize_validate_commitment_policy_on_decrypt,
    _deserialize_validate_commitment_policy_on_encrypt,
)
from .errors import ServiceError
from .models import (
    AlgorithmSuiteInfo,
    CreateAwsKmsDiscoveryKeyringInput,
    CreateAwsKmsDiscoveryMultiKeyringInput,
    CreateAwsKmsEcdhKeyringInput,
    CreateAwsKmsHierarchicalKeyringInput,
    CreateAwsKmsKeyringInput,
    CreateAwsKmsMrkDiscoveryKeyringInput,
    CreateAwsKmsMrkDiscoveryMultiKeyringInput,
    CreateAwsKmsMrkKeyringInput,
    CreateAwsKmsMrkMultiKeyringInput,
    CreateAwsKmsMultiKeyringInput,
    CreateAwsKmsRsaKeyringInput,
    CreateCryptographicMaterialsCacheInput,
    CreateDefaultClientSupplierInput,
    CreateDefaultCryptographicMaterialsManagerInput,
    CreateMultiKeyringInput,
    CreateRawAesKeyringInput,
    CreateRawEcdhKeyringInput,
    CreateRawRsaKeyringInput,
    CreateRequiredEncryptionContextCMMInput,
    DecryptionMaterials,
    EncryptionMaterials,
    InitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput,
    Unit,
    ValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput,
)
from .serialize import (
    _serialize_create_aws_kms_discovery_keyring,
    _serialize_create_aws_kms_discovery_multi_keyring,
    _serialize_create_aws_kms_ecdh_keyring,
    _serialize_create_aws_kms_hierarchical_keyring,
    _serialize_create_aws_kms_keyring,
    _serialize_create_aws_kms_mrk_discovery_keyring,
    _serialize_create_aws_kms_mrk_discovery_multi_keyring,
    _serialize_create_aws_kms_mrk_keyring,
    _serialize_create_aws_kms_mrk_multi_keyring,
    _serialize_create_aws_kms_multi_keyring,
    _serialize_create_aws_kms_rsa_keyring,
    _serialize_create_cryptographic_materials_cache,
    _serialize_create_default_client_supplier,
    _serialize_create_default_cryptographic_materials_manager,
    _serialize_create_multi_keyring,
    _serialize_create_raw_aes_keyring,
    _serialize_create_raw_ecdh_keyring,
    _serialize_create_raw_rsa_keyring,
    _serialize_create_required_encryption_context_cmm,
    _serialize_decryption_materials_with_plaintext_data_key,
    _serialize_encryption_materials_has_plaintext_data_key,
    _serialize_get_algorithm_suite_info,
    _serialize_initialize_decryption_materials,
    _serialize_initialize_encryption_materials,
    _serialize_valid_algorithm_suite_info,
    _serialize_valid_decryption_materials_transition,
    _serialize_valid_encryption_materials_transition,
    _serialize_validate_commitment_policy_on_decrypt,
    _serialize_validate_commitment_policy_on_encrypt,
)


Input = TypeVar("Input")
Output = TypeVar("Output")


class AwsCryptographicMaterialProviders:
    """Client for AwsCryptographicMaterialProviders.

    :param config: Configuration for the client.
    """

    def __init__(
        self,
        config: MaterialProvidersConfig | None = None,
        dafny_client: IAwsCryptographicMaterialProvidersClient | None = None,
    ):
        if config is None:
            self._config = Config()
        else:
            self._config = config

        client_plugins: list[Plugin] = [
            set_config_impl,
        ]

        for plugin in client_plugins:
            plugin(self._config)

        if dafny_client is not None:
            self._config.dafnyImplInterface.impl = dafny_client

    def create_aws_kms_keyring(
        self, input: CreateAwsKmsKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS Keyring, which wraps and unwraps data keys using
        single symmetric AWS KMS Key.

        :param input: Inputs for for creating a AWS KMS Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_keyring,
            deserialize=_deserialize_create_aws_kms_keyring,
            config=self._config,
            operation_name="CreateAwsKmsKeyring",
        )

    def create_aws_kms_discovery_keyring(
        self, input: CreateAwsKmsDiscoveryKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS Discovery Keyring, which supports unwrapping data
        keys wrapped by a symmetric AWS KMS Key for a single region.

        :param input: Inputs for for creating a AWS KMS Discovery
            Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_discovery_keyring,
            deserialize=_deserialize_create_aws_kms_discovery_keyring,
            config=self._config,
            operation_name="CreateAwsKmsDiscoveryKeyring",
        )

    def create_aws_kms_multi_keyring(
        self, input: CreateAwsKmsMultiKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS Multi-Keyring, which wraps and unwraps data keys
        using one or more symmetric AWS KMS Keys.

        :param input: Inputs for for creating a AWS KMS Multi-Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_multi_keyring,
            deserialize=_deserialize_create_aws_kms_multi_keyring,
            config=self._config,
            operation_name="CreateAwsKmsMultiKeyring",
        )

    def create_aws_kms_discovery_multi_keyring(
        self, input: CreateAwsKmsDiscoveryMultiKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS Discovery Multi-Keyring, which supports
        unwrapping data keys wrapped by a symmetric AWS KMS Key, for multiple
        regions.

        :param input: Inputs for for creating an AWS KMS Discovery
            Multi-Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_discovery_multi_keyring,
            deserialize=_deserialize_create_aws_kms_discovery_multi_keyring,
            config=self._config,
            operation_name="CreateAwsKmsDiscoveryMultiKeyring",
        )

    def create_aws_kms_mrk_keyring(
        self, input: CreateAwsKmsMrkKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS MRK Keyring, which wraps and unwraps data keys
        using single symmetric AWS KMS Key or AWS KMS Multi-Region Key.

        :param input: Inputs for for creating an AWS KMS MRK Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_mrk_keyring,
            deserialize=_deserialize_create_aws_kms_mrk_keyring,
            config=self._config,
            operation_name="CreateAwsKmsMrkKeyring",
        )

    def create_aws_kms_mrk_multi_keyring(
        self, input: CreateAwsKmsMrkMultiKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS MRK Multi-Keyring, which wraps and unwraps data
        keys using one or more symmetric AWS KMS Keys or AWS KMS Multi-Region
        Keys.

        :param input: Inputs for for creating a AWS KMS MRK Multi-
            Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_mrk_multi_keyring,
            deserialize=_deserialize_create_aws_kms_mrk_multi_keyring,
            config=self._config,
            operation_name="CreateAwsKmsMrkMultiKeyring",
        )

    def create_aws_kms_mrk_discovery_keyring(
        self, input: CreateAwsKmsMrkDiscoveryKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS MRK Discovery Keyring, which supports unwrapping
        data keys wrapped by a symmetric AWS KMS Key or AWS KMS Multi-Region
        Key in a particular region.

        :param input: Inputs for for creating a AWS KMS MRK Discovery
            Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_mrk_discovery_keyring,
            deserialize=_deserialize_create_aws_kms_mrk_discovery_keyring,
            config=self._config,
            operation_name="CreateAwsKmsMrkDiscoveryKeyring",
        )

    def create_aws_kms_mrk_discovery_multi_keyring(
        self, input: CreateAwsKmsMrkDiscoveryMultiKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS MRK Discovery Multi-Keyring that supports
        unwrapping data keys wrapped by a symmetric AWS KMS Key or AWS KMS
        Multi-Region Key, for a single region.

        :param input: Inputs for for creating a AWS KMS MRK Discovery
            Multi-Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_mrk_discovery_multi_keyring,
            deserialize=_deserialize_create_aws_kms_mrk_discovery_multi_keyring,
            config=self._config,
            operation_name="CreateAwsKmsMrkDiscoveryMultiKeyring",
        )

    def create_aws_kms_hierarchical_keyring(
        self, input: CreateAwsKmsHierarchicalKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates a Hierarchical Keyring, which supports wrapping and
        unwrapping data keys using Branch Keys persisted in DynamoDB and
        protected by a symmetric AWS KMS Key or AWS KMS Multi-Region Key.

        :param input: Inputs for creating a Hierarchical Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_hierarchical_keyring,
            deserialize=_deserialize_create_aws_kms_hierarchical_keyring,
            config=self._config,
            operation_name="CreateAwsKmsHierarchicalKeyring",
        )

    def create_aws_kms_rsa_keyring(
        self, input: CreateAwsKmsRsaKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS RSA Keyring, which wraps and unwraps data keys
        using a single asymmetric AWS KMS Key for RSA.

        :param input: Inputs for creating a AWS KMS RSA Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_rsa_keyring,
            deserialize=_deserialize_create_aws_kms_rsa_keyring,
            config=self._config,
            operation_name="CreateAwsKmsRsaKeyring",
        )

    def create_aws_kms_ecdh_keyring(
        self, input: CreateAwsKmsEcdhKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates an AWS KMS ECDH Keyring, which wraps and unwraps data keys
        by deriving a shared data key from the established shared secret
        between parties through the ECDH protocol.

        :param input: Inputs for creating an AWS KMS ECDH Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_aws_kms_ecdh_keyring,
            deserialize=_deserialize_create_aws_kms_ecdh_keyring,
            config=self._config,
            operation_name="CreateAwsKmsEcdhKeyring",
        )

    def create_multi_keyring(
        self, input: CreateMultiKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates a Multi-Keyring comprised of one or more other Keyrings.

        :param input: Inputs for creating a Multi-Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_multi_keyring,
            deserialize=_deserialize_create_multi_keyring,
            config=self._config,
            operation_name="CreateMultiKeyring",
        )

    def create_raw_aes_keyring(
        self, input: CreateRawAesKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates a Raw AES Keyring, which wraps and unwraps data keys locally
        using AES_GCM.

        :param input: Inputs for creating a Raw AES Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_raw_aes_keyring,
            deserialize=_deserialize_create_raw_aes_keyring,
            config=self._config,
            operation_name="CreateRawAesKeyring",
        )

    def create_raw_rsa_keyring(
        self, input: CreateRawRsaKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates a Raw RSA Keyring, which wraps and unwraps data keys locally
        using RSA.

        :param input: Inputs for creating a Raw RAW Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_raw_rsa_keyring,
            deserialize=_deserialize_create_raw_rsa_keyring,
            config=self._config,
            operation_name="CreateRawRsaKeyring",
        )

    def create_raw_ecdh_keyring(
        self, input: CreateRawEcdhKeyringInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.Keyring":
        """Creates a Raw ECDH Keyring, which wraps and unwraps data keys by
        deriving a shared data key from the established shared secret between
        parties through the ECDH protocol.

        :param input: Inputs for creating a raw ECDH Keyring.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_raw_ecdh_keyring,
            deserialize=_deserialize_create_raw_ecdh_keyring,
            config=self._config,
            operation_name="CreateRawEcdhKeyring",
        )

    def create_default_cryptographic_materials_manager(
        self, input: CreateDefaultCryptographicMaterialsManagerInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager":
        """Creates a Default Cryptographic Materials Manager.

        :param input: Inputs for creating a Default Cryptographic
            Materials Manager.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_default_cryptographic_materials_manager,
            deserialize=_deserialize_create_default_cryptographic_materials_manager,
            config=self._config,
            operation_name="CreateDefaultCryptographicMaterialsManager",
        )

    def create_required_encryption_context_cmm(
        self, input: CreateRequiredEncryptionContextCMMInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsManager":
        """Creates an Required Encryption Context Cryptographic Materials
        Manager.

        :param input: Inputs for creating an Required Encryption Context
            Cryptographic Materials Manager.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_required_encryption_context_cmm,
            deserialize=_deserialize_create_required_encryption_context_cmm,
            config=self._config,
            operation_name="CreateRequiredEncryptionContextCMM",
        )

    def create_cryptographic_materials_cache(
        self, input: CreateCryptographicMaterialsCacheInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.CryptographicMaterialsCache":
        """Invokes the CreateCryptographicMaterialsCache operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_cryptographic_materials_cache,
            deserialize=_deserialize_create_cryptographic_materials_cache,
            config=self._config,
            operation_name="CreateCryptographicMaterialsCache",
        )

    def create_default_client_supplier(
        self, input: CreateDefaultClientSupplierInput
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.references.ClientSupplier":
        """Invokes the CreateDefaultClientSupplier operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_create_default_client_supplier,
            deserialize=_deserialize_create_default_client_supplier,
            config=self._config,
            operation_name="CreateDefaultClientSupplier",
        )

    def initialize_encryption_materials(
        self, input: InitializeEncryptionMaterialsInput
    ) -> EncryptionMaterials:
        """Invokes the InitializeEncryptionMaterials operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_initialize_encryption_materials,
            deserialize=_deserialize_initialize_encryption_materials,
            config=self._config,
            operation_name="InitializeEncryptionMaterials",
        )

    def initialize_decryption_materials(
        self, input: InitializeDecryptionMaterialsInput
    ) -> DecryptionMaterials:
        """Invokes the InitializeDecryptionMaterials operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_initialize_decryption_materials,
            deserialize=_deserialize_initialize_decryption_materials,
            config=self._config,
            operation_name="InitializeDecryptionMaterials",
        )

    def valid_encryption_materials_transition(
        self, input: ValidEncryptionMaterialsTransitionInput
    ) -> Unit:
        """Invokes the ValidEncryptionMaterialsTransition operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_valid_encryption_materials_transition,
            deserialize=_deserialize_valid_encryption_materials_transition,
            config=self._config,
            operation_name="ValidEncryptionMaterialsTransition",
        )

    def valid_decryption_materials_transition(
        self, input: ValidDecryptionMaterialsTransitionInput
    ) -> Unit:
        """Invokes the ValidDecryptionMaterialsTransition operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_valid_decryption_materials_transition,
            deserialize=_deserialize_valid_decryption_materials_transition,
            config=self._config,
            operation_name="ValidDecryptionMaterialsTransition",
        )

    def encryption_materials_has_plaintext_data_key(
        self, input: EncryptionMaterials
    ) -> Unit:
        """Invokes the EncryptionMaterialsHasPlaintextDataKey operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_encryption_materials_has_plaintext_data_key,
            deserialize=_deserialize_encryption_materials_has_plaintext_data_key,
            config=self._config,
            operation_name="EncryptionMaterialsHasPlaintextDataKey",
        )

    def decryption_materials_with_plaintext_data_key(
        self, input: DecryptionMaterials
    ) -> Unit:
        """Invokes the DecryptionMaterialsWithPlaintextDataKey operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_decryption_materials_with_plaintext_data_key,
            deserialize=_deserialize_decryption_materials_with_plaintext_data_key,
            config=self._config,
            operation_name="DecryptionMaterialsWithPlaintextDataKey",
        )

    def get_algorithm_suite_info(self, input: bytes | bytearray) -> AlgorithmSuiteInfo:
        """Invokes the GetAlgorithmSuiteInfo operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_get_algorithm_suite_info,
            deserialize=_deserialize_get_algorithm_suite_info,
            config=self._config,
            operation_name="GetAlgorithmSuiteInfo",
        )

    def valid_algorithm_suite_info(self, input: AlgorithmSuiteInfo) -> Unit:
        """Invokes the ValidAlgorithmSuiteInfo operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_valid_algorithm_suite_info,
            deserialize=_deserialize_valid_algorithm_suite_info,
            config=self._config,
            operation_name="ValidAlgorithmSuiteInfo",
        )

    def validate_commitment_policy_on_encrypt(
        self, input: ValidateCommitmentPolicyOnEncryptInput
    ) -> Unit:
        """Invokes the ValidateCommitmentPolicyOnEncrypt operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_validate_commitment_policy_on_encrypt,
            deserialize=_deserialize_validate_commitment_policy_on_encrypt,
            config=self._config,
            operation_name="ValidateCommitmentPolicyOnEncrypt",
        )

    def validate_commitment_policy_on_decrypt(
        self, input: ValidateCommitmentPolicyOnDecryptInput
    ) -> Unit:
        """Invokes the ValidateCommitmentPolicyOnDecrypt operation.

        :param input: The operation's input.
        """
        return self._execute_operation(
            input=input,
            plugins=[],
            serialize=_serialize_validate_commitment_policy_on_decrypt,
            deserialize=_deserialize_validate_commitment_policy_on_decrypt,
            config=self._config,
            operation_name="ValidateCommitmentPolicyOnDecrypt",
        )

    def _execute_operation(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], DafnyRequest],
        deserialize: Callable[[DafnyResponse, Config], Output],
        config: Config,
        operation_name: str,
    ) -> Output:
        try:
            return self._handle_execution(
                input, plugins, serialize, deserialize, config, operation_name
            )
        except Exception as e:
            # Make sure every exception that we throw is an instance of ServiceError so
            # customers can reliably catch everything we throw.
            if not isinstance(e, ServiceError):
                raise ServiceError(e) from e
            raise e

    def _handle_execution(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], DafnyRequest],
        deserialize: Callable[[DafnyResponse, Config], Output],
        config: Config,
        operation_name: str,
    ) -> Output:
        context: InterceptorContext[Input, None, None, None] = InterceptorContext(
            request=input,
            response=None,
            transport_request=None,
            transport_response=None,
        )
        _client_interceptors = config.interceptors
        client_interceptors = cast(
            list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
            _client_interceptors,
        )
        interceptors = client_interceptors

        try:
            # Step 1a: Invoke read_before_execution on client-level interceptors
            for interceptor in client_interceptors:
                interceptor.read_before_execution(context)

            # Step 1b: Run operation-level plugins
            for plugin in plugins:
                plugin(config)

            _client_interceptors = config.interceptors
            interceptors = cast(
                list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
                _client_interceptors,
            )

            # Step 1c: Invoke the read_before_execution hooks on newly added
            # interceptors.
            for interceptor in interceptors:
                if interceptor not in client_interceptors:
                    interceptor.read_before_execution(context)

            # Step 2: Invoke the modify_before_serialization hooks
            for interceptor in interceptors:
                context._request = interceptor.modify_before_serialization(context)

            # Step 3: Invoke the read_before_serialization hooks
            for interceptor in interceptors:
                interceptor.read_before_serialization(context)

            # Step 4: Serialize the request
            context_with_transport_request = cast(
                InterceptorContext[Input, None, DafnyRequest, None], context
            )
            context_with_transport_request._transport_request = serialize(
                context_with_transport_request.request, config
            )

            # Step 5: Invoke read_after_serialization
            for interceptor in interceptors:
                interceptor.read_after_serialization(context_with_transport_request)

            # Step 6: Invoke modify_before_retry_loop
            for interceptor in interceptors:
                context_with_transport_request._transport_request = (
                    interceptor.modify_before_retry_loop(context_with_transport_request)
                )

            # Step 7: Acquire the retry token.
            retry_strategy = config.retry_strategy
            retry_token = retry_strategy.acquire_initial_retry_token()

            while True:
                # Make an attempt, creating a copy of the context so we don't pass
                # around old data.
                context_with_response = self._handle_attempt(
                    deserialize,
                    interceptors,
                    context_with_transport_request.copy(),
                    config,
                    operation_name,
                )

                # We perform this type-ignored re-assignment because `context` needs
                # to point at the latest context so it can be generically handled
                # later on. This is only an issue here because we've created a copy,
                # so we're no longer simply pointing at the same object in memory
                # with different names and type hints. It is possible to address this
                # without having to fall back to the type ignore, but it would impose
                # unnecessary runtime costs.
                context = context_with_response  # type: ignore

                if isinstance(context_with_response.response, Exception):
                    # Step 7u: Reacquire retry token if the attempt failed
                    try:
                        retry_token = retry_strategy.refresh_retry_token_for_retry(
                            token_to_renew=retry_token,
                            error_info=RetryErrorInfo(
                                # TODO: Determine the error type.
                                error_type=RetryErrorType.CLIENT_ERROR,
                            ),
                        )
                    except SmithyRetryException:
                        raise context_with_response.response
                else:
                    # Step 8: Invoke record_success
                    retry_strategy.record_success(token=retry_token)
                    break
        except Exception as e:
            context._response = e

        # At this point, the context's request will have been definitively set, and
        # The response will be set either with the modeled output or an exception. The
        # transport_request and transport_response may be set or None.
        execution_context = cast(
            InterceptorContext[
                Input, Output, DafnyRequest | None, DafnyResponse | None
            ],
            context,
        )
        return self._finalize_execution(interceptors, execution_context)

    def _handle_attempt(
        self,
        deserialize: Callable[[DafnyResponse, Config], Output],
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, None, DafnyRequest, None],
        config: Config,
        operation_name: str,
    ) -> InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None]:
        try:
            # Step 7a: Invoke read_before_attempt
            for interceptor in interceptors:
                interceptor.read_before_attempt(context)

            # Step 7m: Involve client Dafny impl
            if config.dafnyImplInterface.impl is None:
                raise Exception("No impl found on the operation config.")

            context_with_response = cast(
                InterceptorContext[Input, None, DafnyRequest, DafnyResponse], context
            )

            context_with_response._transport_response = (
                config.dafnyImplInterface.handle_request(
                    input=context_with_response.transport_request
                )
            )

            # Step 7n: Invoke read_after_transmit
            for interceptor in interceptors:
                interceptor.read_after_transmit(context_with_response)

            # Step 7o: Invoke modify_before_deserialization
            for interceptor in interceptors:
                context_with_response._transport_response = (
                    interceptor.modify_before_deserialization(context_with_response)
                )

            # Step 7p: Invoke read_before_deserialization
            for interceptor in interceptors:
                interceptor.read_before_deserialization(context_with_response)

            # Step 7q: deserialize
            context_with_output = cast(
                InterceptorContext[Input, Output, DafnyRequest, DafnyResponse],
                context_with_response,
            )
            context_with_output._response = deserialize(
                context_with_output._transport_response, config
            )

            # Step 7r: Invoke read_after_deserialization
            for interceptor in interceptors:
                interceptor.read_after_deserialization(context_with_output)
        except Exception as e:
            context._response = e

        # At this point, the context's request and transport_request have definitively been set,
        # the response is either set or an exception, and the transport_resposne is either set or
        # None. This will also be true after _finalize_attempt because there is no opportunity
        # there to set the transport_response.
        attempt_context = cast(
            InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None],
            context,
        )
        return self._finalize_attempt(interceptors, attempt_context)

    def _finalize_attempt(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None],
    ) -> InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None]:
        # Step 7s: Invoke modify_before_attempt_completion
        try:
            for interceptor in interceptors:
                context._response = interceptor.modify_before_attempt_completion(
                    context
                )
        except Exception as e:
            context._response = e

        # Step 7t: Invoke read_after_attempt
        for interceptor in interceptors:
            try:
                interceptor.read_after_attempt(context)
            except Exception as e:
                context._response = e

        return context

    def _finalize_execution(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[
            Input, Output, DafnyRequest | None, DafnyResponse | None
        ],
    ) -> Output:
        try:
            # Step 9: Invoke modify_before_completion
            for interceptor in interceptors:
                context._response = interceptor.modify_before_completion(context)

        except Exception as e:
            context._response = e

        # Step 11: Invoke read_after_execution
        for interceptor in interceptors:
            try:
                interceptor.read_after_execution(context)
            except Exception as e:
                context._response = e

        # Step 12: Return / throw
        if isinstance(context.response, Exception):
            raise context.response

        # We may want to add some aspects of this context to the output types so we can
        # return it to the end-users.
        return context.response
