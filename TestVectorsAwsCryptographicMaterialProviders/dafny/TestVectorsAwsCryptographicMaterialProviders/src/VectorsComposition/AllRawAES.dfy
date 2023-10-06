// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllRawAES {
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened JSON.Values
  import opened KeyDescriptionJson

  // These are all the PositiveKeyDescription for the RawAESKeyring
  const aesPersistentKeyNames := [ "aes-128", "aes-192", "aes-256"]
  const AllRawAES :=
    set
      key <- aesPersistentKeyNames
      ::
        var keyDescription := Object([
                                       ("type", String("raw")),
                                       ("encryption-algorithm", String("aes")),
                                       ("provider-id", String("aws-raw-vectors-persistent-" + key)),
                                       ("key", String(key))
                                     ]);
        PositiveKeyDescriptionJSON(
          description := "Generated RawAES " + key,
          encrypt := keyDescription,
          decrypt := keyDescription
        )

  const Tests :=
    set
      keyDescription <- AllRawAES,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )
}
