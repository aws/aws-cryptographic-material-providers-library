// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

pub trait CryptographicMaterialsCache {
    fn put_cache_entry(
    &mut self,
    input: crate::operation::put_cache_entry::PutCacheEntryInput,
  ) -> Result<
    (),
    crate::types::error::Error,
  >;

  fn update_usage_metadata(
    &mut self,
    input: crate::operation::update_usage_metadata::UpdateUsageMetadataInput,
  ) -> Result<
    (),
    crate::types::error::Error,
  >;

  fn get_cache_entry(
    &mut self,
    input: crate::operation::get_cache_entry::GetCacheEntryInput,
  ) -> Result<
    crate::operation::get_cache_entry::GetCacheEntryOutput,
    crate::types::error::Error,
  >;

  fn delete_cache_entry(
    &mut self,
    input: crate::operation::delete_cache_entry::DeleteCacheEntryInput,
  ) -> Result<
    (),
    crate::types::error::Error,
  >;
}

#[derive(::std::clone::Clone)]
pub struct CryptographicMaterialsCacheRef {
  pub inner: ::std::rc::Rc<std::cell::RefCell<dyn CryptographicMaterialsCache>>
}

impl ::std::cmp::PartialEq for CryptographicMaterialsCacheRef {
    fn eq(&self, other: &CryptographicMaterialsCacheRef) -> bool {
        ::std::rc::Rc::ptr_eq(&self.inner, &other.inner)
    }
}

impl ::std::fmt::Debug for CryptographicMaterialsCacheRef {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "<CryptographicMaterialsCacheRef>")
    }
}

mod put_cache_entry;

mod update_usage_metadata;

mod get_cache_entry;

mod delete_cache_entry;
