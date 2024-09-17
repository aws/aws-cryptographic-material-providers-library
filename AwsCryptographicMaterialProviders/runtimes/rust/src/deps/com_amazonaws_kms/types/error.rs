// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[derive(::std::clone::Clone, ::std::fmt::Debug, ::std::cmp::PartialEq)]
pub enum Error {
    NotFoundException {
    error: aws_sdk_kms::types::error::NotFoundException,
},

InvalidKeyUsageException {
    error: aws_sdk_kms::types::error::InvalidKeyUsageException,
},

UnsupportedOperationException {
    error: aws_sdk_kms::types::error::UnsupportedOperationException,
},

XksProxyUriInUseException {
    error: aws_sdk_kms::types::error::XksProxyUriInUseException,
},

XksProxyVpcEndpointServiceInUseException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceInUseException,
},

KmsInvalidStateException {
    error: aws_sdk_kms::types::error::KmsInvalidStateException,
},

CloudHsmClusterNotActiveException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotActiveException,
},

MalformedPolicyDocumentException {
    error: aws_sdk_kms::types::error::MalformedPolicyDocumentException,
},

ExpiredImportTokenException {
    error: aws_sdk_kms::types::error::ExpiredImportTokenException,
},

XksKeyInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksKeyInvalidConfigurationException,
},

XksProxyVpcEndpointServiceInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceInvalidConfigurationException,
},

XksKeyAlreadyInUseException {
    error: aws_sdk_kms::types::error::XksKeyAlreadyInUseException,
},

IncorrectKeyException {
    error: aws_sdk_kms::types::error::IncorrectKeyException,
},

TagException {
    error: aws_sdk_kms::types::error::TagException,
},

XksProxyVpcEndpointServiceNotFoundException {
    error: aws_sdk_kms::types::error::XksProxyVpcEndpointServiceNotFoundException,
},

CloudHsmClusterNotRelatedException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotRelatedException,
},

InvalidImportTokenException {
    error: aws_sdk_kms::types::error::InvalidImportTokenException,
},

DisabledException {
    error: aws_sdk_kms::types::error::DisabledException,
},

XksProxyInvalidResponseException {
    error: aws_sdk_kms::types::error::XksProxyInvalidResponseException,
},

CustomKeyStoreHasCmKsException {
    error: aws_sdk_kms::types::error::CustomKeyStoreHasCmKsException,
},

CustomKeyStoreNameInUseException {
    error: aws_sdk_kms::types::error::CustomKeyStoreNameInUseException,
},

CloudHsmClusterInUseException {
    error: aws_sdk_kms::types::error::CloudHsmClusterInUseException,
},

XksProxyUriUnreachableException {
    error: aws_sdk_kms::types::error::XksProxyUriUnreachableException,
},

KmsInvalidSignatureException {
    error: aws_sdk_kms::types::error::KmsInvalidSignatureException,
},

LimitExceededException {
    error: aws_sdk_kms::types::error::LimitExceededException,
},

XksProxyInvalidConfigurationException {
    error: aws_sdk_kms::types::error::XksProxyInvalidConfigurationException,
},

InvalidAliasNameException {
    error: aws_sdk_kms::types::error::InvalidAliasNameException,
},

CustomKeyStoreInvalidStateException {
    error: aws_sdk_kms::types::error::CustomKeyStoreInvalidStateException,
},

InvalidCiphertextException {
    error: aws_sdk_kms::types::error::InvalidCiphertextException,
},

XksProxyUriEndpointInUseException {
    error: aws_sdk_kms::types::error::XksProxyUriEndpointInUseException,
},

XksProxyIncorrectAuthenticationCredentialException {
    error: aws_sdk_kms::types::error::XksProxyIncorrectAuthenticationCredentialException,
},

CloudHsmClusterInvalidConfigurationException {
    error: aws_sdk_kms::types::error::CloudHsmClusterInvalidConfigurationException,
},

CustomKeyStoreNotFoundException {
    error: aws_sdk_kms::types::error::CustomKeyStoreNotFoundException,
},

IncorrectKeyMaterialException {
    error: aws_sdk_kms::types::error::IncorrectKeyMaterialException,
},

KeyUnavailableException {
    error: aws_sdk_kms::types::error::KeyUnavailableException,
},

CloudHsmClusterNotFoundException {
    error: aws_sdk_kms::types::error::CloudHsmClusterNotFoundException,
},

KmsInvalidMacException {
    error: aws_sdk_kms::types::error::KmsInvalidMacException,
},

DependencyTimeoutException {
    error: aws_sdk_kms::types::error::DependencyTimeoutException,
},

IncorrectTrustAnchorException {
    error: aws_sdk_kms::types::error::IncorrectTrustAnchorException,
},

ConflictException {
    error: aws_sdk_kms::types::error::ConflictException,
},

InvalidGrantTokenException {
    error: aws_sdk_kms::types::error::InvalidGrantTokenException,
},

XksKeyNotFoundException {
    error: aws_sdk_kms::types::error::XksKeyNotFoundException,
},

AlreadyExistsException {
    error: aws_sdk_kms::types::error::AlreadyExistsException,
},

DryRunOperationException {
    error: aws_sdk_kms::types::error::DryRunOperationException,
},

KmsInternalException {
    error: aws_sdk_kms::types::error::KmsInternalException,
},

InvalidArnException {
    error: aws_sdk_kms::types::error::InvalidArnException,
},

InvalidMarkerException {
    error: aws_sdk_kms::types::error::InvalidMarkerException,
},

InvalidGrantIdException {
    error: aws_sdk_kms::types::error::InvalidGrantIdException,
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
