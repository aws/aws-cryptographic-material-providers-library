# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PYTHON_MODULE_NAME=aws_cryptographic_materialproviders
# PYTHON_DEPENDENCY_MODULE_NAMES=aws_cryptographic_materialproviders

PROJECT_SERVICES := \
	AwsCryptographicMaterialProviders \
	AwsCryptographyKeyStore \

SERVICE_NAMESPACE_AwsCryptographicMaterialProviders=aws.cryptography.materialProviders
SERVICE_NAMESPACE_AwsCryptographyKeyStore=aws.cryptography.keyStore
SNAKECASE_DIR_AwsCryptographicMaterialProviders:=aws_cryptography_materialproviders
SNAKECASE_DIR_AwsCryptographyKeyStore:=aws_cryptography_keystore
# OUTPUT_LOCAL_SERVICE_AwsCryptographicMaterialProviders := --local-service-test
# OUTPUT_LOCAL_SERVICE_AwsCryptographyKeyStore := --local-service-test

MAX_RESOURCE_COUNT=90000000
# Order is important
# In java they MUST be built
# in the order they depend on each other
PROJECT_DEPENDENCIES := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb

PROJECT_INDEX := \
	AwsCryptographyPrimitives/src/Index.dfy \
	ComAmazonawsKms/src/Index.dfy \
	ComAmazonawsDynamodb/src/Index.dfy

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

DIR_STRUCTURE_V2=V2

# Dependencies for each local service
SERVICE_DEPS_AwsCryptographicMaterialProviders := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \

SERVICE_DEPS_AwsCryptographyKeyStore := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

PYTHON_DEPENDENCY_MODULE_NAMES := \
	--dependency-module-name=aws.cryptography.primitives=aws_cryptography_primitives \
	--dependency-module-name=com.amazonaws.kms=com_amazonaws_kms \
	--dependency-module-name=com.amazonaws.dynamodb=com_amazonaws_dynamodb \
	--dependency-module-name=aws.cryptography.materialProviders=aws_cryptographic_materialproviders \
	--dependency-module-name=aws.cryptography.keyStore=aws_cryptographic_materialproviders \

format_net:
	pushd runtimes/net && dotnet format && popd
