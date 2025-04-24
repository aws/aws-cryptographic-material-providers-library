// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

include "../../../dafny/AwsCryptographyKeyStore/src/KmsUtils.dfy"

module {:options "/functionSyntax:4" } KeyStoreAdminHelpers {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KmsArn
  import KmsUtils
  import KMS = Com.Amazonaws.Kms

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

  datatype InternalSystemKey =
    | TrustStorage()
    | KmsSymEnc(
        nameonly Tuple: KmsUtils.KMSTuple,
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
}