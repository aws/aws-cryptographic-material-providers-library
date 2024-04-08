// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module ErrorMessages {
  import Types = AwsCryptographyMaterialProvidersTypes
  import UTF8
  import UUID
  import opened Wrappers

    method INVALID_DATA_KEYS(encryptedDataKeys: Types.EncryptedDataKeyList)
      returns ( output: Result<string, Types.Error>)
      requires |encryptedDataKeys| > 0
    {
      var errMsg := "";
      for i := 0 to |encryptedDataKeys|
      {
        :- Need(UTF8.Decode(encryptedDataKeys[i].keyProviderId).Success?,
              Types.AwsCryptographicMaterialProvidersException(
                message := "Cannot decode keyProviderId information"
              ));
        :- Need(UTF8.Decode(encryptedDataKeys[i].keyProviderInfo).Success?,
              Types.AwsCryptographicMaterialProvidersException(
                message := "Cannot decode keyProviderId information"
              ));
        var extractedKeyProviderId : string := UTF8.Decode(encryptedDataKeys[i].keyProviderId).Extract();
        if extractedKeyProviderId == "aws-kms"{
          errMsg := "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                "\n Expected: \n KeyProviderId:" + extractedKeyProviderId +                            
                                "\n KeyProviderInfo: " + UTF8.Decode(encryptedDataKeys[i].keyProviderInfo).Extract();
        }
        // else if extractedKeyProviderId == "aws-kms-hierarchy"{
        //   errMsg := "Unable to decrypt data key: No Encrypted Data Keys found to match." +
        //                             "\n Expected: \n KeyProviderId:" + extractedKeyProviderId +                            
        //                             "\n KeyProviderInfo: " + UTF8.Decode(encryptedDataKeys[i].keyProviderInfo).Extract() +
        //                             "\n BranchKeyVersion: " + UUID.FromByteArray(branchKeyVersionUuid).Extract();
        // }
        else{
          errMsg := "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                    "\n Expected: \n KeyProviderId:" + extractedKeyProviderId;
        }
      }
      output := Success(errMsg);
    }
}