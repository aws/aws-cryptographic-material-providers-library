// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "KmsUtils.dfy"

module {:options "/functionSyntax:4" } SystemKeyErrorRefinement {
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KMSKeystoreOperations
  import KMS = Com.Amazonaws.Kms
  import StandardLibrary.String
  import Structure
  import KmsUtils

  // function ParsedErrorContext(
  //   nameonly localOperation: string,
  //   nameonly kmsOperation: string,
  //   nameonly kmsId: string,
  //   nameonly identifier: string,
  //   nameonly itemType: string,
  //   nameonly errorMessage?: Option<string> := None
  // ): (message: string)
  // {
  //   "MPL Operation: " + localOperation + ";"
  //   + " KMS Operation: "  + kmsOperation + ";"
  //   + " KMS ID: "  + kmsId + ";"
  //   + " Branch Key ID: " + identifier + ";"
  //   + " Type:  " + itemType + ";"
  //   + "\nKMS Message: " + errorMessage?.UnwrapOr("")
  // }

  // function SignException(
  //   nameonly branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
  //   nameonly error: KMSKeystoreOperations.KmsError,
  //   nameonly localOperation: string := "InitializeMutation",
  //   nameonly kmsOperation: string := "ReEncrypt"
  // ): (output: Types.Error)
  //   requires branchKeyItem.Type.ActiveHierarchicalSymmetricVersion?
  // {
  //   //TODO-Mutations-GA :: Better error message
  //   var opaqueKmsError? := KmsUtils.ExtractKmsOpaque(error);
  //   var kmsErrorMessage? := KmsUtils.ExtractMessageFromKmsError(error);
  //   var errorContext := ParsedErrorContext(
  //                         localOperation := localOperation,
  //                         kmsOperation := kmsOperation,
  //                         identifier := branchKeyItem.Identifier,
  //                         itemType := Structure.BRANCH_KEY_ACTIVE_TYPE,
  //                         errorMessage? := kmsErrorMessage?);
  //   var message :=
  //     "Key Management denied access while Siging a "
  //     + ". Check access to KMS ARN: " + branchKeyItem.KmsArn  + " ."
  //     + "\n" + errorContext;
  //   Types.MutationToException(message := message)
  // }
}
