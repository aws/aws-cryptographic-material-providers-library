// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } KeyStoreErrorMessages {
  const KMS_CONFIG_KMS_ARN_INVALID :=
    "Key Store's KMS Key ARN is invalid."

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

  const BRANCH_KEY_ID_NEEDED :=
    "Empty string not supported for branch key identifier."

  // If the Item/Record contains an invalid KMS ARN
  const RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN :=
    "The `kms-arn` field for the requested branch key identifier is corrupted."

  const INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE :=
    "Invalid active encrypted branch key from storage."

  const INVALID_BRANCH_KEY_VERSION_FROM_STORAGE :=
    "Invalid encrypted branch key version from storage."

  const INVALID_BEACON_KEY_FROM_STORAGE :=
    "Invalid encrypted beacon key from storage."

  const ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT :=
    "Encryption context attribute name exceeds DDB limit."

  const CREATE_KEY_STORE_DEPRECATED :=
    "Create key store is only supported with legacy configurations. \n" +
    "For details on how to create a DDB table manually see:\n" +
    "https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html#hierarchical-keyring-prereqs"
}
