#!/bin/bash -eu

cd $( dirname ${BASH_SOURCE[0]} )

SRC=../../../AwsCryptographicMaterialProviders/runtimes/rust/src/

cp $SRC/concurrent_call.rs src
# we have a separate copy of dafny_libraries, becuase
# it must not include MutableMap
# cp $SRC/dafny_libraries.rs src
cp $SRC/oslang.rs src
cp $SRC/sets.rs src
cp $SRC/time.rs src
cp $SRC/uuid.rs src
