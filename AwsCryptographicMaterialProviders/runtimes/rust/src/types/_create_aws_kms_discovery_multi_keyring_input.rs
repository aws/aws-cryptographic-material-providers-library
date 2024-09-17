// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(missing_docs)] // documentation missing in model
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct CreateAwsKmsDiscoveryMultiKeyringInput {
    #[allow(missing_docs)] // documentation missing in model
pub client_supplier: ::std::option::Option<crate::types::client_supplier::ClientSupplierRef>,
#[allow(missing_docs)] // documentation missing in model
pub discovery_filter: ::std::option::Option<crate::types::DiscoveryFilter>,
#[allow(missing_docs)] // documentation missing in model
pub grant_tokens: ::std::option::Option<::std::vec::Vec<::std::string::String>>,
#[allow(missing_docs)] // documentation missing in model
pub regions: ::std::option::Option<::std::vec::Vec<::std::string::String>>,
}
impl CreateAwsKmsDiscoveryMultiKeyringInput {
    #[allow(missing_docs)] // documentation missing in model
pub fn client_supplier(&self) -> &::std::option::Option<crate::types::client_supplier::ClientSupplierRef> {
    &self.client_supplier
}
#[allow(missing_docs)] // documentation missing in model
pub fn discovery_filter(&self) -> &::std::option::Option<crate::types::DiscoveryFilter> {
    &self.discovery_filter
}
#[allow(missing_docs)] // documentation missing in model
pub fn grant_tokens(&self) -> &::std::option::Option<::std::vec::Vec<::std::string::String>> {
    &self.grant_tokens
}
#[allow(missing_docs)] // documentation missing in model
pub fn regions(&self) -> &::std::option::Option<::std::vec::Vec<::std::string::String>> {
    &self.regions
}
}
impl CreateAwsKmsDiscoveryMultiKeyringInput {
    /// Creates a new builder-style object to manufacture [`CreateAwsKmsDiscoveryMultiKeyringInput`](crate::types::CreateAwsKmsDiscoveryMultiKeyringInput).
    pub fn builder() -> crate::types::builders::CreateAwsKmsDiscoveryMultiKeyringInputBuilder {
        crate::types::builders::CreateAwsKmsDiscoveryMultiKeyringInputBuilder::default()
    }
}

/// A builder for [`CreateAwsKmsDiscoveryMultiKeyringInput`](crate::types::CreateAwsKmsDiscoveryMultiKeyringInput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct CreateAwsKmsDiscoveryMultiKeyringInputBuilder {
    pub(crate) client_supplier: ::std::option::Option<crate::types::client_supplier::ClientSupplierRef>,
pub(crate) discovery_filter: ::std::option::Option<crate::types::DiscoveryFilter>,
pub(crate) grant_tokens: ::std::option::Option<::std::vec::Vec<::std::string::String>>,
pub(crate) regions: ::std::option::Option<::std::vec::Vec<::std::string::String>>,
}
impl CreateAwsKmsDiscoveryMultiKeyringInputBuilder {
    #[allow(missing_docs)] // documentation missing in model
pub fn client_supplier(mut self, input: impl ::std::convert::Into<crate::types::client_supplier::ClientSupplierRef>) -> Self {
    self.client_supplier = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_client_supplier(mut self, input: ::std::option::Option<crate::types::client_supplier::ClientSupplierRef>) -> Self {
    self.client_supplier = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_client_supplier(&self) -> &::std::option::Option<crate::types::client_supplier::ClientSupplierRef> {
    &self.client_supplier
}
#[allow(missing_docs)] // documentation missing in model
pub fn discovery_filter(mut self, input: impl ::std::convert::Into<crate::types::DiscoveryFilter>) -> Self {
    self.discovery_filter = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_discovery_filter(mut self, input: ::std::option::Option<crate::types::DiscoveryFilter>) -> Self {
    self.discovery_filter = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_discovery_filter(&self) -> &::std::option::Option<crate::types::DiscoveryFilter> {
    &self.discovery_filter
}
#[allow(missing_docs)] // documentation missing in model
pub fn grant_tokens(mut self, input: impl ::std::convert::Into<::std::vec::Vec<::std::string::String>>) -> Self {
    self.grant_tokens = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_grant_tokens(mut self, input: ::std::option::Option<::std::vec::Vec<::std::string::String>>) -> Self {
    self.grant_tokens = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_grant_tokens(&self) -> &::std::option::Option<::std::vec::Vec<::std::string::String>> {
    &self.grant_tokens
}
#[allow(missing_docs)] // documentation missing in model
pub fn regions(mut self, input: impl ::std::convert::Into<::std::vec::Vec<::std::string::String>>) -> Self {
    self.regions = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_regions(mut self, input: ::std::option::Option<::std::vec::Vec<::std::string::String>>) -> Self {
    self.regions = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_regions(&self) -> &::std::option::Option<::std::vec::Vec<::std::string::String>> {
    &self.regions
}
    /// Consumes the builder and constructs a [`CreateAwsKmsDiscoveryMultiKeyringInput`](crate::types::CreateAwsKmsDiscoveryMultiKeyringInput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::CreateAwsKmsDiscoveryMultiKeyringInput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::CreateAwsKmsDiscoveryMultiKeyringInput {
            client_supplier: self.client_supplier,
discovery_filter: self.discovery_filter,
grant_tokens: self.grant_tokens,
regions: self.regions,
        })
    }
}
