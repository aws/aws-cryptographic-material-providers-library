# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2
ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	Metrics \

# MAIN_SERVICE_FOR_RUST := Metrics

# RUST_OTHER_FILES := \
#         runtimes/rust/src/concurrent_call.rs \
#         runtimes/rust/src/dafny_libraries.rs \
#         runtimes/rust/src/kms.rs \
#         runtimes/rust/src/oslang.rs \
#         runtimes/rust/src/sets.rs \
#         runtimes/rust/src/time.rs \
#         runtimes/rust/src/uuid.rs

SERVICE_NAMESPACE_Metrics=aws.cryptography.metrics
MAX_RESOURCE_COUNT=10000000

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

DIR_STRUCTURE_V2=V2

# GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/releases/go/kms"

# GO_DEPENDENCY_MODULE_NAMES := \
# 	--dependency-library-name=sdk.com.amazonaws.kms=github.com/aws/aws-sdk-go-v2/service/kms \

# TRANSLATION_RECORD_GO := \
#     StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr

# # Constants for languages that drop extern names (Python, Go)

TYPES_FILE_PATH=dafny/Metrics/Model/AwsCryptographyMetricsTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.metrics.internaldafny.types\" } AwsCryptographyMetricsTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyMetricsTypes"

INDEX_FILE_PATH=dafny/Metrics/src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.metrics.internaldafny\" } Metrics refines AbstractAwsCryptographyMetricsService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module Metrics refines AbstractAwsCryptographyMetricsService {"

# # Python

# PYTHON_MODULE_NAME=aws_cryptography_internal_kms

# TRANSLATION_RECORD_PYTHON := \
#     --translation-record ../StandardLibrary/runtimes/python/src/smithy_dafny_standard_library/internaldafny/generated/dafny_src-py.dtr
