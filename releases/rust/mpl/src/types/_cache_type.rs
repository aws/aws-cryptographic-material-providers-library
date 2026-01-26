// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
#[allow(missing_docs)]
pub enum CacheType {
    #[allow(missing_docs)]
    Default(crate::types::DefaultCache),
    #[allow(missing_docs)]
    No(crate::types::NoCache),
    #[allow(missing_docs)]
    SingleThreaded(crate::types::SingleThreadedCache),
    #[allow(missing_docs)]
    MultiThreaded(crate::types::MultiThreadedCache),
    #[allow(missing_docs)]
    StormTracking(crate::types::StormTrackingCache),
    /// Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.
    Shared(crate::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef),
    /// The `Unknown` variant represents cases where new union variant was received. Consider upgrading the SDK to the latest available version.
    /// An unknown enum variant
    ///
    /// _Note: If you encounter this error, consider upgrading your SDK to the latest version._
    /// The `Unknown` variant represents cases where the server sent a value that wasn't recognized
    /// by the client. This can happen when the server adds new functionality, but the client has not been updated.
    /// To investigate this, consider turning on debug logging to print the raw HTTP response.
    #[non_exhaustive]
    Unknown,
}
impl CacheType {
    /// Tries to convert the enum instance into [`Default`](crate::types::CacheType::Default), extracting the inner [`crate::types::DefaultCache`](crate::types::DefaultCache).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_default(&self) -> ::std::result::Result<&crate::types::DefaultCache, &Self> {
        if let crate::types::CacheType::Default(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Tries to convert the enum instance into [`No`](crate::types::CacheType::No), extracting the inner [`crate::types::NoCache`](crate::types::NoCache).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_no(&self) -> ::std::result::Result<&crate::types::NoCache, &Self> {
        if let crate::types::CacheType::No(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Tries to convert the enum instance into [`SingleThreaded`](crate::types::CacheType::SingleThreaded), extracting the inner [`crate::types::SingleThreadedCache`](crate::types::SingleThreadedCache).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_single_threaded(
        &self,
    ) -> ::std::result::Result<&crate::types::SingleThreadedCache, &Self> {
        if let crate::types::CacheType::SingleThreaded(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Tries to convert the enum instance into [`MultiThreaded`](crate::types::CacheType::MultiThreaded), extracting the inner [`crate::types::MultiThreadedCache`](crate::types::MultiThreadedCache).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_multi_threaded(
        &self,
    ) -> ::std::result::Result<&crate::types::MultiThreadedCache, &Self> {
        if let crate::types::CacheType::MultiThreaded(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Tries to convert the enum instance into [`StormTracking`](crate::types::CacheType::StormTracking), extracting the inner [`crate::types::StormTrackingCache`](crate::types::StormTrackingCache).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_storm_tracking(
        &self,
    ) -> ::std::result::Result<&crate::types::StormTrackingCache, &Self> {
        if let crate::types::CacheType::StormTracking(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Tries to convert the enum instance into [`Shared`](crate::types::CacheType::Shared), extracting the inner [`crate::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef`](crate::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef).
    /// Returns `Err(&Self)` if it can't be converted.
    pub fn as_shared(
        &self,
    ) -> ::std::result::Result<
        &crate::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef,
        &Self,
    > {
        if let crate::types::CacheType::Shared(val) = &self {
            ::std::result::Result::Ok(val)
        } else {
            ::std::result::Result::Err(self)
        }
    }
    /// Returns true if this is a [`Default`](crate::types::CacheType::Default).
    pub fn is_default(&self) -> ::std::primitive::bool {
        self.as_default().is_ok()
    }
    /// Returns true if this is a [`No`](crate::types::CacheType::No).
    pub fn is_no(&self) -> ::std::primitive::bool {
        self.as_no().is_ok()
    }
    /// Returns true if this is a [`SingleThreaded`](crate::types::CacheType::SingleThreaded).
    pub fn is_single_threaded(&self) -> ::std::primitive::bool {
        self.as_single_threaded().is_ok()
    }
    /// Returns true if this is a [`MultiThreaded`](crate::types::CacheType::MultiThreaded).
    pub fn is_multi_threaded(&self) -> ::std::primitive::bool {
        self.as_multi_threaded().is_ok()
    }
    /// Returns true if this is a [`StormTracking`](crate::types::CacheType::StormTracking).
    pub fn is_storm_tracking(&self) -> ::std::primitive::bool {
        self.as_storm_tracking().is_ok()
    }
    /// Returns true if this is a [`Shared`](crate::types::CacheType::Shared).
    pub fn is_shared(&self) -> ::std::primitive::bool {
        self.as_shared().is_ok()
    }
    /// Returns true if the enum instance is the `Unknown` variant.
    pub fn is_unknown(&self) -> ::std::primitive::bool {
        matches!(self, Self::Unknown)
    }
}
