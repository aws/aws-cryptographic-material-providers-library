// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"
include "AllRawAES.dfy"

module {:options "-functionSyntax:4"} AllCachingCmm {
  import opened JSON.Values
  import opened KeyDescriptionJson
  import opened Wrappers
  import AllAlgorithmSuites
  import AllRawAES
  import SortedSets
  import StandardLibrary

  const StaticCashablePlaintextDataKey
    := Object([
                ("type", String("static-material-keyring")),
                ("key", String("static-cashable-plaintext-data-key"))
              ])

  const StaticCashableAlgorithmSuite := AllAlgorithmSuites.AlgorithmSuites.GetESDKSuite(
                                          AllAlgorithmSuites.Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)

  const StaticEncryptIdentifier := "+m9XmK8rzu0FLMlFmaElNNLcW7Cpp452Tcb/HepBGBbMR2DEfQBRroQbS6jq1acjpjx5hQ9GRKphCCy/ltmHFw=="
  const StaticDecryptIdentifier := "Bghmwcshq6V3NOB77sSO/bmhGId6EoEVUfq+6MLKpW6YPccqlr/sqxL8R195Jn85LfSb66ovnnJcNmxanxnK+g=="


  const Tests :=
    (set
       encrypt
       <- set
            cacheLimitTtlSeconds <- {5, 10, 12},
            limitBytes <- {5, 10, 12},
            limitMessages <- {5, 10, 12}
            ::
              Object([
                       ("type", String("caching-cmm")),
                       ("underlying", StaticCashablePlaintextDataKey),
                       ("cacheLimitTtlSeconds", Number(Int(cacheLimitTtlSeconds))),
                       ("limitBytes", Number(Int(limitBytes))),
                       ("limitMessages", Number(Int(limitMessages))),
                       ("getEntryIdentifier", String(StaticEncryptIdentifier)),
                       ("putEntryIdentifier", String(StaticEncryptIdentifier))
                     ]),
       decrypt
       <- set
            cacheLimitTtlSeconds <- {5, 10, 12},
            limitBytes <- {5, 10, 12},
            limitMessages <- {5, 10, 12}
            ::
              Object([
                       ("type", String("caching-cmm")),
                       ("underlying", StaticCashablePlaintextDataKey),
                       ("cacheLimitTtlSeconds", Number(Int(cacheLimitTtlSeconds))),
                       ("limitBytes", Number(Int(limitBytes))),
                       ("limitMessages", Number(Int(limitMessages))),
                       ("getEntryIdentifier", String(StaticDecryptIdentifier)),
                       ("putEntryIdentifier", String(StaticDecryptIdentifier))
                     ])
       ::
         ToJson(
         keyDescription := PositiveKeyDescriptionJSON(
             description := "Successful caching test.",
             encrypt := encrypt,
             decrypt := decrypt
           ),
           algorithmSuite := StaticCashableAlgorithmSuite,
           maxPlaintextLength := Some(5)
         ))
    + (set
         encryptIdentifier <- {"", StaticEncryptIdentifier}
         ::
           ToJson(
           keyDescription := NegativeEncryptKeyDescriptionJSON(
               description := "Encrypt caching failure",
               errorDescription := "The get or put will fail because the identifier is wrong.",
               encrypt := Object([
                                   ("type", String("caching-cmm")),
                                   ("underlying", StaticCashablePlaintextDataKey),
                                   ("cacheLimitTtlSeconds", Number(Int(5))),
                                   ("getEntryIdentifier", String(encryptIdentifier)),
                                   ("putEntryIdentifier", String(""))
                                 ])
             ),
             algorithmSuite := StaticCashableAlgorithmSuite,
             maxPlaintextLength := Some(5)
           ))
    + (set
         decryptIdentifier <- {"", StaticDecryptIdentifier}
         ::
           ToJson(
           keyDescription := NegativeDecryptKeyDescriptionJSON(
               description := "Decrypt caching failure",
               decryptErrorDescription := "The get or put will fail because the identifier is wrong.",
               encrypt := Object([
                                   ("type", String("caching-cmm")),
                                   ("underlying", StaticCashablePlaintextDataKey),
                                   ("cacheLimitTtlSeconds", Number(Int(5))),
                                   ("getEntryIdentifier", String(StaticEncryptIdentifier))
                                 ]),
               decrypt := Object([
                                   ("type", String("caching-cmm")),
                                   ("underlying", StaticCashablePlaintextDataKey),
                                   ("cacheLimitTtlSeconds", Number(Int(5))),
                                   ("getEntryIdentifier", String(decryptIdentifier)),
                                   ("putEntryIdentifier", String(""))
                                 ])

             ),
             algorithmSuite := StaticCashableAlgorithmSuite,
             maxPlaintextLength := Some(5)
           ))

}
