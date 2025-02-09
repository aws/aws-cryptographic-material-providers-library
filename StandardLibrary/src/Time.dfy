// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "./StandardLibrary.dfy"
include "./UInt.dfy"
include "./String.dfy"
include "./OsLang.dfy"

module {:extern "Time"} Time {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import StandardLibrary.String
  import OsLang

  // Time is non-deterministic.
  // In this way it is similar to random number.
  // As such it MUST NOT be a Dafny function.
  // Dafny functions MUST be deterministic.
  // var t1 :- GetCurrentTimeStamp();
  // wait
  // var t2 :- GetCurrentTimeStamp();
  // assert t1 == t2; // this will be true if GetCurrentTimeStamp is a function.

  // Returns the number of seconds since some fixed-as-long-as-this-program-is-running moment in the past
  // Time is represented as signed over unsigned because java does not do unsigned
  // values - net can do both so we are able to change the representation to signed.
  method {:extern "CurrentRelativeTime"} GetCurrent() returns (res: int64)
    // We are able to make this claim because it does not make sense for time to
    // be negative.
    ensures res >= 0

  // Returns the number of milliseconds since some fixed-as-long-as-this-program-is-running moment in the past
  // Time is represented as signed over unsigned because java does not do unsigned
  // values - net can do both so we are able to change the representation to signed.
  method {:extern "CurrentRelativeTimeMilli"} GetCurrentMilli() returns (res: int64)
    // We are able to make this claim because it does not make sense for time to
    // be negative.
    ensures res >= 0

  // Returns the number of milliseconds of CPU used by the current process so far.
  // Time is represented as signed over unsigned because java does not do unsigned
  // values - net can do both so we are able to change the representation to signed.
  method {:extern "GetProcessCpuTimeMillis"} GetProcessCpuTimeMillis() returns (res: int64)
    // We are able to make this claim because it does not make sense for time to
    // be negative.
    ensures res >= 0

  // Returns a timestamp for the current time in ISO8601 format in UTC
  // to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
  method {:extern "GetCurrentTimeStamp"} GetCurrentTimeStamp() returns (res: Result<string, string>)

  function method FormatMilli(diff : uint64) : string
  {
    var whole := String.Base10Int2String((diff / 1000) as int);
    var frac := String.Base10Int2String((diff % 1000) as int);
    if |frac| == 1 then
      whole + ".00" + frac
    else if |frac| == 2 then
      whole + ".0" + frac
    else
      whole + "." + frac
  }

  function method FormatMilliDiff(start : int64, end : int64) : string
    requires start >= 0
    requires end >= 0
  {
    if start <= end then
      FormatMilli((end - start) as uint64)
    else
      "-" + FormatMilli((start - end) as uint64)
  }

  datatype AbsoluteTime = AbsoluteTime(
    ClockTime : uint64,
    CpuTime : uint64
  )
  datatype RelativeTime = RelativeTime(
    ClockTime : uint64,
    CpuTime : uint64
  )
  method GetAbsoluteTime() returns (output : AbsoluteTime)
  {
    var ClockTime := GetCurrentMilli();
    var CpuTime := GetProcessCpuTimeMillis();
    return AbsoluteTime (
        ClockTime := ClockTime as uint64,
        CpuTime := CpuTime as uint64
      );
  }

  method PrintTimeSince(start : AbsoluteTime)
  {
    var t := TimeSince(start);
    PrintTime(t);
  }

  method PrintTimeSinceShort(start : AbsoluteTime)
  {
    var t := TimeSince(start);
    PrintTimeShort(t);
  }

  method PrintTimeSinceShortChained(start : AbsoluteTime) returns (x : AbsoluteTime)
  {
    var end := GetAbsoluteTime();
    PrintTimeShort(TimeDiff(start, end));
    return end;
  }

  function method TimeDiff(start : AbsoluteTime, end : AbsoluteTime) : RelativeTime
  {
    if start.ClockTime <= end.ClockTime && start.CpuTime <= end.CpuTime then
      RelativeTime (
        ClockTime := end.ClockTime - start.ClockTime,
        CpuTime := end.CpuTime - start.CpuTime
      )
    else
      RelativeTime (
        ClockTime := 0,
        CpuTime := 0
      )
  }

  method TimeSince(start : AbsoluteTime) returns (output : RelativeTime)
  {
    var end := GetAbsoluteTime();
    output := TimeDiff(start, end);
  }

  method PrintTime(time : RelativeTime)
  {
    print "Clock Time : ", FormatMilli(time.ClockTime), " CPU Time : ", FormatMilli(time.CpuTime), "\n";
  }

  method PrintTimeSinceLong(start : AbsoluteTime, tag : string)
  {
    var t := TimeSince(start);
    PrintTimeLong(t, tag);
  }

  method PrintTimeLong(time : RelativeTime, tag : string)
  {
    print tag, " ", OsLang.GetOsShort(), " ", OsLang.GetLanguageShort(), " ", FormatMilli(time.ClockTime), " ", FormatMilli(time.CpuTime), "\n";
  }

  method PrintTimeShort(time : RelativeTime)
  {
    print "CPU:", FormatMilli(time.CpuTime), " ";
  }

  // The next two functions are for the benefit of the extern implementation to call,
  // avoiding direct references to generic datatype constructors
  // since their calling pattern is different between different versions of Dafny
  // (i.e. after 4.2, explicit type descriptors are required).

  function method CreateGetCurrentTimeStampSuccess(value: string): Result<string, string> {
    Success(value)
  }

  function method CreateGetCurrentTimeStampFailure(error: string): Result<string, string> {
    Failure(error)
  }
}
