// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module ErrorMessages {
    function method INVALID_DATA_KEYS(keyProviderId: string, keyProviderInfo: string := "", branchKeyVersion: string := "") : string {
      if keyProviderId == "aws-kms" then
      "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                              "\n Expected: \n KeyProviderId:" + keyProviderId +                            
                              "\n KeyProviderInfo: " + keyProviderInfo

    else if keyProviderId == "aws-kms-hierarchy" then
      "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                "\n Expected: \n KeyProviderId:" + keyProviderId +                            
                                "\n KeyProviderInfo: " + keyProviderInfo +
                                "\n BranchKeyVersion: " + branchKeyVersion

    else
      "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                "\n Expected: \n KeyProviderId:" + keyProviderId
    }
}