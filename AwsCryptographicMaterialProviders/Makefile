# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographicMaterialProviders \
	AwsCryptographyKeyStore \

MAIN_SERVICE_FOR_RUST := AwsCryptographicMaterialProviders

RUST_OTHER_FILES := \
	runtimes/rust/src/aes_gcm.rs \
	runtimes/rust/src/aes_kdf_ctr.rs \
	runtimes/rust/src/digest.rs \
	runtimes/rust/src/ecdh.rs \
	runtimes/rust/src/ecdsa.rs \
	runtimes/rust/src/hmac.rs \
	runtimes/rust/src/random.rs \
	runtimes/rust/src/rsa.rs \
	runtimes/rust/src/concurrent_call.rs \
	runtimes/rust/src/dafny_libraries.rs \
	runtimes/rust/src/sets.rs \
	runtimes/rust/src/time.rs \
	runtimes/rust/src/uuid.rs

SERVICE_NAMESPACE_AwsCryptographicMaterialProviders=aws.cryptography.materialProviders
SERVICE_NAMESPACE_AwsCryptographyKeyStore=aws.cryptography.keyStore

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

