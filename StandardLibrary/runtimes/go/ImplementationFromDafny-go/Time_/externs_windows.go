//go:build windows
// +build windows

package _Time

import (
	"golang.org/x/sys/windows"
)


func GetProcessCpuTimeMillis() int64 {
	windows.GetCurrentProcessId()
	var proc_handle windows.Handle
	var err error
	if proc_handle, err = windows.OpenProcess(windows.PROCESS_QUERY_INFORMATION|windows.PROCESS_VM_READ, false, uint32(windows.GetCurrentProcessId())); err != nil {
		return 0
	}
	var creation_time, exit_time, kernel_time, user_time *windows.Filetime
	if err = windows.GetProcessTimes(proc_handle, creation_time, exit_time, kernel_time, user_time); err != nil {
		return 0
	}
	return (int64(kernel_time.Nanoseconds()) + int64(user_time.Nanoseconds())) / 1000000
}
