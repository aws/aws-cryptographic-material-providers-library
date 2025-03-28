// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

module {:options "/functionSyntax:4" } MutateViaDecryptEncrypt {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened Seq

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import KMSKeystoreOperations

  // TODO-HV-2-M2: Refactor/Remove to use KMSKeyStoreOperations.DecryptKey
  method Decrypt(
    ciphertext: seq<uint8>,
    encryptionContext: Structure.BranchKeyContext,
    kmsArn: string,
    grantTokens: KMSKeystoreOperations.KMS.GrantTokenList,
    kmsClient: KMSKeystoreOperations.KMS.IKMSClient
  ) returns (res: Result<KMSKeystoreOperations.KMS.PlaintextType, KMSKeystoreOperations.KmsError>)
    requires Structure.BranchKeyContext?(encryptionContext)
    requires KMSKeystoreOperations.KmsArn.ValidKmsArn?(kmsArn)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures
      res.Success?
      ==>
        && KMSKeystoreOperations.KMS.IsValid_CiphertextType(ciphertext)
        && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
        && var decryptInput := Seq.Last(kmsClient.History.Decrypt).input;
        && var decryptOutput := Seq.Last(kmsClient.History.Decrypt).output;
        && KMSKeystoreOperations.KMS.DecryptRequest(
             CiphertextBlob := ciphertext,
             EncryptionContext := Some(encryptionContext),
             GrantTokens := Some(grantTokens),
             KeyId := Some(kmsArn)
           ) == decryptInput
        && decryptOutput.Success? && decryptOutput.value.Plaintext.Some? && decryptOutput.value.KeyId.Some?
        && decryptOutput.value.KeyId.value == kmsArn
        && res.value == decryptOutput.value.Plaintext.value
  {
    :- Need(
      KMSKeystoreOperations.KMS.IsValid_CiphertextType(ciphertext),
      KMSKeystoreOperations.Types.KeyManagementException(
        message := "The Branch Key's `enc` or ciphertext field is invalid."
        + " Something must have tampered with the stored item, or the read was bad.")
    );

    var kmsDecryptRequest := KMSKeystoreOperations.KMS.DecryptRequest(
      CiphertextBlob := ciphertext,
      EncryptionContext := Some(encryptionContext),
      GrantTokens := Some(grantTokens),
      KeyId := Some(kmsArn)
    );

    var decryptResponse? := kmsClient.Decrypt(kmsDecryptRequest);
    var decryptResponse :- decryptResponse?
    .MapFailure(e => KMSKeystoreOperations.Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && decryptResponse.KeyId.Some?
      && decryptResponse.KeyId.value == kmsArn,
      KMSKeystoreOperations.Types.KeyManagementException(
        message := "Invalid response from AWS KMS Decrypt: KMS Key ID of response did not match request."
      ));
    :- Need(
      && decryptResponse.Plaintext.Some?
      && KMSKeystoreOperations.KMS.IsValid_PlaintextType(decryptResponse.Plaintext.value),
      KMSKeystoreOperations.Types.KeyManagementException(
        message := "Invalid response from AWS KMS Decrypt: KMS response did not include plaintext."
      ));
    return Success(decryptResponse.Plaintext.value);
  }

  // TODO-HV-2-M2: Refactor/Remove to use KMSKeyStoreOperations.EncryptKey
  method Encrypt(
    plaintext: KMSKeystoreOperations.KMS.PlaintextType,
    encryptionContext: Structure.BranchKeyContext,
    kmsArn: string,
    grantTokens: KMSKeystoreOperations.KMS.GrantTokenList,
    kmsClient: KMSKeystoreOperations.KMS.IKMSClient
  ) returns (res: Result<KMSKeystoreOperations.KMS.CiphertextType, KMSKeystoreOperations.KmsError>)
    requires Structure.BranchKeyContext?(encryptionContext)
    requires KMSKeystoreOperations.KmsArn.ValidKmsArn?(kmsArn)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()
    ensures
      res.Success?
      ==>
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
        && var encryptInput := Seq.Last(kmsClient.History.Encrypt).input;
        && var encryptResponse := Seq.Last(kmsClient.History.Encrypt).output;
        && KMSKeystoreOperations.KMS.EncryptRequest(
             KeyId := kmsArn,
             Plaintext := plaintext,
             EncryptionContext := Some(encryptionContext),
             GrantTokens := Some(grantTokens)
           ) == encryptInput
        && encryptResponse.Success?
        && encryptResponse.value.CiphertextBlob.Some?
        && encryptResponse.value.KeyId.Some?
        && encryptResponse.value.KeyId.value == kmsArn
        && KMSKeystoreOperations.KMS.IsValid_CiphertextType(encryptResponse.value.CiphertextBlob.value)
        && encryptResponse.value.CiphertextBlob.value == res.value
  {
    var kmsEncryptRequest := KMSKeystoreOperations.KMS.EncryptRequest(
      KeyId := kmsArn,
      Plaintext := plaintext,
      EncryptionContext := Some(encryptionContext),
      GrantTokens := Some(grantTokens)
    );

    var encryptResponse? := kmsClient.Encrypt(kmsEncryptRequest);
    var encryptResponse :- encryptResponse?
    .MapFailure(e => KMSKeystoreOperations.Types.ComAmazonawsKms(ComAmazonawsKms := e));

    :- Need(
      && encryptResponse.CiphertextBlob.Some?
      && KMSKeystoreOperations.KMS.IsValid_CiphertextType(encryptResponse.CiphertextBlob.value),
      KMSKeystoreOperations.Types.KeyManagementException(
        message := "Invalid response from AWS KMS Encrypt: KMS response's Ciphertext is invalid."
      )
    );
    :- Need(
      && encryptResponse.KeyId.Some?
      && encryptResponse.KeyId.value == kmsArn,
      KMSKeystoreOperations.Types.KeyManagementException(
        message := "Invalid response from AWS KMS Encrypt: KMS Key ID of response did not match request."
      )
    );
    return Success(encryptResponse.CiphertextBlob.value);
  }
}
