// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
use std::sync::LazyLock;
use crate::deps::com_amazonaws_kms::conversions;

#[derive(::std::clone::Clone, ::std::fmt::Debug)]
pub struct Client {
    pub inner: aws_sdk_kms::Client
}

impl ::std::cmp::PartialEq for Client {
  fn eq(&self, other: &Self) -> bool {
    false
  }
}

/// A runtime for executing operations on the asynchronous client in a blocking manner.
/// Necessary because Dafny only generates synchronous code.
static dafny_tokio_runtime: LazyLock<tokio::runtime::Runtime> = LazyLock::new(|| {
    tokio::runtime::Builder::new_multi_thread()
          .enable_all()
          .build()
          .unwrap()
});

impl dafny_runtime::UpcastObject<dyn std::any::Any> for Client {
    ::dafny_runtime::UpcastObjectFn!(dyn::std::any::Any);
}

impl dafny_runtime::UpcastObject<dyn crate::r#software::amazon::cryptography::services::kms::internaldafny::types::IKMSClient> for Client {
  ::dafny_runtime::UpcastObjectFn!(dyn crate::r#software::amazon::cryptography::services::kms::internaldafny::types::IKMSClient);
}

impl crate::r#software::amazon::cryptography::services::kms::internaldafny::types::IKMSClient
  for Client {
 fn CancelKeyDeletion(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CancelKeyDeletionRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CancelKeyDeletionResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::cancel_key_deletion::_cancel_key_deletion_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::cancel_key_deletion::_cancel_key_deletion_response::to_dafny,
    conversions::cancel_key_deletion::to_dafny_error)
}
 fn ConnectCustomKeyStore(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ConnectCustomKeyStoreRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ConnectCustomKeyStoreResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::connect_custom_key_store::_connect_custom_key_store_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::connect_custom_key_store::_connect_custom_key_store_response::to_dafny,
    conversions::connect_custom_key_store::to_dafny_error)
}
 fn CreateAlias(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateAliasRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::create_alias::_create_alias_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_alias::_create_alias_response::to_dafny,
    conversions::create_alias::to_dafny_error)
}
 fn CreateCustomKeyStore(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateCustomKeyStoreRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateCustomKeyStoreResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::create_custom_key_store::_create_custom_key_store_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_custom_key_store::_create_custom_key_store_response::to_dafny,
    conversions::create_custom_key_store::to_dafny_error)
}
 fn CreateGrant(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateGrantRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateGrantResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::create_grant::_create_grant_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_grant::_create_grant_response::to_dafny,
    conversions::create_grant::to_dafny_error)
}
 fn CreateKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::CreateKeyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::create_key::_create_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_key::_create_key_response::to_dafny,
    conversions::create_key::to_dafny_error)
}
 fn Decrypt(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DecryptRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DecryptResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::decrypt::_decrypt_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::decrypt::_decrypt_response::to_dafny,
    conversions::decrypt::to_dafny_error)
}
 fn DeleteAlias(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeleteAliasRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::delete_alias::_delete_alias_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_alias::_delete_alias_response::to_dafny,
    conversions::delete_alias::to_dafny_error)
}
 fn DeleteCustomKeyStore(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeleteCustomKeyStoreRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeleteCustomKeyStoreResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::delete_custom_key_store::_delete_custom_key_store_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_custom_key_store::_delete_custom_key_store_response::to_dafny,
    conversions::delete_custom_key_store::to_dafny_error)
}
 fn DeleteImportedKeyMaterial(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeleteImportedKeyMaterialRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::delete_imported_key_material::_delete_imported_key_material_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_imported_key_material::_delete_imported_key_material_response::to_dafny,
    conversions::delete_imported_key_material::to_dafny_error)
}
 fn DeriveSharedSecret(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeriveSharedSecretRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DeriveSharedSecretResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::derive_shared_secret::_derive_shared_secret_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::derive_shared_secret::_derive_shared_secret_response::to_dafny,
    conversions::derive_shared_secret::to_dafny_error)
}
 fn DescribeCustomKeyStores(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DescribeCustomKeyStoresRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DescribeCustomKeyStoresResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::describe_custom_key_stores::_describe_custom_key_stores_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_custom_key_stores::_describe_custom_key_stores_response::to_dafny,
    conversions::describe_custom_key_stores::to_dafny_error)
}
 fn DescribeKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DescribeKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DescribeKeyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::describe_key::_describe_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_key::_describe_key_response::to_dafny,
    conversions::describe_key::to_dafny_error)
}
 fn DisableKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DisableKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::disable_key::_disable_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::disable_key::_disable_key_response::to_dafny,
    conversions::disable_key::to_dafny_error)
}
 fn DisableKeyRotation(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DisableKeyRotationRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::disable_key_rotation::_disable_key_rotation_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::disable_key_rotation::_disable_key_rotation_response::to_dafny,
    conversions::disable_key_rotation::to_dafny_error)
}
 fn DisconnectCustomKeyStore(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DisconnectCustomKeyStoreRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::DisconnectCustomKeyStoreResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::disconnect_custom_key_store::_disconnect_custom_key_store_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::disconnect_custom_key_store::_disconnect_custom_key_store_response::to_dafny,
    conversions::disconnect_custom_key_store::to_dafny_error)
}
 fn EnableKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::EnableKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::enable_key::_enable_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::enable_key::_enable_key_response::to_dafny,
    conversions::enable_key::to_dafny_error)
}
 fn EnableKeyRotation(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::EnableKeyRotationRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::enable_key_rotation::_enable_key_rotation_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::enable_key_rotation::_enable_key_rotation_response::to_dafny,
    conversions::enable_key_rotation::to_dafny_error)
}
 fn Encrypt(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::EncryptRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::EncryptResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::encrypt::_encrypt_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::encrypt::_encrypt_response::to_dafny,
    conversions::encrypt::to_dafny_error)
}
 fn GenerateDataKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_data_key::_generate_data_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_data_key::_generate_data_key_response::to_dafny,
    conversions::generate_data_key::to_dafny_error)
}
 fn GenerateDataKeyPair(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_data_key_pair::_generate_data_key_pair_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_data_key_pair::_generate_data_key_pair_response::to_dafny,
    conversions::generate_data_key_pair::to_dafny_error)
}
 fn GenerateDataKeyPairWithoutPlaintext(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairWithoutPlaintextRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyPairWithoutPlaintextResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_data_key_pair_without_plaintext::_generate_data_key_pair_without_plaintext_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_data_key_pair_without_plaintext::_generate_data_key_pair_without_plaintext_response::to_dafny,
    conversions::generate_data_key_pair_without_plaintext::to_dafny_error)
}
 fn GenerateDataKeyWithoutPlaintext(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyWithoutPlaintextRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateDataKeyWithoutPlaintextResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_data_key_without_plaintext::_generate_data_key_without_plaintext_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_data_key_without_plaintext::_generate_data_key_without_plaintext_response::to_dafny,
    conversions::generate_data_key_without_plaintext::to_dafny_error)
}
 fn GenerateMac(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateMacRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateMacResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_mac::_generate_mac_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_mac::_generate_mac_response::to_dafny,
    conversions::generate_mac::to_dafny_error)
}
 fn GenerateRandom(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateRandomRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GenerateRandomResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::generate_random::_generate_random_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::generate_random::_generate_random_response::to_dafny,
    conversions::generate_random::to_dafny_error)
}
 fn GetKeyPolicy(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetKeyPolicyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetKeyPolicyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::get_key_policy::_get_key_policy_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::get_key_policy::_get_key_policy_response::to_dafny,
    conversions::get_key_policy::to_dafny_error)
}
 fn GetKeyRotationStatus(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetKeyRotationStatusRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetKeyRotationStatusResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::get_key_rotation_status::_get_key_rotation_status_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::get_key_rotation_status::_get_key_rotation_status_response::to_dafny,
    conversions::get_key_rotation_status::to_dafny_error)
}
 fn GetParametersForImport(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetParametersForImportRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetParametersForImportResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::get_parameters_for_import::_get_parameters_for_import_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::get_parameters_for_import::_get_parameters_for_import_response::to_dafny,
    conversions::get_parameters_for_import::to_dafny_error)
}
 fn GetPublicKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetPublicKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::GetPublicKeyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::get_public_key::_get_public_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::get_public_key::_get_public_key_response::to_dafny,
    conversions::get_public_key::to_dafny_error)
}
 fn ImportKeyMaterial(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ImportKeyMaterialRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ImportKeyMaterialResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::import_key_material::_import_key_material_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::import_key_material::_import_key_material_response::to_dafny,
    conversions::import_key_material::to_dafny_error)
}
 fn ListAliases(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListAliasesRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListAliasesResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_aliases::_list_aliases_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_aliases::_list_aliases_response::to_dafny,
    conversions::list_aliases::to_dafny_error)
}
 fn ListGrants(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListGrantsRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListGrantsResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_grants::_list_grants_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_grants::_list_grants_response::to_dafny,
    conversions::list_grants::to_dafny_error)
}
 fn ListKeyPolicies(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeyPoliciesRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeyPoliciesResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_key_policies::_list_key_policies_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_key_policies::_list_key_policies_response::to_dafny,
    conversions::list_key_policies::to_dafny_error)
}
 fn ListKeyRotations(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeyRotationsRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeyRotationsResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_key_rotations::_list_key_rotations_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_key_rotations::_list_key_rotations_response::to_dafny,
    conversions::list_key_rotations::to_dafny_error)
}
 fn ListKeys(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeysRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListKeysResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_keys::_list_keys_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_keys::_list_keys_response::to_dafny,
    conversions::list_keys::to_dafny_error)
}
 fn ListResourceTags(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListResourceTagsRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ListResourceTagsResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::list_resource_tags::_list_resource_tags_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_resource_tags::_list_resource_tags_response::to_dafny,
    conversions::list_resource_tags::to_dafny_error)
}
 fn PutKeyPolicy(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::PutKeyPolicyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::put_key_policy::_put_key_policy_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::put_key_policy::_put_key_policy_response::to_dafny,
    conversions::put_key_policy::to_dafny_error)
}
 fn ReEncrypt(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ReEncryptRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ReEncryptResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::re_encrypt::_re_encrypt_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::re_encrypt::_re_encrypt_response::to_dafny,
    conversions::re_encrypt::to_dafny_error)
}
 fn ReplicateKey(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ReplicateKeyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ReplicateKeyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::replicate_key::_replicate_key_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::replicate_key::_replicate_key_response::to_dafny,
    conversions::replicate_key::to_dafny_error)
}
 fn RetireGrant(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::RetireGrantRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::retire_grant::_retire_grant_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::retire_grant::_retire_grant_response::to_dafny,
    conversions::retire_grant::to_dafny_error)
}
 fn RevokeGrant(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::RevokeGrantRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::revoke_grant::_revoke_grant_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::revoke_grant::_revoke_grant_response::to_dafny,
    conversions::revoke_grant::to_dafny_error)
}
 fn RotateKeyOnDemand(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::RotateKeyOnDemandRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::RotateKeyOnDemandResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::rotate_key_on_demand::_rotate_key_on_demand_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::rotate_key_on_demand::_rotate_key_on_demand_response::to_dafny,
    conversions::rotate_key_on_demand::to_dafny_error)
}
 fn ScheduleKeyDeletion(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ScheduleKeyDeletionRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::ScheduleKeyDeletionResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::schedule_key_deletion::_schedule_key_deletion_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::schedule_key_deletion::_schedule_key_deletion_response::to_dafny,
    conversions::schedule_key_deletion::to_dafny_error)
}
 fn Sign(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::SignRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::SignResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::sign::_sign_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::sign::_sign_response::to_dafny,
    conversions::sign::to_dafny_error)
}
 fn TagResource(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::TagResourceRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::tag_resource::_tag_resource_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::tag_resource::_tag_resource_response::to_dafny,
    conversions::tag_resource::to_dafny_error)
}
 fn UntagResource(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UntagResourceRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::untag_resource::_untag_resource_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::untag_resource::_untag_resource_response::to_dafny,
    conversions::untag_resource::to_dafny_error)
}
 fn UpdateAlias(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UpdateAliasRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::update_alias::_update_alias_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_alias::_update_alias_response::to_dafny,
    conversions::update_alias::to_dafny_error)
}
 fn UpdateCustomKeyStore(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UpdateCustomKeyStoreRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UpdateCustomKeyStoreResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::update_custom_key_store::_update_custom_key_store_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_custom_key_store::_update_custom_key_store_response::to_dafny,
    conversions::update_custom_key_store::to_dafny_error)
}
 fn UpdateKeyDescription(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UpdateKeyDescriptionRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::update_key_description::_update_key_description_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_key_description::_update_key_description_response::to_dafny,
    conversions::update_key_description::to_dafny_error)
}
 fn UpdatePrimaryRegion(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::UpdatePrimaryRegionRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::update_primary_region::_update_primary_region_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_primary_region::_update_primary_region_response::to_dafny,
    conversions::update_primary_region::to_dafny_error)
}
 fn Verify(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::VerifyRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::VerifyResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::verify::_verify_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::verify::_verify_response::to_dafny,
    conversions::verify::to_dafny_error)
}
 fn VerifyMac(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::VerifyMacRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::VerifyMacResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::kms::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_kms::conversions::verify_mac::_verify_mac_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::verify_mac::_verify_mac_response::to_dafny,
    conversions::verify_mac::to_dafny_error)
} }
