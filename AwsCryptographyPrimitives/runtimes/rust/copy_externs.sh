#!/bin/bash -eu

cd $( dirname ${BASH_SOURCE[0]} )

SRC=../../../AwsCryptographicMaterialProviders/runtimes/rust/src/

cp $SRC/aes_gcm.rs src
cp $SRC/aes_kdf_ctr.rs src
cp $SRC/concurrent_call.rs src
cp $SRC/dafny_libraries.rs src
cp $SRC/digest.rs src
cp $SRC/ecdh.rs src
cp $SRC/ecdsa.rs src
cp $SRC/hmac.rs src
cp $SRC/random.rs src
cp $SRC/rsa.rs src
cp $SRC/sets.rs src
cp $SRC/time.rs src
cp $SRC/uuid.rs src
