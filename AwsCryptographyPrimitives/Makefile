# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2
ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographyPrimitives \

SERVICE_NAMESPACE_AwsCryptographyPrimitives=aws.cryptography.primitives
MAX_RESOURCE_COUNT=10000000

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/primitives"

TRANSLATION_RECORD_GO := \
    StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr

TYPES_FILE_PATH=Model/AwsCryptographyPrimitivesTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.primitives.internaldafny.types\" } AwsCryptographyPrimitivesTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyPrimitivesTypes"

INDEX_FILE_PATH=src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.primitives.internaldafny\" } Aws.Cryptography.Primitives refines AbstractAwsCryptographyPrimitivesService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module Aws.Cryptography.Primitives refines AbstractAwsCryptographyPrimitivesService {"

