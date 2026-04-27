// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
impl crate::client::Client {
    /// Constructs a fluent builder for the [`ValidDecryptionMaterialsTransition`](crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder) operation.
    ///
    /// - The fluent builder is configurable:
    ///   - [`start(impl Into<Option<crate::types::DecryptionMaterials>>)`](crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder::start) / [`set_start(Option<crate::types::DecryptionMaterials>)`](crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder::set_start): (undocumented)<br>
    ///   - [`stop(impl Into<Option<crate::types::DecryptionMaterials>>)`](crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder::stop) / [`set_stop(Option<crate::types::DecryptionMaterials>)`](crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder::set_stop): (undocumented)<br>
    /// - On success, responds with [`Unit`](crate::operation::valid_decryption_materials_transition::Unit) with field(s):

    /// - On failure, responds with [`SdkError<ValidDecryptionMaterialsTransitionError>`](crate::operation::valid_decryption_materials_transition::ValidDecryptionMaterialsTransitionError)
    pub fn valid_decryption_materials_transition(&self) -> crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder{
        crate::operation::valid_decryption_materials_transition::builders::ValidDecryptionMaterialsTransitionFluentBuilder::new(self.clone())
    }
}
