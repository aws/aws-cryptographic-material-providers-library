// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

module {:options "/functionSyntax:4" } KmsUtils {
  import KMS = ComAmazonawsKmsTypes

  datatype KMSTuple = | KMSTuple(
    kmsClient: KMS.IKMSClient,
    grantTokens: KMS.GrantTokenList)

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
      case decryptEncrypt(kmD, kmE) =>
        && kmD.kmsClient.ValidState()
        && kmE.kmsClient.ValidState()
        && kmD.kmsClient.Modifies == kmD.kmsClient.Modifies
        && kmE.kmsClient.Modifies == kmE.kmsClient.Modifies
           // We will assume this is the case in order to make verification happy
        && kmE.kmsClient.Modifies !! kmD.kmsClient.Modifies
    }
  }
}
