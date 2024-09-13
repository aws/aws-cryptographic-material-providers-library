package UUID

import (
	"fmt"
	"github.com/dafny-lang/DafnyRuntimeGo/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
	"github.com/google/uuid"
)

func ToByteArray(seq dafny.Sequence) Wrappers.Result {
	var s string
	for i := dafny.Iterate(seq); ; {
		val, ok := i()
		if ok {
			s = s + string(val.(dafny.Char))
		} else {
			break
		}
	}
	uuidString := uuid.MustParse(s)
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfBytes(uuidString[:]))
}

func FromByteArray(seq dafny.Sequence) Wrappers.Result {
	byteArray := dafny.ToByteArray(seq)
	uuid, err := uuid.FromBytes(byteArray)
	if err != nil {
		return Wrappers.Companion_Result_.Create_Failure_(fmt.Errorf("Failed To Generate UUID From Byte Array"))
	}
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfChars([]dafny.Char(uuid.String())...))
}

func GenerateUUID() Wrappers.Result {
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfChars([]dafny.Char(uuid.NewString())...))
}
