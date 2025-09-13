// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"

module TestComAmazonawsKms {
  import Com.Amazonaws.Kms
  import opened StandardLibrary.UInt
  import opened Wrappers

  // Does not have GenerateDataKeyWithoutPlaintext permission
  const keyId :=  "arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"
  // No Permissions to call GenerateDataKeyWithoutPlaintext, set on KeyPolicy, not IAM
  const failingKeyId := "arn:aws:kms:us-west-2:370957321024:key/e20ac7b8-3d95-46ee-b3d5-f5dca6393945"
  // From Keystore's Test Fixtures
  const keyIdGenerateWOPlain := "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126"

  // ECC Curve P256 Keys
  const senderKmsKey := "arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9"
  const recipientKmsKey := "arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5"

  // ECC Curve P384
  const incorrectEccCurveKey := "arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e"

  // One test depends on knowing the region it is being run it.
  // For now, hardcode this value to the region we are currently using to test,
  // which is the same region that our test KMS Key lives in.
  // If we want to run tests in other regions we will need a way to
  // grab this value from some config.
  // For now, we prefer to have brittleness in these tests vs. missing a test case
  // that cannot be formally verified.
  const TEST_REGION := "us-west-2"

  // This is required because
  // https://github.com/dafny-lang/dafny/issues/2311
  function method workAround(literal: seq<uint8>)
    :(ret: Kms.Types.CiphertextType)
    requires Kms.Types.IsValid_CiphertextType(literal)
  {literal}

  // These are the operations needed for the Encryption SDK
  method {:test} BasicDecryptTests() {
    var CiphertextBlob : seq<uint8> := [
      1,   1,   1,   0, 120,  64, 243, 140,  39,  94,  49,   9,
      116,  22, 193,   7,  41,  81,  80,  87,  25, 100, 173, 163,
      239,  28,  33, 233,  76, 139, 160, 189, 188, 157,  15, 180,
      20,   0,   0,   0,  98,  48,  96,   6,   9,  42, 134,  72,
      134, 247,  13,   1,   7,   6, 160,  83,  48,  81,   2,   1,
      0,  48,  76,   6,   9,  42, 134,  72, 134, 247,  13,   1,
      7,   1,  48,  30,   6,   9,  96, 134,  72,   1, 101,   3,
      4,   1,  46,  48,  17,   4,  12, 196, 249,  60,   7,  21,
      231,  87,  70, 216,  12,  31,  13,   2,   1,  16, 128,  31,
      222, 119, 162, 112,  88, 153,  39, 197,  21, 182, 116, 176,
      120, 174, 107,  82, 182, 223, 160, 201,  15,  29,   3, 254,
      3, 208,  72, 171,  64, 207, 175
    ];

    BasicDecryptTest(
      input := Kms.Types.DecryptRequest(
        CiphertextBlob := workAround(CiphertextBlob),
        EncryptionContext := Kms.Wrappers.None,
        GrantTokens := Kms.Wrappers.None,
        KeyId := Kms.Wrappers.Some(keyId),
        EncryptionAlgorithm := Kms.Wrappers.None
      ),
      expectedPlaintext := [ 165, 191, 67, 62 ],
      expectedKeyId := keyId
    );
  }

  method {:test} BasicGenerateTests() {
    BasicGenerateTest(
      input := Kms.Types.GenerateDataKeyRequest(
        KeyId := keyId,
        EncryptionContext := Kms.Wrappers.None,
        NumberOfBytes := Kms.Wrappers.Some(32 as Kms.Types.NumberOfBytesType),
        KeySpec := Kms.Wrappers.None,
        GrantTokens := Kms.Wrappers.None
      )
    );
  }

  method {:test} BasicGenerateWithoutPlaintextTests() {
    BasicGenerateWithoutPlaintextTest(
      input := Kms.Types.GenerateDataKeyWithoutPlaintextRequest(
        KeyId := keyIdGenerateWOPlain,
        EncryptionContext := Kms.Wrappers.None,
        NumberOfBytes := Kms.Wrappers.Some(32 as Kms.Types.NumberOfBytesType),
        KeySpec := Kms.Wrappers.None,
        GrantTokens := Kms.Wrappers.None
      )
    );
  }

  method {:test} BasicEncryptTests() {
    BasicEncryptTest(
      input := Kms.Types.EncryptRequest(
        KeyId := keyId,
        // The string "asdf" as bytes
        Plaintext := [ 97, 115, 100, 102 ],
        EncryptionContext := Kms.Wrappers.None,
        GrantTokens := Kms.Wrappers.None,
        EncryptionAlgorithm := Kms.Wrappers.None
      )
    );
  }

  const failingInput := Kms.Types.GenerateDataKeyWithoutPlaintextRequest(
                          KeyId := failingKeyId,
                          EncryptionContext := Kms.Wrappers.None,
                          NumberOfBytes := Kms.Wrappers.Some(32 as Kms.Types.NumberOfBytesType),
                          KeySpec := Kms.Wrappers.None,
                          GrantTokens := Kms.Wrappers.None
                        )

  method {:test} BasicFailTests() {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);
    var ret := client.GenerateDataKeyWithoutPlaintext(failingInput);
    expect ret.Failure?;
    var err: Kms.Types.Error := ret.error;
    expect err.OpaqueWithText?;
    match err {
      case OpaqueWithText(obj, objMessage) => expect true;
      case _ => expect false, "Failing KMS Key MUST cause an OpaqueError that can later be unwrapped to a proper but generic KMS Exception.";
    }
  }

  method BasicDecryptTest(
    nameonly input: Kms.Types.DecryptRequest,
    nameonly expectedPlaintext: Kms.Types.PlaintextType,
    nameonly expectedKeyId: Kms.Types.KeyIdType
  )
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);

    var ret := client.Decrypt(input);

    // print ret;

    expect(ret.Success?);

    var DecryptResponse(KeyId, Plaintext, EncryptionAlgorithm, CiphertextBlob) := ret.value;

    expect Plaintext.Some?;
    expect KeyId.Some?;
    expect Plaintext.value == expectedPlaintext;
    expect KeyId.value == expectedKeyId;
  }

  method BasicGenerateTest(
    nameonly input: Kms.Types.GenerateDataKeyRequest
  )
    requires input.NumberOfBytes.Some?
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);

    var ret := client.GenerateDataKey(input);

    expect(ret.Success?);

    var GenerateDataKeyResponse(CiphertextBlob, Plaintext, KeyId, CiphertextForRecipient) := ret.value;

    expect CiphertextBlob.Some?;
    expect Plaintext.Some?;
    expect KeyId.Some?;
    expect |Plaintext.value| == input.NumberOfBytes.value as nat;

    var decryptInput := Kms.Types.DecryptRequest(
      CiphertextBlob := CiphertextBlob.value,
      EncryptionContext := input.EncryptionContext,
      GrantTokens := input.GrantTokens,
      KeyId := Kms.Wrappers.Some(KeyId.value),
      EncryptionAlgorithm := Kms.Wrappers.None
    );

    BasicDecryptTest(
      input := decryptInput,
      expectedPlaintext := Plaintext.value,
      expectedKeyId := input.KeyId
    );
  }

  method BasicGenerateWithoutPlaintextTest(
    nameonly input: Kms.Types.GenerateDataKeyWithoutPlaintextRequest
  )
    requires input.NumberOfBytes.Some?
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);

    var retGenerate := client.GenerateDataKeyWithoutPlaintext(input);
    // print retGenerate;
    expect(retGenerate.Success?);

    var GenerateDataKeyWithoutPlaintextResponse(CiphertextBlob, KeyId) := retGenerate.value;

    expect CiphertextBlob.Some?;
    expect KeyId.Some?;

    var decryptInput := Kms.Types.DecryptRequest(
      CiphertextBlob := CiphertextBlob.value,
      EncryptionContext := input.EncryptionContext,
      GrantTokens := input.GrantTokens,
      KeyId := Kms.Wrappers.Some(KeyId.value),
      EncryptionAlgorithm := Kms.Wrappers.None
    );

    var ret := client.Decrypt(decryptInput);
    expect(ret.Success?);
    var DecryptResponse(KeyIdTwo, Plaintext, EncryptionAlgorithm, CiphertextBlobTwo) := ret.value;

    expect KeyIdTwo.Some?;
    expect KeyIdTwo.value == KeyId.value;
  }

  method BasicEncryptTest(
    nameonly input: Kms.Types.EncryptRequest
  )
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);

    var ret := client.Encrypt(input);

    expect(ret.Success?);

    var EncryptResponse(CiphertextBlob, KeyId, EncryptionAlgorithm) := ret.value;

    expect CiphertextBlob.Some?;
    expect KeyId.Some?;

    var decryptInput := Kms.Types.DecryptRequest(
      CiphertextBlob := CiphertextBlob.value,
      EncryptionContext := input.EncryptionContext,
      GrantTokens := input.GrantTokens,
      KeyId := Kms.Wrappers.Some(KeyId.value),
      EncryptionAlgorithm := input.EncryptionAlgorithm
    );

    BasicDecryptTest(
      input := decryptInput,
      expectedPlaintext := input.Plaintext,
      expectedKeyId := input.KeyId
    );
  }

  // While we cannot easily test that the expected implementations
  // return Some(), we can at least ensure that the ones that do are correct.
  method {:test} RegionMatchTest() {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);
    var region := Kms.RegionMatch(client, TEST_REGION);
    expect region.None? || region.value;
  }

  // This should default to whatever default SDK uses.
  method {:test} EmptyStringIsDefaultRegion() {
    var client :- expect Kms.KMSClientForRegion("");
  }

  method BasicDeriveSharedSecretTests(
    nameonly input: Kms.Types.DeriveSharedSecretRequest
  )
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);

    var ret := client.DeriveSharedSecret(
      Kms.Types.DeriveSharedSecretRequest(
        KeyId := input.KeyId,
        KeyAgreementAlgorithm := input.KeyAgreementAlgorithm,
        PublicKey := input.PublicKey
      )
    );

    if ret.Success? {
      var DeriveSharedSecretResponse(KeyId, SharedSecret, CiphertextForRecipient, KeyAgreementAlgorithm, KeyOrigin ) := ret.value;

      expect (SharedSecret.Some?);
      expect (KeyId.Some?);

      expect KeyId.value == input.KeyId;

    } else {
      expect (ret.Failure?);
      // print ret.error;
    }

  }

  method GetPublicKeyHelper(
    nameonly input: Kms.Types.GetPublicKeyRequest
  )
    returns (publicKey: Kms.Types.PublicKeyType)
  {
    var client :- expect Kms.KMSClientForRegion(TEST_REGION);
    var ret := client.GetPublicKey(
      Kms.Types.GetPublicKeyRequest(
        KeyId := input.KeyId,
        GrantTokens := input.GrantTokens
      )
    );
    expect(ret.Success?);

    var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := ret.value;
    expect PublicKey.Some?;

    return PublicKey.value;
  }

  method {:test} DeriveSharedSecretTestSuccess() {
    var recipientPublicKey := GetPublicKeyHelper(
      input := Kms.Types.GetPublicKeyRequest(
        KeyId := recipientKmsKey,
        GrantTokens := Kms.Wrappers.None
      )
    );

    BasicDeriveSharedSecretTests(
      input := Kms.Types.DeriveSharedSecretRequest(
        KeyId := senderKmsKey,
        KeyAgreementAlgorithm := Kms.Types.KeyAgreementAlgorithmSpec.ECDH,
        PublicKey := recipientPublicKey
      )
    );
  }

  method {:test} DeriveSharedSecretTestFailure() {
    var recipientPublicKeyOnWrongCurve := GetPublicKeyHelper(
      input := Kms.Types.GetPublicKeyRequest(
        KeyId := incorrectEccCurveKey,
        GrantTokens := Kms.Wrappers.None
      )
    );

    BasicDeriveSharedSecretTests(
      input := Kms.Types.DeriveSharedSecretRequest(
        KeyId := senderKmsKey,
        KeyAgreementAlgorithm := Kms.Types.KeyAgreementAlgorithmSpec.ECDH,
        PublicKey := recipientPublicKeyOnWrongCurve
      )
    );
  }

  // Methods for the benefit of Java tests that need to call Dafny-generated code.

  function method CreateNoneForEncryptionContext(): Option<Kms.Types.EncryptionContextType> {
    None
  }
  function method CreateNoneForKeySpec(): Option<Kms.Types.DataKeySpec> {
    None
  }
  function method CreateNoneForNumberOfBytes(): Option<Kms.Types.NumberOfBytesType> {
    None
  }
  function method CreateNoneForGrantTokens(): Option<Kms.Types.GrantTokenList> {
    None
  }
  function method CreateNoneForDryRun(): Option<bool> {
    None
  }
}
