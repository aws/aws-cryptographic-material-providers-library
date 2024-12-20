// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/OsLang.dfy"

module {:options "/functionSyntax:4" } TestOsLang {
  import OsLang

  method {:test} TestOsLang() {
    print "\n";
    print OsLang.GetOsShort(), "\n";
    print OsLang.GetOsLong(), "\n";
    print OsLang.GetLanguageShort(), "\n";
    print OsLang.GetLanguageLong(), "\n";
    expect OsLang.GetOsShort() == "MacOS";
    expect OsLang.GetLanguageShort() in {"Rust", "Python", "Dotnet", "Java", "Go"};
    expect OsLang.GetOsShort() in {"MacOS", "Windows", "Unix", "Other"};
  }
}
