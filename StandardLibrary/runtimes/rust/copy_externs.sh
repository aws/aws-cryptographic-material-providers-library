#!/bin/bash -eu

echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

cd $( dirname ${BASH_SOURCE[0]} )

SRC=../../../AwsCryptographicMaterialProviders/runtimes/rust/src/

cp $SRC/concurrent_call.rs src
cp $SRC/sets.rs src
cp $SRC/time.rs src
cp $SRC/uuid.rs src
