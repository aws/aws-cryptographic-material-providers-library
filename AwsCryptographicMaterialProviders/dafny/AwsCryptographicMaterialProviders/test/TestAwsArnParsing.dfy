// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/AwsArnParsing.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"

// These tests are not really needed,
// as proofs cover this logic.
// However, it helps to clarify how to use these.
module TestAwsArnParsing {
  import opened AwsArnParsing
  import opened Fixtures
  import opened Wrappers
  
  method {:test} ParseAwsKmsIdentifierAliasSuccess() {
    var actual :- expect ParseAwsKmsIdentifier(kmsKeyAlias);
  }

  method {:test} ParseAwsKmsArnAliasSuccess() {
    var actual :- expect ParseAwsKmsArn(kmsKeyAlias);
    expect actual.region == "us-west-2";
    expect actual.resource.resourceType == "alias";
    expect actual.resource.value == "postalHorn";
  }

  method {:test} ParseAwsKmsArnKeySuccess() {
    var actual :- expect ParseAwsKmsArn(postalHornKeyArn);
    expect actual.region == "us-west-2";
    expect actual.resource.resourceType == "key";
    expect actual.resource.value == "bc127593-f7da-452c-a1f3-cd34c46f81f8";
  }

  method {:test} ParseAwsKmsArnFractionOfAliasFails() {
    var actual := ParseAwsKmsArn("alias/postalHorn");
    expect actual.Failure?;
    expect actual.error == "Malformed arn: alias/postalHorn";
  }

  method {:test} ParseAwsKmsArnFractionOfKeyFails() {
    var actual := ParseAwsKmsArn("key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    expect actual.error == "Malformed arn: key/bc127593-f7da-452c-a1f3-cd34c46f81f8";
    actual := ParseAwsKmsArn("370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    actual := ParseAwsKmsArn("us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    actual := ParseAwsKmsArn("kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
  }
}
