# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographyPrimitives

SERVICE_NAMESPACE_AwsCryptographyPrimitives=aws.cryptography.primitives
MAX_RESOURCE_COUNT=10000000

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

# Constants for languages that drop extern names (Python, Go)

TYPES_FILE_PATH=Model/AwsCryptographyPrimitivesTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.primitives.internaldafny.types\" } AwsCryptographyPrimitivesTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyPrimitivesTypes"

INDEX_FILE_PATH=src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.primitives.internaldafny\" } AtomicPrimitives refines AbstractAwsCryptographyPrimitivesService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module AtomicPrimitives refines AbstractAwsCryptographyPrimitivesService {"

# Python

PYTHON_MODULE_NAME=aws_cryptography_primitives

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/standard_library/internaldafny/generated/dafny_src-py.dtr
