# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    CancelKeyDeletionRequest_CancelKeyDeletionRequest as DafnyCancelKeyDeletionRequest,
    CancelKeyDeletionResponse_CancelKeyDeletionResponse as DafnyCancelKeyDeletionResponse,
    ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest as DafnyConnectCustomKeyStoreRequest,
    ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse as DafnyConnectCustomKeyStoreResponse,
    CreateAliasRequest_CreateAliasRequest as DafnyCreateAliasRequest,
    CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest as DafnyCreateCustomKeyStoreRequest,
    CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse as DafnyCreateCustomKeyStoreResponse,
    CreateGrantRequest_CreateGrantRequest as DafnyCreateGrantRequest,
    CreateGrantResponse_CreateGrantResponse as DafnyCreateGrantResponse,
    CreateKeyRequest_CreateKeyRequest as DafnyCreateKeyRequest,
    CreateKeyResponse_CreateKeyResponse as DafnyCreateKeyResponse,
    DecryptRequest_DecryptRequest as DafnyDecryptRequest,
    DecryptResponse_DecryptResponse as DafnyDecryptResponse,
    DeleteAliasRequest_DeleteAliasRequest as DafnyDeleteAliasRequest,
    DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest as DafnyDeleteCustomKeyStoreRequest,
    DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse as DafnyDeleteCustomKeyStoreResponse,
    DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest as DafnyDeleteImportedKeyMaterialRequest,
    DeriveSharedSecretRequest_DeriveSharedSecretRequest as DafnyDeriveSharedSecretRequest,
    DeriveSharedSecretResponse_DeriveSharedSecretResponse as DafnyDeriveSharedSecretResponse,
    DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest as DafnyDescribeCustomKeyStoresRequest,
    DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse as DafnyDescribeCustomKeyStoresResponse,
    DescribeKeyRequest_DescribeKeyRequest as DafnyDescribeKeyRequest,
    DescribeKeyResponse_DescribeKeyResponse as DafnyDescribeKeyResponse,
    DisableKeyRequest_DisableKeyRequest as DafnyDisableKeyRequest,
    DisableKeyRotationRequest_DisableKeyRotationRequest as DafnyDisableKeyRotationRequest,
    DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest as DafnyDisconnectCustomKeyStoreRequest,
    DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse as DafnyDisconnectCustomKeyStoreResponse,
    EnableKeyRequest_EnableKeyRequest as DafnyEnableKeyRequest,
    EnableKeyRotationRequest_EnableKeyRotationRequest as DafnyEnableKeyRotationRequest,
    EncryptRequest_EncryptRequest as DafnyEncryptRequest,
    EncryptResponse_EncryptResponse as DafnyEncryptResponse,
    GenerateDataKeyPairRequest_GenerateDataKeyPairRequest as DafnyGenerateDataKeyPairRequest,
    GenerateDataKeyPairResponse_GenerateDataKeyPairResponse as DafnyGenerateDataKeyPairResponse,
    GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest as DafnyGenerateDataKeyPairWithoutPlaintextRequest,
    GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse as DafnyGenerateDataKeyPairWithoutPlaintextResponse,
    GenerateDataKeyRequest_GenerateDataKeyRequest as DafnyGenerateDataKeyRequest,
    GenerateDataKeyResponse_GenerateDataKeyResponse as DafnyGenerateDataKeyResponse,
    GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest as DafnyGenerateDataKeyWithoutPlaintextRequest,
    GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse as DafnyGenerateDataKeyWithoutPlaintextResponse,
    GenerateMacRequest_GenerateMacRequest as DafnyGenerateMacRequest,
    GenerateMacResponse_GenerateMacResponse as DafnyGenerateMacResponse,
    GenerateRandomRequest_GenerateRandomRequest as DafnyGenerateRandomRequest,
    GenerateRandomResponse_GenerateRandomResponse as DafnyGenerateRandomResponse,
    GetKeyPolicyRequest_GetKeyPolicyRequest as DafnyGetKeyPolicyRequest,
    GetKeyPolicyResponse_GetKeyPolicyResponse as DafnyGetKeyPolicyResponse,
    GetKeyRotationStatusRequest_GetKeyRotationStatusRequest as DafnyGetKeyRotationStatusRequest,
    GetKeyRotationStatusResponse_GetKeyRotationStatusResponse as DafnyGetKeyRotationStatusResponse,
    GetParametersForImportRequest_GetParametersForImportRequest as DafnyGetParametersForImportRequest,
    GetParametersForImportResponse_GetParametersForImportResponse as DafnyGetParametersForImportResponse,
    GetPublicKeyRequest_GetPublicKeyRequest as DafnyGetPublicKeyRequest,
    GetPublicKeyResponse_GetPublicKeyResponse as DafnyGetPublicKeyResponse,
    ImportKeyMaterialRequest_ImportKeyMaterialRequest as DafnyImportKeyMaterialRequest,
    ImportKeyMaterialResponse_ImportKeyMaterialResponse as DafnyImportKeyMaterialResponse,
    ListAliasesRequest_ListAliasesRequest as DafnyListAliasesRequest,
    ListAliasesResponse_ListAliasesResponse as DafnyListAliasesResponse,
    ListGrantsRequest_ListGrantsRequest as DafnyListGrantsRequest,
    ListGrantsResponse_ListGrantsResponse as DafnyListGrantsResponse,
    ListKeyPoliciesRequest_ListKeyPoliciesRequest as DafnyListKeyPoliciesRequest,
    ListKeyPoliciesResponse_ListKeyPoliciesResponse as DafnyListKeyPoliciesResponse,
    ListKeyRotationsRequest_ListKeyRotationsRequest as DafnyListKeyRotationsRequest,
    ListKeyRotationsResponse_ListKeyRotationsResponse as DafnyListKeyRotationsResponse,
    ListKeysRequest_ListKeysRequest as DafnyListKeysRequest,
    ListKeysResponse_ListKeysResponse as DafnyListKeysResponse,
    ListResourceTagsRequest_ListResourceTagsRequest as DafnyListResourceTagsRequest,
    ListResourceTagsResponse_ListResourceTagsResponse as DafnyListResourceTagsResponse,
    PutKeyPolicyRequest_PutKeyPolicyRequest as DafnyPutKeyPolicyRequest,
    ReEncryptRequest_ReEncryptRequest as DafnyReEncryptRequest,
    ReEncryptResponse_ReEncryptResponse as DafnyReEncryptResponse,
    ReplicateKeyRequest_ReplicateKeyRequest as DafnyReplicateKeyRequest,
    ReplicateKeyResponse_ReplicateKeyResponse as DafnyReplicateKeyResponse,
    RetireGrantRequest_RetireGrantRequest as DafnyRetireGrantRequest,
    RevokeGrantRequest_RevokeGrantRequest as DafnyRevokeGrantRequest,
    RotateKeyOnDemandRequest_RotateKeyOnDemandRequest as DafnyRotateKeyOnDemandRequest,
    RotateKeyOnDemandResponse_RotateKeyOnDemandResponse as DafnyRotateKeyOnDemandResponse,
    ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest as DafnyScheduleKeyDeletionRequest,
    ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse as DafnyScheduleKeyDeletionResponse,
    SignRequest_SignRequest as DafnySignRequest,
    SignResponse_SignResponse as DafnySignResponse,
    TagResourceRequest_TagResourceRequest as DafnyTagResourceRequest,
    UntagResourceRequest_UntagResourceRequest as DafnyUntagResourceRequest,
    UpdateAliasRequest_UpdateAliasRequest as DafnyUpdateAliasRequest,
    UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest as DafnyUpdateCustomKeyStoreRequest,
    UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse as DafnyUpdateCustomKeyStoreResponse,
    UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest as DafnyUpdateKeyDescriptionRequest,
    UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest as DafnyUpdatePrimaryRegionRequest,
    VerifyMacRequest_VerifyMacRequest as DafnyVerifyMacRequest,
    VerifyMacResponse_VerifyMacResponse as DafnyVerifyMacResponse,
    VerifyRequest_VerifyRequest as DafnyVerifyRequest,
    VerifyResponse_VerifyResponse as DafnyVerifyResponse,
)
import aws_cryptography_internal_kms.internaldafny.generated.module_
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk

from . import dafny_to_aws_sdk


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from botocore.exceptions import ClientError
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes


def _sdk_error_to_dafny_error(e: ClientError):
    """Converts the provided native Smithy-modelled error into the
    corresponding Dafny error."""
    if e.response["Error"]["Code"] == "AlreadyExistsException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_AlreadyExistsException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CloudHsmClusterInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CloudHsmClusterInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CloudHsmClusterInvalidConfigurationException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CloudHsmClusterInvalidConfigurationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CloudHsmClusterNotActiveException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CloudHsmClusterNotActiveException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CloudHsmClusterNotFoundException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CloudHsmClusterNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CloudHsmClusterNotRelatedException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CloudHsmClusterNotRelatedException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ConflictException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConflictException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CustomKeyStoreHasCMKsException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreHasCMKsException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CustomKeyStoreInvalidStateException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreInvalidStateException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CustomKeyStoreNameInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreNameInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "CustomKeyStoreNotFoundException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "DependencyTimeoutException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DependencyTimeoutException(
            e.response
        )

    elif e.response["Error"]["Code"] == "DisabledException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DisabledException(
            e.response
        )

    elif e.response["Error"]["Code"] == "DryRunOperationException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DryRunOperationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ExpiredImportTokenException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ExpiredImportTokenException(
            e.response
        )

    elif e.response["Error"]["Code"] == "IncorrectKeyException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_IncorrectKeyException(
            e.response
        )

    elif e.response["Error"]["Code"] == "IncorrectKeyMaterialException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_IncorrectKeyMaterialException(
            e.response
        )

    elif e.response["Error"]["Code"] == "IncorrectTrustAnchorException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_IncorrectTrustAnchorException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidAliasNameException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidAliasNameException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidArnException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidArnException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidCiphertextException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidCiphertextException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidGrantIdException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidGrantIdException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidGrantTokenException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidGrantTokenException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidImportTokenException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidImportTokenException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidKeyUsageException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidKeyUsageException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidMarkerException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_InvalidMarkerException(
            e.response
        )

    elif e.response["Error"]["Code"] == "KeyUnavailableException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUnavailableException(
            e.response
        )

    elif e.response["Error"]["Code"] == "KMSInternalException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KMSInternalException(
            e.response
        )

    elif e.response["Error"]["Code"] == "KMSInvalidMacException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KMSInvalidMacException(
            e.response
        )

    elif e.response["Error"]["Code"] == "KMSInvalidSignatureException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KMSInvalidSignatureException(
            e.response
        )

    elif e.response["Error"]["Code"] == "KMSInvalidStateException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KMSInvalidStateException(
            e.response
        )

    elif e.response["Error"]["Code"] == "LimitExceededException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_LimitExceededException(
            e.response
        )

    elif e.response["Error"]["Code"] == "MalformedPolicyDocumentException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MalformedPolicyDocumentException(
            e.response
        )

    elif e.response["Error"]["Code"] == "NotFoundException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_NotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TagException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_TagException(
            e.response
        )

    elif e.response["Error"]["Code"] == "UnsupportedOperationException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_UnsupportedOperationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksKeyAlreadyInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksKeyAlreadyInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksKeyInvalidConfigurationException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksKeyInvalidConfigurationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksKeyNotFoundException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksKeyNotFoundException(
            e.response
        )

    elif (
        e.response["Error"]["Code"]
        == "XksProxyIncorrectAuthenticationCredentialException"
    ):
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyIncorrectAuthenticationCredentialException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyInvalidConfigurationException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyInvalidConfigurationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyInvalidResponseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyInvalidResponseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyUriEndpointInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyUriEndpointInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyUriInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyUriInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyUriUnreachableException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyUriUnreachableException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyVpcEndpointServiceInUseException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyVpcEndpointServiceInUseException(
            e.response
        )

    elif (
        e.response["Error"]["Code"]
        == "XksProxyVpcEndpointServiceInvalidConfigurationException"
    ):
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyVpcEndpointServiceInvalidConfigurationException(
            e.response
        )

    elif e.response["Error"]["Code"] == "XksProxyVpcEndpointServiceNotFoundException":
        return aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyVpcEndpointServiceNotFoundException(
            e.response
        )

    return aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes.Error_Opaque(
        obj=e,
        alt__text=_dafny.Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(*[iter(repr(e).encode("utf-16-be"))] * 2)
                ]
            )
        ),
    )


class KMSClientShim:
    def __init__(self, _impl, _region):
        self._impl = _impl
        self._region = _region

    def CancelKeyDeletion(
        self, input: DafnyCancelKeyDeletionRequest
    ) -> DafnyCancelKeyDeletionResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CancelKeyDeletionRequest(
            input
        )
        try:
            boto_response_dict = self._impl.cancel_key_deletion(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CancelKeyDeletionResponse(
                boto_response_dict
            )
        )

    def ConnectCustomKeyStore(
        self, input: DafnyConnectCustomKeyStoreRequest
    ) -> DafnyConnectCustomKeyStoreResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ConnectCustomKeyStoreRequest(
            input
        )
        try:
            boto_response_dict = self._impl.connect_custom_key_store(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConnectCustomKeyStoreResponse(
                boto_response_dict
            )
        )

    def CreateAlias(self, input: DafnyCreateAliasRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CreateAliasRequest(
            input
        )
        try:
            boto_response_dict = self._impl.create_alias(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def CreateCustomKeyStore(
        self, input: DafnyCreateCustomKeyStoreRequest
    ) -> DafnyCreateCustomKeyStoreResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CreateCustomKeyStoreRequest(
            input
        )
        try:
            boto_response_dict = self._impl.create_custom_key_store(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CreateCustomKeyStoreResponse(
                boto_response_dict
            )
        )

    def CreateGrant(self, input: DafnyCreateGrantRequest) -> DafnyCreateGrantResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CreateGrantRequest(
            input
        )
        try:
            boto_response_dict = self._impl.create_grant(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CreateGrantResponse(
                boto_response_dict
            )
        )

    def CreateKey(self, input: DafnyCreateKeyRequest) -> DafnyCreateKeyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CreateKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.create_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CreateKeyResponse(
                boto_response_dict
            )
        )

    def Decrypt(self, input: DafnyDecryptRequest) -> DafnyDecryptResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DecryptRequest(
            input
        )
        try:
            boto_response_dict = self._impl.decrypt(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DecryptResponse(
                boto_response_dict
            )
        )

    def DeleteAlias(self, input: DafnyDeleteAliasRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DeleteAliasRequest(
            input
        )
        try:
            boto_response_dict = self._impl.delete_alias(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DeleteCustomKeyStore(
        self, input: DafnyDeleteCustomKeyStoreRequest
    ) -> DafnyDeleteCustomKeyStoreResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DeleteCustomKeyStoreRequest(
            input
        )
        try:
            boto_response_dict = self._impl.delete_custom_key_store(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DeleteCustomKeyStoreResponse(
                boto_response_dict
            )
        )

    def DeleteImportedKeyMaterial(
        self, input: DafnyDeleteImportedKeyMaterialRequest
    ) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DeleteImportedKeyMaterialRequest(
            input
        )
        try:
            boto_response_dict = self._impl.delete_imported_key_material(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DeriveSharedSecret(
        self, input: DafnyDeriveSharedSecretRequest
    ) -> DafnyDeriveSharedSecretResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DeriveSharedSecretRequest(
            input
        )
        try:
            boto_response_dict = self._impl.derive_shared_secret(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DeriveSharedSecretResponse(
                boto_response_dict
            )
        )

    def DescribeCustomKeyStores(
        self, input: DafnyDescribeCustomKeyStoresRequest
    ) -> DafnyDescribeCustomKeyStoresResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DescribeCustomKeyStoresRequest(
            input
        )
        try:
            boto_response_dict = self._impl.describe_custom_key_stores(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DescribeCustomKeyStoresResponse(
                boto_response_dict
            )
        )

    def DescribeKey(self, input: DafnyDescribeKeyRequest) -> DafnyDescribeKeyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DescribeKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.describe_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DescribeKeyResponse(
                boto_response_dict
            )
        )

    def DisableKey(self, input: DafnyDisableKeyRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DisableKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.disable_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DisableKeyRotation(self, input: DafnyDisableKeyRotationRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DisableKeyRotationRequest(
            input
        )
        try:
            boto_response_dict = self._impl.disable_key_rotation(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DisconnectCustomKeyStore(
        self, input: DafnyDisconnectCustomKeyStoreRequest
    ) -> DafnyDisconnectCustomKeyStoreResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DisconnectCustomKeyStoreRequest(
            input
        )
        try:
            boto_response_dict = self._impl.disconnect_custom_key_store(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DisconnectCustomKeyStoreResponse(
                boto_response_dict
            )
        )

    def EnableKey(self, input: DafnyEnableKeyRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EnableKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.enable_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def EnableKeyRotation(self, input: DafnyEnableKeyRotationRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EnableKeyRotationRequest(
            input
        )
        try:
            boto_response_dict = self._impl.enable_key_rotation(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def Encrypt(self, input: DafnyEncryptRequest) -> DafnyEncryptResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptRequest(
            input
        )
        try:
            boto_response_dict = self._impl.encrypt(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptResponse(
                boto_response_dict
            )
        )

    def GenerateDataKey(
        self, input: DafnyGenerateDataKeyRequest
    ) -> DafnyGenerateDataKeyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateDataKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_data_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateDataKeyResponse(
                boto_response_dict
            )
        )

    def GenerateDataKeyPair(
        self, input: DafnyGenerateDataKeyPairRequest
    ) -> DafnyGenerateDataKeyPairResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateDataKeyPairRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_data_key_pair(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateDataKeyPairResponse(
                boto_response_dict
            )
        )

    def GenerateDataKeyPairWithoutPlaintext(
        self, input: DafnyGenerateDataKeyPairWithoutPlaintextRequest
    ) -> DafnyGenerateDataKeyPairWithoutPlaintextResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_data_key_pair_without_plaintext(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextResponse(
                boto_response_dict
            )
        )

    def GenerateDataKeyWithoutPlaintext(
        self, input: DafnyGenerateDataKeyWithoutPlaintextRequest
    ) -> DafnyGenerateDataKeyWithoutPlaintextResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateDataKeyWithoutPlaintextRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_data_key_without_plaintext(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateDataKeyWithoutPlaintextResponse(
                boto_response_dict
            )
        )

    def GenerateMac(self, input: DafnyGenerateMacRequest) -> DafnyGenerateMacResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateMacRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_mac(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateMacResponse(
                boto_response_dict
            )
        )

    def GenerateRandom(
        self, input: DafnyGenerateRandomRequest
    ) -> DafnyGenerateRandomResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GenerateRandomRequest(
            input
        )
        try:
            boto_response_dict = self._impl.generate_random(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GenerateRandomResponse(
                boto_response_dict
            )
        )

    def GetKeyPolicy(
        self, input: DafnyGetKeyPolicyRequest
    ) -> DafnyGetKeyPolicyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GetKeyPolicyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.get_key_policy(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GetKeyPolicyResponse(
                boto_response_dict
            )
        )

    def GetKeyRotationStatus(
        self, input: DafnyGetKeyRotationStatusRequest
    ) -> DafnyGetKeyRotationStatusResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GetKeyRotationStatusRequest(
            input
        )
        try:
            boto_response_dict = self._impl.get_key_rotation_status(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GetKeyRotationStatusResponse(
                boto_response_dict
            )
        )

    def GetParametersForImport(
        self, input: DafnyGetParametersForImportRequest
    ) -> DafnyGetParametersForImportResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GetParametersForImportRequest(
            input
        )
        try:
            boto_response_dict = self._impl.get_parameters_for_import(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GetParametersForImportResponse(
                boto_response_dict
            )
        )

    def GetPublicKey(
        self, input: DafnyGetPublicKeyRequest
    ) -> DafnyGetPublicKeyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GetPublicKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.get_public_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GetPublicKeyResponse(
                boto_response_dict
            )
        )

    def ImportKeyMaterial(
        self, input: DafnyImportKeyMaterialRequest
    ) -> DafnyImportKeyMaterialResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ImportKeyMaterialRequest(
            input
        )
        try:
            boto_response_dict = self._impl.import_key_material(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ImportKeyMaterialResponse(
                boto_response_dict
            )
        )

    def ListAliases(self, input: DafnyListAliasesRequest) -> DafnyListAliasesResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListAliasesRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_aliases(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListAliasesResponse(
                boto_response_dict
            )
        )

    def ListGrants(self, input: DafnyListGrantsRequest) -> DafnyListGrantsResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListGrantsRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_grants(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListGrantsResponse(
                boto_response_dict
            )
        )

    def ListKeyPolicies(
        self, input: DafnyListKeyPoliciesRequest
    ) -> DafnyListKeyPoliciesResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListKeyPoliciesRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_key_policies(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListKeyPoliciesResponse(
                boto_response_dict
            )
        )

    def ListKeyRotations(
        self, input: DafnyListKeyRotationsRequest
    ) -> DafnyListKeyRotationsResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListKeyRotationsRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_key_rotations(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListKeyRotationsResponse(
                boto_response_dict
            )
        )

    def ListKeys(self, input: DafnyListKeysRequest) -> DafnyListKeysResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListKeysRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_keys(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListKeysResponse(
                boto_response_dict
            )
        )

    def ListResourceTags(
        self, input: DafnyListResourceTagsRequest
    ) -> DafnyListResourceTagsResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ListResourceTagsRequest(
            input
        )
        try:
            boto_response_dict = self._impl.list_resource_tags(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ListResourceTagsResponse(
                boto_response_dict
            )
        )

    def PutKeyPolicy(self, input: DafnyPutKeyPolicyRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_PutKeyPolicyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.put_key_policy(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ReEncrypt(self, input: DafnyReEncryptRequest) -> DafnyReEncryptResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ReEncryptRequest(
            input
        )
        try:
            boto_response_dict = self._impl.re_encrypt(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ReEncryptResponse(
                boto_response_dict
            )
        )

    def ReplicateKey(
        self, input: DafnyReplicateKeyRequest
    ) -> DafnyReplicateKeyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ReplicateKeyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.replicate_key(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ReplicateKeyResponse(
                boto_response_dict
            )
        )

    def RetireGrant(self, input: DafnyRetireGrantRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RetireGrantRequest(
            input
        )
        try:
            boto_response_dict = self._impl.retire_grant(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def RevokeGrant(self, input: DafnyRevokeGrantRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RevokeGrantRequest(
            input
        )
        try:
            boto_response_dict = self._impl.revoke_grant(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def RotateKeyOnDemand(
        self, input: DafnyRotateKeyOnDemandRequest
    ) -> DafnyRotateKeyOnDemandResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RotateKeyOnDemandRequest(
            input
        )
        try:
            boto_response_dict = self._impl.rotate_key_on_demand(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RotateKeyOnDemandResponse(
                boto_response_dict
            )
        )

    def ScheduleKeyDeletion(
        self, input: DafnyScheduleKeyDeletionRequest
    ) -> DafnyScheduleKeyDeletionResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ScheduleKeyDeletionRequest(
            input
        )
        try:
            boto_response_dict = self._impl.schedule_key_deletion(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ScheduleKeyDeletionResponse(
                boto_response_dict
            )
        )

    def Sign(self, input: DafnySignRequest) -> DafnySignResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SignRequest(
            input
        )
        try:
            boto_response_dict = self._impl.sign(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SignResponse(
                boto_response_dict
            )
        )

    def TagResource(self, input: DafnyTagResourceRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_TagResourceRequest(
            input
        )
        try:
            boto_response_dict = self._impl.tag_resource(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def UntagResource(self, input: DafnyUntagResourceRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_UntagResourceRequest(
            input
        )
        try:
            boto_response_dict = self._impl.untag_resource(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def UpdateAlias(self, input: DafnyUpdateAliasRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_UpdateAliasRequest(
            input
        )
        try:
            boto_response_dict = self._impl.update_alias(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def UpdateCustomKeyStore(
        self, input: DafnyUpdateCustomKeyStoreRequest
    ) -> DafnyUpdateCustomKeyStoreResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_UpdateCustomKeyStoreRequest(
            input
        )
        try:
            boto_response_dict = self._impl.update_custom_key_store(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_UpdateCustomKeyStoreResponse(
                boto_response_dict
            )
        )

    def UpdateKeyDescription(self, input: DafnyUpdateKeyDescriptionRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_UpdateKeyDescriptionRequest(
            input
        )
        try:
            boto_response_dict = self._impl.update_key_description(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def UpdatePrimaryRegion(self, input: DafnyUpdatePrimaryRegionRequest) -> None:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_UpdatePrimaryRegionRequest(
            input
        )
        try:
            boto_response_dict = self._impl.update_primary_region(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def Verify(self, input: DafnyVerifyRequest) -> DafnyVerifyResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_VerifyRequest(
            input
        )
        try:
            boto_response_dict = self._impl.verify(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_VerifyResponse(
                boto_response_dict
            )
        )

    def VerifyMac(self, input: DafnyVerifyMacRequest) -> DafnyVerifyMacResponse:
        boto_request_dict = aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_VerifyMacRequest(
            input
        )
        try:
            boto_response_dict = self._impl.verify_mac(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_VerifyMacResponse(
                boto_response_dict
            )
        )
