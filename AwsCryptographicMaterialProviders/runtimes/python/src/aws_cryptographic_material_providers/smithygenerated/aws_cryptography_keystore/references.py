# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import abc
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    DeleteMutationInput_DeleteMutationInput as DafnyDeleteMutationInput,
    DeleteMutationOutput_DeleteMutationOutput as DafnyDeleteMutationOutput,
    GetEncryptedActiveBranchKeyInput_GetEncryptedActiveBranchKeyInput as DafnyGetEncryptedActiveBranchKeyInput,
    GetEncryptedActiveBranchKeyOutput_GetEncryptedActiveBranchKeyOutput as DafnyGetEncryptedActiveBranchKeyOutput,
    GetEncryptedBeaconKeyInput_GetEncryptedBeaconKeyInput as DafnyGetEncryptedBeaconKeyInput,
    GetEncryptedBeaconKeyOutput_GetEncryptedBeaconKeyOutput as DafnyGetEncryptedBeaconKeyOutput,
    GetEncryptedBranchKeyVersionInput_GetEncryptedBranchKeyVersionInput as DafnyGetEncryptedBranchKeyVersionInput,
    GetEncryptedBranchKeyVersionOutput_GetEncryptedBranchKeyVersionOutput as DafnyGetEncryptedBranchKeyVersionOutput,
    GetItemsForInitializeMutationInput_GetItemsForInitializeMutationInput as DafnyGetItemsForInitializeMutationInput,
    GetItemsForInitializeMutationOutput_GetItemsForInitializeMutationOutput as DafnyGetItemsForInitializeMutationOutput,
    GetKeyStorageInfoInput_GetKeyStorageInfoInput as DafnyGetKeyStorageInfoInput,
    GetKeyStorageInfoOutput_GetKeyStorageInfoOutput as DafnyGetKeyStorageInfoOutput,
    GetMutationInput_GetMutationInput as DafnyGetMutationInput,
    GetMutationOutput_GetMutationOutput as DafnyGetMutationOutput,
    QueryForVersionsInput_QueryForVersionsInput as DafnyQueryForVersionsInput,
    QueryForVersionsOutput_QueryForVersionsOutput as DafnyQueryForVersionsOutput,
    WriteAtomicMutationInput_WriteAtomicMutationInput as DafnyWriteAtomicMutationInput,
    WriteAtomicMutationOutput_WriteAtomicMutationOutput as DafnyWriteAtomicMutationOutput,
    WriteInitializeMutationInput_WriteInitializeMutationInput as DafnyWriteInitializeMutationInput,
    WriteInitializeMutationOutput_WriteInitializeMutationOutput as DafnyWriteInitializeMutationOutput,
    WriteMutatedVersionsInput_WriteMutatedVersionsInput as DafnyWriteMutatedVersionsInput,
    WriteMutatedVersionsOutput_WriteMutatedVersionsOutput as DafnyWriteMutatedVersionsOutput,
    WriteMutationIndexInput_WriteMutationIndexInput as DafnyWriteMutationIndexInput,
    WriteMutationIndexOutput_WriteMutationIndexOutput as DafnyWriteMutationIndexOutput,
    WriteNewEncryptedBranchKeyInput_WriteNewEncryptedBranchKeyInput as DafnyWriteNewEncryptedBranchKeyInput,
    WriteNewEncryptedBranchKeyOutput_WriteNewEncryptedBranchKeyOutput as DafnyWriteNewEncryptedBranchKeyOutput,
    WriteNewEncryptedBranchKeyVersionInput_WriteNewEncryptedBranchKeyVersionInput as DafnyWriteNewEncryptedBranchKeyVersionInput,
    WriteNewEncryptedBranchKeyVersionOutput_WriteNewEncryptedBranchKeyVersionOutput as DafnyWriteNewEncryptedBranchKeyVersionOutput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors import (
    _smithy_error_to_dafny_error,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from smithy_dafny_standard_library.internaldafny.generated import Wrappers
from typing import Any, Dict


class IKeyStorageInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "WriteNewEncryptedBranchKey")
            and callable(subclass.WriteNewEncryptedBranchKey)
            and hasattr(subclass, "WriteNewEncryptedBranchKeyVersion")
            and callable(subclass.WriteNewEncryptedBranchKeyVersion)
            and hasattr(subclass, "GetEncryptedActiveBranchKey")
            and callable(subclass.GetEncryptedActiveBranchKey)
            and hasattr(subclass, "GetEncryptedBranchKeyVersion")
            and callable(subclass.GetEncryptedBranchKeyVersion)
            and hasattr(subclass, "GetEncryptedBeaconKey")
            and callable(subclass.GetEncryptedBeaconKey)
            and hasattr(subclass, "GetKeyStorageInfo")
            and callable(subclass.GetKeyStorageInfo)
            and hasattr(subclass, "GetItemsForInitializeMutation")
            and callable(subclass.GetItemsForInitializeMutation)
            and hasattr(subclass, "WriteInitializeMutation")
            and callable(subclass.WriteInitializeMutation)
            and hasattr(subclass, "WriteAtomicMutation")
            and callable(subclass.WriteAtomicMutation)
            and hasattr(subclass, "QueryForVersions")
            and callable(subclass.QueryForVersions)
            and hasattr(subclass, "WriteMutatedVersions")
            and callable(subclass.WriteMutatedVersions)
            and hasattr(subclass, "GetMutation")
            and callable(subclass.GetMutation)
            and hasattr(subclass, "DeleteMutation")
            and callable(subclass.DeleteMutation)
            and hasattr(subclass, "WriteMutationIndex")
            and callable(subclass.WriteMutationIndex)
        )

    @abc.abstractmethod
    def write_new_encrypted_branch_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyOutput":
        """WriteNewEncryptedBranchKey persists the active item, decrypt only
        (version) item, and Beacon Key Item of a newly created Branch Key.
        :param param: The information required to atomically write an a new
        branch key into a key store. The identifiers for all keys passed should
        be the same.

        :returns: The output of writing a new branch key. There is
            currently no additional information returned.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def write_new_encrypted_branch_key_version(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionOutput":
        """WriteNewEncryptedBranchKeyVersion persists the new active item,
        decrypt only (version) item of a newly generated Branch Key version.
        :param param: The information required to atomically write a new
        version for an existing branch key into a key store. The identifiers
        for all keys passed should be the same.

        :returns: The output of writing a new version for an existing
            branch key. There is currently no additional information
            returned.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_encrypted_active_branch_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyOutput":
        """Get the ACTIVE branch key for encryption for an existing branch key.

        :param param: Get the ACTIVE version for a particular Branch
            Key.
        :returns: Outputs for getting a Branch Key's ACTIVE version.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_encrypted_branch_key_version(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionOutput":
        """Get a specific branch key version for an existing branch key.

        :param param: Inputs for getting a version of a Branch Key.
        :returns: Outputs for getting a version of a Branch Key.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_encrypted_beacon_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyOutput":
        """Get the beacon key associated with an existing branch key.

        :param param: Inputs for getting a Beacon Key
        :returns: Outputs for getting a Beacon Key
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_key_storage_info(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoOutput":
        """Gets information about the underlying storage system.

        :param param: Input for getting information about the underlying
            storage.
        :returns: Output containing information about the underlying
            storage.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_items_for_initialize_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationOutput":
        """Retrieves the items necessary to initialize a Mutation, while
        checking for any in-flight Mutations.

        These items are the ACTIVE branch key and the beacon key. If a
        Mutation is already in-flight for this Branch Key, the in-flight
        Mutation's Commitment and Index are also returned.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def write_initialize_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationOutput":
        """Atomically writes,

        in the terminal state of a Mutation:
        - new ACTIVE item, if
        provided
        - version (decrypt only) for new ACTIVE, if provided
        - beacon
        key
        Also writes the Mutation Commitment & Index.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def write_atomic_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationOutput":
        """Atomically writes,

        in the terminal state of a Mutation:
        - new ACTIVE item, if
        provided
        - version (decrypt only) for new ACTIVE, if provided
        - beacon key
        - a
        page of version (decrypt only) items
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_for_versions(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsOutput":
        """Query Storage for a page of version (decrypt only) items of a Branch
        Key."""
        raise NotImplementedError

    @abc.abstractmethod
    def write_mutated_versions(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsOutput":
        """Atomically writes, in the terminal state of a Mutation, a page of
        version (decrypt only) items,

        conditioned on:
        - every version already existing
        - every
        version's cipher-text had not changed
        - the Mutation Commitment has not
        changed

        If the Mutation is complete,
        the Mutation Index and Mutation Commitment
        are deleted.
        Otherwise,
        the Mutation Index is updated,
        conditioned on it not
        having been changed since
        it was last read.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationOutput":
        """Check for Mutation Commitment on a Branch Key ID.

        If one exists, returns the Mutation Lock. Otherwise, returns
        nothing.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationOutput":
        """Delete an existing Mutation Commitment & Index."""
        raise NotImplementedError

    @abc.abstractmethod
    def write_mutation_index(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexOutput":
        """Creates a Mutation Index, conditioned on the Mutation Commitment.

        Used in the edge case where the Commitment exists and Index does
        not. The Index may have been deleted to restart the mutation
        from the very beginning.
        """
        raise NotImplementedError

    def WriteNewEncryptedBranchKey(
        self, dafny_input: "DafnyWriteNewEncryptedBranchKeyInput"
    ) -> "DafnyWriteNewEncryptedBranchKeyOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteNewEncryptedBranchKeyInput(
            dafny_input
        )
        try:
            native_output = self.write_new_encrypted_branch_key(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteNewEncryptedBranchKeyOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def WriteNewEncryptedBranchKeyVersion(
        self, dafny_input: "DafnyWriteNewEncryptedBranchKeyVersionInput"
    ) -> "DafnyWriteNewEncryptedBranchKeyVersionOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionInput(
            dafny_input
        )
        try:
            native_output = self.write_new_encrypted_branch_key_version(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetEncryptedActiveBranchKey(
        self, dafny_input: "DafnyGetEncryptedActiveBranchKeyInput"
    ) -> "DafnyGetEncryptedActiveBranchKeyOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedActiveBranchKeyInput(
            dafny_input
        )
        try:
            native_output = self.get_encrypted_active_branch_key(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedActiveBranchKeyOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetEncryptedBranchKeyVersion(
        self, dafny_input: "DafnyGetEncryptedBranchKeyVersionInput"
    ) -> "DafnyGetEncryptedBranchKeyVersionOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedBranchKeyVersionInput(
            dafny_input
        )
        try:
            native_output = self.get_encrypted_branch_key_version(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedBranchKeyVersionOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetEncryptedBeaconKey(
        self, dafny_input: "DafnyGetEncryptedBeaconKeyInput"
    ) -> "DafnyGetEncryptedBeaconKeyOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedBeaconKeyInput(
            dafny_input
        )
        try:
            native_output = self.get_encrypted_beacon_key(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedBeaconKeyOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetKeyStorageInfo(
        self, dafny_input: "DafnyGetKeyStorageInfoInput"
    ) -> "DafnyGetKeyStorageInfoOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetKeyStorageInfoInput(
            dafny_input
        )
        try:
            native_output = self.get_key_storage_info(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetKeyStorageInfoOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetItemsForInitializeMutation(
        self, dafny_input: "DafnyGetItemsForInitializeMutationInput"
    ) -> "DafnyGetItemsForInitializeMutationOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetItemsForInitializeMutationInput(
            dafny_input
        )
        try:
            native_output = self.get_items_for_initialize_mutation(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetItemsForInitializeMutationOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def WriteInitializeMutation(
        self, dafny_input: "DafnyWriteInitializeMutationInput"
    ) -> "DafnyWriteInitializeMutationOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteInitializeMutationInput(
            dafny_input
        )
        try:
            native_output = self.write_initialize_mutation(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteInitializeMutationOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def WriteAtomicMutation(
        self, dafny_input: "DafnyWriteAtomicMutationInput"
    ) -> "DafnyWriteAtomicMutationOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteAtomicMutationInput(
            dafny_input
        )
        try:
            native_output = self.write_atomic_mutation(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteAtomicMutationOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def QueryForVersions(
        self, dafny_input: "DafnyQueryForVersionsInput"
    ) -> "DafnyQueryForVersionsOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_QueryForVersionsInput(
            dafny_input
        )
        try:
            native_output = self.query_for_versions(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_QueryForVersionsOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def WriteMutatedVersions(
        self, dafny_input: "DafnyWriteMutatedVersionsInput"
    ) -> "DafnyWriteMutatedVersionsOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteMutatedVersionsInput(
            dafny_input
        )
        try:
            native_output = self.write_mutated_versions(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteMutatedVersionsOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetMutation(
        self, dafny_input: "DafnyGetMutationInput"
    ) -> "DafnyGetMutationOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetMutationInput(
            dafny_input
        )
        try:
            native_output = self.get_mutation(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetMutationOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def DeleteMutation(
        self, dafny_input: "DafnyDeleteMutationInput"
    ) -> "DafnyDeleteMutationOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DeleteMutationInput(
            dafny_input
        )
        try:
            native_output = self.delete_mutation(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DeleteMutationOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def WriteMutationIndex(
        self, dafny_input: "DafnyWriteMutationIndexInput"
    ) -> "DafnyWriteMutationIndexOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteMutationIndexInput(
            dafny_input
        )
        try:
            native_output = self.write_mutation_index(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteMutationIndexOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class KeyStorageInterface(IKeyStorageInterface):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes.IKeyStorageInterface,
    ):
        self._impl = _impl

    def write_new_encrypted_branch_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyOutput":
        """WriteNewEncryptedBranchKey persists the active item, decrypt only
        (version) item, and Beacon Key Item of a newly created Branch Key.
        :param param: The information required to atomically write an a new
        branch key into a key store. The identifiers for all keys passed should
        be the same.

        :returns: The output of writing a new branch key. There is
            currently no additional information returned.
        """
        dafny_output = self._impl.WriteNewEncryptedBranchKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteNewEncryptedBranchKeyInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteNewEncryptedBranchKeyOutput(
                dafny_output.value
            )

    def write_new_encrypted_branch_key_version(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteNewEncryptedBranchKeyVersionOutput":
        """WriteNewEncryptedBranchKeyVersion persists the new active item,
        decrypt only (version) item of a newly generated Branch Key version.
        :param param: The information required to atomically write a new
        version for an existing branch key into a key store. The identifiers
        for all keys passed should be the same.

        :returns: The output of writing a new version for an existing
            branch key. There is currently no additional information
            returned.
        """
        dafny_output = self._impl.WriteNewEncryptedBranchKeyVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteNewEncryptedBranchKeyVersionOutput(
                dafny_output.value
            )

    def get_encrypted_active_branch_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedActiveBranchKeyOutput":
        """Get the ACTIVE branch key for encryption for an existing branch key.

        :param param: Get the ACTIVE version for a particular Branch
            Key.
        :returns: Outputs for getting a Branch Key's ACTIVE version.
        """
        dafny_output = self._impl.GetEncryptedActiveBranchKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedActiveBranchKeyInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedActiveBranchKeyOutput(
                dafny_output.value
            )

    def get_encrypted_branch_key_version(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBranchKeyVersionOutput":
        """Get a specific branch key version for an existing branch key.

        :param param: Inputs for getting a version of a Branch Key.
        :returns: Outputs for getting a version of a Branch Key.
        """
        dafny_output = self._impl.GetEncryptedBranchKeyVersion(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedBranchKeyVersionInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedBranchKeyVersionOutput(
                dafny_output.value
            )

    def get_encrypted_beacon_key(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetEncryptedBeaconKeyOutput":
        """Get the beacon key associated with an existing branch key.

        :param param: Inputs for getting a Beacon Key
        :returns: Outputs for getting a Beacon Key
        """
        dafny_output = self._impl.GetEncryptedBeaconKey(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetEncryptedBeaconKeyInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetEncryptedBeaconKeyOutput(
                dafny_output.value
            )

    def get_key_storage_info(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetKeyStorageInfoOutput":
        """Gets information about the underlying storage system.

        :param param: Input for getting information about the underlying
            storage.
        :returns: Output containing information about the underlying
            storage.
        """
        dafny_output = self._impl.GetKeyStorageInfo(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetKeyStorageInfoInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetKeyStorageInfoOutput(
                dafny_output.value
            )

    def get_items_for_initialize_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetItemsForInitializeMutationOutput":
        """Retrieves the items necessary to initialize a Mutation, while
        checking for any in-flight Mutations.

        These items are the ACTIVE branch key and the beacon key. If a
        Mutation is already in-flight for this Branch Key, the in-flight
        Mutation's Commitment and Index are also returned.
        """
        dafny_output = self._impl.GetItemsForInitializeMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetItemsForInitializeMutationInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetItemsForInitializeMutationOutput(
                dafny_output.value
            )

    def write_initialize_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationOutput":
        """Atomically writes,

        in the terminal state of a Mutation:
        - new ACTIVE item, if
        provided
        - version (decrypt only) for new ACTIVE, if provided
        - beacon
        key
        Also writes the Mutation Commitment & Index.
        """
        dafny_output = self._impl.WriteInitializeMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteInitializeMutationInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteInitializeMutationOutput(
                dafny_output.value
            )

    def write_atomic_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteAtomicMutationOutput":
        """Atomically writes,

        in the terminal state of a Mutation:
        - new ACTIVE item, if
        provided
        - version (decrypt only) for new ACTIVE, if provided
        - beacon key
        - a
        page of version (decrypt only) items
        """
        dafny_output = self._impl.WriteAtomicMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteAtomicMutationInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteAtomicMutationOutput(
                dafny_output.value
            )

    def query_for_versions(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.QueryForVersionsOutput":
        """Query Storage for a page of version (decrypt only) items of a Branch
        Key."""
        dafny_output = self._impl.QueryForVersions(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_QueryForVersionsInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_QueryForVersionsOutput(
                dafny_output.value
            )

    def write_mutated_versions(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutatedVersionsOutput":
        """Atomically writes, in the terminal state of a Mutation, a page of
        version (decrypt only) items,

        conditioned on:
        - every version already existing
        - every
        version's cipher-text had not changed
        - the Mutation Commitment has not
        changed

        If the Mutation is complete,
        the Mutation Index and Mutation Commitment
        are deleted.
        Otherwise,
        the Mutation Index is updated,
        conditioned on it not
        having been changed since
        it was last read.
        """
        dafny_output = self._impl.WriteMutatedVersions(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteMutatedVersionsInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteMutatedVersionsOutput(
                dafny_output.value
            )

    def get_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationOutput":
        """Check for Mutation Commitment on a Branch Key ID.

        If one exists, returns the Mutation Lock. Otherwise, returns
        nothing.
        """
        dafny_output = self._impl.GetMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetMutationInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetMutationOutput(
                dafny_output.value
            )

    def delete_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.DeleteMutationOutput":
        """Delete an existing Mutation Commitment & Index."""
        dafny_output = self._impl.DeleteMutation(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DeleteMutationInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DeleteMutationOutput(
                dafny_output.value
            )

    def write_mutation_index(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteMutationIndexOutput":
        """Creates a Mutation Index, conditioned on the Mutation Commitment.

        Used in the edge case where the Commitment exists and Index does
        not. The Index may have been deleted to restart the mutation
        from the very beginning.
        """
        dafny_output = self._impl.WriteMutationIndex(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_WriteMutationIndexInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_WriteMutationIndexOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStorageInterface":
        return KeyStorageInterface(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}
