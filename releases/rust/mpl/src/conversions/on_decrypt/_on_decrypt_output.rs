// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: crate::operation::on_decrypt::OnDecryptOutput,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::OnDecryptOutput,
>{
    ::dafny_runtime::Rc::new(crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::OnDecryptOutput::OnDecryptOutput {
        materials: crate::conversions::decryption_materials::to_dafny(&value.materials.clone().unwrap())
,
    })
}
#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::OnDecryptOutput,
    >,
) -> crate::operation::on_decrypt::OnDecryptOutput {
    crate::operation::on_decrypt::OnDecryptOutput::builder()
        .set_materials(Some(crate::conversions::decryption_materials::from_dafny(
            dafny_value.materials().clone(),
        )))
        .build()
        .unwrap()
}
