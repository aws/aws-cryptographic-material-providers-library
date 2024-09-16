#!/bin/bash

source ~/.xxxrc

cd $( dirname -- "${BASH_SOURCE[0]}" )

mv src/implementation_from_dafny.rs src/implementation_from_dafny.saved_rs

cat impl_header.txt > src/implementation_from_dafny.rs

tail +9 src/implementation_from_dafny.saved_rs >> src/implementation_from_dafny.rs

ghead -n -3 tests/tests_from_dafny/mod.rs | tail +3 >> src/implementation_from_dafny.rs
