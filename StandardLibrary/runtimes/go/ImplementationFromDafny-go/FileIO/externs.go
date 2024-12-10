package FileIO

import (
	"io/ioutil"
	os "os"
	"path/filepath"

	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

// TODO: Drop this once we fix the DafnyLibraries.FileIO extern
var m_DafnyLibraries struct {
	FileIO CompanionStruct_Default___
}

func (_static CompanionStruct_Default___) INTERNAL_ReadBytesFromFile(path _dafny.Sequence) (isError bool, bytesRead _dafny.Sequence, errorMsg _dafny.Sequence) {
	p := func() string {
		var s string
		for i := _dafny.Iterate(path); ; {
			val, notEndOfSequence := i()
			if !notEndOfSequence {
				return s
			} else {
				s = s + string(val.(_dafny.Char))
			}
		}
	}()
	dat, err := ioutil.ReadFile(p)
	if err != nil {
		errAsSequence := _dafny.UnicodeSeqOfUtf8Bytes(err.Error())
		return true, _dafny.EmptySeq, errAsSequence
	}
	datAsSequence := _dafny.SeqOfBytes(dat)
	return false, datAsSequence, _dafny.EmptySeq
}

func (_static CompanionStruct_Default___) INTERNAL_WriteBytesToFile(path _dafny.Sequence, bytes _dafny.Sequence) (isError bool, errorMsg _dafny.Sequence) {
	p := func() string {
		var s string
		for i := _dafny.Iterate(path); ; {
			val, notEndOfSequence := i()
			if !notEndOfSequence {
				return s
			} else {
				s = s + string(val.(_dafny.Char))
			}
		}
	}()

	// Create directories
	os.MkdirAll(filepath.Dir(p), os.ModePerm)

	bytesArray := _dafny.ToByteArray(bytes)
	err := ioutil.WriteFile(p, bytesArray, 0644)
	if err != nil {
		errAsSequence := _dafny.UnicodeSeqOfUtf8Bytes(err.Error())
		return true, errAsSequence
	}
	return false, _dafny.EmptySeq
}
