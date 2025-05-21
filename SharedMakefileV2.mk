# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# This evaluates to the local path _of this file_.
# This means that these are the project roots
# that are shared by all libraries in this repo.
PROJECT_ROOT := $(abspath $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

SMITHY_DAFNY_ROOT := $(PROJECT_ROOT)/smithy-dafny
GRADLEW := ./runtimes/java/gradlew

include $(SMITHY_DAFNY_ROOT)/SmithyDafnyMakefile.mk

# TODO-HV-2-BLOCKER :: remove `--allow-warnings` from `verify*` once KMS Keyring proof is fixed
verify:DAFNY_OPTIONS=--allow-deprecation --allow-external-contracts --allow-warnings
verify_single:DAFNY_OPTIONS=--allow-deprecation --allow-external-contracts --allow-warnings
verify_service:DAFNY_OPTIONS=--allow-deprecation --allow-external-contracts --allow-warnings

transpile_implementation_net: DAFNY_OPTIONS=--allow-warnings --compile-suffix --legacy-module-names --allow-external-contracts
transpile_test_net: DAFNY_OPTIONS=--allow-warnings --include-test-runner --compile-suffix --legacy-module-names --allow-external-contracts

transpile_implementation_java: DAFNY_OPTIONS=--allow-warnings --compile-suffix --legacy-data-constructors --legacy-module-names --allow-external-contracts
transpile_test_java: DAFNY_OPTIONS=--allow-warnings --include-test-runner --compile-suffix --legacy-data-constructors --legacy-module-names --allow-external-contracts

transpile_implementation_python: DAFNY_OPTIONS=--allow-warnings --allow-external-contracts
transpile_test_python: DAFNY_OPTIONS=--allow-warnings --include-test-runner --allow-external-contracts
