// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } ErrorMessages {
  const DISCOVERY_CREATE_KEY_NO_ARN_ERROR_MSG :=
    "Key Store's kmsConfiguration is Discovery, a KMS Key ARN is required to Create a Branch Key."

  const CREATE_KEY_KMS_ARN_DISAGREEMENT :=
    "Key Store's kmsConfiguration's KMS Key ARN differs from KMS Key ARN in request."

  const KMS_KEY_ARN_INVALID :=
    "KMS Key ARN in request is invalid."

  const CUSTOM_BRANCH_KEY_ID_NEED_EC :=
    "Custom branch key id requires custom encryption context."

  const GET_KEY_ARN_DISAGREEMENT :=
    "AWS KMS Key ARN does not match configured value"

  const AUGMENT_GRANT_TOKENS_EXCEEDS_TEN :=
    "Augmenting KeyStore's Config's Grant Tokens with Request's Grant Tokens exceeds 10 Token limit."

  const DISCOVERY_CREATE_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn to Create Branch Keys."

  const DISCOVERY_VERSION_KEY_NOT_SUPPORTED :=
    "Key Store's kmsConfiguration MUST BE kmsKeyArn to Version Branch Keys."

  const UTF8_ENCODING_ENCRYPTION_CONTEXT_ERROR :=
    "Unable to UTF8 Encode element of Encryption Context."

  const VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT :=
    "Branch Key's AWS KMS Key ARN read from Dynamodb does not match configured AWS KMS Key ARN."
}
