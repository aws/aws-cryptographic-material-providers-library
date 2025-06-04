// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/PrefixUtils.dfy"

module {:options "/functionSyntax:4" } TestPrefixUtils {
  import opened PrefixUtils

  method {:test} TestFilterMapForKeysThatDoNotBeginWithPrefix() {
    var mapWithPrefix := map[
      "aws-crypto-ec:Koda" := "is a dog.",
      "Robbie" := "is a dog."];
    var actual := FilterMapForKeysThatDoNotBeginWithPrefix(
      prefix := "aws-crypto-ec:",
      aMap := mapWithPrefix);
    expect actual == map["Robbie" := "is a dog."];
  }
}
