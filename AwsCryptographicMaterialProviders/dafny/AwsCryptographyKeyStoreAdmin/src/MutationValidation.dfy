// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

module {:options "/functionSyntax:4" } MutationValidation {
  import opened Structure

  /** This function is largely identical to Structure.DecryptOnlyBranchKeyEncryptionContext, **/
  /** except the "custom Encryption Context" has already been prefixed. **/
  function DecryptOnlyBranchKeyEncryptionContextForMutation(
    branchKeyId: string,
    branchKeyVersion: string,
    timestamp: string,
    logicalKeyStoreName: string,
    kmsKeyArn: string,
    prefixedCustomEncryptionContext: map<string, string>
  ): (output: map<string, string>)
    requires 0 < |branchKeyId|
    requires 0 < |branchKeyVersion|
    requires prefixedCustomEncryptionContext.Keys !! BRANCH_KEY_RESTRICTED_FIELD_NAMES
    ensures BranchKeyContext?(output)
    ensures BRANCH_KEY_TYPE_PREFIX < output[TYPE_FIELD]
    ensures BRANCH_KEY_ACTIVE_VERSION_FIELD !in output
    ensures output[KMS_FIELD] == kmsKeyArn
    ensures output[TABLE_FIELD] == logicalKeyStoreName
    ensures forall k <- prefixedCustomEncryptionContext
              ::
                && k in output
                && output[k] == prefixedCustomEncryptionContext[k]
  {
    map[
      BRANCH_KEY_IDENTIFIER_FIELD := branchKeyId,
      TYPE_FIELD := BRANCH_KEY_TYPE_PREFIX + branchKeyVersion,
      KEY_CREATE_TIME := timestamp,
      TABLE_FIELD := logicalKeyStoreName,
      KMS_FIELD := kmsKeyArn,
      HIERARCHY_VERSION := HIERARCHY_VERSION_VALUE
    ] + prefixedCustomEncryptionContext
  }
}
