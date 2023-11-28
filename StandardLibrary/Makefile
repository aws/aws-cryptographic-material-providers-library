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

_python_underscore_extern_names:
	find src -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/module {:extern \".*\"/s/\./_/g' {} \;
	echo "Skipping Model modification for StandardLibrary"
	find test -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/module {:extern \".*\"/s/\./_/g' {} \;

_python_revert_underscore_extern_names:
	find src -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/module {:extern \".*\"/s/_/\./g' {} \;
	echo "Skipping Model modification for StandardLibrary"
	find test -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/module {:extern \".*\"/s/_/\./g' {} \;

format_net:
	pushd runtimes/net && dotnet format && popd
