// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "KeyWrapping/EdkWrapping.dfy"

module ErrorMessages {
  import Types = AwsCryptographyMaterialProvidersTypes
  import UTF8
  import UUID
  import opened Wrappers
  import EdkWrapping

  function method {:tailrecursion} INVALID_DATA_KEYS(encryptedDataKeys: Types.EncryptedDataKeyList, errMsg: string := "", material : Option<Types.DecryptionMaterials> := None)
    : Result<string, Types.Error>
    decreases |encryptedDataKeys|
  {
    if (|encryptedDataKeys| == 0) then
      Success(errMsg)
    else
      var encryptedDataKey := encryptedDataKeys[0];
      :- Need(UTF8.Decode(encryptedDataKey.keyProviderId).Success?, Types.AwsCryptographicMaterialProvidersException(message := "Failed to get keyProviderId"));
      :- Need(UTF8.Decode(encryptedDataKey.keyProviderInfo).Success?, Types.AwsCryptographicMaterialProvidersException(message := "Failed to get keyProviderInfo"));
      var extractedKeyProviderId := UTF8.Decode(encryptedDataKey.keyProviderId).Extract();
      if (extractedKeyProviderId == "aws-kms") then
        INVALID_DATA_KEYS(encryptedDataKeys[1..], errMsg + "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                "\n Expected: \n KeyProviderId:" + extractedKeyProviderId +                            
                                "\n KeyProviderInfo: " + UTF8.Decode(encryptedDataKey.keyProviderInfo).Extract() + "\n")
      else if extractedKeyProviderId == "aws-kms-hierarchy" then
        :- Need(material.Some?, Types.AwsCryptographicMaterialProvidersException(message := "Material not found to generate INVALID_DATA_KEYS exception."));
        :- Need(EdkWrapping.GetProviderWrappedMaterial(encryptedDataKey.ciphertext, material.Extract().algorithmSuite).Success?, Types.AwsCryptographicMaterialProvidersException(message := "GetProviderWrappedMaterial failed in INVALID_DATA_KEYS exception."));
        var providerWrappedMaterial := EdkWrapping.GetProviderWrappedMaterial(encryptedDataKey.ciphertext, material.Extract().algorithmSuite).Extract();
        var EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX := 12 + 16;
        var EDK_CIPHERTEXT_VERSION_INDEX := EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX + 16;

        :- Need(EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX < EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Wrong branch key version index."));
        :- Need(|providerWrappedMaterial| >= EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Incorrect ciphertext structure length."));
        var branchKeyVersionUuid := providerWrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX .. EDK_CIPHERTEXT_VERSION_INDEX];
        :- Need(UUID.FromByteArray(branchKeyVersionUuid).Success?, Types.AwsCryptographicMaterialProvidersException(message := "GetProviderWrappedMaterial failed in INVALID_DATA_KEYS exception."));
        INVALID_DATA_KEYS(encryptedDataKeys[1..], errMsg + "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                "\n Expected: \n KeyProviderId:" + extractedKeyProviderId +                            
                                "\n KeyProviderInfo: " + UTF8.Decode(encryptedDataKey.keyProviderInfo).Extract() + 
                                "\n BranchKeyVersion: " + UUID.FromByteArray(branchKeyVersionUuid).Extract())
      else
        INVALID_DATA_KEYS(encryptedDataKeys[1..], errMsg + "Unable to decrypt data key: No Encrypted Data Keys found to match." +
                                    "\n Expected: \n KeyProviderId:" + extractedKeyProviderId + "\n")
  }
}