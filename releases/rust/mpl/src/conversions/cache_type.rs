// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::CacheType,
) -> ::dafny_runtime::Rc<
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType,
> {
    ::dafny_runtime::Rc::new(match value {
        crate::types::CacheType::Default(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::Default {
        Default: crate::conversions::default_cache::to_dafny(&x.clone())
,
    },
crate::types::CacheType::No(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::No {
        No: crate::conversions::no_cache::to_dafny(&x.clone())
,
    },
crate::types::CacheType::SingleThreaded(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::SingleThreaded {
        SingleThreaded: crate::conversions::single_threaded_cache::to_dafny(&x.clone())
,
    },
crate::types::CacheType::MultiThreaded(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::MultiThreaded {
        MultiThreaded: crate::conversions::multi_threaded_cache::to_dafny(&x.clone())
,
    },
crate::types::CacheType::StormTracking(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::StormTracking {
        StormTracking: crate::conversions::storm_tracking_cache::to_dafny(&x.clone())
,
    },
crate::types::CacheType::Shared(x) =>
    crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::Shared {
        Shared: crate::conversions::cryptographic_materials_cache::to_dafny(&x.clone())
,
    },
        _ => panic!("Unknown union variant: {:?}", value),
    })
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Rc<
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType,
    >,
) -> crate::types::CacheType {
    match &::dafny_runtime::Rc::unwrap_or_clone(dafny_value) {
        crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::Default {
    Default: x @ _,
} => crate::types::CacheType::Default(crate::conversions::default_cache::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::No {
    No: x @ _,
} => crate::types::CacheType::No(crate::conversions::no_cache::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::SingleThreaded {
    SingleThreaded: x @ _,
} => crate::types::CacheType::SingleThreaded(crate::conversions::single_threaded_cache::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::MultiThreaded {
    MultiThreaded: x @ _,
} => crate::types::CacheType::MultiThreaded(crate::conversions::multi_threaded_cache::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::StormTracking {
    StormTracking: x @ _,
} => crate::types::CacheType::StormTracking(crate::conversions::storm_tracking_cache::from_dafny(x.clone())
),
crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::CacheType::Shared {
    Shared: x @ _,
} => crate::types::CacheType::Shared(crate::conversions::cryptographic_materials_cache::from_dafny(x.clone())
),
    }
}
