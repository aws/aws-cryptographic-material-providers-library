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
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStoreAdmin/src/Index.dfy \

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

DIR_STRUCTURE_V2=V2

# Dependencies for each local service
SERVICE_DEPS_TestVectorsAwsCryptographicMaterialProviders := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStoreAdmin \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

SERVICE_DEPS_KeyVectors := \
	AwsCryptographyPrimitives \
	ComAmazonawsKms \
	ComAmazonawsDynamodb \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStoreAdmin \
	AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders \

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

test_encrypt_vectors_java:
	gradle -p runtimes/java run --args="encrypt --manifest-path . --decrypt-manifest-path ."

test_encrypt_vectors_net: FRAMEWORK=net6.0
test_encrypt_vectors_net:
	dotnet restore runtimes/net
	dotnet build runtimes/net
	dotnet run --project runtimes/net --framework $(FRAMEWORK) encrypt --manifest-path runtimes/net --decrypt-manifest-path runtimes/net

test_decrypt_encrypt_vectors_java:
	gradle -p runtimes/java run --args="decrypt --manifest-path ."

test_decrypt_encrypt_vectors_net: FRAMEWORK=net6.0
test_decrypt_encrypt_vectors_net:
	dotnet restore runtimes/net
	dotnet build runtimes/net
	dotnet run --project runtimes/net --framework $(FRAMEWORK) decrypt --manifest-path runtimes/net
