# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PYTHON_MODULE_NAME=aws_cryptography_primitives

PROJECT_SERVICES := \
	AwsCryptographyPrimitives \

# OUTPUT_LOCAL_SERVICE_AwsCryptographyPrimitives := --local-service-test


SERVICE_NAMESPACE_AwsCryptographyPrimitives=aws.cryptography.primitives
MAX_RESOURCE_COUNT=10000000

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

format_net:
	pushd runtimes/net && dotnet format && popd
