# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

PROJECT_SERVICES := \
	AwsCryptographyPrimitives \

SERVICE_NAMESPACE_AwsCryptographyPrimitives=aws.cryptography.primitives
MAX_RESOURCE_COUNT=10000000

STD_LIBRARY=StandardLibrary
SMITHY_DEPS=model

# Java

JAVA_PACKAGE_NAME = software.amazon.cryptography.primitives

TRANSLATION_RECORD_JAVA:= \
    --translation-record ../StandardLibrary/runtimes/java/src/main/dafny-generated/ImplementationFromDafny-java.dtr

# NET

NET_NAMESPACE_NAME = software.amazon.cryptography.primitives

TRANSLATION_RECORD_NET= \
    --translation-record ../StandardLibrary/runtimes/net/ImplementationFromDafny-cs.dtr
