// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllKms {
  import opened JSON.Values
  import opened KeyDescriptionJson

  const AllAwsKMSKeys := [ "us-west-2-decryptable", "us-west-2-mrk" ]
  const AllKms :=
    set
      key <- AllAwsKMSKeys
      ::
        var keyDescription := Object([
                                       ("type", String("aws-kms")),
                                       ("key", String(key))
                                     ]);
        PositiveKeyDescriptionJSON(
          description := "Generated KMS " + key,
          encrypt := keyDescription,
          decrypt := keyDescription
        )

  const Tests :=
    set
      keyDescription <- AllKms,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
