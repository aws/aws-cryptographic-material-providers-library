// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::Materials,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials,
> {
    ::dafny_runtime::Rc::new(match value {
        crate::types::Materials::Encryption(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::Encryption {
        Encryption: crate::conversions::encryption_materials::to_dafny(&x.clone())
,
    },
crate::types::Materials::Decryption(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::Decryption {
        Decryption: crate::conversions::decryption_materials::to_dafny(&x.clone())
,
    },
crate::types::Materials::BranchKey(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::BranchKey {
        BranchKey: crate::deps::aws_cryptography_keyStore::conversions::branch_key_materials::to_dafny(&x.clone())
,
    },
crate::types::Materials::BeaconKey(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::BeaconKey {
        BeaconKey: crate::deps::aws_cryptography_keyStore::conversions::beacon_key_materials::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials,
    >,
) -> crate::types::Materials {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::Encryption {
    Encryption: x @ _,
} => crate::types::Materials::Encryption(crate::conversions::encryption_materials::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::Decryption {
    Decryption: x @ _,
} => crate::types::Materials::Decryption(crate::conversions::decryption_materials::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::BranchKey {
    BranchKey: x @ _,
} => crate::types::Materials::BranchKey(crate::deps::aws_cryptography_keyStore::conversions::branch_key_materials::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Materials::BeaconKey {
    BeaconKey: x @ _,
} => crate::types::Materials::BeaconKey(crate::deps::aws_cryptography_keyStore::conversions::beacon_key_materials::from_dafny(x.clone())
),
    }
}
