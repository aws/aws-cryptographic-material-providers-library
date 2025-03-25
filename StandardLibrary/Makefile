# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

include ../SharedMakefileV2.mk

MAX_RESOURCE_COUNT=500000000
LIBRARIES :=

# Since everything depends on the StandardLibrary
# it is included as a library in the SharedMakefile.
# However, this means this it could not build...
# So we empty the variable here
# and check in the Makefile
transpile_implementation: STD_LIBRARY=
transpile_test: STD_LIBRARY=
transpile_dependencies: STD_LIBRARY=

GO_MODULE_NAME="github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library"

# Python
PYTHON_MODULE_NAME=smithy_dafny_standard_library

RUST_OTHER_FILES := \
        runtimes/rust/src/concurrent_call.rs \
        runtimes/rust/src/dafny_libraries.rs \
        runtimes/rust/src/oslang.rs \
        runtimes/rust/src/sets.rs \
        runtimes/rust/src/time.rs \
	runtimes/rust/src/uuid.rs

polymorph_rust:
	@echo no polymorph needed for StandardLibrary
