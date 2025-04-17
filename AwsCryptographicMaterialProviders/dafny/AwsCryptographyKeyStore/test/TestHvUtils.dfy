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
    var activeSHA := [
      54, -52, -120, -57, -51, -110, -103, 54, 61, -87, 40, -9, -117, 92, 4,  61,
      37, -12, -23, 55, 89, 127, 107, 13, 85, 46, 122, 20, -71, -95, -108, -61,
      -69, 107, -87, 126, -77, -7, -27, 63, 71, -106, -121, 81, -70, -52, -70, 41
    ];
    var actualActiveSHA :- expect HvUtils.CreateBKCDigest(activeBKC, crypto);
    expect actualActiveSHA == activeSHA;

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
    var decryptOnlySHA: seq<uint8> := [
      109, -70, 69, 45, 104, 55, 54, -65, -121, -113, -80, 85, 47, 62, 20, -115,
      -3, -28, 124, 11, 76, -33, -61, 79, 65, -127, 99, -67, -77, 1, -5, -112,
      -35, -59, -67, -30, 106, -124, -88, -124, 113, 9, -57, 81, -81, 117, -112, 21
    ];
    var actualDecryptOnlySHA :- expect HvUtils.CreateBKCDigest(decryptOnlyBKC, crypto);
    expect actualDecryptOnlySHA == decryptOnlySHA;

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
    var beaconSHA: seq<uint8> := [
      20, 15, 0, -5, 100, 98, 54, -33, 92, -125, 60, 60, 18, -116, -105, 18,
      58, -126, 123, 11, -111, -101, 46, -62, 11, 32, -39, -60, 79, -43, 100, -108,
      -72, 76, -77, -1, -77, 69, -12, 98, 70, 83, 29, -91, 59, 60, 120, 38
    ];
    var actualBeaconSHA: seq<uint8> :- expect HvUtils.CreateBKCDigest(beaconBKC, crypto);
    expect actualBeaconSHA == beaconSHA;
  }
}