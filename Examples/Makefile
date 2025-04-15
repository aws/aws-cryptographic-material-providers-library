# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

include ../SharedMakefileV2.mk

default:
	@echo make targets are : test_java, test_java_concurrent, clean

test_java:
	$(GRADLEW) -p java test

test_java_concurrent:
	$(GRADLEW) -p java testConcurrent

clean:
	$(GRADLEW) -p java clean
