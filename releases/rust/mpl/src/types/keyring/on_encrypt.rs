// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
impl crate::types::keyring::KeyringRef {
    /// Constructs a fluent builder for the [`OnEncrypt`](crate::operation::on_encrypt::builders::OnEncryptFluentBuilder) operation.
    ///
    /// - The fluent builder is configurable:
    ///   - [`materials(impl Into<Option<crate::types::EncryptionMaterials>>)`](crate::operation::on_encrypt::builders::OnEncryptFluentBuilder::materials) / [`set_materials(Option<crate::types::EncryptionMaterials>)`](crate::operation::on_encrypt::builders::OnEncryptFluentBuilder::set_materials): (undocumented)<br>
    /// - On success, responds with [`OnEncryptOutput`](crate::operation::on_encrypt::OnEncryptOutput) with field(s):
    ///   - [`materials(Option<crate::types::EncryptionMaterials>)`](crate::operation::on_encrypt::OnEncryptOutput::materials): (undocumented)
    /// - On failure, responds with [`SdkError<OnEncryptError>`](crate::operation::on_encrypt::OnEncryptError)
    pub fn on_encrypt(&self) -> crate::operation::on_encrypt::builders::OnEncryptFluentBuilder {
        crate::operation::on_encrypt::builders::OnEncryptFluentBuilder::new(self.clone())
    }
}
