# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    AlgorithmSpec_RSAES__OAEP__SHA__1,
    AlgorithmSpec_RSAES__OAEP__SHA__256,
    AlgorithmSpec_RSAES__PKCS1__V1__5,
    AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1,
    AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256,
    AlgorithmSpec_SM2PKE,
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
    CustomKeyStoreType_AWS__CLOUDHSM,
    CustomKeyStoreType_EXTERNAL__KEY__STORE,
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
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256,
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT,
    ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE,
    ExpirationModelType_KEY__MATERIAL__EXPIRES,
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
    KeyAgreementAlgorithmSpec_ECDH,
    KeyEncryptionMechanism_RSAES__OAEP__SHA__256,
    KeyManagerType_AWS,
    KeyManagerType_CUSTOMER,
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
    MacAlgorithmSpec_HMAC__SHA__224,
    MacAlgorithmSpec_HMAC__SHA__256,
    MacAlgorithmSpec_HMAC__SHA__384,
    MacAlgorithmSpec_HMAC__SHA__512,
    MessageType_DIGEST,
    MessageType_RAW,
    MultiRegionKeyType_PRIMARY,
    MultiRegionKeyType_REPLICA,
    OriginType_AWS__CLOUDHSM,
    OriginType_AWS__KMS,
    OriginType_EXTERNAL,
    OriginType_EXTERNAL__KEY__STORE,
    RotationType_AUTOMATIC,
    RotationType_ON__DEMAND,
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
    WrappingKeySpec_RSA__2048,
    WrappingKeySpec_RSA__3072,
    WrappingKeySpec_RSA__4096,
    WrappingKeySpec_SM2,
    XksProxyConnectivityType_PUBLIC__ENDPOINT,
    XksProxyConnectivityType_VPC__ENDPOINT__SERVICE,
)
import com_amazonaws_kms.internaldafny.generated.module_
import com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk
from datetime import datetime


def com_amazonaws_kms_AlreadyExistsException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CloudHsmClusterInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CloudHsmClusterInvalidConfigurationException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CloudHsmClusterNotActiveException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CloudHsmClusterNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CloudHsmClusterNotRelatedException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ConflictException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CustomKeyStoreHasCMKsException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CustomKeyStoreInvalidStateException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CustomKeyStoreNameInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CustomKeyStoreNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_DependencyTimeoutException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_DisabledException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_DryRunOperationException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ExpiredImportTokenException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_IncorrectKeyException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_IncorrectKeyMaterialException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_IncorrectTrustAnchorException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidAliasNameException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidArnException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidCiphertextException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidGrantIdException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidGrantTokenException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidImportTokenException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidKeyUsageException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_InvalidMarkerException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KeyUnavailableException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KMSInternalException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KMSInvalidMacException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KMSInvalidSignatureException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KMSInvalidStateException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_LimitExceededException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_MalformedPolicyDocumentException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_NotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_TagException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_UnsupportedOperationException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksKeyAlreadyInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksKeyInvalidConfigurationException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksKeyNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyIncorrectAuthenticationCredentialException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyInvalidConfigurationException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyInvalidResponseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyUriEndpointInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyUriInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyUriUnreachableException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyVpcEndpointServiceInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyVpcEndpointServiceInvalidConfigurationException(
    dafny_input,
):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_XksProxyVpcEndpointServiceNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = dafny_input.message.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CancelKeyDeletionRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_CancelKeyDeletionResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ConnectCustomKeyStoreRequest(dafny_input):
    output = {}
    output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.VerbatimString(False)
    return output


def com_amazonaws_kms_ConnectCustomKeyStoreResponse(dafny_input):
    output = {}
    return output


def com_amazonaws_kms_CreateAliasRequest(dafny_input):
    output = {}
    output["AliasName"] = dafny_input.AliasName.VerbatimString(False)
    output["TargetKeyId"] = dafny_input.TargetKeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_CustomKeyStoreType(dafny_input):
    # Convert CustomKeyStoreType
    if isinstance(dafny_input, CustomKeyStoreType_AWS__CLOUDHSM):
        return "AWS_CLOUDHSM"

    elif isinstance(dafny_input, CustomKeyStoreType_EXTERNAL__KEY__STORE):
        return "EXTERNAL_KEY_STORE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_XksProxyAuthenticationCredentialType(dafny_input):
    output = {}
    output["AccessKeyId"] = dafny_input.AccessKeyId.VerbatimString(False)
    output["RawSecretAccessKey"] = dafny_input.RawSecretAccessKey.VerbatimString(False)
    return output


def com_amazonaws_kms_XksProxyConnectivityType(dafny_input):
    # Convert XksProxyConnectivityType
    if isinstance(dafny_input, XksProxyConnectivityType_PUBLIC__ENDPOINT):
        return "PUBLIC_ENDPOINT"

    elif isinstance(dafny_input, XksProxyConnectivityType_VPC__ENDPOINT__SERVICE):
        return "VPC_ENDPOINT_SERVICE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_CreateCustomKeyStoreRequest(dafny_input):
    output = {}
    output["CustomKeyStoreName"] = dafny_input.CustomKeyStoreName.VerbatimString(False)
    if dafny_input.CloudHsmClusterId.is_Some:
        output["CloudHsmClusterId"] = (
            dafny_input.CloudHsmClusterId.value.VerbatimString(False)
        )

    if dafny_input.TrustAnchorCertificate.is_Some:
        output["TrustAnchorCertificate"] = (
            dafny_input.TrustAnchorCertificate.value.VerbatimString(False)
        )

    if dafny_input.KeyStorePassword.is_Some:
        output["KeyStorePassword"] = dafny_input.KeyStorePassword.value.VerbatimString(
            False
        )

    if dafny_input.CustomKeyStoreType.is_Some:
        output["CustomKeyStoreType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomKeyStoreType(
                dafny_input.CustomKeyStoreType.value
            )
        )

    if dafny_input.XksProxyUriEndpoint.is_Some:
        output["XksProxyUriEndpoint"] = (
            dafny_input.XksProxyUriEndpoint.value.VerbatimString(False)
        )

    if dafny_input.XksProxyUriPath.is_Some:
        output["XksProxyUriPath"] = dafny_input.XksProxyUriPath.value.VerbatimString(
            False
        )

    if dafny_input.XksProxyVpcEndpointServiceName.is_Some:
        output["XksProxyVpcEndpointServiceName"] = (
            dafny_input.XksProxyVpcEndpointServiceName.value.VerbatimString(False)
        )

    if dafny_input.XksProxyAuthenticationCredential.is_Some:
        output["XksProxyAuthenticationCredential"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyAuthenticationCredentialType(
                dafny_input.XksProxyAuthenticationCredential.value
            )
        )

    if dafny_input.XksProxyConnectivity.is_Some:
        output["XksProxyConnectivity"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyConnectivityType(
                dafny_input.XksProxyConnectivity.value
            )
        )

    return output


def com_amazonaws_kms_CreateCustomKeyStoreResponse(dafny_input):
    output = {}
    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    return output


def com_amazonaws_kms_GrantOperation(dafny_input):
    # Convert GrantOperation
    if isinstance(dafny_input, GrantOperation_Decrypt):
        return "Decrypt"

    elif isinstance(dafny_input, GrantOperation_Encrypt):
        return "Encrypt"

    elif isinstance(dafny_input, GrantOperation_GenerateDataKey):
        return "GenerateDataKey"

    elif isinstance(dafny_input, GrantOperation_GenerateDataKeyWithoutPlaintext):
        return "GenerateDataKeyWithoutPlaintext"

    elif isinstance(dafny_input, GrantOperation_ReEncryptFrom):
        return "ReEncryptFrom"

    elif isinstance(dafny_input, GrantOperation_ReEncryptTo):
        return "ReEncryptTo"

    elif isinstance(dafny_input, GrantOperation_Sign):
        return "Sign"

    elif isinstance(dafny_input, GrantOperation_Verify):
        return "Verify"

    elif isinstance(dafny_input, GrantOperation_GetPublicKey):
        return "GetPublicKey"

    elif isinstance(dafny_input, GrantOperation_CreateGrant):
        return "CreateGrant"

    elif isinstance(dafny_input, GrantOperation_RetireGrant):
        return "RetireGrant"

    elif isinstance(dafny_input, GrantOperation_DescribeKey):
        return "DescribeKey"

    elif isinstance(dafny_input, GrantOperation_GenerateDataKeyPair):
        return "GenerateDataKeyPair"

    elif isinstance(dafny_input, GrantOperation_GenerateDataKeyPairWithoutPlaintext):
        return "GenerateDataKeyPairWithoutPlaintext"

    elif isinstance(dafny_input, GrantOperation_GenerateMac):
        return "GenerateMac"

    elif isinstance(dafny_input, GrantOperation_VerifyMac):
        return "VerifyMac"

    elif isinstance(dafny_input, GrantOperation_DeriveSharedSecret):
        return "DeriveSharedSecret"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_GrantConstraints(dafny_input):
    output = {}
    if dafny_input.EncryptionContextSubset.is_Some:
        output["EncryptionContextSubset"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContextSubset.value.items
        }

    if dafny_input.EncryptionContextEquals.is_Some:
        output["EncryptionContextEquals"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContextEquals.value.items
        }

    return output


def com_amazonaws_kms_CreateGrantRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["GranteePrincipal"] = dafny_input.GranteePrincipal.VerbatimString(False)
    if dafny_input.RetiringPrincipal.is_Some:
        output["RetiringPrincipal"] = (
            dafny_input.RetiringPrincipal.value.VerbatimString(False)
        )

    output["Operations"] = [
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GrantOperation(
            list_element
        )
        for list_element in dafny_input.Operations
    ]
    if dafny_input.Constraints.is_Some:
        output["Constraints"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GrantConstraints(
                dafny_input.Constraints.value
            )
        )

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.Name.is_Some:
        output["Name"] = dafny_input.Name.value.VerbatimString(False)

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_CreateGrantResponse(dafny_input):
    output = {}
    if dafny_input.GrantToken.is_Some:
        output["GrantToken"] = dafny_input.GrantToken.value.VerbatimString(False)

    if dafny_input.GrantId.is_Some:
        output["GrantId"] = dafny_input.GrantId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KeyUsageType(dafny_input):
    # Convert KeyUsageType
    if isinstance(dafny_input, KeyUsageType_SIGN__VERIFY):
        return "SIGN_VERIFY"

    elif isinstance(dafny_input, KeyUsageType_ENCRYPT__DECRYPT):
        return "ENCRYPT_DECRYPT"

    elif isinstance(dafny_input, KeyUsageType_GENERATE__VERIFY__MAC):
        return "GENERATE_VERIFY_MAC"

    elif isinstance(dafny_input, KeyUsageType_KEY__AGREEMENT):
        return "KEY_AGREEMENT"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_CustomerMasterKeySpec(dafny_input):
    # Convert CustomerMasterKeySpec
    if isinstance(dafny_input, CustomerMasterKeySpec_RSA__2048):
        return "RSA_2048"

    elif isinstance(dafny_input, CustomerMasterKeySpec_RSA__3072):
        return "RSA_3072"

    elif isinstance(dafny_input, CustomerMasterKeySpec_RSA__4096):
        return "RSA_4096"

    elif isinstance(dafny_input, CustomerMasterKeySpec_ECC__NIST__P256):
        return "ECC_NIST_P256"

    elif isinstance(dafny_input, CustomerMasterKeySpec_ECC__NIST__P384):
        return "ECC_NIST_P384"

    elif isinstance(dafny_input, CustomerMasterKeySpec_ECC__NIST__P521):
        return "ECC_NIST_P521"

    elif isinstance(dafny_input, CustomerMasterKeySpec_ECC__SECG__P256K1):
        return "ECC_SECG_P256K1"

    elif isinstance(dafny_input, CustomerMasterKeySpec_SYMMETRIC__DEFAULT):
        return "SYMMETRIC_DEFAULT"

    elif isinstance(dafny_input, CustomerMasterKeySpec_HMAC__224):
        return "HMAC_224"

    elif isinstance(dafny_input, CustomerMasterKeySpec_HMAC__256):
        return "HMAC_256"

    elif isinstance(dafny_input, CustomerMasterKeySpec_HMAC__384):
        return "HMAC_384"

    elif isinstance(dafny_input, CustomerMasterKeySpec_HMAC__512):
        return "HMAC_512"

    elif isinstance(dafny_input, CustomerMasterKeySpec_SM2):
        return "SM2"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_KeySpec(dafny_input):
    # Convert KeySpec
    if isinstance(dafny_input, KeySpec_RSA__2048):
        return "RSA_2048"

    elif isinstance(dafny_input, KeySpec_RSA__3072):
        return "RSA_3072"

    elif isinstance(dafny_input, KeySpec_RSA__4096):
        return "RSA_4096"

    elif isinstance(dafny_input, KeySpec_ECC__NIST__P256):
        return "ECC_NIST_P256"

    elif isinstance(dafny_input, KeySpec_ECC__NIST__P384):
        return "ECC_NIST_P384"

    elif isinstance(dafny_input, KeySpec_ECC__NIST__P521):
        return "ECC_NIST_P521"

    elif isinstance(dafny_input, KeySpec_ECC__SECG__P256K1):
        return "ECC_SECG_P256K1"

    elif isinstance(dafny_input, KeySpec_SYMMETRIC__DEFAULT):
        return "SYMMETRIC_DEFAULT"

    elif isinstance(dafny_input, KeySpec_HMAC__224):
        return "HMAC_224"

    elif isinstance(dafny_input, KeySpec_HMAC__256):
        return "HMAC_256"

    elif isinstance(dafny_input, KeySpec_HMAC__384):
        return "HMAC_384"

    elif isinstance(dafny_input, KeySpec_HMAC__512):
        return "HMAC_512"

    elif isinstance(dafny_input, KeySpec_SM2):
        return "SM2"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_OriginType(dafny_input):
    # Convert OriginType
    if isinstance(dafny_input, OriginType_AWS__KMS):
        return "AWS_KMS"

    elif isinstance(dafny_input, OriginType_EXTERNAL):
        return "EXTERNAL"

    elif isinstance(dafny_input, OriginType_AWS__CLOUDHSM):
        return "AWS_CLOUDHSM"

    elif isinstance(dafny_input, OriginType_EXTERNAL__KEY__STORE):
        return "EXTERNAL_KEY_STORE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_Tag(dafny_input):
    output = {}
    output["TagKey"] = dafny_input.TagKey.VerbatimString(False)
    output["TagValue"] = dafny_input.TagValue.VerbatimString(False)
    return output


def com_amazonaws_kms_CreateKeyRequest(dafny_input):
    output = {}
    if dafny_input.Policy.is_Some:
        output["Policy"] = dafny_input.Policy.value.VerbatimString(False)

    if dafny_input.Description.is_Some:
        output["Description"] = dafny_input.Description.value.VerbatimString(False)

    if dafny_input.KeyUsage.is_Some:
        output["KeyUsage"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyUsageType(
                dafny_input.KeyUsage.value
            )
        )

    if dafny_input.CustomerMasterKeySpec.is_Some:
        output["CustomerMasterKeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomerMasterKeySpec(
                dafny_input.CustomerMasterKeySpec.value
            )
        )

    if dafny_input.KeySpec.is_Some:
        output["KeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeySpec(
                dafny_input.KeySpec.value
            )
        )

    if dafny_input.Origin.is_Some:
        output["Origin"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_OriginType(
                dafny_input.Origin.value
            )
        )

    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    if dafny_input.BypassPolicyLockoutSafetyCheck.is_Some:
        output["BypassPolicyLockoutSafetyCheck"] = (
            dafny_input.BypassPolicyLockoutSafetyCheck.value
        )

    if dafny_input.Tags.is_Some:
        output["Tags"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_Tag(
                list_element
            )
            for list_element in dafny_input.Tags.value
        ]

    if dafny_input.MultiRegion.is_Some:
        output["MultiRegion"] = dafny_input.MultiRegion.value

    if dafny_input.XksKeyId.is_Some:
        output["XksKeyId"] = dafny_input.XksKeyId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KeyMetadata(dafny_input):
    output = {}
    if dafny_input.AWSAccountId.is_Some:
        output["AWSAccountId"] = dafny_input.AWSAccountId.value.VerbatimString(False)

    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.Arn.is_Some:
        output["Arn"] = dafny_input.Arn.value.VerbatimString(False)

    if dafny_input.CreationDate.is_Some:
        output["CreationDate"] = datetime.fromisoformat(
            dafny_input.CreationDate.value.VerbatimString(False)
        )

    if dafny_input.Enabled.is_Some:
        output["Enabled"] = dafny_input.Enabled.value

    if dafny_input.Description.is_Some:
        output["Description"] = dafny_input.Description.value.VerbatimString(False)

    if dafny_input.KeyUsage.is_Some:
        output["KeyUsage"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyUsageType(
                dafny_input.KeyUsage.value
            )
        )

    if dafny_input.KeyState.is_Some:
        output["KeyState"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyState(
                dafny_input.KeyState.value
            )
        )

    if dafny_input.DeletionDate.is_Some:
        output["DeletionDate"] = datetime.fromisoformat(
            dafny_input.DeletionDate.value.VerbatimString(False)
        )

    if dafny_input.ValidTo.is_Some:
        output["ValidTo"] = datetime.fromisoformat(
            dafny_input.ValidTo.value.VerbatimString(False)
        )

    if dafny_input.Origin.is_Some:
        output["Origin"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_OriginType(
                dafny_input.Origin.value
            )
        )

    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    if dafny_input.CloudHsmClusterId.is_Some:
        output["CloudHsmClusterId"] = (
            dafny_input.CloudHsmClusterId.value.VerbatimString(False)
        )

    if dafny_input.ExpirationModel.is_Some:
        output["ExpirationModel"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ExpirationModelType(
                dafny_input.ExpirationModel.value
            )
        )

    if dafny_input.KeyManager.is_Some:
        output["KeyManager"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyManagerType(
                dafny_input.KeyManager.value
            )
        )

    if dafny_input.CustomerMasterKeySpec.is_Some:
        output["CustomerMasterKeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomerMasterKeySpec(
                dafny_input.CustomerMasterKeySpec.value
            )
        )

    if dafny_input.KeySpec.is_Some:
        output["KeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeySpec(
                dafny_input.KeySpec.value
            )
        )

    if dafny_input.EncryptionAlgorithms.is_Some:
        output["EncryptionAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.EncryptionAlgorithms.value
        ]

    if dafny_input.SigningAlgorithms.is_Some:
        output["SigningAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.SigningAlgorithms.value
        ]

    if dafny_input.KeyAgreementAlgorithms.is_Some:
        output["KeyAgreementAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.KeyAgreementAlgorithms.value
        ]

    if dafny_input.MultiRegion.is_Some:
        output["MultiRegion"] = dafny_input.MultiRegion.value

    if dafny_input.MultiRegionConfiguration.is_Some:
        output["MultiRegionConfiguration"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MultiRegionConfiguration(
                dafny_input.MultiRegionConfiguration.value
            )
        )

    if dafny_input.PendingDeletionWindowInDays.is_Some:
        output["PendingDeletionWindowInDays"] = (
            dafny_input.PendingDeletionWindowInDays.value
        )

    if dafny_input.MacAlgorithms.is_Some:
        output["MacAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MacAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.MacAlgorithms.value
        ]

    if dafny_input.XksKeyConfiguration.is_Some:
        output["XksKeyConfiguration"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksKeyConfigurationType(
                dafny_input.XksKeyConfiguration.value
            )
        )

    return output


def com_amazonaws_kms_KeyState(dafny_input):
    # Convert KeyState
    if isinstance(dafny_input, KeyState_Creating):
        return "Creating"

    elif isinstance(dafny_input, KeyState_Enabled):
        return "Enabled"

    elif isinstance(dafny_input, KeyState_Disabled):
        return "Disabled"

    elif isinstance(dafny_input, KeyState_PendingDeletion):
        return "PendingDeletion"

    elif isinstance(dafny_input, KeyState_PendingImport):
        return "PendingImport"

    elif isinstance(dafny_input, KeyState_PendingReplicaDeletion):
        return "PendingReplicaDeletion"

    elif isinstance(dafny_input, KeyState_Unavailable):
        return "Unavailable"

    elif isinstance(dafny_input, KeyState_Updating):
        return "Updating"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_ExpirationModelType(dafny_input):
    # Convert ExpirationModelType
    if isinstance(dafny_input, ExpirationModelType_KEY__MATERIAL__EXPIRES):
        return "KEY_MATERIAL_EXPIRES"

    elif isinstance(dafny_input, ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE):
        return "KEY_MATERIAL_DOES_NOT_EXPIRE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_KeyManagerType(dafny_input):
    # Convert KeyManagerType
    if isinstance(dafny_input, KeyManagerType_AWS):
        return "AWS"

    elif isinstance(dafny_input, KeyManagerType_CUSTOMER):
        return "CUSTOMER"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_EncryptionAlgorithmSpec(dafny_input):
    # Convert EncryptionAlgorithmSpec
    if isinstance(dafny_input, EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT):
        return "SYMMETRIC_DEFAULT"

    elif isinstance(dafny_input, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1):
        return "RSAES_OAEP_SHA_1"

    elif isinstance(dafny_input, EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256):
        return "RSAES_OAEP_SHA_256"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_SigningAlgorithmSpec(dafny_input):
    # Convert SigningAlgorithmSpec
    if isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PSS__SHA__256):
        return "RSASSA_PSS_SHA_256"

    elif isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PSS__SHA__384):
        return "RSASSA_PSS_SHA_384"

    elif isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PSS__SHA__512):
        return "RSASSA_PSS_SHA_512"

    elif isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256):
        return "RSASSA_PKCS1_V1_5_SHA_256"

    elif isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384):
        return "RSASSA_PKCS1_V1_5_SHA_384"

    elif isinstance(dafny_input, SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512):
        return "RSASSA_PKCS1_V1_5_SHA_512"

    elif isinstance(dafny_input, SigningAlgorithmSpec_ECDSA__SHA__256):
        return "ECDSA_SHA_256"

    elif isinstance(dafny_input, SigningAlgorithmSpec_ECDSA__SHA__384):
        return "ECDSA_SHA_384"

    elif isinstance(dafny_input, SigningAlgorithmSpec_ECDSA__SHA__512):
        return "ECDSA_SHA_512"

    elif isinstance(dafny_input, SigningAlgorithmSpec_SM2DSA):
        return "SM2DSA"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_KeyAgreementAlgorithmSpec(dafny_input):
    # Convert KeyAgreementAlgorithmSpec
    if isinstance(dafny_input, KeyAgreementAlgorithmSpec_ECDH):
        return "ECDH"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_MultiRegionConfiguration(dafny_input):
    output = {}
    if dafny_input.MultiRegionKeyType.is_Some:
        output["MultiRegionKeyType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MultiRegionKeyType(
                dafny_input.MultiRegionKeyType.value
            )
        )

    if dafny_input.PrimaryKey.is_Some:
        output["PrimaryKey"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MultiRegionKey(
                dafny_input.PrimaryKey.value
            )
        )

    if dafny_input.ReplicaKeys.is_Some:
        output["ReplicaKeys"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MultiRegionKey(
                list_element
            )
            for list_element in dafny_input.ReplicaKeys.value
        ]

    return output


def com_amazonaws_kms_MacAlgorithmSpec(dafny_input):
    # Convert MacAlgorithmSpec
    if isinstance(dafny_input, MacAlgorithmSpec_HMAC__SHA__224):
        return "HMAC_SHA_224"

    elif isinstance(dafny_input, MacAlgorithmSpec_HMAC__SHA__256):
        return "HMAC_SHA_256"

    elif isinstance(dafny_input, MacAlgorithmSpec_HMAC__SHA__384):
        return "HMAC_SHA_384"

    elif isinstance(dafny_input, MacAlgorithmSpec_HMAC__SHA__512):
        return "HMAC_SHA_512"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_XksKeyConfigurationType(dafny_input):
    output = {}
    if dafny_input.Id.is_Some:
        output["Id"] = dafny_input.Id.value.VerbatimString(False)

    return output


def com_amazonaws_kms_MultiRegionKeyType(dafny_input):
    # Convert MultiRegionKeyType
    if isinstance(dafny_input, MultiRegionKeyType_PRIMARY):
        return "PRIMARY"

    elif isinstance(dafny_input, MultiRegionKeyType_REPLICA):
        return "REPLICA"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_MultiRegionKey(dafny_input):
    output = {}
    if dafny_input.Arn.is_Some:
        output["Arn"] = dafny_input.Arn.value.VerbatimString(False)

    if dafny_input.Region.is_Some:
        output["Region"] = dafny_input.Region.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CreateKeyResponse(dafny_input):
    output = {}
    if dafny_input.KeyMetadata.is_Some:
        output["KeyMetadata"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyMetadata(
                dafny_input.KeyMetadata.value
            )
        )

    return output


def com_amazonaws_kms_RecipientInfo(dafny_input):
    output = {}
    if dafny_input.KeyEncryptionAlgorithm.is_Some:
        output["KeyEncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyEncryptionMechanism(
                dafny_input.KeyEncryptionAlgorithm.value
            )
        )

    if dafny_input.AttestationDocument.is_Some:
        output["AttestationDocument"] = bytes(dafny_input.AttestationDocument.value)

    return output


def com_amazonaws_kms_KeyEncryptionMechanism(dafny_input):
    # Convert KeyEncryptionMechanism
    if isinstance(dafny_input, KeyEncryptionMechanism_RSAES__OAEP__SHA__256):
        return "RSAES_OAEP_SHA_256"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_DecryptRequest(dafny_input):
    output = {}
    output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob)
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.EncryptionAlgorithm.is_Some:
        output["EncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.EncryptionAlgorithm.value
            )
        )

    if dafny_input.Recipient.is_Some:
        output["Recipient"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RecipientInfo(
                dafny_input.Recipient.value
            )
        )

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_DecryptResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.Plaintext.is_Some:
        output["Plaintext"] = bytes(dafny_input.Plaintext.value)

    if dafny_input.EncryptionAlgorithm.is_Some:
        output["EncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.EncryptionAlgorithm.value
            )
        )

    if dafny_input.CiphertextForRecipient.is_Some:
        output["CiphertextForRecipient"] = bytes(
            dafny_input.CiphertextForRecipient.value
        )

    return output


def com_amazonaws_kms_DeleteAliasRequest(dafny_input):
    output = {}
    output["AliasName"] = dafny_input.AliasName.VerbatimString(False)
    return output


def com_amazonaws_kms_DeleteCustomKeyStoreRequest(dafny_input):
    output = {}
    output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.VerbatimString(False)
    return output


def com_amazonaws_kms_DeleteCustomKeyStoreResponse(dafny_input):
    output = {}
    return output


def com_amazonaws_kms_DeleteImportedKeyMaterialRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_DeriveSharedSecretRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["KeyAgreementAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
            dafny_input.KeyAgreementAlgorithm
        )
    )
    output["PublicKey"] = bytes(dafny_input.PublicKey)
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    if dafny_input.Recipient.is_Some:
        output["Recipient"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RecipientInfo(
                dafny_input.Recipient.value
            )
        )

    return output


def com_amazonaws_kms_DeriveSharedSecretResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.SharedSecret.is_Some:
        output["SharedSecret"] = bytes(dafny_input.SharedSecret.value)

    if dafny_input.CiphertextForRecipient.is_Some:
        output["CiphertextForRecipient"] = bytes(
            dafny_input.CiphertextForRecipient.value
        )

    if dafny_input.KeyAgreementAlgorithm.is_Some:
        output["KeyAgreementAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                dafny_input.KeyAgreementAlgorithm.value
            )
        )

    if dafny_input.KeyOrigin.is_Some:
        output["KeyOrigin"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_OriginType(
                dafny_input.KeyOrigin.value
            )
        )

    return output


def com_amazonaws_kms_DescribeCustomKeyStoresRequest(dafny_input):
    output = {}
    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    if dafny_input.CustomKeyStoreName.is_Some:
        output["CustomKeyStoreName"] = (
            dafny_input.CustomKeyStoreName.value.VerbatimString(False)
        )

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_CustomKeyStoresListEntry(dafny_input):
    output = {}
    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    if dafny_input.CustomKeyStoreName.is_Some:
        output["CustomKeyStoreName"] = (
            dafny_input.CustomKeyStoreName.value.VerbatimString(False)
        )

    if dafny_input.CloudHsmClusterId.is_Some:
        output["CloudHsmClusterId"] = (
            dafny_input.CloudHsmClusterId.value.VerbatimString(False)
        )

    if dafny_input.TrustAnchorCertificate.is_Some:
        output["TrustAnchorCertificate"] = (
            dafny_input.TrustAnchorCertificate.value.VerbatimString(False)
        )

    if dafny_input.ConnectionState.is_Some:
        output["ConnectionState"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ConnectionStateType(
                dafny_input.ConnectionState.value
            )
        )

    if dafny_input.ConnectionErrorCode.is_Some:
        output["ConnectionErrorCode"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ConnectionErrorCodeType(
                dafny_input.ConnectionErrorCode.value
            )
        )

    if dafny_input.CreationDate.is_Some:
        output["CreationDate"] = datetime.fromisoformat(
            dafny_input.CreationDate.value.VerbatimString(False)
        )

    if dafny_input.CustomKeyStoreType.is_Some:
        output["CustomKeyStoreType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomKeyStoreType(
                dafny_input.CustomKeyStoreType.value
            )
        )

    if dafny_input.XksProxyConfiguration.is_Some:
        output["XksProxyConfiguration"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyConfigurationType(
                dafny_input.XksProxyConfiguration.value
            )
        )

    return output


def com_amazonaws_kms_ConnectionStateType(dafny_input):
    # Convert ConnectionStateType
    if isinstance(dafny_input, ConnectionStateType_CONNECTED):
        return "CONNECTED"

    elif isinstance(dafny_input, ConnectionStateType_CONNECTING):
        return "CONNECTING"

    elif isinstance(dafny_input, ConnectionStateType_FAILED):
        return "FAILED"

    elif isinstance(dafny_input, ConnectionStateType_DISCONNECTED):
        return "DISCONNECTED"

    elif isinstance(dafny_input, ConnectionStateType_DISCONNECTING):
        return "DISCONNECTING"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_ConnectionErrorCodeType(dafny_input):
    # Convert ConnectionErrorCodeType
    if isinstance(dafny_input, ConnectionErrorCodeType_INVALID__CREDENTIALS):
        return "INVALID_CREDENTIALS"

    elif isinstance(dafny_input, ConnectionErrorCodeType_CLUSTER__NOT__FOUND):
        return "CLUSTER_NOT_FOUND"

    elif isinstance(dafny_input, ConnectionErrorCodeType_NETWORK__ERRORS):
        return "NETWORK_ERRORS"

    elif isinstance(dafny_input, ConnectionErrorCodeType_INTERNAL__ERROR):
        return "INTERNAL_ERROR"

    elif isinstance(dafny_input, ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS):
        return "INSUFFICIENT_CLOUDHSM_HSMS"

    elif isinstance(dafny_input, ConnectionErrorCodeType_USER__LOCKED__OUT):
        return "USER_LOCKED_OUT"

    elif isinstance(dafny_input, ConnectionErrorCodeType_USER__NOT__FOUND):
        return "USER_NOT_FOUND"

    elif isinstance(dafny_input, ConnectionErrorCodeType_USER__LOGGED__IN):
        return "USER_LOGGED_IN"

    elif isinstance(dafny_input, ConnectionErrorCodeType_SUBNET__NOT__FOUND):
        return "SUBNET_NOT_FOUND"

    elif isinstance(
        dafny_input, ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET
    ):
        return "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET"

    elif isinstance(dafny_input, ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED):
        return "XKS_PROXY_ACCESS_DENIED"

    elif isinstance(dafny_input, ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE):
        return "XKS_PROXY_NOT_REACHABLE"

    elif isinstance(
        dafny_input, ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND
    ):
        return "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND"

    elif isinstance(dafny_input, ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE):
        return "XKS_PROXY_INVALID_RESPONSE"

    elif isinstance(
        dafny_input, ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION
    ):
        return "XKS_PROXY_INVALID_CONFIGURATION"

    elif isinstance(
        dafny_input,
        ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION,
    ):
        return "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION"

    elif isinstance(dafny_input, ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT):
        return "XKS_PROXY_TIMED_OUT"

    elif isinstance(
        dafny_input, ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION
    ):
        return "XKS_PROXY_INVALID_TLS_CONFIGURATION"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_XksProxyConfigurationType(dafny_input):
    output = {}
    if dafny_input.Connectivity.is_Some:
        output["Connectivity"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyConnectivityType(
                dafny_input.Connectivity.value
            )
        )

    if dafny_input.AccessKeyId.is_Some:
        output["AccessKeyId"] = dafny_input.AccessKeyId.value.VerbatimString(False)

    if dafny_input.UriEndpoint.is_Some:
        output["UriEndpoint"] = dafny_input.UriEndpoint.value.VerbatimString(False)

    if dafny_input.UriPath.is_Some:
        output["UriPath"] = dafny_input.UriPath.value.VerbatimString(False)

    if dafny_input.VpcEndpointServiceName.is_Some:
        output["VpcEndpointServiceName"] = (
            dafny_input.VpcEndpointServiceName.value.VerbatimString(False)
        )

    return output


def com_amazonaws_kms_DescribeCustomKeyStoresResponse(dafny_input):
    output = {}
    if dafny_input.CustomKeyStores.is_Some:
        output["CustomKeyStores"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomKeyStoresListEntry(
                list_element
            )
            for list_element in dafny_input.CustomKeyStores.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_DescribeKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    return output


def com_amazonaws_kms_DescribeKeyResponse(dafny_input):
    output = {}
    if dafny_input.KeyMetadata.is_Some:
        output["KeyMetadata"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyMetadata(
                dafny_input.KeyMetadata.value
            )
        )

    return output


def com_amazonaws_kms_DisableKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_DisableKeyRotationRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_DisconnectCustomKeyStoreRequest(dafny_input):
    output = {}
    output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.VerbatimString(False)
    return output


def com_amazonaws_kms_DisconnectCustomKeyStoreResponse(dafny_input):
    output = {}
    return output


def com_amazonaws_kms_EnableKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_EnableKeyRotationRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.RotationPeriodInDays.is_Some:
        output["RotationPeriodInDays"] = dafny_input.RotationPeriodInDays.value

    return output


def com_amazonaws_kms_EncryptRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["Plaintext"] = bytes(dafny_input.Plaintext)
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.EncryptionAlgorithm.is_Some:
        output["EncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.EncryptionAlgorithm.value
            )
        )

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_EncryptResponse(dafny_input):
    output = {}
    if dafny_input.CiphertextBlob.is_Some:
        output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob.value)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.EncryptionAlgorithm.is_Some:
        output["EncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.EncryptionAlgorithm.value
            )
        )

    return output


def com_amazonaws_kms_DataKeySpec(dafny_input):
    # Convert DataKeySpec
    if isinstance(dafny_input, DataKeySpec_AES__256):
        return "AES_256"

    elif isinstance(dafny_input, DataKeySpec_AES__128):
        return "AES_128"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_GenerateDataKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    if dafny_input.NumberOfBytes.is_Some:
        output["NumberOfBytes"] = dafny_input.NumberOfBytes.value

    if dafny_input.KeySpec.is_Some:
        output["KeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeySpec(
                dafny_input.KeySpec.value
            )
        )

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.Recipient.is_Some:
        output["Recipient"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RecipientInfo(
                dafny_input.Recipient.value
            )
        )

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_GenerateDataKeyResponse(dafny_input):
    output = {}
    if dafny_input.CiphertextBlob.is_Some:
        output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob.value)

    if dafny_input.Plaintext.is_Some:
        output["Plaintext"] = bytes(dafny_input.Plaintext.value)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.CiphertextForRecipient.is_Some:
        output["CiphertextForRecipient"] = bytes(
            dafny_input.CiphertextForRecipient.value
        )

    return output


def com_amazonaws_kms_DataKeyPairSpec(dafny_input):
    # Convert DataKeyPairSpec
    if isinstance(dafny_input, DataKeyPairSpec_RSA__2048):
        return "RSA_2048"

    elif isinstance(dafny_input, DataKeyPairSpec_RSA__3072):
        return "RSA_3072"

    elif isinstance(dafny_input, DataKeyPairSpec_RSA__4096):
        return "RSA_4096"

    elif isinstance(dafny_input, DataKeyPairSpec_ECC__NIST__P256):
        return "ECC_NIST_P256"

    elif isinstance(dafny_input, DataKeyPairSpec_ECC__NIST__P384):
        return "ECC_NIST_P384"

    elif isinstance(dafny_input, DataKeyPairSpec_ECC__NIST__P521):
        return "ECC_NIST_P521"

    elif isinstance(dafny_input, DataKeyPairSpec_ECC__SECG__P256K1):
        return "ECC_SECG_P256K1"

    elif isinstance(dafny_input, DataKeyPairSpec_SM2):
        return "SM2"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_GenerateDataKeyPairRequest(dafny_input):
    output = {}
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["KeyPairSpec"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeyPairSpec(
            dafny_input.KeyPairSpec
        )
    )
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.Recipient.is_Some:
        output["Recipient"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RecipientInfo(
                dafny_input.Recipient.value
            )
        )

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_GenerateDataKeyPairResponse(dafny_input):
    output = {}
    if dafny_input.PrivateKeyCiphertextBlob.is_Some:
        output["PrivateKeyCiphertextBlob"] = bytes(
            dafny_input.PrivateKeyCiphertextBlob.value
        )

    if dafny_input.PrivateKeyPlaintext.is_Some:
        output["PrivateKeyPlaintext"] = bytes(dafny_input.PrivateKeyPlaintext.value)

    if dafny_input.PublicKey.is_Some:
        output["PublicKey"] = bytes(dafny_input.PublicKey.value)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.KeyPairSpec.is_Some:
        output["KeyPairSpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeyPairSpec(
                dafny_input.KeyPairSpec.value
            )
        )

    if dafny_input.CiphertextForRecipient.is_Some:
        output["CiphertextForRecipient"] = bytes(
            dafny_input.CiphertextForRecipient.value
        )

    return output


def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextRequest(dafny_input):
    output = {}
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["KeyPairSpec"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeyPairSpec(
            dafny_input.KeyPairSpec
        )
    )
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextResponse(dafny_input):
    output = {}
    if dafny_input.PrivateKeyCiphertextBlob.is_Some:
        output["PrivateKeyCiphertextBlob"] = bytes(
            dafny_input.PrivateKeyCiphertextBlob.value
        )

    if dafny_input.PublicKey.is_Some:
        output["PublicKey"] = bytes(dafny_input.PublicKey.value)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.KeyPairSpec.is_Some:
        output["KeyPairSpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeyPairSpec(
                dafny_input.KeyPairSpec.value
            )
        )

    return output


def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.EncryptionContext.is_Some:
        output["EncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.EncryptionContext.value.items
        }

    if dafny_input.KeySpec.is_Some:
        output["KeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_DataKeySpec(
                dafny_input.KeySpec.value
            )
        )

    if dafny_input.NumberOfBytes.is_Some:
        output["NumberOfBytes"] = dafny_input.NumberOfBytes.value

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextResponse(dafny_input):
    output = {}
    if dafny_input.CiphertextBlob.is_Some:
        output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob.value)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_GenerateMacRequest(dafny_input):
    output = {}
    output["Message"] = bytes(dafny_input.Message)
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["MacAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MacAlgorithmSpec(
            dafny_input.MacAlgorithm
        )
    )
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_GenerateMacResponse(dafny_input):
    output = {}
    if dafny_input.Mac.is_Some:
        output["Mac"] = bytes(dafny_input.Mac.value)

    if dafny_input.MacAlgorithm.is_Some:
        output["MacAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MacAlgorithmSpec(
                dafny_input.MacAlgorithm.value
            )
        )

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_GenerateRandomRequest(dafny_input):
    output = {}
    if dafny_input.NumberOfBytes.is_Some:
        output["NumberOfBytes"] = dafny_input.NumberOfBytes.value

    if dafny_input.CustomKeyStoreId.is_Some:
        output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.value.VerbatimString(
            False
        )

    if dafny_input.Recipient.is_Some:
        output["Recipient"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RecipientInfo(
                dafny_input.Recipient.value
            )
        )

    return output


def com_amazonaws_kms_GenerateRandomResponse(dafny_input):
    output = {}
    if dafny_input.Plaintext.is_Some:
        output["Plaintext"] = bytes(dafny_input.Plaintext.value)

    if dafny_input.CiphertextForRecipient.is_Some:
        output["CiphertextForRecipient"] = bytes(
            dafny_input.CiphertextForRecipient.value
        )

    return output


def com_amazonaws_kms_GetKeyPolicyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.PolicyName.is_Some:
        output["PolicyName"] = dafny_input.PolicyName.value.VerbatimString(False)

    return output


def com_amazonaws_kms_GetKeyPolicyResponse(dafny_input):
    output = {}
    if dafny_input.Policy.is_Some:
        output["Policy"] = dafny_input.Policy.value.VerbatimString(False)

    if dafny_input.PolicyName.is_Some:
        output["PolicyName"] = dafny_input.PolicyName.value.VerbatimString(False)

    return output


def com_amazonaws_kms_GetKeyRotationStatusRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_GetKeyRotationStatusResponse(dafny_input):
    output = {}
    if dafny_input.KeyRotationEnabled.is_Some:
        output["KeyRotationEnabled"] = dafny_input.KeyRotationEnabled.value

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.RotationPeriodInDays.is_Some:
        output["RotationPeriodInDays"] = dafny_input.RotationPeriodInDays.value

    if dafny_input.NextRotationDate.is_Some:
        output["NextRotationDate"] = datetime.fromisoformat(
            dafny_input.NextRotationDate.value.VerbatimString(False)
        )

    if dafny_input.OnDemandRotationStartDate.is_Some:
        output["OnDemandRotationStartDate"] = datetime.fromisoformat(
            dafny_input.OnDemandRotationStartDate.value.VerbatimString(False)
        )

    return output


def com_amazonaws_kms_AlgorithmSpec(dafny_input):
    # Convert AlgorithmSpec
    if isinstance(dafny_input, AlgorithmSpec_RSAES__PKCS1__V1__5):
        return "RSAES_PKCS1_V1_5"

    elif isinstance(dafny_input, AlgorithmSpec_RSAES__OAEP__SHA__1):
        return "RSAES_OAEP_SHA_1"

    elif isinstance(dafny_input, AlgorithmSpec_RSAES__OAEP__SHA__256):
        return "RSAES_OAEP_SHA_256"

    elif isinstance(dafny_input, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1):
        return "RSA_AES_KEY_WRAP_SHA_1"

    elif isinstance(dafny_input, AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__256):
        return "RSA_AES_KEY_WRAP_SHA_256"

    elif isinstance(dafny_input, AlgorithmSpec_SM2PKE):
        return "SM2PKE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_WrappingKeySpec(dafny_input):
    # Convert WrappingKeySpec
    if isinstance(dafny_input, WrappingKeySpec_RSA__2048):
        return "RSA_2048"

    elif isinstance(dafny_input, WrappingKeySpec_RSA__3072):
        return "RSA_3072"

    elif isinstance(dafny_input, WrappingKeySpec_RSA__4096):
        return "RSA_4096"

    elif isinstance(dafny_input, WrappingKeySpec_SM2):
        return "SM2"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_GetParametersForImportRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["WrappingAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_AlgorithmSpec(
            dafny_input.WrappingAlgorithm
        )
    )
    output["WrappingKeySpec"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_WrappingKeySpec(
            dafny_input.WrappingKeySpec
        )
    )
    return output


def com_amazonaws_kms_GetParametersForImportResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.ImportToken.is_Some:
        output["ImportToken"] = bytes(dafny_input.ImportToken.value)

    if dafny_input.PublicKey.is_Some:
        output["PublicKey"] = bytes(dafny_input.PublicKey.value)

    if dafny_input.ParametersValidTo.is_Some:
        output["ParametersValidTo"] = datetime.fromisoformat(
            dafny_input.ParametersValidTo.value.VerbatimString(False)
        )

    return output


def com_amazonaws_kms_GetPublicKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    return output


def com_amazonaws_kms_GetPublicKeyResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.PublicKey.is_Some:
        output["PublicKey"] = bytes(dafny_input.PublicKey.value)

    if dafny_input.CustomerMasterKeySpec.is_Some:
        output["CustomerMasterKeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_CustomerMasterKeySpec(
                dafny_input.CustomerMasterKeySpec.value
            )
        )

    if dafny_input.KeySpec.is_Some:
        output["KeySpec"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeySpec(
                dafny_input.KeySpec.value
            )
        )

    if dafny_input.KeyUsage.is_Some:
        output["KeyUsage"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyUsageType(
                dafny_input.KeyUsage.value
            )
        )

    if dafny_input.EncryptionAlgorithms.is_Some:
        output["EncryptionAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.EncryptionAlgorithms.value
        ]

    if dafny_input.SigningAlgorithms.is_Some:
        output["SigningAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.SigningAlgorithms.value
        ]

    if dafny_input.KeyAgreementAlgorithms.is_Some:
        output["KeyAgreementAlgorithms"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyAgreementAlgorithmSpec(
                list_element
            )
            for list_element in dafny_input.KeyAgreementAlgorithms.value
        ]

    return output


def com_amazonaws_kms_ImportKeyMaterialRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["ImportToken"] = bytes(dafny_input.ImportToken)
    output["EncryptedKeyMaterial"] = bytes(dafny_input.EncryptedKeyMaterial)
    if dafny_input.ValidTo.is_Some:
        output["ValidTo"] = datetime.fromisoformat(
            dafny_input.ValidTo.value.VerbatimString(False)
        )

    if dafny_input.ExpirationModel.is_Some:
        output["ExpirationModel"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_ExpirationModelType(
                dafny_input.ExpirationModel.value
            )
        )

    return output


def com_amazonaws_kms_ImportKeyMaterialResponse(dafny_input):
    output = {}
    return output


def com_amazonaws_kms_ListAliasesRequest(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_AliasListEntry(dafny_input):
    output = {}
    if dafny_input.AliasName.is_Some:
        output["AliasName"] = dafny_input.AliasName.value.VerbatimString(False)

    if dafny_input.AliasArn.is_Some:
        output["AliasArn"] = dafny_input.AliasArn.value.VerbatimString(False)

    if dafny_input.TargetKeyId.is_Some:
        output["TargetKeyId"] = dafny_input.TargetKeyId.value.VerbatimString(False)

    if dafny_input.CreationDate.is_Some:
        output["CreationDate"] = datetime.fromisoformat(
            dafny_input.CreationDate.value.VerbatimString(False)
        )

    if dafny_input.LastUpdatedDate.is_Some:
        output["LastUpdatedDate"] = datetime.fromisoformat(
            dafny_input.LastUpdatedDate.value.VerbatimString(False)
        )

    return output


def com_amazonaws_kms_ListAliasesResponse(dafny_input):
    output = {}
    if dafny_input.Aliases.is_Some:
        output["Aliases"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_AliasListEntry(
                list_element
            )
            for list_element in dafny_input.Aliases.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_ListGrantsRequest(dafny_input):
    output = {}
    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.GrantId.is_Some:
        output["GrantId"] = dafny_input.GrantId.value.VerbatimString(False)

    if dafny_input.GranteePrincipal.is_Some:
        output["GranteePrincipal"] = dafny_input.GranteePrincipal.value.VerbatimString(
            False
        )

    return output


def com_amazonaws_kms_GrantListEntry(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.GrantId.is_Some:
        output["GrantId"] = dafny_input.GrantId.value.VerbatimString(False)

    if dafny_input.Name.is_Some:
        output["Name"] = dafny_input.Name.value.VerbatimString(False)

    if dafny_input.CreationDate.is_Some:
        output["CreationDate"] = datetime.fromisoformat(
            dafny_input.CreationDate.value.VerbatimString(False)
        )

    if dafny_input.GranteePrincipal.is_Some:
        output["GranteePrincipal"] = dafny_input.GranteePrincipal.value.VerbatimString(
            False
        )

    if dafny_input.RetiringPrincipal.is_Some:
        output["RetiringPrincipal"] = (
            dafny_input.RetiringPrincipal.value.VerbatimString(False)
        )

    if dafny_input.IssuingAccount.is_Some:
        output["IssuingAccount"] = dafny_input.IssuingAccount.value.VerbatimString(
            False
        )

    if dafny_input.Operations.is_Some:
        output["Operations"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GrantOperation(
                list_element
            )
            for list_element in dafny_input.Operations.value
        ]

    if dafny_input.Constraints.is_Some:
        output["Constraints"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GrantConstraints(
                dafny_input.Constraints.value
            )
        )

    return output


def com_amazonaws_kms_ListGrantsResponse(dafny_input):
    output = {}
    if dafny_input.Grants.is_Some:
        output["Grants"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_GrantListEntry(
                list_element
            )
            for list_element in dafny_input.Grants.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_ListKeyPoliciesRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ListKeyPoliciesResponse(dafny_input):
    output = {}
    if dafny_input.PolicyNames.is_Some:
        output["PolicyNames"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.PolicyNames.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_ListKeyRotationsRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_RotationsListEntry(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.RotationDate.is_Some:
        output["RotationDate"] = datetime.fromisoformat(
            dafny_input.RotationDate.value.VerbatimString(False)
        )

    if dafny_input.RotationType.is_Some:
        output["RotationType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RotationType(
                dafny_input.RotationType.value
            )
        )

    return output


def com_amazonaws_kms_RotationType(dafny_input):
    # Convert RotationType
    if isinstance(dafny_input, RotationType_AUTOMATIC):
        return "AUTOMATIC"

    elif isinstance(dafny_input, RotationType_ON__DEMAND):
        return "ON_DEMAND"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_ListKeyRotationsResponse(dafny_input):
    output = {}
    if dafny_input.Rotations.is_Some:
        output["Rotations"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_RotationsListEntry(
                list_element
            )
            for list_element in dafny_input.Rotations.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_ListKeysRequest(dafny_input):
    output = {}
    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_KeyListEntry(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.KeyArn.is_Some:
        output["KeyArn"] = dafny_input.KeyArn.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ListKeysResponse(dafny_input):
    output = {}
    if dafny_input.Keys.is_Some:
        output["Keys"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyListEntry(
                list_element
            )
            for list_element in dafny_input.Keys.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_ListResourceTagsRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Marker.is_Some:
        output["Marker"] = dafny_input.Marker.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ListResourceTagsResponse(dafny_input):
    output = {}
    if dafny_input.Tags.is_Some:
        output["Tags"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_Tag(
                list_element
            )
            for list_element in dafny_input.Tags.value
        ]

    if dafny_input.NextMarker.is_Some:
        output["NextMarker"] = dafny_input.NextMarker.value.VerbatimString(False)

    if dafny_input.Truncated.is_Some:
        output["Truncated"] = dafny_input.Truncated.value

    return output


def com_amazonaws_kms_PutKeyPolicyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.PolicyName.is_Some:
        output["PolicyName"] = dafny_input.PolicyName.value.VerbatimString(False)

    output["Policy"] = dafny_input.Policy.VerbatimString(False)
    if dafny_input.BypassPolicyLockoutSafetyCheck.is_Some:
        output["BypassPolicyLockoutSafetyCheck"] = (
            dafny_input.BypassPolicyLockoutSafetyCheck.value
        )

    return output


def com_amazonaws_kms_ReEncryptRequest(dafny_input):
    output = {}
    output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob)
    if dafny_input.SourceEncryptionContext.is_Some:
        output["SourceEncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.SourceEncryptionContext.value.items
        }

    if dafny_input.SourceKeyId.is_Some:
        output["SourceKeyId"] = dafny_input.SourceKeyId.value.VerbatimString(False)

    output["DestinationKeyId"] = dafny_input.DestinationKeyId.VerbatimString(False)
    if dafny_input.DestinationEncryptionContext.is_Some:
        output["DestinationEncryptionContext"] = {
            key.VerbatimString(False): value.VerbatimString(False)
            for (key, value) in dafny_input.DestinationEncryptionContext.value.items
        }

    if dafny_input.SourceEncryptionAlgorithm.is_Some:
        output["SourceEncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.SourceEncryptionAlgorithm.value
            )
        )

    if dafny_input.DestinationEncryptionAlgorithm.is_Some:
        output["DestinationEncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.DestinationEncryptionAlgorithm.value
            )
        )

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_ReEncryptResponse(dafny_input):
    output = {}
    if dafny_input.CiphertextBlob.is_Some:
        output["CiphertextBlob"] = bytes(dafny_input.CiphertextBlob.value)

    if dafny_input.SourceKeyId.is_Some:
        output["SourceKeyId"] = dafny_input.SourceKeyId.value.VerbatimString(False)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.SourceEncryptionAlgorithm.is_Some:
        output["SourceEncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.SourceEncryptionAlgorithm.value
            )
        )

    if dafny_input.DestinationEncryptionAlgorithm.is_Some:
        output["DestinationEncryptionAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_EncryptionAlgorithmSpec(
                dafny_input.DestinationEncryptionAlgorithm.value
            )
        )

    return output


def com_amazonaws_kms_ReplicateKeyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["ReplicaRegion"] = dafny_input.ReplicaRegion.VerbatimString(False)
    if dafny_input.Policy.is_Some:
        output["Policy"] = dafny_input.Policy.value.VerbatimString(False)

    if dafny_input.BypassPolicyLockoutSafetyCheck.is_Some:
        output["BypassPolicyLockoutSafetyCheck"] = (
            dafny_input.BypassPolicyLockoutSafetyCheck.value
        )

    if dafny_input.Description.is_Some:
        output["Description"] = dafny_input.Description.value.VerbatimString(False)

    if dafny_input.Tags.is_Some:
        output["Tags"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_Tag(
                list_element
            )
            for list_element in dafny_input.Tags.value
        ]

    return output


def com_amazonaws_kms_ReplicateKeyResponse(dafny_input):
    output = {}
    if dafny_input.ReplicaKeyMetadata.is_Some:
        output["ReplicaKeyMetadata"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyMetadata(
                dafny_input.ReplicaKeyMetadata.value
            )
        )

    if dafny_input.ReplicaPolicy.is_Some:
        output["ReplicaPolicy"] = dafny_input.ReplicaPolicy.value.VerbatimString(False)

    if dafny_input.ReplicaTags.is_Some:
        output["ReplicaTags"] = [
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_Tag(
                list_element
            )
            for list_element in dafny_input.ReplicaTags.value
        ]

    return output


def com_amazonaws_kms_RetireGrantRequest(dafny_input):
    output = {}
    if dafny_input.GrantToken.is_Some:
        output["GrantToken"] = dafny_input.GrantToken.value.VerbatimString(False)

    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.GrantId.is_Some:
        output["GrantId"] = dafny_input.GrantId.value.VerbatimString(False)

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_RevokeGrantRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["GrantId"] = dafny_input.GrantId.VerbatimString(False)
    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_RotateKeyOnDemandRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_RotateKeyOnDemandResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    return output


def com_amazonaws_kms_ScheduleKeyDeletionRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    if dafny_input.PendingWindowInDays.is_Some:
        output["PendingWindowInDays"] = dafny_input.PendingWindowInDays.value

    return output


def com_amazonaws_kms_ScheduleKeyDeletionResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.DeletionDate.is_Some:
        output["DeletionDate"] = datetime.fromisoformat(
            dafny_input.DeletionDate.value.VerbatimString(False)
        )

    if dafny_input.KeyState.is_Some:
        output["KeyState"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_KeyState(
                dafny_input.KeyState.value
            )
        )

    if dafny_input.PendingWindowInDays.is_Some:
        output["PendingWindowInDays"] = dafny_input.PendingWindowInDays.value

    return output


def com_amazonaws_kms_MessageType(dafny_input):
    # Convert MessageType
    if isinstance(dafny_input, MessageType_RAW):
        return "RAW"

    elif isinstance(dafny_input, MessageType_DIGEST):
        return "DIGEST"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_kms_SignRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["Message"] = bytes(dafny_input.Message)
    if dafny_input.MessageType.is_Some:
        output["MessageType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MessageType(
                dafny_input.MessageType.value
            )
        )

    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    output["SigningAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
            dafny_input.SigningAlgorithm
        )
    )
    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_SignResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.Signature.is_Some:
        output["Signature"] = bytes(dafny_input.Signature.value)

    if dafny_input.SigningAlgorithm.is_Some:
        output["SigningAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
                dafny_input.SigningAlgorithm.value
            )
        )

    return output


def com_amazonaws_kms_TagResourceRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["Tags"] = [
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_Tag(
            list_element
        )
        for list_element in dafny_input.Tags
    ]
    return output


def com_amazonaws_kms_UntagResourceRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["TagKeys"] = [
        list_element.VerbatimString(False) for list_element in dafny_input.TagKeys
    ]
    return output


def com_amazonaws_kms_UpdateAliasRequest(dafny_input):
    output = {}
    output["AliasName"] = dafny_input.AliasName.VerbatimString(False)
    output["TargetKeyId"] = dafny_input.TargetKeyId.VerbatimString(False)
    return output


def com_amazonaws_kms_UpdateCustomKeyStoreRequest(dafny_input):
    output = {}
    output["CustomKeyStoreId"] = dafny_input.CustomKeyStoreId.VerbatimString(False)
    if dafny_input.NewCustomKeyStoreName.is_Some:
        output["NewCustomKeyStoreName"] = (
            dafny_input.NewCustomKeyStoreName.value.VerbatimString(False)
        )

    if dafny_input.KeyStorePassword.is_Some:
        output["KeyStorePassword"] = dafny_input.KeyStorePassword.value.VerbatimString(
            False
        )

    if dafny_input.CloudHsmClusterId.is_Some:
        output["CloudHsmClusterId"] = (
            dafny_input.CloudHsmClusterId.value.VerbatimString(False)
        )

    if dafny_input.XksProxyUriEndpoint.is_Some:
        output["XksProxyUriEndpoint"] = (
            dafny_input.XksProxyUriEndpoint.value.VerbatimString(False)
        )

    if dafny_input.XksProxyUriPath.is_Some:
        output["XksProxyUriPath"] = dafny_input.XksProxyUriPath.value.VerbatimString(
            False
        )

    if dafny_input.XksProxyVpcEndpointServiceName.is_Some:
        output["XksProxyVpcEndpointServiceName"] = (
            dafny_input.XksProxyVpcEndpointServiceName.value.VerbatimString(False)
        )

    if dafny_input.XksProxyAuthenticationCredential.is_Some:
        output["XksProxyAuthenticationCredential"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyAuthenticationCredentialType(
                dafny_input.XksProxyAuthenticationCredential.value
            )
        )

    if dafny_input.XksProxyConnectivity.is_Some:
        output["XksProxyConnectivity"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_XksProxyConnectivityType(
                dafny_input.XksProxyConnectivity.value
            )
        )

    return output


def com_amazonaws_kms_UpdateCustomKeyStoreResponse(dafny_input):
    output = {}
    return output


def com_amazonaws_kms_UpdateKeyDescriptionRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["Description"] = dafny_input.Description.VerbatimString(False)
    return output


def com_amazonaws_kms_UpdatePrimaryRegionRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["PrimaryRegion"] = dafny_input.PrimaryRegion.VerbatimString(False)
    return output


def com_amazonaws_kms_VerifyRequest(dafny_input):
    output = {}
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["Message"] = bytes(dafny_input.Message)
    if dafny_input.MessageType.is_Some:
        output["MessageType"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MessageType(
                dafny_input.MessageType.value
            )
        )

    output["Signature"] = bytes(dafny_input.Signature)
    output["SigningAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
            dafny_input.SigningAlgorithm
        )
    )
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_VerifyResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.SignatureValid.is_Some:
        output["SignatureValid"] = dafny_input.SignatureValid.value

    if dafny_input.SigningAlgorithm.is_Some:
        output["SigningAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_SigningAlgorithmSpec(
                dafny_input.SigningAlgorithm.value
            )
        )

    return output


def com_amazonaws_kms_VerifyMacRequest(dafny_input):
    output = {}
    output["Message"] = bytes(dafny_input.Message)
    output["KeyId"] = dafny_input.KeyId.VerbatimString(False)
    output["MacAlgorithm"] = (
        com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MacAlgorithmSpec(
            dafny_input.MacAlgorithm
        )
    )
    output["Mac"] = bytes(dafny_input.Mac)
    if dafny_input.GrantTokens.is_Some:
        output["GrantTokens"] = [
            list_element.VerbatimString(False)
            for list_element in dafny_input.GrantTokens.value
        ]

    if dafny_input.DryRun.is_Some:
        output["DryRun"] = dafny_input.DryRun.value

    return output


def com_amazonaws_kms_VerifyMacResponse(dafny_input):
    output = {}
    if dafny_input.KeyId.is_Some:
        output["KeyId"] = dafny_input.KeyId.value.VerbatimString(False)

    if dafny_input.MacValid.is_Some:
        output["MacValid"] = dafny_input.MacValid.value

    if dafny_input.MacAlgorithm.is_Some:
        output["MacAlgorithm"] = (
            com_amazonaws_kms.smithygenerated.com_amazonaws_kms.dafny_to_aws_sdk.com_amazonaws_kms_MacAlgorithmSpec(
                dafny_input.MacAlgorithm.value
            )
        )

    return output
