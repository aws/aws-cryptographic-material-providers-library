package _Time

import (
	"time"

	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func (static *CompanionStruct_Default___) CurrentRelativeTime() int64 {
	return int64(time.Now().Second())
}

func (static *CompanionStruct_Default___) GetCurrentTimeStamp() Wrappers.Result {
	//t := time.Now()
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfChars([]dafny.Char(time.Now().Format("2006-01-02T15:04:05.000000Z"))...))
}
