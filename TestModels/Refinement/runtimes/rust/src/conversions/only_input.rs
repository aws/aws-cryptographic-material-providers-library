// Code generated by software.amazon.smithy.rust.codegen.smithy-rs. DO NOT EDIT.

use std::any::Any;

#[allow(dead_code)]
pub fn to_dafny_error(
    value: crate::operation::only_input::OnlyInputError,
) -> ::std::rc::Rc<crate::r#simple::refinement::internaldafny::types::Error> {
    match value {
        crate::operation::only_input::OnlyInputError::Unhandled(unhandled) => ::std::rc::Rc::new(
            crate::r#simple::refinement::internaldafny::types::Error::Opaque {
                obj: ::dafny_runtime::upcast_object()(
                    ::dafny_runtime::object::new(unhandled),
                ),
            },
        ),
    }
}

#[allow(dead_code)]
pub fn from_dafny_error(
    dafny_value: ::std::rc::Rc<
        crate::r#simple::refinement::internaldafny::types::Error,
    >,
) -> crate::operation::only_input::OnlyInputError {
    // TODO: Losing information here, but we have to figure out how to wrap an arbitrary Dafny value as std::error::Error
    if matches!(&dafny_value.as_ref(), crate::r#simple::refinement::internaldafny::types::Error::CollectionOfErrors { .. }) {
    let error_message = "TODO: can't get message yet";
    crate::operation::only_input::OnlyInputError::generic(::aws_smithy_types::error::metadata::ErrorMetadata::builder().message(error_message).build())
  } else {
    crate::operation::only_input::OnlyInputError::generic(::aws_smithy_types::error::metadata::ErrorMetadata::builder().message("Opaque error").build())
  }
}

pub mod _only_input_input;

pub mod _only_input_output;