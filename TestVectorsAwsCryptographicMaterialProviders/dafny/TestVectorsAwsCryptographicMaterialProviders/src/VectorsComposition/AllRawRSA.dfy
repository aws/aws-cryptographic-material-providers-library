// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"

module {:options "-functionSyntax:4"} AllRawRSA {
  import Types = AwsCryptographyMaterialProvidersTypes
  import opened JSON.Values
  import opened KeyDescriptionJson

  // These are all the PositiveKeyDescription for the RawRSAKeyring
  const rsaPersistentKeyNamesWithoutPublicPrivate := [ "rsa-4096" ]
  const AllRawRSA :=
    set
      key <- rsaPersistentKeyNamesWithoutPublicPrivate,
             padding: Types.PaddingScheme
      ::
        var sharedOptions := [
                               ("type", String("raw")),
                               ("encryption-algorithm", String("rsa")),
                               ("provider-id", String("aws-raw-vectors-persistent-" + key)),
                               ("padding-algorithm", String(match padding
                                case PKCS1() => "pkcs1"
                                case _ => "oaep-mgf1"
                                )),
                               ("padding-hash", String(match padding
                                case PKCS1() => "sha1"
                                case OAEP_SHA1_MGF1() => "sha1"
                                case OAEP_SHA256_MGF1() => "sha256"
                                case OAEP_SHA384_MGF1() => "sha384"
                                case OAEP_SHA512_MGF1() => "sha512"
                                ))
                             ];
        PositiveKeyDescriptionJSON(
          description := "Generated RawRSA " + key + " "
          + match padding
            case PKCS1() => "pkcs1-sha1"
            case OAEP_SHA1_MGF1() => "oaep-mgf1-sha1"
            case OAEP_SHA256_MGF1() => "oaep-mgf1-sha256"
            case OAEP_SHA384_MGF1() => "oaep-mgf1-sha384"
            case OAEP_SHA512_MGF1() => "oaep-mgf1-sha512"
        ,
          encrypt := Object(
            sharedOptions +
            [("key", String(key + "-public"))]
          ),
          decrypt := Object(
            sharedOptions +
            [("key", String(key + "-private"))]
          )
        )

  const Tests :=
    set
      keyDescription <- AllRawRSA,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites
      :: ToJson(
           keyDescription := keyDescription,
           algorithmSuite := algorithmSuite
         )

}
