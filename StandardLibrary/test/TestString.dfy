// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/String.dfy"
include "../src/OsLang.dfy"
include "../../libraries/src/Wrappers.dfy"
include "../../libraries/src/FileIO/FileIO.dfy"

module TestStrings {
  import StandardLibrary.String
  import opened Wrappers
  import opened FileIO
  import OsLang

  method {:test} TestHasSubStringPos()
  {
    var actual := String.HasSubStringPos("Koda is a Dog.", "Koda", 0);
    expect actual == Some(0);
    actual := String.HasSubStringPos("Koda is a Dog.", "Koda", 1);
    expect actual == None;

    actual := String.HasSubStringPos("Koda is a Dog.", "Dog", 0);
    expect actual == Some(10);
    actual := String.HasSubStringPos("Koda is a Dog.", "Dog", 10);
    expect actual == Some(10);
    actual := String.HasSubStringPos("Koda is a Dog.", "Dog", 11);
    expect actual == None;
  }

  method {:test} TestSearchAndReplace()
  {
    var actual := String.SearchAndReplace("Koda is a Dog.", "Koda", "Robbie");
    expect actual == "Robbie is a Dog.";
    actual := String.SearchAndReplace("Koda is a Dog.", "Dog", "good boy");
    expect actual == "Koda is a good boy.";
    actual := String.SearchAndReplace("Koda is a Dog.", "Dog.", "good boy!");
    expect actual == "Koda is a good boy!";
    actual := String.SearchAndReplace("Koda is a Dog.", "Robbie", "good boy!");
    expect actual == "Koda is a Dog.";
    actual := String.SearchAndReplace("Koda is a Dog.", "Koda", "Koda");
    expect actual == "Koda is a Dog.";
  }

  method {:test} TestSearchAndReplaceAll()
  {
    var actual := String.SearchAndReplaceAll("Koda is a Dog.", "Koda", "Robbie");
    expect actual == "Robbie is a Dog.";
    actual := String.SearchAndReplaceAll("Koda is a Dog.", "Dog", "good boy");
    expect actual == "Koda is a good boy.";
    actual := String.SearchAndReplaceAll("Koda is a Dog.", "Dog.", "good boy!");
    expect actual == "Koda is a good boy!";
    actual := String.SearchAndReplaceAll("Koda is a Dog.", "Robbie", "good boy!");
    expect actual == "Koda is a Dog.";
    actual := String.SearchAndReplaceAll("Koda is a Dog.", "Koda", "Koda");
    expect actual == "Koda is a Dog.";

    actual := String.SearchAndReplaceAll("A rose is a rose is a rose.", "rose", "daisy");
    expect actual == "A daisy is a daisy is a daisy.";
    actual := String.SearchAndReplaceAll("rose is a rose is a rose", "rose", "daisy");
    expect actual == "daisy is a daisy is a daisy";
    actual := String.SearchAndReplaceAll("rose is a rose is a rose", "rose", "rose_daisy");
    expect actual == "rose_daisy is a rose_daisy is a rose_daisy";
  }

  method {:test} TestHasSearchAndReplacePos()
  {
    var actual := String.SearchAndReplacePos("Koda is a Dog.", "Koda", "Robbie", 0);
    expect actual == ("Robbie is a Dog.", Some(6));
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Koda", "Robbie", 1);
    expect actual == ("Koda is a Dog.", None);

    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog", "good boy", 0);
    expect actual == ("Koda is a good boy.", Some(18));
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog", "good boy", 10);
    expect actual == ("Koda is a good boy.", Some(18));
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog", "good boy", 11);
    expect actual == ("Koda is a Dog.", None);

    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog.", "good boy!", 0);
    expect actual == ("Koda is a good boy!", Some(19));
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog.", "good boy!", 10);
    expect actual == ("Koda is a good boy!", Some(19));
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Dog.", "good boy!", 11);
    expect actual == ("Koda is a Dog.", None);


    actual := String.SearchAndReplacePos("Koda is a Dog.", "Robbie", "good boy!", 0);
    expect actual == ("Koda is a Dog.", None);
    actual := String.SearchAndReplacePos("Koda is a Dog.", "Koda", "Koda", 0);
    expect actual == ("Koda is a Dog.", Some(4));
  }

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

  function method BadFilename() : string
  {
    if OsLang.GetOsShort() == "Windows" && OsLang.GetLanguageShort() == "Dotnet" then
      "foo:bar:baz"
    else
      "/../../MyFile"
  }
  // This test relies on OS-specific behavior.
  // It appears to work on GHA runners and developers' local environments,
  // but not in Python on the Linux image used by our CodeBuild projects.
  // The team agrees this test does not add significant value and can be removed until
  // it works in expected environments.
  /*
    // ensure that FileIO error are returned properly, and not a panic! or the like
    method {:test} TestBadFileIO()
    {
      var x := WriteBytesToFile(BadFilename(), [1,2,3,4,5]);
      expect x.Failure?;
    }
  */
}