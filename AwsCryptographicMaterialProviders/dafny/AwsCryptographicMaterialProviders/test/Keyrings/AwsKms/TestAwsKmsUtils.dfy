// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../src/Keyrings/AwsKms/AwsKmsUtils.dfy"
include "../../../../AwsCryptographyKeyStore/test/Fixtures.dfy"

// These tests are not really needed,
// as proofs cover this logic.
// However, it helps to clarify how to use these.
module TestAwsKmsUtils {
  import opened Fixtures
  import opened Wrappers
  import opened AwsKmsUtils

  method {:test} ValidateKmsKeyIdKeyArnSuccess() {
    var actual :- expect ValidateKmsKeyId(postalHornKeyArn);
  }

  method {:test} ValidateKmsKeyIdAliasSuccess() {
    var actual :- expect ValidateKmsKeyId(kmsKeyAlias);
  }

  method {:test} ValidateKmsKeyIdFractionOfKeyFails() {
    var actual := ValidateKmsKeyId("key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    actual := ValidateKmsKeyId("370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    actual := ValidateKmsKeyId("us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
    actual := ValidateKmsKeyId("kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8");
    expect actual.Failure?;
  }
}
