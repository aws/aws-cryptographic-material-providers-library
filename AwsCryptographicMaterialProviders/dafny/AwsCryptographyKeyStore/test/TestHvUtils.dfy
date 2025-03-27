// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/HierarchicalVersionUtils.dfy"

module TestHvUtilsModule {
    import HvUtils = HierarchicalVersionUtils
    
    method {:test} TestCreateBKCDigest()
    {
      // Set up test inputs
      var branchKeyContext := map[
        "kms-arn":= "arn:aws:kms:us-west-2:992382771485:key/ad1d7ff3-79f3-40f4-b31d-7be4d9c8b3ca",
        "branch-key-id":= "212ab341-8bd6-4e62-9dd5-8e15563f8768hv2",
        "hierarchy-version":= "1",
        "aws-crypto-ec:Hello":= "Seattle",
        "create-time":= "2025-03-16T13:26:34.930104Z",
        "tablename":= "MyLogicalkeyStore",
        "type":= "branch:version:1f11b6d7-f1ee-4a92-aad2-c467257376db"
      ];
      
      // Create crypto client
      var cryptoClient :- expect HvUtils.ProvideCryptoClient();
      
      // Call the method
      var result := HvUtils.createBKCDigest(branchKeyContext, cryptoClient);
      
      // Assert success
      expect result.Success?;

      print(result);
    }
}