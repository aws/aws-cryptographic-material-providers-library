// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/HierarchicalVersionUtils.dfy"

module TestHvUtils {
  import HvUtils = HierarchicalVersionUtils
  import opened Wrappers
  import opened StandardLibrary.UInt
  import AtomicPrimitives

  method {:test} TestCreateBKCDigest()
  {
    var crypto :- expect HvUtils.ProvideCryptoClient();

    // Active Branch Key Context
    var activeBKC := map[
      "kms-arn" := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126",
      "branch-key-id" := "9747c15f-629e-42c0-aeaf-46f70a0952c4",
      "hierarchy-version" := "2",
      "create-time" := "2025-04-17T07:32:03.000429Z",
      "type" := "branch:ACTIVE",
      "tablename" := "KeyStoreDdbTable",
      "version" := "branch:version:dfb80b71-8e80-4d74-8ac0-0e940533219e",
      "aws-crypto-ec:Robbie" := "is a dog"
    ];
    var expectedActiveSHA : seq<uint8> := [
      54, 204, 136, 199, 205, 146, 153, 54, 61, 169, 40, 247, 139, 92, 4, 61,
      37, 244, 233, 55, 89, 127, 107, 13, 85, 46, 122, 20, 185, 161, 148, 195,
      187, 107, 169, 126, 179, 249, 229, 63, 71, 150, 135, 81, 186, 204, 186, 41
    ];
    var actualActiveSHA :- expect HvUtils.CreateBKCDigest(activeBKC, crypto);
    expect |actualActiveSHA| == 48;
    expect actualActiveSHA == expectedActiveSHA;

    // Decrypt Only Branch Key Context
    var decryptOnlyBKC := map[
      "kms-arn" := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126",
      "branch-key-id" := "9747c15f-629e-42c0-aeaf-46f70a0952c4",
      "hierarchy-version" := "2",
      "create-time" := "2025-04-17T07:32:03.000429Z",
      "type" := "branch:version:dfb80b71-8e80-4d74-8ac0-0e940533219e",
      "tablename" := "KeyStoreDdbTable",
      "aws-crypto-ec:Robbie" := "is a dog"
    ];
    var expectedDecryptOnlySHA: seq<uint8> := [
      109, 186, 69, 45, 104, 55, 54, 191, 135, 143, 176, 85, 47, 62, 20, 141,
      253, 228, 124, 11, 76, 223, 195, 79, 65, 129, 99, 189, 179, 1, 251, 144,
      221, 197, 189, 226, 106, 132, 168, 132, 113, 9, 199, 81, 175, 117, 144, 21
    ];
    var actualDecryptOnlySHA :- expect HvUtils.CreateBKCDigest(decryptOnlyBKC, crypto);
    expect |actualDecryptOnlySHA| == 48;
    expect actualDecryptOnlySHA == expectedDecryptOnlySHA;

    // Beacon Branch Key Context
    var beaconBKC := map[
      "kms-arn" := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126",
      "branch-key-id" := "9747c15f-629e-42c0-aeaf-46f70a0952c4",
      "hierarchy-version" := "2",
      "create-time" := "2025-04-17T07:32:03.000429Z",
      "type" := "beacon:ACTIVE",
      "tablename" := "KeyStoreDdbTable",
      "aws-crypto-ec:Robbie" := "is a dog"
    ];
    var expectedBeaconSHA: seq<uint8> := [
      20, 15, 0, 251, 100, 98, 54, 223, 92, 131, 60, 60, 18, 140, 151, 18,
      58, 130, 123, 11, 145, 155, 46, 194, 11, 32, 217, 196, 79, 213, 100, 148,
      184, 76, 179, 255, 179, 69, 244, 98, 70, 83, 29, 165, 59, 60, 120, 38
    ];
    var actualBeaconSHA: seq<uint8> :- expect HvUtils.CreateBKCDigest(beaconBKC, crypto);
    expect |actualBeaconSHA| == 48;
    expect actualBeaconSHA == expectedBeaconSHA;
  }
}