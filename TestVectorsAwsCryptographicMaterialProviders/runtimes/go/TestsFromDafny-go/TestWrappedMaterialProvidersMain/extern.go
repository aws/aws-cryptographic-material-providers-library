package TestWrappedMaterialProvidersMain

import (
	"fmt"
	os "os"

	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

func GetTestVectorExecutionDirectory() _dafny.Sequence {
	cwd, _ := os.Getwd()
	fmt.Println(dafny.SeqOfChars([]dafny.Char(cwd + "/../")...))
	return dafny.SeqOfChars([]dafny.Char(cwd + "/../")...)
}
