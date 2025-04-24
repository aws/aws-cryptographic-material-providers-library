// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "KmsArn.dfy"

module {:options "/functionSyntax:4" } KmsUtils {
  import opened Wrappers
  import KMS = Com.Amazonaws.Kms
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KmsArn

  datatype KMSTuple = | KMSTuple(
    kmsClient: KMS.Types.IKMSClient,
    grantTokens: KMS.Types.GrantTokenList)
  {
    ghost predicate ValidState()
    {
      && kmsClient.ValidState()
      && kmsClient.Modifies == kmsClient.Modifies
      && KMS.Types.IsValid_GrantTokenList(grantTokens)
    }
    ghost const Modifies := kmsClient.Modifies
  }

  datatype keyManagerStrat =
    | reEncrypt(reEncrypt: KMSTuple)
    | decryptEncrypt(decrypt: KMSTuple, encrypt: KMSTuple)
    | kmsSimple(kmsSimple: KMSTuple)
  {
    ghost predicate ValidState()
    {
      match this
      case decryptEncrypt(kmD, kmE) =>
        // We will assume this is the case in order to make verification happy
        && kmD.ValidState()
        && kmE.ValidState()
        && kmD.Modifies == kmD.Modifies
        && kmE.Modifies == kmE.Modifies
        && kmD.Modifies !! kmE.Modifies
      // TODO : Check with Dafny team about collapsing reEncrypt & kmsSimple
      case reEncrypt(km) => km.ValidState() && km.Modifies == km.Modifies
      case kmsSimple(km) => km.ValidState() && km.Modifies == km.Modifies
    }
    ghost const Modifies := match this
      case decryptEncrypt(kmD, kmE) => kmD.Modifies + kmE.Modifies
      case reEncrypt(km) => km.Modifies
      case kmsSimple(km) => km.Modifies
    ghost const ModifiesMultiSet := match this
      case decryptEncrypt(kmD, kmE) => multiset(kmD.kmsClient.Modifies) + multiset(kmE.kmsClient.Modifies)
      case reEncrypt(km) => multiset(km.kmsClient.Modifies)
      case kmsSimple(km) => multiset(km.kmsClient.Modifies)

    // TODO-HV-2-M2 :: work out complete support
    predicate SupportHV1()
    {
      match this
      case decryptEncrypt(kmD, kmE) => true
      case reEncrypt(km) => true
      case kmsSimple(km) => false
    }
    predicate SupportHV2()
    {
      match this
      case decryptEncrypt(kmD, kmE) => true
      case reEncrypt(km) => false
      case kmsSimple(km) => true
    }
  }



  predicate IsSupportedKeyManagerStrategy(
    terminalHierarchyVersion: KeyStoreTypes.HierarchyVersion,
    keyManagerStrategy: keyManagerStrat
  )
  {
    match terminalHierarchyVersion {
      case v1 => keyManagerStrategy.SupportHV1()
      case v2 => keyManagerStrategy.SupportHV2()
    }
  }

  /**
    * Extracts the KMSTuple (KMS client and grant tokens) from keyManagerStrat.
    * The KMSTuple might not just be for decryption but can also be used for other operations.
    * 
    * The function handles three different key manager strategy patterns:
    * - reEncrypt: Only has one kms client and grant tokens
    * - decryptEncrypt: Uses separate KMS clients for decryption and encryption (returns the decrypt client)
    * - kmsSimple: Only has one kms client and grant tokens
    * 
    * @param keyManagerStrategy The strategy pattern that defines which KMS clients to use
    * @returns A KMSTuple containing KMS client and grant tokens extracted from keyManagerStrat
    */
  function getDecryptKMSTuple(
    keyManagerStrategy: keyManagerStrat
  ) : (output: KMSTuple)
  {
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        KMSTuple(kms.kmsClient, kms.grantTokens)
      case decryptEncrypt(kmsD, kmsE) =>
        KMSTuple(kmsD.kmsClient, kmsD.grantTokens)
      case kmsSimple(kms) =>
        KMSTuple(kms.kmsClient, kms.grantTokens)
    }
  }

  /**
    * Extracts the KMSTuple (KMS client and grant tokens) from keyManagerStrat.
    * The KMSTuple might not just be for encryption but can also be used for other operations.
    * 
    * The function handles three different key manager strategy patterns:
    * - reEncrypt: Only has one kms client and grant tokens
    * - decryptEncrypt: Uses separate KMS clients for decryption and encryption (returns the encrypt client)
    * - kmsSimple: Only has one kms client and grant tokens
    * 
    * @param keyManagerStrategy The strategy pattern that defines which KMS clients to used
    * @returns A KMSTuple containing KMS client and grant tokens extracted from keyManagerStrat
    */
  function getEncryptKMSTuple(
    keyManagerStrategy: keyManagerStrat
  ) : (output: KMSTuple)
  {
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        KMSTuple(kms.kmsClient, kms.grantTokens)
      case decryptEncrypt(kmsD, kmsE) =>
        KMSTuple(kmsE.kmsClient, kmsE.grantTokens)
      case kmsSimple(kms) =>
        KMSTuple(kms.kmsClient, kms.grantTokens)
    }
  }
  
  datatype KeyManagerAndStorage = KeyManagerAndStorage(
    storage : KeyStoreTypes.IKeyStorageInterface,
    keyManagerStrat: keyManagerStrat
  )
  {
    ghost predicate ValidState()
    {
      && storage.ValidState()
      && keyManagerStrat.ValidState()
      && storage.Modifies !! keyManagerStrat.Modifies
    }
    ghost const Modifies := multiset(storage.Modifies) + multiset(keyManagerStrat.Modifies)
  }
}
