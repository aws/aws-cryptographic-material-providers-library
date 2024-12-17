// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "KmsUtils.dfy"

module {:options "/functionSyntax:4" } MutationErrorRefinement {
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KMSKeystoreOperations
  import KMS = Com.Amazonaws.Kms
  import StandardLibrary.String
  import Structure
  import KmsUtils

  function ParsedErrorContext(
    nameonly localOperation: string,
    nameonly kmsOperation: string,
    nameonly identifier: string,
    nameonly itemType: string,
    nameonly errorMessage?: Option<string> := None
  ): (message: string)
  {
    "MPL Operation: " + localOperation + ";"
    + " KMS Operation: "  + kmsOperation + ";"
    + " Branch Key ID: " + identifier + ";"
    + " Branch Key Type:  " + itemType + ";"
    + "\nKMS Message: " + errorMessage?.UnwrapOr("")
  }

  function CreateActiveException(
    nameonly branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly error: KMSKeystoreOperations.KmsError,
    nameonly localOperation: string := "InitializeMutation",
    nameonly kmsOperation: string := "ReEncrypt"
  ): (output: Types.Error)
    requires branchKeyItem.Type.ActiveHierarchicalSymmetricVersion?
  {
    //TODO Mutations-FF :: Decrypt/Encrypt Strategy will need to refactor this
    var opaqueKmsError? := KmsUtils.ExtractKmsOpaque(error);
    var kmsErrorMessage? := KmsUtils.ExtractMessageFromKmsError(error);
    var errorContext := ParsedErrorContext(
                          localOperation := localOperation,
                          kmsOperation := kmsOperation,
                          identifier := branchKeyItem.Identifier,
                          itemType := Structure.BRANCH_KEY_ACTIVE_TYPE,
                          errorMessage? := kmsErrorMessage?);
    var message :=
      "Key Management denied access while creating the new Active item."
      + " Mutation is halted. Check access to KMS ARN: " + branchKeyItem.KmsArn  + " ."
      + "\n" + errorContext;
    Types.MutationToException(message := message)
  }

  function VerifyActiveException(
    nameonly branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly error: KMSKeystoreOperations.KmsError,
    nameonly localOperation: string := "InitializeMutation",
    nameonly kmsOperation: string := "ReEncrypt"
  ): (output: Types.Error)
    requires branchKeyItem.Type.ActiveHierarchicalSymmetricVersion?
  {
    //TODO Mutations-FF :: Decrypt/Encrypt Strategy will need to refactor this
    var opaqueKmsError? := KmsUtils.ExtractKmsOpaque(error);
    var kmsErrorMessage? := KmsUtils.ExtractMessageFromKmsError(error);
    var errorContext := ParsedErrorContext(
                          localOperation := localOperation,
                          kmsOperation := kmsOperation,
                          identifier := branchKeyItem.Identifier,
                          itemType := Structure.BRANCH_KEY_ACTIVE_TYPE,
                          errorMessage? := kmsErrorMessage?);
    var message :=
      "Key Management denied access to the Active Branch Key."
      + " Mutation is halted. Check access to KMS ARN: " + branchKeyItem.KmsArn  + " ."
      + "\n" + errorContext;
    Types.MutationFromException(message := message)
  }

  function VerifyTerminalException(
    branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    error: KMSKeystoreOperations.KmsError,
    nameonly localOperation: string := "ApplyMutation",
    nameonly kmsOperation: string := "ReEncrypt"
  ): (output: Types.Error)
    requires branchKeyItem.Type.HierarchicalSymmetricVersion?
  {
    var opaqueKmsError? := KmsUtils.ExtractKmsOpaque(error);
    var kmsErrorMessage? := KmsUtils.ExtractMessageFromKmsError(error);
    var errorContext := ParsedErrorContext(
                          localOperation := localOperation,
                          kmsOperation := kmsOperation,
                          identifier := branchKeyItem.Identifier,
                          itemType := Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyItem.Type.HierarchicalSymmetricVersion.Version,
                          errorMessage? := kmsErrorMessage?);
    var message :=
      "Key Management denied access to an already mutated item."
      + " Mutation is halted. Check access to KMS ARN: " + branchKeyItem.KmsArn  + " ."
      + "\n" + errorContext;
    Types.MutationToException(message := message)
  }

  method MutateExceptionParse(
    nameonly item: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly error: KMSKeystoreOperations.KmsError,
    nameonly terminalKmsArn: string,
    nameonly localOperation: string := "ApplyMutation",
    nameonly kmsOperation: string := "ReEncrypt"
  )
    returns (output: Types.Error)
  {
    var opaqueKmsError? := KmsUtils.ExtractKmsOpaque(error);
    var kmsErrorMessage? := KmsUtils.ExtractMessageFromKmsError(error);
    var itemType := match item.Type {
      case ActiveHierarchicalSymmetricVersion(version) => Structure.BRANCH_KEY_ACTIVE_TYPE
      case ActiveHierarchicalSymmetricBeacon(version) => Structure.BEACON_KEY_TYPE_VALUE
      case HierarchicalSymmetricVersion(version) => Structure.BRANCH_KEY_TYPE_PREFIX + version.Version
    };
    var errorContext := ParsedErrorContext(
      localOperation := localOperation,
      kmsOperation := kmsOperation,
      identifier := item.Identifier,
      itemType := itemType,
      errorMessage? := kmsErrorMessage?);
    // if it is an opaque KMS Error, and there is a message, it is KMS.Types.OpaqueWithText
    var kmsWithMsg: bool := opaqueKmsError?.Some? && kmsErrorMessage?.Some?;
    var knownKmsStrat: bool := (kmsOperation == "ReEncrypt" || kmsOperation == "Decrypt/Encrypt");
    if (kmsWithMsg && knownKmsStrat) {
      match kmsOperation {
        case "ReEncrypt" =>
          var hasReEncryptFrom? := String.HasSubString(kmsErrorMessage?.value, "ReEncryptFrom");
          var hasReEncryptTo? := String.HasSubString(kmsErrorMessage?.value, "ReEncryptTo");
          if (hasReEncryptFrom?.Some?) {
            return Types.MutationFromException(
                message := "Key Management denied access based on the original properties."
                + " Mutation is halted. Check access to KMS ARN: " + item.KmsArn + "."
                + "\n" + errorContext
              );
          }
          if (hasReEncryptTo?.Some?) {
            return Types.MutationToException(
                message := "Key Management denied access based on the terminal properties."
                + " Mutation is halted. Check access to KMS ARN: " + terminalKmsArn  + "."
                + "\n" + errorContext
              );
          }
        case "Decrypt/Encrypt" =>
          var hasDecrypt? := String.HasSubString(kmsErrorMessage?.value, "Decrypt");
          var hasEncrypt? := String.HasSubString(kmsErrorMessage?.value, "Encrypt");
          if (hasDecrypt?.Some?) {
            return Types.MutationFromException(
                message := "Key Management denied access based on the original properties."
                + " Mutation is halted. Check decrypt access to KMS ARN: " + item.KmsArn + "."
                + "\n" + errorContext
              );
          }
          if (hasEncrypt?.Some?) {
            return Types.MutationToException(
                message := "Key Management denied access based on the terminal properties."
                + " Mutation is halted. Check encrypt access to KMS ARN: " + terminalKmsArn + "."
                + "\n" + errorContext
              );
          }
        case _ =>
          // This will never happen
          return Types.KeyStoreAdminException(
              message := "Key Management through an exception."
              + " Mutation is halted. Check access to KMS."
              + "\n" + errorContext);

      }
    }
    return Types.KeyStoreAdminException(
        message := "Key Management through an exception."
        + " Mutation is halted. Check access to KMS."
        + "\n" + errorContext);
  }
}
