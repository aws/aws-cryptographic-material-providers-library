// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
#[allow(missing_docs)]
pub struct DirectKeyWrapping {}
impl DirectKeyWrapping {}
impl DirectKeyWrapping {
    /// Creates a new builder-style object to manufacture [`DirectKeyWrapping`](crate::types::DirectKeyWrapping).
    pub fn builder() -> crate::types::builders::DirectKeyWrappingBuilder {
        crate::types::builders::DirectKeyWrappingBuilder::default()
    }
}

/// A builder for [`DirectKeyWrapping`](crate::types::DirectKeyWrapping).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct DirectKeyWrappingBuilder {}
impl DirectKeyWrappingBuilder {
    /// Consumes the builder and constructs a [`DirectKeyWrapping`](crate::types::DirectKeyWrapping).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::DirectKeyWrapping,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::DirectKeyWrapping {})
    }
}
