// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

module {:options "/functionSyntax:4" } KmsUtils {
  import opened Wrappers
  import KMS = Com.Amazonaws.Kms
  import KMSKeystoreOperations

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
  {
    ghost predicate ValidState()
    {
      match this
      case reEncrypt(km) =>
        && km.kmsClient.ValidState()
        && km.kmsClient.Modifies == km.kmsClient.Modifies
        && km.ValidState()
        && km.Modifies == km.Modifies
      case decryptEncrypt(kmD, kmE) =>
        && kmD.kmsClient.ValidState()
        && kmE.kmsClient.ValidState()
        && kmD.kmsClient.Modifies == kmD.kmsClient.Modifies
        && kmE.kmsClient.Modifies == kmE.kmsClient.Modifies
           // We will assume this is the case in order to make verification happy
        && kmE.kmsClient.Modifies !! kmD.kmsClient.Modifies
        && kmD.ValidState()
        && kmE.ValidState()
        && kmD.Modifies == kmD.Modifies
        && kmE.Modifies == kmE.Modifies
        && kmD.Modifies !! kmE.Modifies
    }
    ghost const Modifies := match this
      case reEncrypt(km) => km.Modifies
      case decryptEncrypt(kmD, kmE) =>
        kmD.Modifies + kmE.Modifies
  }

  datatype InternalSystemKey =
    | TrustStorage()
    | KmsSymEnc(
        nameonly Tuple: KMSTuple,
        nameonly KeyId: KMS.Types.KeyIdType
      )
  {
    ghost predicate ValidState()
    {
      match this
      case TrustStorage() => true
      case KmsSymEnc(Tuple, KeyId) =>
        && Tuple.ValidState()
        && KMS.Types.IsValid_KeyIdType(KeyId)
        && Tuple.Modifies == Tuple.Modifies
    }
    ghost const Modifies := match this
      case TrustStorage() => {}
      case KmsSymEnc(Tuple, KeyId) => Tuple.Modifies
  }

  function ExtractKmsOpaque(
    error: KMSKeystoreOperations.KmsError
  ): (opaqueError?: Option<KMS.Types.OpaqueError>)
    ensures
      && error.ComAmazonawsKms?
      && error.ComAmazonawsKms.Opaque?
      ==> opaqueError?.Some? && opaqueError?.value == error.ComAmazonawsKms
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => None
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => Some(comAmazonawsKms)
          case OpaqueWithText(obj, objMessage) => Some(comAmazonawsKms)
          case _ => None
        }
    }
  }

  function ExtractMessageFromKmsError(
    error: KMSKeystoreOperations.KmsError
  ): (errorMessage?: Option<string>)
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => Some(s)
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => None
          case OpaqueWithText(obj, objMessage) => Some(objMessage)
          case _ => comAmazonawsKms.message
        }
    }
  }
}