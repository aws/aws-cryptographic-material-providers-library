# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter


class InternalBoto3DynamoDBFormatConverter:
    def __init__(self, item_handler, condition_handler):
        self._item_handler = item_handler
        self._condition_handler = condition_handler

    def BatchExecuteStatementInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchExecuteStatementInput(
            boto3_input, item_handler, condition_handler
        )

    def BatchExecuteStatementOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchExecuteStatementOutput(
            boto3_input, item_handler, condition_handler
        )

    def BatchGetItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchGetItemInput(
            boto3_input, item_handler, condition_handler
        )

    def BatchGetItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchGetItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def BatchWriteItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchWriteItemInput(
            boto3_input, item_handler, condition_handler
        )

    def BatchWriteItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchWriteItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def CreateBackupInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateBackupInput(
            boto3_input, item_handler, condition_handler
        )

    def CreateBackupOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateBackupOutput(
            boto3_input, item_handler, condition_handler
        )

    def CreateGlobalTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateGlobalTableInput(
            boto3_input, item_handler, condition_handler
        )

    def CreateGlobalTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateGlobalTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def CreateTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateTableInput(
            boto3_input, item_handler, condition_handler
        )

    def CreateTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteBackupInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteBackupInput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteBackupOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteBackupOutput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteItemInput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteResourcePolicyInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteResourcePolicyInput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteResourcePolicyOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteResourcePolicyOutput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteTableInput(
            boto3_input, item_handler, condition_handler
        )

    def DeleteTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeBackupInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeBackupInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeBackupOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeBackupOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeContinuousBackupsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeContinuousBackupsInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeContinuousBackupsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeContinuousBackupsOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeContributorInsightsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeContributorInsightsInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeContributorInsightsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeContributorInsightsOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeEndpointsRequest(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeEndpointsRequest(
            boto3_input, item_handler, condition_handler
        )

    def DescribeEndpointsResponse(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeEndpointsResponse(
            boto3_input, item_handler, condition_handler
        )

    def DescribeExportInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeExportInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeExportOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeExportOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeGlobalTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeGlobalTableInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeGlobalTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeGlobalTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeGlobalTableSettingsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeGlobalTableSettingsInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeGlobalTableSettingsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeGlobalTableSettingsOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeImportInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeImportInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeImportOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeImportOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeKinesisStreamingDestinationInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeKinesisStreamingDestinationOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeLimitsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeLimitsInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeLimitsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeLimitsOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTableInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTableReplicaAutoScalingInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTableReplicaAutoScalingOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingOutput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTimeToLiveInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTimeToLiveInput(
            boto3_input, item_handler, condition_handler
        )

    def DescribeTimeToLiveOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DescribeTimeToLiveOutput(
            boto3_input, item_handler, condition_handler
        )

    def DisableKinesisStreamingDestinationInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DisableKinesisStreamingDestinationInput(
            boto3_input, item_handler, condition_handler
        )

    def DisableKinesisStreamingDestinationOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DisableKinesisStreamingDestinationOutput(
            boto3_input, item_handler, condition_handler
        )

    def EnableKinesisStreamingDestinationInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingDestinationInput(
            boto3_input, item_handler, condition_handler
        )

    def EnableKinesisStreamingDestinationOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingDestinationOutput(
            boto3_input, item_handler, condition_handler
        )

    def ExecuteStatementInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExecuteStatementInput(
            boto3_input, item_handler, condition_handler
        )

    def ExecuteStatementOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExecuteStatementOutput(
            boto3_input, item_handler, condition_handler
        )

    def ExecuteTransactionInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExecuteTransactionInput(
            boto3_input, item_handler, condition_handler
        )

    def ExecuteTransactionOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExecuteTransactionOutput(
            boto3_input, item_handler, condition_handler
        )

    def ExportTableToPointInTimeInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportTableToPointInTimeInput(
            boto3_input, item_handler, condition_handler
        )

    def ExportTableToPointInTimeOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportTableToPointInTimeOutput(
            boto3_input, item_handler, condition_handler
        )

    def GetItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GetItemInput(
            boto3_input, item_handler, condition_handler
        )

    def GetItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GetItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def GetResourcePolicyInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GetResourcePolicyInput(
            boto3_input, item_handler, condition_handler
        )

    def GetResourcePolicyOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GetResourcePolicyOutput(
            boto3_input, item_handler, condition_handler
        )

    def ImportTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportTableInput(
            boto3_input, item_handler, condition_handler
        )

    def ImportTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListBackupsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListBackupsInput(
            boto3_input, item_handler, condition_handler
        )

    def ListBackupsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListBackupsOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListContributorInsightsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListContributorInsightsInput(
            boto3_input, item_handler, condition_handler
        )

    def ListContributorInsightsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListContributorInsightsOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListExportsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListExportsInput(
            boto3_input, item_handler, condition_handler
        )

    def ListExportsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListExportsOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListGlobalTablesInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListGlobalTablesInput(
            boto3_input, item_handler, condition_handler
        )

    def ListGlobalTablesOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListGlobalTablesOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListImportsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListImportsInput(
            boto3_input, item_handler, condition_handler
        )

    def ListImportsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListImportsOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListTablesInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListTablesInput(
            boto3_input, item_handler, condition_handler
        )

    def ListTablesOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListTablesOutput(
            boto3_input, item_handler, condition_handler
        )

    def ListTagsOfResourceInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListTagsOfResourceInput(
            boto3_input, item_handler, condition_handler
        )

    def ListTagsOfResourceOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ListTagsOfResourceOutput(
            boto3_input, item_handler, condition_handler
        )

    def PutItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PutItemInput(
            boto3_input, item_handler, condition_handler
        )

    def PutItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PutItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def PutResourcePolicyInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PutResourcePolicyInput(
            boto3_input, item_handler, condition_handler
        )

    def PutResourcePolicyOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PutResourcePolicyOutput(
            boto3_input, item_handler, condition_handler
        )

    def QueryInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_QueryInput(
            boto3_input, item_handler, condition_handler
        )

    def QueryOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_QueryOutput(
            boto3_input, item_handler, condition_handler
        )

    def RestoreTableFromBackupInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_RestoreTableFromBackupInput(
            boto3_input, item_handler, condition_handler
        )

    def RestoreTableFromBackupOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_RestoreTableFromBackupOutput(
            boto3_input, item_handler, condition_handler
        )

    def RestoreTableToPointInTimeInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_RestoreTableToPointInTimeInput(
            boto3_input, item_handler, condition_handler
        )

    def RestoreTableToPointInTimeOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_RestoreTableToPointInTimeOutput(
            boto3_input, item_handler, condition_handler
        )

    def ScanInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ScanInput(
            boto3_input, item_handler, condition_handler
        )

    def ScanOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ScanOutput(
            boto3_input, item_handler, condition_handler
        )

    def TagResourceInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TagResourceInput(
            boto3_input, item_handler, condition_handler
        )

    def Unit(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return None

    def TransactGetItemsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactGetItemsInput(
            boto3_input, item_handler, condition_handler
        )

    def TransactGetItemsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactGetItemsOutput(
            boto3_input, item_handler, condition_handler
        )

    def TransactWriteItemsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactWriteItemsInput(
            boto3_input, item_handler, condition_handler
        )

    def TransactWriteItemsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactWriteItemsOutput(
            boto3_input, item_handler, condition_handler
        )

    def UntagResourceInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UntagResourceInput(
            boto3_input, item_handler, condition_handler
        )

    def Unit(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return None

    def UpdateContinuousBackupsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateContinuousBackupsInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateContinuousBackupsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateContinuousBackupsOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateContributorInsightsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateContributorInsightsInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateContributorInsightsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateContributorInsightsOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateGlobalTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateGlobalTableInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateGlobalTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateGlobalTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateGlobalTableSettingsInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateGlobalTableSettingsInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateGlobalTableSettingsOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateGlobalTableSettingsOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateItemInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateItemInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateItemOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateItemOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateKinesisStreamingDestinationInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateKinesisStreamingDestinationInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateKinesisStreamingDestinationOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateKinesisStreamingDestinationOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTableInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTableInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTableOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTableOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTableReplicaAutoScalingInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTableReplicaAutoScalingOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingOutput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTimeToLiveInput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTimeToLiveInput(
            boto3_input, item_handler, condition_handler
        )

    def UpdateTimeToLiveOutput(self, boto3_input) -> dict:
        original_request = boto3_input
        item_handler = self._item_handler
        condition_handler = self._condition_handler
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateTimeToLiveOutput(
            boto3_input, item_handler, condition_handler
        )
