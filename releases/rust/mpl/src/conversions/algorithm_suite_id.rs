// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::AlgorithmSuiteId,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId,
>{
    ::dafny_runtime::Rc::new(match value {
        crate::types::AlgorithmSuiteId::Esdk(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId::ESDK {
        ESDK: crate::conversions::esdk_algorithm_suite_id::to_dafny(x.clone()),
    },
crate::types::AlgorithmSuiteId::Dbe(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId::DBE {
        DBE: crate::conversions::dbe_algorithm_suite_id::to_dafny(x.clone()),
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId,
    >,
) -> crate::types::AlgorithmSuiteId {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId::ESDK {
    ESDK: x @ _,
} => crate::types::AlgorithmSuiteId::Esdk(crate::conversions::esdk_algorithm_suite_id::from_dafny(x)),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::AlgorithmSuiteId::DBE {
    DBE: x @ _,
} => crate::types::AlgorithmSuiteId::Dbe(crate::conversions::dbe_algorithm_suite_id::from_dafny(x)),
    }
}
