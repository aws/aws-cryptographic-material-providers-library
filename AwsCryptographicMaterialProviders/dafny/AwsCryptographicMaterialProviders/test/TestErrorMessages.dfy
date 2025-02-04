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
    var ExpectErrorMessage := "EncryptedDataKey 0 did not match RSAKeyring. Expected: keyProviderId: TestProvider.\n";
    expect actualErrorMessage == ExpectErrorMessage;
  }

const awskms : UTF8.ValidUTF8Bytes := 
  var s := [0x61, 0x77, 0x73, 0x2d, 0x6b, 0x6d, 0x73];
  assert s == UTF8.EncodeAscii("aws-kms");
  s

const keyproviderInfoA : UTF8.ValidUTF8Bytes := 
  var s := [0x6b, 0x65, 0x79, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x49, 0x6e, 0x66, 0x6f, 0x41];
  assert s == UTF8.EncodeAscii("keyproviderInfoA");
  s

const keyproviderInfoB : UTF8.ValidUTF8Bytes := 
  var s := [0x6b, 0x65, 0x79, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x49, 0x6e, 0x66, 0x6f, 0x42];
  assert s == UTF8.EncodeAscii("keyproviderInfoB");
  s

const keyproviderInfoC : UTF8.ValidUTF8Bytes := 
  var s := [0x6b, 0x65, 0x79, 0x70, 0x72, 0x6f, 0x76, 0x69, 0x64, 0x65, 0x72, 0x49, 0x6e, 0x66, 0x6f, 0x43];
  assert s == UTF8.EncodeAscii("keyproviderInfoC");
  s

const awskmsrsa : UTF8.ValidUTF8Bytes := 
  var s := [0x61, 0x77, 0x73, 0x2d, 0x6b, 0x6d, 0x73, 0x2d, 0x72, 0x73, 0x61];
  assert s == UTF8.EncodeAscii("aws-kms-rsa");
  s

const awskmshierarchy : UTF8.ValidUTF8Bytes := 
  var s := [0x61, 0x77, 0x73, 0x2d, 0x6b, 0x6d, 0x73, 0x2d, 0x68, 0x69, 0x65, 0x72, 0x61, 0x72, 0x63, 0x68, 0x79];
  assert s == UTF8.EncodeAscii("aws-kms-hierarchy");
  s


  method {:test} TestIncorrectDataKeys()
  {
    var dummyKey : Types.EncryptedDataKeyList := [Types.EncryptedDataKey(
                                                    keyProviderId := awskms,
                                                    keyProviderInfo := keyproviderInfoA,
                                                    ciphertext := [1, 2, 3, 4, 5]),
                                                  Types.EncryptedDataKey(
                                                    keyProviderId := awskmsrsa,
                                                    keyProviderInfo := keyproviderInfoB,
                                                    ciphertext := [1, 2, 3, 4, 5]),
                                                  Types.EncryptedDataKey(
                                                    keyProviderId := awskmshierarchy,
                                                    keyProviderInfo := keyproviderInfoC,
                                                    ciphertext := [
                                                      64, 92, 115, 7, 85, 121, 112, 79, 69, 12, 82, 25, 67, 34,
                                                      11, 66, 93, 45, 40, 23, 90, 61, 16, 28, 59, 114, 52, 122,
                                                      50, 23, 11, 101, 48, 53, 30, 120, 51, 74, 77, 53, 57, 99,
                                                      53, 13, 30, 21, 109, 85, 15, 86, 47, 84, 91, 85, 87, 60, 4,
                                                      56, 67, 74, 29, 87, 85, 106, 8, 82, 63, 114, 100, 110, 68,
                                                      58, 83, 24, 111, 41, 21, 91, 122, 61, 118, 37, 72, 38, 67, 2,
                                                      17, 61, 17, 121, 7, 90, 117, 49, 30, 20, 89, 68, 33, 111,
                                                      107, 5, 120, 20, 95, 78, 70, 2, 49, 84, 39, 50, 40, 40, 115,
                                                      114, 76, 18, 103, 84, 34, 123, 1, 125, 61, 33, 13, 18, 81,
                                                      24, 53, 53, 26, 60, 52, 85, 81, 96, 85, 72])
    ];

    var actualErrorMessage :- expect ErrorMessages.IncorrectDataKeys(dummyKey,AS.GetSuite(TEST_DBE_ALG_SUITE_ID));
    var ExpectErrorMessage := "Unable to decrypt data key: No Encrypted Data Keys found to match. \n Expected: \n" +
    "KeyProviderId: aws-kms, KeyProviderInfo: keyproviderInfoA\n" +
    "KeyProviderId: aws-kms-rsa, KeyProviderInfo: keyproviderInfoB\n" +
    "KeyProviderId: aws-kms-hierarchy, KeyProviderInfo: keyproviderInfoC, BranchKeyVersion: 155b7a3d-7625-4826-4302-113d1179075a\n";
    expect actualErrorMessage == ExpectErrorMessage;
  }


}
