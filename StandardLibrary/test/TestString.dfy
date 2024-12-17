// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/String.dfy"
include "../../libraries/src/Wrappers.dfy"
include "../../libraries/src/FileIO/FileIO.dfy"

module TestStrings {
  import StandardLibrary.String
  import opened Wrappers
  import opened FileIO

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
    actual := String.HasSubString("Koda is a Dog.", "");
    expect actual == Some(0), "The empty string is in 'Koda is a Dog.' at index 0, but HasSubString does not think so";
  }

  method {:test} TestHasSubStringNegative()
  {
    var actual := String.HasSubString("Robbie is a Dog.", "Koda");
    expect actual == None, "'Robbie is a Dog.' does not contain Koda";
    actual := String.HasSubString("\t", " ");
    expect actual == None, "A tab is not a space";
    actual := String.HasSubString("large", "larger");
    expect actual == None, "Needle larger than haystack";
  }

  method {:test} TestFileIO()
  {
    var x :- expect WriteBytesToFile("MyFile", [1,2,3,4,5]);
    x :- expect AppendBytesToFile("MyFile", [6,7,8,9,10]);
    x :- expect AppendBytesToFile("MyFile", [11,12,13,14,15]);
    var y :- expect ReadBytesFromFile("MyFile");
    expect y == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
    x :- expect WriteBytesToFile("MyFile", [1,2,3,4,5]);
    y :- expect ReadBytesFromFile("MyFile");
    expect y == [1,2,3,4,5];
  }

  // ensure that FileIO error are returned properly, and not a panic! or the like
  // This fails to fail on Windows+Dotnet, becasue \ instead of /
  // method {:test} TestBadFileIO()
  // {
  //   var x := WriteBytesToFile("/../../MyFile", [1,2,3,4,5]);
  //   expect x.Failure?;
  // }

}