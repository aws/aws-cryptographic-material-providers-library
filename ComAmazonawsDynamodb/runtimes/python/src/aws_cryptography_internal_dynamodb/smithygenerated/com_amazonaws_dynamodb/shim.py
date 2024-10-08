# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes import (
    BatchExecuteStatementInput_BatchExecuteStatementInput as DafnyBatchExecuteStatementInput,
    BatchExecuteStatementOutput_BatchExecuteStatementOutput as DafnyBatchExecuteStatementOutput,
    BatchGetItemInput_BatchGetItemInput as DafnyBatchGetItemInput,
    BatchGetItemOutput_BatchGetItemOutput as DafnyBatchGetItemOutput,
    BatchWriteItemInput_BatchWriteItemInput as DafnyBatchWriteItemInput,
    BatchWriteItemOutput_BatchWriteItemOutput as DafnyBatchWriteItemOutput,
    CreateBackupInput_CreateBackupInput as DafnyCreateBackupInput,
    CreateBackupOutput_CreateBackupOutput as DafnyCreateBackupOutput,
    CreateGlobalTableInput_CreateGlobalTableInput as DafnyCreateGlobalTableInput,
    CreateGlobalTableOutput_CreateGlobalTableOutput as DafnyCreateGlobalTableOutput,
    CreateTableInput_CreateTableInput as DafnyCreateTableInput,
    CreateTableOutput_CreateTableOutput as DafnyCreateTableOutput,
    DeleteBackupInput_DeleteBackupInput as DafnyDeleteBackupInput,
    DeleteBackupOutput_DeleteBackupOutput as DafnyDeleteBackupOutput,
    DeleteItemInput_DeleteItemInput as DafnyDeleteItemInput,
    DeleteItemOutput_DeleteItemOutput as DafnyDeleteItemOutput,
    DeleteTableInput_DeleteTableInput as DafnyDeleteTableInput,
    DeleteTableOutput_DeleteTableOutput as DafnyDeleteTableOutput,
    DescribeBackupInput_DescribeBackupInput as DafnyDescribeBackupInput,
    DescribeBackupOutput_DescribeBackupOutput as DafnyDescribeBackupOutput,
    DescribeContinuousBackupsInput_DescribeContinuousBackupsInput as DafnyDescribeContinuousBackupsInput,
    DescribeContinuousBackupsOutput_DescribeContinuousBackupsOutput as DafnyDescribeContinuousBackupsOutput,
    DescribeContributorInsightsInput_DescribeContributorInsightsInput as DafnyDescribeContributorInsightsInput,
    DescribeContributorInsightsOutput_DescribeContributorInsightsOutput as DafnyDescribeContributorInsightsOutput,
    DescribeEndpointsRequest_DescribeEndpointsRequest as DafnyDescribeEndpointsRequest,
    DescribeEndpointsResponse_DescribeEndpointsResponse as DafnyDescribeEndpointsResponse,
    DescribeExportInput_DescribeExportInput as DafnyDescribeExportInput,
    DescribeExportOutput_DescribeExportOutput as DafnyDescribeExportOutput,
    DescribeGlobalTableInput_DescribeGlobalTableInput as DafnyDescribeGlobalTableInput,
    DescribeGlobalTableOutput_DescribeGlobalTableOutput as DafnyDescribeGlobalTableOutput,
    DescribeGlobalTableSettingsInput_DescribeGlobalTableSettingsInput as DafnyDescribeGlobalTableSettingsInput,
    DescribeGlobalTableSettingsOutput_DescribeGlobalTableSettingsOutput as DafnyDescribeGlobalTableSettingsOutput,
    DescribeImportInput_DescribeImportInput as DafnyDescribeImportInput,
    DescribeImportOutput_DescribeImportOutput as DafnyDescribeImportOutput,
    DescribeKinesisStreamingDestinationInput_DescribeKinesisStreamingDestinationInput as DafnyDescribeKinesisStreamingDestinationInput,
    DescribeKinesisStreamingDestinationOutput_DescribeKinesisStreamingDestinationOutput as DafnyDescribeKinesisStreamingDestinationOutput,
    DescribeLimitsInput_DescribeLimitsInput as DafnyDescribeLimitsInput,
    DescribeLimitsOutput_DescribeLimitsOutput as DafnyDescribeLimitsOutput,
    DescribeTableInput_DescribeTableInput as DafnyDescribeTableInput,
    DescribeTableOutput_DescribeTableOutput as DafnyDescribeTableOutput,
    DescribeTableReplicaAutoScalingInput_DescribeTableReplicaAutoScalingInput as DafnyDescribeTableReplicaAutoScalingInput,
    DescribeTableReplicaAutoScalingOutput_DescribeTableReplicaAutoScalingOutput as DafnyDescribeTableReplicaAutoScalingOutput,
    DescribeTimeToLiveInput_DescribeTimeToLiveInput as DafnyDescribeTimeToLiveInput,
    DescribeTimeToLiveOutput_DescribeTimeToLiveOutput as DafnyDescribeTimeToLiveOutput,
    DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput as DafnyDisableKinesisStreamingDestinationInput,
    DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput as DafnyDisableKinesisStreamingDestinationOutput,
    EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput as DafnyEnableKinesisStreamingDestinationInput,
    EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput as DafnyEnableKinesisStreamingDestinationOutput,
    ExecuteStatementInput_ExecuteStatementInput as DafnyExecuteStatementInput,
    ExecuteStatementOutput_ExecuteStatementOutput as DafnyExecuteStatementOutput,
    ExecuteTransactionInput_ExecuteTransactionInput as DafnyExecuteTransactionInput,
    ExecuteTransactionOutput_ExecuteTransactionOutput as DafnyExecuteTransactionOutput,
    ExportTableToPointInTimeInput_ExportTableToPointInTimeInput as DafnyExportTableToPointInTimeInput,
    ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput as DafnyExportTableToPointInTimeOutput,
    GetItemInput_GetItemInput as DafnyGetItemInput,
    GetItemOutput_GetItemOutput as DafnyGetItemOutput,
    ImportTableInput_ImportTableInput as DafnyImportTableInput,
    ImportTableOutput_ImportTableOutput as DafnyImportTableOutput,
    ListBackupsInput_ListBackupsInput as DafnyListBackupsInput,
    ListBackupsOutput_ListBackupsOutput as DafnyListBackupsOutput,
    ListContributorInsightsInput_ListContributorInsightsInput as DafnyListContributorInsightsInput,
    ListContributorInsightsOutput_ListContributorInsightsOutput as DafnyListContributorInsightsOutput,
    ListExportsInput_ListExportsInput as DafnyListExportsInput,
    ListExportsOutput_ListExportsOutput as DafnyListExportsOutput,
    ListGlobalTablesInput_ListGlobalTablesInput as DafnyListGlobalTablesInput,
    ListGlobalTablesOutput_ListGlobalTablesOutput as DafnyListGlobalTablesOutput,
    ListImportsInput_ListImportsInput as DafnyListImportsInput,
    ListImportsOutput_ListImportsOutput as DafnyListImportsOutput,
    ListTablesInput_ListTablesInput as DafnyListTablesInput,
    ListTablesOutput_ListTablesOutput as DafnyListTablesOutput,
    ListTagsOfResourceInput_ListTagsOfResourceInput as DafnyListTagsOfResourceInput,
    ListTagsOfResourceOutput_ListTagsOfResourceOutput as DafnyListTagsOfResourceOutput,
    PutItemInput_PutItemInput as DafnyPutItemInput,
    PutItemOutput_PutItemOutput as DafnyPutItemOutput,
    QueryInput_QueryInput as DafnyQueryInput,
    QueryOutput_QueryOutput as DafnyQueryOutput,
    RestoreTableFromBackupInput_RestoreTableFromBackupInput as DafnyRestoreTableFromBackupInput,
    RestoreTableFromBackupOutput_RestoreTableFromBackupOutput as DafnyRestoreTableFromBackupOutput,
    RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput as DafnyRestoreTableToPointInTimeInput,
    RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput as DafnyRestoreTableToPointInTimeOutput,
    ScanInput_ScanInput as DafnyScanInput,
    ScanOutput_ScanOutput as DafnyScanOutput,
    TagResourceInput_TagResourceInput as DafnyTagResourceInput,
    TransactGetItemsInput_TransactGetItemsInput as DafnyTransactGetItemsInput,
    TransactGetItemsOutput_TransactGetItemsOutput as DafnyTransactGetItemsOutput,
    TransactWriteItemsInput_TransactWriteItemsInput as DafnyTransactWriteItemsInput,
    TransactWriteItemsOutput_TransactWriteItemsOutput as DafnyTransactWriteItemsOutput,
    UntagResourceInput_UntagResourceInput as DafnyUntagResourceInput,
    UpdateContinuousBackupsInput_UpdateContinuousBackupsInput as DafnyUpdateContinuousBackupsInput,
    UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput as DafnyUpdateContinuousBackupsOutput,
    UpdateContributorInsightsInput_UpdateContributorInsightsInput as DafnyUpdateContributorInsightsInput,
    UpdateContributorInsightsOutput_UpdateContributorInsightsOutput as DafnyUpdateContributorInsightsOutput,
    UpdateGlobalTableInput_UpdateGlobalTableInput as DafnyUpdateGlobalTableInput,
    UpdateGlobalTableOutput_UpdateGlobalTableOutput as DafnyUpdateGlobalTableOutput,
    UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput as DafnyUpdateGlobalTableSettingsInput,
    UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput as DafnyUpdateGlobalTableSettingsOutput,
    UpdateItemInput_UpdateItemInput as DafnyUpdateItemInput,
    UpdateItemOutput_UpdateItemOutput as DafnyUpdateItemOutput,
    UpdateTableInput_UpdateTableInput as DafnyUpdateTableInput,
    UpdateTableOutput_UpdateTableOutput as DafnyUpdateTableOutput,
    UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput as DafnyUpdateTableReplicaAutoScalingInput,
    UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput as DafnyUpdateTableReplicaAutoScalingOutput,
    UpdateTimeToLiveInput_UpdateTimeToLiveInput as DafnyUpdateTimeToLiveInput,
    UpdateTimeToLiveOutput_UpdateTimeToLiveOutput as DafnyUpdateTimeToLiveOutput,
)
import aws_cryptography_internal_dynamodb.internaldafny.generated.module_
import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny
import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk

from . import dafny_to_aws_sdk


import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
from botocore.exceptions import ClientError
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes


def _sdk_error_to_dafny_error(e: ClientError):
    """Converts the provided native Smithy-modelled error into the
    corresponding Dafny error."""
    if e.response["Error"]["Code"] == "BackupInUseException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "BackupNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ConditionalCheckFailedException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalCheckFailedException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ContinuousBackupsUnavailableException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContinuousBackupsUnavailableException(
            e.response
        )

    elif e.response["Error"]["Code"] == "DuplicateItemException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DuplicateItemException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ExportConflictException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportConflictException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ExportNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "GlobalTableAlreadyExistsException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableAlreadyExistsException(
            e.response
        )

    elif e.response["Error"]["Code"] == "GlobalTableNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "IdempotentParameterMismatchException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_IdempotentParameterMismatchException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ImportConflictException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportConflictException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ImportNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "IndexNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_IndexNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InternalServerError":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InternalServerError(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidEndpointException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InvalidEndpointException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidExportTimeException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InvalidExportTimeException(
            e.response
        )

    elif e.response["Error"]["Code"] == "InvalidRestoreTimeException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InvalidRestoreTimeException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ItemCollectionSizeLimitExceededException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionSizeLimitExceededException(
            e.response
        )

    elif e.response["Error"]["Code"] == "LimitExceededException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LimitExceededException(
            e.response
        )

    elif e.response["Error"]["Code"] == "PointInTimeRecoveryUnavailableException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PointInTimeRecoveryUnavailableException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ProvisionedThroughputExceededException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputExceededException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ReplicaAlreadyExistsException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaAlreadyExistsException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ReplicaNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "RequestLimitExceeded":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_RequestLimitExceeded(
            e.response
        )

    elif e.response["Error"]["Code"] == "ResourceInUseException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ResourceInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "ResourceNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ResourceNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TableAlreadyExistsException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableAlreadyExistsException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TableInUseException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableInUseException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TableNotFoundException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableNotFoundException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TransactionCanceledException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactionCanceledException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TransactionConflictException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactionConflictException(
            e.response
        )

    elif e.response["Error"]["Code"] == "TransactionInProgressException":
        return aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactionInProgressException(
            e.response
        )

    return aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes.Error_Opaque(
        obj=e,
        alt__text=_dafny.Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(*[iter(repr(e).encode("utf-16-be"))] * 2)
                ]
            )
        ),
    )


class DynamoDBClientShim:
    def __init__(self, _impl, _region):
        self._impl = _impl
        self._region = _region

    def BatchExecuteStatement(
        self, input: DafnyBatchExecuteStatementInput
    ) -> DafnyBatchExecuteStatementOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchExecuteStatementInput(
            input
        )
        try:
            boto_response_dict = self._impl.batch_execute_statement(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchExecuteStatementOutput(
                boto_response_dict
            )
        )

    def BatchGetItem(self, input: DafnyBatchGetItemInput) -> DafnyBatchGetItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchGetItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.batch_get_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchGetItemOutput(
                boto_response_dict
            )
        )

    def BatchWriteItem(
        self, input: DafnyBatchWriteItemInput
    ) -> DafnyBatchWriteItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchWriteItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.batch_write_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchWriteItemOutput(
                boto_response_dict
            )
        )

    def CreateBackup(self, input: DafnyCreateBackupInput) -> DafnyCreateBackupOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateBackupInput(
            input
        )
        try:
            boto_response_dict = self._impl.create_backup(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateBackupOutput(
                boto_response_dict
            )
        )

    def CreateGlobalTable(
        self, input: DafnyCreateGlobalTableInput
    ) -> DafnyCreateGlobalTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateGlobalTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.create_global_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateGlobalTableOutput(
                boto_response_dict
            )
        )

    def CreateTable(self, input: DafnyCreateTableInput) -> DafnyCreateTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.create_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateTableOutput(
                boto_response_dict
            )
        )

    def DeleteBackup(self, input: DafnyDeleteBackupInput) -> DafnyDeleteBackupOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteBackupInput(
            input
        )
        try:
            boto_response_dict = self._impl.delete_backup(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteBackupOutput(
                boto_response_dict
            )
        )

    def DeleteItem(self, input: DafnyDeleteItemInput) -> DafnyDeleteItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.delete_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteItemOutput(
                boto_response_dict
            )
        )

    def DeleteTable(self, input: DafnyDeleteTableInput) -> DafnyDeleteTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.delete_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteTableOutput(
                boto_response_dict
            )
        )

    def DescribeBackup(
        self, input: DafnyDescribeBackupInput
    ) -> DafnyDescribeBackupOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeBackupInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_backup(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeBackupOutput(
                boto_response_dict
            )
        )

    def DescribeContinuousBackups(
        self, input: DafnyDescribeContinuousBackupsInput
    ) -> DafnyDescribeContinuousBackupsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeContinuousBackupsInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_continuous_backups(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeContinuousBackupsOutput(
                boto_response_dict
            )
        )

    def DescribeContributorInsights(
        self, input: DafnyDescribeContributorInsightsInput
    ) -> DafnyDescribeContributorInsightsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeContributorInsightsInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_contributor_insights(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeContributorInsightsOutput(
                boto_response_dict
            )
        )

    def DescribeEndpoints(
        self, input: DafnyDescribeEndpointsRequest
    ) -> DafnyDescribeEndpointsResponse:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeEndpointsRequest(
            input
        )
        try:
            boto_response_dict = self._impl.describe_endpoints(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeEndpointsResponse(
                boto_response_dict
            )
        )

    def DescribeExport(
        self, input: DafnyDescribeExportInput
    ) -> DafnyDescribeExportOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeExportInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_export(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeExportOutput(
                boto_response_dict
            )
        )

    def DescribeGlobalTable(
        self, input: DafnyDescribeGlobalTableInput
    ) -> DafnyDescribeGlobalTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeGlobalTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_global_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeGlobalTableOutput(
                boto_response_dict
            )
        )

    def DescribeGlobalTableSettings(
        self, input: DafnyDescribeGlobalTableSettingsInput
    ) -> DafnyDescribeGlobalTableSettingsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeGlobalTableSettingsInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_global_table_settings(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeGlobalTableSettingsOutput(
                boto_response_dict
            )
        )

    def DescribeImport(
        self, input: DafnyDescribeImportInput
    ) -> DafnyDescribeImportOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeImportInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_import(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeImportOutput(
                boto_response_dict
            )
        )

    def DescribeKinesisStreamingDestination(
        self, input: DafnyDescribeKinesisStreamingDestinationInput
    ) -> DafnyDescribeKinesisStreamingDestinationOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_kinesis_streaming_destination(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationOutput(
                boto_response_dict
            )
        )

    def DescribeLimits(
        self, input: DafnyDescribeLimitsInput
    ) -> DafnyDescribeLimitsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeLimitsInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_limits(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeLimitsOutput(
                boto_response_dict
            )
        )

    def DescribeTable(self, input: DafnyDescribeTableInput) -> DafnyDescribeTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeTableOutput(
                boto_response_dict
            )
        )

    def DescribeTableReplicaAutoScaling(
        self, input: DafnyDescribeTableReplicaAutoScalingInput
    ) -> DafnyDescribeTableReplicaAutoScalingOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_table_replica_auto_scaling(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingOutput(
                boto_response_dict
            )
        )

    def DescribeTimeToLive(
        self, input: DafnyDescribeTimeToLiveInput
    ) -> DafnyDescribeTimeToLiveOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DescribeTimeToLiveInput(
            input
        )
        try:
            boto_response_dict = self._impl.describe_time_to_live(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DescribeTimeToLiveOutput(
                boto_response_dict
            )
        )

    def DisableKinesisStreamingDestination(
        self, input: DafnyDisableKinesisStreamingDestinationInput
    ) -> DafnyDisableKinesisStreamingDestinationOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DisableKinesisStreamingDestinationInput(
            input
        )
        try:
            boto_response_dict = self._impl.disable_kinesis_streaming_destination(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DisableKinesisStreamingDestinationOutput(
                boto_response_dict
            )
        )

    def EnableKinesisStreamingDestination(
        self, input: DafnyEnableKinesisStreamingDestinationInput
    ) -> DafnyEnableKinesisStreamingDestinationOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_EnableKinesisStreamingDestinationInput(
            input
        )
        try:
            boto_response_dict = self._impl.enable_kinesis_streaming_destination(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_EnableKinesisStreamingDestinationOutput(
                boto_response_dict
            )
        )

    def ExecuteStatement(
        self, input: DafnyExecuteStatementInput
    ) -> DafnyExecuteStatementOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExecuteStatementInput(
            input
        )
        try:
            boto_response_dict = self._impl.execute_statement(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExecuteStatementOutput(
                boto_response_dict
            )
        )

    def ExecuteTransaction(
        self, input: DafnyExecuteTransactionInput
    ) -> DafnyExecuteTransactionOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExecuteTransactionInput(
            input
        )
        try:
            boto_response_dict = self._impl.execute_transaction(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExecuteTransactionOutput(
                boto_response_dict
            )
        )

    def ExportTableToPointInTime(
        self, input: DafnyExportTableToPointInTimeInput
    ) -> DafnyExportTableToPointInTimeOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportTableToPointInTimeInput(
            input
        )
        try:
            boto_response_dict = self._impl.export_table_to_point_in_time(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportTableToPointInTimeOutput(
                boto_response_dict
            )
        )

    def GetItem(self, input: DafnyGetItemInput) -> DafnyGetItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GetItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.get_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GetItemOutput(
                boto_response_dict
            )
        )

    def ImportTable(self, input: DafnyImportTableInput) -> DafnyImportTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.import_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportTableOutput(
                boto_response_dict
            )
        )

    def ListBackups(self, input: DafnyListBackupsInput) -> DafnyListBackupsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListBackupsInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_backups(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListBackupsOutput(
                boto_response_dict
            )
        )

    def ListContributorInsights(
        self, input: DafnyListContributorInsightsInput
    ) -> DafnyListContributorInsightsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListContributorInsightsInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_contributor_insights(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListContributorInsightsOutput(
                boto_response_dict
            )
        )

    def ListExports(self, input: DafnyListExportsInput) -> DafnyListExportsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListExportsInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_exports(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListExportsOutput(
                boto_response_dict
            )
        )

    def ListGlobalTables(
        self, input: DafnyListGlobalTablesInput
    ) -> DafnyListGlobalTablesOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListGlobalTablesInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_global_tables(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListGlobalTablesOutput(
                boto_response_dict
            )
        )

    def ListImports(self, input: DafnyListImportsInput) -> DafnyListImportsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListImportsInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_imports(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListImportsOutput(
                boto_response_dict
            )
        )

    def ListTables(self, input: DafnyListTablesInput) -> DafnyListTablesOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListTablesInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_tables(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListTablesOutput(
                boto_response_dict
            )
        )

    def ListTagsOfResource(
        self, input: DafnyListTagsOfResourceInput
    ) -> DafnyListTagsOfResourceOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ListTagsOfResourceInput(
            input
        )
        try:
            boto_response_dict = self._impl.list_tags_of_resource(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ListTagsOfResourceOutput(
                boto_response_dict
            )
        )

    def PutItem(self, input: DafnyPutItemInput) -> DafnyPutItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_PutItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.put_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PutItemOutput(
                boto_response_dict
            )
        )

    def Query(self, input: DafnyQueryInput) -> DafnyQueryOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_QueryInput(
            input
        )
        try:
            boto_response_dict = self._impl.query(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_QueryOutput(
                boto_response_dict
            )
        )

    def RestoreTableFromBackup(
        self, input: DafnyRestoreTableFromBackupInput
    ) -> DafnyRestoreTableFromBackupOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_RestoreTableFromBackupInput(
            input
        )
        try:
            boto_response_dict = self._impl.restore_table_from_backup(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_RestoreTableFromBackupOutput(
                boto_response_dict
            )
        )

    def RestoreTableToPointInTime(
        self, input: DafnyRestoreTableToPointInTimeInput
    ) -> DafnyRestoreTableToPointInTimeOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_RestoreTableToPointInTimeInput(
            input
        )
        try:
            boto_response_dict = self._impl.restore_table_to_point_in_time(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_RestoreTableToPointInTimeOutput(
                boto_response_dict
            )
        )

    def Scan(self, input: DafnyScanInput) -> DafnyScanOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ScanInput(
            input
        )
        try:
            boto_response_dict = self._impl.scan(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ScanOutput(
                boto_response_dict
            )
        )

    def TagResource(self, input: DafnyTagResourceInput) -> None:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TagResourceInput(
            input
        )
        try:
            boto_response_dict = self._impl.tag_resource(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def TransactGetItems(
        self, input: DafnyTransactGetItemsInput
    ) -> DafnyTransactGetItemsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TransactGetItemsInput(
            input
        )
        try:
            boto_response_dict = self._impl.transact_get_items(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactGetItemsOutput(
                boto_response_dict
            )
        )

    def TransactWriteItems(
        self, input: DafnyTransactWriteItemsInput
    ) -> DafnyTransactWriteItemsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TransactWriteItemsInput(
            input
        )
        try:
            boto_response_dict = self._impl.transact_write_items(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactWriteItemsOutput(
                boto_response_dict
            )
        )

    def UntagResource(self, input: DafnyUntagResourceInput) -> None:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UntagResourceInput(
            input
        )
        try:
            boto_response_dict = self._impl.untag_resource(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def UpdateContinuousBackups(
        self, input: DafnyUpdateContinuousBackupsInput
    ) -> DafnyUpdateContinuousBackupsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateContinuousBackupsInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_continuous_backups(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateContinuousBackupsOutput(
                boto_response_dict
            )
        )

    def UpdateContributorInsights(
        self, input: DafnyUpdateContributorInsightsInput
    ) -> DafnyUpdateContributorInsightsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateContributorInsightsInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_contributor_insights(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateContributorInsightsOutput(
                boto_response_dict
            )
        )

    def UpdateGlobalTable(
        self, input: DafnyUpdateGlobalTableInput
    ) -> DafnyUpdateGlobalTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateGlobalTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_global_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateGlobalTableOutput(
                boto_response_dict
            )
        )

    def UpdateGlobalTableSettings(
        self, input: DafnyUpdateGlobalTableSettingsInput
    ) -> DafnyUpdateGlobalTableSettingsOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateGlobalTableSettingsInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_global_table_settings(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateGlobalTableSettingsOutput(
                boto_response_dict
            )
        )

    def UpdateItem(self, input: DafnyUpdateItemInput) -> DafnyUpdateItemOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateItemInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_item(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateItemOutput(
                boto_response_dict
            )
        )

    def UpdateTable(self, input: DafnyUpdateTableInput) -> DafnyUpdateTableOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateTableInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_table(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateTableOutput(
                boto_response_dict
            )
        )

    def UpdateTableReplicaAutoScaling(
        self, input: DafnyUpdateTableReplicaAutoScalingInput
    ) -> DafnyUpdateTableReplicaAutoScalingOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_table_replica_auto_scaling(
                **boto_request_dict
            )
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingOutput(
                boto_response_dict
            )
        )

    def UpdateTimeToLive(
        self, input: DafnyUpdateTimeToLiveInput
    ) -> DafnyUpdateTimeToLiveOutput:
        boto_request_dict = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateTimeToLiveInput(
            input
        )
        try:
            boto_response_dict = self._impl.update_time_to_live(**boto_request_dict)
        except ClientError as e:
            return Wrappers.Result_Failure(_sdk_error_to_dafny_error(e))

        return Wrappers.Result_Success(
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateTimeToLiveOutput(
                boto_response_dict
            )
        )
