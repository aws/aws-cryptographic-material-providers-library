# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographyPrimitives

MAIN_SERVICE_FOR_RUST := AwsCryptographyPrimitives

RUST_OTHER_FILES := \
        runtimes/rust/src/aes_gcm.rs \
        runtimes/rust/src/aes_kdf_ctr.rs \
        runtimes/rust/src/concurrent_call.rs \
        runtimes/rust/src/dafny_libraries.rs \
        runtimes/rust/src/digest.rs \
        runtimes/rust/src/ecdh.rs \
        runtimes/rust/src/ecdsa.rs \
        runtimes/rust/src/hmac.rs \
        runtimes/rust/src/random.rs \
        runtimes/rust/src/rsa.rs \
        runtimes/rust/src/sets.rs \
        runtimes/rust/src/time.rs \
        runtimes/rust/src/uuid.rs

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
    --translation-record ../StandardLibrary/runtimes/python/src/smithy_dafny_standard_library/internaldafny/generated/dafny_src-py.dtr

GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/primitives"

TRANSLATION_RECORD_GO := \
    StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr