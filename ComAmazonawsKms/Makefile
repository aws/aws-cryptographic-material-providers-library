# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	ComAmazonawsKms \

SERVICE_NAMESPACE_ComAmazonawsKms=com.amazonaws.kms
MAX_RESOURCE_COUNT=10000000
AWS_SDK_CMD := --aws-sdk
STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

# Python

PYTHON_MODULE_NAME=com_amazonaws_kms

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/standard_library/internaldafny/generated/dafny_src-py.dtr
