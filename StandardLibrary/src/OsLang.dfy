// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:extern "OsLang"} OsLang {

  // returns one of : MacOS, Windows, Unix, Other
  function method {:extern} GetOsShort() : string

  // returns one of : Java, Dotnet, Go, Python, Rust
  function method {:extern} GetLanguageShort() : string

  // returns a human readable, language specific, unstable over time, description of the OS
  function method {:extern} GetOsLong() : string

  // returns a human readable, language specific, unstable over time, description of the Language
  function method {:extern} GetLanguageLong() : string

  function method GetPlatformShort() : string
  {
    GetLanguageShort() + " " + GetOsShort()
  }

  function method GetPlatformLong() : string
  {
    GetLanguageLong() + " " + GetOsLong()
  }

}