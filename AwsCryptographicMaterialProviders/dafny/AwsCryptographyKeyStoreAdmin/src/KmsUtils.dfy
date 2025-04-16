// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"

module {:options "/functionSyntax:4" } KmsUtils {
  import opened Wrappers
  import KMS = Com.Amazonaws.Kms
  import KMSKeystoreOperations
  import KeyStoreTypes = KMSKeystoreOperations.Types
  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
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
    opaque predicate SupportHV1()
    {
      match this
      case decryptEncrypt(kmD, kmE) => true
      case reEncrypt(km) => true
      case kmsSimple(km) => false
    }
    opaque predicate SupportHV2()
    {
      match this
      case decryptEncrypt(kmD, kmE) => false
      case reEncrypt(km) => false
      case kmsSimple(km) => true
    }
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
      case BranchKeyCiphertextException(s) => None
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
      case BranchKeyCiphertextException(s) => Some(s)
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => None
          case OpaqueWithText(obj, objMessage) => Some(objMessage)
          case _ => comAmazonawsKms.message
        }
    }
  }

  function KmsSymmetricKeyArnToKMSConfiguration(
    kmsSymmetricArn: Types.KmsSymmetricKeyArn
  ): (output: KeyStoreTypes.KMSConfiguration)
    requires
      match kmsSymmetricArn
      case KmsKeyArn(arn) => KmsArn.ValidKmsArn?(arn)
  {
    match kmsSymmetricArn
    case KmsKeyArn(kmsKeyArn) => KeyStoreTypes.kmsKeyArn(kmsKeyArn)
  }

  // predicate {:isolate_assertions} IsSupportedKeyManagerStrategy(
  //   mutationToApply: StateStrucs.MutationToApply,
  //   keyManagerStrategy: keyManagerStrat
  // )
  // {
  //   && (mutationToApply.Terminal.hierarchyVersion.v1? ==> keyManagerStrategy.SupportHV1())
  //   && (mutationToApply.Terminal.hierarchyVersion.v2? ==> keyManagerStrategy.SupportHV2())
  // }

  opaque predicate IsHV1Supported(
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: keyManagerStrat
  )
  {
    mutationToApply.Terminal.hierarchyVersion.v1? ==> keyManagerStrategy.SupportHV1()
  }

  opaque predicate IsHV2Supported(
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: keyManagerStrat
  )
  {
    mutationToApply.Terminal.hierarchyVersion.v2? ==> keyManagerStrategy.SupportHV2()
  }

  predicate {:isolate_assertions} IsSupportedKeyManagerStrategy(
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: keyManagerStrat
  )
    requires mutationToApply.Terminal.hierarchyVersion.v1? || mutationToApply.Terminal.hierarchyVersion.v2?
  {
    && IsHV1Supported(mutationToApply, keyManagerStrategy)
    && IsHV2Supported(mutationToApply, keyManagerStrategy)
  }
}
