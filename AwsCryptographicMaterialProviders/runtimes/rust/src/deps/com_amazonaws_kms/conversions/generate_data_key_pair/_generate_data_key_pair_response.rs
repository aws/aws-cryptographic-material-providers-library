// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &aws_sdk_kms::operation::generate_data_key_pair::GenerateDataKeyPairOutput
) -> ::std::rc::Rc<
    crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairResponse,
>{
    ::std::rc::Rc::new(crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairResponse::GenerateDataKeyPairResponse {
        PrivateKeyCiphertextBlob: crate::standard_library_conversions::oblob_to_dafny(&value.private_key_ciphertext_blob),
 PrivateKeyPlaintext: crate::standard_library_conversions::oblob_to_dafny(&value.private_key_plaintext),
 PublicKey: crate::standard_library_conversions::oblob_to_dafny(&value.public_key),
 KeyId: crate::standard_library_conversions::ostring_to_dafny(&value.key_id),
 KeyPairSpec: ::std::rc::Rc::new(match &value.key_pair_spec {
    Some(x) => crate::_Wrappers_Compile::Option::Some { value: crate::deps::com_amazonaws_kms::conversions::data_key_pair_spec::to_dafny(x.clone()) },
    None => crate::_Wrappers_Compile::Option::None { }
})
,
 CiphertextForRecipient: crate::standard_library_conversions::oblob_to_dafny(&value.ciphertext_for_recipient),
    })
}
 
