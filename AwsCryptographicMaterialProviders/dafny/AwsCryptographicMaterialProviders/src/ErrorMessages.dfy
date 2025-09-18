// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "KeyWrapping/EdkWrapping.dfy"

module ErrorMessages {
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import UTF8
  import UUID
  import opened Wrappers
  import EdkWrapping

  const SALT_LENGTH := 16 as uint64
  const IV_LENGTH := 12 as uint64
  const VERSION_LENGTH := 16 as uint64

  const KMS_ECDH_DISCOVERY_ENCRYPT_ERROR := "KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt."
  const RAW_ECDH_DISCOVERY_ENCRYPT_ERROR := "PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt."
  const RAW_ECDH_EPHEMERAL_DECRYPT_ERROR := "EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt."

  function method IncorrectRawDataKeys(datakey: string, keyringName: string, keyProviderId: string)
    : string
  {
    "EncryptedDataKey "
    + datakey
    + " did not match " + keyringName + ". "
    + "Expected: keyProviderId: "
    + keyProviderId + ".\n"
  }

  function method {:opaque} IncorrectDataKeys(encryptedDataKeys: Types.EncryptedDataKeyList, material : Types.AlgorithmSuiteInfo,errMsg: string := "")
    : Result<string, Types.Error>
  {
    var expectedValue :- IncorrectDataKeysExpectedValues(encryptedDataKeys, material, errMsg);
    Success("Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n" + expectedValue)
  }

  function method {:tailrecursion} {:opaque} IncorrectDataKeysExpectedValues(encryptedDataKeys: Types.EncryptedDataKeyList, material : Types.AlgorithmSuiteInfo, errMsg: string := "")
    : Result<string, Types.Error>
    decreases |encryptedDataKeys|
  {
    SequenceIsSafeBecauseItIsInMemory(encryptedDataKeys);
    if (|encryptedDataKeys| as uint64 == 0) then
      Success(errMsg)
    else
      var encryptedDataKey := encryptedDataKeys[0 as uint32];
      var extractedKeyProviderId :- UTF8.Decode(encryptedDataKey.keyProviderId).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := e ));
      var extractedKeyProviderInfo :- UTF8.Decode(encryptedDataKey.keyProviderInfo).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := e ));
      if (extractedKeyProviderId != "aws-kms-hierarchy") then
        IncorrectDataKeysExpectedValues(encryptedDataKeys[1 as uint32..], material, errMsg +
                                        "KeyProviderId: " + extractedKeyProviderId +
                                        ", KeyProviderInfo: " + extractedKeyProviderInfo + "\n")
      else
        var providerWrappedMaterial :- EdkWrapping.GetProviderWrappedMaterial(encryptedDataKey.ciphertext, material);
        SequenceIsSafeBecauseItIsInMemory(providerWrappedMaterial);
        var EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX := SALT_LENGTH + IV_LENGTH;
        var EDK_CIPHERTEXT_VERSION_INDEX := EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX + VERSION_LENGTH;
        :- Need(EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX < EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Wrong branch key version index."));
        :- Need(|providerWrappedMaterial| as uint64 >= EDK_CIPHERTEXT_VERSION_INDEX, Types.AwsCryptographicMaterialProvidersException(message := "Incorrect ciphertext structure."));
        var branchKeyVersionUuid := providerWrappedMaterial[EDK_CIPHERTEXT_BRANCH_KEY_VERSION_INDEX .. EDK_CIPHERTEXT_VERSION_INDEX];
        var branchVersion :- UUID.FromByteArray(branchKeyVersionUuid).MapFailure(e => Types.AwsCryptographicMaterialProvidersException( message := e ));
        IncorrectDataKeysExpectedValues(encryptedDataKeys[1 as uint32..], material, errMsg +
                                        "KeyProviderId: " + extractedKeyProviderId +
                                        ", KeyProviderInfo: " + extractedKeyProviderInfo +
                                        ", BranchKeyVersion: " + branchVersion + "\n")
  }
}