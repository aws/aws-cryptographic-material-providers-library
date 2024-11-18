package TestWrappedMaterialProvidersMain

import (
	os "os"

	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

func GetTestVectorExecutionDirectory() dafny.Sequence {
	cwd, _ := os.Getwd()
	return dafny.SeqOfChars([]dafny.Char(cwd)...)
}
