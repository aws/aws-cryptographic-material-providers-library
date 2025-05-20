//go:build !windows
// +build !windows

package _Time

import "syscall"

func GetProcessCpuTimeMillis() int64 {
	var usage syscall.Rusage
	err := syscall.Getrusage(syscall.RUSAGE_SELF, &usage)
	if err != nil {
		return 0
	}
	return (usage.Utime.Nano() + usage.Stime.Nano()) / 1000000
}