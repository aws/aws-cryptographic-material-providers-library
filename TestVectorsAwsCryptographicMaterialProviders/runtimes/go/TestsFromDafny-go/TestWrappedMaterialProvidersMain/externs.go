package TestWrappedMaterialProvidersMain

import "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"

func GetTestVectorExecutionDirectory() dafny.Sequence {
	return dafny.SeqOfChars([]dafny.Char("")...)
}
