// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(dead_code)]
pub fn to_dafny(
    value: &crate::types::branch_key_id_supplier::BranchKeyIdSupplierRef,
) -> ::dafny_runtime::Object<
  dyn crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::IBranchKeyIdSupplier,
>{
    let wrap = BranchKeyIdSupplierWrapper { obj: value.clone() };
    let inner = ::dafny_runtime::Rc::new(::dafny_runtime::UnsafeCell::new(wrap));
    ::dafny_runtime::Object(Some(inner))
}

pub struct BranchKeyIdSupplierWrapper {
    obj: crate::types::branch_key_id_supplier::BranchKeyIdSupplierRef,
}

impl ::dafny_runtime::UpcastObject<::dafny_runtime::DynAny> for BranchKeyIdSupplierWrapper {
    ::dafny_runtime::UpcastObjectFn!(::dafny_runtime::DynAny);
}

#[allow(dead_code)]
pub fn from_dafny(
    dafny_value: ::dafny_runtime::Object<
      dyn crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::IBranchKeyIdSupplier,
    >,
) -> crate::types::branch_key_id_supplier::BranchKeyIdSupplierRef {
    let wrap = IBranchKeyIdSupplierDafnyWrapper {
        obj: dafny_value.clone(),
    };
    crate::types::branch_key_id_supplier::BranchKeyIdSupplierRef {
        inner: ::dafny_runtime::Rc::new(::dafny_runtime::RefCell::new(wrap)),
    }
}

#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct IBranchKeyIdSupplierDafnyWrapper {
  pub(crate) obj: ::dafny_runtime::Object<
      dyn crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::IBranchKeyIdSupplier,
  >,
}

impl crate::software::amazon::cryptography::materialproviders::internaldafny::types::IBranchKeyIdSupplier
  for BranchKeyIdSupplierWrapper
{
  fn r#_GetBranchKeyId_k(
    &self,
    input: &::dafny_runtime::Rc<crate::software::amazon::cryptography::materialproviders::internaldafny::types::GetBranchKeyIdInput>,
) -> ::dafny_runtime::Rc<
    crate::r#_Wrappers_Compile::Result<
        ::dafny_runtime::Rc<crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::GetBranchKeyIdOutput>,
        ::dafny_runtime::Rc<crate::r#software::amazon::cryptography::materialproviders::internaldafny::types::Error>,
    >,
>
{
    let inner_input = crate::conversions::get_branch_key_id::_get_branch_key_id_input::from_dafny(input.clone());
    let inner_result = self.obj.inner.lock().unwrap().get_branch_key_id(inner_input);
    let result = match inner_result {
        Ok(x) => crate::r#_Wrappers_Compile::Result::Success {
            value: crate::conversions::get_branch_key_id::_get_branch_key_id_output::to_dafny(x.clone()),
        },
        Err(x) => crate::r#_Wrappers_Compile::Result::Failure {
            error: crate::conversions::error::to_dafny(x),
        },
    };
    ::dafny_runtime::Rc::new(result)
}
}

impl crate::types::branch_key_id_supplier::BranchKeyIdSupplier
    for IBranchKeyIdSupplierDafnyWrapper
{
    fn get_branch_key_id(
        &self,
        input: crate::operation::get_branch_key_id::GetBranchKeyIdInput,
    ) -> Result<crate::operation::get_branch_key_id::GetBranchKeyIdOutput, crate::types::error::Error>
    {
        let inner_input =
            crate::conversions::get_branch_key_id::_get_branch_key_id_input::to_dafny(input);
        let inner_result = ::dafny_runtime::md!(self.obj.clone()).GetBranchKeyId(&inner_input);
        if matches!(
            inner_result.as_ref(),
            crate::r#_Wrappers_Compile::Result::Success { .. }
        ) {
            Ok(
                crate::conversions::get_branch_key_id::_get_branch_key_id_output::from_dafny(
                    inner_result.value().clone(),
                ),
            )
        } else {
            Err(crate::conversions::error::from_dafny(
                inner_result.error().clone(),
            ))
        }
    }
}
