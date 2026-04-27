// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
#[allow(missing_docs)]
pub struct CreateDefaultClientSupplierInput {}
impl CreateDefaultClientSupplierInput {}
impl CreateDefaultClientSupplierInput {
    /// Creates a new builder-style object to manufacture [`CreateDefaultClientSupplierInput`](crate::types::CreateDefaultClientSupplierInput).
    pub fn builder() -> crate::types::builders::CreateDefaultClientSupplierInputBuilder {
        crate::types::builders::CreateDefaultClientSupplierInputBuilder::default()
    }
}

/// A builder for [`CreateDefaultClientSupplierInput`](crate::types::CreateDefaultClientSupplierInput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct CreateDefaultClientSupplierInputBuilder {}
impl CreateDefaultClientSupplierInputBuilder {
    /// Consumes the builder and constructs a [`CreateDefaultClientSupplierInput`](crate::types::CreateDefaultClientSupplierInput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::CreateDefaultClientSupplierInput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::CreateDefaultClientSupplierInput {})
    }
}
