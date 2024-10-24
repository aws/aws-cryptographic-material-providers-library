// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "./StandardLibrary.dfy"
include "./UInt.dfy"
include "./String.dfy"

module {:extern "Time"} Time {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import StandardLibrary.String

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

  // Returns a timestamp for the current time in ISO8601 format in UTC
  // to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
  method {:extern "GetCurrentTimeStamp"} GetCurrentTimeStamp() returns (res: Result<string, string>)

  function method FormatMilli(diff : nat) : string
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
      FormatMilli(end as nat - start as nat)
    else
      "-" + FormatMilli(start as nat - end as nat)
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
