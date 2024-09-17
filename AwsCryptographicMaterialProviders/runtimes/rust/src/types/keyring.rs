// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

pub trait Keyring {
    fn on_encrypt(
    &mut self,
    input: crate::operation::on_encrypt::OnEncryptInput,
  ) -> Result<
    crate::operation::on_encrypt::OnEncryptOutput,
    crate::types::error::Error,
  >;

  fn on_decrypt(
    &mut self,
    input: crate::operation::on_decrypt::OnDecryptInput,
  ) -> Result<
    crate::operation::on_decrypt::OnDecryptOutput,
    crate::types::error::Error,
  >;
}

#[derive(::std::clone::Clone)]
pub struct KeyringRef {
  pub inner: ::std::rc::Rc<std::cell::RefCell<dyn Keyring>>
}

impl ::std::cmp::PartialEq for KeyringRef {
    fn eq(&self, other: &KeyringRef) -> bool {
        ::std::rc::Rc::ptr_eq(&self.inner, &other.inner)
    }
}

impl ::std::fmt::Debug for KeyringRef {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "<KeyringRef>")
    }
}

mod on_encrypt;

mod on_decrypt;
