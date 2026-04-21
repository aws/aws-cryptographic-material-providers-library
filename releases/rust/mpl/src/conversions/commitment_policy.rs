// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::CommitmentPolicy,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy,
>{
    ::dafny_runtime::Rc::new(match value {
        crate::types::CommitmentPolicy::Esdk(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy::ESDK {
        ESDK: crate::conversions::esdk_commitment_policy::to_dafny(x.clone()),
    },
crate::types::CommitmentPolicy::Dbe(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy::DBE {
        DBE: crate::conversions::dbe_commitment_policy::to_dafny(x.clone()),
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy,
    >,
) -> crate::types::CommitmentPolicy {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy::ESDK {
    ESDK: x @ _,
} => crate::types::CommitmentPolicy::Esdk(crate::conversions::esdk_commitment_policy::from_dafny(x)),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CommitmentPolicy::DBE {
    DBE: x @ _,
} => crate::types::CommitmentPolicy::Dbe(crate::conversions::dbe_commitment_policy::from_dafny(x)),
    }
}
