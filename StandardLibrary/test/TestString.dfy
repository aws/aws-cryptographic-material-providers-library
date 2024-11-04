// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/String.dfy"
include "../../libraries/src/Wrappers.dfy"

module TestStrings {
  import StandardLibrary.String
  import opened Wrappers

  method {:test} TestHasSubStringPositive()
  {
    var actual := String.HasSubString("Koda is a Dog.", "Koda");
    expect actual == Some(0), "'Koda' is in 'Koda is a Dog.' at index 0, but HasSubString does not think so";
    actual := String.HasSubString("Koda is a Dog.", "Koda is a Dog.");
    expect actual == Some(0), "'Koda is a Dog.' is in 'Koda is a Dog.' at index 0, but HasSubString does not think so";
    actual := String.HasSubString("Koda is a Dog.", "Dog.");
    expect actual == Some(10), "'Dog.' is in 'Koda is a Dog.' at index 10, but HasSubString does not think so";
    actual := String.HasSubString("Koda is a Dog.", ".");
    expect actual == Some(13), "'.' is in 'Koda is a Dog.' at index 13, but HasSubString does not think so";
  }

  method {:test} TestHasSubStringNegative()
  {
    var actual := String.HasSubString("Robbie is a Dog.", "Koda");
    expect actual == None, "'Robbie is a Dog.' does not contain Koda";
    actual := String.HasSubString("\t", " ");
    expect actual == None, "A tab is not a space";
  }
}
