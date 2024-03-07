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
}
