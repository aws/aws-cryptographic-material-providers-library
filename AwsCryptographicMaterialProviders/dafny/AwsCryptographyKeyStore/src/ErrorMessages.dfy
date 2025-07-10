// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } KeyStoreErrorMessages {
  const KMS_CONFIG_KMS_ARN_INVALID :=
    "KMSConfiguration's KMS Key ARN is invalid."

  const CUSTOM_BRANCH_KEY_ID_NEED_EC :=
    "Custom branch key identifier requires custom encryption context."

  const GET_KEY_ARN_DISAGREEMENT :=
    "Branch key's KMS Key ARN read from Dynamodb does not match Key Store's configured KMS Key ARN."

  const DISCOVERY_CREATE_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn or kmsMRKeyArn to Create Branch Keys."

  const DISCOVERY_VERSION_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn or kmsMRKeyArn to Version Branch Keys."

  const UTF8_ENCODING_ENCRYPTION_CONTEXT_ERROR :=
    "Unable to UTF8 Encode element of Encryption Context."

  // Leaving this here in case we decide we want a different error message
  const VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT := GET_KEY_ARN_DISAGREEMENT

  // Message assumes KMS resourceTypes are only [ alias, key ]
  const ALIAS_NOT_ALLOWED :=
    "Key Store encountered a KMS Alias ARN instead of a KMS Key ARN, which is not allowed."

  const NO_CORRESPONDING_BRANCH_KEY :=
    "No item found for corresponding branch key identifier."

  const INVALID_HIERARCHY_VERSION :=
    "Invalid hierarchy version. Expected version 1 or 2."

  const BRANCH_KEY_ID_NEEDED :=
    "Empty string not supported for branch key identifier."

  const KMS_DECRYPT_INVALID_KEY_LENGTH_HV2 :=
    "Invalid response from AWS KMS Decrypt: Plaintext is not 80 bytes. This could mean the persisted branch key Item has been tampered."


  // If the Item/Record contains an invalid KMS ARN
  const RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN :=
    "The `kms-arn` field for the requested branch key identifier is corrupted."

  const MD_DIGEST_SHA_NOT_MATCHED :=
    "This branch key item has failed the authentication check. Either it has been tampered with or the wrong 'Logical Key Store Name' has been provided."

  const INVALID_EC_FOUND :=
    "Invalid encryption context found."
    + " This Branch Key has been modified outside of the library"
    + " to include an attribute pair that is not prefixed with 'aws-crypto-ec:'."
    + " This modification, done without using an AWS Crypto Tools library,"
    + " prevents the Branch Key from being used with 'hierarchy-version-2'."
    + " Remove this modification while maintaining the Branch Key's cryptographic integrity,"
    + " and it should be possible to use this Branch Key."

}
