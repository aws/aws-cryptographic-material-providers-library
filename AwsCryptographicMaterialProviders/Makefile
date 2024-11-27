# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2
ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographyKeyStore \
	AwsCryptographicMaterialProviders \

SERVICE_NAMESPACE_AwsCryptographicMaterialProviders=aws.cryptography.materialProviders
SERVICE_NAMESPACE_AwsCryptographyKeyStore=aws.cryptography.keyStore

MAIN_SERVICE_FOR_RUST := AwsCryptographicMaterialProviders

RUST_OTHER_FILES := \
	runtimes/rust/src/aes_gcm.rs \
	runtimes/rust/src/aes_kdf_ctr.rs \
	runtimes/rust/src/ddb.rs \
	runtimes/rust/src/concurrent_call.rs \
	runtimes/rust/src/dafny_libraries.rs \
	runtimes/rust/src/digest.rs \
	runtimes/rust/src/ecdh.rs \
	runtimes/rust/src/ecdsa.rs \
	runtimes/rust/src/hmac.rs \
	runtimes/rust/src/kms.rs \
	runtimes/rust/src/local_cmc.rs \
	runtimes/rust/src/random.rs \
	runtimes/rust/src/rsa.rs \
	runtimes/rust/src/sets.rs \
	runtimes/rust/src/software_externs.rs \
	runtimes/rust/src/storm_tracker.rs \
	runtimes/rust/src/time.rs \
	runtimes/rust/src/uuid.rs

MAX_RESOURCE_COUNT=90000000
# Order is important
# In java they MUST be built
# in the order they depend on each other
PROJECT_DEPENDENCIES := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb

PROJECT_INDEX := \
	AwsCryptographyPrimitives/src/Index.dfy \
	ComAmazonawsKms/src/Index.dfy \
	ComAmazonawsDynamodb/src/Index.dfy

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

DIR_STRUCTURE_V2=V2

# Dependencies for each local service
SERVICE_DEPS_AwsCryptographicMaterialProviders := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \

SERVICE_DEPS_AwsCryptographyKeyStore := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/mpl"

GO_DEPENDENCY_MODULE_NAMES := \
	--dependency-library-name=com.amazonaws.dynamodb=github.com/aws/aws-cryptographic-material-providers-library/dynamodb \
	--dependency-library-name=com.amazonaws.kms=github.com/aws/aws-cryptographic-material-providers-library/kms \
	--dependency-library-name=aws.cryptography.keyStore=github.com/aws/aws-cryptographic-material-providers-library/mpl \
	--dependency-library-name=aws.cryptography.primitives=github.com/aws/aws-cryptographic-material-providers-library/primitives \
	--dependency-library-name=sdk.com.amazonaws.dynamodb=github.com/aws/aws-sdk-go-v2/service/dynamodb \
	--dependency-library-name=sdk.com.amazonaws.kms=github.com/aws/aws-sdk-go-v2/service/kms

TRANSLATION_RECORD_GO := \
    StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    ComAmazonawsKms/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    ComAmazonawsDynamodb/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    AwsCryptographyPrimitives/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr

# Constants for languages that drop extern names (Python, Go)

MPL_CORE_TYPES_FILE_PATH=dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy
MPL_CORE_TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.materialproviders.internaldafny.types\" } AwsCryptographyMaterialProvidersTypes"
MPL_CORE_TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyMaterialProvidersTypes"

MPL_CORE_INDEX_FILE_PATH=dafny/AwsCryptographicMaterialProviders/src/Index.dfy
MPL_CORE_INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.materialproviders.internaldafny\" } MaterialProviders refines AbstractAwsCryptographyMaterialProvidersService"
MPL_CORE_INDEX_FILE_WITHOUT_EXTERN_STRING="module MaterialProviders refines AbstractAwsCryptographyMaterialProvidersService"

KEYSTORE_TYPES_FILE_PATH=dafny/AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy
KEYSTORE_TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.keystore.internaldafny.types\" } AwsCryptographyKeyStoreTypes"
KEYSTORE_TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyKeyStoreTypes"

KEYSTORE_INDEX_FILE_PATH=dafny/AwsCryptographyKeyStore/src/Index.dfy
KEYSTORE_INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.keystore.internaldafny\"} KeyStore refines AbstractAwsCryptographyKeyStoreService"
KEYSTORE_INDEX_FILE_WITHOUT_EXTERN_STRING="module KeyStore refines AbstractAwsCryptographyKeyStoreService"

SYNCHRONIZED_LOCAL_CMC_FILE_PATH=dafny/AwsCryptographicMaterialProviders/src/CMCs/SynchronizedLocalCMC.dfy
SYNCHRONIZED_LOCAL_CMC_WITH_EXTERN_STRING="module {:options \"\/functionSyntax:4\" } {:extern \"software.amazon.cryptography.internaldafny.SynchronizedLocalCMC\" } SynchronizedLocalCMC {"
SYNCHRONIZED_LOCAL_CMC_WITHOUT_EXTERN_STRING="module {:options \"\/functionSyntax:4\" } SynchronizedLocalCMC {"

STORM_TRACKING_CMC_FILE_PATH=dafny/AwsCryptographicMaterialProviders/src/CMCs/StormTrackingCMC.dfy
STORM_TRACKING_CMC_WITH_EXTERN_STRING="module {:options \"\/functionSyntax:4\" } {:extern \"software.amazon.cryptography.internaldafny.StormTrackingCMC\" } StormTrackingCMC {"
STORM_TRACKING_CMC_WITHOUT_EXTERN_STRING="module {:options \"\/functionSyntax:4\" } StormTrackingCMC {"

_sed_types_file_remove_extern:
	$(MAKE) _sed_file SED_FILE_PATH=$(MPL_CORE_TYPES_FILE_PATH) SED_BEFORE_STRING=$(MPL_CORE_TYPES_FILE_WITH_EXTERN_STRING) SED_AFTER_STRING=$(MPL_CORE_TYPES_FILE_WITHOUT_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(KEYSTORE_TYPES_FILE_PATH) SED_BEFORE_STRING=$(KEYSTORE_TYPES_FILE_WITH_EXTERN_STRING) SED_AFTER_STRING=$(KEYSTORE_TYPES_FILE_WITHOUT_EXTERN_STRING)

_sed_index_file_remove_extern:
	$(MAKE) _sed_file SED_FILE_PATH=$(MPL_CORE_INDEX_FILE_PATH) SED_BEFORE_STRING=$(MPL_CORE_INDEX_FILE_WITH_EXTERN_STRING) SED_AFTER_STRING=$(MPL_CORE_INDEX_FILE_WITHOUT_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(KEYSTORE_INDEX_FILE_PATH) SED_BEFORE_STRING=$(KEYSTORE_INDEX_FILE_WITH_EXTERN_STRING) SED_AFTER_STRING=$(KEYSTORE_INDEX_FILE_WITHOUT_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(SYNCHRONIZED_LOCAL_CMC_FILE_PATH) SED_BEFORE_STRING=$(SYNCHRONIZED_LOCAL_CMC_WITH_EXTERN_STRING) SED_AFTER_STRING=$(SYNCHRONIZED_LOCAL_CMC_WITHOUT_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(STORM_TRACKING_CMC_FILE_PATH) SED_BEFORE_STRING=$(STORM_TRACKING_CMC_WITH_EXTERN_STRING) SED_AFTER_STRING=$(STORM_TRACKING_CMC_WITHOUT_EXTERN_STRING)

_sed_types_file_add_extern:
	$(MAKE) _sed_file SED_FILE_PATH=$(MPL_CORE_TYPES_FILE_PATH) SED_BEFORE_STRING=$(MPL_CORE_TYPES_FILE_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(MPL_CORE_TYPES_FILE_WITH_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(KEYSTORE_TYPES_FILE_PATH) SED_BEFORE_STRING=$(KEYSTORE_TYPES_FILE_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(KEYSTORE_TYPES_FILE_WITH_EXTERN_STRING)

_sed_index_file_add_extern:
	$(MAKE) _sed_file SED_FILE_PATH=$(MPL_CORE_INDEX_FILE_PATH) SED_BEFORE_STRING=$(MPL_CORE_INDEX_FILE_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(MPL_CORE_INDEX_FILE_WITH_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(KEYSTORE_INDEX_FILE_PATH) SED_BEFORE_STRING=$(KEYSTORE_INDEX_FILE_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(KEYSTORE_INDEX_FILE_WITH_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(SYNCHRONIZED_LOCAL_CMC_FILE_PATH) SED_BEFORE_STRING=$(SYNCHRONIZED_LOCAL_CMC_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(SYNCHRONIZED_LOCAL_CMC_WITH_EXTERN_STRING)
	$(MAKE) _sed_file SED_FILE_PATH=$(STORM_TRACKING_CMC_FILE_PATH) SED_BEFORE_STRING=$(STORM_TRACKING_CMC_WITHOUT_EXTERN_STRING) SED_AFTER_STRING=$(STORM_TRACKING_CMC_WITH_EXTERN_STRING)

# Python

PYTHON_MODULE_NAME=aws_cryptographic_material_providers

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/smithy_dafny_standard_library/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsKms/runtimes/python/src/aws_cryptography_internal_kms/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsDynamodb/runtimes/python/src/aws_cryptography_internal_dynamodb/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../AwsCryptographyPrimitives/runtimes/python/src/aws_cryptography_primitives/internaldafny/generated/dafny_src-py.dtr

PYTHON_DEPENDENCY_MODULE_NAMES := \
	--dependency-library-name=aws.cryptography.primitives=aws_cryptography_primitives \
	--dependency-library-name=com.amazonaws.kms=aws_cryptography_internal_kms \
	--dependency-library-name=com.amazonaws.dynamodb=aws_cryptography_internal_dynamodb \
	--dependency-library-name=aws.cryptography.materialProviders=aws_cryptographic_material_providers \
	--dependency-library-name=aws.cryptography.keyStore=aws_cryptographic_material_providers \
