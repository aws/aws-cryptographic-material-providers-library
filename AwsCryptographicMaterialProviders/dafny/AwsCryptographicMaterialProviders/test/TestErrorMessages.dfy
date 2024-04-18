// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/ErrorMessages.dfy"

module TestErrorMessages {
  import Types = AwsCryptographyMaterialProvidersTypes
  import ErrorMessages
  import UTF8
  import AS = AlgorithmSuites

  const TEST_DBE_ALG_SUITE_ID := Types.AlgorithmSuiteId.DBE(Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)

  method {:test} TestIncorrectRawDataKeys()
  {
    var datakey := "0";
    var keyringName := "RSAKeyring";
    var keyProviderId := "TestProvider";
    var actualErrorMessage := ErrorMessages.IncorrectRawDataKeys(datakey, keyringName, keyProviderId);
    var ExpectErrorMessage := "EncryptedDataKey "
    + datakey
    + " did not match" + keyringName + ". "
    + "Expected: keyProviderId: "
    + keyProviderId + ". \n";
    expect actualErrorMessage == ExpectErrorMessage;
  }

  method {:test} TestIncorrectDataKeys()
  {
    var dummyKey : Types.EncryptedDataKeyList := [Types.EncryptedDataKey(
                                                    keyProviderId := UTF8.EncodeAscii("aws-kms") ,
                                                    keyProviderInfo := UTF8.EncodeAscii("keyproviderInfoA"),
                                                    ciphertext := [1, 2, 3, 4, 5]),
                                                  Types.EncryptedDataKey(
                                                    keyProviderId := UTF8.EncodeAscii("aws-kms-rsa") ,
                                                    keyProviderInfo := UTF8.EncodeAscii("keyproviderInfoB"),
                                                    ciphertext := [1, 2, 3, 4, 5])
    ];

    var actualErrorMessage :- expect ErrorMessages.IncorrectDataKeys(dummyKey,AS.GetSuite(TEST_DBE_ALG_SUITE_ID));
    var ExpectErrorMessage := "Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n" +
    "KeyProviderId: aws-kms, KeyProviderInfo: keyproviderInfoA\n" +
    "KeyProviderId: aws-kms-rsa, KeyProviderInfo: keyproviderInfoB\n";
    expect actualErrorMessage == ExpectErrorMessage;
  }


}