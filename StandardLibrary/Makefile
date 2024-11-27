# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

CORES=2


MAX_RESOURCE_COUNT=500000000
LIBRARIES :=



# Override with our new version
transpile_go: | remove_extern
	make restore_extern

remove_extern:
	@sed -i '' 's/{:extern "DafnyLibraries.FileIO", "INTERNAL_ReadBytesFromFile"}/{:extern "INTERNAL_ReadBytesFromFile"}/g' ../libraries/src/FileIO/FileIO.dfy
	@sed -i '' 's/{:extern "DafnyLibraries.FileIO", "INTERNAL_WriteBytesToFile"}/{:extern "INTERNAL_WriteBytesToFile"}/g' ../libraries/src/FileIO/FileIO.dfy
	@echo "Remove DafnyLibraries.FileIO externs"

restore_extern:
	@sed -i '' 's/{:extern "INTERNAL_ReadBytesFromFile"}/{:extern "DafnyLibraries.FileIO", "INTERNAL_ReadBytesFromFile"}/g' ../libraries/src/FileIO/FileIO.dfy
	@sed -i '' 's/{:extern "INTERNAL_WriteBytesToFile"}/{:extern "DafnyLibraries.FileIO", "INTERNAL_WriteBytesToFile"}/g' ../libraries/src/FileIO/FileIO.dfy
	@echo "Restore DafnyLibraries.FileIO externs"

# Since everything depends on the StandardLibrary
# it is included as a library in the SharedMakefile.
# However, this means this it could not build...
# So we empty the variable here
# and check in the Makefile
transpile_implementation: STD_LIBRARY=
transpile_test: STD_LIBRARY=
transpile_dependencies: STD_LIBRARY=

GO_MODULE_NAME="github.com/dafny-lang/DafnyStandardLibGo"

# Python
PYTHON_MODULE_NAME=smithy_dafny_standard_library

RUST_OTHER_FILES := \
        runtimes/rust/src/concurrent_call.rs \
        runtimes/rust/src/sets.rs \
        runtimes/rust/src/time.rs \
	runtimes/rust/src/uuid.rs

polymorph_rust:
	@echo no polymorph needed for StandardLibrary

include ../SharedMakefileV2.mk
