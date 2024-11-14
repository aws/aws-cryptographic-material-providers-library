# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

ENABLE_EXTERN_PROCESSING=1

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	KeyVectors \
	TestVectorsAwsCryptographicMaterialProviders \

SMITHY_MODEL_ROOT := $(PROJECT_ROOT)/AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders/Model
OUTPUT_LOCAL_SERVICE_TestVectorsAwsCryptographicMaterialProviders := --local-service-test

SERVICE_NAMESPACE_TestVectorsAwsCryptographicMaterialProviders=aws.cryptography.materialProviders
SERVICE_NAMESPACE_KeyVectors=aws.cryptography.materialProvidersTestVectorKeys

MAX_RESOURCE_COUNT=10000000
# Order is important
# In java they MUST be built
# in the order they depend on each other
PROJECT_DEPENDENCIES := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders

# Since we are packaging projects differently, we cannot make assumptions
# about where the files are located. 
# This is here to get unblocked but should be removed once we have migrated packages
# to the new packaging format.
PROJECT_INDEX := \
	AwsCryptographyPrimitives/src/Index.dfy \
	ComAmazonawsKms/src/Index.dfy \
	ComAmazonawsDynamodb/src/Index.dfy \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders/src/Index.dfy \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore/src/Index.dfy \

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

DIR_STRUCTURE_V2=V2

# Dependencies for each local service
SERVICE_DEPS_TestVectorsAwsCryptographicMaterialProviders := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

SERVICE_DEPS_KeyVectors := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

# Constants for languages that drop extern names (Python, Go)

TYPES_FILE_PATH=dafny/KeyVectors/Model/AwsCryptographyMaterialProvidersTestVectorKeysTypes.dfy
TYPES_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types\" } AwsCryptographyMaterialProvidersTestVectorKeysTypes"
TYPES_FILE_WITHOUT_EXTERN_STRING="module AwsCryptographyMaterialProvidersTestVectorKeysTypes"

INDEX_FILE_PATH=dafny/KeyVectors/src/Index.dfy
INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny\"} KeyVectors refines AbstractAwsCryptographyMaterialProvidersTestVectorKeysService {"
INDEX_FILE_WITHOUT_EXTERN_STRING="module KeyVectors refines AbstractAwsCryptographyMaterialProvidersTestVectorKeysService {"

WRAPPED_INDEX_FILE_PATH=dafny/TestVectorsAwsCryptographicMaterialProviders/src/LibraryIndex.dfy
WRAPPED_INDEX_FILE_WITH_EXTERN_STRING="module {:extern \"software.amazon.cryptography.materialproviders.internaldafny.wrapped\" } WrappedMaterialProviders refines WrappedAbstractAwsCryptographyMaterialProvidersService"
WRAPPED_INDEX_FILE_WITHOUT_EXTERN_STRING="module WrappedMaterialProviders refines WrappedAbstractAwsCryptographyMaterialProvidersService"

# Go
GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/testvectors"

GO_DEPENDENCY_MODULE_NAMES := \
	--dependency-library-name=aws.cryptography.primitives=github.com/aws/aws-cryptographic-material-providers-library/primitives \
	--dependency-library-name=com.amazonaws.kms=github.com/aws/aws-cryptographic-material-providers-library/kms \
	--dependency-library-name=com.amazonaws.dynamodb=github.com/aws/aws-cryptographic-material-providers-library/dynamodb \
	--dependency-library-name=aws.cryptography.materialProviders=github.com/aws/aws-cryptographic-material-providers-library/mpl \
	--dependency-library-name=aws.cryptography.keyStore=github.com/aws/aws-cryptographic-material-providers-library/mpl \
	--dependency-library-name=sdk.com.amazonaws.dynamodb=github.com/aws/aws-sdk-go-v2/service/dynamodb \
	--dependency-library-name=sdk.com.amazonaws.kms=github.com/aws/aws-sdk-go-v2/service/kms

TRANSLATION_RECORD_GO := \
    StandardLibrary/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    ComAmazonawsKms/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    ComAmazonawsDynamodb/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
    AwsCryptographyPrimitives/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr \
	AwsCryptographicMaterialProviders/runtimes/go/ImplementationFromDafny-go/ImplementationFromDafny-go.dtr
	
# Python

# smithy.api namespace is a workaround for having a wrapped localService shim in a different Python package,
# as the aws_cryptography_materialproviders namespace is spread across this package (shim only)
# and the aws_cryptographic_material_providers package (all other files).
# This prevents Polymorph from generating invalid references to files in this package, which is incomplete.
# This is a workaround, but is OK because
# 1) this is only for wrapped localService shims, which are only for testing
# 2) this is a test package
PYTHON_DEPENDENCY_MODULE_NAMES := \
	--dependency-library-name=aws.cryptography.primitives=aws_cryptography_primitives \
	--dependency-library-name=com.amazonaws.kms=aws_cryptography_internal_kms \
	--dependency-library-name=com.amazonaws.dynamodb=aws_cryptography_internal_dynamodb \
	--dependency-library-name=aws.cryptography.materialProviders=aws_cryptographic_material_providers \
	--dependency-library-name=aws.cryptography.keyStore=aws_cryptographic_material_providers \
	--dependency-library-name=smithy.api=aws_cryptographic_material_providers

PYTHON_MODULE_NAME=aws_cryptography_materialproviders_test_vectors

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/smithy_dafny_standard_library/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsKms/runtimes/python/src/aws_cryptography_internal_kms/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsDynamodb/runtimes/python/src/aws_cryptography_internal_dynamodb/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../AwsCryptographyPrimitives/runtimes/python/src/aws_cryptography_primitives/internaldafny/generated/dafny_src-py.dtr \
	--translation-record ../AwsCryptographicMaterialProviders/runtimes/python/src/aws_cryptographic_material_providers/internaldafny/generated/dafny_src-py.dtr

# Python

# Override default test_python to run tox environment for Dafny tests
test_python:
	rm -rf runtimes/python/.tox
	python3 -m tox -c runtimes/python -e dafnytests --verbose

# Commands to generate and test test vectors
test_generate_vectors_java:
	gradle -p runtimes/java run --args="encrypt-manifest --encrypt-manifest-output ."
	gradle -p runtimes/java copyKeysJSONCurr

test_generate_vectors_net: FRAMEWORK=net6.0
test_generate_vectors_net:
	dotnet restore runtimes/net
	dotnet build runtimes/net
	dotnet run --project runtimes/net --framework $(FRAMEWORK) encrypt-manifest --encrypt-manifest-output runtimes/net
	cp dafny/TestVectorsAwsCryptographicMaterialProviders/test/keys.json runtimes/net

test_generate_vectors_python:
	rm -rf runtimes/python/.tox
	python3 -m tox -c runtimes/python --verbose -e cli -- encrypt-manifest --encrypt-manifest-output runtimes/python
	cp dafny/TestVectorsAwsCryptographicMaterialProviders/test/keys.json runtimes/python

test_encrypt_vectors_java:
	gradle -p runtimes/java run --args="encrypt --manifest-path . --decrypt-manifest-path ."

test_encrypt_vectors_net: FRAMEWORK=net6.0
test_encrypt_vectors_net:
	dotnet restore runtimes/net
	dotnet build runtimes/net
	dotnet run --project runtimes/net --framework $(FRAMEWORK) encrypt --manifest-path runtimes/net --decrypt-manifest-path runtimes/net

test_encrypt_vectors_python:
	rm -rf runtimes/python/.tox
	python3 -m tox -c runtimes/python --verbose -e cli -- encrypt --manifest-path runtimes/python --decrypt-manifest-path runtimes/python

test_decrypt_encrypt_vectors_java:
	gradle -p runtimes/java run --args="decrypt --manifest-path ."

test_decrypt_encrypt_vectors_net: FRAMEWORK=net6.0
test_decrypt_encrypt_vectors_net:
	dotnet restore runtimes/net
	dotnet build runtimes/net
	dotnet run --project runtimes/net --framework $(FRAMEWORK) decrypt --manifest-path runtimes/net

test_decrypt_encrypt_vectors_python:
	rm -rf runtimes/python/.tox
	python3 -m tox -c runtimes/python --verbose -e cli -- decrypt --manifest-path runtimes/python
