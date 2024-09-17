// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(missing_docs)] // documentation missing in model
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct CreateDefaultCryptographicMaterialsManagerInput {
    #[allow(missing_docs)] // documentation missing in model
pub keyring: ::std::option::Option<crate::types::keyring::KeyringRef>,
}
impl CreateDefaultCryptographicMaterialsManagerInput {
    #[allow(missing_docs)] // documentation missing in model
pub fn keyring(&self) -> &::std::option::Option<crate::types::keyring::KeyringRef> {
    &self.keyring
}
}
impl CreateDefaultCryptographicMaterialsManagerInput {
    /// Creates a new builder-style object to manufacture [`CreateDefaultCryptographicMaterialsManagerInput`](crate::types::CreateDefaultCryptographicMaterialsManagerInput).
    pub fn builder() -> crate::types::builders::CreateDefaultCryptographicMaterialsManagerInputBuilder {
        crate::types::builders::CreateDefaultCryptographicMaterialsManagerInputBuilder::default()
    }
}

/// A builder for [`CreateDefaultCryptographicMaterialsManagerInput`](crate::types::CreateDefaultCryptographicMaterialsManagerInput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct CreateDefaultCryptographicMaterialsManagerInputBuilder {
    pub(crate) keyring: ::std::option::Option<crate::types::keyring::KeyringRef>,
}
impl CreateDefaultCryptographicMaterialsManagerInputBuilder {
    #[allow(missing_docs)] // documentation missing in model
pub fn keyring(mut self, input: impl ::std::convert::Into<crate::types::keyring::KeyringRef>) -> Self {
    self.keyring = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_keyring(mut self, input: ::std::option::Option<crate::types::keyring::KeyringRef>) -> Self {
    self.keyring = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_keyring(&self) -> &::std::option::Option<crate::types::keyring::KeyringRef> {
    &self.keyring
}
    /// Consumes the builder and constructs a [`CreateDefaultCryptographicMaterialsManagerInput`](crate::types::CreateDefaultCryptographicMaterialsManagerInput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::CreateDefaultCryptographicMaterialsManagerInput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::CreateDefaultCryptographicMaterialsManagerInput {
            keyring: self.keyring,
        })
    }
}
