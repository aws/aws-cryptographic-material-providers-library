// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
/// Orchestration and serialization glue logic for `GetBranchKeyId`.
#[derive(::std::clone::Clone, ::std::default::Default, ::std::fmt::Debug)]
#[non_exhaustive]
pub struct GetBranchKeyId;
impl GetBranchKeyId {
    /// Creates a new `GetBranchKeyId`
    pub fn new() -> Self {
        Self
    }

    pub(crate) async fn send(
        branch_key_id_supplier: &crate::types::branch_key_id_supplier::BranchKeyIdSupplierRef,
        input: crate::operation::get_branch_key_id::GetBranchKeyIdInput,
    ) -> ::std::result::Result<
        crate::operation::get_branch_key_id::GetBranchKeyIdOutput,
        crate::types::error::Error,
    > {
        crate::validation::validate_aws_Pcryptography_PmaterialProviders_HGetBranchKeyIdInput_for_BranchKeyIdSupplier_GetBranchKeyId(&input)
            .map_err(crate::types::error::Error::wrap_validation_err)?;
        branch_key_id_supplier
            .inner
            .lock()
            .unwrap()
            .get_branch_key_id(input)
    }
}

pub use crate::operation::get_branch_key_id::_get_branch_key_id_output::GetBranchKeyIdOutput;

pub use crate::operation::get_branch_key_id::_get_branch_key_id_input::GetBranchKeyIdInput;

pub(crate) mod _get_branch_key_id_output;

pub(crate) mod _get_branch_key_id_input;

/// Builders
pub mod builders;
