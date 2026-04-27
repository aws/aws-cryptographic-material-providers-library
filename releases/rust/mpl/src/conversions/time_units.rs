// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]

pub fn to_dafny(
    value: crate::types::TimeUnits,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits,
> {
    ::dafny_runtime::Rc::new(match value {
        crate::types::TimeUnits::Seconds => crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits::Seconds {},
crate::types::TimeUnits::Milliseconds => crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits::Milliseconds {},
        _ => panic!("Unknown enum variant: {}", value),
    })
}
#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: &crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits,
) -> crate::types::TimeUnits {
    match dafny_value {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits::Seconds {} => crate::types::TimeUnits::Seconds,
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::TimeUnits::Milliseconds {} => crate::types::TimeUnits::Milliseconds,
    }
}
