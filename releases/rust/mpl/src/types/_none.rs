// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
#[allow(missing_docs)]
pub struct None {}
impl None {}
impl None {
    /// Creates a new builder-style object to manufacture [`None`](crate::types::None).
    pub fn builder() -> crate::types::builders::NoneBuilder {
        crate::types::builders::NoneBuilder::default()
    }
}

/// A builder for [`None`](crate::types::None).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct NoneBuilder {}
impl NoneBuilder {
    /// Consumes the builder and constructs a [`None`](crate::types::None).
    pub fn build(
        self,
    ) -> ::std::result::Result<crate::types::None, ::aws_smithy_types::error::operation::BuildError>
    {
        ::std::result::Result::Ok(crate::types::None {})
    }
}
