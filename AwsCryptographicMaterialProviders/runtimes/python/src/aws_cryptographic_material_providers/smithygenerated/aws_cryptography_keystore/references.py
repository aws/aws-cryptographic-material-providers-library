# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import abc
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    ClobberMutationLockInput_ClobberMutationLockInput as DafnyClobberMutationLockInput,
    ClobberMutationLockOutput_ClobberMutationLockOutput as DafnyClobberMutationLockOutput,
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
    WriteInitializeMutationInput_WriteInitializeMutationInput as DafnyWriteInitializeMutationInput,
    WriteInitializeMutationOutput_WriteInitializeMutationOutput as DafnyWriteInitializeMutationOutput,
    WriteMutatedVersionsInput_WriteMutatedVersionsInput as DafnyWriteMutatedVersionsInput,
    WriteMutatedVersionsOutput_WriteMutatedVersionsOutput as DafnyWriteMutatedVersionsOutput,
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
            and hasattr(subclass, "QueryForVersions")
            and callable(subclass.QueryForVersions)
            and hasattr(subclass, "WriteMutatedVersions")
            and callable(subclass.WriteMutatedVersions)
            and hasattr(subclass, "GetMutation")
            and callable(subclass.GetMutation)
            and hasattr(subclass, "DeleteMutation")
            and callable(subclass.DeleteMutation)
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
        """Gets the ACTIVE branch key and the beacon key, and looks for a
        Mutation Commitment & Index, returning them if found."""
        raise NotImplementedError

    @abc.abstractmethod
    def write_initialize_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.WriteInitializeMutationOutput":
        """Atomically writes,

        in the terminal state of a Mutation:
        - new ACTIVE item
        -
        version (decrypt only) for new ACTIVE
        - beacon key
        - mutated Versions
        Also
        writes the Mutation Commitment & Index.
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
        - every version already exsisting
        - every
        version's enc has not changed
        - the Mutation Commitment has not changed
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_mutation(
        self,
        param: "aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.UpdateMutationIndexInput",
    ) -> "aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.UpdateMutationIndexOutput":
        """Updates a Mutation Index."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_mutation_lock(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationLockInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationLockOutput":
        """Check for Mutation Lock on a Branch Key ID.

        If one exists, returns the Mutation Lock. Otherwise, returns
        nothing.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ClobberMutationLockInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ClobberMutationLockOutput":
        """Overwrite an existing Mutation Lock."""
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
        native_input = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetMutationInput(
            dafny_input
        )
        try:
            native_output = self.get_mutation(native_input)
            dafny_output = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetMutationOutput(
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
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetMutationLockInput(
            dafny_input
        )
        try:
            native_output = self.get_mutation_lock(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetMutationLockOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetMutationLockAndIndex(
        self, dafny_input: "DafnyGetMutationLockAndIndexInput"
    ) -> "DafnyGetMutationLockAndIndexOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_ClobberMutationLockInput(
            dafny_input
        )
        try:
            native_output = self.clobber_mutation_lock(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_ClobberMutationLockOutput(
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
        """Gets the ACTIVE branch key and the beacon key, and looks for a
        Mutation Commitment & Index, returning them if found."""
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
        - new ACTIVE item
        -
        version (decrypt only) for new ACTIVE
        - beacon key
        - mutated Versions
        Also
        writes the Mutation Commitment & Index.
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
        - every version already exsisting
        - every
        version's enc has not changed
        - the Mutation Commitment has not changed
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
        param: "aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.UpdateMutationIndexInput",
    ) -> "aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.UpdateMutationIndexOutput":
        """Updates a Mutation Index."""
        dafny_output = self._impl.UpdateMutationIndex(
            aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_UpdateMutationIndexInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_UpdateMutationIndexOutput(
                dafny_output.value
            )

    def get_mutation_lock(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationLockInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.GetMutationLockOutput":
        """Check for Mutation Lock on a Branch Key ID.

        If one exists, returns the Mutation Lock. Otherwise, returns
        nothing.
        """
        dafny_output = self._impl.GetMutationLock(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetMutationLockInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetMutationLockOutput(
                dafny_output.value
            )

    def delete_mutation(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ClobberMutationLockInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.models.ClobberMutationLockOutput":
        """Overwrite an existing Mutation Lock."""
        dafny_output = self._impl.ClobberMutationLock(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_ClobberMutationLockInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.deserialize import (
                _deserialize_error as aws_cryptography_keystore_deserialize_error,
            )

            raise aws_cryptography_keystore_deserialize_error(dafny_output.error)

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_ClobberMutationLockOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "KeyStorageInterface":
        return KeyStorageInterface(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}
