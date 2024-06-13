# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PYTHON_MODULE_NAME=com_amazonaws_dynamodb

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/standard_library/internaldafny/generated/dafny_src-py.dtr

PROJECT_SERVICES := \
	ComAmazonawsDynamodb \

SERVICE_NAMESPACE_ComAmazonawsDynamodb=com.amazonaws.dynamodb
MAX_RESOURCE_COUNT=10000000
AWS_SDK_CMD := --aws-sdk
STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model
