// Copyright Amazon.com Inc. or its affiliates.
// All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:options "/functionSyntax:4"} TestMutationIndexConversion {
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import opened Wrappers
  import DDB = Com.Amazonaws.Dynamodb
  import Structure

  const testLogPrefix := "\nTestMutationIndexConversion :: "

  method {:test} TestMutationIndexToAttributeMapWithoutLastModifiedTime() {
    var index := KeyStoreTypes.MutationIndex(
      Identifier := "test-branch-001",
      CreateTime := "2025-02-10T12:34:56Z",
      UUID := "uuid-001",
      PageIndex := [0x01, 0x02, 0x03],
      LastModifiedTime := Option.None(),
      CiphertextBlob := [0xAA, 0xBB, 0xCC]
    );

    var attrMap := Structure.MutationIndexToAttributeMap(index);

    expect Structure.BRANCH_KEY_IDENTIFIER_FIELD in attrMap, "BRANCH_KEY_IDENTIFIER_FIELD missing";
    expect attrMap[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == "test-branch-001";

    expect Structure.KEY_CREATE_TIME in attrMap, "KEY_CREATE_TIME missing";
    expect attrMap[Structure.KEY_CREATE_TIME].S == "2025-02-10T12:34:56Z";

    expect Structure.M_UUID in attrMap, "M_UUID missing";
    expect attrMap[Structure.M_UUID].S == "uuid-001";

    expect Structure.M_PAGE_INDEX in attrMap, "M_PAGE_INDEX missing";
    expect attrMap[Structure.M_PAGE_INDEX].B == [0x01, 0x02, 0x03];

    expect Structure.ENC_FIELD in attrMap, "ENC_FIELD missing";
    expect attrMap[Structure.ENC_FIELD].B == [0xAA, 0xBB, 0xCC];

    // Ensure LastModifiedTime is NOT present
    expect !(Structure.M_LAST_MODIFIED_TIME in attrMap), "M_LAST_MODIFIED_TIME should not be in the map";

    var reconstructedIndex := Structure.ToMutationIndex(attrMap);

    // Ensure round-trip data is preserved
    expect reconstructedIndex.Identifier == index.Identifier;
    expect reconstructedIndex.CreateTime == index.CreateTime;
    expect reconstructedIndex.UUID == index.UUID;
    expect reconstructedIndex.PageIndex == index.PageIndex;
    expect reconstructedIndex.CiphertextBlob == index.CiphertextBlob;
    expect reconstructedIndex.LastModifiedTime == index.LastModifiedTime;
  }

  method {:test} TestMutationIndexToAttributeMapWithLastModifiedTime() {
    var index := KeyStoreTypes.MutationIndex(
      Identifier := "test-branch-002",
      CreateTime := "2025-02-11T14:45:00Z",
      UUID := "uuid-002",
      PageIndex := [0x04, 0x05, 0x06],
      LastModifiedTime := Option.Some("2025-02-12T10:20:30Z"),
      CiphertextBlob := [0xDD, 0xEE, 0xFF]
    );

    var attrMap := Structure.MutationIndexToAttributeMap(index);

    expect Structure.M_LAST_MODIFIED_TIME in attrMap, "M_LAST_MODIFIED_TIME missing";
    expect attrMap[Structure.M_LAST_MODIFIED_TIME].S == "2025-02-12T10:20:30Z";
  }

  method {:test} TestMutationIndexRoundTripConversion() {
    var originalIndex := KeyStoreTypes.MutationIndex(
      Identifier := "test-roundtrip-001",
      CreateTime := "2025-02-15T18:30:00Z",
      UUID := "uuid-roundtrip",
      PageIndex := [0x10, 0x20, 0x30],
      LastModifiedTime := Option.Some("2025-02-16T20:00:00Z"),
      CiphertextBlob := [0xAB, 0xCD, 0xEF]
    );

    var attrMap := Structure.MutationIndexToAttributeMap(originalIndex);
    var reconstructedIndex := Structure.ToMutationIndex(attrMap);

    // Ensure round-trip data is preserved
    expect reconstructedIndex.Identifier == originalIndex.Identifier;
    expect reconstructedIndex.CreateTime == originalIndex.CreateTime;
    expect reconstructedIndex.UUID == originalIndex.UUID;
    expect reconstructedIndex.PageIndex == originalIndex.PageIndex;
    expect reconstructedIndex.CiphertextBlob == originalIndex.CiphertextBlob;
    expect reconstructedIndex.LastModifiedTime == originalIndex.LastModifiedTime;
  }

  method {:test} TestMutationIndexBackwardCompatibility() {
    var oldData := map[
      Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.MUTATION_INDEX_TYPE),
      Structure.HIERARCHY_VERSION := Structure.HIERARCHY_VERSION_ATTRIBUTE_VALUE,
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S("legacy-001"),
      Structure.KEY_CREATE_TIME := DDB.Types.AttributeValue.S("2025-01-01T10:00:00Z"),
      Structure.M_UUID := DDB.Types.AttributeValue.S("uuid-legacy"),
      Structure.M_PAGE_INDEX := DDB.Types.AttributeValue.B([0x00, 0x11, 0x22]),
      Structure.ENC_FIELD := DDB.Types.AttributeValue.B([0x44, 0x55, 0x66])
    ]; // No LastModifiedTime

    var reconstructedIndex := Structure.ToMutationIndex(oldData);

    expect reconstructedIndex.Identifier == "legacy-001";
    expect reconstructedIndex.CreateTime == "2025-01-01T10:00:00Z";
    expect reconstructedIndex.UUID == "uuid-legacy";
    expect reconstructedIndex.PageIndex == [0x00, 0x11, 0x22];
    expect reconstructedIndex.CiphertextBlob == [0x44, 0x55, 0x66];

    // Ensure LastModifiedTime defaults to None
    expect !reconstructedIndex.LastModifiedTime.Some?;
  }

  method {:test} TestMutationIndexHandlesOptionalLastModifiedTime() {
    var baseData := map[
      Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.MUTATION_INDEX_TYPE),
      Structure.HIERARCHY_VERSION := Structure.HIERARCHY_VERSION_ATTRIBUTE_VALUE,
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S("test-mixed-001"),
      Structure.KEY_CREATE_TIME := DDB.Types.AttributeValue.S("2025-02-20T12:00:00Z"),
      Structure.M_UUID := DDB.Types.AttributeValue.S("uuid-mixed"),
      Structure.M_PAGE_INDEX := DDB.Types.AttributeValue.B([0x77, 0x88, 0x99]),
      Structure.ENC_FIELD := DDB.Types.AttributeValue.B([0xAA, 0xBB, 0xCC]),
      Structure.M_LAST_MODIFIED_TIME := DDB.Types.AttributeValue.S("2025-02-22T09:00:00Z")
    ];

    var reconstructedIndex := Structure.ToMutationIndex(baseData);

    expect reconstructedIndex.Identifier == "test-mixed-001";
    expect reconstructedIndex.CreateTime == "2025-02-20T12:00:00Z";
    expect reconstructedIndex.UUID == "uuid-mixed";
    expect reconstructedIndex.PageIndex == [0x77, 0x88, 0x99];
    expect reconstructedIndex.CiphertextBlob == [0xAA, 0xBB, 0xCC];

    // Ensure LastModifiedTime is correctly interpreted
    expect reconstructedIndex.LastModifiedTime.Some?;
    expect reconstructedIndex.LastModifiedTime.value == "2025-02-22T09:00:00Z";
  }
}