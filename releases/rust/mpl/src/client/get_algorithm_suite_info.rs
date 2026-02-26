// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
impl crate::client::Client {
    /// Constructs a fluent builder for the [`GetAlgorithmSuiteInfo`](crate::operation::get_algorithm_suite_info::builders::GetAlgorithmSuiteInfoFluentBuilder) operation.
    ///
    /// - The fluent builder is configurable:
    ///   - [`binary_id(impl Into<Option<::aws_smithy_types::Blob>>)`](crate::operation::get_algorithm_suite_info::builders::GetAlgorithmSuiteInfoFluentBuilder::binary_id) / [`set_binary_id(Option<::aws_smithy_types::Blob>)`](crate::operation::get_algorithm_suite_info::builders::GetAlgorithmSuiteInfoFluentBuilder::set_binary_id): (undocumented)<br>
    /// - On success, responds with [`AlgorithmSuiteInfo`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo) with field(s):
    ///   - [`binary_id(Option<::aws_smithy_types::Blob>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::binary_id): (undocumented)
    ///   - [`commitment(Option<crate::types::DerivationAlgorithm>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::commitment): (undocumented)
    ///   - [`edk_wrapping(Option<crate::types::EdkWrappingAlgorithm>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::edk_wrapping): (undocumented)
    ///   - [`encrypt(Option<crate::types::Encrypt>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::encrypt): (undocumented)
    ///   - [`id(Option<crate::types::AlgorithmSuiteId>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::id): (undocumented)
    ///   - [`kdf(Option<crate::types::DerivationAlgorithm>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::kdf): (undocumented)
    ///   - [`message_version(Option<::std::primitive::i32>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::message_version): (undocumented)
    ///   - [`signature(Option<crate::types::SignatureAlgorithm>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::signature): (undocumented)
    ///   - [`symmetric_signature(Option<crate::types::SymmetricSignatureAlgorithm>)`](crate::operation::get_algorithm_suite_info::AlgorithmSuiteInfo::symmetric_signature): (undocumented)
    /// - On failure, responds with [`SdkError<GetAlgorithmSuiteInfoError>`](crate::operation::get_algorithm_suite_info::GetAlgorithmSuiteInfoError)
    pub fn get_algorithm_suite_info(
        &self,
    ) -> crate::operation::get_algorithm_suite_info::builders::GetAlgorithmSuiteInfoFluentBuilder
    {
        crate::operation::get_algorithm_suite_info::builders::GetAlgorithmSuiteInfoFluentBuilder::new(self.clone())
    }
}
