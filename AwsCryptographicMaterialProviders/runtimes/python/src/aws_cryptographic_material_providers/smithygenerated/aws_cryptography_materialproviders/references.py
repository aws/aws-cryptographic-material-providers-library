# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import abc
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
from aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    DecryptMaterialsInput_DecryptMaterialsInput as DafnyDecryptMaterialsInput,
    DecryptMaterialsOutput_DecryptMaterialsOutput as DafnyDecryptMaterialsOutput,
    DeleteCacheEntryInput_DeleteCacheEntryInput as DafnyDeleteCacheEntryInput,
    GetBranchKeyIdInput_GetBranchKeyIdInput as DafnyGetBranchKeyIdInput,
    GetBranchKeyIdOutput_GetBranchKeyIdOutput as DafnyGetBranchKeyIdOutput,
    GetCacheEntryInput_GetCacheEntryInput as DafnyGetCacheEntryInput,
    GetCacheEntryOutput_GetCacheEntryOutput as DafnyGetCacheEntryOutput,
    GetClientInput_GetClientInput as DafnyGetClientInput,
    GetEncryptionMaterialsInput_GetEncryptionMaterialsInput as DafnyGetEncryptionMaterialsInput,
    GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput as DafnyGetEncryptionMaterialsOutput,
    OnDecryptInput_OnDecryptInput as DafnyOnDecryptInput,
    OnDecryptOutput_OnDecryptOutput as DafnyOnDecryptOutput,
    OnEncryptInput_OnEncryptInput as DafnyOnEncryptInput,
    OnEncryptOutput_OnEncryptOutput as DafnyOnEncryptOutput,
    PutCacheEntryInput_PutCacheEntryInput as DafnyPutCacheEntryInput,
    UpdateUsageMetadataInput_UpdateUsageMetadataInput as DafnyUpdateUsageMetadataInput,
)
import aws_cryptographic_material_providers.internaldafny.generated.module_
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.errors import (
    _smithy_error_to_dafny_error,
)
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
import botocore.client
from smithy_dafny_standard_library.internaldafny.generated import Wrappers
from typing import Any, Dict


class IBranchKeyIdSupplier(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "GetBranchKeyId") and callable(subclass.GetBranchKeyId)

    @abc.abstractmethod
    def get_branch_key_id(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdOutput":
        """Given the Encryption Context associated with this encryption or
        decryption, returns the branch key that should be responsible for
        unwrapping or wrapping the data key.

        :param param: Inputs for determining the Branch Key which should
            be used to wrap or unwrap the data key for this encryption
            or decryption
        :returns: Outputs for the Branch Key responsible for wrapping or
            unwrapping the data key in this encryption or decryption.
        """
        raise NotImplementedError

    def GetBranchKeyId(
        self, dafny_input: "DafnyGetBranchKeyIdInput"
    ) -> "DafnyGetBranchKeyIdOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetBranchKeyIdInput(
            dafny_input
        )
        try:
            native_output = self.get_branch_key_id(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetBranchKeyIdOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class BranchKeyIdSupplier(IBranchKeyIdSupplier):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplier,
    ):
        self._impl = _impl

    def get_branch_key_id(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetBranchKeyIdOutput":
        """Given the Encryption Context associated with this encryption or
        decryption, returns the branch key that should be responsible for
        unwrapping or wrapping the data key.

        :param param: Inputs for determining the Branch Key which should
            be used to wrap or unwrap the data key for this encryption
            or decryption
        :returns: Outputs for the Branch Key responsible for wrapping or
            unwrapping the data key in this encryption or decryption.
        """
        dafny_output = self._impl.GetBranchKeyId(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetBranchKeyIdInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetBranchKeyIdOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BranchKeyIdSupplier":
        return BranchKeyIdSupplier(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}


class IClientSupplier(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "GetClient") and callable(subclass.GetClient)

    @abc.abstractmethod
    def get_client(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetClientInput",
    ) -> "botocore.client.BaseClient":
        """Returns an AWS KMS Client.

        :param param: Inputs for getting a AWS KMS Client.
        """
        raise NotImplementedError

    def GetClient(self, dafny_input: "DafnyGetClientInput") -> "DafnyGetClientOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetClientInput(
            dafny_input
        )
        try:
            native_output = self.get_client(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetClientOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class ClientSupplier(IClientSupplier):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IClientSupplier
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IClientSupplier,
    ):
        self._impl = _impl

    def get_client(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetClientInput",
    ) -> "botocore.client.BaseClient":
        """Returns an AWS KMS Client.

        :param param: Inputs for getting a AWS KMS Client.
        """
        dafny_output = self._impl.GetClient(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetClientInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetClientOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ClientSupplier":
        return ClientSupplier(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}


class ICryptographicMaterialsCache(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "PutCacheEntry")
            and callable(subclass.PutCacheEntry)
            and hasattr(subclass, "GetCacheEntry")
            and callable(subclass.GetCacheEntry)
            and hasattr(subclass, "UpdateUsageMetadata")
            and callable(subclass.UpdateUsageMetadata)
            and hasattr(subclass, "DeleteCacheEntry")
            and callable(subclass.DeleteCacheEntry)
        )

    @abc.abstractmethod
    def put_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.PutCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        raise NotImplementedError

    @abc.abstractmethod
    def get_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryOutput":
        raise NotImplementedError

    @abc.abstractmethod
    def update_usage_metadata(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.UpdateUsageMetadataInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        raise NotImplementedError

    @abc.abstractmethod
    def delete_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DeleteCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        raise NotImplementedError

    def PutCacheEntry(self, dafny_input: "DafnyPutCacheEntryInput") -> "None":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_PutCacheEntryInput(
            dafny_input
        )
        try:
            native_output = self.put_cache_entry(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.smithy_api_Unit(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def GetCacheEntry(
        self, dafny_input: "DafnyGetCacheEntryInput"
    ) -> "DafnyGetCacheEntryOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetCacheEntryInput(
            dafny_input
        )
        try:
            native_output = self.get_cache_entry(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetCacheEntryOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def UpdateUsageMetadata(
        self, dafny_input: "DafnyUpdateUsageMetadataInput"
    ) -> "None":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_UpdateUsageMetadataInput(
            dafny_input
        )
        try:
            native_output = self.update_usage_metadata(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.smithy_api_Unit(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def DeleteCacheEntry(self, dafny_input: "DafnyDeleteCacheEntryInput") -> "None":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DeleteCacheEntryInput(
            dafny_input
        )
        try:
            native_output = self.delete_cache_entry(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.smithy_api_Unit(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class CryptographicMaterialsCache(ICryptographicMaterialsCache):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache,
    ):
        self._impl = _impl

    def put_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.PutCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        dafny_output = self._impl.PutCacheEntry(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_PutCacheEntryInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as smithy_api_deserialize_error,
            )

            raise smithy_api_deserialize_error(dafny_output.error)

        else:
            return (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.smithy_api_Unit()
            )

    def get_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetCacheEntryOutput":
        dafny_output = self._impl.GetCacheEntry(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetCacheEntryInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetCacheEntryOutput(
                dafny_output.value
            )

    def update_usage_metadata(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.UpdateUsageMetadataInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        dafny_output = self._impl.UpdateUsageMetadata(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_UpdateUsageMetadataInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as smithy_api_deserialize_error,
            )

            raise smithy_api_deserialize_error(dafny_output.error)

        else:
            return (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.smithy_api_Unit()
            )

    def delete_cache_entry(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DeleteCacheEntryInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.Unit":
        dafny_output = self._impl.DeleteCacheEntry(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DeleteCacheEntryInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as smithy_api_deserialize_error,
            )

            raise smithy_api_deserialize_error(dafny_output.error)

        else:
            return (
                aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.smithy_api_Unit()
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CryptographicMaterialsCache":
        return CryptographicMaterialsCache(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}


class ICryptographicMaterialsManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "GetEncryptionMaterials")
            and callable(subclass.GetEncryptionMaterials)
            and hasattr(subclass, "DecryptMaterials")
            and callable(subclass.DecryptMaterials)
        )

    @abc.abstractmethod
    def get_encryption_materials(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsOutput":
        raise NotImplementedError

    @abc.abstractmethod
    def decrypt_materials(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsOutput":
        raise NotImplementedError

    def GetEncryptionMaterials(
        self, dafny_input: "DafnyGetEncryptionMaterialsInput"
    ) -> "DafnyGetEncryptionMaterialsOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetEncryptionMaterialsInput(
            dafny_input
        )
        try:
            native_output = self.get_encryption_materials(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def DecryptMaterials(
        self, dafny_input: "DafnyDecryptMaterialsInput"
    ) -> "DafnyDecryptMaterialsOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptMaterialsInput(
            dafny_input
        )
        try:
            native_output = self.decrypt_materials(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptMaterialsOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class CryptographicMaterialsManager(ICryptographicMaterialsManager):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager,
    ):
        self._impl = _impl

    def get_encryption_materials(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.GetEncryptionMaterialsOutput":
        dafny_output = self._impl.GetEncryptionMaterials(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_GetEncryptionMaterialsInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(
                dafny_output.value
            )

    def decrypt_materials(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.DecryptMaterialsOutput":
        dafny_output = self._impl.DecryptMaterials(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptMaterialsInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptMaterialsOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CryptographicMaterialsManager":
        return CryptographicMaterialsManager(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}


class IKeyring(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "OnEncrypt")
            and callable(subclass.OnEncrypt)
            and hasattr(subclass, "OnDecrypt")
            and callable(subclass.OnDecrypt)
        )

    @abc.abstractmethod
    def on_encrypt(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptOutput":
        raise NotImplementedError

    @abc.abstractmethod
    def on_decrypt(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptOutput":
        raise NotImplementedError

    def OnEncrypt(self, dafny_input: "DafnyOnEncryptInput") -> "DafnyOnEncryptOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_OnEncryptInput(
            dafny_input
        )
        try:
            native_output = self.on_encrypt(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_OnEncryptOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)

    def OnDecrypt(self, dafny_input: "DafnyOnDecryptInput") -> "DafnyOnDecryptOutput":
        """Do not use.

        This method allows custom implementations of this interface to
        interact with generated code.
        """
        native_input = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_OnDecryptInput(
            dafny_input
        )
        try:
            native_output = self.on_decrypt(native_input)
            dafny_output = aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_OnDecryptOutput(
                native_output
            )
            return Wrappers.Result_Success(dafny_output)
        except Exception as e:
            error = _smithy_error_to_dafny_error(e)
            return Wrappers.Result_Failure(error)


class Keyring(IKeyring):

    _impl: (
        aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IKeyring
    )

    def __init__(
        self,
        _impl: aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IKeyring,
    ):
        self._impl = _impl

    def on_encrypt(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnEncryptOutput":
        dafny_output = self._impl.OnEncrypt(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_OnEncryptInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_OnEncryptOutput(
                dafny_output.value
            )

    def on_decrypt(
        self,
        param: "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptInput",
    ) -> "aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.models.OnDecryptOutput":
        dafny_output = self._impl.OnDecrypt(
            aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_OnDecryptInput(
                param
            )
        )
        if dafny_output.IsFailure():
            from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.deserialize import (
                _deserialize_error as aws_cryptography_materialproviders_deserialize_error,
            )

            raise aws_cryptography_materialproviders_deserialize_error(
                dafny_output.error
            )

        else:
            return aws_cryptographic_material_providers.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_OnDecryptOutput(
                dafny_output.value
            )

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Keyring":
        return Keyring(d["_impl"])

    def as_dict(self) -> Dict[str, Any]:
        return {"_impl": self._impl}
