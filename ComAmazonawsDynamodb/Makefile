# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	ComAmazonawsDynamodb \

MAIN_SERVICE_FOR_RUST := ComAmazonawsDynamodb

RUST_OTHER_FILES := \
        runtimes/rust/src/concurrent_call.rs \
        runtimes/rust/src/dafny_libraries.rs \
        runtimes/rust/src/ddb.rs \
        runtimes/rust/src/oslang.rs \
        runtimes/rust/src/sets.rs \
        runtimes/rust/src/time.rs \
        runtimes/rust/src/uuid.rs

SERVICE_NAMESPACE_ComAmazonawsDynamodb=com.amazonaws.dynamodb
MAX_RESOURCE_COUNT=10000000
AWS_SDK_CMD := --aws-sdk
STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/dynamodb"

GO_DEPENDENCY_MODULE_NAMES := \
	--dependency-library-name=sdk.com.amazonaws.dynamodb=github.com/aws/aws-sdk-go-v2/service/dynamodb \

TRANSLATION_RECORD_GO := \
    StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr

# Constants for languages that drop extern names (Python, Go)

TYPES_FILE_PATH=Model/ComAmazonawsDynamodbTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.services.dynamodb.internaldafny.types\" } ComAmazonawsDynamodbTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module ComAmazonawsDynamodbTypes"

INDEX_FILE_PATH=src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.services.dynamodb.internaldafny\"} Com.Amazonaws.Dynamodb refines AbstractComAmazonawsDynamodbService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module Com.Amazonaws.Dynamodb refines AbstractComAmazonawsDynamodbService {"

# Python

PYTHON_MODULE_NAME=aws_cryptography_internal_dynamodb

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/smithy_dafny_standard_library/internaldafny/generated/dafny_src-py.dtr
