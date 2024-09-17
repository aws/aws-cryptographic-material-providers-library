// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::RawEcdhStaticConfigurations,
) -> ::std::rc::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations,
> {
    ::std::rc::Rc::new(match value {
        crate::types::RawEcdhStaticConfigurations::PublicKeyDiscovery(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::PublicKeyDiscovery {
        PublicKeyDiscovery: crate::conversions::public_key_discovery_input::to_dafny(&x.clone())
,
    },
crate::types::RawEcdhStaticConfigurations::RawPrivateKeyToStaticPublicKey(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::RawPrivateKeyToStaticPublicKey {
        RawPrivateKeyToStaticPublicKey: crate::conversions::raw_private_key_to_static_public_key_input::to_dafny(&x.clone())
,
    },
crate::types::RawEcdhStaticConfigurations::EphemeralPrivateKeyToStaticPublicKey(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::EphemeralPrivateKeyToStaticPublicKey {
        EphemeralPrivateKeyToStaticPublicKey: crate::conversions::ephemeral_private_key_to_static_public_key_input::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::std::rc::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations,
    >,
) -> crate::types::RawEcdhStaticConfigurations {
    match &::std::rc::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::PublicKeyDiscovery {
    PublicKeyDiscovery: x @ _,
} => crate::types::RawEcdhStaticConfigurations::PublicKeyDiscovery(crate::conversions::public_key_discovery_input::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::RawPrivateKeyToStaticPublicKey {
    RawPrivateKeyToStaticPublicKey: x @ _,
} => crate::types::RawEcdhStaticConfigurations::RawPrivateKeyToStaticPublicKey(crate::conversions::raw_private_key_to_static_public_key_input::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::RawEcdhStaticConfigurations::EphemeralPrivateKeyToStaticPublicKey {
    EphemeralPrivateKeyToStaticPublicKey: x @ _,
} => crate::types::RawEcdhStaticConfigurations::EphemeralPrivateKeyToStaticPublicKey(crate::conversions::ephemeral_private_key_to_static_public_key_input::from_dafny(x.clone())
),
    }
}
