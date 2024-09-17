// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
use std::sync::LazyLock;
use crate::deps::com_amazonaws_dynamodb::conversions;

#[derive(::std::clone::Clone, ::std::fmt::Debug)]
pub struct Client {
    pub inner: aws_sdk_dynamodb::Client
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

impl dafny_runtime::UpcastObject<dyn crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::IDynamoDBClient> for Client {
  ::dafny_runtime::UpcastObjectFn!(dyn crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::IDynamoDBClient);
}

impl crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::IDynamoDBClient
  for Client {
 fn BatchExecuteStatement(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchExecuteStatementInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchExecuteStatementOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::batch_execute_statement::_batch_execute_statement_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::batch_execute_statement::_batch_execute_statement_response::to_dafny,
    conversions::batch_execute_statement::to_dafny_error)
}
 fn BatchGetItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchGetItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchGetItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::batch_get_item::_batch_get_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::batch_get_item::_batch_get_item_response::to_dafny,
    conversions::batch_get_item::to_dafny_error)
}
 fn BatchWriteItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchWriteItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::BatchWriteItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::batch_write_item::_batch_write_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::batch_write_item::_batch_write_item_response::to_dafny,
    conversions::batch_write_item::to_dafny_error)
}
 fn CreateBackup(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateBackupInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateBackupOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::create_backup::_create_backup_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_backup::_create_backup_response::to_dafny,
    conversions::create_backup::to_dafny_error)
}
 fn CreateGlobalTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateGlobalTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateGlobalTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::create_global_table::_create_global_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_global_table::_create_global_table_response::to_dafny,
    conversions::create_global_table::to_dafny_error)
}
 fn CreateTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::CreateTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::create_table::_create_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::create_table::_create_table_response::to_dafny,
    conversions::create_table::to_dafny_error)
}
 fn DeleteBackup(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteBackupInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteBackupOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::delete_backup::_delete_backup_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_backup::_delete_backup_response::to_dafny,
    conversions::delete_backup::to_dafny_error)
}
 fn DeleteItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::delete_item::_delete_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_item::_delete_item_response::to_dafny,
    conversions::delete_item::to_dafny_error)
}
 fn DeleteTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DeleteTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::delete_table::_delete_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::delete_table::_delete_table_response::to_dafny,
    conversions::delete_table::to_dafny_error)
}
 fn DescribeBackup(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeBackupInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeBackupOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_backup::_describe_backup_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_backup::_describe_backup_response::to_dafny,
    conversions::describe_backup::to_dafny_error)
}
 fn DescribeContinuousBackups(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeContinuousBackupsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeContinuousBackupsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_continuous_backups::_describe_continuous_backups_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_continuous_backups::_describe_continuous_backups_response::to_dafny,
    conversions::describe_continuous_backups::to_dafny_error)
}
 fn DescribeContributorInsights(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeContributorInsightsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeContributorInsightsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_contributor_insights::_describe_contributor_insights_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_contributor_insights::_describe_contributor_insights_response::to_dafny,
    conversions::describe_contributor_insights::to_dafny_error)
}
 fn DescribeEndpoints(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeEndpointsRequest>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeEndpointsResponse>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_endpoints::_describe_endpoints_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_endpoints::_describe_endpoints_response::to_dafny,
    conversions::describe_endpoints::to_dafny_error)
}
 fn DescribeExport(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeExportInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeExportOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_export::_describe_export_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_export::_describe_export_response::to_dafny,
    conversions::describe_export::to_dafny_error)
}
 fn DescribeGlobalTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeGlobalTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeGlobalTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_global_table::_describe_global_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_global_table::_describe_global_table_response::to_dafny,
    conversions::describe_global_table::to_dafny_error)
}
 fn DescribeGlobalTableSettings(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeGlobalTableSettingsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeGlobalTableSettingsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_global_table_settings::_describe_global_table_settings_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_global_table_settings::_describe_global_table_settings_response::to_dafny,
    conversions::describe_global_table_settings::to_dafny_error)
}
 fn DescribeImport(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeImportInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeImportOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_import::_describe_import_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_import::_describe_import_response::to_dafny,
    conversions::describe_import::to_dafny_error)
}
 fn DescribeKinesisStreamingDestination(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeKinesisStreamingDestinationInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeKinesisStreamingDestinationOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_kinesis_streaming_destination::_describe_kinesis_streaming_destination_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_kinesis_streaming_destination::_describe_kinesis_streaming_destination_response::to_dafny,
    conversions::describe_kinesis_streaming_destination::to_dafny_error)
}
 fn DescribeLimits(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeLimitsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeLimitsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_limits::_describe_limits_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_limits::_describe_limits_response::to_dafny,
    conversions::describe_limits::to_dafny_error)
}
 fn DescribeTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_table::_describe_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_table::_describe_table_response::to_dafny,
    conversions::describe_table::to_dafny_error)
}
 fn DescribeTableReplicaAutoScaling(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTableReplicaAutoScalingInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTableReplicaAutoScalingOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_table_replica_auto_scaling::_describe_table_replica_auto_scaling_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_table_replica_auto_scaling::_describe_table_replica_auto_scaling_response::to_dafny,
    conversions::describe_table_replica_auto_scaling::to_dafny_error)
}
 fn DescribeTimeToLive(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTimeToLiveInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DescribeTimeToLiveOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::describe_time_to_live::_describe_time_to_live_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::describe_time_to_live::_describe_time_to_live_response::to_dafny,
    conversions::describe_time_to_live::to_dafny_error)
}
 fn DisableKinesisStreamingDestination(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DisableKinesisStreamingDestinationInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::DisableKinesisStreamingDestinationOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::disable_kinesis_streaming_destination::_disable_kinesis_streaming_destination_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::disable_kinesis_streaming_destination::_disable_kinesis_streaming_destination_response::to_dafny,
    conversions::disable_kinesis_streaming_destination::to_dafny_error)
}
 fn EnableKinesisStreamingDestination(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::EnableKinesisStreamingDestinationInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::EnableKinesisStreamingDestinationOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::enable_kinesis_streaming_destination::_enable_kinesis_streaming_destination_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::enable_kinesis_streaming_destination::_enable_kinesis_streaming_destination_response::to_dafny,
    conversions::enable_kinesis_streaming_destination::to_dafny_error)
}
 fn ExecuteStatement(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExecuteStatementInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExecuteStatementOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::execute_statement::_execute_statement_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::execute_statement::_execute_statement_response::to_dafny,
    conversions::execute_statement::to_dafny_error)
}
 fn ExecuteTransaction(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExecuteTransactionInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExecuteTransactionOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::execute_transaction::_execute_transaction_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::execute_transaction::_execute_transaction_response::to_dafny,
    conversions::execute_transaction::to_dafny_error)
}
 fn ExportTableToPointInTime(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExportTableToPointInTimeInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ExportTableToPointInTimeOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::export_table_to_point_in_time::_export_table_to_point_in_time_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::export_table_to_point_in_time::_export_table_to_point_in_time_response::to_dafny,
    conversions::export_table_to_point_in_time::to_dafny_error)
}
 fn GetItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::GetItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::GetItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::get_item::_get_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::get_item::_get_item_response::to_dafny,
    conversions::get_item::to_dafny_error)
}
 fn ImportTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ImportTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ImportTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::import_table::_import_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::import_table::_import_table_response::to_dafny,
    conversions::import_table::to_dafny_error)
}
 fn ListBackups(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListBackupsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListBackupsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_backups::_list_backups_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_backups::_list_backups_response::to_dafny,
    conversions::list_backups::to_dafny_error)
}
 fn ListContributorInsights(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListContributorInsightsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListContributorInsightsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_contributor_insights::_list_contributor_insights_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_contributor_insights::_list_contributor_insights_response::to_dafny,
    conversions::list_contributor_insights::to_dafny_error)
}
 fn ListExports(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListExportsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListExportsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_exports::_list_exports_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_exports::_list_exports_response::to_dafny,
    conversions::list_exports::to_dafny_error)
}
 fn ListGlobalTables(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListGlobalTablesInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListGlobalTablesOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_global_tables::_list_global_tables_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_global_tables::_list_global_tables_response::to_dafny,
    conversions::list_global_tables::to_dafny_error)
}
 fn ListImports(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListImportsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListImportsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_imports::_list_imports_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_imports::_list_imports_response::to_dafny,
    conversions::list_imports::to_dafny_error)
}
 fn ListTables(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListTablesInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListTablesOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_tables::_list_tables_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_tables::_list_tables_response::to_dafny,
    conversions::list_tables::to_dafny_error)
}
 fn ListTagsOfResource(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListTagsOfResourceInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ListTagsOfResourceOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::list_tags_of_resource::_list_tags_of_resource_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::list_tags_of_resource::_list_tags_of_resource_response::to_dafny,
    conversions::list_tags_of_resource::to_dafny_error)
}
 fn PutItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::PutItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::PutItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::put_item::_put_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::put_item::_put_item_response::to_dafny,
    conversions::put_item::to_dafny_error)
}
 fn Query(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::QueryInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::QueryOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::query::_query_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::query::_query_response::to_dafny,
    conversions::query::to_dafny_error)
}
 fn RestoreTableFromBackup(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::RestoreTableFromBackupInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::RestoreTableFromBackupOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::restore_table_from_backup::_restore_table_from_backup_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::restore_table_from_backup::_restore_table_from_backup_response::to_dafny,
    conversions::restore_table_from_backup::to_dafny_error)
}
 fn RestoreTableToPointInTime(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::RestoreTableToPointInTimeInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::RestoreTableToPointInTimeOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::restore_table_to_point_in_time::_restore_table_to_point_in_time_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::restore_table_to_point_in_time::_restore_table_to_point_in_time_response::to_dafny,
    conversions::restore_table_to_point_in_time::to_dafny_error)
}
 fn Scan(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ScanInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::ScanOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::scan::_scan_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::scan::_scan_response::to_dafny,
    conversions::scan::to_dafny_error)
}
 fn TagResource(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::TagResourceInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::tag_resource::_tag_resource_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::tag_resource::_tag_resource_response::to_dafny,
    conversions::tag_resource::to_dafny_error)
}
 fn TransactGetItems(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::TransactGetItemsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::TransactGetItemsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::transact_get_items::_transact_get_items_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::transact_get_items::_transact_get_items_response::to_dafny,
    conversions::transact_get_items::to_dafny_error)
}
 fn TransactWriteItems(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::TransactWriteItemsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::TransactWriteItemsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::transact_write_items::_transact_write_items_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::transact_write_items::_transact_write_items_response::to_dafny,
    conversions::transact_write_items::to_dafny_error)
}
 fn UntagResource(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UntagResourceInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    (),
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::untag_resource::_untag_resource_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::untag_resource::_untag_resource_response::to_dafny,
    conversions::untag_resource::to_dafny_error)
}
 fn UpdateContinuousBackups(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateContinuousBackupsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateContinuousBackupsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_continuous_backups::_update_continuous_backups_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_continuous_backups::_update_continuous_backups_response::to_dafny,
    conversions::update_continuous_backups::to_dafny_error)
}
 fn UpdateContributorInsights(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateContributorInsightsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateContributorInsightsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_contributor_insights::_update_contributor_insights_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_contributor_insights::_update_contributor_insights_response::to_dafny,
    conversions::update_contributor_insights::to_dafny_error)
}
 fn UpdateGlobalTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateGlobalTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateGlobalTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_global_table::_update_global_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_global_table::_update_global_table_response::to_dafny,
    conversions::update_global_table::to_dafny_error)
}
 fn UpdateGlobalTableSettings(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateGlobalTableSettingsInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateGlobalTableSettingsOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_global_table_settings::_update_global_table_settings_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_global_table_settings::_update_global_table_settings_response::to_dafny,
    conversions::update_global_table_settings::to_dafny_error)
}
 fn UpdateItem(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateItemInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateItemOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_item::_update_item_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_item::_update_item_response::to_dafny,
    conversions::update_item::to_dafny_error)
}
 fn UpdateTable(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTableInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTableOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_table::_update_table_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_table::_update_table_response::to_dafny,
    conversions::update_table::to_dafny_error)
}
 fn UpdateTableReplicaAutoScaling(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTableReplicaAutoScalingInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTableReplicaAutoScalingOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_table_replica_auto_scaling::_update_table_replica_auto_scaling_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_table_replica_auto_scaling::_update_table_replica_auto_scaling_response::to_dafny,
    conversions::update_table_replica_auto_scaling::to_dafny_error)
}
 fn UpdateTimeToLive(&mut self, input: &std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTimeToLiveInput>)
  -> std::rc::Rc<crate::r#_Wrappers_Compile::Result<
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::UpdateTimeToLiveOutput>,
    std::rc::Rc<crate::r#software::amazon::cryptography::services::dynamodb::internaldafny::types::Error>
  >
> {
  let native_result =
    dafny_tokio_runtime.block_on(crate::deps::com_amazonaws_dynamodb::conversions::update_time_to_live::_update_time_to_live_request::from_dafny(input.clone(), self.inner.clone()).send());
  crate::standard_library_conversions::result_to_dafny(&native_result,
    conversions::update_time_to_live::_update_time_to_live_response::to_dafny,
    conversions::update_time_to_live::to_dafny_error)
} }
