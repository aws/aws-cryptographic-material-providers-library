// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
/// Orchestration and serialization glue logic for `ValidAlgorithmSuiteInfo`.
#[derive(::std::clone::Clone, ::std::default::Default, ::std::fmt::Debug)]
#[non_exhaustive]
pub struct ValidAlgorithmSuiteInfo;
impl ValidAlgorithmSuiteInfo {
    /// Creates a new `ValidAlgorithmSuiteInfo`
    pub fn new() -> Self {
        Self
    }

    pub(crate) async fn send(
        client: &crate::client::Client,
        input: crate::operation::valid_algorithm_suite_info::AlgorithmSuiteInfo,
    ) -> ::std::result::Result<(), crate::types::error::Error> {
        crate::validation::validate_aws_Pcryptography_PmaterialProviders_HAlgorithmSuiteInfo_for_AwsCryptographicMaterialProviders_ValidAlgorithmSuiteInfo(&input)
            .map_err(crate::types::error::Error::wrap_validation_err)?;
        let inner_input = crate::conversions::valid_algorithm_suite_info::_valid_algorithm_suite_info_input::to_dafny(input);
        let inner_result =
            ::dafny_runtime::md!(client.dafny_client.clone()).ValidAlgorithmSuiteInfo(&inner_input);
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

pub use crate::operation::valid_algorithm_suite_info::_unit::Unit;

pub use crate::operation::valid_algorithm_suite_info::_algorithm_suite_info::AlgorithmSuiteInfo;

pub(crate) mod _unit;

pub(crate) mod _algorithm_suite_info;

/// Builders
pub mod builders;
