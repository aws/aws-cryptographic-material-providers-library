// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.services.dynamodb.internaldafny;

import Wrappers_Compile.Option;
import dafny.DafnyMap;
import dafny.DafnySequence;
import dafny.TypeDescriptor;
import java.lang.Boolean;
import java.lang.Byte;
import java.lang.Character;
import java.lang.Double;
import java.lang.Exception;
import java.lang.IllegalArgumentException;
import java.lang.Integer;
import java.lang.Long;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.SuppressWarnings;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.BackupInUseException;
import software.amazon.awssdk.services.dynamodb.model.BackupNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.BatchExecuteStatementRequest;
import software.amazon.awssdk.services.dynamodb.model.BatchExecuteStatementResponse;
import software.amazon.awssdk.services.dynamodb.model.BatchGetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.BatchGetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.BatchWriteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.BatchWriteItemResponse;
import software.amazon.awssdk.services.dynamodb.model.ConditionalCheckFailedException;
import software.amazon.awssdk.services.dynamodb.model.ContinuousBackupsUnavailableException;
import software.amazon.awssdk.services.dynamodb.model.CreateBackupRequest;
import software.amazon.awssdk.services.dynamodb.model.CreateBackupResponse;
import software.amazon.awssdk.services.dynamodb.model.CreateGlobalTableRequest;
import software.amazon.awssdk.services.dynamodb.model.CreateGlobalTableResponse;
import software.amazon.awssdk.services.dynamodb.model.CreateTableRequest;
import software.amazon.awssdk.services.dynamodb.model.CreateTableResponse;
import software.amazon.awssdk.services.dynamodb.model.DeleteBackupRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteBackupResponse;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemResponse;
import software.amazon.awssdk.services.dynamodb.model.DeleteResourcePolicyRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteResourcePolicyResponse;
import software.amazon.awssdk.services.dynamodb.model.DeleteTableRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteTableResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeBackupRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeBackupResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeContinuousBackupsRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeContinuousBackupsResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeContributorInsightsRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeContributorInsightsResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeExportRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeExportResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeGlobalTableRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeGlobalTableResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeGlobalTableSettingsRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeGlobalTableSettingsResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeImportRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeImportResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeKinesisStreamingDestinationRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeKinesisStreamingDestinationResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeLimitsRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeLimitsResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableReplicaAutoScalingRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableReplicaAutoScalingResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableResponse;
import software.amazon.awssdk.services.dynamodb.model.DescribeTimeToLiveRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeTimeToLiveResponse;
import software.amazon.awssdk.services.dynamodb.model.DisableKinesisStreamingDestinationRequest;
import software.amazon.awssdk.services.dynamodb.model.DisableKinesisStreamingDestinationResponse;
import software.amazon.awssdk.services.dynamodb.model.DuplicateItemException;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.EnableKinesisStreamingDestinationRequest;
import software.amazon.awssdk.services.dynamodb.model.EnableKinesisStreamingDestinationResponse;
import software.amazon.awssdk.services.dynamodb.model.ExecuteStatementRequest;
import software.amazon.awssdk.services.dynamodb.model.ExecuteStatementResponse;
import software.amazon.awssdk.services.dynamodb.model.ExecuteTransactionRequest;
import software.amazon.awssdk.services.dynamodb.model.ExecuteTransactionResponse;
import software.amazon.awssdk.services.dynamodb.model.ExportConflictException;
import software.amazon.awssdk.services.dynamodb.model.ExportNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.ExportTableToPointInTimeRequest;
import software.amazon.awssdk.services.dynamodb.model.ExportTableToPointInTimeResponse;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.GetResourcePolicyRequest;
import software.amazon.awssdk.services.dynamodb.model.GetResourcePolicyResponse;
import software.amazon.awssdk.services.dynamodb.model.GlobalTableAlreadyExistsException;
import software.amazon.awssdk.services.dynamodb.model.GlobalTableNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.IdempotentParameterMismatchException;
import software.amazon.awssdk.services.dynamodb.model.ImportConflictException;
import software.amazon.awssdk.services.dynamodb.model.ImportNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.ImportTableRequest;
import software.amazon.awssdk.services.dynamodb.model.ImportTableResponse;
import software.amazon.awssdk.services.dynamodb.model.IndexNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.InternalServerErrorException;
import software.amazon.awssdk.services.dynamodb.model.InvalidExportTimeException;
import software.amazon.awssdk.services.dynamodb.model.InvalidRestoreTimeException;
import software.amazon.awssdk.services.dynamodb.model.ItemCollectionSizeLimitExceededException;
import software.amazon.awssdk.services.dynamodb.model.LimitExceededException;
import software.amazon.awssdk.services.dynamodb.model.ListBackupsRequest;
import software.amazon.awssdk.services.dynamodb.model.ListBackupsResponse;
import software.amazon.awssdk.services.dynamodb.model.ListContributorInsightsRequest;
import software.amazon.awssdk.services.dynamodb.model.ListContributorInsightsResponse;
import software.amazon.awssdk.services.dynamodb.model.ListExportsRequest;
import software.amazon.awssdk.services.dynamodb.model.ListExportsResponse;
import software.amazon.awssdk.services.dynamodb.model.ListGlobalTablesRequest;
import software.amazon.awssdk.services.dynamodb.model.ListGlobalTablesResponse;
import software.amazon.awssdk.services.dynamodb.model.ListImportsRequest;
import software.amazon.awssdk.services.dynamodb.model.ListImportsResponse;
import software.amazon.awssdk.services.dynamodb.model.ListTablesRequest;
import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;
import software.amazon.awssdk.services.dynamodb.model.ListTagsOfResourceRequest;
import software.amazon.awssdk.services.dynamodb.model.ListTagsOfResourceResponse;
import software.amazon.awssdk.services.dynamodb.model.PointInTimeRecoveryUnavailableException;
import software.amazon.awssdk.services.dynamodb.model.PolicyNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.ProvisionedThroughputExceededException;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.PutItemResponse;
import software.amazon.awssdk.services.dynamodb.model.PutResourcePolicyRequest;
import software.amazon.awssdk.services.dynamodb.model.PutResourcePolicyResponse;
import software.amazon.awssdk.services.dynamodb.model.QueryRequest;
import software.amazon.awssdk.services.dynamodb.model.QueryResponse;
import software.amazon.awssdk.services.dynamodb.model.ReplicaAlreadyExistsException;
import software.amazon.awssdk.services.dynamodb.model.ReplicaNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.RequestLimitExceededException;
import software.amazon.awssdk.services.dynamodb.model.ResourceInUseException;
import software.amazon.awssdk.services.dynamodb.model.ResourceNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.RestoreTableFromBackupRequest;
import software.amazon.awssdk.services.dynamodb.model.RestoreTableFromBackupResponse;
import software.amazon.awssdk.services.dynamodb.model.RestoreTableToPointInTimeRequest;
import software.amazon.awssdk.services.dynamodb.model.RestoreTableToPointInTimeResponse;
import software.amazon.awssdk.services.dynamodb.model.ScanRequest;
import software.amazon.awssdk.services.dynamodb.model.ScanResponse;
import software.amazon.awssdk.services.dynamodb.model.TableAlreadyExistsException;
import software.amazon.awssdk.services.dynamodb.model.TableInUseException;
import software.amazon.awssdk.services.dynamodb.model.TableNotFoundException;
import software.amazon.awssdk.services.dynamodb.model.TagResourceRequest;
import software.amazon.awssdk.services.dynamodb.model.TransactGetItemsRequest;
import software.amazon.awssdk.services.dynamodb.model.TransactGetItemsResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsRequest;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactionCanceledException;
import software.amazon.awssdk.services.dynamodb.model.TransactionConflictException;
import software.amazon.awssdk.services.dynamodb.model.TransactionInProgressException;
import software.amazon.awssdk.services.dynamodb.model.UntagResourceRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateContinuousBackupsRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateContinuousBackupsResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateContributorInsightsRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateContributorInsightsResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateGlobalTableRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateGlobalTableResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateGlobalTableSettingsRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateGlobalTableSettingsResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateItemRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateItemResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateKinesisStreamingDestinationRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateKinesisStreamingDestinationResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateTableReplicaAutoScalingRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateTableReplicaAutoScalingResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateTableRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateTableResponse;
import software.amazon.awssdk.services.dynamodb.model.UpdateTimeToLiveRequest;
import software.amazon.awssdk.services.dynamodb.model.UpdateTimeToLiveResponse;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ApproximateCreationDateTimePrecision;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ArchivalSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeDefinition;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValueUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingPolicyDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingPolicyUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingSettingsDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingSettingsUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingTargetTrackingScalingPolicyConfigurationDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupDetails;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupTypeFilter;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchExecuteStatementInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchExecuteStatementOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchGetItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchGetItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementError;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementErrorCodeEnum;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementRequest;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementResponse;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchWriteItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchWriteItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingModeSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CancellationReason;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Capacity;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ComparisonOperator;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Condition;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ConditionCheck;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ConditionalOperator;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ConsumedCapacity;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ConsumedCapacityUnits;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ContinuousBackupsDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ContinuousBackupsStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateBackupInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateBackupOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateGlobalSecondaryIndexAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateGlobalTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateGlobalTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateReplicaAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateReplicationGroupMemberAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CreateTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.CsvOptions;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Delete;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteBackupInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteBackupOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteGlobalSecondaryIndexAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteReplicaAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteReplicationGroupMemberAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteRequest;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteResourcePolicyInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteResourcePolicyOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DeleteTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeBackupInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeBackupOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeContinuousBackupsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeContinuousBackupsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeContributorInsightsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeContributorInsightsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeEndpointsRequest;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeEndpointsResponse;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeExportInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeExportOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableSettingsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableSettingsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeImportInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeImportOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeKinesisStreamingDestinationInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeKinesisStreamingDestinationOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeLimitsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeLimitsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableReplicaAutoScalingInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableReplicaAutoScalingOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTimeToLiveInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTimeToLiveOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DestinationStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DisableKinesisStreamingDestinationInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.DisableKinesisStreamingDestinationOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.EnableKinesisStreamingConfiguration;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.EnableKinesisStreamingDestinationInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.EnableKinesisStreamingDestinationOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Endpoint;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_BackupInUseException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_BackupNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ConditionalCheckFailedException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ContinuousBackupsUnavailableException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_DuplicateItemException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ExportConflictException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ExportNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_GlobalTableAlreadyExistsException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_GlobalTableNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_IdempotentParameterMismatchException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ImportConflictException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ImportNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_IndexNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_InternalServerError;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_InvalidExportTimeException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_InvalidRestoreTimeException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ItemCollectionSizeLimitExceededException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_LimitExceededException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_PointInTimeRecoveryUnavailableException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_PolicyNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ProvisionedThroughputExceededException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ReplicaAlreadyExistsException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ReplicaNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_RequestLimitExceeded;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ResourceInUseException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_ResourceNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TableAlreadyExistsException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TableInUseException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TableNotFoundException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TransactionCanceledException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TransactionConflictException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Error_TransactionInProgressException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExecuteStatementInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExecuteStatementOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExecuteTransactionInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExecuteTransactionOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExpectedAttributeValue;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportFormat;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportTableToPointInTimeInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportTableToPointInTimeOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportViewType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.FailureException;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Get;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GetItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GetItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GetResourcePolicyInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GetResourcePolicyOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndex;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexAutoScalingUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexInfo;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTable;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableGlobalSecondaryIndexSettingsUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IDynamoDBClient;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportTableDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IncrementalExportSpecification;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.IndexStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.InputCompressionType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.InputFormat;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.InputFormatOptions;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ItemCollectionMetrics;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ItemCollectionSizeEstimateBound;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ItemResponse;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.KeySchemaElement;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.KeyType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.KeysAndAttributes;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.KinesisDataStreamDestination;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListBackupsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListBackupsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListContributorInsightsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListContributorInsightsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListExportsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListExportsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListGlobalTablesInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListGlobalTablesOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListImportsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListImportsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListTablesInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListTablesOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListTagsOfResourceInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ListTagsOfResourceOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndex;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndexDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndexInfo;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.OnDemandThroughput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.OnDemandThroughputOverride;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ParameterizedStatement;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PointInTimeRecoveryDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PointInTimeRecoverySpecification;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PointInTimeRecoveryStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Projection;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ProjectionType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughputDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ProvisionedThroughputOverride;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Put;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PutItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PutItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PutRequest;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PutResourcePolicyInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.PutResourcePolicyOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.QueryInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.QueryOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Replica;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaAutoScalingDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaAutoScalingUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndex;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexAutoScalingDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexAutoScalingUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexSettingsDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexSettingsUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaSettingsDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaSettingsUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicationGroupUpdate;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableFromBackupInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableFromBackupOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableToPointInTimeInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableToPointInTimeOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnConsumedCapacity;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnItemCollectionMetrics;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValue;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValuesOnConditionCheckFailure;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.S3BucketSource;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.S3SseAlgorithm;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SSESpecification;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ScalarAttributeType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ScanInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.ScanOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Select;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SourceTableDetails;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.SourceTableFeatureDetails;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamSpecification;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamViewType;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableAutoScalingDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClass;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClassSummary;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableCreationParameters;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TableStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Tag;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TagResourceInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveDescription;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveSpecification;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveStatus;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactGetItem;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactGetItemsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactGetItemsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItem;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.TransactWriteItemsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UntagResourceInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.Update;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContinuousBackupsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContinuousBackupsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContributorInsightsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateContributorInsightsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalSecondaryIndexAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableSettingsInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableSettingsOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateItemInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateItemOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingConfiguration;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingDestinationInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateKinesisStreamingDestinationOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateReplicationGroupMemberAction;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTableInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTableOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTableReplicaAutoScalingInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTableReplicaAutoScalingOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTimeToLiveInput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTimeToLiveOutput;
import software.amazon.cryptography.services.dynamodb.internaldafny.types.WriteRequest;

public class ToDafny {

  public static ArchivalSummary ArchivalSummary(
    software.amazon.awssdk.services.dynamodb.model.ArchivalSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> archivalDateTime;
    archivalDateTime =
      Objects.nonNull(nativeValue.archivalDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.archivalDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> archivalReason;
    archivalReason =
      Objects.nonNull(nativeValue.archivalReason())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.archivalReason()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> archivalBackupArn;
    archivalBackupArn =
      Objects.nonNull(nativeValue.archivalBackupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.archivalBackupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ArchivalSummary(
      archivalDateTime,
      archivalReason,
      archivalBackupArn
    );
  }

  public static AttributeDefinition AttributeDefinition(
    software.amazon.awssdk.services.dynamodb.model.AttributeDefinition nativeValue
  ) {
    DafnySequence<? extends Character> attributeName;
    attributeName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.attributeName()
      );
    ScalarAttributeType attributeType;
    attributeType = ToDafny.ScalarAttributeType(nativeValue.attributeType());
    return new AttributeDefinition(attributeName, attributeType);
  }

  public static DafnySequence<
    ? extends AttributeDefinition
  > AttributeDefinitions(
    List<
      software.amazon.awssdk.services.dynamodb.model.AttributeDefinition
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeDefinition,
      AttributeDefinition._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > AttributeMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > AttributeNameList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValueUpdate
  > AttributeUpdates(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValueUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValueUpdate
    );
  }

  public static AttributeValue AttributeValue(
    software.amazon.awssdk.services.dynamodb.model.AttributeValue nativeValue
  ) {
    switch (nativeValue.type()) {
      case S:
        {
          return AttributeValue.create_S(
            software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
              nativeValue.s()
            )
          );
        }
      case N:
        {
          return AttributeValue.create_N(
            software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
              nativeValue.n()
            )
          );
        }
      case B:
        {
          return AttributeValue.create_B(
            software.amazon.smithy.dafny.conversion.ToDafny.Simple.ByteSequence(
              nativeValue.b().asByteArray()
            )
          );
        }
      case SS:
        {
          return AttributeValue.create_SS(
            ToDafny.StringSetAttributeValue(nativeValue.ss())
          );
        }
      case NS:
        {
          return AttributeValue.create_NS(
            ToDafny.NumberSetAttributeValue(nativeValue.ns())
          );
        }
      case BS:
        {
          return AttributeValue.create_BS(
            ToDafny.BinarySetAttributeValue(
              nativeValue
                .bs()
                .stream()
                .map(software.amazon.awssdk.core.BytesWrapper::asByteBuffer)
                .collect(java.util.stream.Collectors.toList())
            )
          );
        }
      case M:
        {
          return AttributeValue.create_M(
            ToDafny.MapAttributeValue(nativeValue.m())
          );
        }
      case L:
        {
          return AttributeValue.create_L(
            ToDafny.ListAttributeValue(nativeValue.l())
          );
        }
      case NUL:
        {
          return AttributeValue.create_NULL((nativeValue.nul()));
        }
      case BOOL:
        {
          return AttributeValue.create_BOOL((nativeValue.bool()));
        }
      default:
        {
          throw new IllegalArgumentException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue."
          );
        }
    }
  }

  public static DafnySequence<? extends AttributeValue> AttributeValueList(
    List<
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue,
      AttributeValue._typeDescriptor()
    );
  }

  public static AttributeValueUpdate AttributeValueUpdate(
    software.amazon.awssdk.services.dynamodb.model.AttributeValueUpdate nativeValue
  ) {
    Option<AttributeValue> value;
    value =
      Objects.nonNull(nativeValue.value())
        ? Option.create_Some(
          AttributeValue._typeDescriptor(),
          ToDafny.AttributeValue(nativeValue.value())
        )
        : Option.create_None(AttributeValue._typeDescriptor());
    Option<AttributeAction> action;
    action =
      Objects.nonNull(nativeValue.action())
        ? Option.create_Some(
          AttributeAction._typeDescriptor(),
          ToDafny.AttributeAction(nativeValue.action())
        )
        : Option.create_None(AttributeAction._typeDescriptor());
    return new AttributeValueUpdate(value, action);
  }

  public static AutoScalingPolicyDescription AutoScalingPolicyDescription(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingPolicyDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> policyName;
    policyName =
      Objects.nonNull(nativeValue.policyName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policyName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      AutoScalingTargetTrackingScalingPolicyConfigurationDescription
    > targetTrackingScalingPolicyConfiguration;
    targetTrackingScalingPolicyConfiguration =
      Objects.nonNull(nativeValue.targetTrackingScalingPolicyConfiguration())
        ? Option.create_Some(
          AutoScalingTargetTrackingScalingPolicyConfigurationDescription._typeDescriptor(),
          ToDafny.AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
            nativeValue.targetTrackingScalingPolicyConfiguration()
          )
        )
        : Option.create_None(
          AutoScalingTargetTrackingScalingPolicyConfigurationDescription._typeDescriptor()
        );
    return new AutoScalingPolicyDescription(
      policyName,
      targetTrackingScalingPolicyConfiguration
    );
  }

  public static DafnySequence<
    ? extends AutoScalingPolicyDescription
  > AutoScalingPolicyDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.AutoScalingPolicyDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AutoScalingPolicyDescription,
      AutoScalingPolicyDescription._typeDescriptor()
    );
  }

  public static AutoScalingPolicyUpdate AutoScalingPolicyUpdate(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingPolicyUpdate nativeValue
  ) {
    Option<DafnySequence<? extends Character>> policyName;
    policyName =
      Objects.nonNull(nativeValue.policyName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policyName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    AutoScalingTargetTrackingScalingPolicyConfigurationUpdate targetTrackingScalingPolicyConfiguration;
    targetTrackingScalingPolicyConfiguration =
      ToDafny.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
        nativeValue.targetTrackingScalingPolicyConfiguration()
      );
    return new AutoScalingPolicyUpdate(
      policyName,
      targetTrackingScalingPolicyConfiguration
    );
  }

  public static AutoScalingSettingsDescription AutoScalingSettingsDescription(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingSettingsDescription nativeValue
  ) {
    Option<Long> minimumUnits;
    minimumUnits =
      Objects.nonNull(nativeValue.minimumUnits())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.minimumUnits()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> maximumUnits;
    maximumUnits =
      Objects.nonNull(nativeValue.maximumUnits())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.maximumUnits()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<Boolean> autoScalingDisabled;
    autoScalingDisabled =
      Objects.nonNull(nativeValue.autoScalingDisabled())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.autoScalingDisabled())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> autoScalingRoleArn;
    autoScalingRoleArn =
      Objects.nonNull(nativeValue.autoScalingRoleArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.autoScalingRoleArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends AutoScalingPolicyDescription>
    > scalingPolicies;
    scalingPolicies =
      (Objects.nonNull(nativeValue.scalingPolicies()) &&
          nativeValue.scalingPolicies().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            AutoScalingPolicyDescription._typeDescriptor()
          ),
          ToDafny.AutoScalingPolicyDescriptionList(
            nativeValue.scalingPolicies()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            AutoScalingPolicyDescription._typeDescriptor()
          )
        );
    return new AutoScalingSettingsDescription(
      minimumUnits,
      maximumUnits,
      autoScalingDisabled,
      autoScalingRoleArn,
      scalingPolicies
    );
  }

  public static AutoScalingSettingsUpdate AutoScalingSettingsUpdate(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingSettingsUpdate nativeValue
  ) {
    Option<Long> minimumUnits;
    minimumUnits =
      Objects.nonNull(nativeValue.minimumUnits())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.minimumUnits()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> maximumUnits;
    maximumUnits =
      Objects.nonNull(nativeValue.maximumUnits())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.maximumUnits()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<Boolean> autoScalingDisabled;
    autoScalingDisabled =
      Objects.nonNull(nativeValue.autoScalingDisabled())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.autoScalingDisabled())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> autoScalingRoleArn;
    autoScalingRoleArn =
      Objects.nonNull(nativeValue.autoScalingRoleArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.autoScalingRoleArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<AutoScalingPolicyUpdate> scalingPolicyUpdate;
    scalingPolicyUpdate =
      Objects.nonNull(nativeValue.scalingPolicyUpdate())
        ? Option.create_Some(
          AutoScalingPolicyUpdate._typeDescriptor(),
          ToDafny.AutoScalingPolicyUpdate(nativeValue.scalingPolicyUpdate())
        )
        : Option.create_None(AutoScalingPolicyUpdate._typeDescriptor());
    return new AutoScalingSettingsUpdate(
      minimumUnits,
      maximumUnits,
      autoScalingDisabled,
      autoScalingRoleArn,
      scalingPolicyUpdate
    );
  }

  public static AutoScalingTargetTrackingScalingPolicyConfigurationDescription AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingTargetTrackingScalingPolicyConfigurationDescription nativeValue
  ) {
    Option<Boolean> disableScaleIn;
    disableScaleIn =
      Objects.nonNull(nativeValue.disableScaleIn())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.disableScaleIn())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<Integer> scaleInCooldown;
    scaleInCooldown =
      Objects.nonNull(nativeValue.scaleInCooldown())
        ? Option.create_Some(
          TypeDescriptor.INT,
          (nativeValue.scaleInCooldown())
        )
        : Option.create_None(TypeDescriptor.INT);
    Option<Integer> scaleOutCooldown;
    scaleOutCooldown =
      Objects.nonNull(nativeValue.scaleOutCooldown())
        ? Option.create_Some(
          TypeDescriptor.INT,
          (nativeValue.scaleOutCooldown())
        )
        : Option.create_None(TypeDescriptor.INT);
    DafnySequence<? extends Byte> targetValue;
    targetValue =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
        nativeValue.targetValue()
      );
    return new AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
      disableScaleIn,
      scaleInCooldown,
      scaleOutCooldown,
      targetValue
    );
  }

  public static AutoScalingTargetTrackingScalingPolicyConfigurationUpdate AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
    software.amazon.awssdk.services.dynamodb.model.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate nativeValue
  ) {
    Option<Boolean> disableScaleIn;
    disableScaleIn =
      Objects.nonNull(nativeValue.disableScaleIn())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.disableScaleIn())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<Integer> scaleInCooldown;
    scaleInCooldown =
      Objects.nonNull(nativeValue.scaleInCooldown())
        ? Option.create_Some(
          TypeDescriptor.INT,
          (nativeValue.scaleInCooldown())
        )
        : Option.create_None(TypeDescriptor.INT);
    Option<Integer> scaleOutCooldown;
    scaleOutCooldown =
      Objects.nonNull(nativeValue.scaleOutCooldown())
        ? Option.create_Some(
          TypeDescriptor.INT,
          (nativeValue.scaleOutCooldown())
        )
        : Option.create_None(TypeDescriptor.INT);
    DafnySequence<? extends Byte> targetValue;
    targetValue =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
        nativeValue.targetValue()
      );
    return new AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
      disableScaleIn,
      scaleInCooldown,
      scaleOutCooldown,
      targetValue
    );
  }

  public static BackupDescription BackupDescription(
    software.amazon.awssdk.services.dynamodb.model.BackupDescription nativeValue
  ) {
    Option<BackupDetails> backupDetails;
    backupDetails =
      Objects.nonNull(nativeValue.backupDetails())
        ? Option.create_Some(
          BackupDetails._typeDescriptor(),
          ToDafny.BackupDetails(nativeValue.backupDetails())
        )
        : Option.create_None(BackupDetails._typeDescriptor());
    Option<SourceTableDetails> sourceTableDetails;
    sourceTableDetails =
      Objects.nonNull(nativeValue.sourceTableDetails())
        ? Option.create_Some(
          SourceTableDetails._typeDescriptor(),
          ToDafny.SourceTableDetails(nativeValue.sourceTableDetails())
        )
        : Option.create_None(SourceTableDetails._typeDescriptor());
    Option<SourceTableFeatureDetails> sourceTableFeatureDetails;
    sourceTableFeatureDetails =
      Objects.nonNull(nativeValue.sourceTableFeatureDetails())
        ? Option.create_Some(
          SourceTableFeatureDetails._typeDescriptor(),
          ToDafny.SourceTableFeatureDetails(
            nativeValue.sourceTableFeatureDetails()
          )
        )
        : Option.create_None(SourceTableFeatureDetails._typeDescriptor());
    return new BackupDescription(
      backupDetails,
      sourceTableDetails,
      sourceTableFeatureDetails
    );
  }

  public static BackupDetails BackupDetails(
    software.amazon.awssdk.services.dynamodb.model.BackupDetails nativeValue
  ) {
    DafnySequence<? extends Character> backupArn;
    backupArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupArn()
      );
    DafnySequence<? extends Character> backupName;
    backupName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupName()
      );
    Option<Long> backupSizeBytes;
    backupSizeBytes =
      Objects.nonNull(nativeValue.backupSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.backupSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    BackupStatus backupStatus;
    backupStatus = ToDafny.BackupStatus(nativeValue.backupStatus());
    BackupType backupType;
    backupType = ToDafny.BackupType(nativeValue.backupType());
    DafnySequence<? extends Character> backupCreationDateTime;
    backupCreationDateTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupCreationDateTime()
      );
    Option<DafnySequence<? extends Character>> backupExpiryDateTime;
    backupExpiryDateTime =
      Objects.nonNull(nativeValue.backupExpiryDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.backupExpiryDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new BackupDetails(
      backupArn,
      backupName,
      backupSizeBytes,
      backupStatus,
      backupType,
      backupCreationDateTime,
      backupExpiryDateTime
    );
  }

  public static DafnySequence<? extends BackupSummary> BackupSummaries(
    List<
      software.amazon.awssdk.services.dynamodb.model.BackupSummary
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::BackupSummary,
      BackupSummary._typeDescriptor()
    );
  }

  public static BackupSummary BackupSummary(
    software.amazon.awssdk.services.dynamodb.model.BackupSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableId;
    tableId =
      Objects.nonNull(nativeValue.tableId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> backupArn;
    backupArn =
      Objects.nonNull(nativeValue.backupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.backupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> backupName;
    backupName =
      Objects.nonNull(nativeValue.backupName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.backupName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> backupCreationDateTime;
    backupCreationDateTime =
      Objects.nonNull(nativeValue.backupCreationDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.backupCreationDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> backupExpiryDateTime;
    backupExpiryDateTime =
      Objects.nonNull(nativeValue.backupExpiryDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.backupExpiryDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<BackupStatus> backupStatus;
    backupStatus =
      Objects.nonNull(nativeValue.backupStatus())
        ? Option.create_Some(
          BackupStatus._typeDescriptor(),
          ToDafny.BackupStatus(nativeValue.backupStatus())
        )
        : Option.create_None(BackupStatus._typeDescriptor());
    Option<BackupType> backupType;
    backupType =
      Objects.nonNull(nativeValue.backupType())
        ? Option.create_Some(
          BackupType._typeDescriptor(),
          ToDafny.BackupType(nativeValue.backupType())
        )
        : Option.create_None(BackupType._typeDescriptor());
    Option<Long> backupSizeBytes;
    backupSizeBytes =
      Objects.nonNull(nativeValue.backupSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.backupSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new BackupSummary(
      tableName,
      tableId,
      tableArn,
      backupArn,
      backupName,
      backupCreationDateTime,
      backupExpiryDateTime,
      backupStatus,
      backupType,
      backupSizeBytes
    );
  }

  public static BatchExecuteStatementInput BatchExecuteStatementInput(
    BatchExecuteStatementRequest nativeValue
  ) {
    DafnySequence<? extends BatchStatementRequest> statements;
    statements = ToDafny.PartiQLBatchRequest(nativeValue.statements());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    return new BatchExecuteStatementInput(statements, returnConsumedCapacity);
  }

  public static BatchExecuteStatementOutput BatchExecuteStatementOutput(
    BatchExecuteStatementResponse nativeValue
  ) {
    Option<DafnySequence<? extends BatchStatementResponse>> responses;
    responses =
      (Objects.nonNull(nativeValue.responses()) &&
          nativeValue.responses().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            BatchStatementResponse._typeDescriptor()
          ),
          ToDafny.PartiQLBatchResponse(nativeValue.responses())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            BatchStatementResponse._typeDescriptor()
          )
        );
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    return new BatchExecuteStatementOutput(responses, consumedCapacity);
  }

  public static BatchGetItemInput BatchGetItemInput(
    BatchGetItemRequest nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends KeysAndAttributes
    > requestItems;
    requestItems = ToDafny.BatchGetRequestMap(nativeValue.requestItems());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    return new BatchGetItemInput(requestItems, returnConsumedCapacity);
  }

  public static BatchGetItemOutput BatchGetItemOutput(
    BatchGetItemResponse nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<
          ? extends DafnyMap<
            ? extends DafnySequence<? extends Character>,
            ? extends AttributeValue
          >
        >
      >
    > responses;
    responses =
      (Objects.nonNull(nativeValue.responses()) &&
          nativeValue.responses().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              TypeDescriptor.referenceWithInitializer(
                dafny.DafnyMap.class,
                () ->
                  dafny.DafnyMap.<
                    dafny.DafnySequence<? extends Character>,
                    AttributeValue
                  >empty()
              )
            )
          ),
          ToDafny.BatchGetResponseMap(nativeValue.responses())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              TypeDescriptor.referenceWithInitializer(
                dafny.DafnyMap.class,
                () ->
                  dafny.DafnyMap.<
                    dafny.DafnySequence<? extends Character>,
                    AttributeValue
                  >empty()
              )
            )
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends KeysAndAttributes
      >
    > unprocessedKeys;
    unprocessedKeys =
      (Objects.nonNull(nativeValue.unprocessedKeys()) &&
          nativeValue.unprocessedKeys().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            KeysAndAttributes._typeDescriptor()
          ),
          ToDafny.BatchGetRequestMap(nativeValue.unprocessedKeys())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            KeysAndAttributes._typeDescriptor()
          )
        );
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    return new BatchGetItemOutput(responses, unprocessedKeys, consumedCapacity);
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends KeysAndAttributes
  > BatchGetRequestMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.KeysAndAttributes
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::KeysAndAttributes
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<
      ? extends DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    >
  > BatchGetResponseMap(
    Map<
      String,
      List<
        Map<
          String,
          software.amazon.awssdk.services.dynamodb.model.AttributeValue
        >
      >
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ItemList
    );
  }

  public static BatchStatementError BatchStatementError(
    software.amazon.awssdk.services.dynamodb.model.BatchStatementError nativeValue
  ) {
    Option<BatchStatementErrorCodeEnum> code;
    code =
      Objects.nonNull(nativeValue.code())
        ? Option.create_Some(
          BatchStatementErrorCodeEnum._typeDescriptor(),
          ToDafny.BatchStatementErrorCodeEnum(nativeValue.code())
        )
        : Option.create_None(BatchStatementErrorCodeEnum._typeDescriptor());
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.message())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.message()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    return new BatchStatementError(code, message, item);
  }

  public static BatchStatementRequest BatchStatementRequest(
    software.amazon.awssdk.services.dynamodb.model.BatchStatementRequest nativeValue
  ) {
    DafnySequence<? extends Character> statement;
    statement =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.statement()
      );
    Option<DafnySequence<? extends AttributeValue>> parameters;
    parameters =
      (Objects.nonNull(nativeValue.parameters()) &&
          nativeValue.parameters().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor()),
          ToDafny.PreparedStatementParameters(nativeValue.parameters())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor())
        );
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new BatchStatementRequest(
      statement,
      parameters,
      consistentRead,
      returnValuesOnConditionCheckFailure
    );
  }

  public static BatchStatementResponse BatchStatementResponse(
    software.amazon.awssdk.services.dynamodb.model.BatchStatementResponse nativeValue
  ) {
    Option<BatchStatementError> error;
    error =
      Objects.nonNull(nativeValue.error())
        ? Option.create_Some(
          BatchStatementError._typeDescriptor(),
          ToDafny.BatchStatementError(nativeValue.error())
        )
        : Option.create_None(BatchStatementError._typeDescriptor());
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    return new BatchStatementResponse(error, tableName, item);
  }

  public static BatchWriteItemInput BatchWriteItemInput(
    BatchWriteItemRequest nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends DafnySequence<? extends WriteRequest>
    > requestItems;
    requestItems = ToDafny.BatchWriteItemRequestMap(nativeValue.requestItems());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<ReturnItemCollectionMetrics> returnItemCollectionMetrics;
    returnItemCollectionMetrics =
      Objects.nonNull(nativeValue.returnItemCollectionMetrics())
        ? Option.create_Some(
          ReturnItemCollectionMetrics._typeDescriptor(),
          ToDafny.ReturnItemCollectionMetrics(
            nativeValue.returnItemCollectionMetrics()
          )
        )
        : Option.create_None(ReturnItemCollectionMetrics._typeDescriptor());
    return new BatchWriteItemInput(
      requestItems,
      returnConsumedCapacity,
      returnItemCollectionMetrics
    );
  }

  public static BatchWriteItemOutput BatchWriteItemOutput(
    BatchWriteItemResponse nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends WriteRequest>
      >
    > unprocessedItems;
    unprocessedItems =
      (Objects.nonNull(nativeValue.unprocessedItems()) &&
          nativeValue.unprocessedItems().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(WriteRequest._typeDescriptor())
          ),
          ToDafny.BatchWriteItemRequestMap(nativeValue.unprocessedItems())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(WriteRequest._typeDescriptor())
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends ItemCollectionMetrics>
      >
    > itemCollectionMetrics;
    itemCollectionMetrics =
      (Objects.nonNull(nativeValue.itemCollectionMetrics()) &&
          nativeValue.itemCollectionMetrics().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              ItemCollectionMetrics._typeDescriptor()
            )
          ),
          ToDafny.ItemCollectionMetricsPerTable(
            nativeValue.itemCollectionMetrics()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              ItemCollectionMetrics._typeDescriptor()
            )
          )
        );
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    return new BatchWriteItemOutput(
      unprocessedItems,
      itemCollectionMetrics,
      consumedCapacity
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends WriteRequest>
  > BatchWriteItemRequestMap(
    Map<
      String,
      List<software.amazon.awssdk.services.dynamodb.model.WriteRequest>
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::WriteRequests
    );
  }

  public static BillingModeSummary BillingModeSummary(
    software.amazon.awssdk.services.dynamodb.model.BillingModeSummary nativeValue
  ) {
    Option<BillingMode> billingMode;
    billingMode =
      Objects.nonNull(nativeValue.billingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<
      DafnySequence<? extends Character>
    > lastUpdateToPayPerRequestDateTime;
    lastUpdateToPayPerRequestDateTime =
      Objects.nonNull(nativeValue.lastUpdateToPayPerRequestDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastUpdateToPayPerRequestDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new BillingModeSummary(
      billingMode,
      lastUpdateToPayPerRequestDateTime
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Byte>
  > BinarySetAttributeValue(List<ByteBuffer> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::ByteSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.BYTE)
    );
  }

  public static CancellationReason CancellationReason(
    software.amazon.awssdk.services.dynamodb.model.CancellationReason nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<DafnySequence<? extends Character>> code;
    code =
      Objects.nonNull(nativeValue.code())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.code()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.message())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.message()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new CancellationReason(item, code, message);
  }

  public static DafnySequence<
    ? extends CancellationReason
  > CancellationReasonList(
    List<
      software.amazon.awssdk.services.dynamodb.model.CancellationReason
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::CancellationReason,
      CancellationReason._typeDescriptor()
    );
  }

  public static Capacity Capacity(
    software.amazon.awssdk.services.dynamodb.model.Capacity nativeValue
  ) {
    Option<DafnySequence<? extends Byte>> readCapacityUnits;
    readCapacityUnits =
      Objects.nonNull(nativeValue.readCapacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.readCapacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    Option<DafnySequence<? extends Byte>> writeCapacityUnits;
    writeCapacityUnits =
      Objects.nonNull(nativeValue.writeCapacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.writeCapacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    Option<DafnySequence<? extends Byte>> capacityUnits;
    capacityUnits =
      Objects.nonNull(nativeValue.capacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.capacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    return new Capacity(readCapacityUnits, writeCapacityUnits, capacityUnits);
  }

  public static Condition Condition(
    software.amazon.awssdk.services.dynamodb.model.Condition nativeValue
  ) {
    Option<DafnySequence<? extends AttributeValue>> attributeValueList;
    attributeValueList =
      (Objects.nonNull(nativeValue.attributeValueList()) &&
          nativeValue.attributeValueList().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor()),
          ToDafny.AttributeValueList(nativeValue.attributeValueList())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor())
        );
    ComparisonOperator comparisonOperator;
    comparisonOperator =
      ToDafny.ComparisonOperator(nativeValue.comparisonOperator());
    return new Condition(attributeValueList, comparisonOperator);
  }

  public static ConditionCheck ConditionCheck(
    software.amazon.awssdk.services.dynamodb.model.ConditionCheck nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> conditionExpression;
    conditionExpression =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.conditionExpression()
      );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new ConditionCheck(
      key,
      tableName,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static ConsumedCapacity ConsumedCapacity(
    software.amazon.awssdk.services.dynamodb.model.ConsumedCapacity nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Byte>> capacityUnits;
    capacityUnits =
      Objects.nonNull(nativeValue.capacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.capacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    Option<DafnySequence<? extends Byte>> readCapacityUnits;
    readCapacityUnits =
      Objects.nonNull(nativeValue.readCapacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.readCapacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    Option<DafnySequence<? extends Byte>> writeCapacityUnits;
    writeCapacityUnits =
      Objects.nonNull(nativeValue.writeCapacityUnits())
        ? Option.create_Some(
          ConsumedCapacityUnits._typeDescriptor(),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.Double(
            nativeValue.writeCapacityUnits()
          )
        )
        : Option.create_None(ConsumedCapacityUnits._typeDescriptor());
    Option<Capacity> table;
    table =
      Objects.nonNull(nativeValue.table())
        ? Option.create_Some(
          Capacity._typeDescriptor(),
          ToDafny.Capacity(nativeValue.table())
        )
        : Option.create_None(Capacity._typeDescriptor());
    Option<
      DafnyMap<? extends DafnySequence<? extends Character>, ? extends Capacity>
    > localSecondaryIndexes;
    localSecondaryIndexes =
      (Objects.nonNull(nativeValue.localSecondaryIndexes()) &&
          nativeValue.localSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Capacity._typeDescriptor()
          ),
          ToDafny.SecondaryIndexesCapacityMap(
            nativeValue.localSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Capacity._typeDescriptor()
          )
        );
    Option<
      DafnyMap<? extends DafnySequence<? extends Character>, ? extends Capacity>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Capacity._typeDescriptor()
          ),
          ToDafny.SecondaryIndexesCapacityMap(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Capacity._typeDescriptor()
          )
        );
    return new ConsumedCapacity(
      tableName,
      capacityUnits,
      readCapacityUnits,
      writeCapacityUnits,
      table,
      localSecondaryIndexes,
      globalSecondaryIndexes
    );
  }

  public static DafnySequence<
    ? extends ConsumedCapacity
  > ConsumedCapacityMultiple(
    List<
      software.amazon.awssdk.services.dynamodb.model.ConsumedCapacity
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ConsumedCapacity,
      ConsumedCapacity._typeDescriptor()
    );
  }

  public static ContinuousBackupsDescription ContinuousBackupsDescription(
    software.amazon.awssdk.services.dynamodb.model.ContinuousBackupsDescription nativeValue
  ) {
    ContinuousBackupsStatus continuousBackupsStatus;
    continuousBackupsStatus =
      ToDafny.ContinuousBackupsStatus(nativeValue.continuousBackupsStatus());
    Option<PointInTimeRecoveryDescription> pointInTimeRecoveryDescription;
    pointInTimeRecoveryDescription =
      Objects.nonNull(nativeValue.pointInTimeRecoveryDescription())
        ? Option.create_Some(
          PointInTimeRecoveryDescription._typeDescriptor(),
          ToDafny.PointInTimeRecoveryDescription(
            nativeValue.pointInTimeRecoveryDescription()
          )
        )
        : Option.create_None(PointInTimeRecoveryDescription._typeDescriptor());
    return new ContinuousBackupsDescription(
      continuousBackupsStatus,
      pointInTimeRecoveryDescription
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > ContributorInsightsRuleList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static DafnySequence<
    ? extends ContributorInsightsSummary
  > ContributorInsightsSummaries(
    List<
      software.amazon.awssdk.services.dynamodb.model.ContributorInsightsSummary
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ContributorInsightsSummary,
      ContributorInsightsSummary._typeDescriptor()
    );
  }

  public static ContributorInsightsSummary ContributorInsightsSummary(
    software.amazon.awssdk.services.dynamodb.model.ContributorInsightsSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ContributorInsightsStatus> contributorInsightsStatus;
    contributorInsightsStatus =
      Objects.nonNull(nativeValue.contributorInsightsStatus())
        ? Option.create_Some(
          ContributorInsightsStatus._typeDescriptor(),
          ToDafny.ContributorInsightsStatus(
            nativeValue.contributorInsightsStatus()
          )
        )
        : Option.create_None(ContributorInsightsStatus._typeDescriptor());
    return new ContributorInsightsSummary(
      tableName,
      indexName,
      contributorInsightsStatus
    );
  }

  public static CreateBackupInput CreateBackupInput(
    CreateBackupRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> backupName;
    backupName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupName()
      );
    return new CreateBackupInput(tableName, backupName);
  }

  public static CreateBackupOutput CreateBackupOutput(
    CreateBackupResponse nativeValue
  ) {
    Option<BackupDetails> backupDetails;
    backupDetails =
      Objects.nonNull(nativeValue.backupDetails())
        ? Option.create_Some(
          BackupDetails._typeDescriptor(),
          ToDafny.BackupDetails(nativeValue.backupDetails())
        )
        : Option.create_None(BackupDetails._typeDescriptor());
    return new CreateBackupOutput(backupDetails);
  }

  public static CreateGlobalSecondaryIndexAction CreateGlobalSecondaryIndexAction(
    software.amazon.awssdk.services.dynamodb.model.CreateGlobalSecondaryIndexAction nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    Projection projection;
    projection = ToDafny.Projection(nativeValue.projection());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new CreateGlobalSecondaryIndexAction(
      indexName,
      keySchema,
      projection,
      provisionedThroughput,
      onDemandThroughput
    );
  }

  public static CreateGlobalTableInput CreateGlobalTableInput(
    CreateGlobalTableRequest nativeValue
  ) {
    DafnySequence<? extends Character> globalTableName;
    globalTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.globalTableName()
      );
    DafnySequence<? extends Replica> replicationGroup;
    replicationGroup = ToDafny.ReplicaList(nativeValue.replicationGroup());
    return new CreateGlobalTableInput(globalTableName, replicationGroup);
  }

  public static CreateGlobalTableOutput CreateGlobalTableOutput(
    CreateGlobalTableResponse nativeValue
  ) {
    Option<GlobalTableDescription> globalTableDescription;
    globalTableDescription =
      Objects.nonNull(nativeValue.globalTableDescription())
        ? Option.create_Some(
          GlobalTableDescription._typeDescriptor(),
          ToDafny.GlobalTableDescription(nativeValue.globalTableDescription())
        )
        : Option.create_None(GlobalTableDescription._typeDescriptor());
    return new CreateGlobalTableOutput(globalTableDescription);
  }

  public static CreateReplicaAction CreateReplicaAction(
    software.amazon.awssdk.services.dynamodb.model.CreateReplicaAction nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    return new CreateReplicaAction(regionName);
  }

  public static CreateReplicationGroupMemberAction CreateReplicationGroupMemberAction(
    software.amazon.awssdk.services.dynamodb.model.CreateReplicationGroupMemberAction nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    Option<DafnySequence<? extends Character>> kMSMasterKeyId;
    kMSMasterKeyId =
      Objects.nonNull(nativeValue.kmsMasterKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.kmsMasterKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ProvisionedThroughputOverride> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughputOverride._typeDescriptor(),
          ToDafny.ProvisionedThroughputOverride(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughputOverride._typeDescriptor());
    Option<OnDemandThroughputOverride> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughputOverride._typeDescriptor(),
          ToDafny.OnDemandThroughputOverride(
            nativeValue.onDemandThroughputOverride()
          )
        )
        : Option.create_None(OnDemandThroughputOverride._typeDescriptor());
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndex>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndex._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexList(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndex._typeDescriptor()
          )
        );
    Option<TableClass> tableClassOverride;
    tableClassOverride =
      Objects.nonNull(nativeValue.tableClassOverride())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.tableClassOverride())
        )
        : Option.create_None(TableClass._typeDescriptor());
    return new CreateReplicationGroupMemberAction(
      regionName,
      kMSMasterKeyId,
      provisionedThroughputOverride,
      onDemandThroughputOverride,
      globalSecondaryIndexes,
      tableClassOverride
    );
  }

  public static CreateTableInput CreateTableInput(
    CreateTableRequest nativeValue
  ) {
    DafnySequence<? extends AttributeDefinition> attributeDefinitions;
    attributeDefinitions =
      ToDafny.AttributeDefinitions(nativeValue.attributeDefinitions());
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    Option<DafnySequence<? extends LocalSecondaryIndex>> localSecondaryIndexes;
    localSecondaryIndexes =
      (Objects.nonNull(nativeValue.localSecondaryIndexes()) &&
          nativeValue.localSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor()),
          ToDafny.LocalSecondaryIndexList(nativeValue.localSecondaryIndexes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor())
        );
    Option<
      DafnySequence<? extends GlobalSecondaryIndex>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor()),
          ToDafny.GlobalSecondaryIndexList(nativeValue.globalSecondaryIndexes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor())
        );
    Option<BillingMode> billingMode;
    billingMode =
      Objects.nonNull(nativeValue.billingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<StreamSpecification> streamSpecification;
    streamSpecification =
      Objects.nonNull(nativeValue.streamSpecification())
        ? Option.create_Some(
          StreamSpecification._typeDescriptor(),
          ToDafny.StreamSpecification(nativeValue.streamSpecification())
        )
        : Option.create_None(StreamSpecification._typeDescriptor());
    Option<SSESpecification> sSESpecification;
    sSESpecification =
      Objects.nonNull(nativeValue.sseSpecification())
        ? Option.create_Some(
          SSESpecification._typeDescriptor(),
          ToDafny.SSESpecification(nativeValue.sseSpecification())
        )
        : Option.create_None(SSESpecification._typeDescriptor());
    Option<DafnySequence<? extends Tag>> tags;
    tags =
      (Objects.nonNull(nativeValue.tags()) && nativeValue.tags().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(Tag._typeDescriptor()),
          ToDafny.TagList(nativeValue.tags())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(Tag._typeDescriptor())
        );
    Option<TableClass> tableClass;
    tableClass =
      Objects.nonNull(nativeValue.tableClass())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.tableClass())
        )
        : Option.create_None(TableClass._typeDescriptor());
    Option<Boolean> deletionProtectionEnabled;
    deletionProtectionEnabled =
      Objects.nonNull(nativeValue.deletionProtectionEnabled())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.deletionProtectionEnabled())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> resourcePolicy;
    resourcePolicy =
      Objects.nonNull(nativeValue.resourcePolicy())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.resourcePolicy()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new CreateTableInput(
      attributeDefinitions,
      tableName,
      keySchema,
      localSecondaryIndexes,
      globalSecondaryIndexes,
      billingMode,
      provisionedThroughput,
      streamSpecification,
      sSESpecification,
      tags,
      tableClass,
      deletionProtectionEnabled,
      resourcePolicy,
      onDemandThroughput
    );
  }

  public static CreateTableOutput CreateTableOutput(
    CreateTableResponse nativeValue
  ) {
    Option<TableDescription> tableDescription;
    tableDescription =
      Objects.nonNull(nativeValue.tableDescription())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.tableDescription())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new CreateTableOutput(tableDescription);
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > CsvHeaderList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static CsvOptions CsvOptions(
    software.amazon.awssdk.services.dynamodb.model.CsvOptions nativeValue
  ) {
    Option<DafnySequence<? extends Character>> delimiter;
    delimiter =
      Objects.nonNull(nativeValue.delimiter())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.delimiter()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > headerList;
    headerList =
      (Objects.nonNull(nativeValue.headerList()) &&
          nativeValue.headerList().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.CsvHeaderList(nativeValue.headerList())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new CsvOptions(delimiter, headerList);
  }

  public static Delete Delete(
    software.amazon.awssdk.services.dynamodb.model.Delete nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new Delete(
      key,
      tableName,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static DeleteBackupInput DeleteBackupInput(
    DeleteBackupRequest nativeValue
  ) {
    DafnySequence<? extends Character> backupArn;
    backupArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupArn()
      );
    return new DeleteBackupInput(backupArn);
  }

  public static DeleteBackupOutput DeleteBackupOutput(
    DeleteBackupResponse nativeValue
  ) {
    Option<BackupDescription> backupDescription;
    backupDescription =
      Objects.nonNull(nativeValue.backupDescription())
        ? Option.create_Some(
          BackupDescription._typeDescriptor(),
          ToDafny.BackupDescription(nativeValue.backupDescription())
        )
        : Option.create_None(BackupDescription._typeDescriptor());
    return new DeleteBackupOutput(backupDescription);
  }

  public static DeleteGlobalSecondaryIndexAction DeleteGlobalSecondaryIndexAction(
    software.amazon.awssdk.services.dynamodb.model.DeleteGlobalSecondaryIndexAction nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    return new DeleteGlobalSecondaryIndexAction(indexName);
  }

  public static DeleteItemInput DeleteItemInput(DeleteItemRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends ExpectedAttributeValue
      >
    > expected;
    expected =
      (Objects.nonNull(nativeValue.expected()) &&
          nativeValue.expected().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          ),
          ToDafny.ExpectedAttributeMap(nativeValue.expected())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          )
        );
    Option<ConditionalOperator> conditionalOperator;
    conditionalOperator =
      Objects.nonNull(nativeValue.conditionalOperator())
        ? Option.create_Some(
          ConditionalOperator._typeDescriptor(),
          ToDafny.ConditionalOperator(nativeValue.conditionalOperator())
        )
        : Option.create_None(ConditionalOperator._typeDescriptor());
    Option<ReturnValue> returnValues;
    returnValues =
      Objects.nonNull(nativeValue.returnValues())
        ? Option.create_Some(
          ReturnValue._typeDescriptor(),
          ToDafny.ReturnValue(nativeValue.returnValues())
        )
        : Option.create_None(ReturnValue._typeDescriptor());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<ReturnItemCollectionMetrics> returnItemCollectionMetrics;
    returnItemCollectionMetrics =
      Objects.nonNull(nativeValue.returnItemCollectionMetrics())
        ? Option.create_Some(
          ReturnItemCollectionMetrics._typeDescriptor(),
          ToDafny.ReturnItemCollectionMetrics(
            nativeValue.returnItemCollectionMetrics()
          )
        )
        : Option.create_None(ReturnItemCollectionMetrics._typeDescriptor());
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new DeleteItemInput(
      tableName,
      key,
      expected,
      conditionalOperator,
      returnValues,
      returnConsumedCapacity,
      returnItemCollectionMetrics,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static DeleteItemOutput DeleteItemOutput(
    DeleteItemResponse nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > attributes;
    attributes =
      (Objects.nonNull(nativeValue.attributes()) &&
          nativeValue.attributes().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.attributes())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    Option<ItemCollectionMetrics> itemCollectionMetrics;
    itemCollectionMetrics =
      Objects.nonNull(nativeValue.itemCollectionMetrics())
        ? Option.create_Some(
          ItemCollectionMetrics._typeDescriptor(),
          ToDafny.ItemCollectionMetrics(nativeValue.itemCollectionMetrics())
        )
        : Option.create_None(ItemCollectionMetrics._typeDescriptor());
    return new DeleteItemOutput(
      attributes,
      consumedCapacity,
      itemCollectionMetrics
    );
  }

  public static DeleteReplicaAction DeleteReplicaAction(
    software.amazon.awssdk.services.dynamodb.model.DeleteReplicaAction nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    return new DeleteReplicaAction(regionName);
  }

  public static DeleteReplicationGroupMemberAction DeleteReplicationGroupMemberAction(
    software.amazon.awssdk.services.dynamodb.model.DeleteReplicationGroupMemberAction nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    return new DeleteReplicationGroupMemberAction(regionName);
  }

  public static DeleteRequest DeleteRequest(
    software.amazon.awssdk.services.dynamodb.model.DeleteRequest nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    return new DeleteRequest(key);
  }

  public static DeleteResourcePolicyInput DeleteResourcePolicyInput(
    DeleteResourcePolicyRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    Option<DafnySequence<? extends Character>> expectedRevisionId;
    expectedRevisionId =
      Objects.nonNull(nativeValue.expectedRevisionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.expectedRevisionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new DeleteResourcePolicyInput(resourceArn, expectedRevisionId);
  }

  public static DeleteResourcePolicyOutput DeleteResourcePolicyOutput(
    DeleteResourcePolicyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> revisionId;
    revisionId =
      Objects.nonNull(nativeValue.revisionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.revisionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new DeleteResourcePolicyOutput(revisionId);
  }

  public static DeleteTableInput DeleteTableInput(
    DeleteTableRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DeleteTableInput(tableName);
  }

  public static DeleteTableOutput DeleteTableOutput(
    DeleteTableResponse nativeValue
  ) {
    Option<TableDescription> tableDescription;
    tableDescription =
      Objects.nonNull(nativeValue.tableDescription())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.tableDescription())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new DeleteTableOutput(tableDescription);
  }

  public static DescribeBackupInput DescribeBackupInput(
    DescribeBackupRequest nativeValue
  ) {
    DafnySequence<? extends Character> backupArn;
    backupArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupArn()
      );
    return new DescribeBackupInput(backupArn);
  }

  public static DescribeBackupOutput DescribeBackupOutput(
    DescribeBackupResponse nativeValue
  ) {
    Option<BackupDescription> backupDescription;
    backupDescription =
      Objects.nonNull(nativeValue.backupDescription())
        ? Option.create_Some(
          BackupDescription._typeDescriptor(),
          ToDafny.BackupDescription(nativeValue.backupDescription())
        )
        : Option.create_None(BackupDescription._typeDescriptor());
    return new DescribeBackupOutput(backupDescription);
  }

  public static DescribeContinuousBackupsInput DescribeContinuousBackupsInput(
    DescribeContinuousBackupsRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DescribeContinuousBackupsInput(tableName);
  }

  public static DescribeContinuousBackupsOutput DescribeContinuousBackupsOutput(
    DescribeContinuousBackupsResponse nativeValue
  ) {
    Option<ContinuousBackupsDescription> continuousBackupsDescription;
    continuousBackupsDescription =
      Objects.nonNull(nativeValue.continuousBackupsDescription())
        ? Option.create_Some(
          ContinuousBackupsDescription._typeDescriptor(),
          ToDafny.ContinuousBackupsDescription(
            nativeValue.continuousBackupsDescription()
          )
        )
        : Option.create_None(ContinuousBackupsDescription._typeDescriptor());
    return new DescribeContinuousBackupsOutput(continuousBackupsDescription);
  }

  public static DescribeContributorInsightsInput DescribeContributorInsightsInput(
    DescribeContributorInsightsRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new DescribeContributorInsightsInput(tableName, indexName);
  }

  public static DescribeContributorInsightsOutput DescribeContributorInsightsOutput(
    DescribeContributorInsightsResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > contributorInsightsRuleList;
    contributorInsightsRuleList =
      (Objects.nonNull(nativeValue.contributorInsightsRuleList()) &&
          nativeValue.contributorInsightsRuleList().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ContributorInsightsRuleList(
            nativeValue.contributorInsightsRuleList()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<ContributorInsightsStatus> contributorInsightsStatus;
    contributorInsightsStatus =
      Objects.nonNull(nativeValue.contributorInsightsStatus())
        ? Option.create_Some(
          ContributorInsightsStatus._typeDescriptor(),
          ToDafny.ContributorInsightsStatus(
            nativeValue.contributorInsightsStatus()
          )
        )
        : Option.create_None(ContributorInsightsStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> lastUpdateDateTime;
    lastUpdateDateTime =
      Objects.nonNull(nativeValue.lastUpdateDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastUpdateDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<FailureException> failureException;
    failureException =
      Objects.nonNull(nativeValue.failureException())
        ? Option.create_Some(
          FailureException._typeDescriptor(),
          ToDafny.FailureException(nativeValue.failureException())
        )
        : Option.create_None(FailureException._typeDescriptor());
    return new DescribeContributorInsightsOutput(
      tableName,
      indexName,
      contributorInsightsRuleList,
      contributorInsightsStatus,
      lastUpdateDateTime,
      failureException
    );
  }

  public static DescribeEndpointsRequest DescribeEndpointsRequest(
    software.amazon.awssdk.services.dynamodb.model.DescribeEndpointsRequest nativeValue
  ) {
    return new DescribeEndpointsRequest();
  }

  public static DescribeEndpointsResponse DescribeEndpointsResponse(
    software.amazon.awssdk.services.dynamodb.model.DescribeEndpointsResponse nativeValue
  ) {
    DafnySequence<? extends Endpoint> endpoints;
    endpoints = ToDafny.Endpoints(nativeValue.endpoints());
    return new DescribeEndpointsResponse(endpoints);
  }

  public static DescribeExportInput DescribeExportInput(
    DescribeExportRequest nativeValue
  ) {
    DafnySequence<? extends Character> exportArn;
    exportArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.exportArn()
      );
    return new DescribeExportInput(exportArn);
  }

  public static DescribeExportOutput DescribeExportOutput(
    DescribeExportResponse nativeValue
  ) {
    Option<ExportDescription> exportDescription;
    exportDescription =
      Objects.nonNull(nativeValue.exportDescription())
        ? Option.create_Some(
          ExportDescription._typeDescriptor(),
          ToDafny.ExportDescription(nativeValue.exportDescription())
        )
        : Option.create_None(ExportDescription._typeDescriptor());
    return new DescribeExportOutput(exportDescription);
  }

  public static DescribeGlobalTableInput DescribeGlobalTableInput(
    DescribeGlobalTableRequest nativeValue
  ) {
    DafnySequence<? extends Character> globalTableName;
    globalTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.globalTableName()
      );
    return new DescribeGlobalTableInput(globalTableName);
  }

  public static DescribeGlobalTableOutput DescribeGlobalTableOutput(
    DescribeGlobalTableResponse nativeValue
  ) {
    Option<GlobalTableDescription> globalTableDescription;
    globalTableDescription =
      Objects.nonNull(nativeValue.globalTableDescription())
        ? Option.create_Some(
          GlobalTableDescription._typeDescriptor(),
          ToDafny.GlobalTableDescription(nativeValue.globalTableDescription())
        )
        : Option.create_None(GlobalTableDescription._typeDescriptor());
    return new DescribeGlobalTableOutput(globalTableDescription);
  }

  public static DescribeGlobalTableSettingsInput DescribeGlobalTableSettingsInput(
    DescribeGlobalTableSettingsRequest nativeValue
  ) {
    DafnySequence<? extends Character> globalTableName;
    globalTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.globalTableName()
      );
    return new DescribeGlobalTableSettingsInput(globalTableName);
  }

  public static DescribeGlobalTableSettingsOutput DescribeGlobalTableSettingsOutput(
    DescribeGlobalTableSettingsResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> globalTableName;
    globalTableName =
      Objects.nonNull(nativeValue.globalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends ReplicaSettingsDescription>> replicaSettings;
    replicaSettings =
      (Objects.nonNull(nativeValue.replicaSettings()) &&
          nativeValue.replicaSettings().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaSettingsDescription._typeDescriptor()
          ),
          ToDafny.ReplicaSettingsDescriptionList(nativeValue.replicaSettings())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaSettingsDescription._typeDescriptor()
          )
        );
    return new DescribeGlobalTableSettingsOutput(
      globalTableName,
      replicaSettings
    );
  }

  public static DescribeImportInput DescribeImportInput(
    DescribeImportRequest nativeValue
  ) {
    DafnySequence<? extends Character> importArn;
    importArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.importArn()
      );
    return new DescribeImportInput(importArn);
  }

  public static DescribeImportOutput DescribeImportOutput(
    DescribeImportResponse nativeValue
  ) {
    ImportTableDescription importTableDescription;
    importTableDescription =
      ToDafny.ImportTableDescription(nativeValue.importTableDescription());
    return new DescribeImportOutput(importTableDescription);
  }

  public static DescribeKinesisStreamingDestinationInput DescribeKinesisStreamingDestinationInput(
    DescribeKinesisStreamingDestinationRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DescribeKinesisStreamingDestinationInput(tableName);
  }

  public static DescribeKinesisStreamingDestinationOutput DescribeKinesisStreamingDestinationOutput(
    DescribeKinesisStreamingDestinationResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends KinesisDataStreamDestination>
    > kinesisDataStreamDestinations;
    kinesisDataStreamDestinations =
      (Objects.nonNull(nativeValue.kinesisDataStreamDestinations()) &&
          nativeValue.kinesisDataStreamDestinations().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            KinesisDataStreamDestination._typeDescriptor()
          ),
          ToDafny.KinesisDataStreamDestinations(
            nativeValue.kinesisDataStreamDestinations()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            KinesisDataStreamDestination._typeDescriptor()
          )
        );
    return new DescribeKinesisStreamingDestinationOutput(
      tableName,
      kinesisDataStreamDestinations
    );
  }

  public static DescribeLimitsInput DescribeLimitsInput(
    DescribeLimitsRequest nativeValue
  ) {
    return new DescribeLimitsInput();
  }

  public static DescribeLimitsOutput DescribeLimitsOutput(
    DescribeLimitsResponse nativeValue
  ) {
    Option<Long> accountMaxReadCapacityUnits;
    accountMaxReadCapacityUnits =
      Objects.nonNull(nativeValue.accountMaxReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.accountMaxReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> accountMaxWriteCapacityUnits;
    accountMaxWriteCapacityUnits =
      Objects.nonNull(nativeValue.accountMaxWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.accountMaxWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> tableMaxReadCapacityUnits;
    tableMaxReadCapacityUnits =
      Objects.nonNull(nativeValue.tableMaxReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.tableMaxReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> tableMaxWriteCapacityUnits;
    tableMaxWriteCapacityUnits =
      Objects.nonNull(nativeValue.tableMaxWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.tableMaxWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new DescribeLimitsOutput(
      accountMaxReadCapacityUnits,
      accountMaxWriteCapacityUnits,
      tableMaxReadCapacityUnits,
      tableMaxWriteCapacityUnits
    );
  }

  public static DescribeTableInput DescribeTableInput(
    DescribeTableRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DescribeTableInput(tableName);
  }

  public static DescribeTableOutput DescribeTableOutput(
    DescribeTableResponse nativeValue
  ) {
    Option<TableDescription> table;
    table =
      Objects.nonNull(nativeValue.table())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.table())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new DescribeTableOutput(table);
  }

  public static DescribeTableReplicaAutoScalingInput DescribeTableReplicaAutoScalingInput(
    DescribeTableReplicaAutoScalingRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DescribeTableReplicaAutoScalingInput(tableName);
  }

  public static DescribeTableReplicaAutoScalingOutput DescribeTableReplicaAutoScalingOutput(
    DescribeTableReplicaAutoScalingResponse nativeValue
  ) {
    Option<TableAutoScalingDescription> tableAutoScalingDescription;
    tableAutoScalingDescription =
      Objects.nonNull(nativeValue.tableAutoScalingDescription())
        ? Option.create_Some(
          TableAutoScalingDescription._typeDescriptor(),
          ToDafny.TableAutoScalingDescription(
            nativeValue.tableAutoScalingDescription()
          )
        )
        : Option.create_None(TableAutoScalingDescription._typeDescriptor());
    return new DescribeTableReplicaAutoScalingOutput(
      tableAutoScalingDescription
    );
  }

  public static DescribeTimeToLiveInput DescribeTimeToLiveInput(
    DescribeTimeToLiveRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    return new DescribeTimeToLiveInput(tableName);
  }

  public static DescribeTimeToLiveOutput DescribeTimeToLiveOutput(
    DescribeTimeToLiveResponse nativeValue
  ) {
    Option<TimeToLiveDescription> timeToLiveDescription;
    timeToLiveDescription =
      Objects.nonNull(nativeValue.timeToLiveDescription())
        ? Option.create_Some(
          TimeToLiveDescription._typeDescriptor(),
          ToDafny.TimeToLiveDescription(nativeValue.timeToLiveDescription())
        )
        : Option.create_None(TimeToLiveDescription._typeDescriptor());
    return new DescribeTimeToLiveOutput(timeToLiveDescription);
  }

  public static DisableKinesisStreamingDestinationInput DisableKinesisStreamingDestinationInput(
    DisableKinesisStreamingDestinationRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> streamArn;
    streamArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.streamArn()
      );
    Option<
      EnableKinesisStreamingConfiguration
    > enableKinesisStreamingConfiguration;
    enableKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.enableKinesisStreamingConfiguration())
        ? Option.create_Some(
          EnableKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.EnableKinesisStreamingConfiguration(
            nativeValue.enableKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          EnableKinesisStreamingConfiguration._typeDescriptor()
        );
    return new DisableKinesisStreamingDestinationInput(
      tableName,
      streamArn,
      enableKinesisStreamingConfiguration
    );
  }

  public static DisableKinesisStreamingDestinationOutput DisableKinesisStreamingDestinationOutput(
    DisableKinesisStreamingDestinationResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> streamArn;
    streamArn =
      Objects.nonNull(nativeValue.streamArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.streamArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DestinationStatus> destinationStatus;
    destinationStatus =
      Objects.nonNull(nativeValue.destinationStatus())
        ? Option.create_Some(
          DestinationStatus._typeDescriptor(),
          ToDafny.DestinationStatus(nativeValue.destinationStatus())
        )
        : Option.create_None(DestinationStatus._typeDescriptor());
    Option<
      EnableKinesisStreamingConfiguration
    > enableKinesisStreamingConfiguration;
    enableKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.enableKinesisStreamingConfiguration())
        ? Option.create_Some(
          EnableKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.EnableKinesisStreamingConfiguration(
            nativeValue.enableKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          EnableKinesisStreamingConfiguration._typeDescriptor()
        );
    return new DisableKinesisStreamingDestinationOutput(
      tableName,
      streamArn,
      destinationStatus,
      enableKinesisStreamingConfiguration
    );
  }

  public static EnableKinesisStreamingConfiguration EnableKinesisStreamingConfiguration(
    software.amazon.awssdk.services.dynamodb.model.EnableKinesisStreamingConfiguration nativeValue
  ) {
    Option<
      ApproximateCreationDateTimePrecision
    > approximateCreationDateTimePrecision;
    approximateCreationDateTimePrecision =
      Objects.nonNull(nativeValue.approximateCreationDateTimePrecision())
        ? Option.create_Some(
          ApproximateCreationDateTimePrecision._typeDescriptor(),
          ToDafny.ApproximateCreationDateTimePrecision(
            nativeValue.approximateCreationDateTimePrecision()
          )
        )
        : Option.create_None(
          ApproximateCreationDateTimePrecision._typeDescriptor()
        );
    return new EnableKinesisStreamingConfiguration(
      approximateCreationDateTimePrecision
    );
  }

  public static EnableKinesisStreamingDestinationInput EnableKinesisStreamingDestinationInput(
    EnableKinesisStreamingDestinationRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> streamArn;
    streamArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.streamArn()
      );
    Option<
      EnableKinesisStreamingConfiguration
    > enableKinesisStreamingConfiguration;
    enableKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.enableKinesisStreamingConfiguration())
        ? Option.create_Some(
          EnableKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.EnableKinesisStreamingConfiguration(
            nativeValue.enableKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          EnableKinesisStreamingConfiguration._typeDescriptor()
        );
    return new EnableKinesisStreamingDestinationInput(
      tableName,
      streamArn,
      enableKinesisStreamingConfiguration
    );
  }

  public static EnableKinesisStreamingDestinationOutput EnableKinesisStreamingDestinationOutput(
    EnableKinesisStreamingDestinationResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> streamArn;
    streamArn =
      Objects.nonNull(nativeValue.streamArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.streamArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DestinationStatus> destinationStatus;
    destinationStatus =
      Objects.nonNull(nativeValue.destinationStatus())
        ? Option.create_Some(
          DestinationStatus._typeDescriptor(),
          ToDafny.DestinationStatus(nativeValue.destinationStatus())
        )
        : Option.create_None(DestinationStatus._typeDescriptor());
    Option<
      EnableKinesisStreamingConfiguration
    > enableKinesisStreamingConfiguration;
    enableKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.enableKinesisStreamingConfiguration())
        ? Option.create_Some(
          EnableKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.EnableKinesisStreamingConfiguration(
            nativeValue.enableKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          EnableKinesisStreamingConfiguration._typeDescriptor()
        );
    return new EnableKinesisStreamingDestinationOutput(
      tableName,
      streamArn,
      destinationStatus,
      enableKinesisStreamingConfiguration
    );
  }

  public static Endpoint Endpoint(
    software.amazon.awssdk.services.dynamodb.model.Endpoint nativeValue
  ) {
    DafnySequence<? extends Character> address;
    address =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.address()
      );
    Long cachePeriodInMinutes;
    cachePeriodInMinutes = (nativeValue.cachePeriodInMinutes());
    return new Endpoint(address, cachePeriodInMinutes);
  }

  public static DafnySequence<? extends Endpoint> Endpoints(
    List<software.amazon.awssdk.services.dynamodb.model.Endpoint> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Endpoint,
      Endpoint._typeDescriptor()
    );
  }

  public static ExecuteStatementInput ExecuteStatementInput(
    ExecuteStatementRequest nativeValue
  ) {
    DafnySequence<? extends Character> statement;
    statement =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.statement()
      );
    Option<DafnySequence<? extends AttributeValue>> parameters;
    parameters =
      (Objects.nonNull(nativeValue.parameters()) &&
          nativeValue.parameters().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor()),
          ToDafny.PreparedStatementParameters(nativeValue.parameters())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor())
        );
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new ExecuteStatementInput(
      statement,
      parameters,
      consistentRead,
      nextToken,
      returnConsumedCapacity,
      limit,
      returnValuesOnConditionCheckFailure
    );
  }

  public static ExecuteStatementOutput ExecuteStatementOutput(
    ExecuteStatementResponse nativeValue
  ) {
    Option<
      DafnySequence<
        ? extends DafnyMap<
          ? extends DafnySequence<? extends Character>,
          ? extends AttributeValue
        >
      >
    > items;
    items =
      (Objects.nonNull(nativeValue.items()) && nativeValue.items().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          ),
          ToDafny.ItemList(nativeValue.items())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          )
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > lastEvaluatedKey;
    lastEvaluatedKey =
      (Objects.nonNull(nativeValue.lastEvaluatedKey()) &&
          nativeValue.lastEvaluatedKey().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.Key(nativeValue.lastEvaluatedKey())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    return new ExecuteStatementOutput(
      items,
      nextToken,
      consumedCapacity,
      lastEvaluatedKey
    );
  }

  public static ExecuteTransactionInput ExecuteTransactionInput(
    ExecuteTransactionRequest nativeValue
  ) {
    DafnySequence<? extends ParameterizedStatement> transactStatements;
    transactStatements =
      ToDafny.ParameterizedStatements(nativeValue.transactStatements());
    Option<DafnySequence<? extends Character>> clientRequestToken;
    clientRequestToken =
      Objects.nonNull(nativeValue.clientRequestToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientRequestToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    return new ExecuteTransactionInput(
      transactStatements,
      clientRequestToken,
      returnConsumedCapacity
    );
  }

  public static ExecuteTransactionOutput ExecuteTransactionOutput(
    ExecuteTransactionResponse nativeValue
  ) {
    Option<DafnySequence<? extends ItemResponse>> responses;
    responses =
      (Objects.nonNull(nativeValue.responses()) &&
          nativeValue.responses().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ItemResponse._typeDescriptor()),
          ToDafny.ItemResponseList(nativeValue.responses())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ItemResponse._typeDescriptor())
        );
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    return new ExecuteTransactionOutput(responses, consumedCapacity);
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends ExpectedAttributeValue
  > ExpectedAttributeMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.ExpectedAttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ExpectedAttributeValue
    );
  }

  public static ExpectedAttributeValue ExpectedAttributeValue(
    software.amazon.awssdk.services.dynamodb.model.ExpectedAttributeValue nativeValue
  ) {
    Option<AttributeValue> value;
    value =
      Objects.nonNull(nativeValue.value())
        ? Option.create_Some(
          AttributeValue._typeDescriptor(),
          ToDafny.AttributeValue(nativeValue.value())
        )
        : Option.create_None(AttributeValue._typeDescriptor());
    Option<Boolean> exists;
    exists =
      Objects.nonNull(nativeValue.exists())
        ? Option.create_Some(TypeDescriptor.BOOLEAN, (nativeValue.exists()))
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<ComparisonOperator> comparisonOperator;
    comparisonOperator =
      Objects.nonNull(nativeValue.comparisonOperator())
        ? Option.create_Some(
          ComparisonOperator._typeDescriptor(),
          ToDafny.ComparisonOperator(nativeValue.comparisonOperator())
        )
        : Option.create_None(ComparisonOperator._typeDescriptor());
    Option<DafnySequence<? extends AttributeValue>> attributeValueList;
    attributeValueList =
      (Objects.nonNull(nativeValue.attributeValueList()) &&
          nativeValue.attributeValueList().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor()),
          ToDafny.AttributeValueList(nativeValue.attributeValueList())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor())
        );
    return new ExpectedAttributeValue(
      value,
      exists,
      comparisonOperator,
      attributeValueList
    );
  }

  public static ExportDescription ExportDescription(
    software.amazon.awssdk.services.dynamodb.model.ExportDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> exportArn;
    exportArn =
      Objects.nonNull(nativeValue.exportArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ExportStatus> exportStatus;
    exportStatus =
      Objects.nonNull(nativeValue.exportStatus())
        ? Option.create_Some(
          ExportStatus._typeDescriptor(),
          ToDafny.ExportStatus(nativeValue.exportStatus())
        )
        : Option.create_None(ExportStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> startTime;
    startTime =
      Objects.nonNull(nativeValue.startTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.startTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> endTime;
    endTime =
      Objects.nonNull(nativeValue.endTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.endTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> exportManifest;
    exportManifest =
      Objects.nonNull(nativeValue.exportManifest())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportManifest()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableId;
    tableId =
      Objects.nonNull(nativeValue.tableId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> exportTime;
    exportTime =
      Objects.nonNull(nativeValue.exportTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> clientToken;
    clientToken =
      Objects.nonNull(nativeValue.clientToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> s3Bucket;
    s3Bucket =
      Objects.nonNull(nativeValue.s3Bucket())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3Bucket()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> s3BucketOwner;
    s3BucketOwner =
      Objects.nonNull(nativeValue.s3BucketOwner())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3BucketOwner()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> s3Prefix;
    s3Prefix =
      Objects.nonNull(nativeValue.s3Prefix())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3Prefix()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<S3SseAlgorithm> s3SseAlgorithm;
    s3SseAlgorithm =
      Objects.nonNull(nativeValue.s3SseAlgorithm())
        ? Option.create_Some(
          S3SseAlgorithm._typeDescriptor(),
          ToDafny.S3SseAlgorithm(nativeValue.s3SseAlgorithm())
        )
        : Option.create_None(S3SseAlgorithm._typeDescriptor());
    Option<DafnySequence<? extends Character>> s3SseKmsKeyId;
    s3SseKmsKeyId =
      Objects.nonNull(nativeValue.s3SseKmsKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3SseKmsKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> failureCode;
    failureCode =
      Objects.nonNull(nativeValue.failureCode())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.failureCode()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> failureMessage;
    failureMessage =
      Objects.nonNull(nativeValue.failureMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.failureMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ExportFormat> exportFormat;
    exportFormat =
      Objects.nonNull(nativeValue.exportFormat())
        ? Option.create_Some(
          ExportFormat._typeDescriptor(),
          ToDafny.ExportFormat(nativeValue.exportFormat())
        )
        : Option.create_None(ExportFormat._typeDescriptor());
    Option<Long> billedSizeBytes;
    billedSizeBytes =
      Objects.nonNull(nativeValue.billedSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.billedSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> itemCount;
    itemCount =
      Objects.nonNull(nativeValue.itemCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.itemCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<ExportType> exportType;
    exportType =
      Objects.nonNull(nativeValue.exportType())
        ? Option.create_Some(
          ExportType._typeDescriptor(),
          ToDafny.ExportType(nativeValue.exportType())
        )
        : Option.create_None(ExportType._typeDescriptor());
    Option<IncrementalExportSpecification> incrementalExportSpecification;
    incrementalExportSpecification =
      Objects.nonNull(nativeValue.incrementalExportSpecification())
        ? Option.create_Some(
          IncrementalExportSpecification._typeDescriptor(),
          ToDafny.IncrementalExportSpecification(
            nativeValue.incrementalExportSpecification()
          )
        )
        : Option.create_None(IncrementalExportSpecification._typeDescriptor());
    return new ExportDescription(
      exportArn,
      exportStatus,
      startTime,
      endTime,
      exportManifest,
      tableArn,
      tableId,
      exportTime,
      clientToken,
      s3Bucket,
      s3BucketOwner,
      s3Prefix,
      s3SseAlgorithm,
      s3SseKmsKeyId,
      failureCode,
      failureMessage,
      exportFormat,
      billedSizeBytes,
      itemCount,
      exportType,
      incrementalExportSpecification
    );
  }

  public static DafnySequence<? extends ExportSummary> ExportSummaries(
    List<
      software.amazon.awssdk.services.dynamodb.model.ExportSummary
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ExportSummary,
      ExportSummary._typeDescriptor()
    );
  }

  public static ExportSummary ExportSummary(
    software.amazon.awssdk.services.dynamodb.model.ExportSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> exportArn;
    exportArn =
      Objects.nonNull(nativeValue.exportArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ExportStatus> exportStatus;
    exportStatus =
      Objects.nonNull(nativeValue.exportStatus())
        ? Option.create_Some(
          ExportStatus._typeDescriptor(),
          ToDafny.ExportStatus(nativeValue.exportStatus())
        )
        : Option.create_None(ExportStatus._typeDescriptor());
    Option<ExportType> exportType;
    exportType =
      Objects.nonNull(nativeValue.exportType())
        ? Option.create_Some(
          ExportType._typeDescriptor(),
          ToDafny.ExportType(nativeValue.exportType())
        )
        : Option.create_None(ExportType._typeDescriptor());
    return new ExportSummary(exportArn, exportStatus, exportType);
  }

  public static ExportTableToPointInTimeInput ExportTableToPointInTimeInput(
    ExportTableToPointInTimeRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableArn;
    tableArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableArn()
      );
    Option<DafnySequence<? extends Character>> exportTime;
    exportTime =
      Objects.nonNull(nativeValue.exportTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> clientToken;
    clientToken =
      Objects.nonNull(nativeValue.clientToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    DafnySequence<? extends Character> s3Bucket;
    s3Bucket =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.s3Bucket()
      );
    Option<DafnySequence<? extends Character>> s3BucketOwner;
    s3BucketOwner =
      Objects.nonNull(nativeValue.s3BucketOwner())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3BucketOwner()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> s3Prefix;
    s3Prefix =
      Objects.nonNull(nativeValue.s3Prefix())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3Prefix()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<S3SseAlgorithm> s3SseAlgorithm;
    s3SseAlgorithm =
      Objects.nonNull(nativeValue.s3SseAlgorithm())
        ? Option.create_Some(
          S3SseAlgorithm._typeDescriptor(),
          ToDafny.S3SseAlgorithm(nativeValue.s3SseAlgorithm())
        )
        : Option.create_None(S3SseAlgorithm._typeDescriptor());
    Option<DafnySequence<? extends Character>> s3SseKmsKeyId;
    s3SseKmsKeyId =
      Objects.nonNull(nativeValue.s3SseKmsKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3SseKmsKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ExportFormat> exportFormat;
    exportFormat =
      Objects.nonNull(nativeValue.exportFormat())
        ? Option.create_Some(
          ExportFormat._typeDescriptor(),
          ToDafny.ExportFormat(nativeValue.exportFormat())
        )
        : Option.create_None(ExportFormat._typeDescriptor());
    Option<ExportType> exportType;
    exportType =
      Objects.nonNull(nativeValue.exportType())
        ? Option.create_Some(
          ExportType._typeDescriptor(),
          ToDafny.ExportType(nativeValue.exportType())
        )
        : Option.create_None(ExportType._typeDescriptor());
    Option<IncrementalExportSpecification> incrementalExportSpecification;
    incrementalExportSpecification =
      Objects.nonNull(nativeValue.incrementalExportSpecification())
        ? Option.create_Some(
          IncrementalExportSpecification._typeDescriptor(),
          ToDafny.IncrementalExportSpecification(
            nativeValue.incrementalExportSpecification()
          )
        )
        : Option.create_None(IncrementalExportSpecification._typeDescriptor());
    return new ExportTableToPointInTimeInput(
      tableArn,
      exportTime,
      clientToken,
      s3Bucket,
      s3BucketOwner,
      s3Prefix,
      s3SseAlgorithm,
      s3SseKmsKeyId,
      exportFormat,
      exportType,
      incrementalExportSpecification
    );
  }

  public static ExportTableToPointInTimeOutput ExportTableToPointInTimeOutput(
    ExportTableToPointInTimeResponse nativeValue
  ) {
    Option<ExportDescription> exportDescription;
    exportDescription =
      Objects.nonNull(nativeValue.exportDescription())
        ? Option.create_Some(
          ExportDescription._typeDescriptor(),
          ToDafny.ExportDescription(nativeValue.exportDescription())
        )
        : Option.create_None(ExportDescription._typeDescriptor());
    return new ExportTableToPointInTimeOutput(exportDescription);
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends Character>
  > ExpressionAttributeNameMap(Map<String, String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > ExpressionAttributeValueMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static FailureException FailureException(
    software.amazon.awssdk.services.dynamodb.model.FailureException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> exceptionName;
    exceptionName =
      Objects.nonNull(nativeValue.exceptionName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exceptionName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> exceptionDescription;
    exceptionDescription =
      Objects.nonNull(nativeValue.exceptionDescription())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exceptionDescription()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new FailureException(exceptionName, exceptionDescription);
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends Condition
  > FilterConditionMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.Condition
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Condition
    );
  }

  public static Get Get(
    software.amazon.awssdk.services.dynamodb.model.Get nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> projectionExpression;
    projectionExpression =
      Objects.nonNull(nativeValue.projectionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.projectionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new Get(
      key,
      tableName,
      projectionExpression,
      expressionAttributeNames
    );
  }

  public static GetItemInput GetItemInput(GetItemRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > attributesToGet;
    attributesToGet =
      (Objects.nonNull(nativeValue.attributesToGet()) &&
          nativeValue.attributesToGet().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.AttributeNameList(nativeValue.attributesToGet())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<DafnySequence<? extends Character>> projectionExpression;
    projectionExpression =
      Objects.nonNull(nativeValue.projectionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.projectionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new GetItemInput(
      tableName,
      key,
      attributesToGet,
      consistentRead,
      returnConsumedCapacity,
      projectionExpression,
      expressionAttributeNames
    );
  }

  public static GetItemOutput GetItemOutput(GetItemResponse nativeValue) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    return new GetItemOutput(item, consumedCapacity);
  }

  public static GetResourcePolicyInput GetResourcePolicyInput(
    GetResourcePolicyRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    return new GetResourcePolicyInput(resourceArn);
  }

  public static GetResourcePolicyOutput GetResourcePolicyOutput(
    GetResourcePolicyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> policy;
    policy =
      Objects.nonNull(nativeValue.policy())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.policy()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> revisionId;
    revisionId =
      Objects.nonNull(nativeValue.revisionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.revisionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new GetResourcePolicyOutput(policy, revisionId);
  }

  public static GlobalSecondaryIndex GlobalSecondaryIndex(
    software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndex nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    Projection projection;
    projection = ToDafny.Projection(nativeValue.projection());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new GlobalSecondaryIndex(
      indexName,
      keySchema,
      projection,
      provisionedThroughput,
      onDemandThroughput
    );
  }

  public static GlobalSecondaryIndexAutoScalingUpdate GlobalSecondaryIndexAutoScalingUpdate(
    software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexAutoScalingUpdate nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<AutoScalingSettingsUpdate> provisionedWriteCapacityAutoScalingUpdate;
    provisionedWriteCapacityAutoScalingUpdate =
      Objects.nonNull(nativeValue.provisionedWriteCapacityAutoScalingUpdate())
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.provisionedWriteCapacityAutoScalingUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    return new GlobalSecondaryIndexAutoScalingUpdate(
      indexName,
      provisionedWriteCapacityAutoScalingUpdate
    );
  }

  public static DafnySequence<
    ? extends GlobalSecondaryIndexAutoScalingUpdate
  > GlobalSecondaryIndexAutoScalingUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexAutoScalingUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalSecondaryIndexAutoScalingUpdate,
      GlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
    );
  }

  public static GlobalSecondaryIndexDescription GlobalSecondaryIndexDescription(
    software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends KeySchemaElement>> keySchema;
    keySchema =
      (Objects.nonNull(nativeValue.keySchema()) &&
          nativeValue.keySchema().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor()),
          ToDafny.KeySchema(nativeValue.keySchema())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor())
        );
    Option<Projection> projection;
    projection =
      Objects.nonNull(nativeValue.projection())
        ? Option.create_Some(
          Projection._typeDescriptor(),
          ToDafny.Projection(nativeValue.projection())
        )
        : Option.create_None(Projection._typeDescriptor());
    Option<IndexStatus> indexStatus;
    indexStatus =
      Objects.nonNull(nativeValue.indexStatus())
        ? Option.create_Some(
          IndexStatus._typeDescriptor(),
          ToDafny.IndexStatus(nativeValue.indexStatus())
        )
        : Option.create_None(IndexStatus._typeDescriptor());
    Option<Boolean> backfilling;
    backfilling =
      Objects.nonNull(nativeValue.backfilling())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.backfilling())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<ProvisionedThroughputDescription> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughputDescription._typeDescriptor(),
          ToDafny.ProvisionedThroughputDescription(
            nativeValue.provisionedThroughput()
          )
        )
        : Option.create_None(
          ProvisionedThroughputDescription._typeDescriptor()
        );
    Option<Long> indexSizeBytes;
    indexSizeBytes =
      Objects.nonNull(nativeValue.indexSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.indexSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> itemCount;
    itemCount =
      Objects.nonNull(nativeValue.itemCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.itemCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<DafnySequence<? extends Character>> indexArn;
    indexArn =
      Objects.nonNull(nativeValue.indexArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new GlobalSecondaryIndexDescription(
      indexName,
      keySchema,
      projection,
      indexStatus,
      backfilling,
      provisionedThroughput,
      indexSizeBytes,
      itemCount,
      indexArn,
      onDemandThroughput
    );
  }

  public static DafnySequence<
    ? extends GlobalSecondaryIndexDescription
  > GlobalSecondaryIndexDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalSecondaryIndexDescription,
      GlobalSecondaryIndexDescription._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends GlobalSecondaryIndexInfo
  > GlobalSecondaryIndexes(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexInfo
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalSecondaryIndexInfo,
      GlobalSecondaryIndexInfo._typeDescriptor()
    );
  }

  public static GlobalSecondaryIndexInfo GlobalSecondaryIndexInfo(
    software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexInfo nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends KeySchemaElement>> keySchema;
    keySchema =
      (Objects.nonNull(nativeValue.keySchema()) &&
          nativeValue.keySchema().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor()),
          ToDafny.KeySchema(nativeValue.keySchema())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor())
        );
    Option<Projection> projection;
    projection =
      Objects.nonNull(nativeValue.projection())
        ? Option.create_Some(
          Projection._typeDescriptor(),
          ToDafny.Projection(nativeValue.projection())
        )
        : Option.create_None(Projection._typeDescriptor());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new GlobalSecondaryIndexInfo(
      indexName,
      keySchema,
      projection,
      provisionedThroughput,
      onDemandThroughput
    );
  }

  public static DafnySequence<
    ? extends GlobalSecondaryIndex
  > GlobalSecondaryIndexList(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndex
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalSecondaryIndex,
      GlobalSecondaryIndex._typeDescriptor()
    );
  }

  public static GlobalSecondaryIndexUpdate GlobalSecondaryIndexUpdate(
    software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexUpdate nativeValue
  ) {
    Option<UpdateGlobalSecondaryIndexAction> update;
    update =
      Objects.nonNull(nativeValue.update())
        ? Option.create_Some(
          UpdateGlobalSecondaryIndexAction._typeDescriptor(),
          ToDafny.UpdateGlobalSecondaryIndexAction(nativeValue.update())
        )
        : Option.create_None(
          UpdateGlobalSecondaryIndexAction._typeDescriptor()
        );
    Option<CreateGlobalSecondaryIndexAction> create;
    create =
      Objects.nonNull(nativeValue.create())
        ? Option.create_Some(
          CreateGlobalSecondaryIndexAction._typeDescriptor(),
          ToDafny.CreateGlobalSecondaryIndexAction(nativeValue.create())
        )
        : Option.create_None(
          CreateGlobalSecondaryIndexAction._typeDescriptor()
        );
    Option<DeleteGlobalSecondaryIndexAction> delete;
    delete =
      Objects.nonNull(nativeValue.delete())
        ? Option.create_Some(
          DeleteGlobalSecondaryIndexAction._typeDescriptor(),
          ToDafny.DeleteGlobalSecondaryIndexAction(nativeValue.delete())
        )
        : Option.create_None(
          DeleteGlobalSecondaryIndexAction._typeDescriptor()
        );
    return new GlobalSecondaryIndexUpdate(update, create, delete);
  }

  public static DafnySequence<
    ? extends GlobalSecondaryIndexUpdate
  > GlobalSecondaryIndexUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalSecondaryIndexUpdate,
      GlobalSecondaryIndexUpdate._typeDescriptor()
    );
  }

  public static GlobalTable GlobalTable(
    software.amazon.awssdk.services.dynamodb.model.GlobalTable nativeValue
  ) {
    Option<DafnySequence<? extends Character>> globalTableName;
    globalTableName =
      Objects.nonNull(nativeValue.globalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Replica>> replicationGroup;
    replicationGroup =
      (Objects.nonNull(nativeValue.replicationGroup()) &&
          nativeValue.replicationGroup().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(Replica._typeDescriptor()),
          ToDafny.ReplicaList(nativeValue.replicationGroup())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(Replica._typeDescriptor())
        );
    return new GlobalTable(globalTableName, replicationGroup);
  }

  public static GlobalTableDescription GlobalTableDescription(
    software.amazon.awssdk.services.dynamodb.model.GlobalTableDescription nativeValue
  ) {
    Option<DafnySequence<? extends ReplicaDescription>> replicationGroup;
    replicationGroup =
      (Objects.nonNull(nativeValue.replicationGroup()) &&
          nativeValue.replicationGroup().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ReplicaDescription._typeDescriptor()),
          ToDafny.ReplicaDescriptionList(nativeValue.replicationGroup())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ReplicaDescription._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> globalTableArn;
    globalTableArn =
      Objects.nonNull(nativeValue.globalTableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> creationDateTime;
    creationDateTime =
      Objects.nonNull(nativeValue.creationDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<GlobalTableStatus> globalTableStatus;
    globalTableStatus =
      Objects.nonNull(nativeValue.globalTableStatus())
        ? Option.create_Some(
          GlobalTableStatus._typeDescriptor(),
          ToDafny.GlobalTableStatus(nativeValue.globalTableStatus())
        )
        : Option.create_None(GlobalTableStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> globalTableName;
    globalTableName =
      Objects.nonNull(nativeValue.globalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new GlobalTableDescription(
      replicationGroup,
      globalTableArn,
      creationDateTime,
      globalTableStatus,
      globalTableName
    );
  }

  public static GlobalTableGlobalSecondaryIndexSettingsUpdate GlobalTableGlobalSecondaryIndexSettingsUpdate(
    software.amazon.awssdk.services.dynamodb.model.GlobalTableGlobalSecondaryIndexSettingsUpdate nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    Option<Long> provisionedWriteCapacityUnits;
    provisionedWriteCapacityUnits =
      Objects.nonNull(nativeValue.provisionedWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.provisionedWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsUpdate
    > provisionedWriteCapacityAutoScalingSettingsUpdate;
    provisionedWriteCapacityAutoScalingSettingsUpdate =
      Objects.nonNull(
          nativeValue.provisionedWriteCapacityAutoScalingSettingsUpdate()
        )
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.provisionedWriteCapacityAutoScalingSettingsUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    return new GlobalTableGlobalSecondaryIndexSettingsUpdate(
      indexName,
      provisionedWriteCapacityUnits,
      provisionedWriteCapacityAutoScalingSettingsUpdate
    );
  }

  public static DafnySequence<
    ? extends GlobalTableGlobalSecondaryIndexSettingsUpdate
  > GlobalTableGlobalSecondaryIndexSettingsUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.GlobalTableGlobalSecondaryIndexSettingsUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalTableGlobalSecondaryIndexSettingsUpdate,
      GlobalTableGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
    );
  }

  public static DafnySequence<? extends GlobalTable> GlobalTableList(
    List<software.amazon.awssdk.services.dynamodb.model.GlobalTable> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::GlobalTable,
      GlobalTable._typeDescriptor()
    );
  }

  public static ImportSummary ImportSummary(
    software.amazon.awssdk.services.dynamodb.model.ImportSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> importArn;
    importArn =
      Objects.nonNull(nativeValue.importArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.importArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ImportStatus> importStatus;
    importStatus =
      Objects.nonNull(nativeValue.importStatus())
        ? Option.create_Some(
          ImportStatus._typeDescriptor(),
          ToDafny.ImportStatus(nativeValue.importStatus())
        )
        : Option.create_None(ImportStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<S3BucketSource> s3BucketSource;
    s3BucketSource =
      Objects.nonNull(nativeValue.s3BucketSource())
        ? Option.create_Some(
          S3BucketSource._typeDescriptor(),
          ToDafny.S3BucketSource(nativeValue.s3BucketSource())
        )
        : Option.create_None(S3BucketSource._typeDescriptor());
    Option<DafnySequence<? extends Character>> cloudWatchLogGroupArn;
    cloudWatchLogGroupArn =
      Objects.nonNull(nativeValue.cloudWatchLogGroupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudWatchLogGroupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<InputFormat> inputFormat;
    inputFormat =
      Objects.nonNull(nativeValue.inputFormat())
        ? Option.create_Some(
          InputFormat._typeDescriptor(),
          ToDafny.InputFormat(nativeValue.inputFormat())
        )
        : Option.create_None(InputFormat._typeDescriptor());
    Option<DafnySequence<? extends Character>> startTime;
    startTime =
      Objects.nonNull(nativeValue.startTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.startTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> endTime;
    endTime =
      Objects.nonNull(nativeValue.endTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.endTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ImportSummary(
      importArn,
      importStatus,
      tableArn,
      s3BucketSource,
      cloudWatchLogGroupArn,
      inputFormat,
      startTime,
      endTime
    );
  }

  public static DafnySequence<? extends ImportSummary> ImportSummaryList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ImportSummary
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ImportSummary,
      ImportSummary._typeDescriptor()
    );
  }

  public static ImportTableDescription ImportTableDescription(
    software.amazon.awssdk.services.dynamodb.model.ImportTableDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> importArn;
    importArn =
      Objects.nonNull(nativeValue.importArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.importArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ImportStatus> importStatus;
    importStatus =
      Objects.nonNull(nativeValue.importStatus())
        ? Option.create_Some(
          ImportStatus._typeDescriptor(),
          ToDafny.ImportStatus(nativeValue.importStatus())
        )
        : Option.create_None(ImportStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableId;
    tableId =
      Objects.nonNull(nativeValue.tableId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> clientToken;
    clientToken =
      Objects.nonNull(nativeValue.clientToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<S3BucketSource> s3BucketSource;
    s3BucketSource =
      Objects.nonNull(nativeValue.s3BucketSource())
        ? Option.create_Some(
          S3BucketSource._typeDescriptor(),
          ToDafny.S3BucketSource(nativeValue.s3BucketSource())
        )
        : Option.create_None(S3BucketSource._typeDescriptor());
    Option<Long> errorCount;
    errorCount =
      Objects.nonNull(nativeValue.errorCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.errorCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<DafnySequence<? extends Character>> cloudWatchLogGroupArn;
    cloudWatchLogGroupArn =
      Objects.nonNull(nativeValue.cloudWatchLogGroupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.cloudWatchLogGroupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<InputFormat> inputFormat;
    inputFormat =
      Objects.nonNull(nativeValue.inputFormat())
        ? Option.create_Some(
          InputFormat._typeDescriptor(),
          ToDafny.InputFormat(nativeValue.inputFormat())
        )
        : Option.create_None(InputFormat._typeDescriptor());
    Option<InputFormatOptions> inputFormatOptions;
    inputFormatOptions =
      Objects.nonNull(nativeValue.inputFormatOptions())
        ? Option.create_Some(
          InputFormatOptions._typeDescriptor(),
          ToDafny.InputFormatOptions(nativeValue.inputFormatOptions())
        )
        : Option.create_None(InputFormatOptions._typeDescriptor());
    Option<InputCompressionType> inputCompressionType;
    inputCompressionType =
      Objects.nonNull(nativeValue.inputCompressionType())
        ? Option.create_Some(
          InputCompressionType._typeDescriptor(),
          ToDafny.InputCompressionType(nativeValue.inputCompressionType())
        )
        : Option.create_None(InputCompressionType._typeDescriptor());
    Option<TableCreationParameters> tableCreationParameters;
    tableCreationParameters =
      Objects.nonNull(nativeValue.tableCreationParameters())
        ? Option.create_Some(
          TableCreationParameters._typeDescriptor(),
          ToDafny.TableCreationParameters(nativeValue.tableCreationParameters())
        )
        : Option.create_None(TableCreationParameters._typeDescriptor());
    Option<DafnySequence<? extends Character>> startTime;
    startTime =
      Objects.nonNull(nativeValue.startTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.startTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> endTime;
    endTime =
      Objects.nonNull(nativeValue.endTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.endTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Long> processedSizeBytes;
    processedSizeBytes =
      Objects.nonNull(nativeValue.processedSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.processedSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> processedItemCount;
    processedItemCount =
      Objects.nonNull(nativeValue.processedItemCount())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.processedItemCount())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> importedItemCount;
    importedItemCount =
      Objects.nonNull(nativeValue.importedItemCount())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.importedItemCount())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<DafnySequence<? extends Character>> failureCode;
    failureCode =
      Objects.nonNull(nativeValue.failureCode())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.failureCode()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> failureMessage;
    failureMessage =
      Objects.nonNull(nativeValue.failureMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.failureMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ImportTableDescription(
      importArn,
      importStatus,
      tableArn,
      tableId,
      clientToken,
      s3BucketSource,
      errorCount,
      cloudWatchLogGroupArn,
      inputFormat,
      inputFormatOptions,
      inputCompressionType,
      tableCreationParameters,
      startTime,
      endTime,
      processedSizeBytes,
      processedItemCount,
      importedItemCount,
      failureCode,
      failureMessage
    );
  }

  public static ImportTableInput ImportTableInput(
    ImportTableRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> clientToken;
    clientToken =
      Objects.nonNull(nativeValue.clientToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    S3BucketSource s3BucketSource;
    s3BucketSource = ToDafny.S3BucketSource(nativeValue.s3BucketSource());
    InputFormat inputFormat;
    inputFormat = ToDafny.InputFormat(nativeValue.inputFormat());
    Option<InputFormatOptions> inputFormatOptions;
    inputFormatOptions =
      Objects.nonNull(nativeValue.inputFormatOptions())
        ? Option.create_Some(
          InputFormatOptions._typeDescriptor(),
          ToDafny.InputFormatOptions(nativeValue.inputFormatOptions())
        )
        : Option.create_None(InputFormatOptions._typeDescriptor());
    Option<InputCompressionType> inputCompressionType;
    inputCompressionType =
      Objects.nonNull(nativeValue.inputCompressionType())
        ? Option.create_Some(
          InputCompressionType._typeDescriptor(),
          ToDafny.InputCompressionType(nativeValue.inputCompressionType())
        )
        : Option.create_None(InputCompressionType._typeDescriptor());
    TableCreationParameters tableCreationParameters;
    tableCreationParameters =
      ToDafny.TableCreationParameters(nativeValue.tableCreationParameters());
    return new ImportTableInput(
      clientToken,
      s3BucketSource,
      inputFormat,
      inputFormatOptions,
      inputCompressionType,
      tableCreationParameters
    );
  }

  public static ImportTableOutput ImportTableOutput(
    ImportTableResponse nativeValue
  ) {
    ImportTableDescription importTableDescription;
    importTableDescription =
      ToDafny.ImportTableDescription(nativeValue.importTableDescription());
    return new ImportTableOutput(importTableDescription);
  }

  public static IncrementalExportSpecification IncrementalExportSpecification(
    software.amazon.awssdk.services.dynamodb.model.IncrementalExportSpecification nativeValue
  ) {
    Option<DafnySequence<? extends Character>> exportFromTime;
    exportFromTime =
      Objects.nonNull(nativeValue.exportFromTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportFromTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> exportToTime;
    exportToTime =
      Objects.nonNull(nativeValue.exportToTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exportToTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ExportViewType> exportViewType;
    exportViewType =
      Objects.nonNull(nativeValue.exportViewType())
        ? Option.create_Some(
          ExportViewType._typeDescriptor(),
          ToDafny.ExportViewType(nativeValue.exportViewType())
        )
        : Option.create_None(ExportViewType._typeDescriptor());
    return new IncrementalExportSpecification(
      exportFromTime,
      exportToTime,
      exportViewType
    );
  }

  public static InputFormatOptions InputFormatOptions(
    software.amazon.awssdk.services.dynamodb.model.InputFormatOptions nativeValue
  ) {
    Option<CsvOptions> csv;
    csv =
      Objects.nonNull(nativeValue.csv())
        ? Option.create_Some(
          CsvOptions._typeDescriptor(),
          ToDafny.CsvOptions(nativeValue.csv())
        )
        : Option.create_None(CsvOptions._typeDescriptor());
    return new InputFormatOptions(csv);
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > ItemCollectionKeyAttributeMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static ItemCollectionMetrics ItemCollectionMetrics(
    software.amazon.awssdk.services.dynamodb.model.ItemCollectionMetrics nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > itemCollectionKey;
    itemCollectionKey =
      (Objects.nonNull(nativeValue.itemCollectionKey()) &&
          nativeValue.itemCollectionKey().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ItemCollectionKeyAttributeMap(nativeValue.itemCollectionKey())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      DafnySequence<? extends DafnySequence<? extends Byte>>
    > sizeEstimateRangeGB;
    sizeEstimateRangeGB =
      (Objects.nonNull(nativeValue.sizeEstimateRangeGB()) &&
          nativeValue.sizeEstimateRangeGB().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ItemCollectionSizeEstimateBound._typeDescriptor()
          ),
          ToDafny.ItemCollectionSizeEstimateRange(
            nativeValue.sizeEstimateRangeGB()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ItemCollectionSizeEstimateBound._typeDescriptor()
          )
        );
    return new ItemCollectionMetrics(itemCollectionKey, sizeEstimateRangeGB);
  }

  public static DafnySequence<
    ? extends ItemCollectionMetrics
  > ItemCollectionMetricsMultiple(
    List<
      software.amazon.awssdk.services.dynamodb.model.ItemCollectionMetrics
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ItemCollectionMetrics,
      ItemCollectionMetrics._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends DafnySequence<? extends ItemCollectionMetrics>
  > ItemCollectionMetricsPerTable(
    Map<
      String,
      List<software.amazon.awssdk.services.dynamodb.model.ItemCollectionMetrics>
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ItemCollectionMetricsMultiple
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Byte>
  > ItemCollectionSizeEstimateRange(List<Double> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::Double,
      ItemCollectionSizeEstimateBound._typeDescriptor()
    );
  }

  @SuppressWarnings("unchecked")
  public static DafnySequence<
    ? extends DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    >
  > ItemList(
    List<
      Map<String, software.amazon.awssdk.services.dynamodb.model.AttributeValue>
    > nativeValue
  ) {
    return (dafny.DafnySequence<
        ? extends dafny.DafnyMap<
          ? extends dafny.DafnySequence<? extends java.lang.Character>,
          ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue
        >
      >) software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeMap,
      TypeDescriptor.referenceWithInitializer(
        dafny.DafnyMap.class,
        () ->
          dafny.DafnyMap.<
            dafny.DafnySequence<? extends Character>,
            AttributeValue
          >empty()
      )
    );
  }

  public static ItemResponse ItemResponse(
    software.amazon.awssdk.services.dynamodb.model.ItemResponse nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    return new ItemResponse(item);
  }

  public static DafnySequence<? extends ItemResponse> ItemResponseList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ItemResponse
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ItemResponse,
      ItemResponse._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > Key(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends Condition
  > KeyConditions(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.Condition
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Condition
    );
  }

  @SuppressWarnings("unchecked")
  public static DafnySequence<
    ? extends DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    >
  > KeyList(
    List<
      Map<String, software.amazon.awssdk.services.dynamodb.model.AttributeValue>
    > nativeValue
  ) {
    return (dafny.DafnySequence<
        ? extends dafny.DafnyMap<
          ? extends dafny.DafnySequence<? extends java.lang.Character>,
          ? extends software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeValue
        >
      >) software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Key,
      TypeDescriptor.referenceWithInitializer(
        dafny.DafnyMap.class,
        () ->
          dafny.DafnyMap.<
            dafny.DafnySequence<? extends Character>,
            AttributeValue
          >empty()
      )
    );
  }

  public static KeysAndAttributes KeysAndAttributes(
    software.amazon.awssdk.services.dynamodb.model.KeysAndAttributes nativeValue
  ) {
    DafnySequence<
      ? extends DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > keys;
    keys = ToDafny.KeyList(nativeValue.keys());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > attributesToGet;
    attributesToGet =
      (Objects.nonNull(nativeValue.attributesToGet()) &&
          nativeValue.attributesToGet().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.AttributeNameList(nativeValue.attributesToGet())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> projectionExpression;
    projectionExpression =
      Objects.nonNull(nativeValue.projectionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.projectionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new KeysAndAttributes(
      keys,
      attributesToGet,
      consistentRead,
      projectionExpression,
      expressionAttributeNames
    );
  }

  public static DafnySequence<? extends KeySchemaElement> KeySchema(
    List<
      software.amazon.awssdk.services.dynamodb.model.KeySchemaElement
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::KeySchemaElement,
      KeySchemaElement._typeDescriptor()
    );
  }

  public static KeySchemaElement KeySchemaElement(
    software.amazon.awssdk.services.dynamodb.model.KeySchemaElement nativeValue
  ) {
    DafnySequence<? extends Character> attributeName;
    attributeName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.attributeName()
      );
    KeyType keyType;
    keyType = ToDafny.KeyType(nativeValue.keyType());
    return new KeySchemaElement(attributeName, keyType);
  }

  public static KinesisDataStreamDestination KinesisDataStreamDestination(
    software.amazon.awssdk.services.dynamodb.model.KinesisDataStreamDestination nativeValue
  ) {
    Option<DafnySequence<? extends Character>> streamArn;
    streamArn =
      Objects.nonNull(nativeValue.streamArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.streamArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DestinationStatus> destinationStatus;
    destinationStatus =
      Objects.nonNull(nativeValue.destinationStatus())
        ? Option.create_Some(
          DestinationStatus._typeDescriptor(),
          ToDafny.DestinationStatus(nativeValue.destinationStatus())
        )
        : Option.create_None(DestinationStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> destinationStatusDescription;
    destinationStatusDescription =
      Objects.nonNull(nativeValue.destinationStatusDescription())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.destinationStatusDescription()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      ApproximateCreationDateTimePrecision
    > approximateCreationDateTimePrecision;
    approximateCreationDateTimePrecision =
      Objects.nonNull(nativeValue.approximateCreationDateTimePrecision())
        ? Option.create_Some(
          ApproximateCreationDateTimePrecision._typeDescriptor(),
          ToDafny.ApproximateCreationDateTimePrecision(
            nativeValue.approximateCreationDateTimePrecision()
          )
        )
        : Option.create_None(
          ApproximateCreationDateTimePrecision._typeDescriptor()
        );
    return new KinesisDataStreamDestination(
      streamArn,
      destinationStatus,
      destinationStatusDescription,
      approximateCreationDateTimePrecision
    );
  }

  public static DafnySequence<
    ? extends KinesisDataStreamDestination
  > KinesisDataStreamDestinations(
    List<
      software.amazon.awssdk.services.dynamodb.model.KinesisDataStreamDestination
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::KinesisDataStreamDestination,
      KinesisDataStreamDestination._typeDescriptor()
    );
  }

  public static DafnySequence<? extends AttributeValue> ListAttributeValue(
    List<
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue,
      AttributeValue._typeDescriptor()
    );
  }

  public static ListBackupsInput ListBackupsInput(
    ListBackupsRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    Option<DafnySequence<? extends Character>> timeRangeLowerBound;
    timeRangeLowerBound =
      Objects.nonNull(nativeValue.timeRangeLowerBound())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.timeRangeLowerBound()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> timeRangeUpperBound;
    timeRangeUpperBound =
      Objects.nonNull(nativeValue.timeRangeUpperBound())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.timeRangeUpperBound()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> exclusiveStartBackupArn;
    exclusiveStartBackupArn =
      Objects.nonNull(nativeValue.exclusiveStartBackupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exclusiveStartBackupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<BackupTypeFilter> backupType;
    backupType =
      Objects.nonNull(nativeValue.backupType())
        ? Option.create_Some(
          BackupTypeFilter._typeDescriptor(),
          ToDafny.BackupTypeFilter(nativeValue.backupType())
        )
        : Option.create_None(BackupTypeFilter._typeDescriptor());
    return new ListBackupsInput(
      tableName,
      limit,
      timeRangeLowerBound,
      timeRangeUpperBound,
      exclusiveStartBackupArn,
      backupType
    );
  }

  public static ListBackupsOutput ListBackupsOutput(
    ListBackupsResponse nativeValue
  ) {
    Option<DafnySequence<? extends BackupSummary>> backupSummaries;
    backupSummaries =
      (Objects.nonNull(nativeValue.backupSummaries()) &&
          nativeValue.backupSummaries().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(BackupSummary._typeDescriptor()),
          ToDafny.BackupSummaries(nativeValue.backupSummaries())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(BackupSummary._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> lastEvaluatedBackupArn;
    lastEvaluatedBackupArn =
      Objects.nonNull(nativeValue.lastEvaluatedBackupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastEvaluatedBackupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListBackupsOutput(backupSummaries, lastEvaluatedBackupArn);
  }

  public static ListContributorInsightsInput ListContributorInsightsInput(
    ListContributorInsightsRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> maxResults;
    maxResults =
      Objects.nonNull(nativeValue.maxResults())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.maxResults()))
        : Option.create_None(TypeDescriptor.INT);
    return new ListContributorInsightsInput(tableName, nextToken, maxResults);
  }

  public static ListContributorInsightsOutput ListContributorInsightsOutput(
    ListContributorInsightsResponse nativeValue
  ) {
    Option<
      DafnySequence<? extends ContributorInsightsSummary>
    > contributorInsightsSummaries;
    contributorInsightsSummaries =
      (Objects.nonNull(nativeValue.contributorInsightsSummaries()) &&
          nativeValue.contributorInsightsSummaries().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ContributorInsightsSummary._typeDescriptor()
          ),
          ToDafny.ContributorInsightsSummaries(
            nativeValue.contributorInsightsSummaries()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ContributorInsightsSummary._typeDescriptor()
          )
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListContributorInsightsOutput(
      contributorInsightsSummaries,
      nextToken
    );
  }

  public static ListExportsInput ListExportsInput(
    ListExportsRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> maxResults;
    maxResults =
      Objects.nonNull(nativeValue.maxResults())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.maxResults()))
        : Option.create_None(TypeDescriptor.INT);
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListExportsInput(tableArn, maxResults, nextToken);
  }

  public static ListExportsOutput ListExportsOutput(
    ListExportsResponse nativeValue
  ) {
    Option<DafnySequence<? extends ExportSummary>> exportSummaries;
    exportSummaries =
      (Objects.nonNull(nativeValue.exportSummaries()) &&
          nativeValue.exportSummaries().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ExportSummary._typeDescriptor()),
          ToDafny.ExportSummaries(nativeValue.exportSummaries())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ExportSummary._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListExportsOutput(exportSummaries, nextToken);
  }

  public static ListGlobalTablesInput ListGlobalTablesInput(
    ListGlobalTablesRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> exclusiveStartGlobalTableName;
    exclusiveStartGlobalTableName =
      Objects.nonNull(nativeValue.exclusiveStartGlobalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exclusiveStartGlobalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    Option<DafnySequence<? extends Character>> regionName;
    regionName =
      Objects.nonNull(nativeValue.regionName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.regionName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListGlobalTablesInput(
      exclusiveStartGlobalTableName,
      limit,
      regionName
    );
  }

  public static ListGlobalTablesOutput ListGlobalTablesOutput(
    ListGlobalTablesResponse nativeValue
  ) {
    Option<DafnySequence<? extends GlobalTable>> globalTables;
    globalTables =
      (Objects.nonNull(nativeValue.globalTables()) &&
          nativeValue.globalTables().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(GlobalTable._typeDescriptor()),
          ToDafny.GlobalTableList(nativeValue.globalTables())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(GlobalTable._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> lastEvaluatedGlobalTableName;
    lastEvaluatedGlobalTableName =
      Objects.nonNull(nativeValue.lastEvaluatedGlobalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastEvaluatedGlobalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListGlobalTablesOutput(
      globalTables,
      lastEvaluatedGlobalTableName
    );
  }

  public static ListImportsInput ListImportsInput(
    ListImportsRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> pageSize;
    pageSize =
      Objects.nonNull(nativeValue.pageSize())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.pageSize()))
        : Option.create_None(TypeDescriptor.INT);
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListImportsInput(tableArn, pageSize, nextToken);
  }

  public static ListImportsOutput ListImportsOutput(
    ListImportsResponse nativeValue
  ) {
    Option<DafnySequence<? extends ImportSummary>> importSummaryList;
    importSummaryList =
      (Objects.nonNull(nativeValue.importSummaryList()) &&
          nativeValue.importSummaryList().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ImportSummary._typeDescriptor()),
          ToDafny.ImportSummaryList(nativeValue.importSummaryList())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ImportSummary._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListImportsOutput(importSummaryList, nextToken);
  }

  public static ListTablesInput ListTablesInput(ListTablesRequest nativeValue) {
    Option<DafnySequence<? extends Character>> exclusiveStartTableName;
    exclusiveStartTableName =
      Objects.nonNull(nativeValue.exclusiveStartTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.exclusiveStartTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    return new ListTablesInput(exclusiveStartTableName, limit);
  }

  public static ListTablesOutput ListTablesOutput(
    ListTablesResponse nativeValue
  ) {
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > tableNames;
    tableNames =
      (Objects.nonNull(nativeValue.tableNames()) &&
          nativeValue.tableNames().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.TableNameList(nativeValue.tableNames())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<DafnySequence<? extends Character>> lastEvaluatedTableName;
    lastEvaluatedTableName =
      Objects.nonNull(nativeValue.lastEvaluatedTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastEvaluatedTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListTablesOutput(tableNames, lastEvaluatedTableName);
  }

  public static ListTagsOfResourceInput ListTagsOfResourceInput(
    ListTagsOfResourceRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListTagsOfResourceInput(resourceArn, nextToken);
  }

  public static ListTagsOfResourceOutput ListTagsOfResourceOutput(
    ListTagsOfResourceResponse nativeValue
  ) {
    Option<DafnySequence<? extends Tag>> tags;
    tags =
      (Objects.nonNull(nativeValue.tags()) && nativeValue.tags().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(Tag._typeDescriptor()),
          ToDafny.TagList(nativeValue.tags())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(Tag._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> nextToken;
    nextToken =
      Objects.nonNull(nativeValue.nextToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.nextToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new ListTagsOfResourceOutput(tags, nextToken);
  }

  public static LocalSecondaryIndex LocalSecondaryIndex(
    software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndex nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    Projection projection;
    projection = ToDafny.Projection(nativeValue.projection());
    return new LocalSecondaryIndex(indexName, keySchema, projection);
  }

  public static LocalSecondaryIndexDescription LocalSecondaryIndexDescription(
    software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndexDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends KeySchemaElement>> keySchema;
    keySchema =
      (Objects.nonNull(nativeValue.keySchema()) &&
          nativeValue.keySchema().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor()),
          ToDafny.KeySchema(nativeValue.keySchema())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor())
        );
    Option<Projection> projection;
    projection =
      Objects.nonNull(nativeValue.projection())
        ? Option.create_Some(
          Projection._typeDescriptor(),
          ToDafny.Projection(nativeValue.projection())
        )
        : Option.create_None(Projection._typeDescriptor());
    Option<Long> indexSizeBytes;
    indexSizeBytes =
      Objects.nonNull(nativeValue.indexSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.indexSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> itemCount;
    itemCount =
      Objects.nonNull(nativeValue.itemCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.itemCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<DafnySequence<? extends Character>> indexArn;
    indexArn =
      Objects.nonNull(nativeValue.indexArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new LocalSecondaryIndexDescription(
      indexName,
      keySchema,
      projection,
      indexSizeBytes,
      itemCount,
      indexArn
    );
  }

  public static DafnySequence<
    ? extends LocalSecondaryIndexDescription
  > LocalSecondaryIndexDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndexDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::LocalSecondaryIndexDescription,
      LocalSecondaryIndexDescription._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends LocalSecondaryIndexInfo
  > LocalSecondaryIndexes(
    List<
      software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndexInfo
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::LocalSecondaryIndexInfo,
      LocalSecondaryIndexInfo._typeDescriptor()
    );
  }

  public static LocalSecondaryIndexInfo LocalSecondaryIndexInfo(
    software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndexInfo nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends KeySchemaElement>> keySchema;
    keySchema =
      (Objects.nonNull(nativeValue.keySchema()) &&
          nativeValue.keySchema().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor()),
          ToDafny.KeySchema(nativeValue.keySchema())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor())
        );
    Option<Projection> projection;
    projection =
      Objects.nonNull(nativeValue.projection())
        ? Option.create_Some(
          Projection._typeDescriptor(),
          ToDafny.Projection(nativeValue.projection())
        )
        : Option.create_None(Projection._typeDescriptor());
    return new LocalSecondaryIndexInfo(indexName, keySchema, projection);
  }

  public static DafnySequence<
    ? extends LocalSecondaryIndex
  > LocalSecondaryIndexList(
    List<
      software.amazon.awssdk.services.dynamodb.model.LocalSecondaryIndex
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::LocalSecondaryIndex,
      LocalSecondaryIndex._typeDescriptor()
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > MapAttributeValue(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > NonKeyAttributeNameList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > NumberSetAttributeValue(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static OnDemandThroughput OnDemandThroughput(
    software.amazon.awssdk.services.dynamodb.model.OnDemandThroughput nativeValue
  ) {
    Option<Long> maxReadRequestUnits;
    maxReadRequestUnits =
      Objects.nonNull(nativeValue.maxReadRequestUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.maxReadRequestUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> maxWriteRequestUnits;
    maxWriteRequestUnits =
      Objects.nonNull(nativeValue.maxWriteRequestUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.maxWriteRequestUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new OnDemandThroughput(maxReadRequestUnits, maxWriteRequestUnits);
  }

  public static OnDemandThroughputOverride OnDemandThroughputOverride(
    software.amazon.awssdk.services.dynamodb.model.OnDemandThroughputOverride nativeValue
  ) {
    Option<Long> maxReadRequestUnits;
    maxReadRequestUnits =
      Objects.nonNull(nativeValue.maxReadRequestUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.maxReadRequestUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new OnDemandThroughputOverride(maxReadRequestUnits);
  }

  public static ParameterizedStatement ParameterizedStatement(
    software.amazon.awssdk.services.dynamodb.model.ParameterizedStatement nativeValue
  ) {
    DafnySequence<? extends Character> statement;
    statement =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.statement()
      );
    Option<DafnySequence<? extends AttributeValue>> parameters;
    parameters =
      (Objects.nonNull(nativeValue.parameters()) &&
          nativeValue.parameters().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor()),
          ToDafny.PreparedStatementParameters(nativeValue.parameters())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeValue._typeDescriptor())
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new ParameterizedStatement(
      statement,
      parameters,
      returnValuesOnConditionCheckFailure
    );
  }

  public static DafnySequence<
    ? extends ParameterizedStatement
  > ParameterizedStatements(
    List<
      software.amazon.awssdk.services.dynamodb.model.ParameterizedStatement
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ParameterizedStatement,
      ParameterizedStatement._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends BatchStatementRequest
  > PartiQLBatchRequest(
    List<
      software.amazon.awssdk.services.dynamodb.model.BatchStatementRequest
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::BatchStatementRequest,
      BatchStatementRequest._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends BatchStatementResponse
  > PartiQLBatchResponse(
    List<
      software.amazon.awssdk.services.dynamodb.model.BatchStatementResponse
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::BatchStatementResponse,
      BatchStatementResponse._typeDescriptor()
    );
  }

  public static PointInTimeRecoveryDescription PointInTimeRecoveryDescription(
    software.amazon.awssdk.services.dynamodb.model.PointInTimeRecoveryDescription nativeValue
  ) {
    Option<PointInTimeRecoveryStatus> pointInTimeRecoveryStatus;
    pointInTimeRecoveryStatus =
      Objects.nonNull(nativeValue.pointInTimeRecoveryStatus())
        ? Option.create_Some(
          PointInTimeRecoveryStatus._typeDescriptor(),
          ToDafny.PointInTimeRecoveryStatus(
            nativeValue.pointInTimeRecoveryStatus()
          )
        )
        : Option.create_None(PointInTimeRecoveryStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> earliestRestorableDateTime;
    earliestRestorableDateTime =
      Objects.nonNull(nativeValue.earliestRestorableDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.earliestRestorableDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> latestRestorableDateTime;
    latestRestorableDateTime =
      Objects.nonNull(nativeValue.latestRestorableDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.latestRestorableDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PointInTimeRecoveryDescription(
      pointInTimeRecoveryStatus,
      earliestRestorableDateTime,
      latestRestorableDateTime
    );
  }

  public static PointInTimeRecoverySpecification PointInTimeRecoverySpecification(
    software.amazon.awssdk.services.dynamodb.model.PointInTimeRecoverySpecification nativeValue
  ) {
    Boolean pointInTimeRecoveryEnabled;
    pointInTimeRecoveryEnabled = (nativeValue.pointInTimeRecoveryEnabled());
    return new PointInTimeRecoverySpecification(pointInTimeRecoveryEnabled);
  }

  public static DafnySequence<
    ? extends AttributeValue
  > PreparedStatementParameters(
    List<
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue,
      AttributeValue._typeDescriptor()
    );
  }

  public static Projection Projection(
    software.amazon.awssdk.services.dynamodb.model.Projection nativeValue
  ) {
    Option<ProjectionType> projectionType;
    projectionType =
      Objects.nonNull(nativeValue.projectionType())
        ? Option.create_Some(
          ProjectionType._typeDescriptor(),
          ToDafny.ProjectionType(nativeValue.projectionType())
        )
        : Option.create_None(ProjectionType._typeDescriptor());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > nonKeyAttributes;
    nonKeyAttributes =
      (Objects.nonNull(nativeValue.nonKeyAttributes()) &&
          nativeValue.nonKeyAttributes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.NonKeyAttributeNameList(nativeValue.nonKeyAttributes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    return new Projection(projectionType, nonKeyAttributes);
  }

  public static ProvisionedThroughput ProvisionedThroughput(
    software.amazon.awssdk.services.dynamodb.model.ProvisionedThroughput nativeValue
  ) {
    Long readCapacityUnits;
    readCapacityUnits = (nativeValue.readCapacityUnits());
    Long writeCapacityUnits;
    writeCapacityUnits = (nativeValue.writeCapacityUnits());
    return new ProvisionedThroughput(readCapacityUnits, writeCapacityUnits);
  }

  public static ProvisionedThroughputDescription ProvisionedThroughputDescription(
    software.amazon.awssdk.services.dynamodb.model.ProvisionedThroughputDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> lastIncreaseDateTime;
    lastIncreaseDateTime =
      Objects.nonNull(nativeValue.lastIncreaseDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastIncreaseDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> lastDecreaseDateTime;
    lastDecreaseDateTime =
      Objects.nonNull(nativeValue.lastDecreaseDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastDecreaseDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Long> numberOfDecreasesToday;
    numberOfDecreasesToday =
      Objects.nonNull(nativeValue.numberOfDecreasesToday())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.numberOfDecreasesToday())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> readCapacityUnits;
    readCapacityUnits =
      Objects.nonNull(nativeValue.readCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.readCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> writeCapacityUnits;
    writeCapacityUnits =
      Objects.nonNull(nativeValue.writeCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.writeCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new ProvisionedThroughputDescription(
      lastIncreaseDateTime,
      lastDecreaseDateTime,
      numberOfDecreasesToday,
      readCapacityUnits,
      writeCapacityUnits
    );
  }

  public static ProvisionedThroughputOverride ProvisionedThroughputOverride(
    software.amazon.awssdk.services.dynamodb.model.ProvisionedThroughputOverride nativeValue
  ) {
    Option<Long> readCapacityUnits;
    readCapacityUnits =
      Objects.nonNull(nativeValue.readCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.readCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    return new ProvisionedThroughputOverride(readCapacityUnits);
  }

  public static Put Put(
    software.amazon.awssdk.services.dynamodb.model.Put nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > item;
    item = ToDafny.PutItemInputAttributeMap(nativeValue.item());
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new Put(
      item,
      tableName,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static PutItemInput PutItemInput(PutItemRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > item;
    item = ToDafny.PutItemInputAttributeMap(nativeValue.item());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends ExpectedAttributeValue
      >
    > expected;
    expected =
      (Objects.nonNull(nativeValue.expected()) &&
          nativeValue.expected().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          ),
          ToDafny.ExpectedAttributeMap(nativeValue.expected())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          )
        );
    Option<ReturnValue> returnValues;
    returnValues =
      Objects.nonNull(nativeValue.returnValues())
        ? Option.create_Some(
          ReturnValue._typeDescriptor(),
          ToDafny.ReturnValue(nativeValue.returnValues())
        )
        : Option.create_None(ReturnValue._typeDescriptor());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<ReturnItemCollectionMetrics> returnItemCollectionMetrics;
    returnItemCollectionMetrics =
      Objects.nonNull(nativeValue.returnItemCollectionMetrics())
        ? Option.create_Some(
          ReturnItemCollectionMetrics._typeDescriptor(),
          ToDafny.ReturnItemCollectionMetrics(
            nativeValue.returnItemCollectionMetrics()
          )
        )
        : Option.create_None(ReturnItemCollectionMetrics._typeDescriptor());
    Option<ConditionalOperator> conditionalOperator;
    conditionalOperator =
      Objects.nonNull(nativeValue.conditionalOperator())
        ? Option.create_Some(
          ConditionalOperator._typeDescriptor(),
          ToDafny.ConditionalOperator(nativeValue.conditionalOperator())
        )
        : Option.create_None(ConditionalOperator._typeDescriptor());
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new PutItemInput(
      tableName,
      item,
      expected,
      returnValues,
      returnConsumedCapacity,
      returnItemCollectionMetrics,
      conditionalOperator,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends AttributeValue
  > PutItemInputAttributeMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.AttributeValue
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::AttributeValue
    );
  }

  public static PutItemOutput PutItemOutput(PutItemResponse nativeValue) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > attributes;
    attributes =
      (Objects.nonNull(nativeValue.attributes()) &&
          nativeValue.attributes().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.attributes())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    Option<ItemCollectionMetrics> itemCollectionMetrics;
    itemCollectionMetrics =
      Objects.nonNull(nativeValue.itemCollectionMetrics())
        ? Option.create_Some(
          ItemCollectionMetrics._typeDescriptor(),
          ToDafny.ItemCollectionMetrics(nativeValue.itemCollectionMetrics())
        )
        : Option.create_None(ItemCollectionMetrics._typeDescriptor());
    return new PutItemOutput(
      attributes,
      consumedCapacity,
      itemCollectionMetrics
    );
  }

  public static PutRequest PutRequest(
    software.amazon.awssdk.services.dynamodb.model.PutRequest nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > item;
    item = ToDafny.PutItemInputAttributeMap(nativeValue.item());
    return new PutRequest(item);
  }

  public static PutResourcePolicyInput PutResourcePolicyInput(
    PutResourcePolicyRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    DafnySequence<? extends Character> policy;
    policy =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.policy()
      );
    Option<DafnySequence<? extends Character>> expectedRevisionId;
    expectedRevisionId =
      Objects.nonNull(nativeValue.expectedRevisionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.expectedRevisionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Boolean> confirmRemoveSelfResourceAccess;
    confirmRemoveSelfResourceAccess =
      Objects.nonNull(nativeValue.confirmRemoveSelfResourceAccess())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.confirmRemoveSelfResourceAccess())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    return new PutResourcePolicyInput(
      resourceArn,
      policy,
      expectedRevisionId,
      confirmRemoveSelfResourceAccess
    );
  }

  public static PutResourcePolicyOutput PutResourcePolicyOutput(
    PutResourcePolicyResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> revisionId;
    revisionId =
      Objects.nonNull(nativeValue.revisionId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.revisionId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new PutResourcePolicyOutput(revisionId);
  }

  public static QueryInput QueryInput(QueryRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Select> select;
    select =
      Objects.nonNull(nativeValue.select())
        ? Option.create_Some(
          Select._typeDescriptor(),
          ToDafny.Select(nativeValue.select())
        )
        : Option.create_None(Select._typeDescriptor());
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > attributesToGet;
    attributesToGet =
      (Objects.nonNull(nativeValue.attributesToGet()) &&
          nativeValue.attributesToGet().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.AttributeNameList(nativeValue.attributesToGet())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends Condition
      >
    > keyConditions;
    keyConditions =
      (Objects.nonNull(nativeValue.keyConditions()) &&
          nativeValue.keyConditions().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          ),
          ToDafny.KeyConditions(nativeValue.keyConditions())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends Condition
      >
    > queryFilter;
    queryFilter =
      (Objects.nonNull(nativeValue.queryFilter()) &&
          nativeValue.queryFilter().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          ),
          ToDafny.FilterConditionMap(nativeValue.queryFilter())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          )
        );
    Option<ConditionalOperator> conditionalOperator;
    conditionalOperator =
      Objects.nonNull(nativeValue.conditionalOperator())
        ? Option.create_Some(
          ConditionalOperator._typeDescriptor(),
          ToDafny.ConditionalOperator(nativeValue.conditionalOperator())
        )
        : Option.create_None(ConditionalOperator._typeDescriptor());
    Option<Boolean> scanIndexForward;
    scanIndexForward =
      Objects.nonNull(nativeValue.scanIndexForward())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.scanIndexForward())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > exclusiveStartKey;
    exclusiveStartKey =
      (Objects.nonNull(nativeValue.exclusiveStartKey()) &&
          nativeValue.exclusiveStartKey().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.Key(nativeValue.exclusiveStartKey())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<DafnySequence<? extends Character>> projectionExpression;
    projectionExpression =
      Objects.nonNull(nativeValue.projectionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.projectionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> filterExpression;
    filterExpression =
      Objects.nonNull(nativeValue.filterExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.filterExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> keyConditionExpression;
    keyConditionExpression =
      Objects.nonNull(nativeValue.keyConditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.keyConditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    return new QueryInput(
      tableName,
      indexName,
      select,
      attributesToGet,
      limit,
      consistentRead,
      keyConditions,
      queryFilter,
      conditionalOperator,
      scanIndexForward,
      exclusiveStartKey,
      returnConsumedCapacity,
      projectionExpression,
      filterExpression,
      keyConditionExpression,
      expressionAttributeNames,
      expressionAttributeValues
    );
  }

  public static QueryOutput QueryOutput(QueryResponse nativeValue) {
    Option<
      DafnySequence<
        ? extends DafnyMap<
          ? extends DafnySequence<? extends Character>,
          ? extends AttributeValue
        >
      >
    > items;
    items =
      (Objects.nonNull(nativeValue.items()) && nativeValue.items().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          ),
          ToDafny.ItemList(nativeValue.items())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          )
        );
    Option<Integer> count;
    count =
      Objects.nonNull(nativeValue.count())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.count()))
        : Option.create_None(TypeDescriptor.INT);
    Option<Integer> scannedCount;
    scannedCount =
      Objects.nonNull(nativeValue.scannedCount())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.scannedCount()))
        : Option.create_None(TypeDescriptor.INT);
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > lastEvaluatedKey;
    lastEvaluatedKey =
      (Objects.nonNull(nativeValue.lastEvaluatedKey()) &&
          nativeValue.lastEvaluatedKey().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.Key(nativeValue.lastEvaluatedKey())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    return new QueryOutput(
      items,
      count,
      scannedCount,
      lastEvaluatedKey,
      consumedCapacity
    );
  }

  public static Replica Replica(
    software.amazon.awssdk.services.dynamodb.model.Replica nativeValue
  ) {
    Option<DafnySequence<? extends Character>> regionName;
    regionName =
      Objects.nonNull(nativeValue.regionName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.regionName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Replica(regionName);
  }

  public static ReplicaAutoScalingDescription ReplicaAutoScalingDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaAutoScalingDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> regionName;
    regionName =
      Objects.nonNull(nativeValue.regionName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.regionName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexAutoScalingDescription._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexAutoScalingDescriptionList(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexAutoScalingDescription._typeDescriptor()
          )
        );
    Option<
      AutoScalingSettingsDescription
    > replicaProvisionedReadCapacityAutoScalingSettings;
    replicaProvisionedReadCapacityAutoScalingSettings =
      Objects.nonNull(
          nativeValue.replicaProvisionedReadCapacityAutoScalingSettings()
        )
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.replicaProvisionedReadCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<
      AutoScalingSettingsDescription
    > replicaProvisionedWriteCapacityAutoScalingSettings;
    replicaProvisionedWriteCapacityAutoScalingSettings =
      Objects.nonNull(
          nativeValue.replicaProvisionedWriteCapacityAutoScalingSettings()
        )
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.replicaProvisionedWriteCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<ReplicaStatus> replicaStatus;
    replicaStatus =
      Objects.nonNull(nativeValue.replicaStatus())
        ? Option.create_Some(
          ReplicaStatus._typeDescriptor(),
          ToDafny.ReplicaStatus(nativeValue.replicaStatus())
        )
        : Option.create_None(ReplicaStatus._typeDescriptor());
    return new ReplicaAutoScalingDescription(
      regionName,
      globalSecondaryIndexes,
      replicaProvisionedReadCapacityAutoScalingSettings,
      replicaProvisionedWriteCapacityAutoScalingSettings,
      replicaStatus
    );
  }

  public static DafnySequence<
    ? extends ReplicaAutoScalingDescription
  > ReplicaAutoScalingDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaAutoScalingDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaAutoScalingDescription,
      ReplicaAutoScalingDescription._typeDescriptor()
    );
  }

  public static ReplicaAutoScalingUpdate ReplicaAutoScalingUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicaAutoScalingUpdate nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>
    > replicaGlobalSecondaryIndexUpdates;
    replicaGlobalSecondaryIndexUpdates =
      (Objects.nonNull(nativeValue.replicaGlobalSecondaryIndexUpdates()) &&
          nativeValue.replicaGlobalSecondaryIndexUpdates().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexAutoScalingUpdateList(
            nativeValue.replicaGlobalSecondaryIndexUpdates()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
          )
        );
    Option<
      AutoScalingSettingsUpdate
    > replicaProvisionedReadCapacityAutoScalingUpdate;
    replicaProvisionedReadCapacityAutoScalingUpdate =
      Objects.nonNull(
          nativeValue.replicaProvisionedReadCapacityAutoScalingUpdate()
        )
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.replicaProvisionedReadCapacityAutoScalingUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    return new ReplicaAutoScalingUpdate(
      regionName,
      replicaGlobalSecondaryIndexUpdates,
      replicaProvisionedReadCapacityAutoScalingUpdate
    );
  }

  public static DafnySequence<
    ? extends ReplicaAutoScalingUpdate
  > ReplicaAutoScalingUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaAutoScalingUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaAutoScalingUpdate,
      ReplicaAutoScalingUpdate._typeDescriptor()
    );
  }

  public static ReplicaDescription ReplicaDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> regionName;
    regionName =
      Objects.nonNull(nativeValue.regionName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.regionName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ReplicaStatus> replicaStatus;
    replicaStatus =
      Objects.nonNull(nativeValue.replicaStatus())
        ? Option.create_Some(
          ReplicaStatus._typeDescriptor(),
          ToDafny.ReplicaStatus(nativeValue.replicaStatus())
        )
        : Option.create_None(ReplicaStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> replicaStatusDescription;
    replicaStatusDescription =
      Objects.nonNull(nativeValue.replicaStatusDescription())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.replicaStatusDescription()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> replicaStatusPercentProgress;
    replicaStatusPercentProgress =
      Objects.nonNull(nativeValue.replicaStatusPercentProgress())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.replicaStatusPercentProgress()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> kMSMasterKeyId;
    kMSMasterKeyId =
      Objects.nonNull(nativeValue.kmsMasterKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.kmsMasterKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ProvisionedThroughputOverride> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughputOverride._typeDescriptor(),
          ToDafny.ProvisionedThroughputOverride(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughputOverride._typeDescriptor());
    Option<OnDemandThroughputOverride> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughputOverride._typeDescriptor(),
          ToDafny.OnDemandThroughputOverride(
            nativeValue.onDemandThroughputOverride()
          )
        )
        : Option.create_None(OnDemandThroughputOverride._typeDescriptor());
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexDescription._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexDescriptionList(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexDescription._typeDescriptor()
          )
        );
    Option<DafnySequence<? extends Character>> replicaInaccessibleDateTime;
    replicaInaccessibleDateTime =
      Objects.nonNull(nativeValue.replicaInaccessibleDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.replicaInaccessibleDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<TableClassSummary> replicaTableClassSummary;
    replicaTableClassSummary =
      Objects.nonNull(nativeValue.replicaTableClassSummary())
        ? Option.create_Some(
          TableClassSummary._typeDescriptor(),
          ToDafny.TableClassSummary(nativeValue.replicaTableClassSummary())
        )
        : Option.create_None(TableClassSummary._typeDescriptor());
    return new ReplicaDescription(
      regionName,
      replicaStatus,
      replicaStatusDescription,
      replicaStatusPercentProgress,
      kMSMasterKeyId,
      provisionedThroughputOverride,
      onDemandThroughputOverride,
      globalSecondaryIndexes,
      replicaInaccessibleDateTime,
      replicaTableClassSummary
    );
  }

  public static DafnySequence<
    ? extends ReplicaDescription
  > ReplicaDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaDescription,
      ReplicaDescription._typeDescriptor()
    );
  }

  public static ReplicaGlobalSecondaryIndex ReplicaGlobalSecondaryIndex(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndex nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    Option<ProvisionedThroughputOverride> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughputOverride._typeDescriptor(),
          ToDafny.ProvisionedThroughputOverride(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughputOverride._typeDescriptor());
    Option<OnDemandThroughputOverride> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughputOverride._typeDescriptor(),
          ToDafny.OnDemandThroughputOverride(
            nativeValue.onDemandThroughputOverride()
          )
        )
        : Option.create_None(OnDemandThroughputOverride._typeDescriptor());
    return new ReplicaGlobalSecondaryIndex(
      indexName,
      provisionedThroughputOverride,
      onDemandThroughputOverride
    );
  }

  public static ReplicaGlobalSecondaryIndexAutoScalingDescription ReplicaGlobalSecondaryIndexAutoScalingDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexAutoScalingDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<IndexStatus> indexStatus;
    indexStatus =
      Objects.nonNull(nativeValue.indexStatus())
        ? Option.create_Some(
          IndexStatus._typeDescriptor(),
          ToDafny.IndexStatus(nativeValue.indexStatus())
        )
        : Option.create_None(IndexStatus._typeDescriptor());
    Option<
      AutoScalingSettingsDescription
    > provisionedReadCapacityAutoScalingSettings;
    provisionedReadCapacityAutoScalingSettings =
      Objects.nonNull(nativeValue.provisionedReadCapacityAutoScalingSettings())
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.provisionedReadCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<
      AutoScalingSettingsDescription
    > provisionedWriteCapacityAutoScalingSettings;
    provisionedWriteCapacityAutoScalingSettings =
      Objects.nonNull(nativeValue.provisionedWriteCapacityAutoScalingSettings())
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.provisionedWriteCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    return new ReplicaGlobalSecondaryIndexAutoScalingDescription(
      indexName,
      indexStatus,
      provisionedReadCapacityAutoScalingSettings,
      provisionedWriteCapacityAutoScalingSettings
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndexAutoScalingDescription
  > ReplicaGlobalSecondaryIndexAutoScalingDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexAutoScalingDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndexAutoScalingDescription,
      ReplicaGlobalSecondaryIndexAutoScalingDescription._typeDescriptor()
    );
  }

  public static ReplicaGlobalSecondaryIndexAutoScalingUpdate ReplicaGlobalSecondaryIndexAutoScalingUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexAutoScalingUpdate nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<AutoScalingSettingsUpdate> provisionedReadCapacityAutoScalingUpdate;
    provisionedReadCapacityAutoScalingUpdate =
      Objects.nonNull(nativeValue.provisionedReadCapacityAutoScalingUpdate())
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.provisionedReadCapacityAutoScalingUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    return new ReplicaGlobalSecondaryIndexAutoScalingUpdate(
      indexName,
      provisionedReadCapacityAutoScalingUpdate
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate
  > ReplicaGlobalSecondaryIndexAutoScalingUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexAutoScalingUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndexAutoScalingUpdate,
      ReplicaGlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
    );
  }

  public static ReplicaGlobalSecondaryIndexDescription ReplicaGlobalSecondaryIndexDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ProvisionedThroughputOverride> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughputOverride._typeDescriptor(),
          ToDafny.ProvisionedThroughputOverride(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughputOverride._typeDescriptor());
    Option<OnDemandThroughputOverride> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughputOverride._typeDescriptor(),
          ToDafny.OnDemandThroughputOverride(
            nativeValue.onDemandThroughputOverride()
          )
        )
        : Option.create_None(OnDemandThroughputOverride._typeDescriptor());
    return new ReplicaGlobalSecondaryIndexDescription(
      indexName,
      provisionedThroughputOverride,
      onDemandThroughputOverride
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndexDescription
  > ReplicaGlobalSecondaryIndexDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndexDescription,
      ReplicaGlobalSecondaryIndexDescription._typeDescriptor()
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndex
  > ReplicaGlobalSecondaryIndexList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndex
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndex,
      ReplicaGlobalSecondaryIndex._typeDescriptor()
    );
  }

  public static ReplicaGlobalSecondaryIndexSettingsDescription ReplicaGlobalSecondaryIndexSettingsDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexSettingsDescription nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    Option<IndexStatus> indexStatus;
    indexStatus =
      Objects.nonNull(nativeValue.indexStatus())
        ? Option.create_Some(
          IndexStatus._typeDescriptor(),
          ToDafny.IndexStatus(nativeValue.indexStatus())
        )
        : Option.create_None(IndexStatus._typeDescriptor());
    Option<Long> provisionedReadCapacityUnits;
    provisionedReadCapacityUnits =
      Objects.nonNull(nativeValue.provisionedReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.provisionedReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsDescription
    > provisionedReadCapacityAutoScalingSettings;
    provisionedReadCapacityAutoScalingSettings =
      Objects.nonNull(nativeValue.provisionedReadCapacityAutoScalingSettings())
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.provisionedReadCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<Long> provisionedWriteCapacityUnits;
    provisionedWriteCapacityUnits =
      Objects.nonNull(nativeValue.provisionedWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.provisionedWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsDescription
    > provisionedWriteCapacityAutoScalingSettings;
    provisionedWriteCapacityAutoScalingSettings =
      Objects.nonNull(nativeValue.provisionedWriteCapacityAutoScalingSettings())
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.provisionedWriteCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    return new ReplicaGlobalSecondaryIndexSettingsDescription(
      indexName,
      indexStatus,
      provisionedReadCapacityUnits,
      provisionedReadCapacityAutoScalingSettings,
      provisionedWriteCapacityUnits,
      provisionedWriteCapacityAutoScalingSettings
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndexSettingsDescription
  > ReplicaGlobalSecondaryIndexSettingsDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexSettingsDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndexSettingsDescription,
      ReplicaGlobalSecondaryIndexSettingsDescription._typeDescriptor()
    );
  }

  public static ReplicaGlobalSecondaryIndexSettingsUpdate ReplicaGlobalSecondaryIndexSettingsUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexSettingsUpdate nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    Option<Long> provisionedReadCapacityUnits;
    provisionedReadCapacityUnits =
      Objects.nonNull(nativeValue.provisionedReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.provisionedReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsUpdate
    > provisionedReadCapacityAutoScalingSettingsUpdate;
    provisionedReadCapacityAutoScalingSettingsUpdate =
      Objects.nonNull(
          nativeValue.provisionedReadCapacityAutoScalingSettingsUpdate()
        )
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.provisionedReadCapacityAutoScalingSettingsUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    return new ReplicaGlobalSecondaryIndexSettingsUpdate(
      indexName,
      provisionedReadCapacityUnits,
      provisionedReadCapacityAutoScalingSettingsUpdate
    );
  }

  public static DafnySequence<
    ? extends ReplicaGlobalSecondaryIndexSettingsUpdate
  > ReplicaGlobalSecondaryIndexSettingsUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaGlobalSecondaryIndexSettingsUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaGlobalSecondaryIndexSettingsUpdate,
      ReplicaGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
    );
  }

  public static DafnySequence<? extends Replica> ReplicaList(
    List<software.amazon.awssdk.services.dynamodb.model.Replica> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Replica,
      Replica._typeDescriptor()
    );
  }

  public static ReplicaSettingsDescription ReplicaSettingsDescription(
    software.amazon.awssdk.services.dynamodb.model.ReplicaSettingsDescription nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    Option<ReplicaStatus> replicaStatus;
    replicaStatus =
      Objects.nonNull(nativeValue.replicaStatus())
        ? Option.create_Some(
          ReplicaStatus._typeDescriptor(),
          ToDafny.ReplicaStatus(nativeValue.replicaStatus())
        )
        : Option.create_None(ReplicaStatus._typeDescriptor());
    Option<BillingModeSummary> replicaBillingModeSummary;
    replicaBillingModeSummary =
      Objects.nonNull(nativeValue.replicaBillingModeSummary())
        ? Option.create_Some(
          BillingModeSummary._typeDescriptor(),
          ToDafny.BillingModeSummary(nativeValue.replicaBillingModeSummary())
        )
        : Option.create_None(BillingModeSummary._typeDescriptor());
    Option<Long> replicaProvisionedReadCapacityUnits;
    replicaProvisionedReadCapacityUnits =
      Objects.nonNull(nativeValue.replicaProvisionedReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.replicaProvisionedReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsDescription
    > replicaProvisionedReadCapacityAutoScalingSettings;
    replicaProvisionedReadCapacityAutoScalingSettings =
      Objects.nonNull(
          nativeValue.replicaProvisionedReadCapacityAutoScalingSettings()
        )
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.replicaProvisionedReadCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<Long> replicaProvisionedWriteCapacityUnits;
    replicaProvisionedWriteCapacityUnits =
      Objects.nonNull(nativeValue.replicaProvisionedWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.replicaProvisionedWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsDescription
    > replicaProvisionedWriteCapacityAutoScalingSettings;
    replicaProvisionedWriteCapacityAutoScalingSettings =
      Objects.nonNull(
          nativeValue.replicaProvisionedWriteCapacityAutoScalingSettings()
        )
        ? Option.create_Some(
          AutoScalingSettingsDescription._typeDescriptor(),
          ToDafny.AutoScalingSettingsDescription(
            nativeValue.replicaProvisionedWriteCapacityAutoScalingSettings()
          )
        )
        : Option.create_None(AutoScalingSettingsDescription._typeDescriptor());
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>
    > replicaGlobalSecondaryIndexSettings;
    replicaGlobalSecondaryIndexSettings =
      (Objects.nonNull(nativeValue.replicaGlobalSecondaryIndexSettings()) &&
          nativeValue.replicaGlobalSecondaryIndexSettings().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexSettingsDescription._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexSettingsDescriptionList(
            nativeValue.replicaGlobalSecondaryIndexSettings()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexSettingsDescription._typeDescriptor()
          )
        );
    Option<TableClassSummary> replicaTableClassSummary;
    replicaTableClassSummary =
      Objects.nonNull(nativeValue.replicaTableClassSummary())
        ? Option.create_Some(
          TableClassSummary._typeDescriptor(),
          ToDafny.TableClassSummary(nativeValue.replicaTableClassSummary())
        )
        : Option.create_None(TableClassSummary._typeDescriptor());
    return new ReplicaSettingsDescription(
      regionName,
      replicaStatus,
      replicaBillingModeSummary,
      replicaProvisionedReadCapacityUnits,
      replicaProvisionedReadCapacityAutoScalingSettings,
      replicaProvisionedWriteCapacityUnits,
      replicaProvisionedWriteCapacityAutoScalingSettings,
      replicaGlobalSecondaryIndexSettings,
      replicaTableClassSummary
    );
  }

  public static DafnySequence<
    ? extends ReplicaSettingsDescription
  > ReplicaSettingsDescriptionList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaSettingsDescription
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaSettingsDescription,
      ReplicaSettingsDescription._typeDescriptor()
    );
  }

  public static ReplicaSettingsUpdate ReplicaSettingsUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicaSettingsUpdate nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    Option<Long> replicaProvisionedReadCapacityUnits;
    replicaProvisionedReadCapacityUnits =
      Objects.nonNull(nativeValue.replicaProvisionedReadCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.replicaProvisionedReadCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsUpdate
    > replicaProvisionedReadCapacityAutoScalingSettingsUpdate;
    replicaProvisionedReadCapacityAutoScalingSettingsUpdate =
      Objects.nonNull(
          nativeValue.replicaProvisionedReadCapacityAutoScalingSettingsUpdate()
        )
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.replicaProvisionedReadCapacityAutoScalingSettingsUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>
    > replicaGlobalSecondaryIndexSettingsUpdate;
    replicaGlobalSecondaryIndexSettingsUpdate =
      (Objects.nonNull(
            nativeValue.replicaGlobalSecondaryIndexSettingsUpdate()
          ) &&
          nativeValue.replicaGlobalSecondaryIndexSettingsUpdate().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexSettingsUpdateList(
            nativeValue.replicaGlobalSecondaryIndexSettingsUpdate()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
          )
        );
    Option<TableClass> replicaTableClass;
    replicaTableClass =
      Objects.nonNull(nativeValue.replicaTableClass())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.replicaTableClass())
        )
        : Option.create_None(TableClass._typeDescriptor());
    return new ReplicaSettingsUpdate(
      regionName,
      replicaProvisionedReadCapacityUnits,
      replicaProvisionedReadCapacityAutoScalingSettingsUpdate,
      replicaGlobalSecondaryIndexSettingsUpdate,
      replicaTableClass
    );
  }

  public static DafnySequence<
    ? extends ReplicaSettingsUpdate
  > ReplicaSettingsUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaSettingsUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaSettingsUpdate,
      ReplicaSettingsUpdate._typeDescriptor()
    );
  }

  public static ReplicationGroupUpdate ReplicationGroupUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicationGroupUpdate nativeValue
  ) {
    Option<CreateReplicationGroupMemberAction> create;
    create =
      Objects.nonNull(nativeValue.create())
        ? Option.create_Some(
          CreateReplicationGroupMemberAction._typeDescriptor(),
          ToDafny.CreateReplicationGroupMemberAction(nativeValue.create())
        )
        : Option.create_None(
          CreateReplicationGroupMemberAction._typeDescriptor()
        );
    Option<UpdateReplicationGroupMemberAction> update;
    update =
      Objects.nonNull(nativeValue.update())
        ? Option.create_Some(
          UpdateReplicationGroupMemberAction._typeDescriptor(),
          ToDafny.UpdateReplicationGroupMemberAction(nativeValue.update())
        )
        : Option.create_None(
          UpdateReplicationGroupMemberAction._typeDescriptor()
        );
    Option<DeleteReplicationGroupMemberAction> delete;
    delete =
      Objects.nonNull(nativeValue.delete())
        ? Option.create_Some(
          DeleteReplicationGroupMemberAction._typeDescriptor(),
          ToDafny.DeleteReplicationGroupMemberAction(nativeValue.delete())
        )
        : Option.create_None(
          DeleteReplicationGroupMemberAction._typeDescriptor()
        );
    return new ReplicationGroupUpdate(create, update, delete);
  }

  public static DafnySequence<
    ? extends ReplicationGroupUpdate
  > ReplicationGroupUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicationGroupUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicationGroupUpdate,
      ReplicationGroupUpdate._typeDescriptor()
    );
  }

  public static ReplicaUpdate ReplicaUpdate(
    software.amazon.awssdk.services.dynamodb.model.ReplicaUpdate nativeValue
  ) {
    Option<CreateReplicaAction> create;
    create =
      Objects.nonNull(nativeValue.create())
        ? Option.create_Some(
          CreateReplicaAction._typeDescriptor(),
          ToDafny.CreateReplicaAction(nativeValue.create())
        )
        : Option.create_None(CreateReplicaAction._typeDescriptor());
    Option<DeleteReplicaAction> delete;
    delete =
      Objects.nonNull(nativeValue.delete())
        ? Option.create_Some(
          DeleteReplicaAction._typeDescriptor(),
          ToDafny.DeleteReplicaAction(nativeValue.delete())
        )
        : Option.create_None(DeleteReplicaAction._typeDescriptor());
    return new ReplicaUpdate(create, delete);
  }

  public static DafnySequence<? extends ReplicaUpdate> ReplicaUpdateList(
    List<
      software.amazon.awssdk.services.dynamodb.model.ReplicaUpdate
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::ReplicaUpdate,
      ReplicaUpdate._typeDescriptor()
    );
  }

  public static RestoreSummary RestoreSummary(
    software.amazon.awssdk.services.dynamodb.model.RestoreSummary nativeValue
  ) {
    Option<DafnySequence<? extends Character>> sourceBackupArn;
    sourceBackupArn =
      Objects.nonNull(nativeValue.sourceBackupArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceBackupArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> sourceTableArn;
    sourceTableArn =
      Objects.nonNull(nativeValue.sourceTableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceTableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    DafnySequence<? extends Character> restoreDateTime;
    restoreDateTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.restoreDateTime()
      );
    Boolean restoreInProgress;
    restoreInProgress = (nativeValue.restoreInProgress());
    return new RestoreSummary(
      sourceBackupArn,
      sourceTableArn,
      restoreDateTime,
      restoreInProgress
    );
  }

  public static RestoreTableFromBackupInput RestoreTableFromBackupInput(
    RestoreTableFromBackupRequest nativeValue
  ) {
    DafnySequence<? extends Character> targetTableName;
    targetTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.targetTableName()
      );
    DafnySequence<? extends Character> backupArn;
    backupArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.backupArn()
      );
    Option<BillingMode> billingModeOverride;
    billingModeOverride =
      Objects.nonNull(nativeValue.billingModeOverride())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingModeOverride())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<
      DafnySequence<? extends GlobalSecondaryIndex>
    > globalSecondaryIndexOverride;
    globalSecondaryIndexOverride =
      (Objects.nonNull(nativeValue.globalSecondaryIndexOverride()) &&
          nativeValue.globalSecondaryIndexOverride().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor()),
          ToDafny.GlobalSecondaryIndexList(
            nativeValue.globalSecondaryIndexOverride()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor())
        );
    Option<
      DafnySequence<? extends LocalSecondaryIndex>
    > localSecondaryIndexOverride;
    localSecondaryIndexOverride =
      (Objects.nonNull(nativeValue.localSecondaryIndexOverride()) &&
          nativeValue.localSecondaryIndexOverride().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor()),
          ToDafny.LocalSecondaryIndexList(
            nativeValue.localSecondaryIndexOverride()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor())
        );
    Option<ProvisionedThroughput> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughputOverride())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    Option<SSESpecification> sSESpecificationOverride;
    sSESpecificationOverride =
      Objects.nonNull(nativeValue.sseSpecificationOverride())
        ? Option.create_Some(
          SSESpecification._typeDescriptor(),
          ToDafny.SSESpecification(nativeValue.sseSpecificationOverride())
        )
        : Option.create_None(SSESpecification._typeDescriptor());
    return new RestoreTableFromBackupInput(
      targetTableName,
      backupArn,
      billingModeOverride,
      globalSecondaryIndexOverride,
      localSecondaryIndexOverride,
      provisionedThroughputOverride,
      onDemandThroughputOverride,
      sSESpecificationOverride
    );
  }

  public static RestoreTableFromBackupOutput RestoreTableFromBackupOutput(
    RestoreTableFromBackupResponse nativeValue
  ) {
    Option<TableDescription> tableDescription;
    tableDescription =
      Objects.nonNull(nativeValue.tableDescription())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.tableDescription())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new RestoreTableFromBackupOutput(tableDescription);
  }

  public static RestoreTableToPointInTimeInput RestoreTableToPointInTimeInput(
    RestoreTableToPointInTimeRequest nativeValue
  ) {
    Option<DafnySequence<? extends Character>> sourceTableArn;
    sourceTableArn =
      Objects.nonNull(nativeValue.sourceTableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceTableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> sourceTableName;
    sourceTableName =
      Objects.nonNull(nativeValue.sourceTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.sourceTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    DafnySequence<? extends Character> targetTableName;
    targetTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.targetTableName()
      );
    Option<Boolean> useLatestRestorableTime;
    useLatestRestorableTime =
      Objects.nonNull(nativeValue.useLatestRestorableTime())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.useLatestRestorableTime())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<DafnySequence<? extends Character>> restoreDateTime;
    restoreDateTime =
      Objects.nonNull(nativeValue.restoreDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.restoreDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<BillingMode> billingModeOverride;
    billingModeOverride =
      Objects.nonNull(nativeValue.billingModeOverride())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingModeOverride())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<
      DafnySequence<? extends GlobalSecondaryIndex>
    > globalSecondaryIndexOverride;
    globalSecondaryIndexOverride =
      (Objects.nonNull(nativeValue.globalSecondaryIndexOverride()) &&
          nativeValue.globalSecondaryIndexOverride().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor()),
          ToDafny.GlobalSecondaryIndexList(
            nativeValue.globalSecondaryIndexOverride()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor())
        );
    Option<
      DafnySequence<? extends LocalSecondaryIndex>
    > localSecondaryIndexOverride;
    localSecondaryIndexOverride =
      (Objects.nonNull(nativeValue.localSecondaryIndexOverride()) &&
          nativeValue.localSecondaryIndexOverride().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor()),
          ToDafny.LocalSecondaryIndexList(
            nativeValue.localSecondaryIndexOverride()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(LocalSecondaryIndex._typeDescriptor())
        );
    Option<ProvisionedThroughput> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughputOverride())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    Option<SSESpecification> sSESpecificationOverride;
    sSESpecificationOverride =
      Objects.nonNull(nativeValue.sseSpecificationOverride())
        ? Option.create_Some(
          SSESpecification._typeDescriptor(),
          ToDafny.SSESpecification(nativeValue.sseSpecificationOverride())
        )
        : Option.create_None(SSESpecification._typeDescriptor());
    return new RestoreTableToPointInTimeInput(
      sourceTableArn,
      sourceTableName,
      targetTableName,
      useLatestRestorableTime,
      restoreDateTime,
      billingModeOverride,
      globalSecondaryIndexOverride,
      localSecondaryIndexOverride,
      provisionedThroughputOverride,
      onDemandThroughputOverride,
      sSESpecificationOverride
    );
  }

  public static RestoreTableToPointInTimeOutput RestoreTableToPointInTimeOutput(
    RestoreTableToPointInTimeResponse nativeValue
  ) {
    Option<TableDescription> tableDescription;
    tableDescription =
      Objects.nonNull(nativeValue.tableDescription())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.tableDescription())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new RestoreTableToPointInTimeOutput(tableDescription);
  }

  public static S3BucketSource S3BucketSource(
    software.amazon.awssdk.services.dynamodb.model.S3BucketSource nativeValue
  ) {
    Option<DafnySequence<? extends Character>> s3BucketOwner;
    s3BucketOwner =
      Objects.nonNull(nativeValue.s3BucketOwner())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3BucketOwner()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    DafnySequence<? extends Character> s3Bucket;
    s3Bucket =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.s3Bucket()
      );
    Option<DafnySequence<? extends Character>> s3KeyPrefix;
    s3KeyPrefix =
      Objects.nonNull(nativeValue.s3KeyPrefix())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.s3KeyPrefix()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new S3BucketSource(s3BucketOwner, s3Bucket, s3KeyPrefix);
  }

  public static ScanInput ScanInput(ScanRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnySequence<? extends DafnySequence<? extends Character>>
    > attributesToGet;
    attributesToGet =
      (Objects.nonNull(nativeValue.attributesToGet()) &&
          nativeValue.attributesToGet().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.AttributeNameList(nativeValue.attributesToGet())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<Integer> limit;
    limit =
      Objects.nonNull(nativeValue.limit())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.limit()))
        : Option.create_None(TypeDescriptor.INT);
    Option<Select> select;
    select =
      Objects.nonNull(nativeValue.select())
        ? Option.create_Some(
          Select._typeDescriptor(),
          ToDafny.Select(nativeValue.select())
        )
        : Option.create_None(Select._typeDescriptor());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends Condition
      >
    > scanFilter;
    scanFilter =
      (Objects.nonNull(nativeValue.scanFilter()) &&
          nativeValue.scanFilter().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          ),
          ToDafny.FilterConditionMap(nativeValue.scanFilter())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            Condition._typeDescriptor()
          )
        );
    Option<ConditionalOperator> conditionalOperator;
    conditionalOperator =
      Objects.nonNull(nativeValue.conditionalOperator())
        ? Option.create_Some(
          ConditionalOperator._typeDescriptor(),
          ToDafny.ConditionalOperator(nativeValue.conditionalOperator())
        )
        : Option.create_None(ConditionalOperator._typeDescriptor());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > exclusiveStartKey;
    exclusiveStartKey =
      (Objects.nonNull(nativeValue.exclusiveStartKey()) &&
          nativeValue.exclusiveStartKey().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.Key(nativeValue.exclusiveStartKey())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<Integer> totalSegments;
    totalSegments =
      Objects.nonNull(nativeValue.totalSegments())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.totalSegments()))
        : Option.create_None(TypeDescriptor.INT);
    Option<Integer> segment;
    segment =
      Objects.nonNull(nativeValue.segment())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.segment()))
        : Option.create_None(TypeDescriptor.INT);
    Option<DafnySequence<? extends Character>> projectionExpression;
    projectionExpression =
      Objects.nonNull(nativeValue.projectionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.projectionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> filterExpression;
    filterExpression =
      Objects.nonNull(nativeValue.filterExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.filterExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<Boolean> consistentRead;
    consistentRead =
      Objects.nonNull(nativeValue.consistentRead())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.consistentRead())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    return new ScanInput(
      tableName,
      indexName,
      attributesToGet,
      limit,
      select,
      scanFilter,
      conditionalOperator,
      exclusiveStartKey,
      returnConsumedCapacity,
      totalSegments,
      segment,
      projectionExpression,
      filterExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      consistentRead
    );
  }

  public static ScanOutput ScanOutput(ScanResponse nativeValue) {
    Option<
      DafnySequence<
        ? extends DafnyMap<
          ? extends DafnySequence<? extends Character>,
          ? extends AttributeValue
        >
      >
    > items;
    items =
      (Objects.nonNull(nativeValue.items()) && nativeValue.items().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          ),
          ToDafny.ItemList(nativeValue.items())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            TypeDescriptor.referenceWithInitializer(
              dafny.DafnyMap.class,
              () ->
                dafny.DafnyMap.<
                  dafny.DafnySequence<? extends Character>,
                  AttributeValue
                >empty()
            )
          )
        );
    Option<Integer> count;
    count =
      Objects.nonNull(nativeValue.count())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.count()))
        : Option.create_None(TypeDescriptor.INT);
    Option<Integer> scannedCount;
    scannedCount =
      Objects.nonNull(nativeValue.scannedCount())
        ? Option.create_Some(TypeDescriptor.INT, (nativeValue.scannedCount()))
        : Option.create_None(TypeDescriptor.INT);
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > lastEvaluatedKey;
    lastEvaluatedKey =
      (Objects.nonNull(nativeValue.lastEvaluatedKey()) &&
          nativeValue.lastEvaluatedKey().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.Key(nativeValue.lastEvaluatedKey())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    return new ScanOutput(
      items,
      count,
      scannedCount,
      lastEvaluatedKey,
      consumedCapacity
    );
  }

  public static DafnyMap<
    ? extends DafnySequence<? extends Character>,
    ? extends Capacity
  > SecondaryIndexesCapacityMap(
    Map<
      String,
      software.amazon.awssdk.services.dynamodb.model.Capacity
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToMap(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Capacity
    );
  }

  public static SourceTableDetails SourceTableDetails(
    software.amazon.awssdk.services.dynamodb.model.SourceTableDetails nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> tableId;
    tableId =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableId()
      );
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<Long> tableSizeBytes;
    tableSizeBytes =
      Objects.nonNull(nativeValue.tableSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.tableSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    DafnySequence<? extends Character> tableCreationDateTime;
    tableCreationDateTime =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableCreationDateTime()
      );
    ProvisionedThroughput provisionedThroughput;
    provisionedThroughput =
      ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    Option<Long> itemCount;
    itemCount =
      Objects.nonNull(nativeValue.itemCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.itemCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<BillingMode> billingMode;
    billingMode =
      Objects.nonNull(nativeValue.billingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    return new SourceTableDetails(
      tableName,
      tableId,
      tableArn,
      tableSizeBytes,
      keySchema,
      tableCreationDateTime,
      provisionedThroughput,
      onDemandThroughput,
      itemCount,
      billingMode
    );
  }

  public static SourceTableFeatureDetails SourceTableFeatureDetails(
    software.amazon.awssdk.services.dynamodb.model.SourceTableFeatureDetails nativeValue
  ) {
    Option<
      DafnySequence<? extends LocalSecondaryIndexInfo>
    > localSecondaryIndexes;
    localSecondaryIndexes =
      (Objects.nonNull(nativeValue.localSecondaryIndexes()) &&
          nativeValue.localSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            LocalSecondaryIndexInfo._typeDescriptor()
          ),
          ToDafny.LocalSecondaryIndexes(nativeValue.localSecondaryIndexes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            LocalSecondaryIndexInfo._typeDescriptor()
          )
        );
    Option<
      DafnySequence<? extends GlobalSecondaryIndexInfo>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexInfo._typeDescriptor()
          ),
          ToDafny.GlobalSecondaryIndexes(nativeValue.globalSecondaryIndexes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexInfo._typeDescriptor()
          )
        );
    Option<StreamSpecification> streamDescription;
    streamDescription =
      Objects.nonNull(nativeValue.streamDescription())
        ? Option.create_Some(
          StreamSpecification._typeDescriptor(),
          ToDafny.StreamSpecification(nativeValue.streamDescription())
        )
        : Option.create_None(StreamSpecification._typeDescriptor());
    Option<TimeToLiveDescription> timeToLiveDescription;
    timeToLiveDescription =
      Objects.nonNull(nativeValue.timeToLiveDescription())
        ? Option.create_Some(
          TimeToLiveDescription._typeDescriptor(),
          ToDafny.TimeToLiveDescription(nativeValue.timeToLiveDescription())
        )
        : Option.create_None(TimeToLiveDescription._typeDescriptor());
    Option<SSEDescription> sSEDescription;
    sSEDescription =
      Objects.nonNull(nativeValue.sseDescription())
        ? Option.create_Some(
          SSEDescription._typeDescriptor(),
          ToDafny.SSEDescription(nativeValue.sseDescription())
        )
        : Option.create_None(SSEDescription._typeDescriptor());
    return new SourceTableFeatureDetails(
      localSecondaryIndexes,
      globalSecondaryIndexes,
      streamDescription,
      timeToLiveDescription,
      sSEDescription
    );
  }

  public static SSEDescription SSEDescription(
    software.amazon.awssdk.services.dynamodb.model.SSEDescription nativeValue
  ) {
    Option<SSEStatus> status;
    status =
      Objects.nonNull(nativeValue.status())
        ? Option.create_Some(
          SSEStatus._typeDescriptor(),
          ToDafny.SSEStatus(nativeValue.status())
        )
        : Option.create_None(SSEStatus._typeDescriptor());
    Option<SSEType> sSEType;
    sSEType =
      Objects.nonNull(nativeValue.sseType())
        ? Option.create_Some(
          SSEType._typeDescriptor(),
          ToDafny.SSEType(nativeValue.sseType())
        )
        : Option.create_None(SSEType._typeDescriptor());
    Option<DafnySequence<? extends Character>> kMSMasterKeyArn;
    kMSMasterKeyArn =
      Objects.nonNull(nativeValue.kmsMasterKeyArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.kmsMasterKeyArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> inaccessibleEncryptionDateTime;
    inaccessibleEncryptionDateTime =
      Objects.nonNull(nativeValue.inaccessibleEncryptionDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.inaccessibleEncryptionDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new SSEDescription(
      status,
      sSEType,
      kMSMasterKeyArn,
      inaccessibleEncryptionDateTime
    );
  }

  public static SSESpecification SSESpecification(
    software.amazon.awssdk.services.dynamodb.model.SSESpecification nativeValue
  ) {
    Option<Boolean> enabled;
    enabled =
      Objects.nonNull(nativeValue.enabled())
        ? Option.create_Some(TypeDescriptor.BOOLEAN, (nativeValue.enabled()))
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<SSEType> sSEType;
    sSEType =
      Objects.nonNull(nativeValue.sseType())
        ? Option.create_Some(
          SSEType._typeDescriptor(),
          ToDafny.SSEType(nativeValue.sseType())
        )
        : Option.create_None(SSEType._typeDescriptor());
    Option<DafnySequence<? extends Character>> kMSMasterKeyId;
    kMSMasterKeyId =
      Objects.nonNull(nativeValue.kmsMasterKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.kmsMasterKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new SSESpecification(enabled, sSEType, kMSMasterKeyId);
  }

  public static StreamSpecification StreamSpecification(
    software.amazon.awssdk.services.dynamodb.model.StreamSpecification nativeValue
  ) {
    Boolean streamEnabled;
    streamEnabled = (nativeValue.streamEnabled());
    Option<StreamViewType> streamViewType;
    streamViewType =
      Objects.nonNull(nativeValue.streamViewType())
        ? Option.create_Some(
          StreamViewType._typeDescriptor(),
          ToDafny.StreamViewType(nativeValue.streamViewType())
        )
        : Option.create_None(StreamViewType._typeDescriptor());
    return new StreamSpecification(streamEnabled, streamViewType);
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > StringSetAttributeValue(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static TableAutoScalingDescription TableAutoScalingDescription(
    software.amazon.awssdk.services.dynamodb.model.TableAutoScalingDescription nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<TableStatus> tableStatus;
    tableStatus =
      Objects.nonNull(nativeValue.tableStatus())
        ? Option.create_Some(
          TableStatus._typeDescriptor(),
          ToDafny.TableStatus(nativeValue.tableStatus())
        )
        : Option.create_None(TableStatus._typeDescriptor());
    Option<DafnySequence<? extends ReplicaAutoScalingDescription>> replicas;
    replicas =
      (Objects.nonNull(nativeValue.replicas()) &&
          nativeValue.replicas().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaAutoScalingDescription._typeDescriptor()
          ),
          ToDafny.ReplicaAutoScalingDescriptionList(nativeValue.replicas())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaAutoScalingDescription._typeDescriptor()
          )
        );
    return new TableAutoScalingDescription(tableName, tableStatus, replicas);
  }

  public static TableClassSummary TableClassSummary(
    software.amazon.awssdk.services.dynamodb.model.TableClassSummary nativeValue
  ) {
    Option<TableClass> tableClass;
    tableClass =
      Objects.nonNull(nativeValue.tableClass())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.tableClass())
        )
        : Option.create_None(TableClass._typeDescriptor());
    Option<DafnySequence<? extends Character>> lastUpdateDateTime;
    lastUpdateDateTime =
      Objects.nonNull(nativeValue.lastUpdateDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.lastUpdateDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new TableClassSummary(tableClass, lastUpdateDateTime);
  }

  public static TableCreationParameters TableCreationParameters(
    software.amazon.awssdk.services.dynamodb.model.TableCreationParameters nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends AttributeDefinition> attributeDefinitions;
    attributeDefinitions =
      ToDafny.AttributeDefinitions(nativeValue.attributeDefinitions());
    DafnySequence<? extends KeySchemaElement> keySchema;
    keySchema = ToDafny.KeySchema(nativeValue.keySchema());
    Option<BillingMode> billingMode;
    billingMode =
      Objects.nonNull(nativeValue.billingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    Option<SSESpecification> sSESpecification;
    sSESpecification =
      Objects.nonNull(nativeValue.sseSpecification())
        ? Option.create_Some(
          SSESpecification._typeDescriptor(),
          ToDafny.SSESpecification(nativeValue.sseSpecification())
        )
        : Option.create_None(SSESpecification._typeDescriptor());
    Option<
      DafnySequence<? extends GlobalSecondaryIndex>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor()),
          ToDafny.GlobalSecondaryIndexList(nativeValue.globalSecondaryIndexes())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(GlobalSecondaryIndex._typeDescriptor())
        );
    return new TableCreationParameters(
      tableName,
      attributeDefinitions,
      keySchema,
      billingMode,
      provisionedThroughput,
      onDemandThroughput,
      sSESpecification,
      globalSecondaryIndexes
    );
  }

  public static TableDescription TableDescription(
    software.amazon.awssdk.services.dynamodb.model.TableDescription nativeValue
  ) {
    Option<DafnySequence<? extends AttributeDefinition>> attributeDefinitions;
    attributeDefinitions =
      (Objects.nonNull(nativeValue.attributeDefinitions()) &&
          nativeValue.attributeDefinitions().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeDefinition._typeDescriptor()),
          ToDafny.AttributeDefinitions(nativeValue.attributeDefinitions())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeDefinition._typeDescriptor())
        );
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends KeySchemaElement>> keySchema;
    keySchema =
      (Objects.nonNull(nativeValue.keySchema()) &&
          nativeValue.keySchema().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor()),
          ToDafny.KeySchema(nativeValue.keySchema())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(KeySchemaElement._typeDescriptor())
        );
    Option<TableStatus> tableStatus;
    tableStatus =
      Objects.nonNull(nativeValue.tableStatus())
        ? Option.create_Some(
          TableStatus._typeDescriptor(),
          ToDafny.TableStatus(nativeValue.tableStatus())
        )
        : Option.create_None(TableStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> creationDateTime;
    creationDateTime =
      Objects.nonNull(nativeValue.creationDateTime())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.creationDateTime()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ProvisionedThroughputDescription> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughputDescription._typeDescriptor(),
          ToDafny.ProvisionedThroughputDescription(
            nativeValue.provisionedThroughput()
          )
        )
        : Option.create_None(
          ProvisionedThroughputDescription._typeDescriptor()
        );
    Option<Long> tableSizeBytes;
    tableSizeBytes =
      Objects.nonNull(nativeValue.tableSizeBytes())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.tableSizeBytes())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<Long> itemCount;
    itemCount =
      Objects.nonNull(nativeValue.itemCount())
        ? Option.create_Some(TypeDescriptor.LONG, (nativeValue.itemCount()))
        : Option.create_None(TypeDescriptor.LONG);
    Option<DafnySequence<? extends Character>> tableArn;
    tableArn =
      Objects.nonNull(nativeValue.tableArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> tableId;
    tableId =
      Objects.nonNull(nativeValue.tableId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<BillingModeSummary> billingModeSummary;
    billingModeSummary =
      Objects.nonNull(nativeValue.billingModeSummary())
        ? Option.create_Some(
          BillingModeSummary._typeDescriptor(),
          ToDafny.BillingModeSummary(nativeValue.billingModeSummary())
        )
        : Option.create_None(BillingModeSummary._typeDescriptor());
    Option<
      DafnySequence<? extends LocalSecondaryIndexDescription>
    > localSecondaryIndexes;
    localSecondaryIndexes =
      (Objects.nonNull(nativeValue.localSecondaryIndexes()) &&
          nativeValue.localSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            LocalSecondaryIndexDescription._typeDescriptor()
          ),
          ToDafny.LocalSecondaryIndexDescriptionList(
            nativeValue.localSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            LocalSecondaryIndexDescription._typeDescriptor()
          )
        );
    Option<
      DafnySequence<? extends GlobalSecondaryIndexDescription>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexDescription._typeDescriptor()
          ),
          ToDafny.GlobalSecondaryIndexDescriptionList(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexDescription._typeDescriptor()
          )
        );
    Option<StreamSpecification> streamSpecification;
    streamSpecification =
      Objects.nonNull(nativeValue.streamSpecification())
        ? Option.create_Some(
          StreamSpecification._typeDescriptor(),
          ToDafny.StreamSpecification(nativeValue.streamSpecification())
        )
        : Option.create_None(StreamSpecification._typeDescriptor());
    Option<DafnySequence<? extends Character>> latestStreamLabel;
    latestStreamLabel =
      Objects.nonNull(nativeValue.latestStreamLabel())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.latestStreamLabel()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> latestStreamArn;
    latestStreamArn =
      Objects.nonNull(nativeValue.latestStreamArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.latestStreamArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> globalTableVersion;
    globalTableVersion =
      Objects.nonNull(nativeValue.globalTableVersion())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableVersion()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends ReplicaDescription>> replicas;
    replicas =
      (Objects.nonNull(nativeValue.replicas()) &&
          nativeValue.replicas().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ReplicaDescription._typeDescriptor()),
          ToDafny.ReplicaDescriptionList(nativeValue.replicas())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ReplicaDescription._typeDescriptor())
        );
    Option<RestoreSummary> restoreSummary;
    restoreSummary =
      Objects.nonNull(nativeValue.restoreSummary())
        ? Option.create_Some(
          RestoreSummary._typeDescriptor(),
          ToDafny.RestoreSummary(nativeValue.restoreSummary())
        )
        : Option.create_None(RestoreSummary._typeDescriptor());
    Option<SSEDescription> sSEDescription;
    sSEDescription =
      Objects.nonNull(nativeValue.sseDescription())
        ? Option.create_Some(
          SSEDescription._typeDescriptor(),
          ToDafny.SSEDescription(nativeValue.sseDescription())
        )
        : Option.create_None(SSEDescription._typeDescriptor());
    Option<ArchivalSummary> archivalSummary;
    archivalSummary =
      Objects.nonNull(nativeValue.archivalSummary())
        ? Option.create_Some(
          ArchivalSummary._typeDescriptor(),
          ToDafny.ArchivalSummary(nativeValue.archivalSummary())
        )
        : Option.create_None(ArchivalSummary._typeDescriptor());
    Option<TableClassSummary> tableClassSummary;
    tableClassSummary =
      Objects.nonNull(nativeValue.tableClassSummary())
        ? Option.create_Some(
          TableClassSummary._typeDescriptor(),
          ToDafny.TableClassSummary(nativeValue.tableClassSummary())
        )
        : Option.create_None(TableClassSummary._typeDescriptor());
    Option<Boolean> deletionProtectionEnabled;
    deletionProtectionEnabled =
      Objects.nonNull(nativeValue.deletionProtectionEnabled())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.deletionProtectionEnabled())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new TableDescription(
      attributeDefinitions,
      tableName,
      keySchema,
      tableStatus,
      creationDateTime,
      provisionedThroughput,
      tableSizeBytes,
      itemCount,
      tableArn,
      tableId,
      billingModeSummary,
      localSecondaryIndexes,
      globalSecondaryIndexes,
      streamSpecification,
      latestStreamLabel,
      latestStreamArn,
      globalTableVersion,
      replicas,
      restoreSummary,
      sSEDescription,
      archivalSummary,
      tableClassSummary,
      deletionProtectionEnabled,
      onDemandThroughput
    );
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > TableNameList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static Tag Tag(
    software.amazon.awssdk.services.dynamodb.model.Tag nativeValue
  ) {
    DafnySequence<? extends Character> key;
    key =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.key()
      );
    DafnySequence<? extends Character> value;
    value =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.value()
      );
    return new Tag(key, value);
  }

  public static DafnySequence<
    ? extends DafnySequence<? extends Character>
  > TagKeyList(List<String> nativeValue) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.smithy.dafny.conversion.ToDafny.Simple::CharacterSequence,
      DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
    );
  }

  public static DafnySequence<? extends Tag> TagList(
    List<software.amazon.awssdk.services.dynamodb.model.Tag> nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::Tag,
      Tag._typeDescriptor()
    );
  }

  public static TagResourceInput TagResourceInput(
    TagResourceRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    DafnySequence<? extends Tag> tags;
    tags = ToDafny.TagList(nativeValue.tags());
    return new TagResourceInput(resourceArn, tags);
  }

  public static TimeToLiveDescription TimeToLiveDescription(
    software.amazon.awssdk.services.dynamodb.model.TimeToLiveDescription nativeValue
  ) {
    Option<TimeToLiveStatus> timeToLiveStatus;
    timeToLiveStatus =
      Objects.nonNull(nativeValue.timeToLiveStatus())
        ? Option.create_Some(
          TimeToLiveStatus._typeDescriptor(),
          ToDafny.TimeToLiveStatus(nativeValue.timeToLiveStatus())
        )
        : Option.create_None(TimeToLiveStatus._typeDescriptor());
    Option<DafnySequence<? extends Character>> attributeName;
    attributeName =
      Objects.nonNull(nativeValue.attributeName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.attributeName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new TimeToLiveDescription(timeToLiveStatus, attributeName);
  }

  public static TimeToLiveSpecification TimeToLiveSpecification(
    software.amazon.awssdk.services.dynamodb.model.TimeToLiveSpecification nativeValue
  ) {
    Boolean enabled;
    enabled = (nativeValue.enabled());
    DafnySequence<? extends Character> attributeName;
    attributeName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.attributeName()
      );
    return new TimeToLiveSpecification(enabled, attributeName);
  }

  public static TransactGetItem TransactGetItem(
    software.amazon.awssdk.services.dynamodb.model.TransactGetItem nativeValue
  ) {
    Get get;
    get = ToDafny.Get(nativeValue.get());
    return new TransactGetItem(get);
  }

  public static DafnySequence<? extends TransactGetItem> TransactGetItemList(
    List<
      software.amazon.awssdk.services.dynamodb.model.TransactGetItem
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::TransactGetItem,
      TransactGetItem._typeDescriptor()
    );
  }

  public static TransactGetItemsInput TransactGetItemsInput(
    TransactGetItemsRequest nativeValue
  ) {
    DafnySequence<? extends TransactGetItem> transactItems;
    transactItems = ToDafny.TransactGetItemList(nativeValue.transactItems());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    return new TransactGetItemsInput(transactItems, returnConsumedCapacity);
  }

  public static TransactGetItemsOutput TransactGetItemsOutput(
    TransactGetItemsResponse nativeValue
  ) {
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    Option<DafnySequence<? extends ItemResponse>> responses;
    responses =
      (Objects.nonNull(nativeValue.responses()) &&
          nativeValue.responses().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ItemResponse._typeDescriptor()),
          ToDafny.ItemResponseList(nativeValue.responses())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ItemResponse._typeDescriptor())
        );
    return new TransactGetItemsOutput(consumedCapacity, responses);
  }

  public static TransactWriteItem TransactWriteItem(
    software.amazon.awssdk.services.dynamodb.model.TransactWriteItem nativeValue
  ) {
    Option<ConditionCheck> conditionCheck;
    conditionCheck =
      Objects.nonNull(nativeValue.conditionCheck())
        ? Option.create_Some(
          ConditionCheck._typeDescriptor(),
          ToDafny.ConditionCheck(nativeValue.conditionCheck())
        )
        : Option.create_None(ConditionCheck._typeDescriptor());
    Option<Put> put;
    put =
      Objects.nonNull(nativeValue.put())
        ? Option.create_Some(
          Put._typeDescriptor(),
          ToDafny.Put(nativeValue.put())
        )
        : Option.create_None(Put._typeDescriptor());
    Option<Delete> delete;
    delete =
      Objects.nonNull(nativeValue.delete())
        ? Option.create_Some(
          Delete._typeDescriptor(),
          ToDafny.Delete(nativeValue.delete())
        )
        : Option.create_None(Delete._typeDescriptor());
    Option<Update> update;
    update =
      Objects.nonNull(nativeValue.update())
        ? Option.create_Some(
          Update._typeDescriptor(),
          ToDafny.Update(nativeValue.update())
        )
        : Option.create_None(Update._typeDescriptor());
    return new TransactWriteItem(conditionCheck, put, delete, update);
  }

  public static DafnySequence<
    ? extends TransactWriteItem
  > TransactWriteItemList(
    List<
      software.amazon.awssdk.services.dynamodb.model.TransactWriteItem
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::TransactWriteItem,
      TransactWriteItem._typeDescriptor()
    );
  }

  public static TransactWriteItemsInput TransactWriteItemsInput(
    TransactWriteItemsRequest nativeValue
  ) {
    DafnySequence<? extends TransactWriteItem> transactItems;
    transactItems = ToDafny.TransactWriteItemList(nativeValue.transactItems());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<ReturnItemCollectionMetrics> returnItemCollectionMetrics;
    returnItemCollectionMetrics =
      Objects.nonNull(nativeValue.returnItemCollectionMetrics())
        ? Option.create_Some(
          ReturnItemCollectionMetrics._typeDescriptor(),
          ToDafny.ReturnItemCollectionMetrics(
            nativeValue.returnItemCollectionMetrics()
          )
        )
        : Option.create_None(ReturnItemCollectionMetrics._typeDescriptor());
    Option<DafnySequence<? extends Character>> clientRequestToken;
    clientRequestToken =
      Objects.nonNull(nativeValue.clientRequestToken())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.clientRequestToken()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new TransactWriteItemsInput(
      transactItems,
      returnConsumedCapacity,
      returnItemCollectionMetrics,
      clientRequestToken
    );
  }

  public static TransactWriteItemsOutput TransactWriteItemsOutput(
    TransactWriteItemsResponse nativeValue
  ) {
    Option<DafnySequence<? extends ConsumedCapacity>> consumedCapacity;
    consumedCapacity =
      (Objects.nonNull(nativeValue.consumedCapacity()) &&
          nativeValue.consumedCapacity().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor()),
          ToDafny.ConsumedCapacityMultiple(nativeValue.consumedCapacity())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ConsumedCapacity._typeDescriptor())
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends ItemCollectionMetrics>
      >
    > itemCollectionMetrics;
    itemCollectionMetrics =
      (Objects.nonNull(nativeValue.itemCollectionMetrics()) &&
          nativeValue.itemCollectionMetrics().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              ItemCollectionMetrics._typeDescriptor()
            )
          ),
          ToDafny.ItemCollectionMetricsPerTable(
            nativeValue.itemCollectionMetrics()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(
              ItemCollectionMetrics._typeDescriptor()
            )
          )
        );
    return new TransactWriteItemsOutput(
      consumedCapacity,
      itemCollectionMetrics
    );
  }

  public static UntagResourceInput UntagResourceInput(
    UntagResourceRequest nativeValue
  ) {
    DafnySequence<? extends Character> resourceArn;
    resourceArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.resourceArn()
      );
    DafnySequence<? extends DafnySequence<? extends Character>> tagKeys;
    tagKeys = ToDafny.TagKeyList(nativeValue.tagKeys());
    return new UntagResourceInput(resourceArn, tagKeys);
  }

  public static Update Update(
    software.amazon.awssdk.services.dynamodb.model.Update nativeValue
  ) {
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    DafnySequence<? extends Character> updateExpression;
    updateExpression =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.updateExpression()
      );
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new Update(
      key,
      updateExpression,
      tableName,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static UpdateContinuousBackupsInput UpdateContinuousBackupsInput(
    UpdateContinuousBackupsRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    PointInTimeRecoverySpecification pointInTimeRecoverySpecification;
    pointInTimeRecoverySpecification =
      ToDafny.PointInTimeRecoverySpecification(
        nativeValue.pointInTimeRecoverySpecification()
      );
    return new UpdateContinuousBackupsInput(
      tableName,
      pointInTimeRecoverySpecification
    );
  }

  public static UpdateContinuousBackupsOutput UpdateContinuousBackupsOutput(
    UpdateContinuousBackupsResponse nativeValue
  ) {
    Option<ContinuousBackupsDescription> continuousBackupsDescription;
    continuousBackupsDescription =
      Objects.nonNull(nativeValue.continuousBackupsDescription())
        ? Option.create_Some(
          ContinuousBackupsDescription._typeDescriptor(),
          ToDafny.ContinuousBackupsDescription(
            nativeValue.continuousBackupsDescription()
          )
        )
        : Option.create_None(ContinuousBackupsDescription._typeDescriptor());
    return new UpdateContinuousBackupsOutput(continuousBackupsDescription);
  }

  public static UpdateContributorInsightsInput UpdateContributorInsightsInput(
    UpdateContributorInsightsRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    ContributorInsightsAction contributorInsightsAction;
    contributorInsightsAction =
      ToDafny.ContributorInsightsAction(
        nativeValue.contributorInsightsAction()
      );
    return new UpdateContributorInsightsInput(
      tableName,
      indexName,
      contributorInsightsAction
    );
  }

  public static UpdateContributorInsightsOutput UpdateContributorInsightsOutput(
    UpdateContributorInsightsResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> indexName;
    indexName =
      Objects.nonNull(nativeValue.indexName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.indexName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ContributorInsightsStatus> contributorInsightsStatus;
    contributorInsightsStatus =
      Objects.nonNull(nativeValue.contributorInsightsStatus())
        ? Option.create_Some(
          ContributorInsightsStatus._typeDescriptor(),
          ToDafny.ContributorInsightsStatus(
            nativeValue.contributorInsightsStatus()
          )
        )
        : Option.create_None(ContributorInsightsStatus._typeDescriptor());
    return new UpdateContributorInsightsOutput(
      tableName,
      indexName,
      contributorInsightsStatus
    );
  }

  public static UpdateGlobalSecondaryIndexAction UpdateGlobalSecondaryIndexAction(
    software.amazon.awssdk.services.dynamodb.model.UpdateGlobalSecondaryIndexAction nativeValue
  ) {
    DafnySequence<? extends Character> indexName;
    indexName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.indexName()
      );
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new UpdateGlobalSecondaryIndexAction(
      indexName,
      provisionedThroughput,
      onDemandThroughput
    );
  }

  public static UpdateGlobalTableInput UpdateGlobalTableInput(
    UpdateGlobalTableRequest nativeValue
  ) {
    DafnySequence<? extends Character> globalTableName;
    globalTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.globalTableName()
      );
    DafnySequence<? extends ReplicaUpdate> replicaUpdates;
    replicaUpdates = ToDafny.ReplicaUpdateList(nativeValue.replicaUpdates());
    return new UpdateGlobalTableInput(globalTableName, replicaUpdates);
  }

  public static UpdateGlobalTableOutput UpdateGlobalTableOutput(
    UpdateGlobalTableResponse nativeValue
  ) {
    Option<GlobalTableDescription> globalTableDescription;
    globalTableDescription =
      Objects.nonNull(nativeValue.globalTableDescription())
        ? Option.create_Some(
          GlobalTableDescription._typeDescriptor(),
          ToDafny.GlobalTableDescription(nativeValue.globalTableDescription())
        )
        : Option.create_None(GlobalTableDescription._typeDescriptor());
    return new UpdateGlobalTableOutput(globalTableDescription);
  }

  public static UpdateGlobalTableSettingsInput UpdateGlobalTableSettingsInput(
    UpdateGlobalTableSettingsRequest nativeValue
  ) {
    DafnySequence<? extends Character> globalTableName;
    globalTableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.globalTableName()
      );
    Option<BillingMode> globalTableBillingMode;
    globalTableBillingMode =
      Objects.nonNull(nativeValue.globalTableBillingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.globalTableBillingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<Long> globalTableProvisionedWriteCapacityUnits;
    globalTableProvisionedWriteCapacityUnits =
      Objects.nonNull(nativeValue.globalTableProvisionedWriteCapacityUnits())
        ? Option.create_Some(
          TypeDescriptor.LONG,
          (nativeValue.globalTableProvisionedWriteCapacityUnits())
        )
        : Option.create_None(TypeDescriptor.LONG);
    Option<
      AutoScalingSettingsUpdate
    > globalTableProvisionedWriteCapacityAutoScalingSettingsUpdate;
    globalTableProvisionedWriteCapacityAutoScalingSettingsUpdate =
      Objects.nonNull(
          nativeValue.globalTableProvisionedWriteCapacityAutoScalingSettingsUpdate()
        )
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.globalTableProvisionedWriteCapacityAutoScalingSettingsUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    Option<
      DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>
    > globalTableGlobalSecondaryIndexSettingsUpdate;
    globalTableGlobalSecondaryIndexSettingsUpdate =
      (Objects.nonNull(
            nativeValue.globalTableGlobalSecondaryIndexSettingsUpdate()
          ) &&
          nativeValue.globalTableGlobalSecondaryIndexSettingsUpdate().size() >
            0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            GlobalTableGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
          ),
          ToDafny.GlobalTableGlobalSecondaryIndexSettingsUpdateList(
            nativeValue.globalTableGlobalSecondaryIndexSettingsUpdate()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            GlobalTableGlobalSecondaryIndexSettingsUpdate._typeDescriptor()
          )
        );
    Option<
      DafnySequence<? extends ReplicaSettingsUpdate>
    > replicaSettingsUpdate;
    replicaSettingsUpdate =
      (Objects.nonNull(nativeValue.replicaSettingsUpdate()) &&
          nativeValue.replicaSettingsUpdate().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaSettingsUpdate._typeDescriptor()
          ),
          ToDafny.ReplicaSettingsUpdateList(nativeValue.replicaSettingsUpdate())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(ReplicaSettingsUpdate._typeDescriptor())
        );
    return new UpdateGlobalTableSettingsInput(
      globalTableName,
      globalTableBillingMode,
      globalTableProvisionedWriteCapacityUnits,
      globalTableProvisionedWriteCapacityAutoScalingSettingsUpdate,
      globalTableGlobalSecondaryIndexSettingsUpdate,
      replicaSettingsUpdate
    );
  }

  public static UpdateGlobalTableSettingsOutput UpdateGlobalTableSettingsOutput(
    UpdateGlobalTableSettingsResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> globalTableName;
    globalTableName =
      Objects.nonNull(nativeValue.globalTableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.globalTableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends ReplicaSettingsDescription>> replicaSettings;
    replicaSettings =
      (Objects.nonNull(nativeValue.replicaSettings()) &&
          nativeValue.replicaSettings().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaSettingsDescription._typeDescriptor()
          ),
          ToDafny.ReplicaSettingsDescriptionList(nativeValue.replicaSettings())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaSettingsDescription._typeDescriptor()
          )
        );
    return new UpdateGlobalTableSettingsOutput(
      globalTableName,
      replicaSettings
    );
  }

  public static UpdateItemInput UpdateItemInput(UpdateItemRequest nativeValue) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnyMap<
      ? extends DafnySequence<? extends Character>,
      ? extends AttributeValue
    > key;
    key = ToDafny.Key(nativeValue.key());
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValueUpdate
      >
    > attributeUpdates;
    attributeUpdates =
      (Objects.nonNull(nativeValue.attributeUpdates()) &&
          nativeValue.attributeUpdates().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValueUpdate._typeDescriptor()
          ),
          ToDafny.AttributeUpdates(nativeValue.attributeUpdates())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValueUpdate._typeDescriptor()
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends ExpectedAttributeValue
      >
    > expected;
    expected =
      (Objects.nonNull(nativeValue.expected()) &&
          nativeValue.expected().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          ),
          ToDafny.ExpectedAttributeMap(nativeValue.expected())
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            ExpectedAttributeValue._typeDescriptor()
          )
        );
    Option<ConditionalOperator> conditionalOperator;
    conditionalOperator =
      Objects.nonNull(nativeValue.conditionalOperator())
        ? Option.create_Some(
          ConditionalOperator._typeDescriptor(),
          ToDafny.ConditionalOperator(nativeValue.conditionalOperator())
        )
        : Option.create_None(ConditionalOperator._typeDescriptor());
    Option<ReturnValue> returnValues;
    returnValues =
      Objects.nonNull(nativeValue.returnValues())
        ? Option.create_Some(
          ReturnValue._typeDescriptor(),
          ToDafny.ReturnValue(nativeValue.returnValues())
        )
        : Option.create_None(ReturnValue._typeDescriptor());
    Option<ReturnConsumedCapacity> returnConsumedCapacity;
    returnConsumedCapacity =
      Objects.nonNull(nativeValue.returnConsumedCapacity())
        ? Option.create_Some(
          ReturnConsumedCapacity._typeDescriptor(),
          ToDafny.ReturnConsumedCapacity(nativeValue.returnConsumedCapacity())
        )
        : Option.create_None(ReturnConsumedCapacity._typeDescriptor());
    Option<ReturnItemCollectionMetrics> returnItemCollectionMetrics;
    returnItemCollectionMetrics =
      Objects.nonNull(nativeValue.returnItemCollectionMetrics())
        ? Option.create_Some(
          ReturnItemCollectionMetrics._typeDescriptor(),
          ToDafny.ReturnItemCollectionMetrics(
            nativeValue.returnItemCollectionMetrics()
          )
        )
        : Option.create_None(ReturnItemCollectionMetrics._typeDescriptor());
    Option<DafnySequence<? extends Character>> updateExpression;
    updateExpression =
      Objects.nonNull(nativeValue.updateExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.updateExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> conditionExpression;
    conditionExpression =
      Objects.nonNull(nativeValue.conditionExpression())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.conditionExpression()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends DafnySequence<? extends Character>
      >
    > expressionAttributeNames;
    expressionAttributeNames =
      (Objects.nonNull(nativeValue.expressionAttributeNames()) &&
          nativeValue.expressionAttributeNames().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          ),
          ToDafny.ExpressionAttributeNameMap(
            nativeValue.expressionAttributeNames()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
          )
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > expressionAttributeValues;
    expressionAttributeValues =
      (Objects.nonNull(nativeValue.expressionAttributeValues()) &&
          nativeValue.expressionAttributeValues().size() > 0)
        ? Option.create_Some(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          ),
          ToDafny.ExpressionAttributeValueMap(
            nativeValue.expressionAttributeValues()
          )
        )
        : Option.create_None(
          DafnyMap._typeDescriptor(
            DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
            AttributeValue._typeDescriptor()
          )
        );
    Option<
      ReturnValuesOnConditionCheckFailure
    > returnValuesOnConditionCheckFailure;
    returnValuesOnConditionCheckFailure =
      Objects.nonNull(nativeValue.returnValuesOnConditionCheckFailure())
        ? Option.create_Some(
          ReturnValuesOnConditionCheckFailure._typeDescriptor(),
          ToDafny.ReturnValuesOnConditionCheckFailure(
            nativeValue.returnValuesOnConditionCheckFailure()
          )
        )
        : Option.create_None(
          ReturnValuesOnConditionCheckFailure._typeDescriptor()
        );
    return new UpdateItemInput(
      tableName,
      key,
      attributeUpdates,
      expected,
      conditionalOperator,
      returnValues,
      returnConsumedCapacity,
      returnItemCollectionMetrics,
      updateExpression,
      conditionExpression,
      expressionAttributeNames,
      expressionAttributeValues,
      returnValuesOnConditionCheckFailure
    );
  }

  public static UpdateItemOutput UpdateItemOutput(
    UpdateItemResponse nativeValue
  ) {
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > attributes;
    attributes =
      (Objects.nonNull(nativeValue.attributes()) &&
          nativeValue.attributes().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.attributes())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    Option<ConsumedCapacity> consumedCapacity;
    consumedCapacity =
      Objects.nonNull(nativeValue.consumedCapacity())
        ? Option.create_Some(
          ConsumedCapacity._typeDescriptor(),
          ToDafny.ConsumedCapacity(nativeValue.consumedCapacity())
        )
        : Option.create_None(ConsumedCapacity._typeDescriptor());
    Option<ItemCollectionMetrics> itemCollectionMetrics;
    itemCollectionMetrics =
      Objects.nonNull(nativeValue.itemCollectionMetrics())
        ? Option.create_Some(
          ItemCollectionMetrics._typeDescriptor(),
          ToDafny.ItemCollectionMetrics(nativeValue.itemCollectionMetrics())
        )
        : Option.create_None(ItemCollectionMetrics._typeDescriptor());
    return new UpdateItemOutput(
      attributes,
      consumedCapacity,
      itemCollectionMetrics
    );
  }

  public static UpdateKinesisStreamingConfiguration UpdateKinesisStreamingConfiguration(
    software.amazon.awssdk.services.dynamodb.model.UpdateKinesisStreamingConfiguration nativeValue
  ) {
    Option<
      ApproximateCreationDateTimePrecision
    > approximateCreationDateTimePrecision;
    approximateCreationDateTimePrecision =
      Objects.nonNull(nativeValue.approximateCreationDateTimePrecision())
        ? Option.create_Some(
          ApproximateCreationDateTimePrecision._typeDescriptor(),
          ToDafny.ApproximateCreationDateTimePrecision(
            nativeValue.approximateCreationDateTimePrecision()
          )
        )
        : Option.create_None(
          ApproximateCreationDateTimePrecision._typeDescriptor()
        );
    return new UpdateKinesisStreamingConfiguration(
      approximateCreationDateTimePrecision
    );
  }

  public static UpdateKinesisStreamingDestinationInput UpdateKinesisStreamingDestinationInput(
    UpdateKinesisStreamingDestinationRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    DafnySequence<? extends Character> streamArn;
    streamArn =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.streamArn()
      );
    Option<
      UpdateKinesisStreamingConfiguration
    > updateKinesisStreamingConfiguration;
    updateKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.updateKinesisStreamingConfiguration())
        ? Option.create_Some(
          UpdateKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.UpdateKinesisStreamingConfiguration(
            nativeValue.updateKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          UpdateKinesisStreamingConfiguration._typeDescriptor()
        );
    return new UpdateKinesisStreamingDestinationInput(
      tableName,
      streamArn,
      updateKinesisStreamingConfiguration
    );
  }

  public static UpdateKinesisStreamingDestinationOutput UpdateKinesisStreamingDestinationOutput(
    UpdateKinesisStreamingDestinationResponse nativeValue
  ) {
    Option<DafnySequence<? extends Character>> tableName;
    tableName =
      Objects.nonNull(nativeValue.tableName())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.tableName()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends Character>> streamArn;
    streamArn =
      Objects.nonNull(nativeValue.streamArn())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.streamArn()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DestinationStatus> destinationStatus;
    destinationStatus =
      Objects.nonNull(nativeValue.destinationStatus())
        ? Option.create_Some(
          DestinationStatus._typeDescriptor(),
          ToDafny.DestinationStatus(nativeValue.destinationStatus())
        )
        : Option.create_None(DestinationStatus._typeDescriptor());
    Option<
      UpdateKinesisStreamingConfiguration
    > updateKinesisStreamingConfiguration;
    updateKinesisStreamingConfiguration =
      Objects.nonNull(nativeValue.updateKinesisStreamingConfiguration())
        ? Option.create_Some(
          UpdateKinesisStreamingConfiguration._typeDescriptor(),
          ToDafny.UpdateKinesisStreamingConfiguration(
            nativeValue.updateKinesisStreamingConfiguration()
          )
        )
        : Option.create_None(
          UpdateKinesisStreamingConfiguration._typeDescriptor()
        );
    return new UpdateKinesisStreamingDestinationOutput(
      tableName,
      streamArn,
      destinationStatus,
      updateKinesisStreamingConfiguration
    );
  }

  public static UpdateReplicationGroupMemberAction UpdateReplicationGroupMemberAction(
    software.amazon.awssdk.services.dynamodb.model.UpdateReplicationGroupMemberAction nativeValue
  ) {
    DafnySequence<? extends Character> regionName;
    regionName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.regionName()
      );
    Option<DafnySequence<? extends Character>> kMSMasterKeyId;
    kMSMasterKeyId =
      Objects.nonNull(nativeValue.kmsMasterKeyId())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.kmsMasterKeyId()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<ProvisionedThroughputOverride> provisionedThroughputOverride;
    provisionedThroughputOverride =
      Objects.nonNull(nativeValue.provisionedThroughputOverride())
        ? Option.create_Some(
          ProvisionedThroughputOverride._typeDescriptor(),
          ToDafny.ProvisionedThroughputOverride(
            nativeValue.provisionedThroughputOverride()
          )
        )
        : Option.create_None(ProvisionedThroughputOverride._typeDescriptor());
    Option<OnDemandThroughputOverride> onDemandThroughputOverride;
    onDemandThroughputOverride =
      Objects.nonNull(nativeValue.onDemandThroughputOverride())
        ? Option.create_Some(
          OnDemandThroughputOverride._typeDescriptor(),
          ToDafny.OnDemandThroughputOverride(
            nativeValue.onDemandThroughputOverride()
          )
        )
        : Option.create_None(OnDemandThroughputOverride._typeDescriptor());
    Option<
      DafnySequence<? extends ReplicaGlobalSecondaryIndex>
    > globalSecondaryIndexes;
    globalSecondaryIndexes =
      (Objects.nonNull(nativeValue.globalSecondaryIndexes()) &&
          nativeValue.globalSecondaryIndexes().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndex._typeDescriptor()
          ),
          ToDafny.ReplicaGlobalSecondaryIndexList(
            nativeValue.globalSecondaryIndexes()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaGlobalSecondaryIndex._typeDescriptor()
          )
        );
    Option<TableClass> tableClassOverride;
    tableClassOverride =
      Objects.nonNull(nativeValue.tableClassOverride())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.tableClassOverride())
        )
        : Option.create_None(TableClass._typeDescriptor());
    return new UpdateReplicationGroupMemberAction(
      regionName,
      kMSMasterKeyId,
      provisionedThroughputOverride,
      onDemandThroughputOverride,
      globalSecondaryIndexes,
      tableClassOverride
    );
  }

  public static UpdateTableInput UpdateTableInput(
    UpdateTableRequest nativeValue
  ) {
    Option<DafnySequence<? extends AttributeDefinition>> attributeDefinitions;
    attributeDefinitions =
      (Objects.nonNull(nativeValue.attributeDefinitions()) &&
          nativeValue.attributeDefinitions().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(AttributeDefinition._typeDescriptor()),
          ToDafny.AttributeDefinitions(nativeValue.attributeDefinitions())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(AttributeDefinition._typeDescriptor())
        );
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<BillingMode> billingMode;
    billingMode =
      Objects.nonNull(nativeValue.billingMode())
        ? Option.create_Some(
          BillingMode._typeDescriptor(),
          ToDafny.BillingMode(nativeValue.billingMode())
        )
        : Option.create_None(BillingMode._typeDescriptor());
    Option<ProvisionedThroughput> provisionedThroughput;
    provisionedThroughput =
      Objects.nonNull(nativeValue.provisionedThroughput())
        ? Option.create_Some(
          ProvisionedThroughput._typeDescriptor(),
          ToDafny.ProvisionedThroughput(nativeValue.provisionedThroughput())
        )
        : Option.create_None(ProvisionedThroughput._typeDescriptor());
    Option<
      DafnySequence<? extends GlobalSecondaryIndexUpdate>
    > globalSecondaryIndexUpdates;
    globalSecondaryIndexUpdates =
      (Objects.nonNull(nativeValue.globalSecondaryIndexUpdates()) &&
          nativeValue.globalSecondaryIndexUpdates().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexUpdate._typeDescriptor()
          ),
          ToDafny.GlobalSecondaryIndexUpdateList(
            nativeValue.globalSecondaryIndexUpdates()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexUpdate._typeDescriptor()
          )
        );
    Option<StreamSpecification> streamSpecification;
    streamSpecification =
      Objects.nonNull(nativeValue.streamSpecification())
        ? Option.create_Some(
          StreamSpecification._typeDescriptor(),
          ToDafny.StreamSpecification(nativeValue.streamSpecification())
        )
        : Option.create_None(StreamSpecification._typeDescriptor());
    Option<SSESpecification> sSESpecification;
    sSESpecification =
      Objects.nonNull(nativeValue.sseSpecification())
        ? Option.create_Some(
          SSESpecification._typeDescriptor(),
          ToDafny.SSESpecification(nativeValue.sseSpecification())
        )
        : Option.create_None(SSESpecification._typeDescriptor());
    Option<DafnySequence<? extends ReplicationGroupUpdate>> replicaUpdates;
    replicaUpdates =
      (Objects.nonNull(nativeValue.replicaUpdates()) &&
          nativeValue.replicaUpdates().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicationGroupUpdate._typeDescriptor()
          ),
          ToDafny.ReplicationGroupUpdateList(nativeValue.replicaUpdates())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicationGroupUpdate._typeDescriptor()
          )
        );
    Option<TableClass> tableClass;
    tableClass =
      Objects.nonNull(nativeValue.tableClass())
        ? Option.create_Some(
          TableClass._typeDescriptor(),
          ToDafny.TableClass(nativeValue.tableClass())
        )
        : Option.create_None(TableClass._typeDescriptor());
    Option<Boolean> deletionProtectionEnabled;
    deletionProtectionEnabled =
      Objects.nonNull(nativeValue.deletionProtectionEnabled())
        ? Option.create_Some(
          TypeDescriptor.BOOLEAN,
          (nativeValue.deletionProtectionEnabled())
        )
        : Option.create_None(TypeDescriptor.BOOLEAN);
    Option<OnDemandThroughput> onDemandThroughput;
    onDemandThroughput =
      Objects.nonNull(nativeValue.onDemandThroughput())
        ? Option.create_Some(
          OnDemandThroughput._typeDescriptor(),
          ToDafny.OnDemandThroughput(nativeValue.onDemandThroughput())
        )
        : Option.create_None(OnDemandThroughput._typeDescriptor());
    return new UpdateTableInput(
      attributeDefinitions,
      tableName,
      billingMode,
      provisionedThroughput,
      globalSecondaryIndexUpdates,
      streamSpecification,
      sSESpecification,
      replicaUpdates,
      tableClass,
      deletionProtectionEnabled,
      onDemandThroughput
    );
  }

  public static UpdateTableOutput UpdateTableOutput(
    UpdateTableResponse nativeValue
  ) {
    Option<TableDescription> tableDescription;
    tableDescription =
      Objects.nonNull(nativeValue.tableDescription())
        ? Option.create_Some(
          TableDescription._typeDescriptor(),
          ToDafny.TableDescription(nativeValue.tableDescription())
        )
        : Option.create_None(TableDescription._typeDescriptor());
    return new UpdateTableOutput(tableDescription);
  }

  public static UpdateTableReplicaAutoScalingInput UpdateTableReplicaAutoScalingInput(
    UpdateTableReplicaAutoScalingRequest nativeValue
  ) {
    Option<
      DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>
    > globalSecondaryIndexUpdates;
    globalSecondaryIndexUpdates =
      (Objects.nonNull(nativeValue.globalSecondaryIndexUpdates()) &&
          nativeValue.globalSecondaryIndexUpdates().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
          ),
          ToDafny.GlobalSecondaryIndexAutoScalingUpdateList(
            nativeValue.globalSecondaryIndexUpdates()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            GlobalSecondaryIndexAutoScalingUpdate._typeDescriptor()
          )
        );
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    Option<AutoScalingSettingsUpdate> provisionedWriteCapacityAutoScalingUpdate;
    provisionedWriteCapacityAutoScalingUpdate =
      Objects.nonNull(nativeValue.provisionedWriteCapacityAutoScalingUpdate())
        ? Option.create_Some(
          AutoScalingSettingsUpdate._typeDescriptor(),
          ToDafny.AutoScalingSettingsUpdate(
            nativeValue.provisionedWriteCapacityAutoScalingUpdate()
          )
        )
        : Option.create_None(AutoScalingSettingsUpdate._typeDescriptor());
    Option<DafnySequence<? extends ReplicaAutoScalingUpdate>> replicaUpdates;
    replicaUpdates =
      (Objects.nonNull(nativeValue.replicaUpdates()) &&
          nativeValue.replicaUpdates().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(
            ReplicaAutoScalingUpdate._typeDescriptor()
          ),
          ToDafny.ReplicaAutoScalingUpdateList(nativeValue.replicaUpdates())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(
            ReplicaAutoScalingUpdate._typeDescriptor()
          )
        );
    return new UpdateTableReplicaAutoScalingInput(
      globalSecondaryIndexUpdates,
      tableName,
      provisionedWriteCapacityAutoScalingUpdate,
      replicaUpdates
    );
  }

  public static UpdateTableReplicaAutoScalingOutput UpdateTableReplicaAutoScalingOutput(
    UpdateTableReplicaAutoScalingResponse nativeValue
  ) {
    Option<TableAutoScalingDescription> tableAutoScalingDescription;
    tableAutoScalingDescription =
      Objects.nonNull(nativeValue.tableAutoScalingDescription())
        ? Option.create_Some(
          TableAutoScalingDescription._typeDescriptor(),
          ToDafny.TableAutoScalingDescription(
            nativeValue.tableAutoScalingDescription()
          )
        )
        : Option.create_None(TableAutoScalingDescription._typeDescriptor());
    return new UpdateTableReplicaAutoScalingOutput(tableAutoScalingDescription);
  }

  public static UpdateTimeToLiveInput UpdateTimeToLiveInput(
    UpdateTimeToLiveRequest nativeValue
  ) {
    DafnySequence<? extends Character> tableName;
    tableName =
      software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
        nativeValue.tableName()
      );
    TimeToLiveSpecification timeToLiveSpecification;
    timeToLiveSpecification =
      ToDafny.TimeToLiveSpecification(nativeValue.timeToLiveSpecification());
    return new UpdateTimeToLiveInput(tableName, timeToLiveSpecification);
  }

  public static UpdateTimeToLiveOutput UpdateTimeToLiveOutput(
    UpdateTimeToLiveResponse nativeValue
  ) {
    Option<TimeToLiveSpecification> timeToLiveSpecification;
    timeToLiveSpecification =
      Objects.nonNull(nativeValue.timeToLiveSpecification())
        ? Option.create_Some(
          TimeToLiveSpecification._typeDescriptor(),
          ToDafny.TimeToLiveSpecification(nativeValue.timeToLiveSpecification())
        )
        : Option.create_None(TimeToLiveSpecification._typeDescriptor());
    return new UpdateTimeToLiveOutput(timeToLiveSpecification);
  }

  public static WriteRequest WriteRequest(
    software.amazon.awssdk.services.dynamodb.model.WriteRequest nativeValue
  ) {
    Option<PutRequest> putRequest;
    putRequest =
      Objects.nonNull(nativeValue.putRequest())
        ? Option.create_Some(
          PutRequest._typeDescriptor(),
          ToDafny.PutRequest(nativeValue.putRequest())
        )
        : Option.create_None(PutRequest._typeDescriptor());
    Option<DeleteRequest> deleteRequest;
    deleteRequest =
      Objects.nonNull(nativeValue.deleteRequest())
        ? Option.create_Some(
          DeleteRequest._typeDescriptor(),
          ToDafny.DeleteRequest(nativeValue.deleteRequest())
        )
        : Option.create_None(DeleteRequest._typeDescriptor());
    return new WriteRequest(putRequest, deleteRequest);
  }

  public static DafnySequence<? extends WriteRequest> WriteRequests(
    List<
      software.amazon.awssdk.services.dynamodb.model.WriteRequest
    > nativeValue
  ) {
    return software.amazon.smithy.dafny.conversion.ToDafny.Aggregate.GenericToSequence(
      nativeValue,
      software.amazon.cryptography.services.dynamodb.internaldafny.ToDafny::WriteRequest,
      WriteRequest._typeDescriptor()
    );
  }

  public static Error Error(BackupInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_BackupInUseException(message);
  }

  public static Error Error(BackupNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_BackupNotFoundException(message);
  }

  public static Error Error(ConditionalCheckFailedException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<
      DafnyMap<
        ? extends DafnySequence<? extends Character>,
        ? extends AttributeValue
      >
    > item;
    item =
      (Objects.nonNull(nativeValue.item()) && nativeValue.item().size() > 0)
        ? Option.create_Some(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          ),
          ToDafny.AttributeMap(nativeValue.item())
        )
        : Option.create_None(
          TypeDescriptor.referenceWithInitializer(
            dafny.DafnyMap.class,
            () ->
              dafny.DafnyMap.<
                dafny.DafnySequence<? extends Character>,
                AttributeValue
              >empty()
          )
        );
    return new Error_ConditionalCheckFailedException(message, item);
  }

  public static Error Error(ContinuousBackupsUnavailableException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ContinuousBackupsUnavailableException(message);
  }

  public static Error Error(DuplicateItemException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_DuplicateItemException(message);
  }

  public static Error Error(ExportConflictException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ExportConflictException(message);
  }

  public static Error Error(ExportNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ExportNotFoundException(message);
  }

  public static Error Error(GlobalTableAlreadyExistsException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_GlobalTableAlreadyExistsException(message);
  }

  public static Error Error(GlobalTableNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_GlobalTableNotFoundException(message);
  }

  public static Error Error(IdempotentParameterMismatchException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_IdempotentParameterMismatchException(message);
  }

  public static Error Error(ImportConflictException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ImportConflictException(message);
  }

  public static Error Error(ImportNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ImportNotFoundException(message);
  }

  public static Error Error(IndexNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_IndexNotFoundException(message);
  }

  public static Error Error(InternalServerErrorException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_InternalServerError(message);
  }

  public static Error Error(InvalidExportTimeException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_InvalidExportTimeException(message);
  }

  public static Error Error(InvalidRestoreTimeException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_InvalidRestoreTimeException(message);
  }

  public static Error Error(
    ItemCollectionSizeLimitExceededException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ItemCollectionSizeLimitExceededException(message);
  }

  public static Error Error(LimitExceededException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_LimitExceededException(message);
  }

  public static Error Error(
    PointInTimeRecoveryUnavailableException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_PointInTimeRecoveryUnavailableException(message);
  }

  public static Error Error(PolicyNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_PolicyNotFoundException(message);
  }

  public static Error Error(
    ProvisionedThroughputExceededException nativeValue
  ) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ProvisionedThroughputExceededException(message);
  }

  public static Error Error(ReplicaAlreadyExistsException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ReplicaAlreadyExistsException(message);
  }

  public static Error Error(ReplicaNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ReplicaNotFoundException(message);
  }

  public static Error Error(RequestLimitExceededException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_RequestLimitExceeded(message);
  }

  public static Error Error(ResourceInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ResourceInUseException(message);
  }

  public static Error Error(ResourceNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_ResourceNotFoundException(message);
  }

  public static Error Error(TableAlreadyExistsException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_TableAlreadyExistsException(message);
  }

  public static Error Error(TableInUseException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_TableInUseException(message);
  }

  public static Error Error(TableNotFoundException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_TableNotFoundException(message);
  }

  public static Error Error(TransactionCanceledException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    Option<DafnySequence<? extends CancellationReason>> cancellationReasons;
    cancellationReasons =
      (Objects.nonNull(nativeValue.cancellationReasons()) &&
          nativeValue.cancellationReasons().size() > 0)
        ? Option.create_Some(
          DafnySequence._typeDescriptor(CancellationReason._typeDescriptor()),
          ToDafny.CancellationReasonList(nativeValue.cancellationReasons())
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(CancellationReason._typeDescriptor())
        );
    return new Error_TransactionCanceledException(message, cancellationReasons);
  }

  public static Error Error(TransactionConflictException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_TransactionConflictException(message);
  }

  public static Error Error(TransactionInProgressException nativeValue) {
    Option<DafnySequence<? extends Character>> message;
    message =
      Objects.nonNull(nativeValue.getMessage())
        ? Option.create_Some(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR),
          software.amazon.smithy.dafny.conversion.ToDafny.Simple.CharacterSequence(
            nativeValue.getMessage()
          )
        )
        : Option.create_None(
          DafnySequence._typeDescriptor(TypeDescriptor.CHAR)
        );
    return new Error_TransactionInProgressException(message);
  }

  public static ApproximateCreationDateTimePrecision ApproximateCreationDateTimePrecision(
    software.amazon.awssdk.services.dynamodb.model.ApproximateCreationDateTimePrecision nativeValue
  ) {
    switch (nativeValue) {
      case MILLISECOND:
        {
          return ApproximateCreationDateTimePrecision.create_MILLISECOND();
        }
      case MICROSECOND:
        {
          return ApproximateCreationDateTimePrecision.create_MICROSECOND();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ApproximateCreationDateTimePrecision."
          );
        }
    }
  }

  public static AttributeAction AttributeAction(
    software.amazon.awssdk.services.dynamodb.model.AttributeAction nativeValue
  ) {
    switch (nativeValue) {
      case ADD:
        {
          return AttributeAction.create_ADD();
        }
      case PUT:
        {
          return AttributeAction.create_PUT();
        }
      case DELETE:
        {
          return AttributeAction.create_DELETE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeAction."
          );
        }
    }
  }

  public static BackupStatus BackupStatus(
    software.amazon.awssdk.services.dynamodb.model.BackupStatus nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return BackupStatus.create_CREATING();
        }
      case DELETED:
        {
          return BackupStatus.create_DELETED();
        }
      case AVAILABLE:
        {
          return BackupStatus.create_AVAILABLE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupStatus."
          );
        }
    }
  }

  public static BackupType BackupType(
    software.amazon.awssdk.services.dynamodb.model.BackupType nativeValue
  ) {
    switch (nativeValue) {
      case USER:
        {
          return BackupType.create_USER();
        }
      case SYSTEM:
        {
          return BackupType.create_SYSTEM();
        }
      case AWS_BACKUP:
        {
          return BackupType.create_AWS__BACKUP();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupType."
          );
        }
    }
  }

  public static BackupTypeFilter BackupTypeFilter(
    software.amazon.awssdk.services.dynamodb.model.BackupTypeFilter nativeValue
  ) {
    switch (nativeValue) {
      case USER:
        {
          return BackupTypeFilter.create_USER();
        }
      case SYSTEM:
        {
          return BackupTypeFilter.create_SYSTEM();
        }
      case AWS_BACKUP:
        {
          return BackupTypeFilter.create_AWS__BACKUP();
        }
      case ALL:
        {
          return BackupTypeFilter.create_ALL();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupTypeFilter."
          );
        }
    }
  }

  public static BatchStatementErrorCodeEnum BatchStatementErrorCodeEnum(
    software.amazon.awssdk.services.dynamodb.model.BatchStatementErrorCodeEnum nativeValue
  ) {
    switch (nativeValue) {
      case CONDITIONAL_CHECK_FAILED:
        {
          return BatchStatementErrorCodeEnum.create_ConditionalCheckFailed();
        }
      case ITEM_COLLECTION_SIZE_LIMIT_EXCEEDED:
        {
          return BatchStatementErrorCodeEnum.create_ItemCollectionSizeLimitExceeded();
        }
      case REQUEST_LIMIT_EXCEEDED:
        {
          return BatchStatementErrorCodeEnum.create_RequestLimitExceeded();
        }
      case VALIDATION_ERROR:
        {
          return BatchStatementErrorCodeEnum.create_ValidationError();
        }
      case PROVISIONED_THROUGHPUT_EXCEEDED:
        {
          return BatchStatementErrorCodeEnum.create_ProvisionedThroughputExceeded();
        }
      case TRANSACTION_CONFLICT:
        {
          return BatchStatementErrorCodeEnum.create_TransactionConflict();
        }
      case THROTTLING_ERROR:
        {
          return BatchStatementErrorCodeEnum.create_ThrottlingError();
        }
      case INTERNAL_SERVER_ERROR:
        {
          return BatchStatementErrorCodeEnum.create_InternalServerError();
        }
      case RESOURCE_NOT_FOUND:
        {
          return BatchStatementErrorCodeEnum.create_ResourceNotFound();
        }
      case ACCESS_DENIED:
        {
          return BatchStatementErrorCodeEnum.create_AccessDenied();
        }
      case DUPLICATE_ITEM:
        {
          return BatchStatementErrorCodeEnum.create_DuplicateItem();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.BatchStatementErrorCodeEnum."
          );
        }
    }
  }

  public static BillingMode BillingMode(
    software.amazon.awssdk.services.dynamodb.model.BillingMode nativeValue
  ) {
    switch (nativeValue) {
      case PROVISIONED:
        {
          return BillingMode.create_PROVISIONED();
        }
      case PAY_PER_REQUEST:
        {
          return BillingMode.create_PAY__PER__REQUEST();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.BillingMode."
          );
        }
    }
  }

  public static ComparisonOperator ComparisonOperator(
    software.amazon.awssdk.services.dynamodb.model.ComparisonOperator nativeValue
  ) {
    switch (nativeValue) {
      case EQ:
        {
          return ComparisonOperator.create_EQ();
        }
      case NE:
        {
          return ComparisonOperator.create_NE();
        }
      case IN:
        {
          return ComparisonOperator.create_IN();
        }
      case LE:
        {
          return ComparisonOperator.create_LE();
        }
      case LT:
        {
          return ComparisonOperator.create_LT();
        }
      case GE:
        {
          return ComparisonOperator.create_GE();
        }
      case GT:
        {
          return ComparisonOperator.create_GT();
        }
      case BETWEEN:
        {
          return ComparisonOperator.create_BETWEEN();
        }
      case NOT_NULL:
        {
          return ComparisonOperator.create_NOT__NULL();
        }
      case NULL:
        {
          return ComparisonOperator.create_NULL();
        }
      case CONTAINS:
        {
          return ComparisonOperator.create_CONTAINS();
        }
      case NOT_CONTAINS:
        {
          return ComparisonOperator.create_NOT__CONTAINS();
        }
      case BEGINS_WITH:
        {
          return ComparisonOperator.create_BEGINS__WITH();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ComparisonOperator."
          );
        }
    }
  }

  public static ConditionalOperator ConditionalOperator(
    software.amazon.awssdk.services.dynamodb.model.ConditionalOperator nativeValue
  ) {
    switch (nativeValue) {
      case AND:
        {
          return ConditionalOperator.create_AND();
        }
      case OR:
        {
          return ConditionalOperator.create_OR();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ConditionalOperator."
          );
        }
    }
  }

  public static ContinuousBackupsStatus ContinuousBackupsStatus(
    software.amazon.awssdk.services.dynamodb.model.ContinuousBackupsStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLED:
        {
          return ContinuousBackupsStatus.create_ENABLED();
        }
      case DISABLED:
        {
          return ContinuousBackupsStatus.create_DISABLED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ContinuousBackupsStatus."
          );
        }
    }
  }

  public static ContributorInsightsAction ContributorInsightsAction(
    software.amazon.awssdk.services.dynamodb.model.ContributorInsightsAction nativeValue
  ) {
    switch (nativeValue) {
      case ENABLE:
        {
          return ContributorInsightsAction.create_ENABLE();
        }
      case DISABLE:
        {
          return ContributorInsightsAction.create_DISABLE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsAction."
          );
        }
    }
  }

  public static ContributorInsightsStatus ContributorInsightsStatus(
    software.amazon.awssdk.services.dynamodb.model.ContributorInsightsStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLING:
        {
          return ContributorInsightsStatus.create_ENABLING();
        }
      case ENABLED:
        {
          return ContributorInsightsStatus.create_ENABLED();
        }
      case DISABLING:
        {
          return ContributorInsightsStatus.create_DISABLING();
        }
      case DISABLED:
        {
          return ContributorInsightsStatus.create_DISABLED();
        }
      case FAILED:
        {
          return ContributorInsightsStatus.create_FAILED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ContributorInsightsStatus."
          );
        }
    }
  }

  public static DestinationStatus DestinationStatus(
    software.amazon.awssdk.services.dynamodb.model.DestinationStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLING:
        {
          return DestinationStatus.create_ENABLING();
        }
      case ACTIVE:
        {
          return DestinationStatus.create_ACTIVE();
        }
      case DISABLING:
        {
          return DestinationStatus.create_DISABLING();
        }
      case DISABLED:
        {
          return DestinationStatus.create_DISABLED();
        }
      case ENABLE_FAILED:
        {
          return DestinationStatus.create_ENABLE__FAILED();
        }
      case UPDATING:
        {
          return DestinationStatus.create_UPDATING();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.DestinationStatus."
          );
        }
    }
  }

  public static ExportFormat ExportFormat(
    software.amazon.awssdk.services.dynamodb.model.ExportFormat nativeValue
  ) {
    switch (nativeValue) {
      case DYNAMODB_JSON:
        {
          return ExportFormat.create_DYNAMODB__JSON();
        }
      case ION:
        {
          return ExportFormat.create_ION();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportFormat."
          );
        }
    }
  }

  public static ExportStatus ExportStatus(
    software.amazon.awssdk.services.dynamodb.model.ExportStatus nativeValue
  ) {
    switch (nativeValue) {
      case IN_PROGRESS:
        {
          return ExportStatus.create_IN__PROGRESS();
        }
      case COMPLETED:
        {
          return ExportStatus.create_COMPLETED();
        }
      case FAILED:
        {
          return ExportStatus.create_FAILED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportStatus."
          );
        }
    }
  }

  public static ExportType ExportType(
    software.amazon.awssdk.services.dynamodb.model.ExportType nativeValue
  ) {
    switch (nativeValue) {
      case FULL_EXPORT:
        {
          return ExportType.create_FULL__EXPORT();
        }
      case INCREMENTAL_EXPORT:
        {
          return ExportType.create_INCREMENTAL__EXPORT();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportType."
          );
        }
    }
  }

  public static ExportViewType ExportViewType(
    software.amazon.awssdk.services.dynamodb.model.ExportViewType nativeValue
  ) {
    switch (nativeValue) {
      case NEW_IMAGE:
        {
          return ExportViewType.create_NEW__IMAGE();
        }
      case NEW_AND_OLD_IMAGES:
        {
          return ExportViewType.create_NEW__AND__OLD__IMAGES();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportViewType."
          );
        }
    }
  }

  public static GlobalTableStatus GlobalTableStatus(
    software.amazon.awssdk.services.dynamodb.model.GlobalTableStatus nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return GlobalTableStatus.create_CREATING();
        }
      case ACTIVE:
        {
          return GlobalTableStatus.create_ACTIVE();
        }
      case DELETING:
        {
          return GlobalTableStatus.create_DELETING();
        }
      case UPDATING:
        {
          return GlobalTableStatus.create_UPDATING();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableStatus."
          );
        }
    }
  }

  public static ImportStatus ImportStatus(
    software.amazon.awssdk.services.dynamodb.model.ImportStatus nativeValue
  ) {
    switch (nativeValue) {
      case IN_PROGRESS:
        {
          return ImportStatus.create_IN__PROGRESS();
        }
      case COMPLETED:
        {
          return ImportStatus.create_COMPLETED();
        }
      case CANCELLING:
        {
          return ImportStatus.create_CANCELLING();
        }
      case CANCELLED:
        {
          return ImportStatus.create_CANCELLED();
        }
      case FAILED:
        {
          return ImportStatus.create_FAILED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ImportStatus."
          );
        }
    }
  }

  public static IndexStatus IndexStatus(
    software.amazon.awssdk.services.dynamodb.model.IndexStatus nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return IndexStatus.create_CREATING();
        }
      case UPDATING:
        {
          return IndexStatus.create_UPDATING();
        }
      case DELETING:
        {
          return IndexStatus.create_DELETING();
        }
      case ACTIVE:
        {
          return IndexStatus.create_ACTIVE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.IndexStatus."
          );
        }
    }
  }

  public static InputCompressionType InputCompressionType(
    software.amazon.awssdk.services.dynamodb.model.InputCompressionType nativeValue
  ) {
    switch (nativeValue) {
      case GZIP:
        {
          return InputCompressionType.create_GZIP();
        }
      case ZSTD:
        {
          return InputCompressionType.create_ZSTD();
        }
      case NONE:
        {
          return InputCompressionType.create_NONE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.InputCompressionType."
          );
        }
    }
  }

  public static InputFormat InputFormat(
    software.amazon.awssdk.services.dynamodb.model.InputFormat nativeValue
  ) {
    switch (nativeValue) {
      case DYNAMODB_JSON:
        {
          return InputFormat.create_DYNAMODB__JSON();
        }
      case ION:
        {
          return InputFormat.create_ION();
        }
      case CSV:
        {
          return InputFormat.create_CSV();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.InputFormat."
          );
        }
    }
  }

  public static KeyType KeyType(
    software.amazon.awssdk.services.dynamodb.model.KeyType nativeValue
  ) {
    switch (nativeValue) {
      case HASH:
        {
          return KeyType.create_HASH();
        }
      case RANGE:
        {
          return KeyType.create_RANGE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.KeyType."
          );
        }
    }
  }

  public static PointInTimeRecoveryStatus PointInTimeRecoveryStatus(
    software.amazon.awssdk.services.dynamodb.model.PointInTimeRecoveryStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLED:
        {
          return PointInTimeRecoveryStatus.create_ENABLED();
        }
      case DISABLED:
        {
          return PointInTimeRecoveryStatus.create_DISABLED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.PointInTimeRecoveryStatus."
          );
        }
    }
  }

  public static ProjectionType ProjectionType(
    software.amazon.awssdk.services.dynamodb.model.ProjectionType nativeValue
  ) {
    switch (nativeValue) {
      case ALL:
        {
          return ProjectionType.create_ALL();
        }
      case KEYS_ONLY:
        {
          return ProjectionType.create_KEYS__ONLY();
        }
      case INCLUDE:
        {
          return ProjectionType.create_INCLUDE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ProjectionType."
          );
        }
    }
  }

  public static ReplicaStatus ReplicaStatus(
    software.amazon.awssdk.services.dynamodb.model.ReplicaStatus nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return ReplicaStatus.create_CREATING();
        }
      case CREATION_FAILED:
        {
          return ReplicaStatus.create_CREATION__FAILED();
        }
      case UPDATING:
        {
          return ReplicaStatus.create_UPDATING();
        }
      case DELETING:
        {
          return ReplicaStatus.create_DELETING();
        }
      case ACTIVE:
        {
          return ReplicaStatus.create_ACTIVE();
        }
      case REGION_DISABLED:
        {
          return ReplicaStatus.create_REGION__DISABLED();
        }
      case INACCESSIBLE_ENCRYPTION_CREDENTIALS:
        {
          return ReplicaStatus.create_INACCESSIBLE__ENCRYPTION__CREDENTIALS();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaStatus."
          );
        }
    }
  }

  public static ReturnConsumedCapacity ReturnConsumedCapacity(
    software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity nativeValue
  ) {
    switch (nativeValue) {
      case INDEXES:
        {
          return ReturnConsumedCapacity.create_INDEXES();
        }
      case TOTAL:
        {
          return ReturnConsumedCapacity.create_TOTAL();
        }
      case NONE:
        {
          return ReturnConsumedCapacity.create_NONE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnConsumedCapacity."
          );
        }
    }
  }

  public static ReturnItemCollectionMetrics ReturnItemCollectionMetrics(
    software.amazon.awssdk.services.dynamodb.model.ReturnItemCollectionMetrics nativeValue
  ) {
    switch (nativeValue) {
      case SIZE:
        {
          return ReturnItemCollectionMetrics.create_SIZE();
        }
      case NONE:
        {
          return ReturnItemCollectionMetrics.create_NONE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnItemCollectionMetrics."
          );
        }
    }
  }

  public static ReturnValue ReturnValue(
    software.amazon.awssdk.services.dynamodb.model.ReturnValue nativeValue
  ) {
    switch (nativeValue) {
      case NONE:
        {
          return ReturnValue.create_NONE();
        }
      case ALL_OLD:
        {
          return ReturnValue.create_ALL__OLD();
        }
      case UPDATED_OLD:
        {
          return ReturnValue.create_UPDATED__OLD();
        }
      case ALL_NEW:
        {
          return ReturnValue.create_ALL__NEW();
        }
      case UPDATED_NEW:
        {
          return ReturnValue.create_UPDATED__NEW();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValue."
          );
        }
    }
  }

  public static ReturnValuesOnConditionCheckFailure ReturnValuesOnConditionCheckFailure(
    software.amazon.awssdk.services.dynamodb.model.ReturnValuesOnConditionCheckFailure nativeValue
  ) {
    switch (nativeValue) {
      case ALL_OLD:
        {
          return ReturnValuesOnConditionCheckFailure.create_ALL__OLD();
        }
      case NONE:
        {
          return ReturnValuesOnConditionCheckFailure.create_NONE();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValuesOnConditionCheckFailure."
          );
        }
    }
  }

  public static S3SseAlgorithm S3SseAlgorithm(
    software.amazon.awssdk.services.dynamodb.model.S3SseAlgorithm nativeValue
  ) {
    switch (nativeValue) {
      case AES256:
        {
          return S3SseAlgorithm.create_AES256();
        }
      case KMS:
        {
          return S3SseAlgorithm.create_KMS();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.S3SseAlgorithm."
          );
        }
    }
  }

  public static ScalarAttributeType ScalarAttributeType(
    software.amazon.awssdk.services.dynamodb.model.ScalarAttributeType nativeValue
  ) {
    switch (nativeValue) {
      case S:
        {
          return ScalarAttributeType.create_S();
        }
      case N:
        {
          return ScalarAttributeType.create_N();
        }
      case B:
        {
          return ScalarAttributeType.create_B();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.ScalarAttributeType."
          );
        }
    }
  }

  public static Select Select(
    software.amazon.awssdk.services.dynamodb.model.Select nativeValue
  ) {
    switch (nativeValue) {
      case ALL_ATTRIBUTES:
        {
          return Select.create_ALL__ATTRIBUTES();
        }
      case ALL_PROJECTED_ATTRIBUTES:
        {
          return Select.create_ALL__PROJECTED__ATTRIBUTES();
        }
      case SPECIFIC_ATTRIBUTES:
        {
          return Select.create_SPECIFIC__ATTRIBUTES();
        }
      case COUNT:
        {
          return Select.create_COUNT();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.Select."
          );
        }
    }
  }

  public static SSEStatus SSEStatus(
    software.amazon.awssdk.services.dynamodb.model.SSEStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLING:
        {
          return SSEStatus.create_ENABLING();
        }
      case ENABLED:
        {
          return SSEStatus.create_ENABLED();
        }
      case DISABLING:
        {
          return SSEStatus.create_DISABLING();
        }
      case DISABLED:
        {
          return SSEStatus.create_DISABLED();
        }
      case UPDATING:
        {
          return SSEStatus.create_UPDATING();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEStatus."
          );
        }
    }
  }

  public static SSEType SSEType(
    software.amazon.awssdk.services.dynamodb.model.SSEType nativeValue
  ) {
    switch (nativeValue) {
      case AES256:
        {
          return SSEType.create_AES256();
        }
      case KMS:
        {
          return SSEType.create_KMS();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEType."
          );
        }
    }
  }

  public static StreamViewType StreamViewType(
    software.amazon.awssdk.services.dynamodb.model.StreamViewType nativeValue
  ) {
    switch (nativeValue) {
      case NEW_IMAGE:
        {
          return StreamViewType.create_NEW__IMAGE();
        }
      case OLD_IMAGE:
        {
          return StreamViewType.create_OLD__IMAGE();
        }
      case NEW_AND_OLD_IMAGES:
        {
          return StreamViewType.create_NEW__AND__OLD__IMAGES();
        }
      case KEYS_ONLY:
        {
          return StreamViewType.create_KEYS__ONLY();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.StreamViewType."
          );
        }
    }
  }

  public static TableClass TableClass(
    software.amazon.awssdk.services.dynamodb.model.TableClass nativeValue
  ) {
    switch (nativeValue) {
      case STANDARD:
        {
          return TableClass.create_STANDARD();
        }
      case STANDARD_INFREQUENT_ACCESS:
        {
          return TableClass.create_STANDARD__INFREQUENT__ACCESS();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClass."
          );
        }
    }
  }

  public static TableStatus TableStatus(
    software.amazon.awssdk.services.dynamodb.model.TableStatus nativeValue
  ) {
    switch (nativeValue) {
      case CREATING:
        {
          return TableStatus.create_CREATING();
        }
      case UPDATING:
        {
          return TableStatus.create_UPDATING();
        }
      case DELETING:
        {
          return TableStatus.create_DELETING();
        }
      case ACTIVE:
        {
          return TableStatus.create_ACTIVE();
        }
      case INACCESSIBLE_ENCRYPTION_CREDENTIALS:
        {
          return TableStatus.create_INACCESSIBLE__ENCRYPTION__CREDENTIALS();
        }
      case ARCHIVING:
        {
          return TableStatus.create_ARCHIVING();
        }
      case ARCHIVED:
        {
          return TableStatus.create_ARCHIVED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.TableStatus."
          );
        }
    }
  }

  public static TimeToLiveStatus TimeToLiveStatus(
    software.amazon.awssdk.services.dynamodb.model.TimeToLiveStatus nativeValue
  ) {
    switch (nativeValue) {
      case ENABLING:
        {
          return TimeToLiveStatus.create_ENABLING();
        }
      case DISABLING:
        {
          return TimeToLiveStatus.create_DISABLING();
        }
      case ENABLED:
        {
          return TimeToLiveStatus.create_ENABLED();
        }
      case DISABLED:
        {
          return TimeToLiveStatus.create_DISABLED();
        }
      default:
        {
          throw new RuntimeException(
            "Cannot convert " +
            nativeValue +
            " to software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveStatus."
          );
        }
    }
  }

  public static ApproximateCreationDateTimePrecision ApproximateCreationDateTimePrecision(
    String nativeValue
  ) {
    return ApproximateCreationDateTimePrecision(
      software.amazon.awssdk.services.dynamodb.model.ApproximateCreationDateTimePrecision.fromValue(
        nativeValue
      )
    );
  }

  public static AttributeAction AttributeAction(String nativeValue) {
    return AttributeAction(
      software.amazon.awssdk.services.dynamodb.model.AttributeAction.fromValue(
        nativeValue
      )
    );
  }

  public static BackupStatus BackupStatus(String nativeValue) {
    return BackupStatus(
      software.amazon.awssdk.services.dynamodb.model.BackupStatus.fromValue(
        nativeValue
      )
    );
  }

  public static BackupType BackupType(String nativeValue) {
    return BackupType(
      software.amazon.awssdk.services.dynamodb.model.BackupType.fromValue(
        nativeValue
      )
    );
  }

  public static BackupTypeFilter BackupTypeFilter(String nativeValue) {
    return BackupTypeFilter(
      software.amazon.awssdk.services.dynamodb.model.BackupTypeFilter.fromValue(
        nativeValue
      )
    );
  }

  public static BatchStatementErrorCodeEnum BatchStatementErrorCodeEnum(
    String nativeValue
  ) {
    return BatchStatementErrorCodeEnum(
      software.amazon.awssdk.services.dynamodb.model.BatchStatementErrorCodeEnum.fromValue(
        nativeValue
      )
    );
  }

  public static BillingMode BillingMode(String nativeValue) {
    return BillingMode(
      software.amazon.awssdk.services.dynamodb.model.BillingMode.fromValue(
        nativeValue
      )
    );
  }

  public static ComparisonOperator ComparisonOperator(String nativeValue) {
    return ComparisonOperator(
      software.amazon.awssdk.services.dynamodb.model.ComparisonOperator.fromValue(
        nativeValue
      )
    );
  }

  public static ConditionalOperator ConditionalOperator(String nativeValue) {
    return ConditionalOperator(
      software.amazon.awssdk.services.dynamodb.model.ConditionalOperator.fromValue(
        nativeValue
      )
    );
  }

  public static ContinuousBackupsStatus ContinuousBackupsStatus(
    String nativeValue
  ) {
    return ContinuousBackupsStatus(
      software.amazon.awssdk.services.dynamodb.model.ContinuousBackupsStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ContributorInsightsAction ContributorInsightsAction(
    String nativeValue
  ) {
    return ContributorInsightsAction(
      software.amazon.awssdk.services.dynamodb.model.ContributorInsightsAction.fromValue(
        nativeValue
      )
    );
  }

  public static ContributorInsightsStatus ContributorInsightsStatus(
    String nativeValue
  ) {
    return ContributorInsightsStatus(
      software.amazon.awssdk.services.dynamodb.model.ContributorInsightsStatus.fromValue(
        nativeValue
      )
    );
  }

  public static DestinationStatus DestinationStatus(String nativeValue) {
    return DestinationStatus(
      software.amazon.awssdk.services.dynamodb.model.DestinationStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ExportFormat ExportFormat(String nativeValue) {
    return ExportFormat(
      software.amazon.awssdk.services.dynamodb.model.ExportFormat.fromValue(
        nativeValue
      )
    );
  }

  public static ExportStatus ExportStatus(String nativeValue) {
    return ExportStatus(
      software.amazon.awssdk.services.dynamodb.model.ExportStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ExportType ExportType(String nativeValue) {
    return ExportType(
      software.amazon.awssdk.services.dynamodb.model.ExportType.fromValue(
        nativeValue
      )
    );
  }

  public static ExportViewType ExportViewType(String nativeValue) {
    return ExportViewType(
      software.amazon.awssdk.services.dynamodb.model.ExportViewType.fromValue(
        nativeValue
      )
    );
  }

  public static GlobalTableStatus GlobalTableStatus(String nativeValue) {
    return GlobalTableStatus(
      software.amazon.awssdk.services.dynamodb.model.GlobalTableStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ImportStatus ImportStatus(String nativeValue) {
    return ImportStatus(
      software.amazon.awssdk.services.dynamodb.model.ImportStatus.fromValue(
        nativeValue
      )
    );
  }

  public static IndexStatus IndexStatus(String nativeValue) {
    return IndexStatus(
      software.amazon.awssdk.services.dynamodb.model.IndexStatus.fromValue(
        nativeValue
      )
    );
  }

  public static InputCompressionType InputCompressionType(String nativeValue) {
    return InputCompressionType(
      software.amazon.awssdk.services.dynamodb.model.InputCompressionType.fromValue(
        nativeValue
      )
    );
  }

  public static InputFormat InputFormat(String nativeValue) {
    return InputFormat(
      software.amazon.awssdk.services.dynamodb.model.InputFormat.fromValue(
        nativeValue
      )
    );
  }

  public static KeyType KeyType(String nativeValue) {
    return KeyType(
      software.amazon.awssdk.services.dynamodb.model.KeyType.fromValue(
        nativeValue
      )
    );
  }

  public static PointInTimeRecoveryStatus PointInTimeRecoveryStatus(
    String nativeValue
  ) {
    return PointInTimeRecoveryStatus(
      software.amazon.awssdk.services.dynamodb.model.PointInTimeRecoveryStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ProjectionType ProjectionType(String nativeValue) {
    return ProjectionType(
      software.amazon.awssdk.services.dynamodb.model.ProjectionType.fromValue(
        nativeValue
      )
    );
  }

  public static ReplicaStatus ReplicaStatus(String nativeValue) {
    return ReplicaStatus(
      software.amazon.awssdk.services.dynamodb.model.ReplicaStatus.fromValue(
        nativeValue
      )
    );
  }

  public static ReturnConsumedCapacity ReturnConsumedCapacity(
    String nativeValue
  ) {
    return ReturnConsumedCapacity(
      software.amazon.awssdk.services.dynamodb.model.ReturnConsumedCapacity.fromValue(
        nativeValue
      )
    );
  }

  public static ReturnItemCollectionMetrics ReturnItemCollectionMetrics(
    String nativeValue
  ) {
    return ReturnItemCollectionMetrics(
      software.amazon.awssdk.services.dynamodb.model.ReturnItemCollectionMetrics.fromValue(
        nativeValue
      )
    );
  }

  public static ReturnValue ReturnValue(String nativeValue) {
    return ReturnValue(
      software.amazon.awssdk.services.dynamodb.model.ReturnValue.fromValue(
        nativeValue
      )
    );
  }

  public static ReturnValuesOnConditionCheckFailure ReturnValuesOnConditionCheckFailure(
    String nativeValue
  ) {
    return ReturnValuesOnConditionCheckFailure(
      software.amazon.awssdk.services.dynamodb.model.ReturnValuesOnConditionCheckFailure.fromValue(
        nativeValue
      )
    );
  }

  public static S3SseAlgorithm S3SseAlgorithm(String nativeValue) {
    return S3SseAlgorithm(
      software.amazon.awssdk.services.dynamodb.model.S3SseAlgorithm.fromValue(
        nativeValue
      )
    );
  }

  public static ScalarAttributeType ScalarAttributeType(String nativeValue) {
    return ScalarAttributeType(
      software.amazon.awssdk.services.dynamodb.model.ScalarAttributeType.fromValue(
        nativeValue
      )
    );
  }

  public static Select Select(String nativeValue) {
    return Select(
      software.amazon.awssdk.services.dynamodb.model.Select.fromValue(
        nativeValue
      )
    );
  }

  public static SSEStatus SSEStatus(String nativeValue) {
    return SSEStatus(
      software.amazon.awssdk.services.dynamodb.model.SSEStatus.fromValue(
        nativeValue
      )
    );
  }

  public static SSEType SSEType(String nativeValue) {
    return SSEType(
      software.amazon.awssdk.services.dynamodb.model.SSEType.fromValue(
        nativeValue
      )
    );
  }

  public static StreamViewType StreamViewType(String nativeValue) {
    return StreamViewType(
      software.amazon.awssdk.services.dynamodb.model.StreamViewType.fromValue(
        nativeValue
      )
    );
  }

  public static TableClass TableClass(String nativeValue) {
    return TableClass(
      software.amazon.awssdk.services.dynamodb.model.TableClass.fromValue(
        nativeValue
      )
    );
  }

  public static TableStatus TableStatus(String nativeValue) {
    return TableStatus(
      software.amazon.awssdk.services.dynamodb.model.TableStatus.fromValue(
        nativeValue
      )
    );
  }

  public static TimeToLiveStatus TimeToLiveStatus(String nativeValue) {
    return TimeToLiveStatus(
      software.amazon.awssdk.services.dynamodb.model.TimeToLiveStatus.fromValue(
        nativeValue
      )
    );
  }

  public static Error Error(DynamoDbException nativeValue) {
    // While this is logically identical to the other Opaque Error case,
    // it is semantically distinct.
    // An un-modeled Service Error is different from a Java Heap Exhaustion error.
    // In the future, Smithy-Dafny MAY allow for this distinction.
    // Which would allow Dafny developers to treat the two differently.
    return Error.create_OpaqueWithText(
      nativeValue,
      dafny.DafnySequence.asString(nativeValue.getMessage())
    );
  }

  public static Error Error(Exception nativeValue) {
    // While this is logically identical to the other Opaque Error case,
    // it is semantically distinct.
    // An un-modeled Service Error is different from a Java Heap Exhaustion error.
    // In the future, Smithy-Dafny MAY allow for this distinction.
    // Which would allow Dafny developers to treat the two differently.
    return Error.create_OpaqueWithText(
      nativeValue,
      dafny.DafnySequence.asString(nativeValue.getMessage())
    );
  }

  public static IDynamoDBClient DynamoDB_20120810(DynamoDbClient nativeValue) {
    return new Shim(nativeValue, null);
  }
}
