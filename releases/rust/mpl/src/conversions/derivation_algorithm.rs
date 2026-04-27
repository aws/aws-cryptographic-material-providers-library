// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::DerivationAlgorithm,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm,
>{
    ::dafny_runtime::Rc::new(match value {
        crate::types::DerivationAlgorithm::Hkdf(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::HKDF {
        HKDF: crate::conversions::hkdf::to_dafny(&x.clone())
,
    },
crate::types::DerivationAlgorithm::Identity(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::IDENTITY {
        IDENTITY: crate::conversions::identity::to_dafny(&x.clone())
,
    },
crate::types::DerivationAlgorithm::None(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::None {
        _None: crate::conversions::none::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm,
    >,
) -> crate::types::DerivationAlgorithm {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::HKDF {
    HKDF: x @ _,
} => crate::types::DerivationAlgorithm::Hkdf(crate::conversions::hkdf::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::IDENTITY {
    IDENTITY: x @ _,
} => crate::types::DerivationAlgorithm::Identity(crate::conversions::identity::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::DerivationAlgorithm::None {
    _None: x @ _,
} => crate::types::DerivationAlgorithm::None(crate::conversions::none::from_dafny(x.clone())
),
    }
}
