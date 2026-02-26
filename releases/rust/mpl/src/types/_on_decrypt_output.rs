// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
#[allow(missing_docs)]
pub struct OnDecryptOutput {
    #[allow(missing_docs)]
    pub materials: ::std::option::Option<crate::types::DecryptionMaterials>,
}
impl OnDecryptOutput {
    #[allow(missing_docs)]
    pub fn materials(&self) -> &::std::option::Option<crate::types::DecryptionMaterials> {
        &self.materials
    }
}
impl OnDecryptOutput {
    /// Creates a new builder-style object to manufacture [`OnDecryptOutput`](crate::types::OnDecryptOutput).
    pub fn builder() -> crate::types::builders::OnDecryptOutputBuilder {
        crate::types::builders::OnDecryptOutputBuilder::default()
    }
}

/// A builder for [`OnDecryptOutput`](crate::types::OnDecryptOutput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct OnDecryptOutputBuilder {
    pub(crate) materials: ::std::option::Option<crate::types::DecryptionMaterials>,
}
impl OnDecryptOutputBuilder {
    #[allow(missing_docs)]
    pub fn materials(
        mut self,
        input: impl ::std::convert::Into<crate::types::DecryptionMaterials>,
    ) -> Self {
        self.materials = ::std::option::Option::Some(input.into());
        self
    }
    #[allow(missing_docs)]
    pub fn set_materials(
        mut self,
        input: ::std::option::Option<crate::types::DecryptionMaterials>,
    ) -> Self {
        self.materials = input;
        self
    }
    #[allow(missing_docs)]
    pub fn get_materials(&self) -> &::std::option::Option<crate::types::DecryptionMaterials> {
        &self.materials
    }
    /// Consumes the builder and constructs a [`OnDecryptOutput`](crate::types::OnDecryptOutput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::OnDecryptOutput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::OnDecryptOutput {
            materials: self.materials,
        })
    }
}
