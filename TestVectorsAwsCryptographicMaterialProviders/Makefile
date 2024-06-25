# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

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

# Python

# smithy.api namespace is a workaround for having a wrapped localService shim in a different Python package,
# as the aws_cryptography_materialproviders namespace is spread across this package (shim only)
# and the aws_cryptographic_material_providers package (all other files).
# This prevents Polymorph from generating invalid references to files in this package, which is incomplete.
# This is a workaround, but is OK because
# 1) this is only for wrapped localService shims, which are only for testing
# 2) this is a test package
PYTHON_DEPENDENCY_MODULE_NAMES := \
	--dependency-module-name=aws.cryptography.primitives=aws_cryptography_primitives \
	--dependency-module-name=com.amazonaws.kms=com_amazonaws_kms \
	--dependency-module-name=com.amazonaws.dynamodb=com_amazonaws_dynamodb \
	--dependency-module-name=aws.cryptography.materialProviders=aws_cryptographic_materialproviders \
	--dependency-module-name=aws.cryptography.keyStore=aws_cryptographic_materialproviders \
	--dependency-module-name=smithy.api=aws_cryptographic_materialproviders

PYTHON_MODULE_NAME=aws_cryptography_materialproviderstestvectorkeys

TRANSLATION_RECORD_PYTHON := \
    --translation-record ../StandardLibrary/runtimes/python/src/standard_library/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsKms/runtimes/python/src/com_amazonaws_kms/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../ComAmazonawsDynamodb/runtimes/python/src/com_amazonaws_dynamodb/internaldafny/generated/dafny_src-py.dtr \
    --translation-record ../AwsCryptographyPrimitives/runtimes/python/src/aws_cryptography_primitives/internaldafny/generated/dafny_src-py.dtr \
	--translation-record ../AwsCryptographicMaterialProviders/runtimes/python/src/aws_cryptographic_materialproviders/internaldafny/generated/dafny_src-py.dtr
