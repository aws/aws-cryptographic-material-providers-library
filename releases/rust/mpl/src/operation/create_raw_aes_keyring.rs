// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
/// Orchestration and serialization glue logic for `CreateRawAesKeyring`.
#[derive(::std::clone::Clone, ::std::default::Default, ::std::fmt::Debug)]
#[non_exhaustive]
pub struct CreateRawAesKeyring;
impl CreateRawAesKeyring {
    /// Creates a new `CreateRawAesKeyring`
    pub fn new() -> Self {
        Self
    }

    pub(crate) async fn send(
        client: &crate::client::Client,
        input: crate::operation::create_raw_aes_keyring::CreateRawAesKeyringInput,
    ) -> ::std::result::Result<crate::types::keyring::KeyringRef, crate::types::error::Error> {
        crate::validation::validate_aws_Pcryptography_PmaterialProviders_HCreateRawAesKeyringInput_for_AwsCryptographicMaterialProviders_CreateRawAesKeyring(&input)
            .map_err(crate::types::error::Error::wrap_validation_err)?;
        let inner_input =
            crate::conversions::create_raw_aes_keyring::_create_raw_aes_keyring_input::to_dafny(
                input,
            );
        let inner_result =
            ::dafny_runtime::md!(client.dafny_client.clone()).CreateRawAesKeyring(&inner_input);
        if matches!(
            inner_result.as_ref(),
            crate::r#_Wrappers_Compile::Result::Success { .. }
        ) {
            Ok(crate::conversions::keyring::from_dafny(
                inner_result.value().clone(),
            ))
        } else {
            Err(crate::conversions::error::from_dafny(
                inner_result.error().clone(),
            ))
        }
    }
}

pub use crate::operation::create_raw_aes_keyring::_create_keyring_output::CreateKeyringOutput;

pub use crate::operation::create_raw_aes_keyring::_create_raw_aes_keyring_input::CreateRawAesKeyringInput;

pub(crate) mod _create_keyring_output;

pub(crate) mod _create_raw_aes_keyring_input;

/// Builders
pub mod builders;
