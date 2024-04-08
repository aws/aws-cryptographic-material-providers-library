// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module ErrorMessages {
  import Types = AwsCryptographyMaterialProvidersTypes
  import UTF8
  import UUID
  import opened Wrappers

    function method {:tailrecursion} INVALID_DATA_KEYS(encryptedDataKeys: Types.EncryptedDataKeyList, errMsg: string)
      : Result<string, Types.Error>
      decreases |encryptedDataKeys|
    {
      if (|encryptedDataKeys| == 0) then
        Success(errMsg)
      else
        var encryptedDataKey := encryptedDataKeys[0];
        :- Need(UTF8.Decode(encryptedDataKey.keyProviderId).Success?, Types.AwsCryptographicMaterialProvidersException(message := "error"));
        :- Need(UTF8.Decode(encryptedDataKey.keyProviderInfo).Success?, Types.AwsCryptographicMaterialProvidersException(message := "error"));
        var extractedKeyProviderId := UTF8.Decode(encryptedDataKey.keyProviderId).Extract();
        if (extractedKeyProviderId == "aws-kms") then
          INVALID_DATA_KEYS(encryptedDataKeys[1..], errMsg + "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                  "\n Expected: \n KeyProviderId:" + extractedKeyProviderId +                            
                                  "\n KeyProviderInfo: " + UTF8.Decode(encryptedDataKey.keyProviderInfo).Extract() + "\n")
          
        else
          INVALID_DATA_KEYS(encryptedDataKeys[1..], errMsg + "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                      "\n Expected: \n KeyProviderId:" + extractedKeyProviderId + "\n")
    }
}