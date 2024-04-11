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

  const SALT_LENGTH := 16
  const IV_LENGTH := 12
  const VERSION_LENGTH := 16

  function method INVALID_RAW_DATA_KEYS_ERROR(datakey: string, keyringName: string, keyProviderId: string)
    : string
  {
    "EncryptedDataKey "
      + datakey
      + " did not match" + keyringName + ". " 
      + "Expected: keyProviderId: "
      + keyProviderId + "."
  }

  function method INVALID_DATA_KEYS(encryptedDataKeys: Types.EncryptedDataKeyList, material : Types.DecryptionMaterials,errMsg: string := "")
    : Result<string, Types.Error> 
  {
    var expectedValue :- INVALID_DATA_KEYS_EXPECTED_VALUES(encryptedDataKeys, material, errMsg).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := "Getting invalid data keys expected value failed." ));
    Success("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n" + expectedValue)
  }

  function method {:tailrecursion} INVALID_DATA_KEYS_EXPECTED_VALUES(encryptedDataKeys: Types.EncryptedDataKeyList, material : Types.DecryptionMaterials,errMsg: string := "")
    : Result<string, Types.Error>
    decreases |encryptedDataKeys|
  {
    if (|encryptedDataKeys| == 0) then
      Success(errMsg)
    else
      var encryptedDataKey := encryptedDataKeys[0];
      var extractedKeyProviderId :- UTF8.Decode(encryptedDataKey.keyProviderId).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := e ));
      var extractedKeyProviderInfo :- UTF8.Decode(encryptedDataKey.keyProviderInfo).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := e ));
      if (extractedKeyProviderId == "aws-kms") then
        INVALID_DATA_KEYS_EXPECTED_VALUES(encryptedDataKeys[1..], material,errMsg +
                                "KeyProviderId: " + extractedKeyProviderId +                            
                                ", KeyProviderInfo: " + extractedKeyProviderInfo + "\n")
      else
        var providerWrappedMaterial :- EdkWrapping.GetProviderWrappedMaterial(encryptedDataKey.ciphertext, material.algorithmSuite).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := "Failed to get provider wrapped material" ));
        var EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX := SALT_LENGTH + IV_LENGTH;
        var EDK_CIPHERTEXT_VERSION_INDEX := EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX + VERSION_LENGTH;
        :- Need(EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX < EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Wrong branch key version index."));
        :- Need(|providerWrappedMaterial| >= EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Incorrect ciphertext structure length."));
        var branchKeyVersionUuid := providerWrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX .. EDK_CIPHERTEXT_VERSION_INDEX];
        var branchVersion :- UUID.FromByteArray(branchKeyVersionUuid).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := "Failed to get provider wrapped material" ));
        INVALID_DATA_KEYS_EXPECTED_VALUES(encryptedDataKeys[1..], material, errMsg + 
                                "KeyProviderId: " + extractedKeyProviderId +                            
                                ", KeyProviderInfo: " + extractedKeyProviderInfo + 
                                ", BranchKeyVersion: " + branchVersion + "\n")
  }
}