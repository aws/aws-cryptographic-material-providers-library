// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[derive(::std::clone::Clone, ::std::fmt::Debug, ::std::cmp::PartialEq)]
pub enum Error {
    DependencyTimeoutException {
    error: aws_sdk_kms::types::error::DependencyTimeoutException,
},

DisabledException {
    error: aws_sdk_kms::types::error::DisabledException,
},

DryRunOperationException {
    error: aws_sdk_kms::types::error::DryRunOperationException,
},

InvalidGrantTokenException {
    error: aws_sdk_kms::types::error::InvalidGrantTokenException,
},

InvalidKeyUsageException {
    error: aws_sdk_kms::types::error::InvalidKeyUsageException,
},

KeyUnavailableException {
    error: aws_sdk_kms::types::error::KeyUnavailableException,
},

KmsInternalException {
    error: aws_sdk_kms::types::error::KmsInternalException,
},

KmsInvalidStateException {
    error: aws_sdk_kms::types::error::KmsInvalidStateException,
},

NotFoundException {
    error: aws_sdk_kms::types::error::NotFoundException,
},

ConflictException {
    error: aws_sdk_kms::types::error::ConflictException,
},

InvalidArnException {
    error: aws_sdk_kms::types::error::InvalidArnException,
},

LimitExceededException {
    error: aws_sdk_kms::types::error::LimitExceededException,
},

UnsupportedOperationException {
    error: aws_sdk_kms::types::error::UnsupportedOperationException,
},

MalformedPolicyDocumentException {
    error: aws_sdk_kms::types::error::MalformedPolicyDocumentException,
},

CloudHsmClusterInvalidConfigurationException {
    error: aws_sdk_kms::types::error::CloudHsmClusterInvalidConfigurationException,
},

CustomKeyStoreInvalidStateException {
    error: aws_sdk_kms::types::error::CustomKeyStoreInvalidStateException,
},

CustomKeyStoreNotFoundException {
    error: aws_sdk_kms::types::error::CustomKeyStoreNotFoundException,
},

TagException {
    error: aws_sdk_kms::types::error::TagException,
},

XksKeyAlreadyInUseException {
    error: aws_sdk_kms::types::error::XksKeyAlreadyInUseException,
},

XksKeyInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksKeyInvalidConfigurationException,
},

XksKeyNotFoundException {
    error: aws_sdk_kms::types::error::XksKeyNotFoundException,
},

InvalidMarkerException {
    error: aws_sdk_kms::types::error::InvalidMarkerException,
},

InvalidGrantIdException {
    error: aws_sdk_kms::types::error::InvalidGrantIdException,
},

ExpiredImportTokenException {
    error: aws_sdk_kms::types::error::ExpiredImportTokenException,
},

IncorrectKeyMaterialException {
    error: aws_sdk_kms::types::error::IncorrectKeyMaterialException,
},

InvalidCiphertextException {
    error: aws_sdk_kms::types::error::InvalidCiphertextException,
},

InvalidImportTokenException {
    error: aws_sdk_kms::types::error::InvalidImportTokenException,
},

KmsInvalidSignatureException {
    error: aws_sdk_kms::types::error::KmsInvalidSignatureException,
},

IncorrectKeyException {
    error: aws_sdk_kms::types::error::IncorrectKeyException,
},

CloudHsmClusterInUseException {
    error: aws_sdk_kms::types::error::CloudHsmClusterInUseException,
},

CloudHsmClusterNotActiveException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotActiveException,
},

CloudHsmClusterNotFoundException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotFoundException,
},

CustomKeyStoreNameInUseException {
    error: aws_sdk_kms::types::error::CustomKeyStoreNameInUseException,
},

IncorrectTrustAnchorException {
    error: aws_sdk_kms::types::error::IncorrectTrustAnchorException,
},

XksProxyIncorrectAuthenticationCredentialException {
    error: aws_sdk_kms::types::error::XksProxyIncorrectAuthenticationCredentialException,
},

XksProxyInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksProxyInvalidConfigurationException,
},

XksProxyInvalidResponseException {
    error: aws_sdk_kms::types::error::XksProxyInvalidResponseException,
},

XksProxyUriEndpointInUseException {
    error: aws_sdk_kms::types::error::XksProxyUriEndpointInUseException,
},

XksProxyUriInUseException {
    error: aws_sdk_kms::types::error::XksProxyUriInUseException,
},

XksProxyUriUnreachableException {
    error: aws_sdk_kms::types::error::XksProxyUriUnreachableException,
},

XksProxyVpcEndpointServiceInUseException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceInUseException,
},

XksProxyVpcEndpointServiceInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceInvalidConfigurationException,
},

XksProxyVpcEndpointServiceNotFoundException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceNotFoundException,
},

CloudHsmClusterNotRelatedException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotRelatedException,
},

CustomKeyStoreHasCmKsException {
    error: aws_sdk_kms::types::error::CustomKeyStoreHasCmKsException,
},

AlreadyExistsException {
    error: aws_sdk_kms::types::error::AlreadyExistsException,
},

InvalidAliasNameException {
    error: aws_sdk_kms::types::error::InvalidAliasNameException,
},

KmsInvalidMacException {
    error: aws_sdk_kms::types::error::KmsInvalidMacException,
},
    Opaque {
        obj: ::dafny_runtime::Object<dyn ::std::any::Any>,
    },
}

impl ::std::cmp::Eq for Error {}

impl ::std::fmt::Display for Error {
    fn fmt(&self, f: &mut ::std::fmt::Formatter) -> ::std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

impl ::std::error::Error for Error {}
