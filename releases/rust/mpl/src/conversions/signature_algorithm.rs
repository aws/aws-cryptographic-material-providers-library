// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::SignatureAlgorithm,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm,
>{
    ::dafny_runtime::Rc::new(match value {
        crate::types::SignatureAlgorithm::Ecdsa(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm::ECDSA {
        ECDSA: crate::conversions::ecdsa::to_dafny(&x.clone())
,
    },
crate::types::SignatureAlgorithm::None(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm::None {
        _None: crate::conversions::none::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm,
    >,
) -> crate::types::SignatureAlgorithm {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm::ECDSA {
    ECDSA: x @ _,
} => crate::types::SignatureAlgorithm::Ecdsa(crate::conversions::ecdsa::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::SignatureAlgorithm::None {
    _None: x @ _,
} => crate::types::SignatureAlgorithm::None(crate::conversions::none::from_dafny(x.clone())
),
    }
}
