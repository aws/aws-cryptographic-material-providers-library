// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "KeyStoreAdminHelpers.dfy"

module {:options "/functionSyntax:4" } MutationErrorRefinement {
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KMSKeystoreOperations
  import KMS = Com.Amazonaws.Kms
  import StandardLibrary.String
  import Structure
  import KeyStoreAdminHelpers

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

  function GenerateNewActiveException(
    nameonly identifier: string,
    nameonly kmsArn: string,
    nameonly error: KMSKeystoreOperations.KmsError,
    nameonly localOperation: string := "InitializeMutation",
    nameonly kmsOperation: string := "GenerateDataKeyWithoutPlaintext"
  ): (output: Types.Error)
  {
    var kmsError? := KMSKeystoreOperations.ExtractKmsError(error);
    var kmsErrorMessage? := KMSKeystoreOperations.ExtractMessageFromKmsError(error);
    var errorContext := ParsedErrorContext(
                          localOperation := localOperation,
                          kmsOperation := kmsOperation,
                          identifier := identifier,
                          itemType := Structure.BRANCH_KEY_ACTIVE_TYPE,
                          errorMessage? := kmsErrorMessage?);
    var message :=
      "Key Management denied access while creating the new Active item."
      + " Mutation is halted. Check access to KMS ARN: " + kmsArn  + " ."
      + "\n" + errorContext;
    Types.MutationToException(message := message)
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
    var kmsError? := KMSKeystoreOperations.ExtractKmsError(error);
    var kmsErrorMessage? := KMSKeystoreOperations.ExtractMessageFromKmsError(error);
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
    var kmsError? := KMSKeystoreOperations.ExtractKmsError(error);
    var kmsErrorMessage? := KMSKeystoreOperations.ExtractMessageFromKmsError(error);
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
    var kmsError? := KMSKeystoreOperations.ExtractKmsError(error);
    var kmsErrorMessage? := KMSKeystoreOperations.ExtractMessageFromKmsError(error);
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

  type MutationKMSError = e: Types.Error | (e.MutationFromException? || e.MutationToException? || e.KeyStoreAdminException?) witness *

  method MutateExceptionParse(
    nameonly item: KeyStoreTypes.EncryptedHierarchicalKey,
    nameonly error: KMSKeystoreOperations.KmsError,
    nameonly terminalKmsArn: string,
    nameonly localOperation: string := "ApplyMutation",
    nameonly kmsOperation: string := "ReEncrypt"
  )
    returns (output: MutationKMSError)
    requires kmsOperation == "ReEncrypt" || kmsOperation == "Encrypt" || kmsOperation == "Decrypt"
    requires localOperation == "ApplyMutation" || localOperation == "InitializeMutation"
  {
    var kmsError? := KMSKeystoreOperations.ExtractKmsError(error);
    var kmsErrorMessage? := KMSKeystoreOperations.ExtractMessageFromKmsError(error);
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
    // If it is a KMS Error, and there is a message, it is a valid KMS.Types.Error,
    // This will helps to refine KMS Error to matching KMS Arn
    var kmsWithMsg: bool := kmsError?.Some? && kmsErrorMessage?.Some?;
    // If kmsWithMsg and we can match the error message based on the KMS Operation
    if (kmsWithMsg) {
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
        case "Decrypt" =>
          var hasDecrypt? := String.HasSubString(kmsErrorMessage?.value, "Decrypt");
          if (hasDecrypt?.Some?) {
            return Types.MutationFromException(
                message := "Key Management denied access based on the original properties."
                + " Mutation is halted. Check decrypt access to KMS ARN: " + item.KmsArn + "."
                + "\n" + errorContext
              );
          }
        case "Encrypt" =>
          var hasEncrypt? := String.HasSubString(kmsErrorMessage?.value, "Encrypt");
          if (hasEncrypt?.Some?) {
            return Types.MutationToException(
                message := "Key Management denied access based on the terminal properties."
                + " Mutation is halted. Check encrypt access to KMS ARN: " + terminalKmsArn + "."
                + "\n" + errorContext
              );
          }
      }
    }
    // If kmsWithMsg we CAN match the error message based on the KMS ARN;
    // these catch KMS Key disabled or scheduled for deletion on the ReEncrypt case.
    // While we could push this if-block into the ReEncrypt case above,
    // we have not done a complete audit of all the KMS Error messages possible,
    // and KMS could change the error messages.
    // Matching on the KMS ARN is therefore still desirable,
    // even though, at this time, we believe this will only fire for ReEncrypt.
    // Examples:
    //   An error occurred (DisabledException) when calling the ReEncrypt operation: arn:aws:kms:us-west-2:827585335069:key/ea9fe275-3667-4e16-8043-80a307cfb20b is disabled.
    //   An error occurred (KMSInvalidStateException) when calling the ReEncrypt operation: arn:aws:kms:us-west-2:827585335069:key/ea9fe275-3667-4e16-8043-80a307cfb20b is pending deletion.
    if (kmsWithMsg) {
      var hasOriginalArn? := String.HasSubString(kmsErrorMessage?.value, item.KmsArn);
      var hasTerminalArn? := String.HasSubString(kmsErrorMessage?.value, terminalKmsArn);
      if (hasOriginalArn?.Some?) {
        return Types.MutationFromException(
            message := "Key Management denied access to the original KMS Key."
            + " Mutation is halted. Check access to KMS ARN: " + item.KmsArn + "."
            + "\n" + errorContext
          );
      } else if (hasTerminalArn?.Some?) {
        return Types.MutationToException(
            message := "Key Management denied access to the terminal KMS Key."
            + " Mutation is halted. Check encrypt access to KMS ARN: " + terminalKmsArn + "."
            + "\n" + errorContext
          );
      }
    }
    // Else we cannot match the error message by either the operation or the KMS ARN, log what we can and move on
    // The exception could be a network (UnknownHostException) or Creds (SigV4 failure)
    // Example:
    //   SdkClientException: Received an UnknownHostException when attempting to interact with a service. See cause for the exact endpoint that is failing to resolve. If this is happening on an endpoint that previously worked, there may be a network connectivity issue or your DNS cache could be storing endpoints for too long.
    match kmsOperation {
      case "ReEncrypt" =>
        return Types.KeyStoreAdminException(
            message := "Key Management ReEncrypt call failed."
            + " Mutation is halted. Check access/connectivity to KMS."
            + "\n Source KMS ARN: " + item.KmsArn
            + "\n Destination KMS ARN: " + terminalKmsArn
            + "\n" + errorContext
          );
      case "Decrypt" =>
        return Types.KeyStoreAdminException(
            message := "Key Management Decrypt call failed."
            + " Mutation is halted. Check access/connectivity to KMS."
            + "\n KMS ARN: " + item.KmsArn
            + "\n" + errorContext
          );
      case "Encrypt" =>
        return Types.KeyStoreAdminException(
            message := "Key Management Encrypt call failed."
            + " Mutation is halted. Check access/connectivity to KMS."
            + "\n KMS ARN: " + terminalKmsArn
            + "\n" + errorContext
          );
    }
  }
}
