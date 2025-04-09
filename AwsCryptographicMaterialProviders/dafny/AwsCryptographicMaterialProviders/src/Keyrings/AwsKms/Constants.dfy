// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../../AwsArnParsing.dfy"

module Constants {
  import UTF8
  import Types = AwsCryptographyMaterialProvidersTypes
  import AwsArnParsing
  import opened UInt = StandardLibrary.UInt
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes

  const UINT32_TO_SEQ_LEN := 4
  const KDF_SALT_LEN: int32 := 32
  const KDF_EXPECTED_LEN: int32 := 64
  const ECDH_COMMITMENT_KEY_LENGTH := 32
  const ECDH_COMMITMENT_KEY_INDEX := 32
  const ECDH_WRAPPED_KEY_MATERIAL_INDEX := 64
  const ECDH_KDF_STRING: string := "ecdh-key-derivation"
  const ECDH_KDF_PRF_STRING: string := "HMAC_SHA384"
  const ECDH_KDF_DELIMETER: seq<uint8> := [0x00]

  const ECDH_PROVIDER_INFO_256_LEN :uint32  := 75
  const ECDH_PROVIDER_INFO_384_LEN :uint32  := 107
  const ECDH_PROVIDER_INFO_521_LEN :uint32  := 143
  const ECDH_PROVIDER_INFO_RPL_INDEX := 1 as uint32
  const ECDH_PROVIDER_INFO_RPK_INDEX := ECDH_PROVIDER_INFO_RPL_INDEX + ECDH_PROVIDER_INFO_PUBLIC_KEY_LEN as uint32
  const ECDH_PROVIDER_INFO_PUBLIC_KEY_LEN : int := 4
  const ECDH_PUBLIC_KEY_LEN_ECC_NIST_256 := 91
  const ECDH_PUBLIC_KEY_LEN_ECC_NIST_384 := 120
  const ECDH_PUBLIC_KEY_LEN_ECC_NIST_521 := 158

  const ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_256 := 33
  const ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_384 := 49
  const ECDH_PUBLIC_KEY_COMPRESSED_LEN_ECC_NIST_521 := 67

  const CIPHERTEXT_WRAPPED_MATERIAL_INDEX := 68
  const ECDH_AES_256_ENC_KEY_LENGTH: int32 := 32
  const ECDH_AES_256_ENC_TAG_LENGTH: int32 := 16
  const ECDH_AES_256_ENC_IV_LENGTH: int32 := 12
  const ECDH_AES_256_ENC_ALG := PrimitiveTypes.AES_GCM(
                                  keyLength := ECDH_AES_256_ENC_KEY_LENGTH,
                                  //= aws-encryption-sdk-specification/framework/raw-ecdh-keyring.md#data-key-wrapping
                                  //= type=implication
                                  //# - MUST use an authentication tag byte of length 16.
                                  tagLength := ECDH_AES_256_ENC_TAG_LENGTH,
                                  ivLength := ECDH_AES_256_ENC_IV_LENGTH
                                )

  // UTF-8 encoded "aws-kms"
  const PROVIDER_ID: UTF8.ValidUTF8Bytes :=
    var s := [0x61, 0x77, 0x73, 0x2D, 0x6B, 0x6D, 0x73];
    assert UTF8.ValidUTF8Range(s, 0, 7);
    s

  // UTF-8 encoded "aws-kms-hierarchy"
  const PROVIDER_ID_HIERARCHY:  UTF8.ValidUTF8Bytes :=
    var s := [0x61, 0x77, 0x73, 0x2D, 0x6B, 0x6D, 0x73,
              0x2D, 0x68, 0x69, 0x65, 0x72, 0x61, 0x72, 0x63, 0x68, 0x79];
    assert UTF8.ValidUTF8Range(s, 0, 17);
    s

  // UTF-8 encoded "aws-kms-rsa"
  const RSA_PROVIDER_ID: UTF8.ValidUTF8Bytes :=
    var s := [ 0x61, 0x77, 0x73, 0x2d, 0x6b, 0x6d, 0x73, 0x2d, 0x72, 0x73, 0x61 ];
    assert UTF8.ValidUTF8Range(s, 0, 11);
    s

  // UTF-8 Encoded "aws-kms-ecdh"
  const KMS_ECDH_PROVIDER_ID: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii("aws-kms-ecdh")

  // UTF-8 Encoded "raw-ecdh"
  const RAW_ECDH_PROVIDER_ID: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii("raw-ecdh")

  // UTF-8 Encoded "HMAC_SHA384"
  const ECDH_KDF_PRF_NAME: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii("HMAC_SHA384")

  // UTF-8 Encoded "ecdh-key-derivation"
  const ECDH_KDF_UTF8: UTF8.ValidUTF8Bytes := UTF8.EncodeAscii("ecdh-key-derivation")

  type AwsKmsEncryptedDataKey = edk: Types.EncryptedDataKey |
      && edk.keyProviderId == PROVIDER_ID
      && UTF8.ValidUTF8Seq(edk.keyProviderInfo)
    witness *

  /*
   * A datatype to make it easier to work with Encrypted Data Keys
   * that are protected by AWS KMS. Though the EDK technically contains
   * the ARN (in the keyProviderInfo field), pulling it out into a
   * dedicated variable which has already been converted into a usable
   * format makes our lives easier.
   */
  datatype AwsKmsEdkHelper = AwsKmsEdkHelper(
    edk: AwsKmsEncryptedDataKey,
    arn: AwsArnParsing.AwsKmsArn
  )
}
