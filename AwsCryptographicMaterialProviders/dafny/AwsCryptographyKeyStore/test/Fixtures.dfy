// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../../StandardLibrary/src/Index.dfy"
include "../src/Index.dfy"

module Fixtures {
  import opened StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import UTF8
    // The following are test resources that exist in tests accounts:

  const branchKeyStoreName := "KeyStoreDdbTable"
  const logicalKeyStoreName := branchKeyStoreName
  const branchKeyId := "75789115-1deb-4fe3-a2ec-be9e885d1945"
  const branchKeyIdActiveVersion := "fed7ad33-0774-4f97-aa5e-6c766fc8af9f"

  const branchKeyIdWithEC := "4bb57643-07c1-419e-92ad-0df0df149d7c"
  // This is branchKeyIdActiveVersion above, as utf8bytes
  const branchKeyIdActiveVersionUtf8Bytes: seq<uint8> := [
    102, 101, 100, 55,  97, 100,  51, 51,  45,
    48,  55,  55, 52,  45,  52, 102, 57,  55,
    45,  97,  97, 53, 101,  45,  54, 99,  55,
    54,  54, 102, 99,  56,  97, 102, 57, 102
  ]
  // THESE ARE TESTING RESOURCES DO NOT USE IN A PRODUCTION ENVIRONMENT
  const keyArn := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126"
  const mkrKeyArn := "arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297"
  const keyId := "9d989aa2-2f9c-438c-a745-cc57d3ad0126"

  const MrkArnEast : string := "arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  const MrkArnWest : string := "arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  // Key MUST NOT exist in ap-south-2
  const MrkArnAP : string := "arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7"
  const KmsConfigEast : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnEast)
  const KmsConfigWest : Types.KMSConfiguration := Types.KMSConfiguration.kmsKeyArn(MrkArnWest)
  const KmsMrkConfigEast : Types.KMSConfiguration := Types.KMSConfiguration.mrkKmsKeyArn(MrkArnEast)
  const KmsMrkConfigWest : Types.KMSConfiguration := Types.KMSConfiguration.mrkKmsKeyArn(MrkArnWest)
  const KmsMrkConfigAP : Types.KMSConfiguration := Types.KMSConfiguration.mrkKmsKeyArn(MrkArnAP)
  const KmsMrkEC : Types.EncryptionContext := map[UTF8.EncodeAscii("abc") := UTF8.EncodeAscii("123")]
  const EastBranchKey : string := "MyEastBranch2"
  const WestBranchKey : string := "MyWestBranch2"
}
