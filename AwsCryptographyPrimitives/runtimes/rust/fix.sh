#!/bin/bash

cd $( dirname -- "${BASH_SOURCE[0]}" )
pwd

../../../StandardLibrary/runtimes/rust/fix.sh

mv src/implementation_from_dafny.rs src/implementation_from_dafny.saved_rs

cat impl_header.txt > src/implementation_from_dafny.rs

tail +9 src/implementation_from_dafny.saved_rs >> src/implementation_from_dafny.rs

ghead -n -3 tests/tests_from_dafny/mod.rs | tail +3 >> src/implementation_from_dafny.rs

perl -i -pe 's/crate::r#_Wrappers_Compile/mpl_standard_library::_Wrappers_Compile/g' src/implementation_from_dafny.rs
perl -i -pe 's/crate::r#_HexStrings_Compile/mpl_standard_library::_HexStrings_Compile/g' src/implementation_from_dafny.rs
perl -i -pe 's/crate::r#_StandardLibrary_Compile/mpl_standard_library::_StandardLibrary_Compile/g' src/implementation_from_dafny.rs
perl -i -pe 's/crate::UTF8/mpl_standard_library::UTF8/g' src/implementation_from_dafny.rs
