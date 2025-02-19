# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2

USE_DAFNY_STANDARD_LIBRARIES=1

include ../SharedMakefileV2.mk

MAX_RESOURCE_COUNT=500000000
LIBRARIES :=

# Since everything depends on the StandardLibrary
# it is included as a library in the SharedMakefile.
# However, this means this it could not build...
# So we empty the variable here
# and check in the Makefile
transpile_dependencies: STD_LIBRARY=

# Override SharedMakefile's transpile_implementation to not reference
# StandardLibrary as a Library
transpile_implementation: SRC_INDEX_TRANSPILE=$(if $(SRC_INDEX),$(SRC_INDEX),src)
transpile_implementation:
	find ./dafny/**/$(SRC_INDEX_TRANSPILE)/ ./$(SRC_INDEX_TRANSPILE)/ -name 'Index.dfy' | sed -e 's/^/include "/' -e 's/$$/"/' | dafny \
	translate $(TARGET) \
		--stdin \
		--no-verify \
		--cores:$(CORES) \
		--optimize-erasable-datatype-wrapper:false \
		--unicode-char:false \
		--function-syntax:3 \
		--output $(OUT) \
		$(if $(USE_DAFNY_STANDARD_LIBRARIES), ./bin/DafnyStandardLibraries-smithy-dafny-subset.doo, ) \
		$(DAFNY_OPTIONS) \
		$(DAFNY_OTHER_FILES) \
		$(TRANSPILE_MODULE_NAME)

transpile_test:
	dafny --version
	find ./dafny/**/$(TEST_INDEX_TRANSPILE) ./$(TEST_INDEX_TRANSPILE) -name "*.dfy" -name '*.dfy' | sed -e 's/^/include "/' -e 's/$$/"/' | dafny \
		translate $(TARGET) \
		--stdin \
		--no-verify \
		--cores:$(CORES) \
		--optimize-erasable-datatype-wrapper:false \
		--unicode-char:false \
		--function-syntax:3 \
		--output $(OUT) \
		$(DAFNY_OPTIONS) \
		$(DAFNY_OTHER_FILES) \
		$(if $(strip $(STD_LIBRARY)) , --library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy, ) \
		$(if $(USE_DAFNY_STANDARD_LIBRARIES) , --library:./bin/DafnyStandardLibraries-smithy-dafny-subset.doo, ) \
		$(TRANSLATION_RECORD) \
		$(SOURCE_TRANSLATION_RECORD) \
		$(TRANSPILE_MODULE_NAME) \
		$(TRANSPILE_DEPENDENCIES) \

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

polymorph_dafny: $(if $(USE_DAFNY_STANDARD_LIBRARIES), build_dafny_stdlibs, )

build_dafny_stdlibs:
	dafny build -t:lib --output $(LIBRARY_ROOT)/bin/DafnyStandardLibraries-smithy-dafny-subset.doo \
		../smithy-dafny/TestModels/dafny-dependencies/StandardLibrary/DafnyStandardLibraries-smithy-dafny-subset.toml
