# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	ComAmazonawsKms \

SERVICE_NAMESPACE_ComAmazonawsKms=com.amazonaws.kms
MAX_RESOURCE_COUNT=10000000
AWS_SDK_CMD := --aws-sdk
STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

# Constants for languages that drop extern names (Python, Go)

TYPES_FILE_PATH=Model/ComAmazonawsKmsTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.services.kms.internaldafny.types\" } ComAmazonawsKmsTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module ComAmazonawsKmsTypes"

INDEX_FILE_PATH=src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.services.kms.internaldafny\"} Com.Amazonaws.Kms refines AbstractComAmazonawsKmsService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module Com.Amazonaws.Kms refines AbstractComAmazonawsKmsService {"

# Python

PYTHON_MODULE_NAME=com_amazonaws_kms

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/standard_library/internaldafny/generated/dafny_src-py.dtr
