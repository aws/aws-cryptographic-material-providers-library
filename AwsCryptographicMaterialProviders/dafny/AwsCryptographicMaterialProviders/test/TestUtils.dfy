// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/Materials.dfy"

module TestUtils {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import UTF8
  import MaterialProviders
  import Types = AwsCryptographyMaterialProvidersTypes
  import Materials

  // These are public resources and MUST NOT be used in any production environment
  const KMS_RSA_PUBLIC_KEY := "-----BEGIN PUBLIC KEY-----\n"
                              + "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA27Uc/fBaMVhxCE/SpCMQ\n"
                              + "oSBRSzQJw+o2hBaA+FiPGtiJ/aPy7sn18aCkelaSj4kwoC79b/arNHlkjc7OJFsN\n"
                              + "/GoFKgNvaiY4lOeJqEiWQGSSgHtsJLdbO2u4OOSxh8qIRAMKbMgQDVX4FR/PLKeK\n"
                              + "fc2aCDvcNSpAM++8NlNmv7+xQBJydr5ce91eISbHkFRkK3/bAM+1iddupoRw4Wo2\n"
                              + "r3avzrg5xBHmzR7u1FTab22Op3Hgb2dBLZH43wNKAceVwKqKA8UNAxashFON7xK9\n"
                              + "yy4kfOL0Z/nhxRKe4jRZ/5v508qIzgzCksYy7Y3QbMejAtiYnr7s5/d5KWw0swou\n"
                              + "twIDAQAB\n"
                              + "-----END PUBLIC KEY-----"
  const KMS_RSA_PRIVATE_KEY_ARN := "arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297"

  const SHARED_TEST_KEY_ARN := "arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"

  const ACCOUNT_IDS := ["658956600833"]

  const PARTITION := "aws"

  // These ECC Keys are only available in the KMS
  const KMS_ECC_256_KEY_ARN_S := "arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9"
  const KMS_ECC_256_KEY_ARN_R := "arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5"

  const KMS_ECC_384_KEY_ARN_S := "arn:aws:kms:us-west-2:370957321024:key/7f35a704-f4fb-469d-98b1-62a1fa2cc44e"
  const KMS_ECC_384_KEY_ARN_R := "arn:aws:kms:us-west-2:370957321024:key/29f0bef9-1677-4e74-b67e-acefab1295ff"

  const KMS_ECC_521_KEY_ARN_S := "arn:aws:kms:us-west-2:370957321024:key/41b502e3-cc9d-442f-bd7b-d67faed0f22e"
  const KMS_ECC_521_KEY_ARN_R := "arn:aws:kms:us-west-2:370957321024:key/c45f1043-53bb-4f37-adc5-4d25d4a84f9d"

  const KMS_ECC_256_PUBLIC_KEY_S := "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE18m54QsLUnhWU7gT8hkAceNbZ/WBGNUUSPCeIKqOyX5psiqyC1TXPOJXqKKaVv5Mg91WV9UjpboblOhNU35nRw=="
  const KMS_ECC_256_PUBLIC_KEY_R := "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9istdPCuX9nF8EmA4tioe/k0TCa2M9VeBW1N9n0sxPA6uPVOfLtE4+KuYxAGT0dYoK6CY93nowUy1yS+R7A+wA=="

  const KMS_ECC_384_PUBLIC_KEY_S := "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEfQ0OHFvwskFVjQwfqV7jpo62I6uyGY+5SPRZb6CuJ96bVreLZXh485BcPv09O/DWnpTBm8LL+YcfsqM3ECvi2ee3bDGpH6xIdr28uvyG75t5wqBjYYtZQFDf/ydfG9mm"
  const KMS_ECC_384_PUBLIC_KEY_R := "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEWgGNWQ+vEwlMxyMQkSsOAYGfT6IlgEkcanEOSjbeEpEnh8JHEiBHQ6QaROxJ7c3nEkbjbi0m+7ejBEGtkiqaY5Dsv5u1iV4fc/2v1RzPba1ZtudEmM16Eyy9LHswdJ7v"

  const KMS_ECC_521_PUBLIC_KEY_S := "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAz86qnfp3s0cl+73PQhlUstfdg9EZDA/jtLjBTWYp/1EB7RHNm8q5hMg5kBfjRDUFhbRBMlUV1xBOTgqzoSWj4oAABnQKiXXGGyu6PMN4D9nVMDsOpJ1pWU7rQexWDahBrK+5hx3beFXUpvvFRQrGAt2icUXm18VO6Qwbp0da9jyGDSY="
  const KMS_ECC_521_PUBLIC_KEY_R := "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAxLxcjtYfqc4+4oJZY0gGv2Ehu++CnVFea6uwXgEgLifq4eDSSVmQYvU8majsufpBXQwVjnDlQ7pGRw1j6K4FaLAAgYuMrmrwKtx/ZZtkbXzCwrqJY+sfCk8U5m89DX331cdBAhR2uVSPL2d5hp8up5v+EBpNArtdC5lZMx2ZrwKKYuQ="

  // THESE ARE TESTING RESOURCES; DO NOT USE IN A PROD ENVIRONMENT
  // RUN openssl ecparam -name secp256r1 -genkey -noout -out private.pem
  const ECC_P256_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n"
                            + "22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n"
                            + "7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n"
                            + "-----END PRIVATE KEY-----"
  // B64 Encoded DER REPRESENATION OF THE PUBLIC KEY
  const ECC_P256_PUBLIC := "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEp1IMe0q5R4TyJ9zHGX3N3BCLPPlxX+yb4XLldcFhCxmfAI7sJyoxNInpRMEmOR2M1ghe+9xbyWlhmBmBoUm2vA=="

  const ECC_P256_PRIVATE_R := "-----BEGIN PRIVATE KEY-----\n"
                              + "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgxpnoWJBwDUkwvLHA\n"
                              + "YZgRRby9FdJtxAMvAcPPW6iaD+2hRANCAASihMmHeVwzccmYmFKPO5rlR+M3MBRH\n"
                              + "zdCaw8TGxfX25tCKkhQUm6kUlPqaCzirEYPbUt3wK8XJ6jF5iRzuGxad\n"
                              + "-----END PRIVATE KEY-----\n"
  const ECC_P256_PUBLIC_R := "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEooTJh3lcM3HJmJhSjzua5UfjNzAUR83QmsPExsX19ubQipIUFJupFJT6mgs4qxGD21Ld8CvFyeoxeYkc7hsWnQ=="

  const ECC_P384_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n"
                            + "6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n"
                            + "GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n"
                            + "b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n"
                            + "-----END PRIVATE KEY-----"
  const ECC_P384_PUBLIC := "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGsj1ugd2lRilhQWwx90nrjIYmNhiDxvrQRB5jGd0FGhuqjZ0MV0vkKUfeSFskFmYyJ8g5NrqXm9U4rz9FGGsvnSEvDKwRTO6CwbCSKsRokUNRDxSKQS7+JprXjpmuarf"

  const ECC_P384_PRIVATE_R := "-----BEGIN PRIVATE KEY-----\n"
                              + "MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDBX0BpijAta/CndWCkA\n"
                              + "hl4fu2mIlnsh8umliaBBDHjA2T/3eeYWid5m96Bs2QxYIn6hZANiAAR/qhoNylqV\n"
                              + "2084hlZEXr8XWj9DuZ0WHgJ/rniicwqxXEFwPCkeh7VvpO7+tN8HxUoWpPLSdkCK\n"
                              + "nWeq6senikNb4RNp3Na43wPyF2SjQI/uzujHjlrVrea2zvJP7rsLdAI=\n"
                              + "-----END PRIVATE KEY-----\n"
  const ECC_P384_PUBLIC_R  := "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEf6oaDcpaldtPOIZWRF6/F1o/Q7mdFh4Cf654onMKsVxBcDwpHoe1b6Tu/rTfB8VKFqTy0nZAip1nqurHp4pDW+ETadzWuN8D8hdko0CP7s7ox45a1a3mts7yT+67C3QC"


  const ECC_P521_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n"
                            + "xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n"
                            + "oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n"
                            + "I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n"
                            + "C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n"
                            + "Qg==\n"
                            + "-----END PRIVATE KEY-----"
  const ECC_P521_PUBLIC := "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQB3jJzJGnYdp5HrVE3A7yhOFgnHU3SBSmg6sLTCG6v8uTeBCO+zsWMCj+yHRgQvZ/xpHDSFsekfdc3NwCHfWu1azkBffh4rZ25Qci9btzepFoVHwt7q8tdU/HZDVvi21ZJl/Ad/rOlWhEFimvkmAXpj1dOWiYVNMWmhfzIbCxsCi6T6UI="

  const ECC_P521_PRIVATE_R := "-----BEGIN PRIVATE KEY-----\n"
                              + "MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIAGQrViOzSEfLFHdlp\n"
                              + "rFcl/iWrPt7vWyga71fnLOzj4nTWBJ/Pua+xOVfTGjgplH4t16sRl4qk113Zv8zY\n"
                              + "XfgTJvChgYkDgYYABACKN7raKlNTwzxw97HarkQB7+9cTvw1grfhwW6AkUIS8b6J\n"
                              + "7CgTTSKZ6M5XQ0leYOZMkqXgjlpUfki4G3XXa4hw0wBUw+x9qtoAlwJNYhUsYg7N\n"
                              + "bm7IF9TQSuAzWgrSfIjOJfjrHjBR0TLmtk26xxKZIw36JSl9qb9b8LqlLk8uW6eE\n"
                              + "Lw==\n"
                              + "-----END PRIVATE KEY-----"
  const ECC_P521_PUBLIC_R  := "MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQAije62ipTU8M8cPex2q5EAe/vXE78NYK34cFugJFCEvG+iewoE00imejOV0NJXmDmTJKl4I5aVH5IuBt112uIcNMAVMPsfaraAJcCTWIVLGIOzW5uyBfU0ErgM1oK0nyIziX46x4wUdEy5rZNuscSmSMN+iUpfam/W/C6pS5PLlunhC8="

  // This axiom should only be used by tests to skip UTF8 verification of long sequences
  // long to be serialized in 16 bytes, in order to avoid a false negative for from verification.
  lemma {:axiom} AssumeLongSeqIsValidUTF8(s: seq<uint8>)
    requires |s| >= 0x1000
    ensures UTF8.ValidUTF8Seq(s)

  method GenerateInvalidEncryptionContext() returns (encCtx: Types.EncryptionContext)
  {
    var validUTF8char: UTF8.ValidUTF8Bytes :- expect UTF8.Encode("a");
    var key: UTF8.ValidUTF8Bytes := [];
    while |key| < UINT16_LIMIT {
      UTF8.ValidUTF8Concat(key, validUTF8char);
      key := key + validUTF8char;
    }
    encCtx := map[key := [0]];
  }

  // Generates a large encryption context that approaches the upper bounds of
  // what is able to be serialized in the message format.
  // Building a map item by item is slow in dafny, so this method should be used sparingly.
  method GenerateLargeValidEncryptionContext() returns (r: Types.EncryptionContext)
  {
    // KVPairsMaxSize - KVPairsLenLen / KVPairLen ==>
    // (2^16 - 1 - 2) / (2 + 2 + 2 + 1) ==> (2^16 - 3) / 7 ==> 9361
    // which is close to the max number of pairs you can stuff into a valid AAD.
    // We look for 9361 valid 2 byte UTF8 sequences (sticking to 2 bytes for simplicity).
    assert (0x1_0000 - 1 - 2) / (2 + 2 + 2 + 1) == (0x1_0000 - 3) / 7 == 9361;
    var numMaxPairs := 9361;
    var val :- expect UTF8.Encode("a");
    var encCtx: map<UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes> := map[];

    // Instead of proving termination for looking for Valid UTF8 sequences,
    // provide an upper bound to while loop
    var i := 0;
    while |encCtx| < numMaxPairs && i < 0x1_0000
      invariant forall k :: k in encCtx ==> |k| + |encCtx[k]| == 3
      decreases 0x1_0000 - i
    {
      var key := UInt16ToSeq(i as uint16);
      if UTF8.ValidUTF8Seq(key) {
        encCtx := encCtx[key := val];
      }
      i := i + 1;
    }
    // // Check that we actually built a encCtx of the correct size
    // expect SerializableTypes.IsESDKEncryptionContext(encCtx);

    return encCtx;
  }

  datatype SmallEncryptionContextVariation = Empty | A | AB | BA

  method SmallEncryptionContext(v: SmallEncryptionContextVariation)
    returns (encryptionContext: Types.EncryptionContext)
    ensures encryptionContext.Keys !! Materials.RESERVED_KEY_VALUES
  {
    var keyA :- expect UTF8.Encode("keyA");
    var valA :- expect UTF8.Encode("valA");
    var keyB :- expect UTF8.Encode("keyB");
    var valB :- expect UTF8.Encode("valB");
    match v {
      case Empty =>
        encryptionContext := map[];
      case A =>
        encryptionContext := map[keyA := valA];
      case AB =>
        encryptionContext := map[keyA := valA, keyB := valB];
      case BA =>
        // this is really the same as AB; this lets us test that this is also true at run time
        encryptionContext := map[keyB := valB, keyA := valA];
    }
    // ValidSmallEncryptionContext(encryptionContext);
  }

  method GenerateMockEncryptedDataKey(
    keyProviderId: string,
    keyProviderInfo: string
  ) returns (edk: Types.EncryptedDataKey)
  {
    var encodedkeyProviderId :- expect UTF8.Encode(keyProviderId);
    var encodedKeyProviderInfo :- expect UTF8.Encode(keyProviderInfo);
    var fakeCiphertext :- expect UTF8.Encode("fakeCiphertext");
    return Types.EncryptedDataKey(
        keyProviderId := encodedkeyProviderId,
        keyProviderInfo := encodedKeyProviderInfo,
        ciphertext := fakeCiphertext
      );
  }

  method NamespaceAndName(n: nat) returns (namespace: string, name: string)
    requires 0 <= n < 10
    ensures |namespace| < UINT16_LIMIT
    ensures |name| < UINT16_LIMIT
  {
    var s := "child" + [n as char + '0'];
    namespace := s + " Namespace";
    name := s + " Name";
  }

}
