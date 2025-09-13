# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from _dafny import Map, Seq
from aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    AlgorithmSpec_RSAES__OAEP__SHA__1,
    AlgorithmSpec_RSAES__OAEP__SHA__256,
    AlgorithmSpec_RSAES__PKCS1__V1__5,
    AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1,
    AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256,
    AlgorithmSpec_SM2PKE,
    AliasListEntry_AliasListEntry as DafnyAliasListEntry,
    CancelKeyDeletionRequest_CancelKeyDeletionRequest as DafnyCancelKeyDeletionRequest,
    CancelKeyDeletionResponse_CancelKeyDeletionResponse as DafnyCancelKeyDeletionResponse,
    ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest as DafnyConnectCustomKeyStoreRequest,
    ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse as DafnyConnectCustomKeyStoreResponse,
    ConnectionErrorCodeType_CLUSTER__NOT__FOUND,
    ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS,
    ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET,
    ConnectionErrorCodeType_INTERNAL__ERROR,
    ConnectionErrorCodeType_INVALID__CREDENTIALS,
    ConnectionErrorCodeType_NETWORK__ERRORS,
    ConnectionErrorCodeType_SUBNET__NOT__FOUND,
    ConnectionErrorCodeType_USER__LOCKED__OUT,
    ConnectionErrorCodeType_USER__LOGGED__IN,
    ConnectionErrorCodeType_USER__NOT__FOUND,
    ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED,
    ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION,
    ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE,
    ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION,
    ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE,
    ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT,
    ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION,
    ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND,
    ConnectionStateType_CONNECTED,
    ConnectionStateType_CONNECTING,
    ConnectionStateType_DISCONNECTED,
    ConnectionStateType_DISCONNECTING,
    ConnectionStateType_FAILED,
    CreateAliasRequest_CreateAliasRequest as DafnyCreateAliasRequest,
    CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest as DafnyCreateCustomKeyStoreRequest,
    CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse as DafnyCreateCustomKeyStoreResponse,
    CreateGrantRequest_CreateGrantRequest as DafnyCreateGrantRequest,
    CreateGrantResponse_CreateGrantResponse as DafnyCreateGrantResponse,
    CreateKeyRequest_CreateKeyRequest as DafnyCreateKeyRequest,
    CreateKeyResponse_CreateKeyResponse as DafnyCreateKeyResponse,
    CustomKeyStoreType_AWS__CLOUDHSM,
    CustomKeyStoreType_EXTERNAL__KEY__STORE,
    CustomKeyStoresListEntry_CustomKeyStoresListEntry as DafnyCustomKeyStoresListEntry,
    CustomerMasterKeySpec_ECC__NIST__P256,
    CustomerMasterKeySpec_ECC__NIST__P384,
    CustomerMasterKeySpec_ECC__NIST__P521,
    CustomerMasterKeySpec_ECC__SECG__P256K1,
    CustomerMasterKeySpec_HMAC__224,
    CustomerMasterKeySpec_HMAC__256,
    CustomerMasterKeySpec_HMAC__384,
    CustomerMasterKeySpec_HMAC__512,
    CustomerMasterKeySpec_RSA__2048,
    CustomerMasterKeySpec_RSA__3072,
    CustomerMasterKeySpec_RSA__4096,
    CustomerMasterKeySpec_SM2,
    CustomerMasterKeySpec_SYMMETRIC__DEFAULT,
    DataKeyPairSpec_ECC__NIST__P256,
    DataKeyPairSpec_ECC__NIST__P384,
    DataKeyPairSpec_ECC__NIST__P521,
    DataKeyPairSpec_ECC__SECG__P256K1,
    DataKeyPairSpec_RSA__2048,
    DataKeyPairSpec_RSA__3072,
    DataKeyPairSpec_RSA__4096,
    DataKeyPairSpec_SM2,
    DataKeySpec_AES__128,
    DataKeySpec_AES__256,
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
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256,
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT,
    Error_AlreadyExistsException,
    Error_CloudHsmClusterInUseException,
    Error_CloudHsmClusterInvalidConfigurationException,
    Error_CloudHsmClusterNotActiveException,
    Error_CloudHsmClusterNotFoundException,
    Error_CloudHsmClusterNotRelatedException,
    Error_ConflictException,
    Error_CustomKeyStoreHasCMKsException,
    Error_CustomKeyStoreInvalidStateException,
    Error_CustomKeyStoreNameInUseException,
    Error_CustomKeyStoreNotFoundException,
    Error_DependencyTimeoutException,
    Error_DisabledException,
    Error_DryRunOperationException,
    Error_ExpiredImportTokenException,
    Error_IncorrectKeyException,
    Error_IncorrectKeyMaterialException,
    Error_IncorrectTrustAnchorException,
    Error_InvalidAliasNameException,
    Error_InvalidArnException,
    Error_InvalidCiphertextException,
    Error_InvalidGrantIdException,
    Error_InvalidGrantTokenException,
    Error_InvalidImportTokenException,
    Error_InvalidKeyUsageException,
    Error_InvalidMarkerException,
    Error_KMSInternalException,
    Error_KMSInvalidMacException,
    Error_KMSInvalidSignatureException,
    Error_KMSInvalidStateException,
    Error_KeyUnavailableException,
    Error_LimitExceededException,
    Error_MalformedPolicyDocumentException,
    Error_NotFoundException,
    Error_TagException,
    Error_UnsupportedOperationException,
    Error_XksKeyAlreadyInUseException,
    Error_XksKeyInvalidConfigurationException,
    Error_XksKeyNotFoundException,
    Error_XksProxyIncorrectAuthenticationCredentialException,
    Error_XksProxyInvalidConfigurationException,
    Error_XksProxyInvalidResponseException,
    Error_XksProxyUriEndpointInUseException,
    Error_XksProxyUriInUseException,
    Error_XksProxyUriUnreachableException,
    Error_XksProxyVpcEndpointServiceInUseException,
    Error_XksProxyVpcEndpointServiceInvalidConfigurationException,
    Error_XksProxyVpcEndpointServiceNotFoundException,
    ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE,
    ExpirationModelType_KEY__MATERIAL__EXPIRES,
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
    GrantConstraints_GrantConstraints as DafnyGrantConstraints,
    GrantListEntry_GrantListEntry as DafnyGrantListEntry,
    GrantOperation_CreateGrant,
    GrantOperation_Decrypt,
    GrantOperation_DeriveSharedSecret,
    GrantOperation_DescribeKey,
    GrantOperation_Encrypt,
    GrantOperation_GenerateDataKey,
    GrantOperation_GenerateDataKeyPair,
    GrantOperation_GenerateDataKeyPairWithoutPlaintext,
    GrantOperation_GenerateDataKeyWithoutPlaintext,
    GrantOperation_GenerateMac,
    GrantOperation_GetPublicKey,
    GrantOperation_ReEncryptFrom,
    GrantOperation_ReEncryptTo,
    GrantOperation_RetireGrant,
    GrantOperation_Sign,
    GrantOperation_Verify,
    GrantOperation_VerifyMac,
    ImportKeyMaterialRequest_ImportKeyMaterialRequest as DafnyImportKeyMaterialRequest,
    ImportKeyMaterialResponse_ImportKeyMaterialResponse as DafnyImportKeyMaterialResponse,
    KeyAgreementAlgorithmSpec_ECDH,
    KeyEncryptionMechanism_RSAES__OAEP__SHA__256,
    KeyListEntry_KeyListEntry as DafnyKeyListEntry,
    KeyManagerType_AWS,
    KeyManagerType_CUSTOMER,
    KeyMetadata_KeyMetadata as DafnyKeyMetadata,
    KeySpec_ECC__NIST__P256,
    KeySpec_ECC__NIST__P384,
    KeySpec_ECC__NIST__P521,
    KeySpec_ECC__SECG__P256K1,
    KeySpec_HMAC__224,
    KeySpec_HMAC__256,
    KeySpec_HMAC__384,
    KeySpec_HMAC__512,
    KeySpec_RSA__2048,
    KeySpec_RSA__3072,
    KeySpec_RSA__4096,
    KeySpec_SM2,
    KeySpec_SYMMETRIC__DEFAULT,
    KeyState_Creating,
    KeyState_Disabled,
    KeyState_Enabled,
    KeyState_PendingDeletion,
    KeyState_PendingImport,
    KeyState_PendingReplicaDeletion,
    KeyState_Unavailable,
    KeyState_Updating,
    KeyUsageType_ENCRYPT__DECRYPT,
    KeyUsageType_GENERATE__VERIFY__MAC,
    KeyUsageType_KEY__AGREEMENT,
    KeyUsageType_SIGN__VERIFY,
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
    MacAlgorithmSpec_HMAC__SHA__224,
    MacAlgorithmSpec_HMAC__SHA__256,
    MacAlgorithmSpec_HMAC__SHA__384,
    MacAlgorithmSpec_HMAC__SHA__512,
    MessageType_DIGEST,
    MessageType_RAW,
    MultiRegionConfiguration_MultiRegionConfiguration as DafnyMultiRegionConfiguration,
    MultiRegionKeyType_PRIMARY,
    MultiRegionKeyType_REPLICA,
    MultiRegionKey_MultiRegionKey as DafnyMultiRegionKey,
    OriginType_AWS__CLOUDHSM,
    OriginType_AWS__KMS,
    OriginType_EXTERNAL,
    OriginType_EXTERNAL__KEY__STORE,
    PutKeyPolicyRequest_PutKeyPolicyRequest as DafnyPutKeyPolicyRequest,
    ReEncryptRequest_ReEncryptRequest as DafnyReEncryptRequest,
    ReEncryptResponse_ReEncryptResponse as DafnyReEncryptResponse,
    RecipientInfo_RecipientInfo as DafnyRecipientInfo,
    ReplicateKeyRequest_ReplicateKeyRequest as DafnyReplicateKeyRequest,
    ReplicateKeyResponse_ReplicateKeyResponse as DafnyReplicateKeyResponse,
    RetireGrantRequest_RetireGrantRequest as DafnyRetireGrantRequest,
    RevokeGrantRequest_RevokeGrantRequest as DafnyRevokeGrantRequest,
    RotateKeyOnDemandRequest_RotateKeyOnDemandRequest as DafnyRotateKeyOnDemandRequest,
    RotateKeyOnDemandResponse_RotateKeyOnDemandResponse as DafnyRotateKeyOnDemandResponse,
    RotationType_AUTOMATIC,
    RotationType_ON__DEMAND,
    RotationsListEntry_RotationsListEntry as DafnyRotationsListEntry,
    ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest as DafnyScheduleKeyDeletionRequest,
    ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse as DafnyScheduleKeyDeletionResponse,
    SignRequest_SignRequest as DafnySignRequest,
    SignResponse_SignResponse as DafnySignResponse,
    SigningAlgorithmSpec_ECDSA__SHA__256,
    SigningAlgorithmSpec_ECDSA__SHA__384,
    SigningAlgorithmSpec_ECDSA__SHA__512,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__256,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__384,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__512,
    SigningAlgorithmSpec_SM2DSA,
    TagResourceRequest_TagResourceRequest as DafnyTagResourceRequest,
    Tag_Tag as DafnyTag,
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
    WrappingKeySpec_RSA__2048,
    WrappingKeySpec_RSA__3072,
    WrappingKeySpec_RSA__4096,
    WrappingKeySpec_SM2,
    XksKeyConfigurationType_XksKeyConfigurationType as DafnyXksKeyConfigurationType,
    XksProxyAuthenticationCredentialType_XksProxyAuthenticationCredentialType as DafnyXksProxyAuthenticationCredentialType,
    XksProxyConfigurationType_XksProxyConfigurationType as DafnyXksProxyConfigurationType,
    XksProxyConnectivityType_PUBLIC__ENDPOINT,
    XksProxyConnectivityType_VPC__ENDPOINT__SERVICE,
)
import aws_cryptography_internal_kms.internaldafny.generated.module_
import aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def com_amazonaws_kms_AlreadyExistsException(native_input):
    return Error_AlreadyExistsException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CloudHsmClusterInUseException(native_input):
    return Error_CloudHsmClusterInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CloudHsmClusterInvalidConfigurationException(native_input):
    return Error_CloudHsmClusterInvalidConfigurationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CloudHsmClusterNotActiveException(native_input):
    return Error_CloudHsmClusterNotActiveException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CloudHsmClusterNotFoundException(native_input):
    return Error_CloudHsmClusterNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CloudHsmClusterNotRelatedException(native_input):
    return Error_CloudHsmClusterNotRelatedException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_ConflictException(native_input):
    return Error_ConflictException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CustomKeyStoreHasCMKsException(native_input):
    return Error_CustomKeyStoreHasCMKsException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CustomKeyStoreInvalidStateException(native_input):
    return Error_CustomKeyStoreInvalidStateException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CustomKeyStoreNameInUseException(native_input):
    return Error_CustomKeyStoreNameInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CustomKeyStoreNotFoundException(native_input):
    return Error_CustomKeyStoreNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DependencyTimeoutException(native_input):
    return Error_DependencyTimeoutException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DisabledException(native_input):
    return Error_DisabledException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DryRunOperationException(native_input):
    return Error_DryRunOperationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_ExpiredImportTokenException(native_input):
    return Error_ExpiredImportTokenException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_IncorrectKeyException(native_input):
    return Error_IncorrectKeyException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_IncorrectKeyMaterialException(native_input):
    return Error_IncorrectKeyMaterialException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_IncorrectTrustAnchorException(native_input):
    return Error_IncorrectTrustAnchorException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidAliasNameException(native_input):
    return Error_InvalidAliasNameException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidArnException(native_input):
    return Error_InvalidArnException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidCiphertextException(native_input):
    return Error_InvalidCiphertextException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidGrantIdException(native_input):
    return Error_InvalidGrantIdException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidGrantTokenException(native_input):
    return Error_InvalidGrantTokenException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidImportTokenException(native_input):
    return Error_InvalidImportTokenException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidKeyUsageException(native_input):
    return Error_InvalidKeyUsageException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_InvalidMarkerException(native_input):
    return Error_InvalidMarkerException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_KeyUnavailableException(native_input):
    return Error_KeyUnavailableException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_KMSInternalException(native_input):
    return Error_KMSInternalException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_KMSInvalidMacException(native_input):
    return Error_KMSInvalidMacException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_KMSInvalidSignatureException(native_input):
    return Error_KMSInvalidSignatureException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_KMSInvalidStateException(native_input):
    return Error_KMSInvalidStateException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_LimitExceededException(native_input):
    return Error_LimitExceededException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_MalformedPolicyDocumentException(native_input):
    return Error_MalformedPolicyDocumentException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_NotFoundException(native_input):
    return Error_NotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_TagException(native_input):
    return Error_TagException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_UnsupportedOperationException(native_input):
    return Error_UnsupportedOperationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksKeyAlreadyInUseException(native_input):
    return Error_XksKeyAlreadyInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksKeyInvalidConfigurationException(native_input):
    return Error_XksKeyInvalidConfigurationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksKeyNotFoundException(native_input):
    return Error_XksKeyNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyIncorrectAuthenticationCredentialException(native_input):
    return Error_XksProxyIncorrectAuthenticationCredentialException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyInvalidConfigurationException(native_input):
    return Error_XksProxyInvalidConfigurationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyInvalidResponseException(native_input):
    return Error_XksProxyInvalidResponseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyUriEndpointInUseException(native_input):
    return Error_XksProxyUriEndpointInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyUriInUseException(native_input):
    return Error_XksProxyUriInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyUriUnreachableException(native_input):
    return Error_XksProxyUriUnreachableException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyVpcEndpointServiceInUseException(native_input):
    return Error_XksProxyVpcEndpointServiceInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyVpcEndpointServiceInvalidConfigurationException(
    native_input,
):
    return Error_XksProxyVpcEndpointServiceInvalidConfigurationException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyVpcEndpointServiceNotFoundException(native_input):
    return Error_XksProxyVpcEndpointServiceNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CancelKeyDeletionRequest(native_input):
    return DafnyCancelKeyDeletionRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CancelKeyDeletionResponse(native_input):
    return DafnyCancelKeyDeletionResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ConnectCustomKeyStoreRequest(native_input):
    return DafnyConnectCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["CustomKeyStoreId"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_ConnectCustomKeyStoreResponse(native_input):
    return DafnyConnectCustomKeyStoreResponse()


def com_amazonaws_kms_CreateAliasRequest(native_input):
    return DafnyCreateAliasRequest(
        AliasName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AliasName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TargetKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TargetKeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CreateCustomKeyStoreRequest(native_input):
    return DafnyCreateCustomKeyStoreRequest(
        CustomKeyStoreName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["CustomKeyStoreName"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        CloudHsmClusterId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudHsmClusterId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudHsmClusterId" in native_input.keys()
            else Option_None()
        ),
        TrustAnchorCertificate=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["TrustAnchorCertificate"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TrustAnchorCertificate" in native_input.keys()
            else Option_None()
        ),
        KeyStorePassword=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KeyStorePassword"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KeyStorePassword" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreType(
                    native_input["CustomKeyStoreType"]
                )
            )
            if "CustomKeyStoreType" in native_input.keys()
            else Option_None()
        ),
        XksProxyUriEndpoint=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["XksProxyUriEndpoint"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyUriEndpoint" in native_input.keys()
            else Option_None()
        ),
        XksProxyUriPath=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["XksProxyUriPath"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyUriPath" in native_input.keys()
            else Option_None()
        ),
        XksProxyVpcEndpointServiceName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "XksProxyVpcEndpointServiceName"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyVpcEndpointServiceName" in native_input.keys()
            else Option_None()
        ),
        XksProxyAuthenticationCredential=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyAuthenticationCredentialType(
                    native_input["XksProxyAuthenticationCredential"]
                )
            )
            if "XksProxyAuthenticationCredential" in native_input.keys()
            else Option_None()
        ),
        XksProxyConnectivity=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyConnectivityType(
                    native_input["XksProxyConnectivity"]
                )
            )
            if "XksProxyConnectivity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_CustomKeyStoreType(native_input):
    # Convert CustomKeyStoreType
    if native_input == "AWS_CLOUDHSM":
        return CustomKeyStoreType_AWS__CLOUDHSM()
    elif native_input == "EXTERNAL_KEY_STORE":
        return CustomKeyStoreType_EXTERNAL__KEY__STORE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_XksProxyAuthenticationCredentialType(native_input):
    return DafnyXksProxyAuthenticationCredentialType(
        AccessKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AccessKeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        RawSecretAccessKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RawSecretAccessKey"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_XksProxyConnectivityType(native_input):
    # Convert XksProxyConnectivityType
    if native_input == "PUBLIC_ENDPOINT":
        return XksProxyConnectivityType_PUBLIC__ENDPOINT()
    elif native_input == "VPC_ENDPOINT_SERVICE":
        return XksProxyConnectivityType_VPC__ENDPOINT__SERVICE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_CreateCustomKeyStoreResponse(native_input):
    return DafnyCreateCustomKeyStoreResponse(
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_CreateGrantRequest(native_input):
    return DafnyCreateGrantRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GranteePrincipal=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GranteePrincipal"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        RetiringPrincipal=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["RetiringPrincipal"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RetiringPrincipal" in native_input.keys()
            else Option_None()
        ),
        Operations=Seq(
            [
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantOperation(
                    list_element
                )
                for list_element in native_input["Operations"]
            ]
        ),
        Constraints=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantConstraints(
                    native_input["Constraints"]
                )
            )
            if "Constraints" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        Name=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Name"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Name" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GrantOperation(native_input):
    # Convert GrantOperation
    if native_input == "Decrypt":
        return GrantOperation_Decrypt()
    elif native_input == "Encrypt":
        return GrantOperation_Encrypt()
    elif native_input == "GenerateDataKey":
        return GrantOperation_GenerateDataKey()
    elif native_input == "GenerateDataKeyWithoutPlaintext":
        return GrantOperation_GenerateDataKeyWithoutPlaintext()
    elif native_input == "ReEncryptFrom":
        return GrantOperation_ReEncryptFrom()
    elif native_input == "ReEncryptTo":
        return GrantOperation_ReEncryptTo()
    elif native_input == "Sign":
        return GrantOperation_Sign()
    elif native_input == "Verify":
        return GrantOperation_Verify()
    elif native_input == "GetPublicKey":
        return GrantOperation_GetPublicKey()
    elif native_input == "CreateGrant":
        return GrantOperation_CreateGrant()
    elif native_input == "RetireGrant":
        return GrantOperation_RetireGrant()
    elif native_input == "DescribeKey":
        return GrantOperation_DescribeKey()
    elif native_input == "GenerateDataKeyPair":
        return GrantOperation_GenerateDataKeyPair()
    elif native_input == "GenerateDataKeyPairWithoutPlaintext":
        return GrantOperation_GenerateDataKeyPairWithoutPlaintext()
    elif native_input == "GenerateMac":
        return GrantOperation_GenerateMac()
    elif native_input == "VerifyMac":
        return GrantOperation_VerifyMac()
    elif native_input == "DeriveSharedSecret":
        return GrantOperation_DeriveSharedSecret()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_GrantConstraints(native_input):
    return DafnyGrantConstraints(
        EncryptionContextSubset=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "EncryptionContextSubset"
                        ].items()
                    }
                )
            )
            if "EncryptionContextSubset" in native_input.keys()
            else Option_None()
        ),
        EncryptionContextEquals=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "EncryptionContextEquals"
                        ].items()
                    }
                )
            )
            if "EncryptionContextEquals" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_CreateGrantResponse(native_input):
    return DafnyCreateGrantResponse(
        GrantToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GrantToken" in native_input.keys()
            else Option_None()
        ),
        GrantId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "GrantId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_CreateKeyRequest(native_input):
    return DafnyCreateKeyRequest(
        Policy=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Policy"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Policy" in native_input.keys()
            else Option_None()
        ),
        Description=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Description"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "Description" in native_input.keys()
            else Option_None()
        ),
        KeyUsage=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(
                    native_input["KeyUsage"]
                )
            )
            if "KeyUsage" in native_input.keys()
            else Option_None()
        ),
        CustomerMasterKeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(
                    native_input["CustomerMasterKeySpec"]
                )
            )
            if "CustomerMasterKeySpec" in native_input.keys()
            else Option_None()
        ),
        KeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(
                    native_input["KeySpec"]
                )
            )
            if "KeySpec" in native_input.keys()
            else Option_None()
        ),
        Origin=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_OriginType(
                    native_input["Origin"]
                )
            )
            if "Origin" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
        BypassPolicyLockoutSafetyCheck=(
            Option_Some(native_input["BypassPolicyLockoutSafetyCheck"])
            if "BypassPolicyLockoutSafetyCheck" in native_input.keys()
            else Option_None()
        ),
        Tags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(
                            list_element
                        )
                        for list_element in native_input["Tags"]
                    ]
                )
            )
            if "Tags" in native_input.keys()
            else Option_None()
        ),
        MultiRegion=(
            Option_Some(native_input["MultiRegion"])
            if "MultiRegion" in native_input.keys()
            else Option_None()
        ),
        XksKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["XksKeyId"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksKeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_KeyUsageType(native_input):
    # Convert KeyUsageType
    if native_input == "SIGN_VERIFY":
        return KeyUsageType_SIGN__VERIFY()
    elif native_input == "ENCRYPT_DECRYPT":
        return KeyUsageType_ENCRYPT__DECRYPT()
    elif native_input == "GENERATE_VERIFY_MAC":
        return KeyUsageType_GENERATE__VERIFY__MAC()
    elif native_input == "KEY_AGREEMENT":
        return KeyUsageType_KEY__AGREEMENT()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_CustomerMasterKeySpec(native_input):
    # Convert CustomerMasterKeySpec
    if native_input == "RSA_2048":
        return CustomerMasterKeySpec_RSA__2048()
    elif native_input == "RSA_3072":
        return CustomerMasterKeySpec_RSA__3072()
    elif native_input == "RSA_4096":
        return CustomerMasterKeySpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return CustomerMasterKeySpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return CustomerMasterKeySpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return CustomerMasterKeySpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return CustomerMasterKeySpec_ECC__SECG__P256K1()
    elif native_input == "SYMMETRIC_DEFAULT":
        return CustomerMasterKeySpec_SYMMETRIC__DEFAULT()
    elif native_input == "HMAC_224":
        return CustomerMasterKeySpec_HMAC__224()
    elif native_input == "HMAC_256":
        return CustomerMasterKeySpec_HMAC__256()
    elif native_input == "HMAC_384":
        return CustomerMasterKeySpec_HMAC__384()
    elif native_input == "HMAC_512":
        return CustomerMasterKeySpec_HMAC__512()
    elif native_input == "SM2":
        return CustomerMasterKeySpec_SM2()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_KeySpec(native_input):
    # Convert KeySpec
    if native_input == "RSA_2048":
        return KeySpec_RSA__2048()
    elif native_input == "RSA_3072":
        return KeySpec_RSA__3072()
    elif native_input == "RSA_4096":
        return KeySpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return KeySpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return KeySpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return KeySpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return KeySpec_ECC__SECG__P256K1()
    elif native_input == "SYMMETRIC_DEFAULT":
        return KeySpec_SYMMETRIC__DEFAULT()
    elif native_input == "HMAC_224":
        return KeySpec_HMAC__224()
    elif native_input == "HMAC_256":
        return KeySpec_HMAC__256()
    elif native_input == "HMAC_384":
        return KeySpec_HMAC__384()
    elif native_input == "HMAC_512":
        return KeySpec_HMAC__512()
    elif native_input == "SM2":
        return KeySpec_SM2()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_OriginType(native_input):
    # Convert OriginType
    if native_input == "AWS_KMS":
        return OriginType_AWS__KMS()
    elif native_input == "EXTERNAL":
        return OriginType_EXTERNAL()
    elif native_input == "AWS_CLOUDHSM":
        return OriginType_AWS__CLOUDHSM()
    elif native_input == "EXTERNAL_KEY_STORE":
        return OriginType_EXTERNAL__KEY__STORE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_Tag(native_input):
    return DafnyTag(
        TagKey=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TagKey"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TagValue=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TagValue"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_CreateKeyResponse(native_input):
    return DafnyCreateKeyResponse(
        KeyMetadata=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(
                    native_input["KeyMetadata"]
                )
            )
            if "KeyMetadata" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_KeyMetadata(native_input):
    return DafnyKeyMetadata(
        AWSAccountId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["AWSAccountId"].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AWSAccountId" in native_input.keys()
            else Option_None()
        ),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Arn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Arn"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Arn" in native_input.keys()
            else Option_None()
        ),
        CreationDate=(
            Option_Some(_dafny.Seq(native_input["CreationDate"].isoformat()))
            if "CreationDate" in native_input.keys()
            else Option_None()
        ),
        Enabled=(
            Option_Some(native_input["Enabled"])
            if "Enabled" in native_input.keys()
            else Option_None()
        ),
        Description=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Description"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "Description" in native_input.keys()
            else Option_None()
        ),
        KeyUsage=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(
                    native_input["KeyUsage"]
                )
            )
            if "KeyUsage" in native_input.keys()
            else Option_None()
        ),
        KeyState=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyState(
                    native_input["KeyState"]
                )
            )
            if "KeyState" in native_input.keys()
            else Option_None()
        ),
        DeletionDate=(
            Option_Some(_dafny.Seq(native_input["DeletionDate"].isoformat()))
            if "DeletionDate" in native_input.keys()
            else Option_None()
        ),
        ValidTo=(
            Option_Some(_dafny.Seq(native_input["ValidTo"].isoformat()))
            if "ValidTo" in native_input.keys()
            else Option_None()
        ),
        Origin=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_OriginType(
                    native_input["Origin"]
                )
            )
            if "Origin" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
        CloudHsmClusterId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudHsmClusterId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudHsmClusterId" in native_input.keys()
            else Option_None()
        ),
        ExpirationModel=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ExpirationModelType(
                    native_input["ExpirationModel"]
                )
            )
            if "ExpirationModel" in native_input.keys()
            else Option_None()
        ),
        KeyManager=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyManagerType(
                    native_input["KeyManager"]
                )
            )
            if "KeyManager" in native_input.keys()
            else Option_None()
        ),
        CustomerMasterKeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(
                    native_input["CustomerMasterKeySpec"]
                )
            )
            if "CustomerMasterKeySpec" in native_input.keys()
            else Option_None()
        ),
        KeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(
                    native_input["KeySpec"]
                )
            )
            if "KeySpec" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["EncryptionAlgorithms"]
                    ]
                )
            )
            if "EncryptionAlgorithms" in native_input.keys()
            else Option_None()
        ),
        SigningAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["SigningAlgorithms"]
                    ]
                )
            )
            if "SigningAlgorithms" in native_input.keys()
            else Option_None()
        ),
        KeyAgreementAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["KeyAgreementAlgorithms"]
                    ]
                )
            )
            if "KeyAgreementAlgorithms" in native_input.keys()
            else Option_None()
        ),
        MultiRegion=(
            Option_Some(native_input["MultiRegion"])
            if "MultiRegion" in native_input.keys()
            else Option_None()
        ),
        MultiRegionConfiguration=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionConfiguration(
                    native_input["MultiRegionConfiguration"]
                )
            )
            if "MultiRegionConfiguration" in native_input.keys()
            else Option_None()
        ),
        PendingDeletionWindowInDays=(
            Option_Some(native_input["PendingDeletionWindowInDays"])
            if "PendingDeletionWindowInDays" in native_input.keys()
            else Option_None()
        ),
        MacAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MacAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["MacAlgorithms"]
                    ]
                )
            )
            if "MacAlgorithms" in native_input.keys()
            else Option_None()
        ),
        XksKeyConfiguration=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksKeyConfigurationType(
                    native_input["XksKeyConfiguration"]
                )
            )
            if "XksKeyConfiguration" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_KeyState(native_input):
    # Convert KeyState
    if native_input == "Creating":
        return KeyState_Creating()
    elif native_input == "Enabled":
        return KeyState_Enabled()
    elif native_input == "Disabled":
        return KeyState_Disabled()
    elif native_input == "PendingDeletion":
        return KeyState_PendingDeletion()
    elif native_input == "PendingImport":
        return KeyState_PendingImport()
    elif native_input == "PendingReplicaDeletion":
        return KeyState_PendingReplicaDeletion()
    elif native_input == "Unavailable":
        return KeyState_Unavailable()
    elif native_input == "Updating":
        return KeyState_Updating()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_ExpirationModelType(native_input):
    # Convert ExpirationModelType
    if native_input == "KEY_MATERIAL_EXPIRES":
        return ExpirationModelType_KEY__MATERIAL__EXPIRES()
    elif native_input == "KEY_MATERIAL_DOES_NOT_EXPIRE":
        return ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_KeyManagerType(native_input):
    # Convert KeyManagerType
    if native_input == "AWS":
        return KeyManagerType_AWS()
    elif native_input == "CUSTOMER":
        return KeyManagerType_CUSTOMER()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_EncryptionAlgorithmSpec(native_input):
    # Convert EncryptionAlgorithmSpec
    if native_input == "SYMMETRIC_DEFAULT":
        return EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT()
    elif native_input == "RSAES_OAEP_SHA_1":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1()
    elif native_input == "RSAES_OAEP_SHA_256":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_SigningAlgorithmSpec(native_input):
    # Convert SigningAlgorithmSpec
    if native_input == "RSASSA_PSS_SHA_256":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__256()
    elif native_input == "RSASSA_PSS_SHA_384":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__384()
    elif native_input == "RSASSA_PSS_SHA_512":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__512()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_256":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_384":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_512":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512()
    elif native_input == "ECDSA_SHA_256":
        return SigningAlgorithmSpec_ECDSA__SHA__256()
    elif native_input == "ECDSA_SHA_384":
        return SigningAlgorithmSpec_ECDSA__SHA__384()
    elif native_input == "ECDSA_SHA_512":
        return SigningAlgorithmSpec_ECDSA__SHA__512()
    elif native_input == "SM2DSA":
        return SigningAlgorithmSpec_SM2DSA()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_KeyAgreementAlgorithmSpec(native_input):
    # Convert KeyAgreementAlgorithmSpec
    if native_input == "ECDH":
        return KeyAgreementAlgorithmSpec_ECDH()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_MultiRegionConfiguration(native_input):
    return DafnyMultiRegionConfiguration(
        MultiRegionKeyType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKeyType(
                    native_input["MultiRegionKeyType"]
                )
            )
            if "MultiRegionKeyType" in native_input.keys()
            else Option_None()
        ),
        PrimaryKey=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKey(
                    native_input["PrimaryKey"]
                )
            )
            if "PrimaryKey" in native_input.keys()
            else Option_None()
        ),
        ReplicaKeys=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKey(
                            list_element
                        )
                        for list_element in native_input["ReplicaKeys"]
                    ]
                )
            )
            if "ReplicaKeys" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_MacAlgorithmSpec(native_input):
    # Convert MacAlgorithmSpec
    if native_input == "HMAC_SHA_224":
        return MacAlgorithmSpec_HMAC__SHA__224()
    elif native_input == "HMAC_SHA_256":
        return MacAlgorithmSpec_HMAC__SHA__256()
    elif native_input == "HMAC_SHA_384":
        return MacAlgorithmSpec_HMAC__SHA__384()
    elif native_input == "HMAC_SHA_512":
        return MacAlgorithmSpec_HMAC__SHA__512()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_XksKeyConfigurationType(native_input):
    return DafnyXksKeyConfigurationType(
        Id=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Id"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Id" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_MultiRegionKeyType(native_input):
    # Convert MultiRegionKeyType
    if native_input == "PRIMARY":
        return MultiRegionKeyType_PRIMARY()
    elif native_input == "REPLICA":
        return MultiRegionKeyType_REPLICA()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_MultiRegionKey(native_input):
    return DafnyMultiRegionKey(
        Arn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Arn"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Arn" in native_input.keys()
            else Option_None()
        ),
        Region=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Region"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Region" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DecryptRequest(native_input):
    return DafnyDecryptRequest(
        CiphertextBlob=Seq(native_input["CiphertextBlob"]),
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["EncryptionAlgorithm"]
                )
            )
            if "EncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        Recipient=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RecipientInfo(
                    native_input["Recipient"]
                )
            )
            if "Recipient" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RecipientInfo(native_input):
    return DafnyRecipientInfo(
        KeyEncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyEncryptionMechanism(
                    native_input["KeyEncryptionAlgorithm"]
                )
            )
            if "KeyEncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        AttestationDocument=(
            Option_Some(Seq(native_input["AttestationDocument"]))
            if "AttestationDocument" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_KeyEncryptionMechanism(native_input):
    # Convert KeyEncryptionMechanism
    if native_input == "RSAES_OAEP_SHA_256":
        return KeyEncryptionMechanism_RSAES__OAEP__SHA__256()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_DecryptResponse(native_input):
    return DafnyDecryptResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        Plaintext=(
            Option_Some(Seq(native_input["Plaintext"]))
            if "Plaintext" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["EncryptionAlgorithm"]
                )
            )
            if "EncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        CiphertextForRecipient=(
            Option_Some(Seq(native_input["CiphertextForRecipient"]))
            if "CiphertextForRecipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DeleteAliasRequest(native_input):
    return DafnyDeleteAliasRequest(
        AliasName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AliasName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DeleteCustomKeyStoreRequest(native_input):
    return DafnyDeleteCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["CustomKeyStoreId"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DeleteCustomKeyStoreResponse(native_input):
    return DafnyDeleteCustomKeyStoreResponse()


def com_amazonaws_kms_DeleteImportedKeyMaterialRequest(native_input):
    return DafnyDeleteImportedKeyMaterialRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DeriveSharedSecretRequest(native_input):
    return DafnyDeriveSharedSecretRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeyAgreementAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
            native_input["KeyAgreementAlgorithm"]
        ),
        PublicKey=Seq(native_input["PublicKey"]),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
        Recipient=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RecipientInfo(
                    native_input["Recipient"]
                )
            )
            if "Recipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DeriveSharedSecretResponse(native_input):
    return DafnyDeriveSharedSecretResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        SharedSecret=(
            Option_Some(Seq(native_input["SharedSecret"]))
            if "SharedSecret" in native_input.keys()
            else Option_None()
        ),
        CiphertextForRecipient=(
            Option_Some(Seq(native_input["CiphertextForRecipient"]))
            if "CiphertextForRecipient" in native_input.keys()
            else Option_None()
        ),
        KeyAgreementAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                    native_input["KeyAgreementAlgorithm"]
                )
            )
            if "KeyAgreementAlgorithm" in native_input.keys()
            else Option_None()
        ),
        KeyOrigin=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_OriginType(
                    native_input["KeyOrigin"]
                )
            )
            if "KeyOrigin" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DescribeCustomKeyStoresRequest(native_input):
    return DafnyDescribeCustomKeyStoresRequest(
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreName" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DescribeCustomKeyStoresResponse(native_input):
    return DafnyDescribeCustomKeyStoresResponse(
        CustomKeyStores=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoresListEntry(
                            list_element
                        )
                        for list_element in native_input["CustomKeyStores"]
                    ]
                )
            )
            if "CustomKeyStores" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_CustomKeyStoresListEntry(native_input):
    return DafnyCustomKeyStoresListEntry(
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreName" in native_input.keys()
            else Option_None()
        ),
        CloudHsmClusterId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudHsmClusterId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudHsmClusterId" in native_input.keys()
            else Option_None()
        ),
        TrustAnchorCertificate=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["TrustAnchorCertificate"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TrustAnchorCertificate" in native_input.keys()
            else Option_None()
        ),
        ConnectionState=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConnectionStateType(
                    native_input["ConnectionState"]
                )
            )
            if "ConnectionState" in native_input.keys()
            else Option_None()
        ),
        ConnectionErrorCode=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConnectionErrorCodeType(
                    native_input["ConnectionErrorCode"]
                )
            )
            if "ConnectionErrorCode" in native_input.keys()
            else Option_None()
        ),
        CreationDate=(
            Option_Some(_dafny.Seq(native_input["CreationDate"].isoformat()))
            if "CreationDate" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoreType(
                    native_input["CustomKeyStoreType"]
                )
            )
            if "CustomKeyStoreType" in native_input.keys()
            else Option_None()
        ),
        XksProxyConfiguration=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyConfigurationType(
                    native_input["XksProxyConfiguration"]
                )
            )
            if "XksProxyConfiguration" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ConnectionStateType(native_input):
    # Convert ConnectionStateType
    if native_input == "CONNECTED":
        return ConnectionStateType_CONNECTED()
    elif native_input == "CONNECTING":
        return ConnectionStateType_CONNECTING()
    elif native_input == "FAILED":
        return ConnectionStateType_FAILED()
    elif native_input == "DISCONNECTED":
        return ConnectionStateType_DISCONNECTED()
    elif native_input == "DISCONNECTING":
        return ConnectionStateType_DISCONNECTING()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_ConnectionErrorCodeType(native_input):
    # Convert ConnectionErrorCodeType
    if native_input == "INVALID_CREDENTIALS":
        return ConnectionErrorCodeType_INVALID__CREDENTIALS()
    elif native_input == "CLUSTER_NOT_FOUND":
        return ConnectionErrorCodeType_CLUSTER__NOT__FOUND()
    elif native_input == "NETWORK_ERRORS":
        return ConnectionErrorCodeType_NETWORK__ERRORS()
    elif native_input == "INTERNAL_ERROR":
        return ConnectionErrorCodeType_INTERNAL__ERROR()
    elif native_input == "INSUFFICIENT_CLOUDHSM_HSMS":
        return ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS()
    elif native_input == "USER_LOCKED_OUT":
        return ConnectionErrorCodeType_USER__LOCKED__OUT()
    elif native_input == "USER_NOT_FOUND":
        return ConnectionErrorCodeType_USER__NOT__FOUND()
    elif native_input == "USER_LOGGED_IN":
        return ConnectionErrorCodeType_USER__LOGGED__IN()
    elif native_input == "SUBNET_NOT_FOUND":
        return ConnectionErrorCodeType_SUBNET__NOT__FOUND()
    elif native_input == "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET":
        return ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET()
    elif native_input == "XKS_PROXY_ACCESS_DENIED":
        return ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED()
    elif native_input == "XKS_PROXY_NOT_REACHABLE":
        return ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE()
    elif native_input == "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND":
        return ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND()
    elif native_input == "XKS_PROXY_INVALID_RESPONSE":
        return ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE()
    elif native_input == "XKS_PROXY_INVALID_CONFIGURATION":
        return ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION()
    elif native_input == "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION":
        return (
            ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION()
        )
    elif native_input == "XKS_PROXY_TIMED_OUT":
        return ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT()
    elif native_input == "XKS_PROXY_INVALID_TLS_CONFIGURATION":
        return ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_XksProxyConfigurationType(native_input):
    return DafnyXksProxyConfigurationType(
        Connectivity=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyConnectivityType(
                    native_input["Connectivity"]
                )
            )
            if "Connectivity" in native_input.keys()
            else Option_None()
        ),
        AccessKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["AccessKeyId"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AccessKeyId" in native_input.keys()
            else Option_None()
        ),
        UriEndpoint=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["UriEndpoint"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "UriEndpoint" in native_input.keys()
            else Option_None()
        ),
        UriPath=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["UriPath"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "UriPath" in native_input.keys()
            else Option_None()
        ),
        VpcEndpointServiceName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["VpcEndpointServiceName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "VpcEndpointServiceName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DescribeKeyRequest(native_input):
    return DafnyDescribeKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DescribeKeyResponse(native_input):
    return DafnyDescribeKeyResponse(
        KeyMetadata=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(
                    native_input["KeyMetadata"]
                )
            )
            if "KeyMetadata" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DisableKeyRequest(native_input):
    return DafnyDisableKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DisableKeyRotationRequest(native_input):
    return DafnyDisableKeyRotationRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DisconnectCustomKeyStoreRequest(native_input):
    return DafnyDisconnectCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["CustomKeyStoreId"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_DisconnectCustomKeyStoreResponse(native_input):
    return DafnyDisconnectCustomKeyStoreResponse()


def com_amazonaws_kms_EnableKeyRequest(native_input):
    return DafnyEnableKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_EnableKeyRotationRequest(native_input):
    return DafnyEnableKeyRotationRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        RotationPeriodInDays=(
            Option_Some(native_input["RotationPeriodInDays"])
            if "RotationPeriodInDays" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_EncryptRequest(native_input):
    return DafnyEncryptRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Plaintext=Seq(native_input["Plaintext"]),
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["EncryptionAlgorithm"]
                )
            )
            if "EncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_EncryptResponse(native_input):
    return DafnyEncryptResponse(
        CiphertextBlob=(
            Option_Some(Seq(native_input["CiphertextBlob"]))
            if "CiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["EncryptionAlgorithm"]
                )
            )
            if "EncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyRequest(native_input):
    return DafnyGenerateDataKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        NumberOfBytes=(
            Option_Some(native_input["NumberOfBytes"])
            if "NumberOfBytes" in native_input.keys()
            else Option_None()
        ),
        KeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeySpec(
                    native_input["KeySpec"]
                )
            )
            if "KeySpec" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        Recipient=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RecipientInfo(
                    native_input["Recipient"]
                )
            )
            if "Recipient" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DataKeySpec(native_input):
    # Convert DataKeySpec
    if native_input == "AES_256":
        return DataKeySpec_AES__256()
    elif native_input == "AES_128":
        return DataKeySpec_AES__128()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_GenerateDataKeyResponse(native_input):
    return DafnyGenerateDataKeyResponse(
        CiphertextBlob=(
            Option_Some(Seq(native_input["CiphertextBlob"]))
            if "CiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        Plaintext=(
            Option_Some(Seq(native_input["Plaintext"]))
            if "Plaintext" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        CiphertextForRecipient=(
            Option_Some(Seq(native_input["CiphertextForRecipient"]))
            if "CiphertextForRecipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyPairRequest(native_input):
    return DafnyGenerateDataKeyPairRequest(
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeyPairSpec=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(
            native_input["KeyPairSpec"]
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        Recipient=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RecipientInfo(
                    native_input["Recipient"]
                )
            )
            if "Recipient" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_DataKeyPairSpec(native_input):
    # Convert DataKeyPairSpec
    if native_input == "RSA_2048":
        return DataKeyPairSpec_RSA__2048()
    elif native_input == "RSA_3072":
        return DataKeyPairSpec_RSA__3072()
    elif native_input == "RSA_4096":
        return DataKeyPairSpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return DataKeyPairSpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return DataKeyPairSpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return DataKeyPairSpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return DataKeyPairSpec_ECC__SECG__P256K1()
    elif native_input == "SM2":
        return DataKeyPairSpec_SM2()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_GenerateDataKeyPairResponse(native_input):
    return DafnyGenerateDataKeyPairResponse(
        PrivateKeyCiphertextBlob=(
            Option_Some(Seq(native_input["PrivateKeyCiphertextBlob"]))
            if "PrivateKeyCiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        PrivateKeyPlaintext=(
            Option_Some(Seq(native_input["PrivateKeyPlaintext"]))
            if "PrivateKeyPlaintext" in native_input.keys()
            else Option_None()
        ),
        PublicKey=(
            Option_Some(Seq(native_input["PublicKey"]))
            if "PublicKey" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        KeyPairSpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(
                    native_input["KeyPairSpec"]
                )
            )
            if "KeyPairSpec" in native_input.keys()
            else Option_None()
        ),
        CiphertextForRecipient=(
            Option_Some(Seq(native_input["CiphertextForRecipient"]))
            if "CiphertextForRecipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextRequest(native_input):
    return DafnyGenerateDataKeyPairWithoutPlaintextRequest(
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeyPairSpec=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(
            native_input["KeyPairSpec"]
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextResponse(native_input):
    return DafnyGenerateDataKeyPairWithoutPlaintextResponse(
        PrivateKeyCiphertextBlob=(
            Option_Some(Seq(native_input["PrivateKeyCiphertextBlob"]))
            if "PrivateKeyCiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        PublicKey=(
            Option_Some(Seq(native_input["PublicKey"]))
            if "PublicKey" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        KeyPairSpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(
                    native_input["KeyPairSpec"]
                )
            )
            if "KeyPairSpec" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextRequest(native_input):
    return DafnyGenerateDataKeyWithoutPlaintextRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        EncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input["EncryptionContext"].items()
                    }
                )
            )
            if "EncryptionContext" in native_input.keys()
            else Option_None()
        ),
        KeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeySpec(
                    native_input["KeySpec"]
                )
            )
            if "KeySpec" in native_input.keys()
            else Option_None()
        ),
        NumberOfBytes=(
            Option_Some(native_input["NumberOfBytes"])
            if "NumberOfBytes" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextResponse(native_input):
    return DafnyGenerateDataKeyWithoutPlaintextResponse(
        CiphertextBlob=(
            Option_Some(Seq(native_input["CiphertextBlob"]))
            if "CiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateMacRequest(native_input):
    return DafnyGenerateMacRequest(
        Message=Seq(native_input["Message"]),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        MacAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MacAlgorithmSpec(
            native_input["MacAlgorithm"]
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateMacResponse(native_input):
    return DafnyGenerateMacResponse(
        Mac=(
            Option_Some(Seq(native_input["Mac"]))
            if "Mac" in native_input.keys()
            else Option_None()
        ),
        MacAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MacAlgorithmSpec(
                    native_input["MacAlgorithm"]
                )
            )
            if "MacAlgorithm" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateRandomRequest(native_input):
    return DafnyGenerateRandomRequest(
        NumberOfBytes=(
            Option_Some(native_input["NumberOfBytes"])
            if "NumberOfBytes" in native_input.keys()
            else Option_None()
        ),
        CustomKeyStoreId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CustomKeyStoreId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CustomKeyStoreId" in native_input.keys()
            else Option_None()
        ),
        Recipient=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RecipientInfo(
                    native_input["Recipient"]
                )
            )
            if "Recipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GenerateRandomResponse(native_input):
    return DafnyGenerateRandomResponse(
        Plaintext=(
            Option_Some(Seq(native_input["Plaintext"]))
            if "Plaintext" in native_input.keys()
            else Option_None()
        ),
        CiphertextForRecipient=(
            Option_Some(Seq(native_input["CiphertextForRecipient"]))
            if "CiphertextForRecipient" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetKeyPolicyRequest(native_input):
    return DafnyGetKeyPolicyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PolicyName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["PolicyName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "PolicyName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetKeyPolicyResponse(native_input):
    return DafnyGetKeyPolicyResponse(
        Policy=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Policy"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Policy" in native_input.keys()
            else Option_None()
        ),
        PolicyName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["PolicyName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "PolicyName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetKeyRotationStatusRequest(native_input):
    return DafnyGetKeyRotationStatusRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_GetKeyRotationStatusResponse(native_input):
    return DafnyGetKeyRotationStatusResponse(
        KeyRotationEnabled=(
            Option_Some(native_input["KeyRotationEnabled"])
            if "KeyRotationEnabled" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        RotationPeriodInDays=(
            Option_Some(native_input["RotationPeriodInDays"])
            if "RotationPeriodInDays" in native_input.keys()
            else Option_None()
        ),
        NextRotationDate=(
            Option_Some(_dafny.Seq(native_input["NextRotationDate"].isoformat()))
            if "NextRotationDate" in native_input.keys()
            else Option_None()
        ),
        OnDemandRotationStartDate=(
            Option_Some(
                _dafny.Seq(native_input["OnDemandRotationStartDate"].isoformat())
            )
            if "OnDemandRotationStartDate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetParametersForImportRequest(native_input):
    return DafnyGetParametersForImportRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        WrappingAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_AlgorithmSpec(
            native_input["WrappingAlgorithm"]
        ),
        WrappingKeySpec=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_WrappingKeySpec(
            native_input["WrappingKeySpec"]
        ),
    )


def com_amazonaws_kms_AlgorithmSpec(native_input):
    # Convert AlgorithmSpec
    if native_input == "RSAES_PKCS1_V1_5":
        return AlgorithmSpec_RSAES__PKCS1__V1__5()
    elif native_input == "RSAES_OAEP_SHA_1":
        return AlgorithmSpec_RSAES__OAEP__SHA__1()
    elif native_input == "RSAES_OAEP_SHA_256":
        return AlgorithmSpec_RSAES__OAEP__SHA__256()
    elif native_input == "RSA_AES_KEY_WRAP_SHA_1":
        return AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1()
    elif native_input == "RSA_AES_KEY_WRAP_SHA_256":
        return AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256()
    elif native_input == "SM2PKE":
        return AlgorithmSpec_SM2PKE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_WrappingKeySpec(native_input):
    # Convert WrappingKeySpec
    if native_input == "RSA_2048":
        return WrappingKeySpec_RSA__2048()
    elif native_input == "RSA_3072":
        return WrappingKeySpec_RSA__3072()
    elif native_input == "RSA_4096":
        return WrappingKeySpec_RSA__4096()
    elif native_input == "SM2":
        return WrappingKeySpec_SM2()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_GetParametersForImportResponse(native_input):
    return DafnyGetParametersForImportResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        ImportToken=(
            Option_Some(Seq(native_input["ImportToken"]))
            if "ImportToken" in native_input.keys()
            else Option_None()
        ),
        PublicKey=(
            Option_Some(Seq(native_input["PublicKey"]))
            if "PublicKey" in native_input.keys()
            else Option_None()
        ),
        ParametersValidTo=(
            Option_Some(_dafny.Seq(native_input["ParametersValidTo"].isoformat()))
            if "ParametersValidTo" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetPublicKeyRequest(native_input):
    return DafnyGetPublicKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GetPublicKeyResponse(native_input):
    return DafnyGetPublicKeyResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        PublicKey=(
            Option_Some(Seq(native_input["PublicKey"]))
            if "PublicKey" in native_input.keys()
            else Option_None()
        ),
        CustomerMasterKeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(
                    native_input["CustomerMasterKeySpec"]
                )
            )
            if "CustomerMasterKeySpec" in native_input.keys()
            else Option_None()
        ),
        KeySpec=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(
                    native_input["KeySpec"]
                )
            )
            if "KeySpec" in native_input.keys()
            else Option_None()
        ),
        KeyUsage=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(
                    native_input["KeyUsage"]
                )
            )
            if "KeyUsage" in native_input.keys()
            else Option_None()
        ),
        EncryptionAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["EncryptionAlgorithms"]
                    ]
                )
            )
            if "EncryptionAlgorithms" in native_input.keys()
            else Option_None()
        ),
        SigningAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["SigningAlgorithms"]
                    ]
                )
            )
            if "SigningAlgorithms" in native_input.keys()
            else Option_None()
        ),
        KeyAgreementAlgorithms=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                            list_element
                        )
                        for list_element in native_input["KeyAgreementAlgorithms"]
                    ]
                )
            )
            if "KeyAgreementAlgorithms" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ImportKeyMaterialRequest(native_input):
    return DafnyImportKeyMaterialRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ImportToken=Seq(native_input["ImportToken"]),
        EncryptedKeyMaterial=Seq(native_input["EncryptedKeyMaterial"]),
        ValidTo=(
            Option_Some(_dafny.Seq(native_input["ValidTo"].isoformat()))
            if "ValidTo" in native_input.keys()
            else Option_None()
        ),
        ExpirationModel=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ExpirationModelType(
                    native_input["ExpirationModel"]
                )
            )
            if "ExpirationModel" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ImportKeyMaterialResponse(native_input):
    return DafnyImportKeyMaterialResponse()


def com_amazonaws_kms_ListAliasesRequest(native_input):
    return DafnyListAliasesRequest(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListAliasesResponse(native_input):
    return DafnyListAliasesResponse(
        Aliases=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_AliasListEntry(
                            list_element
                        )
                        for list_element in native_input["Aliases"]
                    ]
                )
            )
            if "Aliases" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_AliasListEntry(native_input):
    return DafnyAliasListEntry(
        AliasName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["AliasName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AliasName" in native_input.keys()
            else Option_None()
        ),
        AliasArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["AliasArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AliasArn" in native_input.keys()
            else Option_None()
        ),
        TargetKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TargetKeyId"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TargetKeyId" in native_input.keys()
            else Option_None()
        ),
        CreationDate=(
            Option_Some(_dafny.Seq(native_input["CreationDate"].isoformat()))
            if "CreationDate" in native_input.keys()
            else Option_None()
        ),
        LastUpdatedDate=(
            Option_Some(_dafny.Seq(native_input["LastUpdatedDate"].isoformat()))
            if "LastUpdatedDate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListGrantsRequest(native_input):
    return DafnyListGrantsRequest(
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GrantId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "GrantId" in native_input.keys()
            else Option_None()
        ),
        GranteePrincipal=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GranteePrincipal"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GranteePrincipal" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListGrantsResponse(native_input):
    return DafnyListGrantsResponse(
        Grants=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantListEntry(
                            list_element
                        )
                        for list_element in native_input["Grants"]
                    ]
                )
            )
            if "Grants" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_GrantListEntry(native_input):
    return DafnyGrantListEntry(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        GrantId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "GrantId" in native_input.keys()
            else Option_None()
        ),
        Name=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Name"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Name" in native_input.keys()
            else Option_None()
        ),
        CreationDate=(
            Option_Some(_dafny.Seq(native_input["CreationDate"].isoformat()))
            if "CreationDate" in native_input.keys()
            else Option_None()
        ),
        GranteePrincipal=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GranteePrincipal"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GranteePrincipal" in native_input.keys()
            else Option_None()
        ),
        RetiringPrincipal=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["RetiringPrincipal"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RetiringPrincipal" in native_input.keys()
            else Option_None()
        ),
        IssuingAccount=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["IssuingAccount"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IssuingAccount" in native_input.keys()
            else Option_None()
        ),
        Operations=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantOperation(
                            list_element
                        )
                        for list_element in native_input["Operations"]
                    ]
                )
            )
            if "Operations" in native_input.keys()
            else Option_None()
        ),
        Constraints=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantConstraints(
                    native_input["Constraints"]
                )
            )
            if "Constraints" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListKeyPoliciesRequest(native_input):
    return DafnyListKeyPoliciesRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListKeyPoliciesResponse(native_input):
    return DafnyListKeyPoliciesResponse(
        PolicyNames=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["PolicyNames"]
                    ]
                )
            )
            if "PolicyNames" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListKeyRotationsRequest(native_input):
    return DafnyListKeyRotationsRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListKeyRotationsResponse(native_input):
    return DafnyListKeyRotationsResponse(
        Rotations=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RotationsListEntry(
                            list_element
                        )
                        for list_element in native_input["Rotations"]
                    ]
                )
            )
            if "Rotations" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RotationsListEntry(native_input):
    return DafnyRotationsListEntry(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        RotationDate=(
            Option_Some(_dafny.Seq(native_input["RotationDate"].isoformat()))
            if "RotationDate" in native_input.keys()
            else Option_None()
        ),
        RotationType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_RotationType(
                    native_input["RotationType"]
                )
            )
            if "RotationType" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RotationType(native_input):
    # Convert RotationType
    if native_input == "AUTOMATIC":
        return RotationType_AUTOMATIC()
    elif native_input == "ON_DEMAND":
        return RotationType_ON__DEMAND()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_ListKeysRequest(native_input):
    return DafnyListKeysRequest(
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListKeysResponse(native_input):
    return DafnyListKeysResponse(
        Keys=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyListEntry(
                            list_element
                        )
                        for list_element in native_input["Keys"]
                    ]
                )
            )
            if "Keys" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_KeyListEntry(native_input):
    return DafnyKeyListEntry(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        KeyArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyArn"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyArn" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListResourceTagsRequest(native_input):
    return DafnyListResourceTagsRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Marker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Marker"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Marker" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ListResourceTagsResponse(native_input):
    return DafnyListResourceTagsResponse(
        Tags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(
                            list_element
                        )
                        for list_element in native_input["Tags"]
                    ]
                )
            )
            if "Tags" in native_input.keys()
            else Option_None()
        ),
        NextMarker=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextMarker"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextMarker" in native_input.keys()
            else Option_None()
        ),
        Truncated=(
            Option_Some(native_input["Truncated"])
            if "Truncated" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_PutKeyPolicyRequest(native_input):
    return DafnyPutKeyPolicyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PolicyName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["PolicyName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "PolicyName" in native_input.keys()
            else Option_None()
        ),
        Policy=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Policy"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BypassPolicyLockoutSafetyCheck=(
            Option_Some(native_input["BypassPolicyLockoutSafetyCheck"])
            if "BypassPolicyLockoutSafetyCheck" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ReEncryptRequest(native_input):
    return DafnyReEncryptRequest(
        CiphertextBlob=Seq(native_input["CiphertextBlob"]),
        SourceEncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "SourceEncryptionContext"
                        ].items()
                    }
                )
            )
            if "SourceEncryptionContext" in native_input.keys()
            else Option_None()
        ),
        SourceKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["SourceKeyId"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceKeyId" in native_input.keys()
            else Option_None()
        ),
        DestinationKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["DestinationKeyId"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        DestinationEncryptionContext=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "DestinationEncryptionContext"
                        ].items()
                    }
                )
            )
            if "DestinationEncryptionContext" in native_input.keys()
            else Option_None()
        ),
        SourceEncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["SourceEncryptionAlgorithm"]
                )
            )
            if "SourceEncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        DestinationEncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["DestinationEncryptionAlgorithm"]
                )
            )
            if "DestinationEncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ReEncryptResponse(native_input):
    return DafnyReEncryptResponse(
        CiphertextBlob=(
            Option_Some(Seq(native_input["CiphertextBlob"]))
            if "CiphertextBlob" in native_input.keys()
            else Option_None()
        ),
        SourceKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["SourceKeyId"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceKeyId" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        SourceEncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["SourceEncryptionAlgorithm"]
                )
            )
            if "SourceEncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
        DestinationEncryptionAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(
                    native_input["DestinationEncryptionAlgorithm"]
                )
            )
            if "DestinationEncryptionAlgorithm" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ReplicateKeyRequest(native_input):
    return DafnyReplicateKeyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicaRegion=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ReplicaRegion"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Policy=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Policy"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Policy" in native_input.keys()
            else Option_None()
        ),
        BypassPolicyLockoutSafetyCheck=(
            Option_Some(native_input["BypassPolicyLockoutSafetyCheck"])
            if "BypassPolicyLockoutSafetyCheck" in native_input.keys()
            else Option_None()
        ),
        Description=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Description"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "Description" in native_input.keys()
            else Option_None()
        ),
        Tags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(
                            list_element
                        )
                        for list_element in native_input["Tags"]
                    ]
                )
            )
            if "Tags" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ReplicateKeyResponse(native_input):
    return DafnyReplicateKeyResponse(
        ReplicaKeyMetadata=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(
                    native_input["ReplicaKeyMetadata"]
                )
            )
            if "ReplicaKeyMetadata" in native_input.keys()
            else Option_None()
        ),
        ReplicaPolicy=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ReplicaPolicy"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ReplicaPolicy" in native_input.keys()
            else Option_None()
        ),
        ReplicaTags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(
                            list_element
                        )
                        for list_element in native_input["ReplicaTags"]
                    ]
                )
            )
            if "ReplicaTags" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RetireGrantRequest(native_input):
    return DafnyRetireGrantRequest(
        GrantToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GrantToken" in native_input.keys()
            else Option_None()
        ),
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        GrantId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["GrantId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "GrantId" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RevokeGrantRequest(native_input):
    return DafnyRevokeGrantRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GrantId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GrantId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_RotateKeyOnDemandRequest(native_input):
    return DafnyRotateKeyOnDemandRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_RotateKeyOnDemandResponse(native_input):
    return DafnyRotateKeyOnDemandResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ScheduleKeyDeletionRequest(native_input):
    return DafnyScheduleKeyDeletionRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PendingWindowInDays=(
            Option_Some(native_input["PendingWindowInDays"])
            if "PendingWindowInDays" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_ScheduleKeyDeletionResponse(native_input):
    return DafnyScheduleKeyDeletionResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        DeletionDate=(
            Option_Some(_dafny.Seq(native_input["DeletionDate"].isoformat()))
            if "DeletionDate" in native_input.keys()
            else Option_None()
        ),
        KeyState=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyState(
                    native_input["KeyState"]
                )
            )
            if "KeyState" in native_input.keys()
            else Option_None()
        ),
        PendingWindowInDays=(
            Option_Some(native_input["PendingWindowInDays"])
            if "PendingWindowInDays" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_SignRequest(native_input):
    return DafnySignRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Message=Seq(native_input["Message"]),
        MessageType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MessageType(
                    native_input["MessageType"]
                )
            )
            if "MessageType" in native_input.keys()
            else Option_None()
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        SigningAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
            native_input["SigningAlgorithm"]
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_MessageType(native_input):
    # Convert MessageType
    if native_input == "RAW":
        return MessageType_RAW()
    elif native_input == "DIGEST":
        return MessageType_DIGEST()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_kms_SignResponse(native_input):
    return DafnySignResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        Signature=(
            Option_Some(Seq(native_input["Signature"]))
            if "Signature" in native_input.keys()
            else Option_None()
        ),
        SigningAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
                    native_input["SigningAlgorithm"]
                )
            )
            if "SigningAlgorithm" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_TagResourceRequest(native_input):
    return DafnyTagResourceRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Tags=Seq(
            [
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(
                    list_element
                )
                for list_element in native_input["Tags"]
            ]
        ),
    )


def com_amazonaws_kms_UntagResourceRequest(native_input):
    return DafnyUntagResourceRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TagKeys=Seq(
            [
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(list_element.encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
                for list_element in native_input["TagKeys"]
            ]
        ),
    )


def com_amazonaws_kms_UpdateAliasRequest(native_input):
    return DafnyUpdateAliasRequest(
        AliasName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AliasName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TargetKeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TargetKeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_UpdateCustomKeyStoreRequest(native_input):
    return DafnyUpdateCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["CustomKeyStoreId"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        NewCustomKeyStoreName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["NewCustomKeyStoreName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NewCustomKeyStoreName" in native_input.keys()
            else Option_None()
        ),
        KeyStorePassword=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KeyStorePassword"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KeyStorePassword" in native_input.keys()
            else Option_None()
        ),
        CloudHsmClusterId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudHsmClusterId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudHsmClusterId" in native_input.keys()
            else Option_None()
        ),
        XksProxyUriEndpoint=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["XksProxyUriEndpoint"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyUriEndpoint" in native_input.keys()
            else Option_None()
        ),
        XksProxyUriPath=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["XksProxyUriPath"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyUriPath" in native_input.keys()
            else Option_None()
        ),
        XksProxyVpcEndpointServiceName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "XksProxyVpcEndpointServiceName"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "XksProxyVpcEndpointServiceName" in native_input.keys()
            else Option_None()
        ),
        XksProxyAuthenticationCredential=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyAuthenticationCredentialType(
                    native_input["XksProxyAuthenticationCredential"]
                )
            )
            if "XksProxyAuthenticationCredential" in native_input.keys()
            else Option_None()
        ),
        XksProxyConnectivity=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_XksProxyConnectivityType(
                    native_input["XksProxyConnectivity"]
                )
            )
            if "XksProxyConnectivity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_UpdateCustomKeyStoreResponse(native_input):
    return DafnyUpdateCustomKeyStoreResponse()


def com_amazonaws_kms_UpdateKeyDescriptionRequest(native_input):
    return DafnyUpdateKeyDescriptionRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Description=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Description"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_UpdatePrimaryRegionRequest(native_input):
    return DafnyUpdatePrimaryRegionRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PrimaryRegion=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["PrimaryRegion"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_kms_VerifyRequest(native_input):
    return DafnyVerifyRequest(
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Message=Seq(native_input["Message"]),
        MessageType=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MessageType(
                    native_input["MessageType"]
                )
            )
            if "MessageType" in native_input.keys()
            else Option_None()
        ),
        Signature=Seq(native_input["Signature"]),
        SigningAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
            native_input["SigningAlgorithm"]
        ),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_VerifyResponse(native_input):
    return DafnyVerifyResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        SignatureValid=(
            Option_Some(native_input["SignatureValid"])
            if "SignatureValid" in native_input.keys()
            else Option_None()
        ),
        SigningAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(
                    native_input["SigningAlgorithm"]
                )
            )
            if "SigningAlgorithm" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_VerifyMacRequest(native_input):
    return DafnyVerifyMacRequest(
        Message=Seq(native_input["Message"]),
        KeyId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        MacAlgorithm=aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MacAlgorithmSpec(
            native_input["MacAlgorithm"]
        ),
        Mac=Seq(native_input["Mac"]),
        GrantTokens=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["GrantTokens"]
                    ]
                )
            )
            if "GrantTokens" in native_input.keys()
            else Option_None()
        ),
        DryRun=(
            Option_Some(native_input["DryRun"])
            if "DryRun" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_kms_VerifyMacResponse(native_input):
    return DafnyVerifyMacResponse(
        KeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["KeyId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "KeyId" in native_input.keys()
            else Option_None()
        ),
        MacValid=(
            Option_Some(native_input["MacValid"])
            if "MacValid" in native_input.keys()
            else Option_None()
        ),
        MacAlgorithm=(
            Option_Some(
                aws_cryptography_internal_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MacAlgorithmSpec(
                    native_input["MacAlgorithm"]
                )
            )
            if "MacAlgorithm" in native_input.keys()
            else Option_None()
        ),
    )
