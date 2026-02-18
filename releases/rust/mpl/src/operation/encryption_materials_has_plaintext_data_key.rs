// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
/// Orchestration and serialization glue logic for `EncryptionMaterialsHasPlaintextDataKey`.
#[derive(::std::clone::Clone, ::std::default::Default, ::std::fmt::Debug)]
#[non_exhaustive]
pub struct EncryptionMaterialsHasPlaintextDataKey;
impl EncryptionMaterialsHasPlaintextDataKey {
    /// Creates a new `EncryptionMaterialsHasPlaintextDataKey`
    pub fn new() -> Self {
        Self
    }

    pub(crate) async fn send(
        client: &crate::client::Client,
        input: crate::operation::encryption_materials_has_plaintext_data_key::EncryptionMaterials,
    ) -> ::std::result::Result<(), crate::types::error::Error> {
        crate::validation::validate_aws_Pcryptography_PmaterialProviders_HEncryptionMaterials_for_AwsCryptographicMaterialProviders_EncryptionMaterialsHasPlaintextDataKey(&input)
            .map_err(crate::types::error::Error::wrap_validation_err)?;
        let inner_input = crate::conversions::encryption_materials_has_plaintext_data_key::_encryption_materials_has_plaintext_data_key_input::to_dafny(input);
        let inner_result = ::dafny_runtime::md!(client.dafny_client.clone())
            .EncryptionMaterialsHasPlaintextDataKey(&inner_input);
        if matches!(
            inner_result.as_ref(),
            crate::r#_Wrappers_Compile::Result::Success { .. }
        ) {
            Ok(())
        } else {
            Err(crate::conversions::error::from_dafny(
                inner_result.error().clone(),
            ))
        }
    }
}

pub use crate::operation::encryption_materials_has_plaintext_data_key::_unit::Unit;

pub use crate::operation::encryption_materials_has_plaintext_data_key::_encryption_materials::EncryptionMaterials;

pub(crate) mod _unit;

pub(crate) mod _encryption_materials;

/// Builders
pub mod builders;
