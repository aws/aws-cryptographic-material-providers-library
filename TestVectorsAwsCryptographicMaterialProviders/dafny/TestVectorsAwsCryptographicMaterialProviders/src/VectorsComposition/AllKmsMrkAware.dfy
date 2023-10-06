// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllKmsMrkAware {
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened JSON.Values
  import opened KeyDescriptionJson

  const AllAwsKMSMrkKeys := [ "us-west-2-mrk", "us-east-1-mrk" ]
  const AllKmsMrkAware :=
    set
      encryptKey <- AllAwsKMSMrkKeys,
      decryptKey <- AllAwsKMSMrkKeys
      ::
        PositiveKeyDescriptionJSON(
          description := "Generated KMS MRK " + encryptKey + "->" + decryptKey,
          encrypt := Object([
                              ("type", String("aws-kms-mrk-aware")),
                              ("key", String(encryptKey))
                            ]),
          decrypt := Object([
                              ("type", String("aws-kms-mrk-aware")),
                              ("key", String(decryptKey))
                            ])
        )

  const Tests :=
    set
      keyDescription <- AllKmsMrkAware,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
