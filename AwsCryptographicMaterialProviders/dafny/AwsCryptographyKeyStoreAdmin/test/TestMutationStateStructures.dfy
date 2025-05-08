// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "AdminFixtures.dfy"
include "../src/MutationStateStructures.dfy"

/** Tests the logic in Mutation State Structures */
module {:options "/functionSyntax:4" } TestMutationStateStructures {
  import opened Wrappers
  import UUID
  import Fixtures
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import AdminFixtures
  import CleanupItems
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import JSON = JSON.API

  import MutationStateStructures

  // Helper method to validate MutationDetails equality
  method ValidateMutationDetails(actual: Types.MutationDetails, expected: Types.MutationDetails)
  {
    // Validate Original Properties
    expect actual.Original.KmsArn == expected.Original.KmsArn;
    expect actual.Original.EncryptionContext == expected.Original.EncryptionContext;
    expect actual.Original.HierarchyVersion == expected.Original.HierarchyVersion;

    // Validate Terminal Properties
    expect actual.Terminal.KmsArn == expected.Terminal.KmsArn;
    expect actual.Terminal.EncryptionContext == expected.Terminal.EncryptionContext;
    expect actual.Terminal.HierarchyVersion == expected.Terminal.HierarchyVersion;

    // Validate Mutations Input
    expect actual.Input.TerminalKmsArn == expected.Input.TerminalKmsArn;
    expect actual.Input.TerminalEncryptionContext == expected.Input.TerminalEncryptionContext;
    expect actual.Input.TerminalHierarchyVersion == expected.Input.TerminalHierarchyVersion;

    // Validate Remaining Commitment fields
    expect actual.SystemKey == expected.SystemKey;
    expect actual.CreateTime == expected.CreateTime;
    expect actual.UUID == expected.UUID;
  }

  // Test a pre-HV-2 Mutation Commitment Deserializes Correctly
  method {:test} TestPreHV2DeserializeMutation()
  {
    var underTest :- expect AdminFixtures.DefaultAdmin();

    // Test case 1: System Key
    var expectedDetails1 := Types.MutationDetails(
      Original := Types.MutableBranchKeyContext(
        KmsArn := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126",
        EncryptionContext := map["aws-crypto-ec:ExampleContextKey" := "ExampleContextValue"],
        HierarchyVersion := KeyStoreTypes.HierarchyVersion.v1
      ),
      Terminal := Types.MutableBranchKeyContext(
        KmsArn := "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8",
        EncryptionContext := map["aws-crypto-ec:Robbie" := "is a dog."],
        HierarchyVersion := KeyStoreTypes.HierarchyVersion.v1
      ),
      Input := Types.Mutations(
        TerminalKmsArn := Some("arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"),
        TerminalEncryptionContext := Some(map["Robbie" := "is a dog."]),
        TerminalHierarchyVersion := None
      ),
      SystemKey := "KMS Symmetric Encryption",
      CreateTime := "2025-04-18T21:18:41.000871Z",
      UUID := "0aa2b18c-c639-4558-bb30-158ac2a22571"
    );

    var response1 := underTest.DescribeMutation(Types.DescribeMutationInput(
                                                  Identifier := AdminFixtures.STATIC_PRE_HV2_MUTATION_WITH_SYSTEM_KEY
                                                ));
    expect response1.Success?;
    expect response1.value.MutationInFlight.Yes?;
    ValidateMutationDetails(
      response1.value.MutationInFlight.Yes.MutationDetails,
      expectedDetails1
    );

    // Test case 2: Trust Storage
    var expectedDetails2 := Types.MutationDetails(
      Original := Types.MutableBranchKeyContext(
        KmsArn := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126",
        EncryptionContext := map["aws-crypto-ec:ExampleContextKey" := "ExampleContextValue"],
        HierarchyVersion := KeyStoreTypes.HierarchyVersion.v1
      ),
      Terminal := Types.MutableBranchKeyContext(
        KmsArn := "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8",
        EncryptionContext := map["aws-crypto-ec:Robbie" := "is a dog."],
        HierarchyVersion := KeyStoreTypes.HierarchyVersion.v1
      ),
      Input := Types.Mutations(
        TerminalKmsArn := Some("arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"),
        TerminalEncryptionContext := Some(map["Robbie" := "is a dog."]),
        TerminalHierarchyVersion := None
      ),
      SystemKey := "Trust Storage",
      CreateTime := "2025-04-18T21:18:42.000475Z",
      UUID := "7c9d2406-4836-40db-819c-fb41d4067910"
    );

    var response2 := underTest.DescribeMutation(Types.DescribeMutationInput(
                                                  Identifier := AdminFixtures.STATIC_PRE_HV2_MUTATION_WITH_TRUST_STORAGE
                                                ));
    expect response2.Success?;
    expect response2.value.MutationInFlight.Yes?;
    ValidateMutationDetails(
      response2.value.MutationInFlight.Yes.MutationDetails,
      expectedDetails2
    );
  }

  method {:test} TestJSON()
  {
    var ec := map[
      "aws-crypto-ec:\n\n\u0007" := "VAPTTEST",
      "aws-crypto-ec:beerArn" := "arn:aws:beer:us-west-2:111122223333:ipa/50a8ec44-db00-4623-9c3f-daac62d61e28"
    ];
    var json := MutationStateStructures.EncryptionContextStringToJSON(ec);
    print("\nJSON value:\n");
    print(json);
    var backFromJSON := MutationStateStructures.JSONToEncryptionContextString(json);
    print(backFromJSON);
    expect ec == backFromJSON;

    var originalBytes :- expect JSON.Serialize(json);
    print("\nSerialized bytes:\n");
    print(originalBytes);
    var jsonFromDeserialize :- expect JSON.Deserialize(originalBytes);
    print("\nDeserialized bytes:\n");
    print(jsonFromDeserialize);
    expect jsonFromDeserialize == json;
  }

  /*
    // Helper method to recover in-flight mutation from pre HV-2 and complete the mutation.
    method TestPreHV2DeserializeMutationSystemKey(
      id : string
    )
    {
      var underTest :- expect AdminFixtures.DefaultAdmin();
      var kmsClient :- expect Fixtures.ProvideKMSClient();
      var reEncryptStrategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
      var kmsSystemKey := Types.SystemKey.kmsSymmetricEncryption(
        kmsSymmetricEncryption := Types.KmsSymmetricEncryption(
          KmsArn := Fixtures.kmsSystemKey,
          AwsKms := KeyStoreTypes.AwsKms(
            grantTokens := None,
            kmsClient := Some(kmsClient))));
      var request := Types.DescribeMutationInput(
        Identifier:= id
      );
      var response := underTest.DescribeMutation(request);
      expect response.Success?, "Mutation Commitment is present, however unable to deserialize.";
      expect response.value.MutationInFlight.Yes?;
      var token := response.value.MutationInFlight.Yes.MutationToken;

      var testInput := Types.ApplyMutationInput(
        MutationToken := token,
        PageSize := Some(10), //Some(24),
        Strategy := Some(reEncryptStrategy),
        SystemKey := kmsSystemKey);
  
      var applyOutput? :- expect underTest.ApplyMutation(testInput);
      expect applyOutput?.MutationResult.CompleteMutation?, "Should COMPLETE mutations for pre HV-2 in-flight mutations";
    }

    // This test verifies that in-flight mutation can be successfully recovered with pre-HV-2 changes and complete mutation
    // It copies a static branch key with in-flight/in-complete muations from static table to simulate an in-flight mutation
    // After copying, it verifies the mutation can be properly deserialized, recovered and completed.
    method {:test} copyBranchKeyTest() {
      var ddbClient? :- expect Fixtures.ProvideDDBClient();
  
      var bkid := AdminFixtures.STATIC_PRE_HV2_MUTATION_WITH_SYSTEM_KEY;
  
      // Delete the Branch Key, if there's one already exists in Testing Key Store Table.
      // var _ := CleanupItems.DeleteBranchKey(Identifier:= bkid, ddbClient:=ddbClient?);
  
      var isCopied :- expect Fixtures.CopyBranchKey(
        Identifier := bkid,
        sourceTableName := Fixtures.staticBranchKeyStoreName,
        targetTableName := Fixtures.branchKeyStoreName,
        hierarchyVersion := "1",
        ddbClient := ddbClient?
      );
      expect isCopied, "There are still some items left which are not copied from static key store table.";
  
      TestPreHV2DeserializeMutationSystemKey(bkid);
    }
  */
}
