// Code generated by software.amazon.smithy.rust.codegen.smithy-rs. DO NOT EDIT.
#[allow(missing_docs)] // documentation missing in model
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct GetRefinementOutput {
    #[allow(missing_docs)] // documentation missing in model
    pub required_string: ::std::string::String,
    #[allow(missing_docs)] // documentation missing in model
    pub optional_string: ::std::option::Option<::std::string::String>,
}
impl GetRefinementOutput {
    #[allow(missing_docs)] // documentation missing in model
    pub fn required_string(&self) -> &str {
        use std::ops::Deref;
        self.required_string.deref()
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn optional_string(&self) -> ::std::option::Option<&str> {
        self.optional_string.as_deref()
    }
}
impl GetRefinementOutput {
    /// Creates a new builder-style object to manufacture [`GetRefinementOutput`](crate::operation::get_refinement::GetRefinementOutput).
    pub fn builder() -> crate::operation::get_refinement::builders::GetRefinementOutputBuilder {
        crate::operation::get_refinement::builders::GetRefinementOutputBuilder::default()
    }
}

/// A builder for [`GetRefinementOutput`](crate::operation::get_refinement::GetRefinementOutput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct GetRefinementOutputBuilder {
    pub(crate) required_string: ::std::option::Option<::std::string::String>,
    pub(crate) optional_string: ::std::option::Option<::std::string::String>,
}
impl GetRefinementOutputBuilder {
    #[allow(missing_docs)] // documentation missing in model
    /// This field is required.
    pub fn required_string(
        mut self,
        input: impl ::std::convert::Into<::std::string::String>,
    ) -> Self {
        self.required_string = ::std::option::Option::Some(input.into());
        self
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn set_required_string(
        mut self,
        input: ::std::option::Option<::std::string::String>,
    ) -> Self {
        self.required_string = input;
        self
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn get_required_string(&self) -> &::std::option::Option<::std::string::String> {
        &self.required_string
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn optional_string(
        mut self,
        input: impl ::std::convert::Into<::std::string::String>,
    ) -> Self {
        self.optional_string = ::std::option::Option::Some(input.into());
        self
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn set_optional_string(
        mut self,
        input: ::std::option::Option<::std::string::String>,
    ) -> Self {
        self.optional_string = input;
        self
    }
    #[allow(missing_docs)] // documentation missing in model
    pub fn get_optional_string(&self) -> &::std::option::Option<::std::string::String> {
        &self.optional_string
    }
    /// Consumes the builder and constructs a [`GetRefinementOutput`](crate::operation::get_refinement::GetRefinementOutput).
    /// This method will fail if any of the following fields are not set:
    /// - [`required_string`](crate::operation::get_refinement::builders::GetRefinementOutputBuilder::required_string)
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::operation::get_refinement::GetRefinementOutput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::operation::get_refinement::GetRefinementOutput {
            required_string: self.required_string.ok_or_else(|| {
                ::aws_smithy_types::error::operation::BuildError::missing_field(
                    "required_string",
                    "required_string was not specified but it is required when building GetRefinementOutput",
                )
            })?,
            optional_string: self.optional_string,
        })
    }
}