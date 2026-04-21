// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::SymmetricSignatureAlgorithm,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm,
>{
    ::dafny_runtime::Rc::new(match value {
        crate::types::SymmetricSignatureAlgorithm::Hmac(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm::HMAC {
        HMAC: crate::deps::aws_cryptography_primitives::conversions::digest_algorithm::to_dafny(x.clone()),
    },
crate::types::SymmetricSignatureAlgorithm::None(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm::None {
        _None: crate::conversions::none::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm,
    >,
) -> crate::types::SymmetricSignatureAlgorithm {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm::HMAC {
    HMAC: x @ _,
} => crate::types::SymmetricSignatureAlgorithm::Hmac(crate::deps::aws_cryptography_primitives::conversions::digest_algorithm::from_dafny(x)),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SymmetricSignatureAlgorithm::None {
    _None: x @ _,
} => crate::types::SymmetricSignatureAlgorithm::None(crate::conversions::none::from_dafny(x.clone())
),
    }
}
