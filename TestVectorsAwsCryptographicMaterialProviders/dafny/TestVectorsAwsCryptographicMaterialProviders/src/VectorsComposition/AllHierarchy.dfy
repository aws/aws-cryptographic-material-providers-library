// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllHierarchy {
  import opened JSON.Values
  import opened KeyDescriptionJson

  const AllHierarchy :=
    set
      keyId <- [ "static-branch-key-1" ]
      ::
        PositiveKeyDescriptionJSON(
          description := "Hierarchy KMS " + keyId,
          encrypt := Object([
                              ("type", String("aws-kms-hierarchy")),
                              ("key", String(keyId))
                            ]),
          decrypt := Object([
                              ("type", String("aws-kms-hierarchy")),
                              ("key", String(keyId))
                            ])
        )

  const Tests :=
    set
      keyDescription <- AllHierarchy,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
