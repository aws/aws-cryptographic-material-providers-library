// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

module {:options "/functionSyntax:4" } MutationErrorRefinement {
  import opened Wrappers
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import KMSKeystoreOperations
  import KMS = Com.Amazonaws.Kms

  function ExtractKmsOpaque(
    error: KMSKeystoreOperations.KmsError
  ): (opaqueError?: Option<KMS.Types.OpaqueError>)
    ensures
      && error.ComAmazonawsKms?
      && error.ComAmazonawsKms.Opaque?
      ==> opaqueError?.Some? && opaqueError?.value == error.ComAmazonawsKms
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => None
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => Some(comAmazonawsKms)
          case _ => None
        }
    }
  }

  function ExtractMessageFromKmsError(
    error: KMSKeystoreOperations.KmsError
  ): (errorMessage?: Option<string>)
  {
    match error {
      case Opaque(obj) => None
      case KeyManagementException(s) => Some(s)
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
        match comAmazonawsKms {
          case Opaque(obj) => None
          case _ => comAmazonawsKms.message
        }
    }
  }

  function DefaultKmsErrorMessage(
    nameonly localOperation: string,
    nameonly kmsOperation: string,
    nameonly identifier: string,
    nameonly kmsArn: string,
    nameonly while?: Option<string> := None,
    nameonly errorMessage?: Option<string> := None
  ): (message: string)
  {
    "KMS through an exception for "
    + localOperation + "'s " + kmsOperation
    + (if while?.Some? then " while " + while?.value else ".")
    + " KMS ARN: " + kmsArn
    + "\tBranch Key ID: " + identifier
    + "\nKMS Message: " + errorMessage?.UnwrapOr("")
  }

  function VerifyActiveException(
    branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    error: KMSKeystoreOperations.KmsError
  ): (output: Types.Error)
    requires branchKeyItem.Type.ActiveHierarchicalSymmetricVersion?
  {
    var message := DefaultKmsErrorMessage(
                     localOperation := "InitializeMutation",
                     kmsOperation := "ReEncrypt",
                     identifier := branchKeyItem.Identifier,
                     kmsArn := branchKeyItem.KmsArn,
                     while? := Some("verifying the Active Branch Key. Do you have permission for the original KMS ARN?"),
                     errorMessage? := ExtractMessageFromKmsError(error));
    Types.MutationFromException(message := message)
  }

  function VerifyTerminalException(
    branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    error: KMSKeystoreOperations.KmsError
  ): (output: Types.Error)
    requires branchKeyItem.Type.HierarchicalSymmetricVersion?
  {
    var message := DefaultKmsErrorMessage(
                     localOperation := "ApplyMutation",
                     kmsOperation := "ReEncrypt",
                     identifier := branchKeyItem.Identifier,
                     kmsArn := branchKeyItem.KmsArn,
                     while? := Some("verifying a Version with terminal properities."
                                    + " Do you have permission for the terminal KMS ARN?"
                                    + " Version (Decrypt Only): " + branchKeyItem.Type.HierarchicalSymmetricVersion.Version),
                     errorMessage? := ExtractMessageFromKmsError(error));
    Types.MutationToException(message := message)
  }

  // https://github.com/smithy-lang/smithy-dafny/issues/609
  // TODO-Mutations-GA :: Once we can get a string from KMS Oapque,
  // we can check it for ReEncryptTo or ReEncryptFrom.
  // Than, this function can return
  // MutationToException or MutationFromException
  function MutateException(
    branchKeyItem: KeyStoreTypes.EncryptedHierarchicalKey,
    error: KMSKeystoreOperations.KmsError,
    terminalKmsArn: string
  ): (output: Types.Error)
    requires branchKeyItem.Type.HierarchicalSymmetricVersion? || branchKeyItem.Type.ActiveHierarchicalSymmetricBeacon?
  {
    var while? :=
      if branchKeyItem.Type.HierarchicalSymmetricVersion?
      then Some("mutating a Version."
                + " Do you have permission for the original and terminal KMS ARN?"
                + " Version (Decrypt Only): " + branchKeyItem.Type.HierarchicalSymmetricVersion.Version)
      else Some("mutating the Beacon Key."
                + " Do you have permission for the the original and terminal KMS ARN?");
    // https://github.com/smithy-lang/smithy-dafny/issues/609
    // If opaqueKmsError?.Some?, parse for ReEncryptTo or ReEncrytFrom
    var opaqueKmsError? := ExtractKmsOpaque(error);
    var message := DefaultKmsErrorMessage(
                     localOperation := "ApplyMutation",
                     kmsOperation := "ReEncrypt",
                     identifier := branchKeyItem.Identifier,
                     kmsArn := "original: " + branchKeyItem.KmsArn + "\tterminal: " + terminalKmsArn,
                     while? := while?,
                     errorMessage? := ExtractMessageFromKmsError(error));
    if opaqueKmsError?.Some?
    then Types.ComAmazonawsKms(ComAmazonawsKms := opaqueKmsError?.value)
    else Types.KeyStoreAdminException(message := message)
  }
}
