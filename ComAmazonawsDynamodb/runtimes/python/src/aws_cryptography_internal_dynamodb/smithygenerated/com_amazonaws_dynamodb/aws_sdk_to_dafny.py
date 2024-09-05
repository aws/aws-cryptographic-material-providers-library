# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import _dafny
from _dafny import Map, Seq
from aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes import (
    ArchivalSummary_ArchivalSummary as DafnyArchivalSummary,
    AttributeAction_ADD,
    AttributeAction_DELETE,
    AttributeAction_PUT,
    AttributeDefinition_AttributeDefinition as DafnyAttributeDefinition,
    AttributeValueUpdate_AttributeValueUpdate as DafnyAttributeValueUpdate,
    AttributeValue_B,
    AttributeValue_BOOL,
    AttributeValue_BS,
    AttributeValue_L,
    AttributeValue_M,
    AttributeValue_N,
    AttributeValue_NS,
    AttributeValue_NULL,
    AttributeValue_S,
    AttributeValue_SS,
    AutoScalingPolicyDescription_AutoScalingPolicyDescription as DafnyAutoScalingPolicyDescription,
    AutoScalingPolicyUpdate_AutoScalingPolicyUpdate as DafnyAutoScalingPolicyUpdate,
    AutoScalingSettingsDescription_AutoScalingSettingsDescription as DafnyAutoScalingSettingsDescription,
    AutoScalingSettingsUpdate_AutoScalingSettingsUpdate as DafnyAutoScalingSettingsUpdate,
    AutoScalingTargetTrackingScalingPolicyConfigurationDescription_AutoScalingTargetTrackingScalingPolicyConfigurationDescription as DafnyAutoScalingTargetTrackingScalingPolicyConfigurationDescription,
    AutoScalingTargetTrackingScalingPolicyConfigurationUpdate_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate as DafnyAutoScalingTargetTrackingScalingPolicyConfigurationUpdate,
    BackupDescription_BackupDescription as DafnyBackupDescription,
    BackupDetails_BackupDetails as DafnyBackupDetails,
    BackupStatus_AVAILABLE,
    BackupStatus_CREATING,
    BackupStatus_DELETED,
    BackupSummary_BackupSummary as DafnyBackupSummary,
    BackupTypeFilter_ALL,
    BackupTypeFilter_AWS__BACKUP,
    BackupTypeFilter_SYSTEM,
    BackupTypeFilter_USER,
    BackupType_AWS__BACKUP,
    BackupType_SYSTEM,
    BackupType_USER,
    BatchExecuteStatementInput_BatchExecuteStatementInput as DafnyBatchExecuteStatementInput,
    BatchExecuteStatementOutput_BatchExecuteStatementOutput as DafnyBatchExecuteStatementOutput,
    BatchGetItemInput_BatchGetItemInput as DafnyBatchGetItemInput,
    BatchGetItemOutput_BatchGetItemOutput as DafnyBatchGetItemOutput,
    BatchStatementErrorCodeEnum_AccessDenied,
    BatchStatementErrorCodeEnum_ConditionalCheckFailed,
    BatchStatementErrorCodeEnum_DuplicateItem,
    BatchStatementErrorCodeEnum_InternalServerError,
    BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded,
    BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded,
    BatchStatementErrorCodeEnum_RequestLimitExceeded,
    BatchStatementErrorCodeEnum_ResourceNotFound,
    BatchStatementErrorCodeEnum_ThrottlingError,
    BatchStatementErrorCodeEnum_TransactionConflict,
    BatchStatementErrorCodeEnum_ValidationError,
    BatchStatementError_BatchStatementError as DafnyBatchStatementError,
    BatchStatementRequest_BatchStatementRequest as DafnyBatchStatementRequest,
    BatchStatementResponse_BatchStatementResponse as DafnyBatchStatementResponse,
    BatchWriteItemInput_BatchWriteItemInput as DafnyBatchWriteItemInput,
    BatchWriteItemOutput_BatchWriteItemOutput as DafnyBatchWriteItemOutput,
    BillingModeSummary_BillingModeSummary as DafnyBillingModeSummary,
    BillingMode_PAY__PER__REQUEST,
    BillingMode_PROVISIONED,
    CancellationReason_CancellationReason as DafnyCancellationReason,
    Capacity_Capacity as DafnyCapacity,
    ComparisonOperator_BEGINS__WITH,
    ComparisonOperator_BETWEEN,
    ComparisonOperator_CONTAINS,
    ComparisonOperator_EQ,
    ComparisonOperator_GE,
    ComparisonOperator_GT,
    ComparisonOperator_IN,
    ComparisonOperator_LE,
    ComparisonOperator_LT,
    ComparisonOperator_NE,
    ComparisonOperator_NOT__CONTAINS,
    ComparisonOperator_NOT__NULL,
    ComparisonOperator_NULL,
    ConditionCheck_ConditionCheck as DafnyConditionCheck,
    Condition_Condition as DafnyCondition,
    ConditionalOperator_AND,
    ConditionalOperator_OR,
    ConsumedCapacity_ConsumedCapacity as DafnyConsumedCapacity,
    ContinuousBackupsDescription_ContinuousBackupsDescription as DafnyContinuousBackupsDescription,
    ContinuousBackupsStatus_DISABLED,
    ContinuousBackupsStatus_ENABLED,
    ContributorInsightsAction_DISABLE,
    ContributorInsightsAction_ENABLE,
    ContributorInsightsStatus_DISABLED,
    ContributorInsightsStatus_DISABLING,
    ContributorInsightsStatus_ENABLED,
    ContributorInsightsStatus_ENABLING,
    ContributorInsightsStatus_FAILED,
    ContributorInsightsSummary_ContributorInsightsSummary as DafnyContributorInsightsSummary,
    CreateBackupInput_CreateBackupInput as DafnyCreateBackupInput,
    CreateBackupOutput_CreateBackupOutput as DafnyCreateBackupOutput,
    CreateGlobalSecondaryIndexAction_CreateGlobalSecondaryIndexAction as DafnyCreateGlobalSecondaryIndexAction,
    CreateGlobalTableInput_CreateGlobalTableInput as DafnyCreateGlobalTableInput,
    CreateGlobalTableOutput_CreateGlobalTableOutput as DafnyCreateGlobalTableOutput,
    CreateReplicaAction_CreateReplicaAction as DafnyCreateReplicaAction,
    CreateReplicationGroupMemberAction_CreateReplicationGroupMemberAction as DafnyCreateReplicationGroupMemberAction,
    CreateTableInput_CreateTableInput as DafnyCreateTableInput,
    CreateTableOutput_CreateTableOutput as DafnyCreateTableOutput,
    CsvOptions_CsvOptions as DafnyCsvOptions,
    DeleteBackupInput_DeleteBackupInput as DafnyDeleteBackupInput,
    DeleteBackupOutput_DeleteBackupOutput as DafnyDeleteBackupOutput,
    DeleteGlobalSecondaryIndexAction_DeleteGlobalSecondaryIndexAction as DafnyDeleteGlobalSecondaryIndexAction,
    DeleteItemInput_DeleteItemInput as DafnyDeleteItemInput,
    DeleteItemOutput_DeleteItemOutput as DafnyDeleteItemOutput,
    DeleteReplicaAction_DeleteReplicaAction as DafnyDeleteReplicaAction,
    DeleteReplicationGroupMemberAction_DeleteReplicationGroupMemberAction as DafnyDeleteReplicationGroupMemberAction,
    DeleteRequest_DeleteRequest as DafnyDeleteRequest,
    DeleteTableInput_DeleteTableInput as DafnyDeleteTableInput,
    DeleteTableOutput_DeleteTableOutput as DafnyDeleteTableOutput,
    Delete_Delete as DafnyDelete,
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
    DestinationStatus_ACTIVE,
    DestinationStatus_DISABLED,
    DestinationStatus_DISABLING,
    DestinationStatus_ENABLE__FAILED,
    DestinationStatus_ENABLING,
    DisableKinesisStreamingDestinationInput_DisableKinesisStreamingDestinationInput as DafnyDisableKinesisStreamingDestinationInput,
    DisableKinesisStreamingDestinationOutput_DisableKinesisStreamingDestinationOutput as DafnyDisableKinesisStreamingDestinationOutput,
    EnableKinesisStreamingDestinationInput_EnableKinesisStreamingDestinationInput as DafnyEnableKinesisStreamingDestinationInput,
    EnableKinesisStreamingDestinationOutput_EnableKinesisStreamingDestinationOutput as DafnyEnableKinesisStreamingDestinationOutput,
    Endpoint_Endpoint as DafnyEndpoint,
    Error_BackupInUseException,
    Error_BackupNotFoundException,
    Error_ConditionalCheckFailedException,
    Error_ContinuousBackupsUnavailableException,
    Error_DuplicateItemException,
    Error_ExportConflictException,
    Error_ExportNotFoundException,
    Error_GlobalTableAlreadyExistsException,
    Error_GlobalTableNotFoundException,
    Error_IdempotentParameterMismatchException,
    Error_ImportConflictException,
    Error_ImportNotFoundException,
    Error_IndexNotFoundException,
    Error_InternalServerError,
    Error_InvalidEndpointException,
    Error_InvalidExportTimeException,
    Error_InvalidRestoreTimeException,
    Error_ItemCollectionSizeLimitExceededException,
    Error_LimitExceededException,
    Error_PointInTimeRecoveryUnavailableException,
    Error_ProvisionedThroughputExceededException,
    Error_ReplicaAlreadyExistsException,
    Error_ReplicaNotFoundException,
    Error_RequestLimitExceeded,
    Error_ResourceInUseException,
    Error_ResourceNotFoundException,
    Error_TableAlreadyExistsException,
    Error_TableInUseException,
    Error_TableNotFoundException,
    Error_TransactionCanceledException,
    Error_TransactionConflictException,
    Error_TransactionInProgressException,
    ExecuteStatementInput_ExecuteStatementInput as DafnyExecuteStatementInput,
    ExecuteStatementOutput_ExecuteStatementOutput as DafnyExecuteStatementOutput,
    ExecuteTransactionInput_ExecuteTransactionInput as DafnyExecuteTransactionInput,
    ExecuteTransactionOutput_ExecuteTransactionOutput as DafnyExecuteTransactionOutput,
    ExpectedAttributeValue_ExpectedAttributeValue as DafnyExpectedAttributeValue,
    ExportDescription_ExportDescription as DafnyExportDescription,
    ExportFormat_DYNAMODB__JSON,
    ExportFormat_ION,
    ExportStatus_COMPLETED,
    ExportStatus_FAILED,
    ExportStatus_IN__PROGRESS,
    ExportSummary_ExportSummary as DafnyExportSummary,
    ExportTableToPointInTimeInput_ExportTableToPointInTimeInput as DafnyExportTableToPointInTimeInput,
    ExportTableToPointInTimeOutput_ExportTableToPointInTimeOutput as DafnyExportTableToPointInTimeOutput,
    FailureException_FailureException as DafnyFailureException,
    GetItemInput_GetItemInput as DafnyGetItemInput,
    GetItemOutput_GetItemOutput as DafnyGetItemOutput,
    Get_Get as DafnyGet,
    GlobalSecondaryIndexAutoScalingUpdate_GlobalSecondaryIndexAutoScalingUpdate as DafnyGlobalSecondaryIndexAutoScalingUpdate,
    GlobalSecondaryIndexDescription_GlobalSecondaryIndexDescription as DafnyGlobalSecondaryIndexDescription,
    GlobalSecondaryIndexInfo_GlobalSecondaryIndexInfo as DafnyGlobalSecondaryIndexInfo,
    GlobalSecondaryIndexUpdate_GlobalSecondaryIndexUpdate as DafnyGlobalSecondaryIndexUpdate,
    GlobalSecondaryIndex_GlobalSecondaryIndex as DafnyGlobalSecondaryIndex,
    GlobalTableDescription_GlobalTableDescription as DafnyGlobalTableDescription,
    GlobalTableGlobalSecondaryIndexSettingsUpdate_GlobalTableGlobalSecondaryIndexSettingsUpdate as DafnyGlobalTableGlobalSecondaryIndexSettingsUpdate,
    GlobalTableStatus_ACTIVE,
    GlobalTableStatus_CREATING,
    GlobalTableStatus_DELETING,
    GlobalTableStatus_UPDATING,
    GlobalTable_GlobalTable as DafnyGlobalTable,
    ImportStatus_CANCELLED,
    ImportStatus_CANCELLING,
    ImportStatus_COMPLETED,
    ImportStatus_FAILED,
    ImportStatus_IN__PROGRESS,
    ImportSummary_ImportSummary as DafnyImportSummary,
    ImportTableDescription_ImportTableDescription as DafnyImportTableDescription,
    ImportTableInput_ImportTableInput as DafnyImportTableInput,
    ImportTableOutput_ImportTableOutput as DafnyImportTableOutput,
    IndexStatus_ACTIVE,
    IndexStatus_CREATING,
    IndexStatus_DELETING,
    IndexStatus_UPDATING,
    InputCompressionType_GZIP,
    InputCompressionType_NONE,
    InputCompressionType_ZSTD,
    InputFormatOptions_InputFormatOptions as DafnyInputFormatOptions,
    InputFormat_CSV,
    InputFormat_DYNAMODB__JSON,
    InputFormat_ION,
    ItemCollectionMetrics_ItemCollectionMetrics as DafnyItemCollectionMetrics,
    ItemResponse_ItemResponse as DafnyItemResponse,
    KeySchemaElement_KeySchemaElement as DafnyKeySchemaElement,
    KeyType_HASH,
    KeyType_RANGE,
    KeysAndAttributes_KeysAndAttributes as DafnyKeysAndAttributes,
    KinesisDataStreamDestination_KinesisDataStreamDestination as DafnyKinesisDataStreamDestination,
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
    LocalSecondaryIndexDescription_LocalSecondaryIndexDescription as DafnyLocalSecondaryIndexDescription,
    LocalSecondaryIndexInfo_LocalSecondaryIndexInfo as DafnyLocalSecondaryIndexInfo,
    LocalSecondaryIndex_LocalSecondaryIndex as DafnyLocalSecondaryIndex,
    ParameterizedStatement_ParameterizedStatement as DafnyParameterizedStatement,
    PointInTimeRecoveryDescription_PointInTimeRecoveryDescription as DafnyPointInTimeRecoveryDescription,
    PointInTimeRecoverySpecification_PointInTimeRecoverySpecification as DafnyPointInTimeRecoverySpecification,
    PointInTimeRecoveryStatus_DISABLED,
    PointInTimeRecoveryStatus_ENABLED,
    ProjectionType_ALL,
    ProjectionType_INCLUDE,
    ProjectionType_KEYS__ONLY,
    Projection_Projection as DafnyProjection,
    ProvisionedThroughputDescription_ProvisionedThroughputDescription as DafnyProvisionedThroughputDescription,
    ProvisionedThroughputOverride_ProvisionedThroughputOverride as DafnyProvisionedThroughputOverride,
    ProvisionedThroughput_ProvisionedThroughput as DafnyProvisionedThroughput,
    PutItemInput_PutItemInput as DafnyPutItemInput,
    PutItemOutput_PutItemOutput as DafnyPutItemOutput,
    PutRequest_PutRequest as DafnyPutRequest,
    Put_Put as DafnyPut,
    QueryInput_QueryInput as DafnyQueryInput,
    QueryOutput_QueryOutput as DafnyQueryOutput,
    ReplicaAutoScalingDescription_ReplicaAutoScalingDescription as DafnyReplicaAutoScalingDescription,
    ReplicaAutoScalingUpdate_ReplicaAutoScalingUpdate as DafnyReplicaAutoScalingUpdate,
    ReplicaDescription_ReplicaDescription as DafnyReplicaDescription,
    ReplicaGlobalSecondaryIndexAutoScalingDescription_ReplicaGlobalSecondaryIndexAutoScalingDescription as DafnyReplicaGlobalSecondaryIndexAutoScalingDescription,
    ReplicaGlobalSecondaryIndexAutoScalingUpdate_ReplicaGlobalSecondaryIndexAutoScalingUpdate as DafnyReplicaGlobalSecondaryIndexAutoScalingUpdate,
    ReplicaGlobalSecondaryIndexDescription_ReplicaGlobalSecondaryIndexDescription as DafnyReplicaGlobalSecondaryIndexDescription,
    ReplicaGlobalSecondaryIndexSettingsDescription_ReplicaGlobalSecondaryIndexSettingsDescription as DafnyReplicaGlobalSecondaryIndexSettingsDescription,
    ReplicaGlobalSecondaryIndexSettingsUpdate_ReplicaGlobalSecondaryIndexSettingsUpdate as DafnyReplicaGlobalSecondaryIndexSettingsUpdate,
    ReplicaGlobalSecondaryIndex_ReplicaGlobalSecondaryIndex as DafnyReplicaGlobalSecondaryIndex,
    ReplicaSettingsDescription_ReplicaSettingsDescription as DafnyReplicaSettingsDescription,
    ReplicaSettingsUpdate_ReplicaSettingsUpdate as DafnyReplicaSettingsUpdate,
    ReplicaStatus_ACTIVE,
    ReplicaStatus_CREATING,
    ReplicaStatus_CREATION__FAILED,
    ReplicaStatus_DELETING,
    ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS,
    ReplicaStatus_REGION__DISABLED,
    ReplicaStatus_UPDATING,
    ReplicaUpdate_ReplicaUpdate as DafnyReplicaUpdate,
    Replica_Replica as DafnyReplica,
    ReplicationGroupUpdate_ReplicationGroupUpdate as DafnyReplicationGroupUpdate,
    RestoreSummary_RestoreSummary as DafnyRestoreSummary,
    RestoreTableFromBackupInput_RestoreTableFromBackupInput as DafnyRestoreTableFromBackupInput,
    RestoreTableFromBackupOutput_RestoreTableFromBackupOutput as DafnyRestoreTableFromBackupOutput,
    RestoreTableToPointInTimeInput_RestoreTableToPointInTimeInput as DafnyRestoreTableToPointInTimeInput,
    RestoreTableToPointInTimeOutput_RestoreTableToPointInTimeOutput as DafnyRestoreTableToPointInTimeOutput,
    ReturnConsumedCapacity_INDEXES,
    ReturnConsumedCapacity_NONE,
    ReturnConsumedCapacity_TOTAL,
    ReturnItemCollectionMetrics_NONE,
    ReturnItemCollectionMetrics_SIZE,
    ReturnValue_ALL__NEW,
    ReturnValue_ALL__OLD,
    ReturnValue_NONE,
    ReturnValue_UPDATED__NEW,
    ReturnValue_UPDATED__OLD,
    ReturnValuesOnConditionCheckFailure_ALL__OLD,
    ReturnValuesOnConditionCheckFailure_NONE,
    S3BucketSource_S3BucketSource as DafnyS3BucketSource,
    S3SseAlgorithm_AES256,
    S3SseAlgorithm_KMS,
    SSEDescription_SSEDescription as DafnySSEDescription,
    SSESpecification_SSESpecification as DafnySSESpecification,
    SSEStatus_DISABLED,
    SSEStatus_DISABLING,
    SSEStatus_ENABLED,
    SSEStatus_ENABLING,
    SSEStatus_UPDATING,
    SSEType_AES256,
    SSEType_KMS,
    ScalarAttributeType_B,
    ScalarAttributeType_N,
    ScalarAttributeType_S,
    ScanInput_ScanInput as DafnyScanInput,
    ScanOutput_ScanOutput as DafnyScanOutput,
    Select_ALL__ATTRIBUTES,
    Select_ALL__PROJECTED__ATTRIBUTES,
    Select_COUNT,
    Select_SPECIFIC__ATTRIBUTES,
    SourceTableDetails_SourceTableDetails as DafnySourceTableDetails,
    SourceTableFeatureDetails_SourceTableFeatureDetails as DafnySourceTableFeatureDetails,
    StreamSpecification_StreamSpecification as DafnyStreamSpecification,
    StreamViewType_KEYS__ONLY,
    StreamViewType_NEW__AND__OLD__IMAGES,
    StreamViewType_NEW__IMAGE,
    StreamViewType_OLD__IMAGE,
    TableAutoScalingDescription_TableAutoScalingDescription as DafnyTableAutoScalingDescription,
    TableClassSummary_TableClassSummary as DafnyTableClassSummary,
    TableClass_STANDARD,
    TableClass_STANDARD__INFREQUENT__ACCESS,
    TableCreationParameters_TableCreationParameters as DafnyTableCreationParameters,
    TableDescription_TableDescription as DafnyTableDescription,
    TableStatus_ACTIVE,
    TableStatus_ARCHIVED,
    TableStatus_ARCHIVING,
    TableStatus_CREATING,
    TableStatus_DELETING,
    TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS,
    TableStatus_UPDATING,
    TagResourceInput_TagResourceInput as DafnyTagResourceInput,
    Tag_Tag as DafnyTag,
    TimeToLiveDescription_TimeToLiveDescription as DafnyTimeToLiveDescription,
    TimeToLiveSpecification_TimeToLiveSpecification as DafnyTimeToLiveSpecification,
    TimeToLiveStatus_DISABLED,
    TimeToLiveStatus_DISABLING,
    TimeToLiveStatus_ENABLED,
    TimeToLiveStatus_ENABLING,
    TransactGetItem_TransactGetItem as DafnyTransactGetItem,
    TransactGetItemsInput_TransactGetItemsInput as DafnyTransactGetItemsInput,
    TransactGetItemsOutput_TransactGetItemsOutput as DafnyTransactGetItemsOutput,
    TransactWriteItem_TransactWriteItem as DafnyTransactWriteItem,
    TransactWriteItemsInput_TransactWriteItemsInput as DafnyTransactWriteItemsInput,
    TransactWriteItemsOutput_TransactWriteItemsOutput as DafnyTransactWriteItemsOutput,
    UntagResourceInput_UntagResourceInput as DafnyUntagResourceInput,
    UpdateContinuousBackupsInput_UpdateContinuousBackupsInput as DafnyUpdateContinuousBackupsInput,
    UpdateContinuousBackupsOutput_UpdateContinuousBackupsOutput as DafnyUpdateContinuousBackupsOutput,
    UpdateContributorInsightsInput_UpdateContributorInsightsInput as DafnyUpdateContributorInsightsInput,
    UpdateContributorInsightsOutput_UpdateContributorInsightsOutput as DafnyUpdateContributorInsightsOutput,
    UpdateGlobalSecondaryIndexAction_UpdateGlobalSecondaryIndexAction as DafnyUpdateGlobalSecondaryIndexAction,
    UpdateGlobalTableInput_UpdateGlobalTableInput as DafnyUpdateGlobalTableInput,
    UpdateGlobalTableOutput_UpdateGlobalTableOutput as DafnyUpdateGlobalTableOutput,
    UpdateGlobalTableSettingsInput_UpdateGlobalTableSettingsInput as DafnyUpdateGlobalTableSettingsInput,
    UpdateGlobalTableSettingsOutput_UpdateGlobalTableSettingsOutput as DafnyUpdateGlobalTableSettingsOutput,
    UpdateItemInput_UpdateItemInput as DafnyUpdateItemInput,
    UpdateItemOutput_UpdateItemOutput as DafnyUpdateItemOutput,
    UpdateReplicationGroupMemberAction_UpdateReplicationGroupMemberAction as DafnyUpdateReplicationGroupMemberAction,
    UpdateTableInput_UpdateTableInput as DafnyUpdateTableInput,
    UpdateTableOutput_UpdateTableOutput as DafnyUpdateTableOutput,
    UpdateTableReplicaAutoScalingInput_UpdateTableReplicaAutoScalingInput as DafnyUpdateTableReplicaAutoScalingInput,
    UpdateTableReplicaAutoScalingOutput_UpdateTableReplicaAutoScalingOutput as DafnyUpdateTableReplicaAutoScalingOutput,
    UpdateTimeToLiveInput_UpdateTimeToLiveInput as DafnyUpdateTimeToLiveInput,
    UpdateTimeToLiveOutput_UpdateTimeToLiveOutput as DafnyUpdateTimeToLiveOutput,
    Update_Update as DafnyUpdate,
    WriteRequest_WriteRequest as DafnyWriteRequest,
)
import aws_cryptography_internal_dynamodb.internaldafny.generated.module_
import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny
from smithy_dafny_standard_library.internaldafny.generated.Wrappers import (
    Option_None,
    Option_Some,
)


def com_amazonaws_dynamodb_BackupInUseException(native_input):
    return Error_BackupInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_BackupNotFoundException(native_input):
    return Error_BackupNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ConditionalCheckFailedException(native_input):
    return Error_ConditionalCheckFailedException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ContinuousBackupsUnavailableException(native_input):
    return Error_ContinuousBackupsUnavailableException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DuplicateItemException(native_input):
    return Error_DuplicateItemException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ExportConflictException(native_input):
    return Error_ExportConflictException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ExportNotFoundException(native_input):
    return Error_ExportNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_GlobalTableAlreadyExistsException(native_input):
    return Error_GlobalTableAlreadyExistsException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_GlobalTableNotFoundException(native_input):
    return Error_GlobalTableNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_IdempotentParameterMismatchException(native_input):
    return Error_IdempotentParameterMismatchException(
        Message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ImportConflictException(native_input):
    return Error_ImportConflictException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ImportNotFoundException(native_input):
    return Error_ImportNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_IndexNotFoundException(native_input):
    return Error_IndexNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_InternalServerError(native_input):
    return Error_InternalServerError(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_InvalidEndpointException(native_input):
    return Error_InvalidEndpointException(
        Message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_InvalidExportTimeException(native_input):
    return Error_InvalidExportTimeException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_InvalidRestoreTimeException(native_input):
    return Error_InvalidRestoreTimeException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ItemCollectionSizeLimitExceededException(native_input):
    return Error_ItemCollectionSizeLimitExceededException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_LimitExceededException(native_input):
    return Error_LimitExceededException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_PointInTimeRecoveryUnavailableException(native_input):
    return Error_PointInTimeRecoveryUnavailableException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ProvisionedThroughputExceededException(native_input):
    return Error_ProvisionedThroughputExceededException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ReplicaAlreadyExistsException(native_input):
    return Error_ReplicaAlreadyExistsException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ReplicaNotFoundException(native_input):
    return Error_ReplicaNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_RequestLimitExceeded(native_input):
    return Error_RequestLimitExceeded(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ResourceInUseException(native_input):
    return Error_ResourceInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ResourceNotFoundException(native_input):
    return Error_ResourceNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_TableAlreadyExistsException(native_input):
    return Error_TableAlreadyExistsException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_TableInUseException(native_input):
    return Error_TableInUseException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_TableNotFoundException(native_input):
    return Error_TableNotFoundException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_TransactionCanceledException(native_input):
    return Error_TransactionCanceledException(
        Message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        CancellationReasons=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CancellationReason(
                    list_element
                )
                for list_element in native_input["CancellationReasons"]
            ]
        ),
    )


def com_amazonaws_dynamodb_CancellationReason(native_input):
    return DafnyCancellationReason(
        Item=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Item"].items()
                    }
                )
            )
            if "Item" in native_input.keys()
            else Option_None()
        ),
        Code=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Code"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Code" in native_input.keys()
            else Option_None()
        ),
        Message=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Message"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Message" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AttributeValue(native_input):
    if "S" in native_input.keys():
        AttributeValue_union_value = AttributeValue_S(
            Seq(
                "".join(
                    [
                        chr(int.from_bytes(pair, "big"))
                        for pair in zip(
                            *[iter(native_input["S"].encode("utf-16-be"))] * 2
                        )
                    ]
                )
            )
        )
    elif "N" in native_input.keys():
        AttributeValue_union_value = AttributeValue_N(
            Seq(
                "".join(
                    [
                        chr(int.from_bytes(pair, "big"))
                        for pair in zip(
                            *[iter(native_input["N"].encode("utf-16-be"))] * 2
                        )
                    ]
                )
            )
        )
    elif "B" in native_input.keys():
        AttributeValue_union_value = AttributeValue_B(Seq(native_input["B"]))
    elif "SS" in native_input.keys():
        AttributeValue_union_value = AttributeValue_SS(
            Seq(
                [
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(list_element.encode("utf-16-be"))] * 2
                                )
                            ]
                        )
                    )
                    for list_element in native_input["SS"]
                ]
            )
        )
    elif "NS" in native_input.keys():
        AttributeValue_union_value = AttributeValue_NS(
            Seq(
                [
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(
                                    *[iter(list_element.encode("utf-16-be"))] * 2
                                )
                            ]
                        )
                    )
                    for list_element in native_input["NS"]
                ]
            )
        )
    elif "BS" in native_input.keys():
        AttributeValue_union_value = AttributeValue_BS(
            Seq([Seq(list_element) for list_element in native_input["BS"]])
        )
    elif "M" in native_input.keys():
        AttributeValue_union_value = AttributeValue_M(
            Map(
                {
                    Seq(
                        "".join(
                            [
                                chr(int.from_bytes(pair, "big"))
                                for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                            ]
                        )
                    ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                        value
                    )
                    for (key, value) in native_input["M"].items()
                }
            )
        )
    elif "L" in native_input.keys():
        AttributeValue_union_value = AttributeValue_L(
            Seq(
                [
                    aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                        list_element
                    )
                    for list_element in native_input["L"]
                ]
            )
        )
    elif "NULL" in native_input.keys():
        AttributeValue_union_value = AttributeValue_NULL(native_input["NULL"])
    elif "BOOL" in native_input.keys():
        AttributeValue_union_value = AttributeValue_BOOL(native_input["BOOL"])
    else:
        raise ValueError(
            "No recognized union value in union type: " + str(native_input)
        )

    return AttributeValue_union_value


def com_amazonaws_dynamodb_TransactionConflictException(native_input):
    return Error_TransactionConflictException(
        message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_TransactionInProgressException(native_input):
    return Error_TransactionInProgressException(
        Message=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Error"]["Message"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_BatchExecuteStatementInput(native_input):
    return DafnyBatchExecuteStatementInput(
        Statements=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchStatementRequest(
                    list_element
                )
                for list_element in native_input["Statements"]
            ]
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchStatementRequest(native_input):
    return DafnyBatchStatementRequest(
        Statement=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Statement"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Parameters=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            list_element
                        )
                        for list_element in native_input["Parameters"]
                    ]
                )
            )
            if "Parameters" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReturnConsumedCapacity(native_input):
    # Convert ReturnConsumedCapacity
    if native_input == "INDEXES":
        return ReturnConsumedCapacity_INDEXES()
    elif native_input == "TOTAL":
        return ReturnConsumedCapacity_TOTAL()
    elif native_input == "NONE":
        return ReturnConsumedCapacity_NONE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_BatchExecuteStatementOutput(native_input):
    return DafnyBatchExecuteStatementOutput(
        Responses=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchStatementResponse(
                            list_element
                        )
                        for list_element in native_input["Responses"]
                    ]
                )
            )
            if "Responses" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchStatementResponse(native_input):
    return DafnyBatchStatementResponse(
        Error=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchStatementError(
                    native_input["Error"]
                )
            )
            if "Error" in native_input.keys()
            else Option_None()
        ),
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        Item=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Item"].items()
                    }
                )
            )
            if "Item" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchStatementError(native_input):
    return DafnyBatchStatementError(
        Code=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(
                    native_input["Code"]
                )
            )
            if "Code" in native_input.keys()
            else Option_None()
        ),
        Message=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Message"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "Message" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(native_input):
    # Convert BatchStatementErrorCodeEnum
    if native_input == "ConditionalCheckFailed":
        return BatchStatementErrorCodeEnum_ConditionalCheckFailed()
    elif native_input == "ItemCollectionSizeLimitExceeded":
        return BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded()
    elif native_input == "RequestLimitExceeded":
        return BatchStatementErrorCodeEnum_RequestLimitExceeded()
    elif native_input == "ValidationError":
        return BatchStatementErrorCodeEnum_ValidationError()
    elif native_input == "ProvisionedThroughputExceeded":
        return BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded()
    elif native_input == "TransactionConflict":
        return BatchStatementErrorCodeEnum_TransactionConflict()
    elif native_input == "ThrottlingError":
        return BatchStatementErrorCodeEnum_ThrottlingError()
    elif native_input == "InternalServerError":
        return BatchStatementErrorCodeEnum_InternalServerError()
    elif native_input == "ResourceNotFound":
        return BatchStatementErrorCodeEnum_ResourceNotFound()
    elif native_input == "AccessDenied":
        return BatchStatementErrorCodeEnum_AccessDenied()
    elif native_input == "DuplicateItem":
        return BatchStatementErrorCodeEnum_DuplicateItem()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ConsumedCapacity(native_input):
    return DafnyConsumedCapacity(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        CapacityUnits=(
            Option_Some(native_input["CapacityUnits"])
            if "CapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ReadCapacityUnits=(
            Option_Some(native_input["ReadCapacityUnits"])
            if "ReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        WriteCapacityUnits=(
            Option_Some(native_input["WriteCapacityUnits"])
            if "WriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        Table=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Capacity(
                    native_input["Table"]
                )
            )
            if "Table" in native_input.keys()
            else Option_None()
        ),
        LocalSecondaryIndexes=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Capacity(
                            value
                        )
                        for (key, value) in native_input[
                            "LocalSecondaryIndexes"
                        ].items()
                    }
                )
            )
            if "LocalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Capacity(
                            value
                        )
                        for (key, value) in native_input[
                            "GlobalSecondaryIndexes"
                        ].items()
                    }
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_Capacity(native_input):
    return DafnyCapacity(
        ReadCapacityUnits=(
            Option_Some(native_input["ReadCapacityUnits"])
            if "ReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        WriteCapacityUnits=(
            Option_Some(native_input["WriteCapacityUnits"])
            if "WriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        CapacityUnits=(
            Option_Some(native_input["CapacityUnits"])
            if "CapacityUnits" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchGetItemInput(native_input):
    return DafnyBatchGetItemInput(
        RequestItems=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeysAndAttributes(
                    value
                )
                for (key, value) in native_input["RequestItems"].items()
            }
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_KeysAndAttributes(native_input):
    return DafnyKeysAndAttributes(
        Keys=Seq(
            [
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in list_element.items()
                    }
                )
                for list_element in native_input["Keys"]
            ]
        ),
        AttributesToGet=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["AttributesToGet"]
                    ]
                )
            )
            if "AttributesToGet" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
        ProjectionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ProjectionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ProjectionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchGetItemOutput(native_input):
    return DafnyBatchGetItemOutput(
        Responses=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            [
                                Map(
                                    {
                                        Seq(
                                            "".join(
                                                [
                                                    chr(int.from_bytes(pair, "big"))
                                                    for pair in zip(
                                                        *[iter(key.encode("utf-16-be"))]
                                                        * 2
                                                    )
                                                ]
                                            )
                                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                                            value
                                        )
                                        for (key, value) in list_element.items()
                                    }
                                )
                                for list_element in value
                            ]
                        )
                        for (key, value) in native_input["Responses"].items()
                    }
                )
            )
            if "Responses" in native_input.keys()
            else Option_None()
        ),
        UnprocessedKeys=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeysAndAttributes(
                            value
                        )
                        for (key, value) in native_input["UnprocessedKeys"].items()
                    }
                )
            )
            if "UnprocessedKeys" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BatchWriteItemInput(native_input):
    return DafnyBatchWriteItemInput(
        RequestItems=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_WriteRequest(
                            list_element
                        )
                        for list_element in value
                    ]
                )
                for (key, value) in native_input["RequestItems"].items()
            }
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ReturnItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                    native_input["ReturnItemCollectionMetrics"]
                )
            )
            if "ReturnItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_WriteRequest(native_input):
    return DafnyWriteRequest(
        PutRequest=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PutRequest(
                    native_input["PutRequest"]
                )
            )
            if "PutRequest" in native_input.keys()
            else Option_None()
        ),
        DeleteRequest=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteRequest(
                    native_input["DeleteRequest"]
                )
            )
            if "DeleteRequest" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_PutRequest(native_input):
    return DafnyPutRequest(
        Item=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Item"].items()
            }
        ),
    )


def com_amazonaws_dynamodb_DeleteRequest(native_input):
    return DafnyDeleteRequest(
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
    )


def com_amazonaws_dynamodb_ReturnItemCollectionMetrics(native_input):
    # Convert ReturnItemCollectionMetrics
    if native_input == "SIZE":
        return ReturnItemCollectionMetrics_SIZE()
    elif native_input == "NONE":
        return ReturnItemCollectionMetrics_NONE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_BatchWriteItemOutput(native_input):
    return DafnyBatchWriteItemOutput(
        UnprocessedItems=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            [
                                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_WriteRequest(
                                    list_element
                                )
                                for list_element in value
                            ]
                        )
                        for (key, value) in native_input["UnprocessedItems"].items()
                    }
                )
            )
            if "UnprocessedItems" in native_input.keys()
            else Option_None()
        ),
        ItemCollectionMetrics=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            [
                                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionMetrics(
                                    list_element
                                )
                                for list_element in value
                            ]
                        )
                        for (key, value) in native_input[
                            "ItemCollectionMetrics"
                        ].items()
                    }
                )
            )
            if "ItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ItemCollectionMetrics(native_input):
    return DafnyItemCollectionMetrics(
        ItemCollectionKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["ItemCollectionKey"].items()
                    }
                )
            )
            if "ItemCollectionKey" in native_input.keys()
            else Option_None()
        ),
        SizeEstimateRangeGB=(
            Option_Some(
                Seq(
                    [
                        list_element
                        for list_element in native_input["SizeEstimateRangeGB"]
                    ]
                )
            )
            if "SizeEstimateRangeGB" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_CreateBackupInput(native_input):
    return DafnyCreateBackupInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BackupName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_CreateBackupOutput(native_input):
    return DafnyCreateBackupOutput(
        BackupDetails=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupDetails(
                    native_input["BackupDetails"]
                )
            )
            if "BackupDetails" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BackupDetails(native_input):
    return DafnyBackupDetails(
        BackupArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BackupName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BackupSizeBytes=(
            Option_Some(native_input["BackupSizeBytes"])
            if "BackupSizeBytes" in native_input.keys()
            else Option_None()
        ),
        BackupStatus=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupStatus(
            native_input["BackupStatus"]
        ),
        BackupType=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupType(
            native_input["BackupType"]
        ),
        BackupCreationDateTime=_dafny.Seq(
            native_input["BackupCreationDateTime"].isoformat()
        ),
        BackupExpiryDateTime=(
            Option_Some(_dafny.Seq(native_input["BackupExpiryDateTime"].isoformat()))
            if "BackupExpiryDateTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BackupStatus(native_input):
    # Convert BackupStatus
    if native_input == "CREATING":
        return BackupStatus_CREATING()
    elif native_input == "DELETED":
        return BackupStatus_DELETED()
    elif native_input == "AVAILABLE":
        return BackupStatus_AVAILABLE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_BackupType(native_input):
    # Convert BackupType
    if native_input == "USER":
        return BackupType_USER()
    elif native_input == "SYSTEM":
        return BackupType_SYSTEM()
    elif native_input == "AWS_BACKUP":
        return BackupType_AWS__BACKUP()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_CreateGlobalTableInput(native_input):
    return DafnyCreateGlobalTableInput(
        GlobalTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GlobalTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicationGroup=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Replica(
                    list_element
                )
                for list_element in native_input["ReplicationGroup"]
            ]
        ),
    )


def com_amazonaws_dynamodb_Replica(native_input):
    return DafnyReplica(
        RegionName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["RegionName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RegionName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_CreateGlobalTableOutput(native_input):
    return DafnyCreateGlobalTableOutput(
        GlobalTableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableDescription(
                    native_input["GlobalTableDescription"]
                )
            )
            if "GlobalTableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalTableDescription(native_input):
    return DafnyGlobalTableDescription(
        ReplicationGroup=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaDescription(
                            list_element
                        )
                        for list_element in native_input["ReplicationGroup"]
                    ]
                )
            )
            if "ReplicationGroup" in native_input.keys()
            else Option_None()
        ),
        GlobalTableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableArn" in native_input.keys()
            else Option_None()
        ),
        CreationDateTime=(
            Option_Some(_dafny.Seq(native_input["CreationDateTime"].isoformat()))
            if "CreationDateTime" in native_input.keys()
            else Option_None()
        ),
        GlobalTableStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableStatus(
                    native_input["GlobalTableStatus"]
                )
            )
            if "GlobalTableStatus" in native_input.keys()
            else Option_None()
        ),
        GlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaDescription(native_input):
    return DafnyReplicaDescription(
        RegionName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["RegionName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RegionName" in native_input.keys()
            else Option_None()
        ),
        ReplicaStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaStatus(
                    native_input["ReplicaStatus"]
                )
            )
            if "ReplicaStatus" in native_input.keys()
            else Option_None()
        ),
        ReplicaStatusDescription=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ReplicaStatusDescription"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ReplicaStatusDescription" in native_input.keys()
            else Option_None()
        ),
        ReplicaStatusPercentProgress=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "ReplicaStatusPercentProgress"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ReplicaStatusPercentProgress" in native_input.keys()
            else Option_None()
        ),
        KMSMasterKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KMSMasterKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KMSMasterKeyId" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        ReplicaInaccessibleDateTime=(
            Option_Some(
                _dafny.Seq(native_input["ReplicaInaccessibleDateTime"].isoformat())
            )
            if "ReplicaInaccessibleDateTime" in native_input.keys()
            else Option_None()
        ),
        ReplicaTableClassSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClassSummary(
                    native_input["ReplicaTableClassSummary"]
                )
            )
            if "ReplicaTableClassSummary" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalTableStatus(native_input):
    # Convert GlobalTableStatus
    if native_input == "CREATING":
        return GlobalTableStatus_CREATING()
    elif native_input == "ACTIVE":
        return GlobalTableStatus_ACTIVE()
    elif native_input == "DELETING":
        return GlobalTableStatus_DELETING()
    elif native_input == "UPDATING":
        return GlobalTableStatus_UPDATING()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ReplicaStatus(native_input):
    # Convert ReplicaStatus
    if native_input == "CREATING":
        return ReplicaStatus_CREATING()
    elif native_input == "CREATION_FAILED":
        return ReplicaStatus_CREATION__FAILED()
    elif native_input == "UPDATING":
        return ReplicaStatus_UPDATING()
    elif native_input == "DELETING":
        return ReplicaStatus_DELETING()
    elif native_input == "ACTIVE":
        return ReplicaStatus_ACTIVE()
    elif native_input == "REGION_DISABLED":
        return ReplicaStatus_REGION__DISABLED()
    elif native_input == "INACCESSIBLE_ENCRYPTION_CREDENTIALS":
        return ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ProvisionedThroughputOverride(native_input):
    return DafnyProvisionedThroughputOverride(
        ReadCapacityUnits=(
            Option_Some(native_input["ReadCapacityUnits"])
            if "ReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(native_input):
    return DafnyReplicaGlobalSecondaryIndexDescription(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TableClassSummary(native_input):
    return DafnyTableClassSummary(
        TableClass=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["TableClass"]
                )
            )
            if "TableClass" in native_input.keys()
            else Option_None()
        ),
        LastUpdateDateTime=(
            Option_Some(_dafny.Seq(native_input["LastUpdateDateTime"].isoformat()))
            if "LastUpdateDateTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TableClass(native_input):
    # Convert TableClass
    if native_input == "STANDARD":
        return TableClass_STANDARD()
    elif native_input == "STANDARD_INFREQUENT_ACCESS":
        return TableClass_STANDARD__INFREQUENT__ACCESS()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_CreateTableInput(native_input):
    return DafnyCreateTableInput(
        AttributeDefinitions=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeDefinition(
                    list_element
                )
                for list_element in native_input["AttributeDefinitions"]
            ]
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        LocalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LocalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["LocalSecondaryIndexes"]
                    ]
                )
            )
            if "LocalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        BillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingMode"]
                )
            )
            if "BillingMode" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
        StreamSpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_StreamSpecification(
                    native_input["StreamSpecification"]
                )
            )
            if "StreamSpecification" in native_input.keys()
            else Option_None()
        ),
        SSESpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSESpecification(
                    native_input["SSESpecification"]
                )
            )
            if "SSESpecification" in native_input.keys()
            else Option_None()
        ),
        Tags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Tag(
                            list_element
                        )
                        for list_element in native_input["Tags"]
                    ]
                )
            )
            if "Tags" in native_input.keys()
            else Option_None()
        ),
        TableClass=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["TableClass"]
                )
            )
            if "TableClass" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AttributeDefinition(native_input):
    return DafnyAttributeDefinition(
        AttributeName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AttributeName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        AttributeType=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ScalarAttributeType(
            native_input["AttributeType"]
        ),
    )


def com_amazonaws_dynamodb_ScalarAttributeType(native_input):
    # Convert ScalarAttributeType
    if native_input == "S":
        return ScalarAttributeType_S()
    elif native_input == "N":
        return ScalarAttributeType_N()
    elif native_input == "B":
        return ScalarAttributeType_B()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_KeySchemaElement(native_input):
    return DafnyKeySchemaElement(
        AttributeName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AttributeName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeyType=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeyType(
            native_input["KeyType"]
        ),
    )


def com_amazonaws_dynamodb_KeyType(native_input):
    # Convert KeyType
    if native_input == "HASH":
        return KeyType_HASH()
    elif native_input == "RANGE":
        return KeyType_RANGE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_LocalSecondaryIndex(native_input):
    return DafnyLocalSecondaryIndex(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        Projection=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
            native_input["Projection"]
        ),
    )


def com_amazonaws_dynamodb_Projection(native_input):
    return DafnyProjection(
        ProjectionType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProjectionType(
                    native_input["ProjectionType"]
                )
            )
            if "ProjectionType" in native_input.keys()
            else Option_None()
        ),
        NonKeyAttributes=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["NonKeyAttributes"]
                    ]
                )
            )
            if "NonKeyAttributes" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ProjectionType(native_input):
    # Convert ProjectionType
    if native_input == "ALL":
        return ProjectionType_ALL()
    elif native_input == "KEYS_ONLY":
        return ProjectionType_KEYS__ONLY()
    elif native_input == "INCLUDE":
        return ProjectionType_INCLUDE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_GlobalSecondaryIndex(native_input):
    return DafnyGlobalSecondaryIndex(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        Projection=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
            native_input["Projection"]
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ProvisionedThroughput(native_input):
    return DafnyProvisionedThroughput(
        ReadCapacityUnits=native_input["ReadCapacityUnits"],
        WriteCapacityUnits=native_input["WriteCapacityUnits"],
    )


def com_amazonaws_dynamodb_BillingMode(native_input):
    # Convert BillingMode
    if native_input == "PROVISIONED":
        return BillingMode_PROVISIONED()
    elif native_input == "PAY_PER_REQUEST":
        return BillingMode_PAY__PER__REQUEST()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_StreamSpecification(native_input):
    return DafnyStreamSpecification(
        StreamEnabled=native_input["StreamEnabled"],
        StreamViewType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_StreamViewType(
                    native_input["StreamViewType"]
                )
            )
            if "StreamViewType" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_StreamViewType(native_input):
    # Convert StreamViewType
    if native_input == "NEW_IMAGE":
        return StreamViewType_NEW__IMAGE()
    elif native_input == "OLD_IMAGE":
        return StreamViewType_OLD__IMAGE()
    elif native_input == "NEW_AND_OLD_IMAGES":
        return StreamViewType_NEW__AND__OLD__IMAGES()
    elif native_input == "KEYS_ONLY":
        return StreamViewType_KEYS__ONLY()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_SSESpecification(native_input):
    return DafnySSESpecification(
        Enabled=(
            Option_Some(native_input["Enabled"])
            if "Enabled" in native_input.keys()
            else Option_None()
        ),
        SSEType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSEType(
                    native_input["SSEType"]
                )
            )
            if "SSEType" in native_input.keys()
            else Option_None()
        ),
        KMSMasterKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KMSMasterKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KMSMasterKeyId" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_SSEType(native_input):
    # Convert SSEType
    if native_input == "AES256":
        return SSEType_AES256()
    elif native_input == "KMS":
        return SSEType_KMS()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_Tag(native_input):
    return DafnyTag(
        Key=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Key"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Value=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Value"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_CreateTableOutput(native_input):
    return DafnyCreateTableOutput(
        TableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["TableDescription"]
                )
            )
            if "TableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TableDescription(native_input):
    return DafnyTableDescription(
        AttributeDefinitions=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeDefinition(
                            list_element
                        )
                        for list_element in native_input["AttributeDefinitions"]
                    ]
                )
            )
            if "AttributeDefinitions" in native_input.keys()
            else Option_None()
        ),
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        KeySchema=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                            list_element
                        )
                        for list_element in native_input["KeySchema"]
                    ]
                )
            )
            if "KeySchema" in native_input.keys()
            else Option_None()
        ),
        TableStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableStatus(
                    native_input["TableStatus"]
                )
            )
            if "TableStatus" in native_input.keys()
            else Option_None()
        ),
        CreationDateTime=(
            Option_Some(_dafny.Seq(native_input["CreationDateTime"].isoformat()))
            if "CreationDateTime" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
        TableSizeBytes=(
            Option_Some(native_input["TableSizeBytes"])
            if "TableSizeBytes" in native_input.keys()
            else Option_None()
        ),
        ItemCount=(
            Option_Some(native_input["ItemCount"])
            if "ItemCount" in native_input.keys()
            else Option_None()
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        TableId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "TableId" in native_input.keys()
            else Option_None()
        ),
        BillingModeSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingModeSummary(
                    native_input["BillingModeSummary"]
                )
            )
            if "BillingModeSummary" in native_input.keys()
            else Option_None()
        ),
        LocalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LocalSecondaryIndexDescription(
                            list_element
                        )
                        for list_element in native_input["LocalSecondaryIndexes"]
                    ]
                )
            )
            if "LocalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        StreamSpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_StreamSpecification(
                    native_input["StreamSpecification"]
                )
            )
            if "StreamSpecification" in native_input.keys()
            else Option_None()
        ),
        LatestStreamLabel=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["LatestStreamLabel"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "LatestStreamLabel" in native_input.keys()
            else Option_None()
        ),
        LatestStreamArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["LatestStreamArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "LatestStreamArn" in native_input.keys()
            else Option_None()
        ),
        GlobalTableVersion=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableVersion"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableVersion" in native_input.keys()
            else Option_None()
        ),
        Replicas=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaDescription(
                            list_element
                        )
                        for list_element in native_input["Replicas"]
                    ]
                )
            )
            if "Replicas" in native_input.keys()
            else Option_None()
        ),
        RestoreSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_RestoreSummary(
                    native_input["RestoreSummary"]
                )
            )
            if "RestoreSummary" in native_input.keys()
            else Option_None()
        ),
        SSEDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSEDescription(
                    native_input["SSEDescription"]
                )
            )
            if "SSEDescription" in native_input.keys()
            else Option_None()
        ),
        ArchivalSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ArchivalSummary(
                    native_input["ArchivalSummary"]
                )
            )
            if "ArchivalSummary" in native_input.keys()
            else Option_None()
        ),
        TableClassSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClassSummary(
                    native_input["TableClassSummary"]
                )
            )
            if "TableClassSummary" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TableStatus(native_input):
    # Convert TableStatus
    if native_input == "CREATING":
        return TableStatus_CREATING()
    elif native_input == "UPDATING":
        return TableStatus_UPDATING()
    elif native_input == "DELETING":
        return TableStatus_DELETING()
    elif native_input == "ACTIVE":
        return TableStatus_ACTIVE()
    elif native_input == "INACCESSIBLE_ENCRYPTION_CREDENTIALS":
        return TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS()
    elif native_input == "ARCHIVING":
        return TableStatus_ARCHIVING()
    elif native_input == "ARCHIVED":
        return TableStatus_ARCHIVED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ProvisionedThroughputDescription(native_input):
    return DafnyProvisionedThroughputDescription(
        LastIncreaseDateTime=(
            Option_Some(_dafny.Seq(native_input["LastIncreaseDateTime"].isoformat()))
            if "LastIncreaseDateTime" in native_input.keys()
            else Option_None()
        ),
        LastDecreaseDateTime=(
            Option_Some(_dafny.Seq(native_input["LastDecreaseDateTime"].isoformat()))
            if "LastDecreaseDateTime" in native_input.keys()
            else Option_None()
        ),
        NumberOfDecreasesToday=(
            Option_Some(native_input["NumberOfDecreasesToday"])
            if "NumberOfDecreasesToday" in native_input.keys()
            else Option_None()
        ),
        ReadCapacityUnits=(
            Option_Some(native_input["ReadCapacityUnits"])
            if "ReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        WriteCapacityUnits=(
            Option_Some(native_input["WriteCapacityUnits"])
            if "WriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BillingModeSummary(native_input):
    return DafnyBillingModeSummary(
        BillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingMode"]
                )
            )
            if "BillingMode" in native_input.keys()
            else Option_None()
        ),
        LastUpdateToPayPerRequestDateTime=(
            Option_Some(
                _dafny.Seq(
                    native_input["LastUpdateToPayPerRequestDateTime"].isoformat()
                )
            )
            if "LastUpdateToPayPerRequestDateTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_LocalSecondaryIndexDescription(native_input):
    return DafnyLocalSecondaryIndexDescription(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        KeySchema=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                            list_element
                        )
                        for list_element in native_input["KeySchema"]
                    ]
                )
            )
            if "KeySchema" in native_input.keys()
            else Option_None()
        ),
        Projection=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
                    native_input["Projection"]
                )
            )
            if "Projection" in native_input.keys()
            else Option_None()
        ),
        IndexSizeBytes=(
            Option_Some(native_input["IndexSizeBytes"])
            if "IndexSizeBytes" in native_input.keys()
            else Option_None()
        ),
        ItemCount=(
            Option_Some(native_input["ItemCount"])
            if "ItemCount" in native_input.keys()
            else Option_None()
        ),
        IndexArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexArn" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(native_input):
    return DafnyGlobalSecondaryIndexDescription(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        KeySchema=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                            list_element
                        )
                        for list_element in native_input["KeySchema"]
                    ]
                )
            )
            if "KeySchema" in native_input.keys()
            else Option_None()
        ),
        Projection=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
                    native_input["Projection"]
                )
            )
            if "Projection" in native_input.keys()
            else Option_None()
        ),
        IndexStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_IndexStatus(
                    native_input["IndexStatus"]
                )
            )
            if "IndexStatus" in native_input.keys()
            else Option_None()
        ),
        Backfilling=(
            Option_Some(native_input["Backfilling"])
            if "Backfilling" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
        IndexSizeBytes=(
            Option_Some(native_input["IndexSizeBytes"])
            if "IndexSizeBytes" in native_input.keys()
            else Option_None()
        ),
        ItemCount=(
            Option_Some(native_input["ItemCount"])
            if "ItemCount" in native_input.keys()
            else Option_None()
        ),
        IndexArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexArn" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_RestoreSummary(native_input):
    return DafnyRestoreSummary(
        SourceBackupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["SourceBackupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceBackupArn" in native_input.keys()
            else Option_None()
        ),
        SourceTableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["SourceTableArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceTableArn" in native_input.keys()
            else Option_None()
        ),
        RestoreDateTime=_dafny.Seq(native_input["RestoreDateTime"].isoformat()),
        RestoreInProgress=native_input["RestoreInProgress"],
    )


def com_amazonaws_dynamodb_SSEDescription(native_input):
    return DafnySSEDescription(
        Status=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSEStatus(
                    native_input["Status"]
                )
            )
            if "Status" in native_input.keys()
            else Option_None()
        ),
        SSEType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSEType(
                    native_input["SSEType"]
                )
            )
            if "SSEType" in native_input.keys()
            else Option_None()
        ),
        KMSMasterKeyArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KMSMasterKeyArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KMSMasterKeyArn" in native_input.keys()
            else Option_None()
        ),
        InaccessibleEncryptionDateTime=(
            Option_Some(
                _dafny.Seq(native_input["InaccessibleEncryptionDateTime"].isoformat())
            )
            if "InaccessibleEncryptionDateTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ArchivalSummary(native_input):
    return DafnyArchivalSummary(
        ArchivalDateTime=(
            Option_Some(_dafny.Seq(native_input["ArchivalDateTime"].isoformat()))
            if "ArchivalDateTime" in native_input.keys()
            else Option_None()
        ),
        ArchivalReason=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ArchivalReason"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ArchivalReason" in native_input.keys()
            else Option_None()
        ),
        ArchivalBackupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ArchivalBackupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ArchivalBackupArn" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_IndexStatus(native_input):
    # Convert IndexStatus
    if native_input == "CREATING":
        return IndexStatus_CREATING()
    elif native_input == "UPDATING":
        return IndexStatus_UPDATING()
    elif native_input == "DELETING":
        return IndexStatus_DELETING()
    elif native_input == "ACTIVE":
        return IndexStatus_ACTIVE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_SSEStatus(native_input):
    # Convert SSEStatus
    if native_input == "ENABLING":
        return SSEStatus_ENABLING()
    elif native_input == "ENABLED":
        return SSEStatus_ENABLED()
    elif native_input == "DISABLING":
        return SSEStatus_DISABLING()
    elif native_input == "DISABLED":
        return SSEStatus_DISABLED()
    elif native_input == "UPDATING":
        return SSEStatus_UPDATING()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DeleteBackupInput(native_input):
    return DafnyDeleteBackupInput(
        BackupArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DeleteBackupOutput(native_input):
    return DafnyDeleteBackupOutput(
        BackupDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupDescription(
                    native_input["BackupDescription"]
                )
            )
            if "BackupDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BackupDescription(native_input):
    return DafnyBackupDescription(
        BackupDetails=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupDetails(
                    native_input["BackupDetails"]
                )
            )
            if "BackupDetails" in native_input.keys()
            else Option_None()
        ),
        SourceTableDetails=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SourceTableDetails(
                    native_input["SourceTableDetails"]
                )
            )
            if "SourceTableDetails" in native_input.keys()
            else Option_None()
        ),
        SourceTableFeatureDetails=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SourceTableFeatureDetails(
                    native_input["SourceTableFeatureDetails"]
                )
            )
            if "SourceTableFeatureDetails" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_SourceTableDetails(native_input):
    return DafnySourceTableDetails(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TableId=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableId"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        TableSizeBytes=(
            Option_Some(native_input["TableSizeBytes"])
            if "TableSizeBytes" in native_input.keys()
            else Option_None()
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        TableCreationDateTime=_dafny.Seq(
            native_input["TableCreationDateTime"].isoformat()
        ),
        ProvisionedThroughput=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
            native_input["ProvisionedThroughput"]
        ),
        ItemCount=(
            Option_Some(native_input["ItemCount"])
            if "ItemCount" in native_input.keys()
            else Option_None()
        ),
        BillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingMode"]
                )
            )
            if "BillingMode" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_SourceTableFeatureDetails(native_input):
    return DafnySourceTableFeatureDetails(
        LocalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LocalSecondaryIndexInfo(
                            list_element
                        )
                        for list_element in native_input["LocalSecondaryIndexes"]
                    ]
                )
            )
            if "LocalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        StreamDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_StreamSpecification(
                    native_input["StreamDescription"]
                )
            )
            if "StreamDescription" in native_input.keys()
            else Option_None()
        ),
        TimeToLiveDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TimeToLiveDescription(
                    native_input["TimeToLiveDescription"]
                )
            )
            if "TimeToLiveDescription" in native_input.keys()
            else Option_None()
        ),
        SSEDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSEDescription(
                    native_input["SSEDescription"]
                )
            )
            if "SSEDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_LocalSecondaryIndexInfo(native_input):
    return DafnyLocalSecondaryIndexInfo(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        KeySchema=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                            list_element
                        )
                        for list_element in native_input["KeySchema"]
                    ]
                )
            )
            if "KeySchema" in native_input.keys()
            else Option_None()
        ),
        Projection=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
                    native_input["Projection"]
                )
            )
            if "Projection" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(native_input):
    return DafnyGlobalSecondaryIndexInfo(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        KeySchema=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                            list_element
                        )
                        for list_element in native_input["KeySchema"]
                    ]
                )
            )
            if "KeySchema" in native_input.keys()
            else Option_None()
        ),
        Projection=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
                    native_input["Projection"]
                )
            )
            if "Projection" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TimeToLiveDescription(native_input):
    return DafnyTimeToLiveDescription(
        TimeToLiveStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TimeToLiveStatus(
                    native_input["TimeToLiveStatus"]
                )
            )
            if "TimeToLiveStatus" in native_input.keys()
            else Option_None()
        ),
        AttributeName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["AttributeName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AttributeName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TimeToLiveStatus(native_input):
    # Convert TimeToLiveStatus
    if native_input == "ENABLING":
        return TimeToLiveStatus_ENABLING()
    elif native_input == "DISABLING":
        return TimeToLiveStatus_DISABLING()
    elif native_input == "ENABLED":
        return TimeToLiveStatus_ENABLED()
    elif native_input == "DISABLED":
        return TimeToLiveStatus_DISABLED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DeleteItemInput(native_input):
    return DafnyDeleteItemInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        Expected=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExpectedAttributeValue(
                            value
                        )
                        for (key, value) in native_input["Expected"].items()
                    }
                )
            )
            if "Expected" in native_input.keys()
            else Option_None()
        ),
        ConditionalOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalOperator(
                    native_input["ConditionalOperator"]
                )
            )
            if "ConditionalOperator" in native_input.keys()
            else Option_None()
        ),
        ReturnValues=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValue(
                    native_input["ReturnValues"]
                )
            )
            if "ReturnValues" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ReturnItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                    native_input["ReturnItemCollectionMetrics"]
                )
            )
            if "ReturnItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExpectedAttributeValue(native_input):
    return DafnyExpectedAttributeValue(
        Value=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    native_input["Value"]
                )
            )
            if "Value" in native_input.keys()
            else Option_None()
        ),
        Exists=(
            Option_Some(native_input["Exists"])
            if "Exists" in native_input.keys()
            else Option_None()
        ),
        ComparisonOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ComparisonOperator(
                    native_input["ComparisonOperator"]
                )
            )
            if "ComparisonOperator" in native_input.keys()
            else Option_None()
        ),
        AttributeValueList=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            list_element
                        )
                        for list_element in native_input["AttributeValueList"]
                    ]
                )
            )
            if "AttributeValueList" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ComparisonOperator(native_input):
    # Convert ComparisonOperator
    if native_input == "EQ":
        return ComparisonOperator_EQ()
    elif native_input == "NE":
        return ComparisonOperator_NE()
    elif native_input == "IN":
        return ComparisonOperator_IN()
    elif native_input == "LE":
        return ComparisonOperator_LE()
    elif native_input == "LT":
        return ComparisonOperator_LT()
    elif native_input == "GE":
        return ComparisonOperator_GE()
    elif native_input == "GT":
        return ComparisonOperator_GT()
    elif native_input == "BETWEEN":
        return ComparisonOperator_BETWEEN()
    elif native_input == "NOT_NULL":
        return ComparisonOperator_NOT__NULL()
    elif native_input == "NULL":
        return ComparisonOperator_NULL()
    elif native_input == "CONTAINS":
        return ComparisonOperator_CONTAINS()
    elif native_input == "NOT_CONTAINS":
        return ComparisonOperator_NOT__CONTAINS()
    elif native_input == "BEGINS_WITH":
        return ComparisonOperator_BEGINS__WITH()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ConditionalOperator(native_input):
    # Convert ConditionalOperator
    if native_input == "AND":
        return ConditionalOperator_AND()
    elif native_input == "OR":
        return ConditionalOperator_OR()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ReturnValue(native_input):
    # Convert ReturnValue
    if native_input == "NONE":
        return ReturnValue_NONE()
    elif native_input == "ALL_OLD":
        return ReturnValue_ALL__OLD()
    elif native_input == "UPDATED_OLD":
        return ReturnValue_UPDATED__OLD()
    elif native_input == "ALL_NEW":
        return ReturnValue_ALL__NEW()
    elif native_input == "UPDATED_NEW":
        return ReturnValue_UPDATED__NEW()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DeleteItemOutput(native_input):
    return DafnyDeleteItemOutput(
        Attributes=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Attributes"].items()
                    }
                )
            )
            if "Attributes" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    native_input["ItemCollectionMetrics"]
                )
            )
            if "ItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DeleteTableInput(native_input):
    return DafnyDeleteTableInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DeleteTableOutput(native_input):
    return DafnyDeleteTableOutput(
        TableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["TableDescription"]
                )
            )
            if "TableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeBackupInput(native_input):
    return DafnyDescribeBackupInput(
        BackupArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeBackupOutput(native_input):
    return DafnyDescribeBackupOutput(
        BackupDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupDescription(
                    native_input["BackupDescription"]
                )
            )
            if "BackupDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeContinuousBackupsInput(native_input):
    return DafnyDescribeContinuousBackupsInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeContinuousBackupsOutput(native_input):
    return DafnyDescribeContinuousBackupsOutput(
        ContinuousBackupsDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                    native_input["ContinuousBackupsDescription"]
                )
            )
            if "ContinuousBackupsDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ContinuousBackupsDescription(native_input):
    return DafnyContinuousBackupsDescription(
        ContinuousBackupsStatus=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContinuousBackupsStatus(
            native_input["ContinuousBackupsStatus"]
        ),
        PointInTimeRecoveryDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PointInTimeRecoveryDescription(
                    native_input["PointInTimeRecoveryDescription"]
                )
            )
            if "PointInTimeRecoveryDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ContinuousBackupsStatus(native_input):
    # Convert ContinuousBackupsStatus
    if native_input == "ENABLED":
        return ContinuousBackupsStatus_ENABLED()
    elif native_input == "DISABLED":
        return ContinuousBackupsStatus_DISABLED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_PointInTimeRecoveryDescription(native_input):
    return DafnyPointInTimeRecoveryDescription(
        PointInTimeRecoveryStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PointInTimeRecoveryStatus(
                    native_input["PointInTimeRecoveryStatus"]
                )
            )
            if "PointInTimeRecoveryStatus" in native_input.keys()
            else Option_None()
        ),
        EarliestRestorableDateTime=(
            Option_Some(
                _dafny.Seq(native_input["EarliestRestorableDateTime"].isoformat())
            )
            if "EarliestRestorableDateTime" in native_input.keys()
            else Option_None()
        ),
        LatestRestorableDateTime=(
            Option_Some(
                _dafny.Seq(native_input["LatestRestorableDateTime"].isoformat())
            )
            if "LatestRestorableDateTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_PointInTimeRecoveryStatus(native_input):
    # Convert PointInTimeRecoveryStatus
    if native_input == "ENABLED":
        return PointInTimeRecoveryStatus_ENABLED()
    elif native_input == "DISABLED":
        return PointInTimeRecoveryStatus_DISABLED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DescribeContributorInsightsInput(native_input):
    return DafnyDescribeContributorInsightsInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeContributorInsightsOutput(native_input):
    return DafnyDescribeContributorInsightsOutput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ContributorInsightsRuleList=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["ContributorInsightsRuleList"]
                    ]
                )
            )
            if "ContributorInsightsRuleList" in native_input.keys()
            else Option_None()
        ),
        ContributorInsightsStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContributorInsightsStatus(
                    native_input["ContributorInsightsStatus"]
                )
            )
            if "ContributorInsightsStatus" in native_input.keys()
            else Option_None()
        ),
        LastUpdateDateTime=(
            Option_Some(_dafny.Seq(native_input["LastUpdateDateTime"].isoformat()))
            if "LastUpdateDateTime" in native_input.keys()
            else Option_None()
        ),
        FailureException=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_FailureException(
                    native_input["FailureException"]
                )
            )
            if "FailureException" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ContributorInsightsStatus(native_input):
    # Convert ContributorInsightsStatus
    if native_input == "ENABLING":
        return ContributorInsightsStatus_ENABLING()
    elif native_input == "ENABLED":
        return ContributorInsightsStatus_ENABLED()
    elif native_input == "DISABLING":
        return ContributorInsightsStatus_DISABLING()
    elif native_input == "DISABLED":
        return ContributorInsightsStatus_DISABLED()
    elif native_input == "FAILED":
        return ContributorInsightsStatus_FAILED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_FailureException(native_input):
    return DafnyFailureException(
        ExceptionName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ExceptionName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExceptionName" in native_input.keys()
            else Option_None()
        ),
        ExceptionDescription=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ExceptionDescription"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExceptionDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeEndpointsRequest(native_input):
    return DafnyDescribeEndpointsRequest()


def com_amazonaws_dynamodb_DescribeEndpointsResponse(native_input):
    return DafnyDescribeEndpointsResponse(
        Endpoints=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Endpoint(
                    list_element
                )
                for list_element in native_input["Endpoints"]
            ]
        ),
    )


def com_amazonaws_dynamodb_Endpoint(native_input):
    return DafnyEndpoint(
        Address=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Address"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        CachePeriodInMinutes=native_input["CachePeriodInMinutes"],
    )


def com_amazonaws_dynamodb_DescribeExportInput(native_input):
    return DafnyDescribeExportInput(
        ExportArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ExportArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeExportOutput(native_input):
    return DafnyDescribeExportOutput(
        ExportDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportDescription(
                    native_input["ExportDescription"]
                )
            )
            if "ExportDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExportDescription(native_input):
    return DafnyExportDescription(
        ExportArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ExportArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExportArn" in native_input.keys()
            else Option_None()
        ),
        ExportStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportStatus(
                    native_input["ExportStatus"]
                )
            )
            if "ExportStatus" in native_input.keys()
            else Option_None()
        ),
        StartTime=(
            Option_Some(_dafny.Seq(native_input["StartTime"].isoformat()))
            if "StartTime" in native_input.keys()
            else Option_None()
        ),
        EndTime=(
            Option_Some(_dafny.Seq(native_input["EndTime"].isoformat()))
            if "EndTime" in native_input.keys()
            else Option_None()
        ),
        ExportManifest=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ExportManifest"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExportManifest" in native_input.keys()
            else Option_None()
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        TableId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "TableId" in native_input.keys()
            else Option_None()
        ),
        ExportTime=(
            Option_Some(_dafny.Seq(native_input["ExportTime"].isoformat()))
            if "ExportTime" in native_input.keys()
            else Option_None()
        ),
        ClientToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ClientToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientToken" in native_input.keys()
            else Option_None()
        ),
        S3Bucket=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["S3Bucket"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3Bucket" in native_input.keys()
            else Option_None()
        ),
        S3BucketOwner=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["S3BucketOwner"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3BucketOwner" in native_input.keys()
            else Option_None()
        ),
        S3Prefix=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["S3Prefix"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3Prefix" in native_input.keys()
            else Option_None()
        ),
        S3SseAlgorithm=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_S3SseAlgorithm(
                    native_input["S3SseAlgorithm"]
                )
            )
            if "S3SseAlgorithm" in native_input.keys()
            else Option_None()
        ),
        S3SseKmsKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["S3SseKmsKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3SseKmsKeyId" in native_input.keys()
            else Option_None()
        ),
        FailureCode=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["FailureCode"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FailureCode" in native_input.keys()
            else Option_None()
        ),
        FailureMessage=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["FailureMessage"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FailureMessage" in native_input.keys()
            else Option_None()
        ),
        ExportFormat=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportFormat(
                    native_input["ExportFormat"]
                )
            )
            if "ExportFormat" in native_input.keys()
            else Option_None()
        ),
        BilledSizeBytes=(
            Option_Some(native_input["BilledSizeBytes"])
            if "BilledSizeBytes" in native_input.keys()
            else Option_None()
        ),
        ItemCount=(
            Option_Some(native_input["ItemCount"])
            if "ItemCount" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExportStatus(native_input):
    # Convert ExportStatus
    if native_input == "IN_PROGRESS":
        return ExportStatus_IN__PROGRESS()
    elif native_input == "COMPLETED":
        return ExportStatus_COMPLETED()
    elif native_input == "FAILED":
        return ExportStatus_FAILED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_S3SseAlgorithm(native_input):
    # Convert S3SseAlgorithm
    if native_input == "AES256":
        return S3SseAlgorithm_AES256()
    elif native_input == "KMS":
        return S3SseAlgorithm_KMS()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ExportFormat(native_input):
    # Convert ExportFormat
    if native_input == "DYNAMODB_JSON":
        return ExportFormat_DYNAMODB__JSON()
    elif native_input == "ION":
        return ExportFormat_ION()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DescribeGlobalTableInput(native_input):
    return DafnyDescribeGlobalTableInput(
        GlobalTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GlobalTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeGlobalTableOutput(native_input):
    return DafnyDescribeGlobalTableOutput(
        GlobalTableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableDescription(
                    native_input["GlobalTableDescription"]
                )
            )
            if "GlobalTableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsInput(native_input):
    return DafnyDescribeGlobalTableSettingsInput(
        GlobalTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GlobalTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsOutput(native_input):
    return DafnyDescribeGlobalTableSettingsOutput(
        GlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableName" in native_input.keys()
            else Option_None()
        ),
        ReplicaSettings=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                            list_element
                        )
                        for list_element in native_input["ReplicaSettings"]
                    ]
                )
            )
            if "ReplicaSettings" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaSettingsDescription(native_input):
    return DafnyReplicaSettingsDescription(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicaStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaStatus(
                    native_input["ReplicaStatus"]
                )
            )
            if "ReplicaStatus" in native_input.keys()
            else Option_None()
        ),
        ReplicaBillingModeSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingModeSummary(
                    native_input["ReplicaBillingModeSummary"]
                )
            )
            if "ReplicaBillingModeSummary" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedReadCapacityUnits=(
            Option_Some(native_input["ReplicaProvisionedReadCapacityUnits"])
            if "ReplicaProvisionedReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedReadCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ReplicaProvisionedReadCapacityAutoScalingSettings"]
                )
            )
            if "ReplicaProvisionedReadCapacityAutoScalingSettings"
            in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedWriteCapacityUnits=(
            Option_Some(native_input["ReplicaProvisionedWriteCapacityUnits"])
            if "ReplicaProvisionedWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedWriteCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
                )
            )
            if "ReplicaProvisionedWriteCapacityAutoScalingSettings"
            in native_input.keys()
            else Option_None()
        ),
        ReplicaGlobalSecondaryIndexSettings=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(
                            list_element
                        )
                        for list_element in native_input[
                            "ReplicaGlobalSecondaryIndexSettings"
                        ]
                    ]
                )
            )
            if "ReplicaGlobalSecondaryIndexSettings" in native_input.keys()
            else Option_None()
        ),
        ReplicaTableClassSummary=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClassSummary(
                    native_input["ReplicaTableClassSummary"]
                )
            )
            if "ReplicaTableClassSummary" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AutoScalingSettingsDescription(native_input):
    return DafnyAutoScalingSettingsDescription(
        MinimumUnits=(
            Option_Some(native_input["MinimumUnits"])
            if "MinimumUnits" in native_input.keys()
            else Option_None()
        ),
        MaximumUnits=(
            Option_Some(native_input["MaximumUnits"])
            if "MaximumUnits" in native_input.keys()
            else Option_None()
        ),
        AutoScalingDisabled=(
            Option_Some(native_input["AutoScalingDisabled"])
            if "AutoScalingDisabled" in native_input.keys()
            else Option_None()
        ),
        AutoScalingRoleArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["AutoScalingRoleArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AutoScalingRoleArn" in native_input.keys()
            else Option_None()
        ),
        ScalingPolicies=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingPolicyDescription(
                            list_element
                        )
                        for list_element in native_input["ScalingPolicies"]
                    ]
                )
            )
            if "ScalingPolicies" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(native_input):
    return DafnyReplicaGlobalSecondaryIndexSettingsDescription(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        IndexStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_IndexStatus(
                    native_input["IndexStatus"]
                )
            )
            if "IndexStatus" in native_input.keys()
            else Option_None()
        ),
        ProvisionedReadCapacityUnits=(
            Option_Some(native_input["ProvisionedReadCapacityUnits"])
            if "ProvisionedReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ProvisionedReadCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ProvisionedReadCapacityAutoScalingSettings"]
                )
            )
            if "ProvisionedReadCapacityAutoScalingSettings" in native_input.keys()
            else Option_None()
        ),
        ProvisionedWriteCapacityUnits=(
            Option_Some(native_input["ProvisionedWriteCapacityUnits"])
            if "ProvisionedWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ProvisionedWriteCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ProvisionedWriteCapacityAutoScalingSettings"]
                )
            )
            if "ProvisionedWriteCapacityAutoScalingSettings" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AutoScalingPolicyDescription(native_input):
    return DafnyAutoScalingPolicyDescription(
        PolicyName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["PolicyName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "PolicyName" in native_input.keys()
            else Option_None()
        ),
        TargetTrackingScalingPolicyConfiguration=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
                    native_input["TargetTrackingScalingPolicyConfiguration"]
                )
            )
            if "TargetTrackingScalingPolicyConfiguration" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
    native_input,
):
    return DafnyAutoScalingTargetTrackingScalingPolicyConfigurationDescription(
        DisableScaleIn=(
            Option_Some(native_input["DisableScaleIn"])
            if "DisableScaleIn" in native_input.keys()
            else Option_None()
        ),
        ScaleInCooldown=(
            Option_Some(native_input["ScaleInCooldown"])
            if "ScaleInCooldown" in native_input.keys()
            else Option_None()
        ),
        ScaleOutCooldown=(
            Option_Some(native_input["ScaleOutCooldown"])
            if "ScaleOutCooldown" in native_input.keys()
            else Option_None()
        ),
        TargetValue=native_input["TargetValue"],
    )


def com_amazonaws_dynamodb_DescribeImportInput(native_input):
    return DafnyDescribeImportInput(
        ImportArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ImportArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeImportOutput(native_input):
    return DafnyDescribeImportOutput(
        ImportTableDescription=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportTableDescription(
            native_input["ImportTableDescription"]
        ),
    )


def com_amazonaws_dynamodb_ImportTableDescription(native_input):
    return DafnyImportTableDescription(
        ImportArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ImportArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ImportArn" in native_input.keys()
            else Option_None()
        ),
        ImportStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportStatus(
                    native_input["ImportStatus"]
                )
            )
            if "ImportStatus" in native_input.keys()
            else Option_None()
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        TableId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "TableId" in native_input.keys()
            else Option_None()
        ),
        ClientToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ClientToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientToken" in native_input.keys()
            else Option_None()
        ),
        S3BucketSource=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_S3BucketSource(
                    native_input["S3BucketSource"]
                )
            )
            if "S3BucketSource" in native_input.keys()
            else Option_None()
        ),
        ErrorCount=(
            Option_Some(native_input["ErrorCount"])
            if "ErrorCount" in native_input.keys()
            else Option_None()
        ),
        CloudWatchLogGroupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudWatchLogGroupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudWatchLogGroupArn" in native_input.keys()
            else Option_None()
        ),
        InputFormat=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputFormat(
                    native_input["InputFormat"]
                )
            )
            if "InputFormat" in native_input.keys()
            else Option_None()
        ),
        InputFormatOptions=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputFormatOptions(
                    native_input["InputFormatOptions"]
                )
            )
            if "InputFormatOptions" in native_input.keys()
            else Option_None()
        ),
        InputCompressionType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputCompressionType(
                    native_input["InputCompressionType"]
                )
            )
            if "InputCompressionType" in native_input.keys()
            else Option_None()
        ),
        TableCreationParameters=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableCreationParameters(
                    native_input["TableCreationParameters"]
                )
            )
            if "TableCreationParameters" in native_input.keys()
            else Option_None()
        ),
        StartTime=(
            Option_Some(_dafny.Seq(native_input["StartTime"].isoformat()))
            if "StartTime" in native_input.keys()
            else Option_None()
        ),
        EndTime=(
            Option_Some(_dafny.Seq(native_input["EndTime"].isoformat()))
            if "EndTime" in native_input.keys()
            else Option_None()
        ),
        ProcessedSizeBytes=(
            Option_Some(native_input["ProcessedSizeBytes"])
            if "ProcessedSizeBytes" in native_input.keys()
            else Option_None()
        ),
        ProcessedItemCount=(
            Option_Some(native_input["ProcessedItemCount"])
            if "ProcessedItemCount" in native_input.keys()
            else Option_None()
        ),
        ImportedItemCount=(
            Option_Some(native_input["ImportedItemCount"])
            if "ImportedItemCount" in native_input.keys()
            else Option_None()
        ),
        FailureCode=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["FailureCode"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FailureCode" in native_input.keys()
            else Option_None()
        ),
        FailureMessage=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["FailureMessage"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FailureMessage" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ImportStatus(native_input):
    # Convert ImportStatus
    if native_input == "IN_PROGRESS":
        return ImportStatus_IN__PROGRESS()
    elif native_input == "COMPLETED":
        return ImportStatus_COMPLETED()
    elif native_input == "CANCELLING":
        return ImportStatus_CANCELLING()
    elif native_input == "CANCELLED":
        return ImportStatus_CANCELLED()
    elif native_input == "FAILED":
        return ImportStatus_FAILED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_S3BucketSource(native_input):
    return DafnyS3BucketSource(
        S3BucketOwner=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["S3BucketOwner"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3BucketOwner" in native_input.keys()
            else Option_None()
        ),
        S3Bucket=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["S3Bucket"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        S3KeyPrefix=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["S3KeyPrefix"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3KeyPrefix" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_InputFormat(native_input):
    # Convert InputFormat
    if native_input == "DYNAMODB_JSON":
        return InputFormat_DYNAMODB__JSON()
    elif native_input == "ION":
        return InputFormat_ION()
    elif native_input == "CSV":
        return InputFormat_CSV()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_InputFormatOptions(native_input):
    return DafnyInputFormatOptions(
        Csv=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CsvOptions(
                    native_input["Csv"]
                )
            )
            if "Csv" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_InputCompressionType(native_input):
    # Convert InputCompressionType
    if native_input == "GZIP":
        return InputCompressionType_GZIP()
    elif native_input == "ZSTD":
        return InputCompressionType_ZSTD()
    elif native_input == "NONE":
        return InputCompressionType_NONE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_TableCreationParameters(native_input):
    return DafnyTableCreationParameters(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        AttributeDefinitions=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeDefinition(
                    list_element
                )
                for list_element in native_input["AttributeDefinitions"]
            ]
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        BillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingMode"]
                )
            )
            if "BillingMode" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
        SSESpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSESpecification(
                    native_input["SSESpecification"]
                )
            )
            if "SSESpecification" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_CsvOptions(native_input):
    return DafnyCsvOptions(
        Delimiter=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["Delimiter"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "Delimiter" in native_input.keys()
            else Option_None()
        ),
        HeaderList=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["HeaderList"]
                    ]
                )
            )
            if "HeaderList" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationInput(native_input):
    return DafnyDescribeKinesisStreamingDestinationInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationOutput(native_input):
    return DafnyDescribeKinesisStreamingDestinationOutput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        KinesisDataStreamDestinations=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KinesisDataStreamDestination(
                            list_element
                        )
                        for list_element in native_input[
                            "KinesisDataStreamDestinations"
                        ]
                    ]
                )
            )
            if "KinesisDataStreamDestinations" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_KinesisDataStreamDestination(native_input):
    return DafnyKinesisDataStreamDestination(
        StreamArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["StreamArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "StreamArn" in native_input.keys()
            else Option_None()
        ),
        DestinationStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DestinationStatus(
                    native_input["DestinationStatus"]
                )
            )
            if "DestinationStatus" in native_input.keys()
            else Option_None()
        ),
        DestinationStatusDescription=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "DestinationStatusDescription"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "DestinationStatusDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DestinationStatus(native_input):
    # Convert DestinationStatus
    if native_input == "ENABLING":
        return DestinationStatus_ENABLING()
    elif native_input == "ACTIVE":
        return DestinationStatus_ACTIVE()
    elif native_input == "DISABLING":
        return DestinationStatus_DISABLING()
    elif native_input == "DISABLED":
        return DestinationStatus_DISABLED()
    elif native_input == "ENABLE_FAILED":
        return DestinationStatus_ENABLE__FAILED()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_DescribeLimitsInput(native_input):
    return DafnyDescribeLimitsInput()


def com_amazonaws_dynamodb_DescribeLimitsOutput(native_input):
    return DafnyDescribeLimitsOutput(
        AccountMaxReadCapacityUnits=(
            Option_Some(native_input["AccountMaxReadCapacityUnits"])
            if "AccountMaxReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        AccountMaxWriteCapacityUnits=(
            Option_Some(native_input["AccountMaxWriteCapacityUnits"])
            if "AccountMaxWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        TableMaxReadCapacityUnits=(
            Option_Some(native_input["TableMaxReadCapacityUnits"])
            if "TableMaxReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        TableMaxWriteCapacityUnits=(
            Option_Some(native_input["TableMaxWriteCapacityUnits"])
            if "TableMaxWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeTableInput(native_input):
    return DafnyDescribeTableInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeTableOutput(native_input):
    return DafnyDescribeTableOutput(
        Table=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["Table"]
                )
            )
            if "Table" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingInput(native_input):
    return DafnyDescribeTableReplicaAutoScalingInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingOutput(native_input):
    return DafnyDescribeTableReplicaAutoScalingOutput(
        TableAutoScalingDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableAutoScalingDescription(
                    native_input["TableAutoScalingDescription"]
                )
            )
            if "TableAutoScalingDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TableAutoScalingDescription(native_input):
    return DafnyTableAutoScalingDescription(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        TableStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableStatus(
                    native_input["TableStatus"]
                )
            )
            if "TableStatus" in native_input.keys()
            else Option_None()
        ),
        Replicas=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaAutoScalingDescription(
                            list_element
                        )
                        for list_element in native_input["Replicas"]
                    ]
                )
            )
            if "Replicas" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaAutoScalingDescription(native_input):
    return DafnyReplicaAutoScalingDescription(
        RegionName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["RegionName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RegionName" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedReadCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ReplicaProvisionedReadCapacityAutoScalingSettings"]
                )
            )
            if "ReplicaProvisionedReadCapacityAutoScalingSettings"
            in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedWriteCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
                )
            )
            if "ReplicaProvisionedWriteCapacityAutoScalingSettings"
            in native_input.keys()
            else Option_None()
        ),
        ReplicaStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaStatus(
                    native_input["ReplicaStatus"]
                )
            )
            if "ReplicaStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
    native_input,
):
    return DafnyReplicaGlobalSecondaryIndexAutoScalingDescription(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        IndexStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_IndexStatus(
                    native_input["IndexStatus"]
                )
            )
            if "IndexStatus" in native_input.keys()
            else Option_None()
        ),
        ProvisionedReadCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ProvisionedReadCapacityAutoScalingSettings"]
                )
            )
            if "ProvisionedReadCapacityAutoScalingSettings" in native_input.keys()
            else Option_None()
        ),
        ProvisionedWriteCapacityAutoScalingSettings=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                    native_input["ProvisionedWriteCapacityAutoScalingSettings"]
                )
            )
            if "ProvisionedWriteCapacityAutoScalingSettings" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DescribeTimeToLiveInput(native_input):
    return DafnyDescribeTimeToLiveInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DescribeTimeToLiveOutput(native_input):
    return DafnyDescribeTimeToLiveOutput(
        TimeToLiveDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TimeToLiveDescription(
                    native_input["TimeToLiveDescription"]
                )
            )
            if "TimeToLiveDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationInput(native_input):
    return DafnyDisableKinesisStreamingDestinationInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        StreamArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["StreamArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationOutput(native_input):
    return DafnyDisableKinesisStreamingDestinationOutput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        StreamArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["StreamArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "StreamArn" in native_input.keys()
            else Option_None()
        ),
        DestinationStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DestinationStatus(
                    native_input["DestinationStatus"]
                )
            )
            if "DestinationStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationInput(native_input):
    return DafnyEnableKinesisStreamingDestinationInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        StreamArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["StreamArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationOutput(native_input):
    return DafnyEnableKinesisStreamingDestinationOutput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        StreamArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["StreamArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "StreamArn" in native_input.keys()
            else Option_None()
        ),
        DestinationStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DestinationStatus(
                    native_input["DestinationStatus"]
                )
            )
            if "DestinationStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExecuteStatementInput(native_input):
    return DafnyExecuteStatementInput(
        Statement=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Statement"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Parameters=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            list_element
                        )
                        for list_element in native_input["Parameters"]
                    ]
                )
            )
            if "Parameters" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExecuteStatementOutput(native_input):
    return DafnyExecuteStatementOutput(
        Items=(
            Option_Some(
                Seq(
                    [
                        Map(
                            {
                                Seq(
                                    "".join(
                                        [
                                            chr(int.from_bytes(pair, "big"))
                                            for pair in zip(
                                                *[iter(key.encode("utf-16-be"))] * 2
                                            )
                                        ]
                                    )
                                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                                    value
                                )
                                for (key, value) in list_element.items()
                            }
                        )
                        for list_element in native_input["Items"]
                    ]
                )
            )
            if "Items" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["LastEvaluatedKey"].items()
                    }
                )
            )
            if "LastEvaluatedKey" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExecuteTransactionInput(native_input):
    return DafnyExecuteTransactionInput(
        TransactStatements=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ParameterizedStatement(
                    list_element
                )
                for list_element in native_input["TransactStatements"]
            ]
        ),
        ClientRequestToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ClientRequestToken"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientRequestToken" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ParameterizedStatement(native_input):
    return DafnyParameterizedStatement(
        Statement=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["Statement"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Parameters=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            list_element
                        )
                        for list_element in native_input["Parameters"]
                    ]
                )
            )
            if "Parameters" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExecuteTransactionOutput(native_input):
    return DafnyExecuteTransactionOutput(
        Responses=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemResponse(
                            list_element
                        )
                        for list_element in native_input["Responses"]
                    ]
                )
            )
            if "Responses" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ItemResponse(native_input):
    return DafnyItemResponse(
        Item=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Item"].items()
                    }
                )
            )
            if "Item" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExportTableToPointInTimeInput(native_input):
    return DafnyExportTableToPointInTimeInput(
        TableArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ExportTime=(
            Option_Some(_dafny.Seq(native_input["ExportTime"].isoformat()))
            if "ExportTime" in native_input.keys()
            else Option_None()
        ),
        ClientToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ClientToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientToken" in native_input.keys()
            else Option_None()
        ),
        S3Bucket=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["S3Bucket"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        S3BucketOwner=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["S3BucketOwner"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3BucketOwner" in native_input.keys()
            else Option_None()
        ),
        S3Prefix=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["S3Prefix"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3Prefix" in native_input.keys()
            else Option_None()
        ),
        S3SseAlgorithm=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_S3SseAlgorithm(
                    native_input["S3SseAlgorithm"]
                )
            )
            if "S3SseAlgorithm" in native_input.keys()
            else Option_None()
        ),
        S3SseKmsKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["S3SseKmsKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "S3SseKmsKeyId" in native_input.keys()
            else Option_None()
        ),
        ExportFormat=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportFormat(
                    native_input["ExportFormat"]
                )
            )
            if "ExportFormat" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExportTableToPointInTimeOutput(native_input):
    return DafnyExportTableToPointInTimeOutput(
        ExportDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportDescription(
                    native_input["ExportDescription"]
                )
            )
            if "ExportDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GetItemInput(native_input):
    return DafnyGetItemInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        AttributesToGet=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["AttributesToGet"]
                    ]
                )
            )
            if "AttributesToGet" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ProjectionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ProjectionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ProjectionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GetItemOutput(native_input):
    return DafnyGetItemOutput(
        Item=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Item"].items()
                    }
                )
            )
            if "Item" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ImportTableInput(native_input):
    return DafnyImportTableInput(
        ClientToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ClientToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientToken" in native_input.keys()
            else Option_None()
        ),
        S3BucketSource=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_S3BucketSource(
            native_input["S3BucketSource"]
        ),
        InputFormat=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputFormat(
            native_input["InputFormat"]
        ),
        InputFormatOptions=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputFormatOptions(
                    native_input["InputFormatOptions"]
                )
            )
            if "InputFormatOptions" in native_input.keys()
            else Option_None()
        ),
        InputCompressionType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputCompressionType(
                    native_input["InputCompressionType"]
                )
            )
            if "InputCompressionType" in native_input.keys()
            else Option_None()
        ),
        TableCreationParameters=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableCreationParameters(
            native_input["TableCreationParameters"]
        ),
    )


def com_amazonaws_dynamodb_ImportTableOutput(native_input):
    return DafnyImportTableOutput(
        ImportTableDescription=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportTableDescription(
            native_input["ImportTableDescription"]
        ),
    )


def com_amazonaws_dynamodb_ListBackupsInput(native_input):
    return DafnyListBackupsInput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        TimeRangeLowerBound=(
            Option_Some(_dafny.Seq(native_input["TimeRangeLowerBound"].isoformat()))
            if "TimeRangeLowerBound" in native_input.keys()
            else Option_None()
        ),
        TimeRangeUpperBound=(
            Option_Some(_dafny.Seq(native_input["TimeRangeUpperBound"].isoformat()))
            if "TimeRangeUpperBound" in native_input.keys()
            else Option_None()
        ),
        ExclusiveStartBackupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ExclusiveStartBackupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExclusiveStartBackupArn" in native_input.keys()
            else Option_None()
        ),
        BackupType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupTypeFilter(
                    native_input["BackupType"]
                )
            )
            if "BackupType" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BackupTypeFilter(native_input):
    # Convert BackupTypeFilter
    if native_input == "USER":
        return BackupTypeFilter_USER()
    elif native_input == "SYSTEM":
        return BackupTypeFilter_SYSTEM()
    elif native_input == "AWS_BACKUP":
        return BackupTypeFilter_AWS__BACKUP()
    elif native_input == "ALL":
        return BackupTypeFilter_ALL()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_ListBackupsOutput(native_input):
    return DafnyListBackupsOutput(
        BackupSummaries=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupSummary(
                            list_element
                        )
                        for list_element in native_input["BackupSummaries"]
                    ]
                )
            )
            if "BackupSummaries" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedBackupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["LastEvaluatedBackupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "LastEvaluatedBackupArn" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_BackupSummary(native_input):
    return DafnyBackupSummary(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        TableId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableId"].encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
            )
            if "TableId" in native_input.keys()
            else Option_None()
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        BackupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["BackupArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "BackupArn" in native_input.keys()
            else Option_None()
        ),
        BackupName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["BackupName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "BackupName" in native_input.keys()
            else Option_None()
        ),
        BackupCreationDateTime=(
            Option_Some(_dafny.Seq(native_input["BackupCreationDateTime"].isoformat()))
            if "BackupCreationDateTime" in native_input.keys()
            else Option_None()
        ),
        BackupExpiryDateTime=(
            Option_Some(_dafny.Seq(native_input["BackupExpiryDateTime"].isoformat()))
            if "BackupExpiryDateTime" in native_input.keys()
            else Option_None()
        ),
        BackupStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupStatus(
                    native_input["BackupStatus"]
                )
            )
            if "BackupStatus" in native_input.keys()
            else Option_None()
        ),
        BackupType=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BackupType(
                    native_input["BackupType"]
                )
            )
            if "BackupType" in native_input.keys()
            else Option_None()
        ),
        BackupSizeBytes=(
            Option_Some(native_input["BackupSizeBytes"])
            if "BackupSizeBytes" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListContributorInsightsInput(native_input):
    return DafnyListContributorInsightsInput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
        MaxResults=(
            Option_Some(native_input["MaxResults"])
            if "MaxResults" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListContributorInsightsOutput(native_input):
    return DafnyListContributorInsightsOutput(
        ContributorInsightsSummaries=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContributorInsightsSummary(
                            list_element
                        )
                        for list_element in native_input["ContributorInsightsSummaries"]
                    ]
                )
            )
            if "ContributorInsightsSummaries" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ContributorInsightsSummary(native_input):
    return DafnyContributorInsightsSummary(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ContributorInsightsStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContributorInsightsStatus(
                    native_input["ContributorInsightsStatus"]
                )
            )
            if "ContributorInsightsStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListExportsInput(native_input):
    return DafnyListExportsInput(
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        MaxResults=(
            Option_Some(native_input["MaxResults"])
            if "MaxResults" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListExportsOutput(native_input):
    return DafnyListExportsOutput(
        ExportSummaries=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportSummary(
                            list_element
                        )
                        for list_element in native_input["ExportSummaries"]
                    ]
                )
            )
            if "ExportSummaries" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ExportSummary(native_input):
    return DafnyExportSummary(
        ExportArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ExportArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExportArn" in native_input.keys()
            else Option_None()
        ),
        ExportStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExportStatus(
                    native_input["ExportStatus"]
                )
            )
            if "ExportStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListGlobalTablesInput(native_input):
    return DafnyListGlobalTablesInput(
        ExclusiveStartGlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "ExclusiveStartGlobalTableName"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExclusiveStartGlobalTableName" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        RegionName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["RegionName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "RegionName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListGlobalTablesOutput(native_input):
    return DafnyListGlobalTablesOutput(
        GlobalTables=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTable(
                            list_element
                        )
                        for list_element in native_input["GlobalTables"]
                    ]
                )
            )
            if "GlobalTables" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedGlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input[
                                            "LastEvaluatedGlobalTableName"
                                        ].encode("utf-16-be")
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "LastEvaluatedGlobalTableName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalTable(native_input):
    return DafnyGlobalTable(
        GlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableName" in native_input.keys()
            else Option_None()
        ),
        ReplicationGroup=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Replica(
                            list_element
                        )
                        for list_element in native_input["ReplicationGroup"]
                    ]
                )
            )
            if "ReplicationGroup" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListImportsInput(native_input):
    return DafnyListImportsInput(
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        PageSize=(
            Option_Some(native_input["PageSize"])
            if "PageSize" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListImportsOutput(native_input):
    return DafnyListImportsOutput(
        ImportSummaryList=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportSummary(
                            list_element
                        )
                        for list_element in native_input["ImportSummaryList"]
                    ]
                )
            )
            if "ImportSummaryList" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ImportSummary(native_input):
    return DafnyImportSummary(
        ImportArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["ImportArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ImportArn" in native_input.keys()
            else Option_None()
        ),
        ImportStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ImportStatus(
                    native_input["ImportStatus"]
                )
            )
            if "ImportStatus" in native_input.keys()
            else Option_None()
        ),
        TableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableArn"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableArn" in native_input.keys()
            else Option_None()
        ),
        S3BucketSource=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_S3BucketSource(
                    native_input["S3BucketSource"]
                )
            )
            if "S3BucketSource" in native_input.keys()
            else Option_None()
        ),
        CloudWatchLogGroupArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["CloudWatchLogGroupArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "CloudWatchLogGroupArn" in native_input.keys()
            else Option_None()
        ),
        InputFormat=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_InputFormat(
                    native_input["InputFormat"]
                )
            )
            if "InputFormat" in native_input.keys()
            else Option_None()
        ),
        StartTime=(
            Option_Some(_dafny.Seq(native_input["StartTime"].isoformat()))
            if "StartTime" in native_input.keys()
            else Option_None()
        ),
        EndTime=(
            Option_Some(_dafny.Seq(native_input["EndTime"].isoformat()))
            if "EndTime" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListTablesInput(native_input):
    return DafnyListTablesInput(
        ExclusiveStartTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ExclusiveStartTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ExclusiveStartTableName" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListTablesOutput(native_input):
    return DafnyListTablesOutput(
        TableNames=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["TableNames"]
                    ]
                )
            )
            if "TableNames" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["LastEvaluatedTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "LastEvaluatedTableName" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListTagsOfResourceInput(native_input):
    return DafnyListTagsOfResourceInput(
        ResourceArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ResourceArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ListTagsOfResourceOutput(native_input):
    return DafnyListTagsOfResourceOutput(
        Tags=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Tag(
                            list_element
                        )
                        for list_element in native_input["Tags"]
                    ]
                )
            )
            if "Tags" in native_input.keys()
            else Option_None()
        ),
        NextToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["NextToken"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "NextToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_PutItemInput(native_input):
    return DafnyPutItemInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Item=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Item"].items()
            }
        ),
        Expected=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExpectedAttributeValue(
                            value
                        )
                        for (key, value) in native_input["Expected"].items()
                    }
                )
            )
            if "Expected" in native_input.keys()
            else Option_None()
        ),
        ReturnValues=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValue(
                    native_input["ReturnValues"]
                )
            )
            if "ReturnValues" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ReturnItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                    native_input["ReturnItemCollectionMetrics"]
                )
            )
            if "ReturnItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
        ConditionalOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalOperator(
                    native_input["ConditionalOperator"]
                )
            )
            if "ConditionalOperator" in native_input.keys()
            else Option_None()
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_PutItemOutput(native_input):
    return DafnyPutItemOutput(
        Attributes=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Attributes"].items()
                    }
                )
            )
            if "Attributes" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    native_input["ItemCollectionMetrics"]
                )
            )
            if "ItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_QueryInput(native_input):
    return DafnyQueryInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        Select=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Select(
                    native_input["Select"]
                )
            )
            if "Select" in native_input.keys()
            else Option_None()
        ),
        AttributesToGet=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["AttributesToGet"]
                    ]
                )
            )
            if "AttributesToGet" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
        KeyConditions=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Condition(
                            value
                        )
                        for (key, value) in native_input["KeyConditions"].items()
                    }
                )
            )
            if "KeyConditions" in native_input.keys()
            else Option_None()
        ),
        QueryFilter=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Condition(
                            value
                        )
                        for (key, value) in native_input["QueryFilter"].items()
                    }
                )
            )
            if "QueryFilter" in native_input.keys()
            else Option_None()
        ),
        ConditionalOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalOperator(
                    native_input["ConditionalOperator"]
                )
            )
            if "ConditionalOperator" in native_input.keys()
            else Option_None()
        ),
        ScanIndexForward=(
            Option_Some(native_input["ScanIndexForward"])
            if "ScanIndexForward" in native_input.keys()
            else Option_None()
        ),
        ExclusiveStartKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["ExclusiveStartKey"].items()
                    }
                )
            )
            if "ExclusiveStartKey" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ProjectionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ProjectionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ProjectionExpression" in native_input.keys()
            else Option_None()
        ),
        FilterExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["FilterExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FilterExpression" in native_input.keys()
            else Option_None()
        ),
        KeyConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KeyConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KeyConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_Select(native_input):
    # Convert Select
    if native_input == "ALL_ATTRIBUTES":
        return Select_ALL__ATTRIBUTES()
    elif native_input == "ALL_PROJECTED_ATTRIBUTES":
        return Select_ALL__PROJECTED__ATTRIBUTES()
    elif native_input == "SPECIFIC_ATTRIBUTES":
        return Select_SPECIFIC__ATTRIBUTES()
    elif native_input == "COUNT":
        return Select_COUNT()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_Condition(native_input):
    return DafnyCondition(
        AttributeValueList=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            list_element
                        )
                        for list_element in native_input["AttributeValueList"]
                    ]
                )
            )
            if "AttributeValueList" in native_input.keys()
            else Option_None()
        ),
        ComparisonOperator=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ComparisonOperator(
            native_input["ComparisonOperator"]
        ),
    )


def com_amazonaws_dynamodb_QueryOutput(native_input):
    return DafnyQueryOutput(
        Items=(
            Option_Some(
                Seq(
                    [
                        Map(
                            {
                                Seq(
                                    "".join(
                                        [
                                            chr(int.from_bytes(pair, "big"))
                                            for pair in zip(
                                                *[iter(key.encode("utf-16-be"))] * 2
                                            )
                                        ]
                                    )
                                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                                    value
                                )
                                for (key, value) in list_element.items()
                            }
                        )
                        for list_element in native_input["Items"]
                    ]
                )
            )
            if "Items" in native_input.keys()
            else Option_None()
        ),
        Count=(
            Option_Some(native_input["Count"])
            if "Count" in native_input.keys()
            else Option_None()
        ),
        ScannedCount=(
            Option_Some(native_input["ScannedCount"])
            if "ScannedCount" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["LastEvaluatedKey"].items()
                    }
                )
            )
            if "LastEvaluatedKey" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_RestoreTableFromBackupInput(native_input):
    return DafnyRestoreTableFromBackupInput(
        TargetTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TargetTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BackupArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["BackupArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BillingModeOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingModeOverride"]
                )
            )
            if "BillingModeOverride" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexOverride=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexOverride"]
                    ]
                )
            )
            if "GlobalSecondaryIndexOverride" in native_input.keys()
            else Option_None()
        ),
        LocalSecondaryIndexOverride=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LocalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["LocalSecondaryIndexOverride"]
                    ]
                )
            )
            if "LocalSecondaryIndexOverride" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
        SSESpecificationOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSESpecification(
                    native_input["SSESpecificationOverride"]
                )
            )
            if "SSESpecificationOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_RestoreTableFromBackupOutput(native_input):
    return DafnyRestoreTableFromBackupOutput(
        TableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["TableDescription"]
                )
            )
            if "TableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_RestoreTableToPointInTimeInput(native_input):
    return DafnyRestoreTableToPointInTimeInput(
        SourceTableArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["SourceTableArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceTableArn" in native_input.keys()
            else Option_None()
        ),
        SourceTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["SourceTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "SourceTableName" in native_input.keys()
            else Option_None()
        ),
        TargetTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TargetTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        UseLatestRestorableTime=(
            Option_Some(native_input["UseLatestRestorableTime"])
            if "UseLatestRestorableTime" in native_input.keys()
            else Option_None()
        ),
        RestoreDateTime=(
            Option_Some(_dafny.Seq(native_input["RestoreDateTime"].isoformat()))
            if "RestoreDateTime" in native_input.keys()
            else Option_None()
        ),
        BillingModeOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingModeOverride"]
                )
            )
            if "BillingModeOverride" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexOverride=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexOverride"]
                    ]
                )
            )
            if "GlobalSecondaryIndexOverride" in native_input.keys()
            else Option_None()
        ),
        LocalSecondaryIndexOverride=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_LocalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["LocalSecondaryIndexOverride"]
                    ]
                )
            )
            if "LocalSecondaryIndexOverride" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
        SSESpecificationOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSESpecification(
                    native_input["SSESpecificationOverride"]
                )
            )
            if "SSESpecificationOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_RestoreTableToPointInTimeOutput(native_input):
    return DafnyRestoreTableToPointInTimeOutput(
        TableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["TableDescription"]
                )
            )
            if "TableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ScanInput(native_input):
    return DafnyScanInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        AttributesToGet=(
            Option_Some(
                Seq(
                    [
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(list_element.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for list_element in native_input["AttributesToGet"]
                    ]
                )
            )
            if "AttributesToGet" in native_input.keys()
            else Option_None()
        ),
        Limit=(
            Option_Some(native_input["Limit"])
            if "Limit" in native_input.keys()
            else Option_None()
        ),
        Select=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Select(
                    native_input["Select"]
                )
            )
            if "Select" in native_input.keys()
            else Option_None()
        ),
        ScanFilter=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Condition(
                            value
                        )
                        for (key, value) in native_input["ScanFilter"].items()
                    }
                )
            )
            if "ScanFilter" in native_input.keys()
            else Option_None()
        ),
        ConditionalOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalOperator(
                    native_input["ConditionalOperator"]
                )
            )
            if "ConditionalOperator" in native_input.keys()
            else Option_None()
        ),
        ExclusiveStartKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["ExclusiveStartKey"].items()
                    }
                )
            )
            if "ExclusiveStartKey" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        TotalSegments=(
            Option_Some(native_input["TotalSegments"])
            if "TotalSegments" in native_input.keys()
            else Option_None()
        ),
        Segment=(
            Option_Some(native_input["Segment"])
            if "Segment" in native_input.keys()
            else Option_None()
        ),
        ProjectionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ProjectionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ProjectionExpression" in native_input.keys()
            else Option_None()
        ),
        FilterExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["FilterExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "FilterExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
        ConsistentRead=(
            Option_Some(native_input["ConsistentRead"])
            if "ConsistentRead" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ScanOutput(native_input):
    return DafnyScanOutput(
        Items=(
            Option_Some(
                Seq(
                    [
                        Map(
                            {
                                Seq(
                                    "".join(
                                        [
                                            chr(int.from_bytes(pair, "big"))
                                            for pair in zip(
                                                *[iter(key.encode("utf-16-be"))] * 2
                                            )
                                        ]
                                    )
                                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                                    value
                                )
                                for (key, value) in list_element.items()
                            }
                        )
                        for list_element in native_input["Items"]
                    ]
                )
            )
            if "Items" in native_input.keys()
            else Option_None()
        ),
        Count=(
            Option_Some(native_input["Count"])
            if "Count" in native_input.keys()
            else Option_None()
        ),
        ScannedCount=(
            Option_Some(native_input["ScannedCount"])
            if "ScannedCount" in native_input.keys()
            else Option_None()
        ),
        LastEvaluatedKey=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["LastEvaluatedKey"].items()
                    }
                )
            )
            if "LastEvaluatedKey" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TagResourceInput(native_input):
    return DafnyTagResourceInput(
        ResourceArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ResourceArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Tags=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Tag(
                    list_element
                )
                for list_element in native_input["Tags"]
            ]
        ),
    )


def com_amazonaws_dynamodb_TransactGetItemsInput(native_input):
    return DafnyTransactGetItemsInput(
        TransactItems=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactGetItem(
                    list_element
                )
                for list_element in native_input["TransactItems"]
            ]
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TransactGetItem(native_input):
    return DafnyTransactGetItem(
        Get=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Get(
            native_input["Get"]
        ),
    )


def com_amazonaws_dynamodb_Get(native_input):
    return DafnyGet(
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProjectionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ProjectionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ProjectionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TransactGetItemsOutput(native_input):
    return DafnyTransactGetItemsOutput(
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        Responses=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemResponse(
                            list_element
                        )
                        for list_element in native_input["Responses"]
                    ]
                )
            )
            if "Responses" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TransactWriteItemsInput(native_input):
    return DafnyTransactWriteItemsInput(
        TransactItems=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TransactWriteItem(
                    list_element
                )
                for list_element in native_input["TransactItems"]
            ]
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ReturnItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                    native_input["ReturnItemCollectionMetrics"]
                )
            )
            if "ReturnItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
        ClientRequestToken=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ClientRequestToken"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ClientRequestToken" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_TransactWriteItem(native_input):
    return DafnyTransactWriteItem(
        ConditionCheck=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionCheck(
                    native_input["ConditionCheck"]
                )
            )
            if "ConditionCheck" in native_input.keys()
            else Option_None()
        ),
        Put=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Put(
                    native_input["Put"]
                )
            )
            if "Put" in native_input.keys()
            else Option_None()
        ),
        Delete=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Delete(
                    native_input["Delete"]
                )
            )
            if "Delete" in native_input.keys()
            else Option_None()
        ),
        Update=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Update(
                    native_input["Update"]
                )
            )
            if "Update" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ConditionCheck(native_input):
    return DafnyConditionCheck(
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ConditionExpression=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ConditionExpression"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
        ReturnValuesOnConditionCheckFailure=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                    native_input["ReturnValuesOnConditionCheckFailure"]
                )
            )
            if "ReturnValuesOnConditionCheckFailure" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_Put(native_input):
    return DafnyPut(
        Item=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Item"].items()
            }
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
        ReturnValuesOnConditionCheckFailure=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                    native_input["ReturnValuesOnConditionCheckFailure"]
                )
            )
            if "ReturnValuesOnConditionCheckFailure" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_Delete(native_input):
    return DafnyDelete(
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
        ReturnValuesOnConditionCheckFailure=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                    native_input["ReturnValuesOnConditionCheckFailure"]
                )
            )
            if "ReturnValuesOnConditionCheckFailure" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_Update(native_input):
    return DafnyUpdate(
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        UpdateExpression=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["UpdateExpression"].encode("utf-16-be"))]
                        * 2
                    )
                ]
            )
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
        ReturnValuesOnConditionCheckFailure=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                    native_input["ReturnValuesOnConditionCheckFailure"]
                )
            )
            if "ReturnValuesOnConditionCheckFailure" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(native_input):
    # Convert ReturnValuesOnConditionCheckFailure
    if native_input == "ALL_OLD":
        return ReturnValuesOnConditionCheckFailure_ALL__OLD()
    elif native_input == "NONE":
        return ReturnValuesOnConditionCheckFailure_NONE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_TransactWriteItemsOutput(native_input):
    return DafnyTransactWriteItemsOutput(
        ConsumedCapacity=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                            list_element
                        )
                        for list_element in native_input["ConsumedCapacity"]
                    ]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ItemCollectionMetrics=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            [
                                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionMetrics(
                                    list_element
                                )
                                for list_element in value
                            ]
                        )
                        for (key, value) in native_input[
                            "ItemCollectionMetrics"
                        ].items()
                    }
                )
            )
            if "ItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UntagResourceInput(native_input):
    return DafnyUntagResourceInput(
        ResourceArn=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["ResourceArn"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TagKeys=Seq(
            [
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(list_element.encode("utf-16-be"))] * 2
                            )
                        ]
                    )
                )
                for list_element in native_input["TagKeys"]
            ]
        ),
    )


def com_amazonaws_dynamodb_UpdateContinuousBackupsInput(native_input):
    return DafnyUpdateContinuousBackupsInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        PointInTimeRecoverySpecification=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_PointInTimeRecoverySpecification(
            native_input["PointInTimeRecoverySpecification"]
        ),
    )


def com_amazonaws_dynamodb_PointInTimeRecoverySpecification(native_input):
    return DafnyPointInTimeRecoverySpecification(
        PointInTimeRecoveryEnabled=native_input["PointInTimeRecoveryEnabled"],
    )


def com_amazonaws_dynamodb_UpdateContinuousBackupsOutput(native_input):
    return DafnyUpdateContinuousBackupsOutput(
        ContinuousBackupsDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                    native_input["ContinuousBackupsDescription"]
                )
            )
            if "ContinuousBackupsDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateContributorInsightsInput(native_input):
    return DafnyUpdateContributorInsightsInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ContributorInsightsAction=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContributorInsightsAction(
            native_input["ContributorInsightsAction"]
        ),
    )


def com_amazonaws_dynamodb_ContributorInsightsAction(native_input):
    # Convert ContributorInsightsAction
    if native_input == "ENABLE":
        return ContributorInsightsAction_ENABLE()
    elif native_input == "DISABLE":
        return ContributorInsightsAction_DISABLE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_UpdateContributorInsightsOutput(native_input):
    return DafnyUpdateContributorInsightsOutput(
        TableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["TableName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "TableName" in native_input.keys()
            else Option_None()
        ),
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ContributorInsightsStatus=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ContributorInsightsStatus(
                    native_input["ContributorInsightsStatus"]
                )
            )
            if "ContributorInsightsStatus" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateGlobalTableInput(native_input):
    return DafnyUpdateGlobalTableInput(
        GlobalTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GlobalTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicaUpdates=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaUpdate(
                    list_element
                )
                for list_element in native_input["ReplicaUpdates"]
            ]
        ),
    )


def com_amazonaws_dynamodb_ReplicaUpdate(native_input):
    return DafnyReplicaUpdate(
        Create=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateReplicaAction(
                    native_input["Create"]
                )
            )
            if "Create" in native_input.keys()
            else Option_None()
        ),
        Delete=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteReplicaAction(
                    native_input["Delete"]
                )
            )
            if "Delete" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_CreateReplicaAction(native_input):
    return DafnyCreateReplicaAction(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_DeleteReplicaAction(native_input):
    return DafnyDeleteReplicaAction(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_UpdateGlobalTableOutput(native_input):
    return DafnyUpdateGlobalTableOutput(
        GlobalTableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableDescription(
                    native_input["GlobalTableDescription"]
                )
            )
            if "GlobalTableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsInput(native_input):
    return DafnyUpdateGlobalTableSettingsInput(
        GlobalTableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["GlobalTableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        GlobalTableBillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["GlobalTableBillingMode"]
                )
            )
            if "GlobalTableBillingMode" in native_input.keys()
            else Option_None()
        ),
        GlobalTableProvisionedWriteCapacityUnits=(
            Option_Some(native_input["GlobalTableProvisionedWriteCapacityUnits"])
            if "GlobalTableProvisionedWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input[
                        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"
                    ]
                )
            )
            if "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"
            in native_input.keys()
            else Option_None()
        ),
        GlobalTableGlobalSecondaryIndexSettingsUpdate=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(
                            list_element
                        )
                        for list_element in native_input[
                            "GlobalTableGlobalSecondaryIndexSettingsUpdate"
                        ]
                    ]
                )
            )
            if "GlobalTableGlobalSecondaryIndexSettingsUpdate" in native_input.keys()
            else Option_None()
        ),
        ReplicaSettingsUpdate=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaSettingsUpdate(
                            list_element
                        )
                        for list_element in native_input["ReplicaSettingsUpdate"]
                    ]
                )
            )
            if "ReplicaSettingsUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AutoScalingSettingsUpdate(native_input):
    return DafnyAutoScalingSettingsUpdate(
        MinimumUnits=(
            Option_Some(native_input["MinimumUnits"])
            if "MinimumUnits" in native_input.keys()
            else Option_None()
        ),
        MaximumUnits=(
            Option_Some(native_input["MaximumUnits"])
            if "MaximumUnits" in native_input.keys()
            else Option_None()
        ),
        AutoScalingDisabled=(
            Option_Some(native_input["AutoScalingDisabled"])
            if "AutoScalingDisabled" in native_input.keys()
            else Option_None()
        ),
        AutoScalingRoleArn=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["AutoScalingRoleArn"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "AutoScalingRoleArn" in native_input.keys()
            else Option_None()
        ),
        ScalingPolicyUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingPolicyUpdate(
                    native_input["ScalingPolicyUpdate"]
                )
            )
            if "ScalingPolicyUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AutoScalingPolicyUpdate(native_input):
    return DafnyAutoScalingPolicyUpdate(
        PolicyName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["PolicyName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "PolicyName" in native_input.keys()
            else Option_None()
        ),
        TargetTrackingScalingPolicyConfiguration=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
            native_input["TargetTrackingScalingPolicyConfiguration"]
        ),
    )


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
    native_input,
):
    return DafnyAutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
        DisableScaleIn=(
            Option_Some(native_input["DisableScaleIn"])
            if "DisableScaleIn" in native_input.keys()
            else Option_None()
        ),
        ScaleInCooldown=(
            Option_Some(native_input["ScaleInCooldown"])
            if "ScaleInCooldown" in native_input.keys()
            else Option_None()
        ),
        ScaleOutCooldown=(
            Option_Some(native_input["ScaleOutCooldown"])
            if "ScaleOutCooldown" in native_input.keys()
            else Option_None()
        ),
        TargetValue=native_input["TargetValue"],
    )


def com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(native_input):
    return DafnyGlobalTableGlobalSecondaryIndexSettingsUpdate(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProvisionedWriteCapacityUnits=(
            Option_Some(native_input["ProvisionedWriteCapacityUnits"])
            if "ProvisionedWriteCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ProvisionedWriteCapacityAutoScalingSettingsUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ProvisionedWriteCapacityAutoScalingSettingsUpdate"]
                )
            )
            if "ProvisionedWriteCapacityAutoScalingSettingsUpdate"
            in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaSettingsUpdate(native_input):
    return DafnyReplicaSettingsUpdate(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicaProvisionedReadCapacityUnits=(
            Option_Some(native_input["ReplicaProvisionedReadCapacityUnits"])
            if "ReplicaProvisionedReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input[
                        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"
                    ]
                )
            )
            if "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"
            in native_input.keys()
            else Option_None()
        ),
        ReplicaGlobalSecondaryIndexSettingsUpdate=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(
                            list_element
                        )
                        for list_element in native_input[
                            "ReplicaGlobalSecondaryIndexSettingsUpdate"
                        ]
                    ]
                )
            )
            if "ReplicaGlobalSecondaryIndexSettingsUpdate" in native_input.keys()
            else Option_None()
        ),
        ReplicaTableClass=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["ReplicaTableClass"]
                )
            )
            if "ReplicaTableClass" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(native_input):
    return DafnyReplicaGlobalSecondaryIndexSettingsUpdate(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProvisionedReadCapacityUnits=(
            Option_Some(native_input["ProvisionedReadCapacityUnits"])
            if "ProvisionedReadCapacityUnits" in native_input.keys()
            else Option_None()
        ),
        ProvisionedReadCapacityAutoScalingSettingsUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ProvisionedReadCapacityAutoScalingSettingsUpdate"]
                )
            )
            if "ProvisionedReadCapacityAutoScalingSettingsUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsOutput(native_input):
    return DafnyUpdateGlobalTableSettingsOutput(
        GlobalTableName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["GlobalTableName"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "GlobalTableName" in native_input.keys()
            else Option_None()
        ),
        ReplicaSettings=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                            list_element
                        )
                        for list_element in native_input["ReplicaSettings"]
                    ]
                )
            )
            if "ReplicaSettings" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateItemInput(native_input):
    return DafnyUpdateItemInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        Key=Map(
            {
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(*[iter(key.encode("utf-16-be"))] * 2)
                        ]
                    )
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in native_input["Key"].items()
            }
        ),
        AttributeUpdates=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValueUpdate(
                            value
                        )
                        for (key, value) in native_input["AttributeUpdates"].items()
                    }
                )
            )
            if "AttributeUpdates" in native_input.keys()
            else Option_None()
        ),
        Expected=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ExpectedAttributeValue(
                            value
                        )
                        for (key, value) in native_input["Expected"].items()
                    }
                )
            )
            if "Expected" in native_input.keys()
            else Option_None()
        ),
        ConditionalOperator=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConditionalOperator(
                    native_input["ConditionalOperator"]
                )
            )
            if "ConditionalOperator" in native_input.keys()
            else Option_None()
        ),
        ReturnValues=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnValue(
                    native_input["ReturnValues"]
                )
            )
            if "ReturnValues" in native_input.keys()
            else Option_None()
        ),
        ReturnConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                    native_input["ReturnConsumedCapacity"]
                )
            )
            if "ReturnConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ReturnItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                    native_input["ReturnItemCollectionMetrics"]
                )
            )
            if "ReturnItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
        UpdateExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["UpdateExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "UpdateExpression" in native_input.keys()
            else Option_None()
        ),
        ConditionExpression=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["ConditionExpression"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "ConditionExpression" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeNames=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(value.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeNames"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeNames" in native_input.keys()
            else Option_None()
        ),
        ExpressionAttributeValues=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input[
                            "ExpressionAttributeValues"
                        ].items()
                    }
                )
            )
            if "ExpressionAttributeValues" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AttributeValueUpdate(native_input):
    return DafnyAttributeValueUpdate(
        Value=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                    native_input["Value"]
                )
            )
            if "Value" in native_input.keys()
            else Option_None()
        ),
        Action=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeAction(
                    native_input["Action"]
                )
            )
            if "Action" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_AttributeAction(native_input):
    # Convert AttributeAction
    if native_input == "ADD":
        return AttributeAction_ADD()
    elif native_input == "PUT":
        return AttributeAction_PUT()
    elif native_input == "DELETE":
        return AttributeAction_DELETE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)


def com_amazonaws_dynamodb_UpdateItemOutput(native_input):
    return DafnyUpdateItemOutput(
        Attributes=(
            Option_Some(
                Map(
                    {
                        Seq(
                            "".join(
                                [
                                    chr(int.from_bytes(pair, "big"))
                                    for pair in zip(
                                        *[iter(key.encode("utf-16-be"))] * 2
                                    )
                                ]
                            )
                        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeValue(
                            value
                        )
                        for (key, value) in native_input["Attributes"].items()
                    }
                )
            )
            if "Attributes" in native_input.keys()
            else Option_None()
        ),
        ConsumedCapacity=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ConsumedCapacity(
                    native_input["ConsumedCapacity"]
                )
            )
            if "ConsumedCapacity" in native_input.keys()
            else Option_None()
        ),
        ItemCollectionMetrics=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    native_input["ItemCollectionMetrics"]
                )
            )
            if "ItemCollectionMetrics" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateTableInput(native_input):
    return DafnyUpdateTableInput(
        AttributeDefinitions=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AttributeDefinition(
                            list_element
                        )
                        for list_element in native_input["AttributeDefinitions"]
                    ]
                )
            )
            if "AttributeDefinitions" in native_input.keys()
            else Option_None()
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        BillingMode=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_BillingMode(
                    native_input["BillingMode"]
                )
            )
            if "BillingMode" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexUpdates=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexUpdates"]
                    ]
                )
            )
            if "GlobalSecondaryIndexUpdates" in native_input.keys()
            else Option_None()
        ),
        StreamSpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_StreamSpecification(
                    native_input["StreamSpecification"]
                )
            )
            if "StreamSpecification" in native_input.keys()
            else Option_None()
        ),
        SSESpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_SSESpecification(
                    native_input["SSESpecification"]
                )
            )
            if "SSESpecification" in native_input.keys()
            else Option_None()
        ),
        ReplicaUpdates=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicationGroupUpdate(
                            list_element
                        )
                        for list_element in native_input["ReplicaUpdates"]
                    ]
                )
            )
            if "ReplicaUpdates" in native_input.keys()
            else Option_None()
        ),
        TableClass=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["TableClass"]
                )
            )
            if "TableClass" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(native_input):
    return DafnyGlobalSecondaryIndexUpdate(
        Update=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(
                    native_input["Update"]
                )
            )
            if "Update" in native_input.keys()
            else Option_None()
        ),
        Create=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(
                    native_input["Create"]
                )
            )
            if "Create" in native_input.keys()
            else Option_None()
        ),
        Delete=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(
                    native_input["Delete"]
                )
            )
            if "Delete" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(native_input):
    return DafnyUpdateGlobalSecondaryIndexAction(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProvisionedThroughput=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
            native_input["ProvisionedThroughput"]
        ),
    )


def com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(native_input):
    return DafnyCreateGlobalSecondaryIndexAction(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KeySchema=Seq(
            [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_KeySchemaElement(
                    list_element
                )
                for list_element in native_input["KeySchema"]
            ]
        ),
        Projection=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_Projection(
            native_input["Projection"]
        ),
        ProvisionedThroughput=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughput(
                    native_input["ProvisionedThroughput"]
                )
            )
            if "ProvisionedThroughput" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(native_input):
    return DafnyDeleteGlobalSecondaryIndexAction(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ReplicationGroupUpdate(native_input):
    return DafnyReplicationGroupUpdate(
        Create=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(
                    native_input["Create"]
                )
            )
            if "Create" in native_input.keys()
            else Option_None()
        ),
        Update=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(
                    native_input["Update"]
                )
            )
            if "Update" in native_input.keys()
            else Option_None()
        ),
        Delete=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(
                    native_input["Delete"]
                )
            )
            if "Delete" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(native_input):
    return DafnyCreateReplicationGroupMemberAction(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KMSMasterKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KMSMasterKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KMSMasterKeyId" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        TableClassOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["TableClassOverride"]
                )
            )
            if "TableClassOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(native_input):
    return DafnyUpdateReplicationGroupMemberAction(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        KMSMasterKeyId=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[
                                    iter(
                                        native_input["KMSMasterKeyId"].encode(
                                            "utf-16-be"
                                        )
                                    )
                                ]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "KMSMasterKeyId" in native_input.keys()
            else Option_None()
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
        GlobalSecondaryIndexes=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexes"]
                    ]
                )
            )
            if "GlobalSecondaryIndexes" in native_input.keys()
            else Option_None()
        ),
        TableClassOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableClass(
                    native_input["TableClassOverride"]
                )
            )
            if "TableClassOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(native_input):
    return DafnyDeleteReplicationGroupMemberAction(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(native_input):
    return DafnyReplicaGlobalSecondaryIndex(
        IndexName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["IndexName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProvisionedThroughputOverride=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                    native_input["ProvisionedThroughputOverride"]
                )
            )
            if "ProvisionedThroughputOverride" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateTableOutput(native_input):
    return DafnyUpdateTableOutput(
        TableDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableDescription(
                    native_input["TableDescription"]
                )
            )
            if "TableDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingInput(native_input):
    return DafnyUpdateTableReplicaAutoScalingInput(
        GlobalSecondaryIndexUpdates=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(
                            list_element
                        )
                        for list_element in native_input["GlobalSecondaryIndexUpdates"]
                    ]
                )
            )
            if "GlobalSecondaryIndexUpdates" in native_input.keys()
            else Option_None()
        ),
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ProvisionedWriteCapacityAutoScalingUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ProvisionedWriteCapacityAutoScalingUpdate"]
                )
            )
            if "ProvisionedWriteCapacityAutoScalingUpdate" in native_input.keys()
            else Option_None()
        ),
        ReplicaUpdates=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(
                            list_element
                        )
                        for list_element in native_input["ReplicaUpdates"]
                    ]
                )
            )
            if "ReplicaUpdates" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(native_input):
    return DafnyGlobalSecondaryIndexAutoScalingUpdate(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ProvisionedWriteCapacityAutoScalingUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ProvisionedWriteCapacityAutoScalingUpdate"]
                )
            )
            if "ProvisionedWriteCapacityAutoScalingUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(native_input):
    return DafnyReplicaAutoScalingUpdate(
        RegionName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["RegionName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        ReplicaGlobalSecondaryIndexUpdates=(
            Option_Some(
                Seq(
                    [
                        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(
                            list_element
                        )
                        for list_element in native_input[
                            "ReplicaGlobalSecondaryIndexUpdates"
                        ]
                    ]
                )
            )
            if "ReplicaGlobalSecondaryIndexUpdates" in native_input.keys()
            else Option_None()
        ),
        ReplicaProvisionedReadCapacityAutoScalingUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ReplicaProvisionedReadCapacityAutoScalingUpdate"]
                )
            )
            if "ReplicaProvisionedReadCapacityAutoScalingUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(native_input):
    return DafnyReplicaGlobalSecondaryIndexAutoScalingUpdate(
        IndexName=(
            Option_Some(
                Seq(
                    "".join(
                        [
                            chr(int.from_bytes(pair, "big"))
                            for pair in zip(
                                *[iter(native_input["IndexName"].encode("utf-16-be"))]
                                * 2
                            )
                        ]
                    )
                )
            )
            if "IndexName" in native_input.keys()
            else Option_None()
        ),
        ProvisionedReadCapacityAutoScalingUpdate=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                    native_input["ProvisionedReadCapacityAutoScalingUpdate"]
                )
            )
            if "ProvisionedReadCapacityAutoScalingUpdate" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingOutput(native_input):
    return DafnyUpdateTableReplicaAutoScalingOutput(
        TableAutoScalingDescription=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TableAutoScalingDescription(
                    native_input["TableAutoScalingDescription"]
                )
            )
            if "TableAutoScalingDescription" in native_input.keys()
            else Option_None()
        ),
    )


def com_amazonaws_dynamodb_UpdateTimeToLiveInput(native_input):
    return DafnyUpdateTimeToLiveInput(
        TableName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["TableName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
        TimeToLiveSpecification=aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TimeToLiveSpecification(
            native_input["TimeToLiveSpecification"]
        ),
    )


def com_amazonaws_dynamodb_TimeToLiveSpecification(native_input):
    return DafnyTimeToLiveSpecification(
        Enabled=native_input["Enabled"],
        AttributeName=Seq(
            "".join(
                [
                    chr(int.from_bytes(pair, "big"))
                    for pair in zip(
                        *[iter(native_input["AttributeName"].encode("utf-16-be"))] * 2
                    )
                ]
            )
        ),
    )


def com_amazonaws_dynamodb_UpdateTimeToLiveOutput(native_input):
    return DafnyUpdateTimeToLiveOutput(
        TimeToLiveSpecification=(
            Option_Some(
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_to_dafny.com_amazonaws_dynamodb_TimeToLiveSpecification(
                    native_input["TimeToLiveSpecification"]
                )
            )
            if "TimeToLiveSpecification" in native_input.keys()
            else Option_None()
        ),
    )
