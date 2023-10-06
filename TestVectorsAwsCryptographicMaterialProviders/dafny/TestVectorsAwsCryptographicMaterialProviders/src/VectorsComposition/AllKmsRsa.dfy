// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllKmsRsa {
  import ComAmazonawsKmsTypes
  import opened JSON.Values
  import opened KeyDescriptionJson

  const AllEncryptionAlgorithmSpec :=
    set e: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec
      | !e.SYMMETRIC_DEFAULT?
      :: match e
         case RSAES_OAEP_SHA_1() => "RSAES_OAEP_SHA_1"
         case RSAES_OAEP_SHA_256() => "RSAES_OAEP_SHA_256"
  const AllKmsRsaKeys := [ "us-west-2-rsa-mrk" ]
  const KmsRsa := "KMS RSA "

  const AllKmsRsa :=
    set
      keyId <- AllKmsRsaKeys,
      algorithmSpec <- AllEncryptionAlgorithmSpec
      ::
        PositiveKeyDescriptionJSON(
          description := KmsRsa + keyId,
          encrypt := Object([
                              ("type", String("aws-kms-rsa")),
                              ("key", String(keyId)),
                              ("encryption-algorithm", String(algorithmSpec))
                            ]),
          decrypt := Object([
                              ("type", String("aws-kms-rsa")),
                              ("key", String(keyId)),
                              ("encryption-algorithm", String(algorithmSpec))
                            ])
        )

  const Tests :=
    set
      keyDescription <- AllKmsRsa,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
