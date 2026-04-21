// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
/// Orchestration and serialization glue logic for `UpdateUsageMetadata`.
#[derive(::std::clone::Clone, ::std::default::Default, ::std::fmt::Debug)]
#[non_exhaustive]
pub struct UpdateUsageMetadata;
impl UpdateUsageMetadata {
    /// Creates a new `UpdateUsageMetadata`
    pub fn new() -> Self {
        Self
    }

    pub(crate) async fn send(
        cryptographic_materials_cache: &crate::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef,
        input: crate::operation::update_usage_metadata::UpdateUsageMetadataInput,
    ) -> ::std::result::Result<(), crate::types::error::Error> {
        crate::validation::validate_aws_Pcryptography_PmaterialProviders_HUpdateUsageMetadataInput_for_CryptographicMaterialsCache_UpdateUsageMetadata(&input)
            .map_err(crate::types::error::Error::wrap_validation_err)?;
        cryptographic_materials_cache
            .inner
            .lock()
            .unwrap()
            .update_usage_metadata(input)
    }
}

pub use crate::operation::update_usage_metadata::_unit::Unit;

pub use crate::operation::update_usage_metadata::_update_usage_metadata_input::UpdateUsageMetadataInput;

pub(crate) mod _unit;

pub(crate) mod _update_usage_metadata_input;

/// Builders
pub mod builders;
