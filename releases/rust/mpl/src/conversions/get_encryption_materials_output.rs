// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::GetEncryptionMaterialsOutput,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput,
>{
    ::dafny_runtime::Rc::new(to_dafny_plain(value.clone()))
}

#[allow(dead_code)]
pub fn to_dafny_plain(
    value: crate::types::GetEncryptionMaterialsOutput,
) -> crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput{
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput::GetEncryptionMaterialsOutput {
        encryptionMaterials: crate::conversions::encryption_materials::to_dafny(&value.encryption_materials.clone().unwrap())
,
    }
}

#[allow(dead_code)]
pub fn option_to_dafny(
  value: ::std::option::Option<crate::types::GetEncryptionMaterialsOutput>,
) -> ::dafny_runtime::Rc<crate::_Wrappers_Compile::Option<::dafny_runtime::Rc<
  crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput,
>>>{
    ::dafny_runtime::Rc::new(match value {
        ::std::option::Option::None => crate::_Wrappers_Compile::Option::None {},
        ::std::option::Option::Some(x) => crate::_Wrappers_Compile::Option::Some {
            value: ::dafny_runtime::Rc::new(to_dafny_plain(x)),
        },
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput,
    >,
) -> crate::types::GetEncryptionMaterialsOutput {
    plain_from_dafny(&*dafny_value)
}

#[allow(dead_code)]
pub fn plain_from_dafny(
    dafny_value: &crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput,
) -> crate::types::GetEncryptionMaterialsOutput {
    match dafny_value {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput::GetEncryptionMaterialsOutput {..} =>
            crate::types::GetEncryptionMaterialsOutput::builder()
                .set_encryption_materials(Some( crate::conversions::encryption_materials::from_dafny(dafny_value.encryptionMaterials().clone())
 ))
                .build()
                .unwrap()
    }
}

#[allow(dead_code)]
pub fn option_from_dafny(
    dafny_value: ::dafny_runtime::Rc<crate::_Wrappers_Compile::Option<::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetEncryptionMaterialsOutput,
    >>>,
) -> ::std::option::Option<crate::types::GetEncryptionMaterialsOutput> {
    match &*dafny_value {
        crate::_Wrappers_Compile::Option::Some { value } => {
            ::std::option::Option::Some(plain_from_dafny(value))
        }
        _ => ::std::option::Option::None,
    }
}
