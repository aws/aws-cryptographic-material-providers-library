package _Time

import (
	"syscall"
	"time"

	"github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	"github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
)

var m__Time = CompanionStruct_Default___{}

func (CompanionStruct_Default___) CurrentRelativeTimeMilli() int64 {
	return CurrentRelativeTimeMilli()
}

func (CompanionStruct_Default___) CurrentRelativeTime() int64 {
	return CurrentRelativeTime()
}
func CurrentRelativeTime() int64 {
	return int64(time.Now().Second())
}

func (CompanionStruct_Default___) GetCurrentTimeStamp() Wrappers.Result {
	return GetCurrentTimeStamp()
}

func GetCurrentTimeStamp() Wrappers.Result {
	return Wrappers.Companion_Result_.Create_Success_(dafny.SeqOfChars([]dafny.Char(time.Now().Format("2006-01-02T15:04:05.000000Z"))...))
}

func CurrentRelativeTimeMilli() int64 {
	return time.Now().UnixMilli()
}

func (CompanionStruct_Default___) GetProcessCpuTimeMillis() int64 {
	return GetProcessCpuTimeMillis()
}

func GetProcessCpuTimeMillis() int64 {
	var usage syscall.Rusage
	err := syscall.Getrusage(syscall.RUSAGE_SELF, &usage)
	if err != nil {
		return 0
	}
	return (usage.Utime.Nano() + usage.Stime.Nano()) / 1000000
}
