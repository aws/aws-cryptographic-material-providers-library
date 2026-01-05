// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::AlgorithmSuiteInfo,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo,
>{
    ::dafny_runtime::Rc::new(to_dafny_plain(value.clone()))
}

#[allow(dead_code)]
pub fn to_dafny_plain(
    value: crate::types::AlgorithmSuiteInfo,
) -> crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo{
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo::AlgorithmSuiteInfo {
        id: crate::conversions::algorithm_suite_id::to_dafny(&value.id.clone().unwrap())
,
 binaryId: crate::standard_library_conversions::blob_to_dafny(&value.binary_id.unwrap()),
 messageVersion: value.message_version.clone().unwrap(),
 encrypt: crate::conversions::encrypt::to_dafny(&value.encrypt.clone().unwrap())
,
 kdf: crate::conversions::derivation_algorithm::to_dafny(&value.kdf.clone().unwrap())
,
 commitment: crate::conversions::derivation_algorithm::to_dafny(&value.commitment.clone().unwrap())
,
 signature: crate::conversions::signature_algorithm::to_dafny(&value.signature.clone().unwrap())
,
 symmetricSignature: crate::conversions::symmetric_signature_algorithm::to_dafny(&value.symmetric_signature.clone().unwrap())
,
 edkWrapping: crate::conversions::edk_wrapping_algorithm::to_dafny(&value.edk_wrapping.clone().unwrap())
,
    }
}

#[allow(dead_code)]
pub fn option_to_dafny(
  value: ::std::option::Option<crate::types::AlgorithmSuiteInfo>,
) -> ::dafny_runtime::Rc<crate::_Wrappers_Compile::Option<::dafny_runtime::Rc<
  crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo,
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
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo,
    >,
) -> crate::types::AlgorithmSuiteInfo {
    plain_from_dafny(&*dafny_value)
}

#[allow(dead_code)]
pub fn plain_from_dafny(
    dafny_value: &crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo,
) -> crate::types::AlgorithmSuiteInfo {
    match dafny_value {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo::AlgorithmSuiteInfo {..} =>
            crate::types::AlgorithmSuiteInfo::builder()
                .set_id(Some( crate::conversions::algorithm_suite_id::from_dafny(dafny_value.id().clone())
 ))
 .set_binary_id(Some(crate::standard_library_conversions::blob_from_dafny(dafny_value.binaryId().clone())))
 .set_message_version(Some( dafny_value.messageVersion() .clone() ))
 .set_encrypt(Some( crate::conversions::encrypt::from_dafny(dafny_value.encrypt().clone())
 ))
 .set_kdf(Some( crate::conversions::derivation_algorithm::from_dafny(dafny_value.kdf().clone())
 ))
 .set_commitment(Some( crate::conversions::derivation_algorithm::from_dafny(dafny_value.commitment().clone())
 ))
 .set_signature(Some( crate::conversions::signature_algorithm::from_dafny(dafny_value.signature().clone())
 ))
 .set_symmetric_signature(Some( crate::conversions::symmetric_signature_algorithm::from_dafny(dafny_value.symmetricSignature().clone())
 ))
 .set_edk_wrapping(Some( crate::conversions::edk_wrapping_algorithm::from_dafny(dafny_value.edkWrapping().clone())
 ))
                .build()
                .unwrap()
    }
}

#[allow(dead_code)]
pub fn option_from_dafny(
    dafny_value: ::dafny_runtime::Rc<crate::_Wrappers_Compile::Option<::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteInfo,
    >>>,
) -> ::std::option::Option<crate::types::AlgorithmSuiteInfo> {
    match &*dafny_value {
        crate::_Wrappers_Compile::Option::Some { value } => {
            ::std::option::Option::Some(plain_from_dafny(value))
        }
        _ => ::std::option::Option::None,
    }
}
