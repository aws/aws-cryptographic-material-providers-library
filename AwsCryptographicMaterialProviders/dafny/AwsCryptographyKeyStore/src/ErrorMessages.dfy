// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } ErrorMessages {
  const KMS_KEY_ARN_INVALID :=
    "KMSConfiguration's KMS Key ARN is invalid."

  const CUSTOM_BRANCH_KEY_ID_NEED_EC :=
    "Custom branch key id requires custom encryption context."

  const GET_KEY_ARN_DISAGREEMENT :=
    "Branch Key's AWS KMS Key ARN read from Dynamodb does not match Key Store's configured AWS KMS Key ARN."

  const DISCOVERY_CREATE_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn to Create Branch Keys."

  const DISCOVERY_VERSION_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn to Version Branch Keys."

  const UTF8_ENCODING_ENCRYPTION_CONTEXT_ERROR :=
    "Unable to UTF8 Encode element of Encryption Context."

  // Leaving this here in case we decide we want a different error message
  const VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT := GET_KEY_ARN_DISAGREEMENT

  // Message assumes KMS resourceTypes are only [ alias, key ]
  const KMS_CONFIG_ALIAS_IS_NOT_ALLOWED :=
    "Key Store's kmsConfiguration kmsKeyArn cannot be an alias, it MUST BE a key."
}
