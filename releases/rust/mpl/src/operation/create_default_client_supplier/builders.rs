// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
pub use crate::operation::create_default_client_supplier::_create_default_client_supplier_output::CreateDefaultClientSupplierOutputBuilder;

pub use crate::operation::create_default_client_supplier::_create_default_client_supplier_input::CreateDefaultClientSupplierInputBuilder;

impl CreateDefaultClientSupplierInputBuilder {
    /// Sends a request with this input using the given client.
    pub async fn send_with(
        self,
        client: &crate::client::Client,
    ) -> ::std::result::Result<
        crate::types::client_supplier::ClientSupplierRef,
        crate::types::error::Error,
    > {
        let mut fluent_builder = client.create_default_client_supplier();
        fluent_builder.inner = self;
        fluent_builder.send().await
    }
}
/// Fluent builder constructing a request to `CreateDefaultClientSupplier`.
///
#[derive(::std::clone::Clone, ::std::fmt::Debug)]
pub struct CreateDefaultClientSupplierFluentBuilder {
    client: crate::client::Client,
    pub(crate) inner: crate::operation::create_default_client_supplier::builders::CreateDefaultClientSupplierInputBuilder,
}
impl CreateDefaultClientSupplierFluentBuilder {
    /// Creates a new `CreateDefaultClientSupplier`.
    pub(crate) fn new(client: crate::client::Client) -> Self {
        Self {
            client,
            inner: ::std::default::Default::default(),
        }
    }
    /// Access the CreateDefaultClientSupplier as a reference.
    pub fn as_input(&self) -> &crate::operation::create_default_client_supplier::builders::CreateDefaultClientSupplierInputBuilder{
        &self.inner
    }
    /// Sends the request and returns the response.
    pub async fn send(
        self,
    ) -> ::std::result::Result<
        crate::types::client_supplier::ClientSupplierRef,
        crate::types::error::Error,
    > {
        let input = self
            .inner
            .build()
            // Using Opaque since we don't have a validation-specific error yet.
            // Operations' models don't declare their own validation error,
            // and smithy-rs seems to not generate a ValidationError case unless there is.
            // Vanilla smithy-rs uses SdkError::construction_failure, but we aren't using SdkError.
            .map_err(|mut e| {
                let msg = format!("{:?}", e);
                crate::types::error::Error::OpaqueWithText {
                    obj: ::dafny_runtime::Object::from_ref(&mut e as &mut ::dafny_runtime::DynAny),
                    objMessage: msg,
                }
            })?;
        crate::operation::create_default_client_supplier::CreateDefaultClientSupplier::send(
            &self.client,
            input,
        )
        .await
    }
}
