package _Time

import (
	"time"

	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

func CurrentRelativeTime() int64 {
	return int64(time.Now().Unix())
}

func GetCurrentTimeStamp() Wrappers.Result {
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfChars([]dafny.Char(time.Now().Format("2006-01-02T15:04:05.000000Z"))...))
}

func CurrentRelativeTimeMilli() int64 {
	return time.Now().UnixMilli()
}
