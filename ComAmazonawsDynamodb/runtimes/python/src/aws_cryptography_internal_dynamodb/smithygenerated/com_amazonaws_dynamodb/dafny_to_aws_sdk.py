# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes import (
    AttributeAction_ADD,
    AttributeAction_DELETE,
    AttributeAction_PUT,
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
    BackupStatus_AVAILABLE,
    BackupStatus_CREATING,
    BackupStatus_DELETED,
    BackupTypeFilter_ALL,
    BackupTypeFilter_AWS__BACKUP,
    BackupTypeFilter_SYSTEM,
    BackupTypeFilter_USER,
    BackupType_AWS__BACKUP,
    BackupType_SYSTEM,
    BackupType_USER,
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
    BillingMode_PAY__PER__REQUEST,
    BillingMode_PROVISIONED,
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
    ConditionalOperator_AND,
    ConditionalOperator_OR,
    ContinuousBackupsStatus_DISABLED,
    ContinuousBackupsStatus_ENABLED,
    ContributorInsightsAction_DISABLE,
    ContributorInsightsAction_ENABLE,
    ContributorInsightsStatus_DISABLED,
    ContributorInsightsStatus_DISABLING,
    ContributorInsightsStatus_ENABLED,
    ContributorInsightsStatus_ENABLING,
    ContributorInsightsStatus_FAILED,
    DestinationStatus_ACTIVE,
    DestinationStatus_DISABLED,
    DestinationStatus_DISABLING,
    DestinationStatus_ENABLE__FAILED,
    DestinationStatus_ENABLING,
    ExportFormat_DYNAMODB__JSON,
    ExportFormat_ION,
    ExportStatus_COMPLETED,
    ExportStatus_FAILED,
    ExportStatus_IN__PROGRESS,
    GlobalTableStatus_ACTIVE,
    GlobalTableStatus_CREATING,
    GlobalTableStatus_DELETING,
    GlobalTableStatus_UPDATING,
    ImportStatus_CANCELLED,
    ImportStatus_CANCELLING,
    ImportStatus_COMPLETED,
    ImportStatus_FAILED,
    ImportStatus_IN__PROGRESS,
    IndexStatus_ACTIVE,
    IndexStatus_CREATING,
    IndexStatus_DELETING,
    IndexStatus_UPDATING,
    InputCompressionType_GZIP,
    InputCompressionType_NONE,
    InputCompressionType_ZSTD,
    InputFormat_CSV,
    InputFormat_DYNAMODB__JSON,
    InputFormat_ION,
    KeyType_HASH,
    KeyType_RANGE,
    PointInTimeRecoveryStatus_DISABLED,
    PointInTimeRecoveryStatus_ENABLED,
    ProjectionType_ALL,
    ProjectionType_INCLUDE,
    ProjectionType_KEYS__ONLY,
    ReplicaStatus_ACTIVE,
    ReplicaStatus_CREATING,
    ReplicaStatus_CREATION__FAILED,
    ReplicaStatus_DELETING,
    ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS,
    ReplicaStatus_REGION__DISABLED,
    ReplicaStatus_UPDATING,
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
    S3SseAlgorithm_AES256,
    S3SseAlgorithm_KMS,
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
    Select_ALL__ATTRIBUTES,
    Select_ALL__PROJECTED__ATTRIBUTES,
    Select_COUNT,
    Select_SPECIFIC__ATTRIBUTES,
    StreamViewType_KEYS__ONLY,
    StreamViewType_NEW__AND__OLD__IMAGES,
    StreamViewType_NEW__IMAGE,
    StreamViewType_OLD__IMAGE,
    TableClass_STANDARD,
    TableClass_STANDARD__INFREQUENT__ACCESS,
    TableStatus_ACTIVE,
    TableStatus_ARCHIVED,
    TableStatus_ARCHIVING,
    TableStatus_CREATING,
    TableStatus_DELETING,
    TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS,
    TableStatus_UPDATING,
    TimeToLiveStatus_DISABLED,
    TimeToLiveStatus_DISABLING,
    TimeToLiveStatus_ENABLED,
    TimeToLiveStatus_ENABLING,
)
import aws_cryptography_internal_dynamodb.internaldafny.generated.module_
import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk
from datetime import datetime


def com_amazonaws_dynamodb_BackupInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_BackupNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ConditionalCheckFailedException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ContinuousBackupsUnavailableException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_DuplicateItemException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ExportConflictException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ExportNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_GlobalTableAlreadyExistsException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_GlobalTableNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_IdempotentParameterMismatchException(dafny_input):
    output = {}
    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ImportConflictException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ImportNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_IndexNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_InternalServerError(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_InvalidEndpointException(dafny_input):
    output = {}
    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_InvalidExportTimeException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_InvalidRestoreTimeException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ItemCollectionSizeLimitExceededException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_LimitExceededException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_PointInTimeRecoveryUnavailableException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ProvisionedThroughputExceededException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ReplicaAlreadyExistsException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ReplicaNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_RequestLimitExceeded(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ResourceInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ResourceNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TableAlreadyExistsException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TableInUseException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TableNotFoundException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_CancellationReason(dafny_input):
    output = {}
    if dafny_input.Item.is_Some:
        output["Item"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Item.value.items
        }

    if dafny_input.Code.is_Some:
        output["Code"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Code.value
        ).decode("utf-16-be")

    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_AttributeValue(dafny_input):
    # Convert AttributeValue
    if isinstance(dafny_input, AttributeValue_S):
        AttributeValue_union_value = {
            "S": b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.S).decode(
                "utf-16-be"
            )
        }
    elif isinstance(dafny_input, AttributeValue_N):
        AttributeValue_union_value = {
            "N": b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.N).decode(
                "utf-16-be"
            )
        }
    elif isinstance(dafny_input, AttributeValue_B):
        AttributeValue_union_value = {"B": bytes(dafny_input.B)}
    elif isinstance(dafny_input, AttributeValue_SS):
        AttributeValue_union_value = {
            "SS": [
                b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                    "utf-16-be"
                )
                for list_element in dafny_input.SS
            ]
        }
    elif isinstance(dafny_input, AttributeValue_NS):
        AttributeValue_union_value = {
            "NS": [
                b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                    "utf-16-be"
                )
                for list_element in dafny_input.NS
            ]
        }
    elif isinstance(dafny_input, AttributeValue_BS):
        AttributeValue_union_value = {
            "BS": [bytes(list_element) for list_element in dafny_input.BS]
        }
    elif isinstance(dafny_input, AttributeValue_M):
        AttributeValue_union_value = {
            "M": {
                b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                    "utf-16-be"
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in dafny_input.M.items
            }
        }
    elif isinstance(dafny_input, AttributeValue_L):
        AttributeValue_union_value = {
            "L": [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                    list_element
                )
                for list_element in dafny_input.L
            ]
        }
    elif isinstance(dafny_input, AttributeValue_NULL):
        AttributeValue_union_value = {"NULL": dafny_input.NULL}
    elif isinstance(dafny_input, AttributeValue_BOOL):
        AttributeValue_union_value = {"BOOL": dafny_input.BOOL}
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return AttributeValue_union_value


def com_amazonaws_dynamodb_TransactionCanceledException(dafny_input):
    output = {}
    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    if dafny_input.CancellationReasons.is_Some:
        output["CancellationReasons"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CancellationReason(
                list_element
            )
            for list_element in dafny_input.CancellationReasons.value
        ]

    return output


def com_amazonaws_dynamodb_TransactionConflictException(dafny_input):
    output = {}
    if dafny_input.message.is_Some:
        output["message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TransactionInProgressException(dafny_input):
    output = {}
    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_BatchStatementRequest(dafny_input):
    output = {}
    output["Statement"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.Statement
    ).decode("utf-16-be")
    if dafny_input.Parameters.is_Some:
        output["Parameters"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                list_element
            )
            for list_element in dafny_input.Parameters.value
        ]

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    return output


def com_amazonaws_dynamodb_ReturnConsumedCapacity(dafny_input):
    # Convert ReturnConsumedCapacity
    if isinstance(dafny_input, ReturnConsumedCapacity_INDEXES):
        return "INDEXES"

    elif isinstance(dafny_input, ReturnConsumedCapacity_TOTAL):
        return "TOTAL"

    elif isinstance(dafny_input, ReturnConsumedCapacity_NONE):
        return "NONE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_BatchExecuteStatementInput(dafny_input):
    output = {}
    output["Statements"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchStatementRequest(
            list_element
        )
        for list_element in dafny_input.Statements
    ]
    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_BatchStatementResponse(dafny_input):
    output = {}
    if dafny_input.Error.is_Some:
        output["Error"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchStatementError(
                dafny_input.Error.value
            )
        )

    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.Item.is_Some:
        output["Item"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Item.value.items
        }

    return output


def com_amazonaws_dynamodb_BatchStatementError(dafny_input):
    output = {}
    if dafny_input.Code.is_Some:
        output["Code"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(
                dafny_input.Code.value
            )
        )

    if dafny_input.Message.is_Some:
        output["Message"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Message.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(dafny_input):
    # Convert BatchStatementErrorCodeEnum
    if isinstance(dafny_input, BatchStatementErrorCodeEnum_ConditionalCheckFailed):
        return "ConditionalCheckFailed"

    elif isinstance(
        dafny_input, BatchStatementErrorCodeEnum_ItemCollectionSizeLimitExceeded
    ):
        return "ItemCollectionSizeLimitExceeded"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_RequestLimitExceeded):
        return "RequestLimitExceeded"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_ValidationError):
        return "ValidationError"

    elif isinstance(
        dafny_input, BatchStatementErrorCodeEnum_ProvisionedThroughputExceeded
    ):
        return "ProvisionedThroughputExceeded"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_TransactionConflict):
        return "TransactionConflict"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_ThrottlingError):
        return "ThrottlingError"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_InternalServerError):
        return "InternalServerError"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_ResourceNotFound):
        return "ResourceNotFound"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_AccessDenied):
        return "AccessDenied"

    elif isinstance(dafny_input, BatchStatementErrorCodeEnum_DuplicateItem):
        return "DuplicateItem"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ConsumedCapacity(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.CapacityUnits.is_Some:
        output["CapacityUnits"] = dafny_input.CapacityUnits.value

    if dafny_input.ReadCapacityUnits.is_Some:
        output["ReadCapacityUnits"] = dafny_input.ReadCapacityUnits.value

    if dafny_input.WriteCapacityUnits.is_Some:
        output["WriteCapacityUnits"] = dafny_input.WriteCapacityUnits.value

    if dafny_input.Table.is_Some:
        output["Table"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Capacity(
                dafny_input.Table.value
            )
        )

    if dafny_input.LocalSecondaryIndexes.is_Some:
        output["LocalSecondaryIndexes"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Capacity(
                value
            )
            for (key, value) in dafny_input.LocalSecondaryIndexes.value.items
        }

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Capacity(
                value
            )
            for (key, value) in dafny_input.GlobalSecondaryIndexes.value.items
        }

    return output


def com_amazonaws_dynamodb_Capacity(dafny_input):
    output = {}
    if dafny_input.ReadCapacityUnits.is_Some:
        output["ReadCapacityUnits"] = dafny_input.ReadCapacityUnits.value

    if dafny_input.WriteCapacityUnits.is_Some:
        output["WriteCapacityUnits"] = dafny_input.WriteCapacityUnits.value

    if dafny_input.CapacityUnits.is_Some:
        output["CapacityUnits"] = dafny_input.CapacityUnits.value

    return output


def com_amazonaws_dynamodb_BatchExecuteStatementOutput(dafny_input):
    output = {}
    if dafny_input.Responses.is_Some:
        output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BatchStatementResponse(
                list_element
            )
            for list_element in dafny_input.Responses.value
        ]

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    return output


def com_amazonaws_dynamodb_KeysAndAttributes(dafny_input):
    output = {}
    output["Keys"] = [
        {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in list_element.items
        }
        for list_element in dafny_input.Keys
    ]
    if dafny_input.AttributesToGet.is_Some:
        output["AttributesToGet"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.AttributesToGet.value
        ]

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    if dafny_input.ProjectionExpression.is_Some:
        output["ProjectionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ProjectionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    return output


def com_amazonaws_dynamodb_BatchGetItemInput(dafny_input):
    output = {}
    output["RequestItems"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeysAndAttributes(
            value
        )
        for (key, value) in dafny_input.RequestItems.items
    }
    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_BatchGetItemOutput(dafny_input):
    output = {}
    if dafny_input.Responses.is_Some:
        output["Responses"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode("utf-16-be"): [
                {
                    b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                        "utf-16-be"
                    ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                        value
                    )
                    for (key, value) in list_element.items
                }
                for list_element in value
            ]
            for (key, value) in dafny_input.Responses.value.items
        }

    if dafny_input.UnprocessedKeys.is_Some:
        output["UnprocessedKeys"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeysAndAttributes(
                value
            )
            for (key, value) in dafny_input.UnprocessedKeys.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    return output


def com_amazonaws_dynamodb_WriteRequest(dafny_input):
    output = {}
    if dafny_input.PutRequest.is_Some:
        output["PutRequest"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_PutRequest(
                dafny_input.PutRequest.value
            )
        )

    if dafny_input.DeleteRequest.is_Some:
        output["DeleteRequest"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteRequest(
                dafny_input.DeleteRequest.value
            )
        )

    return output


def com_amazonaws_dynamodb_PutRequest(dafny_input):
    output = {}
    output["Item"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Item.items
    }
    return output


def com_amazonaws_dynamodb_DeleteRequest(dafny_input):
    output = {}
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    return output


def com_amazonaws_dynamodb_ReturnItemCollectionMetrics(dafny_input):
    # Convert ReturnItemCollectionMetrics
    if isinstance(dafny_input, ReturnItemCollectionMetrics_SIZE):
        return "SIZE"

    elif isinstance(dafny_input, ReturnItemCollectionMetrics_NONE):
        return "NONE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_BatchWriteItemInput(dafny_input):
    output = {}
    output["RequestItems"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode("utf-16-be"): [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_WriteRequest(
                list_element
            )
            for list_element in value
        ]
        for (key, value) in dafny_input.RequestItems.items
    }
    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ReturnItemCollectionMetrics.is_Some:
        output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                dafny_input.ReturnItemCollectionMetrics.value
            )
        )

    return output


def com_amazonaws_dynamodb_ItemCollectionMetrics(dafny_input):
    output = {}
    if dafny_input.ItemCollectionKey.is_Some:
        output["ItemCollectionKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ItemCollectionKey.value.items
        }

    if dafny_input.SizeEstimateRangeGB.is_Some:
        output["SizeEstimateRangeGB"] = [
            list_element for list_element in dafny_input.SizeEstimateRangeGB.value
        ]

    return output


def com_amazonaws_dynamodb_BatchWriteItemOutput(dafny_input):
    output = {}
    if dafny_input.UnprocessedItems.is_Some:
        output["UnprocessedItems"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode("utf-16-be"): [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_WriteRequest(
                    list_element
                )
                for list_element in value
            ]
            for (key, value) in dafny_input.UnprocessedItems.value.items
        }

    if dafny_input.ItemCollectionMetrics.is_Some:
        output["ItemCollectionMetrics"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode("utf-16-be"): [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    list_element
                )
                for list_element in value
            ]
            for (key, value) in dafny_input.ItemCollectionMetrics.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    return output


def com_amazonaws_dynamodb_CreateBackupInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["BackupName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_BackupDetails(dafny_input):
    output = {}
    output["BackupArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupArn
    ).decode("utf-16-be")
    output["BackupName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupName
    ).decode("utf-16-be")
    if dafny_input.BackupSizeBytes.is_Some:
        output["BackupSizeBytes"] = dafny_input.BackupSizeBytes.value

    output["BackupStatus"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupStatus(
            dafny_input.BackupStatus
        )
    )
    output["BackupType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupType(
            dafny_input.BackupType
        )
    )
    output["BackupCreationDateTime"] = datetime.fromisoformat(
        dafny_input.BackupCreationDateTime.VerbatimString(False)
    )
    if dafny_input.BackupExpiryDateTime.is_Some:
        output["BackupExpiryDateTime"] = datetime.fromisoformat(
            dafny_input.BackupExpiryDateTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_BackupStatus(dafny_input):
    # Convert BackupStatus
    if isinstance(dafny_input, BackupStatus_CREATING):
        return "CREATING"

    elif isinstance(dafny_input, BackupStatus_DELETED):
        return "DELETED"

    elif isinstance(dafny_input, BackupStatus_AVAILABLE):
        return "AVAILABLE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_BackupType(dafny_input):
    # Convert BackupType
    if isinstance(dafny_input, BackupType_USER):
        return "USER"

    elif isinstance(dafny_input, BackupType_SYSTEM):
        return "SYSTEM"

    elif isinstance(dafny_input, BackupType_AWS__BACKUP):
        return "AWS_BACKUP"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_CreateBackupOutput(dafny_input):
    output = {}
    if dafny_input.BackupDetails.is_Some:
        output["BackupDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupDetails(
                dafny_input.BackupDetails.value
            )
        )

    return output


def com_amazonaws_dynamodb_Replica(dafny_input):
    output = {}
    if dafny_input.RegionName.is_Some:
        output["RegionName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.RegionName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_CreateGlobalTableInput(dafny_input):
    output = {}
    output["GlobalTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName
    ).decode("utf-16-be")
    output["ReplicationGroup"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Replica(
            list_element
        )
        for list_element in dafny_input.ReplicationGroup
    ]
    return output


def com_amazonaws_dynamodb_GlobalTableDescription(dafny_input):
    output = {}
    if dafny_input.ReplicationGroup.is_Some:
        output["ReplicationGroup"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaDescription(
                list_element
            )
            for list_element in dafny_input.ReplicationGroup.value
        ]

    if dafny_input.GlobalTableArn.is_Some:
        output["GlobalTableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableArn.value
        ).decode("utf-16-be")

    if dafny_input.CreationDateTime.is_Some:
        output["CreationDateTime"] = datetime.fromisoformat(
            dafny_input.CreationDateTime.value.VerbatimString(False)
        )

    if dafny_input.GlobalTableStatus.is_Some:
        output["GlobalTableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTableStatus(
                dafny_input.GlobalTableStatus.value
            )
        )

    if dafny_input.GlobalTableName.is_Some:
        output["GlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ReplicaDescription(dafny_input):
    output = {}
    if dafny_input.RegionName.is_Some:
        output["RegionName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.RegionName.value
        ).decode("utf-16-be")

    if dafny_input.ReplicaStatus.is_Some:
        output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaStatus(
                dafny_input.ReplicaStatus.value
            )
        )

    if dafny_input.ReplicaStatusDescription.is_Some:
        output["ReplicaStatusDescription"] = b"".join(
            ord(c).to_bytes(2, "big")
            for c in dafny_input.ReplicaStatusDescription.value
        ).decode("utf-16-be")

    if dafny_input.ReplicaStatusPercentProgress.is_Some:
        output["ReplicaStatusPercentProgress"] = b"".join(
            ord(c).to_bytes(2, "big")
            for c in dafny_input.ReplicaStatusPercentProgress.value
        ).decode("utf-16-be")

    if dafny_input.KMSMasterKeyId.is_Some:
        output["KMSMasterKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KMSMasterKeyId.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.ReplicaInaccessibleDateTime.is_Some:
        output["ReplicaInaccessibleDateTime"] = datetime.fromisoformat(
            dafny_input.ReplicaInaccessibleDateTime.value.VerbatimString(False)
        )

    if dafny_input.ReplicaTableClassSummary.is_Some:
        output["ReplicaTableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClassSummary(
                dafny_input.ReplicaTableClassSummary.value
            )
        )

    return output


def com_amazonaws_dynamodb_GlobalTableStatus(dafny_input):
    # Convert GlobalTableStatus
    if isinstance(dafny_input, GlobalTableStatus_CREATING):
        return "CREATING"

    elif isinstance(dafny_input, GlobalTableStatus_ACTIVE):
        return "ACTIVE"

    elif isinstance(dafny_input, GlobalTableStatus_DELETING):
        return "DELETING"

    elif isinstance(dafny_input, GlobalTableStatus_UPDATING):
        return "UPDATING"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ReplicaStatus(dafny_input):
    # Convert ReplicaStatus
    if isinstance(dafny_input, ReplicaStatus_CREATING):
        return "CREATING"

    elif isinstance(dafny_input, ReplicaStatus_CREATION__FAILED):
        return "CREATION_FAILED"

    elif isinstance(dafny_input, ReplicaStatus_UPDATING):
        return "UPDATING"

    elif isinstance(dafny_input, ReplicaStatus_DELETING):
        return "DELETING"

    elif isinstance(dafny_input, ReplicaStatus_ACTIVE):
        return "ACTIVE"

    elif isinstance(dafny_input, ReplicaStatus_REGION__DISABLED):
        return "REGION_DISABLED"

    elif isinstance(dafny_input, ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS):
        return "INACCESSIBLE_ENCRYPTION_CREDENTIALS"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ProvisionedThroughputOverride(dafny_input):
    output = {}
    if dafny_input.ReadCapacityUnits.is_Some:
        output["ReadCapacityUnits"] = dafny_input.ReadCapacityUnits.value

    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_TableClassSummary(dafny_input):
    output = {}
    if dafny_input.TableClass.is_Some:
        output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.TableClass.value
            )
        )

    if dafny_input.LastUpdateDateTime.is_Some:
        output["LastUpdateDateTime"] = datetime.fromisoformat(
            dafny_input.LastUpdateDateTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_TableClass(dafny_input):
    # Convert TableClass
    if isinstance(dafny_input, TableClass_STANDARD):
        return "STANDARD"

    elif isinstance(dafny_input, TableClass_STANDARD__INFREQUENT__ACCESS):
        return "STANDARD_INFREQUENT_ACCESS"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_CreateGlobalTableOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTableDescription.is_Some:
        output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTableDescription(
                dafny_input.GlobalTableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_AttributeDefinition(dafny_input):
    output = {}
    output["AttributeName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.AttributeName
    ).decode("utf-16-be")
    output["AttributeType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ScalarAttributeType(
            dafny_input.AttributeType
        )
    )
    return output


def com_amazonaws_dynamodb_ScalarAttributeType(dafny_input):
    # Convert ScalarAttributeType
    if isinstance(dafny_input, ScalarAttributeType_S):
        return "S"

    elif isinstance(dafny_input, ScalarAttributeType_N):
        return "N"

    elif isinstance(dafny_input, ScalarAttributeType_B):
        return "B"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_KeySchemaElement(dafny_input):
    output = {}
    output["AttributeName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.AttributeName
    ).decode("utf-16-be")
    output["KeyType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeyType(
            dafny_input.KeyType
        )
    )
    return output


def com_amazonaws_dynamodb_KeyType(dafny_input):
    # Convert KeyType
    if isinstance(dafny_input, KeyType_HASH):
        return "HASH"

    elif isinstance(dafny_input, KeyType_RANGE):
        return "RANGE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_LocalSecondaryIndex(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
            dafny_input.Projection
        )
    )
    return output


def com_amazonaws_dynamodb_Projection(dafny_input):
    output = {}
    if dafny_input.ProjectionType.is_Some:
        output["ProjectionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProjectionType(
                dafny_input.ProjectionType.value
            )
        )

    if dafny_input.NonKeyAttributes.is_Some:
        output["NonKeyAttributes"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.NonKeyAttributes.value
        ]

    return output


def com_amazonaws_dynamodb_ProjectionType(dafny_input):
    # Convert ProjectionType
    if isinstance(dafny_input, ProjectionType_ALL):
        return "ALL"

    elif isinstance(dafny_input, ProjectionType_KEYS__ONLY):
        return "KEYS_ONLY"

    elif isinstance(dafny_input, ProjectionType_INCLUDE):
        return "INCLUDE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_GlobalSecondaryIndex(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
            dafny_input.Projection
        )
    )
    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    return output


def com_amazonaws_dynamodb_ProvisionedThroughput(dafny_input):
    output = {}
    output["ReadCapacityUnits"] = dafny_input.ReadCapacityUnits
    output["WriteCapacityUnits"] = dafny_input.WriteCapacityUnits
    return output


def com_amazonaws_dynamodb_BillingMode(dafny_input):
    # Convert BillingMode
    if isinstance(dafny_input, BillingMode_PROVISIONED):
        return "PROVISIONED"

    elif isinstance(dafny_input, BillingMode_PAY__PER__REQUEST):
        return "PAY_PER_REQUEST"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_StreamSpecification(dafny_input):
    output = {}
    output["StreamEnabled"] = dafny_input.StreamEnabled
    if dafny_input.StreamViewType.is_Some:
        output["StreamViewType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_StreamViewType(
                dafny_input.StreamViewType.value
            )
        )

    return output


def com_amazonaws_dynamodb_StreamViewType(dafny_input):
    # Convert StreamViewType
    if isinstance(dafny_input, StreamViewType_NEW__IMAGE):
        return "NEW_IMAGE"

    elif isinstance(dafny_input, StreamViewType_OLD__IMAGE):
        return "OLD_IMAGE"

    elif isinstance(dafny_input, StreamViewType_NEW__AND__OLD__IMAGES):
        return "NEW_AND_OLD_IMAGES"

    elif isinstance(dafny_input, StreamViewType_KEYS__ONLY):
        return "KEYS_ONLY"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_SSESpecification(dafny_input):
    output = {}
    if dafny_input.Enabled.is_Some:
        output["Enabled"] = dafny_input.Enabled.value

    if dafny_input.SSEType.is_Some:
        output["SSEType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSEType(
                dafny_input.SSEType.value
            )
        )

    if dafny_input.KMSMasterKeyId.is_Some:
        output["KMSMasterKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KMSMasterKeyId.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_SSEType(dafny_input):
    # Convert SSEType
    if isinstance(dafny_input, SSEType_AES256):
        return "AES256"

    elif isinstance(dafny_input, SSEType_KMS):
        return "KMS"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_Tag(dafny_input):
    output = {}
    output["Key"] = b"".join(ord(c).to_bytes(2, "big") for c in dafny_input.Key).decode(
        "utf-16-be"
    )
    output["Value"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.Value
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_CreateTableInput(dafny_input):
    output = {}
    output["AttributeDefinitions"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeDefinition(
            list_element
        )
        for list_element in dafny_input.AttributeDefinitions
    ]
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    if dafny_input.LocalSecondaryIndexes.is_Some:
        output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.LocalSecondaryIndexes.value
        ]

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.BillingMode.is_Some:
        output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingMode.value
            )
        )

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    if dafny_input.StreamSpecification.is_Some:
        output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_StreamSpecification(
                dafny_input.StreamSpecification.value
            )
        )

    if dafny_input.SSESpecification.is_Some:
        output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSESpecification(
                dafny_input.SSESpecification.value
            )
        )

    if dafny_input.Tags.is_Some:
        output["Tags"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Tag(
                list_element
            )
            for list_element in dafny_input.Tags.value
        ]

    if dafny_input.TableClass.is_Some:
        output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.TableClass.value
            )
        )

    return output


def com_amazonaws_dynamodb_TableDescription(dafny_input):
    output = {}
    if dafny_input.AttributeDefinitions.is_Some:
        output["AttributeDefinitions"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeDefinition(
                list_element
            )
            for list_element in dafny_input.AttributeDefinitions.value
        ]

    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.KeySchema.is_Some:
        output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
                list_element
            )
            for list_element in dafny_input.KeySchema.value
        ]

    if dafny_input.TableStatus.is_Some:
        output["TableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableStatus(
                dafny_input.TableStatus.value
            )
        )

    if dafny_input.CreationDateTime.is_Some:
        output["CreationDateTime"] = datetime.fromisoformat(
            dafny_input.CreationDateTime.value.VerbatimString(False)
        )

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                dafny_input.ProvisionedThroughput.value
            )
        )

    if dafny_input.TableSizeBytes.is_Some:
        output["TableSizeBytes"] = dafny_input.TableSizeBytes.value

    if dafny_input.ItemCount.is_Some:
        output["ItemCount"] = dafny_input.ItemCount.value

    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.TableId.is_Some:
        output["TableId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableId.value
        ).decode("utf-16-be")

    if dafny_input.BillingModeSummary.is_Some:
        output["BillingModeSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingModeSummary(
                dafny_input.BillingModeSummary.value
            )
        )

    if dafny_input.LocalSecondaryIndexes.is_Some:
        output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_LocalSecondaryIndexDescription(
                list_element
            )
            for list_element in dafny_input.LocalSecondaryIndexes.value
        ]

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.StreamSpecification.is_Some:
        output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_StreamSpecification(
                dafny_input.StreamSpecification.value
            )
        )

    if dafny_input.LatestStreamLabel.is_Some:
        output["LatestStreamLabel"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.LatestStreamLabel.value
        ).decode("utf-16-be")

    if dafny_input.LatestStreamArn.is_Some:
        output["LatestStreamArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.LatestStreamArn.value
        ).decode("utf-16-be")

    if dafny_input.GlobalTableVersion.is_Some:
        output["GlobalTableVersion"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableVersion.value
        ).decode("utf-16-be")

    if dafny_input.Replicas.is_Some:
        output["Replicas"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaDescription(
                list_element
            )
            for list_element in dafny_input.Replicas.value
        ]

    if dafny_input.RestoreSummary.is_Some:
        output["RestoreSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_RestoreSummary(
                dafny_input.RestoreSummary.value
            )
        )

    if dafny_input.SSEDescription.is_Some:
        output["SSEDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSEDescription(
                dafny_input.SSEDescription.value
            )
        )

    if dafny_input.ArchivalSummary.is_Some:
        output["ArchivalSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ArchivalSummary(
                dafny_input.ArchivalSummary.value
            )
        )

    if dafny_input.TableClassSummary.is_Some:
        output["TableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClassSummary(
                dafny_input.TableClassSummary.value
            )
        )

    return output


def com_amazonaws_dynamodb_TableStatus(dafny_input):
    # Convert TableStatus
    if isinstance(dafny_input, TableStatus_CREATING):
        return "CREATING"

    elif isinstance(dafny_input, TableStatus_UPDATING):
        return "UPDATING"

    elif isinstance(dafny_input, TableStatus_DELETING):
        return "DELETING"

    elif isinstance(dafny_input, TableStatus_ACTIVE):
        return "ACTIVE"

    elif isinstance(dafny_input, TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS):
        return "INACCESSIBLE_ENCRYPTION_CREDENTIALS"

    elif isinstance(dafny_input, TableStatus_ARCHIVING):
        return "ARCHIVING"

    elif isinstance(dafny_input, TableStatus_ARCHIVED):
        return "ARCHIVED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ProvisionedThroughputDescription(dafny_input):
    output = {}
    if dafny_input.LastIncreaseDateTime.is_Some:
        output["LastIncreaseDateTime"] = datetime.fromisoformat(
            dafny_input.LastIncreaseDateTime.value.VerbatimString(False)
        )

    if dafny_input.LastDecreaseDateTime.is_Some:
        output["LastDecreaseDateTime"] = datetime.fromisoformat(
            dafny_input.LastDecreaseDateTime.value.VerbatimString(False)
        )

    if dafny_input.NumberOfDecreasesToday.is_Some:
        output["NumberOfDecreasesToday"] = dafny_input.NumberOfDecreasesToday.value

    if dafny_input.ReadCapacityUnits.is_Some:
        output["ReadCapacityUnits"] = dafny_input.ReadCapacityUnits.value

    if dafny_input.WriteCapacityUnits.is_Some:
        output["WriteCapacityUnits"] = dafny_input.WriteCapacityUnits.value

    return output


def com_amazonaws_dynamodb_BillingModeSummary(dafny_input):
    output = {}
    if dafny_input.BillingMode.is_Some:
        output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingMode.value
            )
        )

    if dafny_input.LastUpdateToPayPerRequestDateTime.is_Some:
        output["LastUpdateToPayPerRequestDateTime"] = datetime.fromisoformat(
            dafny_input.LastUpdateToPayPerRequestDateTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_LocalSecondaryIndexDescription(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.KeySchema.is_Some:
        output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
                list_element
            )
            for list_element in dafny_input.KeySchema.value
        ]

    if dafny_input.Projection.is_Some:
        output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
                dafny_input.Projection.value
            )
        )

    if dafny_input.IndexSizeBytes.is_Some:
        output["IndexSizeBytes"] = dafny_input.IndexSizeBytes.value

    if dafny_input.ItemCount.is_Some:
        output["ItemCount"] = dafny_input.ItemCount.value

    if dafny_input.IndexArn.is_Some:
        output["IndexArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexArn.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.KeySchema.is_Some:
        output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
                list_element
            )
            for list_element in dafny_input.KeySchema.value
        ]

    if dafny_input.Projection.is_Some:
        output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
                dafny_input.Projection.value
            )
        )

    if dafny_input.IndexStatus.is_Some:
        output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_IndexStatus(
                dafny_input.IndexStatus.value
            )
        )

    if dafny_input.Backfilling.is_Some:
        output["Backfilling"] = dafny_input.Backfilling.value

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                dafny_input.ProvisionedThroughput.value
            )
        )

    if dafny_input.IndexSizeBytes.is_Some:
        output["IndexSizeBytes"] = dafny_input.IndexSizeBytes.value

    if dafny_input.ItemCount.is_Some:
        output["ItemCount"] = dafny_input.ItemCount.value

    if dafny_input.IndexArn.is_Some:
        output["IndexArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexArn.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_RestoreSummary(dafny_input):
    output = {}
    if dafny_input.SourceBackupArn.is_Some:
        output["SourceBackupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.SourceBackupArn.value
        ).decode("utf-16-be")

    if dafny_input.SourceTableArn.is_Some:
        output["SourceTableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.SourceTableArn.value
        ).decode("utf-16-be")

    output["RestoreDateTime"] = datetime.fromisoformat(
        dafny_input.RestoreDateTime.VerbatimString(False)
    )
    output["RestoreInProgress"] = dafny_input.RestoreInProgress
    return output


def com_amazonaws_dynamodb_SSEDescription(dafny_input):
    output = {}
    if dafny_input.Status.is_Some:
        output["Status"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSEStatus(
                dafny_input.Status.value
            )
        )

    if dafny_input.SSEType.is_Some:
        output["SSEType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSEType(
                dafny_input.SSEType.value
            )
        )

    if dafny_input.KMSMasterKeyArn.is_Some:
        output["KMSMasterKeyArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KMSMasterKeyArn.value
        ).decode("utf-16-be")

    if dafny_input.InaccessibleEncryptionDateTime.is_Some:
        output["InaccessibleEncryptionDateTime"] = datetime.fromisoformat(
            dafny_input.InaccessibleEncryptionDateTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_ArchivalSummary(dafny_input):
    output = {}
    if dafny_input.ArchivalDateTime.is_Some:
        output["ArchivalDateTime"] = datetime.fromisoformat(
            dafny_input.ArchivalDateTime.value.VerbatimString(False)
        )

    if dafny_input.ArchivalReason.is_Some:
        output["ArchivalReason"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ArchivalReason.value
        ).decode("utf-16-be")

    if dafny_input.ArchivalBackupArn.is_Some:
        output["ArchivalBackupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ArchivalBackupArn.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_IndexStatus(dafny_input):
    # Convert IndexStatus
    if isinstance(dafny_input, IndexStatus_CREATING):
        return "CREATING"

    elif isinstance(dafny_input, IndexStatus_UPDATING):
        return "UPDATING"

    elif isinstance(dafny_input, IndexStatus_DELETING):
        return "DELETING"

    elif isinstance(dafny_input, IndexStatus_ACTIVE):
        return "ACTIVE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_SSEStatus(dafny_input):
    # Convert SSEStatus
    if isinstance(dafny_input, SSEStatus_ENABLING):
        return "ENABLING"

    elif isinstance(dafny_input, SSEStatus_ENABLED):
        return "ENABLED"

    elif isinstance(dafny_input, SSEStatus_DISABLING):
        return "DISABLING"

    elif isinstance(dafny_input, SSEStatus_DISABLED):
        return "DISABLED"

    elif isinstance(dafny_input, SSEStatus_UPDATING):
        return "UPDATING"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_CreateTableOutput(dafny_input):
    output = {}
    if dafny_input.TableDescription.is_Some:
        output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.TableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DeleteBackupInput(dafny_input):
    output = {}
    output["BackupArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_BackupDescription(dafny_input):
    output = {}
    if dafny_input.BackupDetails.is_Some:
        output["BackupDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupDetails(
                dafny_input.BackupDetails.value
            )
        )

    if dafny_input.SourceTableDetails.is_Some:
        output["SourceTableDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SourceTableDetails(
                dafny_input.SourceTableDetails.value
            )
        )

    if dafny_input.SourceTableFeatureDetails.is_Some:
        output["SourceTableFeatureDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SourceTableFeatureDetails(
                dafny_input.SourceTableFeatureDetails.value
            )
        )

    return output


def com_amazonaws_dynamodb_SourceTableDetails(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["TableId"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableId
    ).decode("utf-16-be")
    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.TableSizeBytes.is_Some:
        output["TableSizeBytes"] = dafny_input.TableSizeBytes.value

    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    output["TableCreationDateTime"] = datetime.fromisoformat(
        dafny_input.TableCreationDateTime.VerbatimString(False)
    )
    output["ProvisionedThroughput"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
            dafny_input.ProvisionedThroughput
        )
    )
    if dafny_input.ItemCount.is_Some:
        output["ItemCount"] = dafny_input.ItemCount.value

    if dafny_input.BillingMode.is_Some:
        output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingMode.value
            )
        )

    return output


def com_amazonaws_dynamodb_SourceTableFeatureDetails(dafny_input):
    output = {}
    if dafny_input.LocalSecondaryIndexes.is_Some:
        output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_LocalSecondaryIndexInfo(
                list_element
            )
            for list_element in dafny_input.LocalSecondaryIndexes.value
        ]

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.StreamDescription.is_Some:
        output["StreamDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_StreamSpecification(
                dafny_input.StreamDescription.value
            )
        )

    if dafny_input.TimeToLiveDescription.is_Some:
        output["TimeToLiveDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TimeToLiveDescription(
                dafny_input.TimeToLiveDescription.value
            )
        )

    if dafny_input.SSEDescription.is_Some:
        output["SSEDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSEDescription(
                dafny_input.SSEDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_LocalSecondaryIndexInfo(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.KeySchema.is_Some:
        output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
                list_element
            )
            for list_element in dafny_input.KeySchema.value
        ]

    if dafny_input.Projection.is_Some:
        output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
                dafny_input.Projection.value
            )
        )

    return output


def com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.KeySchema.is_Some:
        output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
                list_element
            )
            for list_element in dafny_input.KeySchema.value
        ]

    if dafny_input.Projection.is_Some:
        output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
                dafny_input.Projection.value
            )
        )

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    return output


def com_amazonaws_dynamodb_TimeToLiveDescription(dafny_input):
    output = {}
    if dafny_input.TimeToLiveStatus.is_Some:
        output["TimeToLiveStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TimeToLiveStatus(
                dafny_input.TimeToLiveStatus.value
            )
        )

    if dafny_input.AttributeName.is_Some:
        output["AttributeName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.AttributeName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TimeToLiveStatus(dafny_input):
    # Convert TimeToLiveStatus
    if isinstance(dafny_input, TimeToLiveStatus_ENABLING):
        return "ENABLING"

    elif isinstance(dafny_input, TimeToLiveStatus_DISABLING):
        return "DISABLING"

    elif isinstance(dafny_input, TimeToLiveStatus_ENABLED):
        return "ENABLED"

    elif isinstance(dafny_input, TimeToLiveStatus_DISABLED):
        return "DISABLED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_DeleteBackupOutput(dafny_input):
    output = {}
    if dafny_input.BackupDescription.is_Some:
        output["BackupDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupDescription(
                dafny_input.BackupDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_ExpectedAttributeValue(dafny_input):
    output = {}
    if dafny_input.Value.is_Some:
        output["Value"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                dafny_input.Value.value
            )
        )

    if dafny_input.Exists.is_Some:
        output["Exists"] = dafny_input.Exists.value

    if dafny_input.ComparisonOperator.is_Some:
        output["ComparisonOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ComparisonOperator(
                dafny_input.ComparisonOperator.value
            )
        )

    if dafny_input.AttributeValueList.is_Some:
        output["AttributeValueList"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                list_element
            )
            for list_element in dafny_input.AttributeValueList.value
        ]

    return output


def com_amazonaws_dynamodb_ComparisonOperator(dafny_input):
    # Convert ComparisonOperator
    if isinstance(dafny_input, ComparisonOperator_EQ):
        return "EQ"

    elif isinstance(dafny_input, ComparisonOperator_NE):
        return "NE"

    elif isinstance(dafny_input, ComparisonOperator_IN):
        return "IN"

    elif isinstance(dafny_input, ComparisonOperator_LE):
        return "LE"

    elif isinstance(dafny_input, ComparisonOperator_LT):
        return "LT"

    elif isinstance(dafny_input, ComparisonOperator_GE):
        return "GE"

    elif isinstance(dafny_input, ComparisonOperator_GT):
        return "GT"

    elif isinstance(dafny_input, ComparisonOperator_BETWEEN):
        return "BETWEEN"

    elif isinstance(dafny_input, ComparisonOperator_NOT__NULL):
        return "NOT_NULL"

    elif isinstance(dafny_input, ComparisonOperator_NULL):
        return "NULL"

    elif isinstance(dafny_input, ComparisonOperator_CONTAINS):
        return "CONTAINS"

    elif isinstance(dafny_input, ComparisonOperator_NOT__CONTAINS):
        return "NOT_CONTAINS"

    elif isinstance(dafny_input, ComparisonOperator_BEGINS__WITH):
        return "BEGINS_WITH"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ConditionalOperator(dafny_input):
    # Convert ConditionalOperator
    if isinstance(dafny_input, ConditionalOperator_AND):
        return "AND"

    elif isinstance(dafny_input, ConditionalOperator_OR):
        return "OR"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ReturnValue(dafny_input):
    # Convert ReturnValue
    if isinstance(dafny_input, ReturnValue_NONE):
        return "NONE"

    elif isinstance(dafny_input, ReturnValue_ALL__OLD):
        return "ALL_OLD"

    elif isinstance(dafny_input, ReturnValue_UPDATED__OLD):
        return "UPDATED_OLD"

    elif isinstance(dafny_input, ReturnValue_ALL__NEW):
        return "ALL_NEW"

    elif isinstance(dafny_input, ReturnValue_UPDATED__NEW):
        return "UPDATED_NEW"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_DeleteItemInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    if dafny_input.Expected.is_Some:
        output["Expected"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value
            )
            for (key, value) in dafny_input.Expected.value.items
        }

    if dafny_input.ConditionalOperator.is_Some:
        output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionalOperator(
                dafny_input.ConditionalOperator.value
            )
        )

    if dafny_input.ReturnValues.is_Some:
        output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValue(
                dafny_input.ReturnValues.value
            )
        )

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ReturnItemCollectionMetrics.is_Some:
        output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                dafny_input.ReturnItemCollectionMetrics.value
            )
        )

    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    return output


def com_amazonaws_dynamodb_DeleteItemOutput(dafny_input):
    output = {}
    if dafny_input.Attributes.is_Some:
        output["Attributes"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Attributes.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    if dafny_input.ItemCollectionMetrics.is_Some:
        output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemCollectionMetrics(
                dafny_input.ItemCollectionMetrics.value
            )
        )

    return output


def com_amazonaws_dynamodb_DeleteTableInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DeleteTableOutput(dafny_input):
    output = {}
    if dafny_input.TableDescription.is_Some:
        output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.TableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeBackupInput(dafny_input):
    output = {}
    output["BackupArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DescribeBackupOutput(dafny_input):
    output = {}
    if dafny_input.BackupDescription.is_Some:
        output["BackupDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupDescription(
                dafny_input.BackupDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeContinuousBackupsInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ContinuousBackupsDescription(dafny_input):
    output = {}
    output["ContinuousBackupsStatus"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContinuousBackupsStatus(
            dafny_input.ContinuousBackupsStatus
        )
    )
    if dafny_input.PointInTimeRecoveryDescription.is_Some:
        output["PointInTimeRecoveryDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_PointInTimeRecoveryDescription(
                dafny_input.PointInTimeRecoveryDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_ContinuousBackupsStatus(dafny_input):
    # Convert ContinuousBackupsStatus
    if isinstance(dafny_input, ContinuousBackupsStatus_ENABLED):
        return "ENABLED"

    elif isinstance(dafny_input, ContinuousBackupsStatus_DISABLED):
        return "DISABLED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_PointInTimeRecoveryDescription(dafny_input):
    output = {}
    if dafny_input.PointInTimeRecoveryStatus.is_Some:
        output["PointInTimeRecoveryStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_PointInTimeRecoveryStatus(
                dafny_input.PointInTimeRecoveryStatus.value
            )
        )

    if dafny_input.EarliestRestorableDateTime.is_Some:
        output["EarliestRestorableDateTime"] = datetime.fromisoformat(
            dafny_input.EarliestRestorableDateTime.value.VerbatimString(False)
        )

    if dafny_input.LatestRestorableDateTime.is_Some:
        output["LatestRestorableDateTime"] = datetime.fromisoformat(
            dafny_input.LatestRestorableDateTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_PointInTimeRecoveryStatus(dafny_input):
    # Convert PointInTimeRecoveryStatus
    if isinstance(dafny_input, PointInTimeRecoveryStatus_ENABLED):
        return "ENABLED"

    elif isinstance(dafny_input, PointInTimeRecoveryStatus_DISABLED):
        return "DISABLED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_DescribeContinuousBackupsOutput(dafny_input):
    output = {}
    if dafny_input.ContinuousBackupsDescription.is_Some:
        output["ContinuousBackupsDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                dafny_input.ContinuousBackupsDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeContributorInsightsInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ContributorInsightsStatus(dafny_input):
    # Convert ContributorInsightsStatus
    if isinstance(dafny_input, ContributorInsightsStatus_ENABLING):
        return "ENABLING"

    elif isinstance(dafny_input, ContributorInsightsStatus_ENABLED):
        return "ENABLED"

    elif isinstance(dafny_input, ContributorInsightsStatus_DISABLING):
        return "DISABLING"

    elif isinstance(dafny_input, ContributorInsightsStatus_DISABLED):
        return "DISABLED"

    elif isinstance(dafny_input, ContributorInsightsStatus_FAILED):
        return "FAILED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_FailureException(dafny_input):
    output = {}
    if dafny_input.ExceptionName.is_Some:
        output["ExceptionName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExceptionName.value
        ).decode("utf-16-be")

    if dafny_input.ExceptionDescription.is_Some:
        output["ExceptionDescription"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExceptionDescription.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_DescribeContributorInsightsOutput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ContributorInsightsRuleList.is_Some:
        output["ContributorInsightsRuleList"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.ContributorInsightsRuleList.value
        ]

    if dafny_input.ContributorInsightsStatus.is_Some:
        output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContributorInsightsStatus(
                dafny_input.ContributorInsightsStatus.value
            )
        )

    if dafny_input.LastUpdateDateTime.is_Some:
        output["LastUpdateDateTime"] = datetime.fromisoformat(
            dafny_input.LastUpdateDateTime.value.VerbatimString(False)
        )

    if dafny_input.FailureException.is_Some:
        output["FailureException"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_FailureException(
                dafny_input.FailureException.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeEndpointsRequest(dafny_input):
    output = {}
    return output


def com_amazonaws_dynamodb_Endpoint(dafny_input):
    output = {}
    output["Address"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.Address
    ).decode("utf-16-be")
    output["CachePeriodInMinutes"] = dafny_input.CachePeriodInMinutes
    return output


def com_amazonaws_dynamodb_DescribeEndpointsResponse(dafny_input):
    output = {}
    output["Endpoints"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Endpoint(
            list_element
        )
        for list_element in dafny_input.Endpoints
    ]
    return output


def com_amazonaws_dynamodb_DescribeExportInput(dafny_input):
    output = {}
    output["ExportArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ExportArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ExportDescription(dafny_input):
    output = {}
    if dafny_input.ExportArn.is_Some:
        output["ExportArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExportArn.value
        ).decode("utf-16-be")

    if dafny_input.ExportStatus.is_Some:
        output["ExportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportStatus(
                dafny_input.ExportStatus.value
            )
        )

    if dafny_input.StartTime.is_Some:
        output["StartTime"] = datetime.fromisoformat(
            dafny_input.StartTime.value.VerbatimString(False)
        )

    if dafny_input.EndTime.is_Some:
        output["EndTime"] = datetime.fromisoformat(
            dafny_input.EndTime.value.VerbatimString(False)
        )

    if dafny_input.ExportManifest.is_Some:
        output["ExportManifest"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExportManifest.value
        ).decode("utf-16-be")

    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.TableId.is_Some:
        output["TableId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableId.value
        ).decode("utf-16-be")

    if dafny_input.ExportTime.is_Some:
        output["ExportTime"] = datetime.fromisoformat(
            dafny_input.ExportTime.value.VerbatimString(False)
        )

    if dafny_input.ClientToken.is_Some:
        output["ClientToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientToken.value
        ).decode("utf-16-be")

    if dafny_input.S3Bucket.is_Some:
        output["S3Bucket"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3Bucket.value
        ).decode("utf-16-be")

    if dafny_input.S3BucketOwner.is_Some:
        output["S3BucketOwner"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3BucketOwner.value
        ).decode("utf-16-be")

    if dafny_input.S3Prefix.is_Some:
        output["S3Prefix"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3Prefix.value
        ).decode("utf-16-be")

    if dafny_input.S3SseAlgorithm.is_Some:
        output["S3SseAlgorithm"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_S3SseAlgorithm(
                dafny_input.S3SseAlgorithm.value
            )
        )

    if dafny_input.S3SseKmsKeyId.is_Some:
        output["S3SseKmsKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3SseKmsKeyId.value
        ).decode("utf-16-be")

    if dafny_input.FailureCode.is_Some:
        output["FailureCode"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FailureCode.value
        ).decode("utf-16-be")

    if dafny_input.FailureMessage.is_Some:
        output["FailureMessage"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FailureMessage.value
        ).decode("utf-16-be")

    if dafny_input.ExportFormat.is_Some:
        output["ExportFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportFormat(
                dafny_input.ExportFormat.value
            )
        )

    if dafny_input.BilledSizeBytes.is_Some:
        output["BilledSizeBytes"] = dafny_input.BilledSizeBytes.value

    if dafny_input.ItemCount.is_Some:
        output["ItemCount"] = dafny_input.ItemCount.value

    return output


def com_amazonaws_dynamodb_ExportStatus(dafny_input):
    # Convert ExportStatus
    if isinstance(dafny_input, ExportStatus_IN__PROGRESS):
        return "IN_PROGRESS"

    elif isinstance(dafny_input, ExportStatus_COMPLETED):
        return "COMPLETED"

    elif isinstance(dafny_input, ExportStatus_FAILED):
        return "FAILED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_S3SseAlgorithm(dafny_input):
    # Convert S3SseAlgorithm
    if isinstance(dafny_input, S3SseAlgorithm_AES256):
        return "AES256"

    elif isinstance(dafny_input, S3SseAlgorithm_KMS):
        return "KMS"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ExportFormat(dafny_input):
    # Convert ExportFormat
    if isinstance(dafny_input, ExportFormat_DYNAMODB__JSON):
        return "DYNAMODB_JSON"

    elif isinstance(dafny_input, ExportFormat_ION):
        return "ION"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_DescribeExportOutput(dafny_input):
    output = {}
    if dafny_input.ExportDescription.is_Some:
        output["ExportDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportDescription(
                dafny_input.ExportDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeGlobalTableInput(dafny_input):
    output = {}
    output["GlobalTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DescribeGlobalTableOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTableDescription.is_Some:
        output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTableDescription(
                dafny_input.GlobalTableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsInput(dafny_input):
    output = {}
    output["GlobalTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ReplicaSettingsDescription(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    if dafny_input.ReplicaStatus.is_Some:
        output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaStatus(
                dafny_input.ReplicaStatus.value
            )
        )

    if dafny_input.ReplicaBillingModeSummary.is_Some:
        output["ReplicaBillingModeSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingModeSummary(
                dafny_input.ReplicaBillingModeSummary.value
            )
        )

    if dafny_input.ReplicaProvisionedReadCapacityUnits.is_Some:
        output["ReplicaProvisionedReadCapacityUnits"] = (
            dafny_input.ReplicaProvisionedReadCapacityUnits.value
        )

    if dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettings.is_Some:
        output["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ReplicaProvisionedWriteCapacityUnits.is_Some:
        output["ReplicaProvisionedWriteCapacityUnits"] = (
            dafny_input.ReplicaProvisionedWriteCapacityUnits.value
        )

    if dafny_input.ReplicaProvisionedWriteCapacityAutoScalingSettings.is_Some:
        output["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ReplicaProvisionedWriteCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ReplicaGlobalSecondaryIndexSettings.is_Some:
        output["ReplicaGlobalSecondaryIndexSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(
                list_element
            )
            for list_element in dafny_input.ReplicaGlobalSecondaryIndexSettings.value
        ]

    if dafny_input.ReplicaTableClassSummary.is_Some:
        output["ReplicaTableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClassSummary(
                dafny_input.ReplicaTableClassSummary.value
            )
        )

    return output


def com_amazonaws_dynamodb_AutoScalingSettingsDescription(dafny_input):
    output = {}
    if dafny_input.MinimumUnits.is_Some:
        output["MinimumUnits"] = dafny_input.MinimumUnits.value

    if dafny_input.MaximumUnits.is_Some:
        output["MaximumUnits"] = dafny_input.MaximumUnits.value

    if dafny_input.AutoScalingDisabled.is_Some:
        output["AutoScalingDisabled"] = dafny_input.AutoScalingDisabled.value

    if dafny_input.AutoScalingRoleArn.is_Some:
        output["AutoScalingRoleArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.AutoScalingRoleArn.value
        ).decode("utf-16-be")

    if dafny_input.ScalingPolicies.is_Some:
        output["ScalingPolicies"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingPolicyDescription(
                list_element
            )
            for list_element in dafny_input.ScalingPolicies.value
        ]

    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    if dafny_input.IndexStatus.is_Some:
        output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_IndexStatus(
                dafny_input.IndexStatus.value
            )
        )

    if dafny_input.ProvisionedReadCapacityUnits.is_Some:
        output["ProvisionedReadCapacityUnits"] = (
            dafny_input.ProvisionedReadCapacityUnits.value
        )

    if dafny_input.ProvisionedReadCapacityAutoScalingSettings.is_Some:
        output["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ProvisionedReadCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ProvisionedWriteCapacityUnits.is_Some:
        output["ProvisionedWriteCapacityUnits"] = (
            dafny_input.ProvisionedWriteCapacityUnits.value
        )

    if dafny_input.ProvisionedWriteCapacityAutoScalingSettings.is_Some:
        output["ProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ProvisionedWriteCapacityAutoScalingSettings.value
            )
        )

    return output


def com_amazonaws_dynamodb_AutoScalingPolicyDescription(dafny_input):
    output = {}
    if dafny_input.PolicyName.is_Some:
        output["PolicyName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.PolicyName.value
        ).decode("utf-16-be")

    if dafny_input.TargetTrackingScalingPolicyConfiguration.is_Some:
        output["TargetTrackingScalingPolicyConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
                dafny_input.TargetTrackingScalingPolicyConfiguration.value
            )
        )

    return output


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
    dafny_input,
):
    output = {}
    if dafny_input.DisableScaleIn.is_Some:
        output["DisableScaleIn"] = dafny_input.DisableScaleIn.value

    if dafny_input.ScaleInCooldown.is_Some:
        output["ScaleInCooldown"] = dafny_input.ScaleInCooldown.value

    if dafny_input.ScaleOutCooldown.is_Some:
        output["ScaleOutCooldown"] = dafny_input.ScaleOutCooldown.value

    output["TargetValue"] = dafny_input.TargetValue
    return output


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTableName.is_Some:
        output["GlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName.value
        ).decode("utf-16-be")

    if dafny_input.ReplicaSettings.is_Some:
        output["ReplicaSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                list_element
            )
            for list_element in dafny_input.ReplicaSettings.value
        ]

    return output


def com_amazonaws_dynamodb_DescribeImportInput(dafny_input):
    output = {}
    output["ImportArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ImportArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ImportTableDescription(dafny_input):
    output = {}
    if dafny_input.ImportArn.is_Some:
        output["ImportArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ImportArn.value
        ).decode("utf-16-be")

    if dafny_input.ImportStatus.is_Some:
        output["ImportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportStatus(
                dafny_input.ImportStatus.value
            )
        )

    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.TableId.is_Some:
        output["TableId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableId.value
        ).decode("utf-16-be")

    if dafny_input.ClientToken.is_Some:
        output["ClientToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientToken.value
        ).decode("utf-16-be")

    if dafny_input.S3BucketSource.is_Some:
        output["S3BucketSource"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_S3BucketSource(
                dafny_input.S3BucketSource.value
            )
        )

    if dafny_input.ErrorCount.is_Some:
        output["ErrorCount"] = dafny_input.ErrorCount.value

    if dafny_input.CloudWatchLogGroupArn.is_Some:
        output["CloudWatchLogGroupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CloudWatchLogGroupArn.value
        ).decode("utf-16-be")

    if dafny_input.InputFormat.is_Some:
        output["InputFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputFormat(
                dafny_input.InputFormat.value
            )
        )

    if dafny_input.InputFormatOptions.is_Some:
        output["InputFormatOptions"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputFormatOptions(
                dafny_input.InputFormatOptions.value
            )
        )

    if dafny_input.InputCompressionType.is_Some:
        output["InputCompressionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputCompressionType(
                dafny_input.InputCompressionType.value
            )
        )

    if dafny_input.TableCreationParameters.is_Some:
        output["TableCreationParameters"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableCreationParameters(
                dafny_input.TableCreationParameters.value
            )
        )

    if dafny_input.StartTime.is_Some:
        output["StartTime"] = datetime.fromisoformat(
            dafny_input.StartTime.value.VerbatimString(False)
        )

    if dafny_input.EndTime.is_Some:
        output["EndTime"] = datetime.fromisoformat(
            dafny_input.EndTime.value.VerbatimString(False)
        )

    if dafny_input.ProcessedSizeBytes.is_Some:
        output["ProcessedSizeBytes"] = dafny_input.ProcessedSizeBytes.value

    if dafny_input.ProcessedItemCount.is_Some:
        output["ProcessedItemCount"] = dafny_input.ProcessedItemCount.value

    if dafny_input.ImportedItemCount.is_Some:
        output["ImportedItemCount"] = dafny_input.ImportedItemCount.value

    if dafny_input.FailureCode.is_Some:
        output["FailureCode"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FailureCode.value
        ).decode("utf-16-be")

    if dafny_input.FailureMessage.is_Some:
        output["FailureMessage"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FailureMessage.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ImportStatus(dafny_input):
    # Convert ImportStatus
    if isinstance(dafny_input, ImportStatus_IN__PROGRESS):
        return "IN_PROGRESS"

    elif isinstance(dafny_input, ImportStatus_COMPLETED):
        return "COMPLETED"

    elif isinstance(dafny_input, ImportStatus_CANCELLING):
        return "CANCELLING"

    elif isinstance(dafny_input, ImportStatus_CANCELLED):
        return "CANCELLED"

    elif isinstance(dafny_input, ImportStatus_FAILED):
        return "FAILED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_S3BucketSource(dafny_input):
    output = {}
    if dafny_input.S3BucketOwner.is_Some:
        output["S3BucketOwner"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3BucketOwner.value
        ).decode("utf-16-be")

    output["S3Bucket"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.S3Bucket
    ).decode("utf-16-be")
    if dafny_input.S3KeyPrefix.is_Some:
        output["S3KeyPrefix"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3KeyPrefix.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_InputFormat(dafny_input):
    # Convert InputFormat
    if isinstance(dafny_input, InputFormat_DYNAMODB__JSON):
        return "DYNAMODB_JSON"

    elif isinstance(dafny_input, InputFormat_ION):
        return "ION"

    elif isinstance(dafny_input, InputFormat_CSV):
        return "CSV"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_InputFormatOptions(dafny_input):
    output = {}
    if dafny_input.Csv.is_Some:
        output["Csv"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CsvOptions(
                dafny_input.Csv.value
            )
        )

    return output


def com_amazonaws_dynamodb_InputCompressionType(dafny_input):
    # Convert InputCompressionType
    if isinstance(dafny_input, InputCompressionType_GZIP):
        return "GZIP"

    elif isinstance(dafny_input, InputCompressionType_ZSTD):
        return "ZSTD"

    elif isinstance(dafny_input, InputCompressionType_NONE):
        return "NONE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_TableCreationParameters(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["AttributeDefinitions"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeDefinition(
            list_element
        )
        for list_element in dafny_input.AttributeDefinitions
    ]
    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    if dafny_input.BillingMode.is_Some:
        output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingMode.value
            )
        )

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    if dafny_input.SSESpecification.is_Some:
        output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSESpecification(
                dafny_input.SSESpecification.value
            )
        )

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    return output


def com_amazonaws_dynamodb_CsvOptions(dafny_input):
    output = {}
    if dafny_input.Delimiter.is_Some:
        output["Delimiter"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.Delimiter.value
        ).decode("utf-16-be")

    if dafny_input.HeaderList.is_Some:
        output["HeaderList"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.HeaderList.value
        ]

    return output


def com_amazonaws_dynamodb_DescribeImportOutput(dafny_input):
    output = {}
    output["ImportTableDescription"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportTableDescription(
            dafny_input.ImportTableDescription
        )
    )
    return output


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_KinesisDataStreamDestination(dafny_input):
    output = {}
    if dafny_input.StreamArn.is_Some:
        output["StreamArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.StreamArn.value
        ).decode("utf-16-be")

    if dafny_input.DestinationStatus.is_Some:
        output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DestinationStatus(
                dafny_input.DestinationStatus.value
            )
        )

    if dafny_input.DestinationStatusDescription.is_Some:
        output["DestinationStatusDescription"] = b"".join(
            ord(c).to_bytes(2, "big")
            for c in dafny_input.DestinationStatusDescription.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_DestinationStatus(dafny_input):
    # Convert DestinationStatus
    if isinstance(dafny_input, DestinationStatus_ENABLING):
        return "ENABLING"

    elif isinstance(dafny_input, DestinationStatus_ACTIVE):
        return "ACTIVE"

    elif isinstance(dafny_input, DestinationStatus_DISABLING):
        return "DISABLING"

    elif isinstance(dafny_input, DestinationStatus_DISABLED):
        return "DISABLED"

    elif isinstance(dafny_input, DestinationStatus_ENABLE__FAILED):
        return "ENABLE_FAILED"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationOutput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.KinesisDataStreamDestinations.is_Some:
        output["KinesisDataStreamDestinations"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KinesisDataStreamDestination(
                list_element
            )
            for list_element in dafny_input.KinesisDataStreamDestinations.value
        ]

    return output


def com_amazonaws_dynamodb_DescribeLimitsInput(dafny_input):
    output = {}
    return output


def com_amazonaws_dynamodb_DescribeLimitsOutput(dafny_input):
    output = {}
    if dafny_input.AccountMaxReadCapacityUnits.is_Some:
        output["AccountMaxReadCapacityUnits"] = (
            dafny_input.AccountMaxReadCapacityUnits.value
        )

    if dafny_input.AccountMaxWriteCapacityUnits.is_Some:
        output["AccountMaxWriteCapacityUnits"] = (
            dafny_input.AccountMaxWriteCapacityUnits.value
        )

    if dafny_input.TableMaxReadCapacityUnits.is_Some:
        output["TableMaxReadCapacityUnits"] = (
            dafny_input.TableMaxReadCapacityUnits.value
        )

    if dafny_input.TableMaxWriteCapacityUnits.is_Some:
        output["TableMaxWriteCapacityUnits"] = (
            dafny_input.TableMaxWriteCapacityUnits.value
        )

    return output


def com_amazonaws_dynamodb_DescribeTableInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DescribeTableOutput(dafny_input):
    output = {}
    if dafny_input.Table.is_Some:
        output["Table"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.Table.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_TableAutoScalingDescription(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.TableStatus.is_Some:
        output["TableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableStatus(
                dafny_input.TableStatus.value
            )
        )

    if dafny_input.Replicas.is_Some:
        output["Replicas"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaAutoScalingDescription(
                list_element
            )
            for list_element in dafny_input.Replicas.value
        ]

    return output


def com_amazonaws_dynamodb_ReplicaAutoScalingDescription(dafny_input):
    output = {}
    if dafny_input.RegionName.is_Some:
        output["RegionName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.RegionName.value
        ).decode("utf-16-be")

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettings.is_Some:
        output["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ReplicaProvisionedWriteCapacityAutoScalingSettings.is_Some:
        output["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ReplicaProvisionedWriteCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ReplicaStatus.is_Some:
        output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaStatus(
                dafny_input.ReplicaStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
    dafny_input,
):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.IndexStatus.is_Some:
        output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_IndexStatus(
                dafny_input.IndexStatus.value
            )
        )

    if dafny_input.ProvisionedReadCapacityAutoScalingSettings.is_Some:
        output["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ProvisionedReadCapacityAutoScalingSettings.value
            )
        )

    if dafny_input.ProvisionedWriteCapacityAutoScalingSettings.is_Some:
        output["ProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                dafny_input.ProvisionedWriteCapacityAutoScalingSettings.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingOutput(dafny_input):
    output = {}
    if dafny_input.TableAutoScalingDescription.is_Some:
        output["TableAutoScalingDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableAutoScalingDescription(
                dafny_input.TableAutoScalingDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DescribeTimeToLiveInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DescribeTimeToLiveOutput(dafny_input):
    output = {}
    if dafny_input.TimeToLiveDescription.is_Some:
        output["TimeToLiveDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TimeToLiveDescription(
                dafny_input.TimeToLiveDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["StreamArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.StreamArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationOutput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.StreamArn.is_Some:
        output["StreamArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.StreamArn.value
        ).decode("utf-16-be")

    if dafny_input.DestinationStatus.is_Some:
        output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DestinationStatus(
                dafny_input.DestinationStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["StreamArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.StreamArn
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationOutput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.StreamArn.is_Some:
        output["StreamArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.StreamArn.value
        ).decode("utf-16-be")

    if dafny_input.DestinationStatus.is_Some:
        output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DestinationStatus(
                dafny_input.DestinationStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_ExecuteStatementInput(dafny_input):
    output = {}
    output["Statement"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.Statement
    ).decode("utf-16-be")
    if dafny_input.Parameters.is_Some:
        output["Parameters"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                list_element
            )
            for list_element in dafny_input.Parameters.value
        ]

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    return output


def com_amazonaws_dynamodb_ExecuteStatementOutput(dafny_input):
    output = {}
    if dafny_input.Items.is_Some:
        output["Items"] = [
            {
                b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                    "utf-16-be"
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in list_element.items
            }
            for list_element in dafny_input.Items.value
        ]

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    if dafny_input.LastEvaluatedKey.is_Some:
        output["LastEvaluatedKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.LastEvaluatedKey.value.items
        }

    return output


def com_amazonaws_dynamodb_ParameterizedStatement(dafny_input):
    output = {}
    output["Statement"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.Statement
    ).decode("utf-16-be")
    if dafny_input.Parameters.is_Some:
        output["Parameters"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                list_element
            )
            for list_element in dafny_input.Parameters.value
        ]

    return output


def com_amazonaws_dynamodb_ExecuteTransactionInput(dafny_input):
    output = {}
    output["TransactStatements"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ParameterizedStatement(
            list_element
        )
        for list_element in dafny_input.TransactStatements
    ]
    if dafny_input.ClientRequestToken.is_Some:
        output["ClientRequestToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientRequestToken.value
        ).decode("utf-16-be")

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_ItemResponse(dafny_input):
    output = {}
    if dafny_input.Item.is_Some:
        output["Item"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Item.value.items
        }

    return output


def com_amazonaws_dynamodb_ExecuteTransactionOutput(dafny_input):
    output = {}
    if dafny_input.Responses.is_Some:
        output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemResponse(
                list_element
            )
            for list_element in dafny_input.Responses.value
        ]

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    return output


def com_amazonaws_dynamodb_ExportTableToPointInTimeInput(dafny_input):
    output = {}
    output["TableArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableArn
    ).decode("utf-16-be")
    if dafny_input.ExportTime.is_Some:
        output["ExportTime"] = datetime.fromisoformat(
            dafny_input.ExportTime.value.VerbatimString(False)
        )

    if dafny_input.ClientToken.is_Some:
        output["ClientToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientToken.value
        ).decode("utf-16-be")

    output["S3Bucket"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.S3Bucket
    ).decode("utf-16-be")
    if dafny_input.S3BucketOwner.is_Some:
        output["S3BucketOwner"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3BucketOwner.value
        ).decode("utf-16-be")

    if dafny_input.S3Prefix.is_Some:
        output["S3Prefix"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3Prefix.value
        ).decode("utf-16-be")

    if dafny_input.S3SseAlgorithm.is_Some:
        output["S3SseAlgorithm"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_S3SseAlgorithm(
                dafny_input.S3SseAlgorithm.value
            )
        )

    if dafny_input.S3SseKmsKeyId.is_Some:
        output["S3SseKmsKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.S3SseKmsKeyId.value
        ).decode("utf-16-be")

    if dafny_input.ExportFormat.is_Some:
        output["ExportFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportFormat(
                dafny_input.ExportFormat.value
            )
        )

    return output


def com_amazonaws_dynamodb_ExportTableToPointInTimeOutput(dafny_input):
    output = {}
    if dafny_input.ExportDescription.is_Some:
        output["ExportDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportDescription(
                dafny_input.ExportDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_GetItemInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    if dafny_input.AttributesToGet.is_Some:
        output["AttributesToGet"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.AttributesToGet.value
        ]

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ProjectionExpression.is_Some:
        output["ProjectionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ProjectionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    return output


def com_amazonaws_dynamodb_GetItemOutput(dafny_input):
    output = {}
    if dafny_input.Item.is_Some:
        output["Item"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Item.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_ImportTableInput(dafny_input):
    output = {}
    if dafny_input.ClientToken.is_Some:
        output["ClientToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientToken.value
        ).decode("utf-16-be")

    output["S3BucketSource"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_S3BucketSource(
            dafny_input.S3BucketSource
        )
    )
    output["InputFormat"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputFormat(
            dafny_input.InputFormat
        )
    )
    if dafny_input.InputFormatOptions.is_Some:
        output["InputFormatOptions"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputFormatOptions(
                dafny_input.InputFormatOptions.value
            )
        )

    if dafny_input.InputCompressionType.is_Some:
        output["InputCompressionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputCompressionType(
                dafny_input.InputCompressionType.value
            )
        )

    output["TableCreationParameters"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableCreationParameters(
            dafny_input.TableCreationParameters
        )
    )
    return output


def com_amazonaws_dynamodb_ImportTableOutput(dafny_input):
    output = {}
    output["ImportTableDescription"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportTableDescription(
            dafny_input.ImportTableDescription
        )
    )
    return output


def com_amazonaws_dynamodb_BackupTypeFilter(dafny_input):
    # Convert BackupTypeFilter
    if isinstance(dafny_input, BackupTypeFilter_USER):
        return "USER"

    elif isinstance(dafny_input, BackupTypeFilter_SYSTEM):
        return "SYSTEM"

    elif isinstance(dafny_input, BackupTypeFilter_AWS__BACKUP):
        return "AWS_BACKUP"

    elif isinstance(dafny_input, BackupTypeFilter_ALL):
        return "ALL"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_ListBackupsInput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.TimeRangeLowerBound.is_Some:
        output["TimeRangeLowerBound"] = datetime.fromisoformat(
            dafny_input.TimeRangeLowerBound.value.VerbatimString(False)
        )

    if dafny_input.TimeRangeUpperBound.is_Some:
        output["TimeRangeUpperBound"] = datetime.fromisoformat(
            dafny_input.TimeRangeUpperBound.value.VerbatimString(False)
        )

    if dafny_input.ExclusiveStartBackupArn.is_Some:
        output["ExclusiveStartBackupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExclusiveStartBackupArn.value
        ).decode("utf-16-be")

    if dafny_input.BackupType.is_Some:
        output["BackupType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupTypeFilter(
                dafny_input.BackupType.value
            )
        )

    return output


def com_amazonaws_dynamodb_BackupSummary(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.TableId.is_Some:
        output["TableId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableId.value
        ).decode("utf-16-be")

    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.BackupArn.is_Some:
        output["BackupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.BackupArn.value
        ).decode("utf-16-be")

    if dafny_input.BackupName.is_Some:
        output["BackupName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.BackupName.value
        ).decode("utf-16-be")

    if dafny_input.BackupCreationDateTime.is_Some:
        output["BackupCreationDateTime"] = datetime.fromisoformat(
            dafny_input.BackupCreationDateTime.value.VerbatimString(False)
        )

    if dafny_input.BackupExpiryDateTime.is_Some:
        output["BackupExpiryDateTime"] = datetime.fromisoformat(
            dafny_input.BackupExpiryDateTime.value.VerbatimString(False)
        )

    if dafny_input.BackupStatus.is_Some:
        output["BackupStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupStatus(
                dafny_input.BackupStatus.value
            )
        )

    if dafny_input.BackupType.is_Some:
        output["BackupType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupType(
                dafny_input.BackupType.value
            )
        )

    if dafny_input.BackupSizeBytes.is_Some:
        output["BackupSizeBytes"] = dafny_input.BackupSizeBytes.value

    return output


def com_amazonaws_dynamodb_ListBackupsOutput(dafny_input):
    output = {}
    if dafny_input.BackupSummaries.is_Some:
        output["BackupSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BackupSummary(
                list_element
            )
            for list_element in dafny_input.BackupSummaries.value
        ]

    if dafny_input.LastEvaluatedBackupArn.is_Some:
        output["LastEvaluatedBackupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.LastEvaluatedBackupArn.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListContributorInsightsInput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    if dafny_input.MaxResults.is_Some:
        output["MaxResults"] = dafny_input.MaxResults.value

    return output


def com_amazonaws_dynamodb_ContributorInsightsSummary(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ContributorInsightsStatus.is_Some:
        output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContributorInsightsStatus(
                dafny_input.ContributorInsightsStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_ListContributorInsightsOutput(dafny_input):
    output = {}
    if dafny_input.ContributorInsightsSummaries.is_Some:
        output["ContributorInsightsSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContributorInsightsSummary(
                list_element
            )
            for list_element in dafny_input.ContributorInsightsSummaries.value
        ]

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListExportsInput(dafny_input):
    output = {}
    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.MaxResults.is_Some:
        output["MaxResults"] = dafny_input.MaxResults.value

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ExportSummary(dafny_input):
    output = {}
    if dafny_input.ExportArn.is_Some:
        output["ExportArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExportArn.value
        ).decode("utf-16-be")

    if dafny_input.ExportStatus.is_Some:
        output["ExportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportStatus(
                dafny_input.ExportStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_ListExportsOutput(dafny_input):
    output = {}
    if dafny_input.ExportSummaries.is_Some:
        output["ExportSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExportSummary(
                list_element
            )
            for list_element in dafny_input.ExportSummaries.value
        ]

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListGlobalTablesInput(dafny_input):
    output = {}
    if dafny_input.ExclusiveStartGlobalTableName.is_Some:
        output["ExclusiveStartGlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big")
            for c in dafny_input.ExclusiveStartGlobalTableName.value
        ).decode("utf-16-be")

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.RegionName.is_Some:
        output["RegionName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.RegionName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_GlobalTable(dafny_input):
    output = {}
    if dafny_input.GlobalTableName.is_Some:
        output["GlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName.value
        ).decode("utf-16-be")

    if dafny_input.ReplicationGroup.is_Some:
        output["ReplicationGroup"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Replica(
                list_element
            )
            for list_element in dafny_input.ReplicationGroup.value
        ]

    return output


def com_amazonaws_dynamodb_ListGlobalTablesOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTables.is_Some:
        output["GlobalTables"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTable(
                list_element
            )
            for list_element in dafny_input.GlobalTables.value
        ]

    if dafny_input.LastEvaluatedGlobalTableName.is_Some:
        output["LastEvaluatedGlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big")
            for c in dafny_input.LastEvaluatedGlobalTableName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListImportsInput(dafny_input):
    output = {}
    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.PageSize.is_Some:
        output["PageSize"] = dafny_input.PageSize.value

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ImportSummary(dafny_input):
    output = {}
    if dafny_input.ImportArn.is_Some:
        output["ImportArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ImportArn.value
        ).decode("utf-16-be")

    if dafny_input.ImportStatus.is_Some:
        output["ImportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportStatus(
                dafny_input.ImportStatus.value
            )
        )

    if dafny_input.TableArn.is_Some:
        output["TableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableArn.value
        ).decode("utf-16-be")

    if dafny_input.S3BucketSource.is_Some:
        output["S3BucketSource"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_S3BucketSource(
                dafny_input.S3BucketSource.value
            )
        )

    if dafny_input.CloudWatchLogGroupArn.is_Some:
        output["CloudWatchLogGroupArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.CloudWatchLogGroupArn.value
        ).decode("utf-16-be")

    if dafny_input.InputFormat.is_Some:
        output["InputFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_InputFormat(
                dafny_input.InputFormat.value
            )
        )

    if dafny_input.StartTime.is_Some:
        output["StartTime"] = datetime.fromisoformat(
            dafny_input.StartTime.value.VerbatimString(False)
        )

    if dafny_input.EndTime.is_Some:
        output["EndTime"] = datetime.fromisoformat(
            dafny_input.EndTime.value.VerbatimString(False)
        )

    return output


def com_amazonaws_dynamodb_ListImportsOutput(dafny_input):
    output = {}
    if dafny_input.ImportSummaryList.is_Some:
        output["ImportSummaryList"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ImportSummary(
                list_element
            )
            for list_element in dafny_input.ImportSummaryList.value
        ]

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListTablesInput(dafny_input):
    output = {}
    if dafny_input.ExclusiveStartTableName.is_Some:
        output["ExclusiveStartTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ExclusiveStartTableName.value
        ).decode("utf-16-be")

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    return output


def com_amazonaws_dynamodb_ListTablesOutput(dafny_input):
    output = {}
    if dafny_input.TableNames.is_Some:
        output["TableNames"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.TableNames.value
        ]

    if dafny_input.LastEvaluatedTableName.is_Some:
        output["LastEvaluatedTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.LastEvaluatedTableName.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListTagsOfResourceInput(dafny_input):
    output = {}
    output["ResourceArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ResourceArn
    ).decode("utf-16-be")
    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_ListTagsOfResourceOutput(dafny_input):
    output = {}
    if dafny_input.Tags.is_Some:
        output["Tags"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Tag(
                list_element
            )
            for list_element in dafny_input.Tags.value
        ]

    if dafny_input.NextToken.is_Some:
        output["NextToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.NextToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_PutItemInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["Item"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Item.items
    }
    if dafny_input.Expected.is_Some:
        output["Expected"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value
            )
            for (key, value) in dafny_input.Expected.value.items
        }

    if dafny_input.ReturnValues.is_Some:
        output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValue(
                dafny_input.ReturnValues.value
            )
        )

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ReturnItemCollectionMetrics.is_Some:
        output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                dafny_input.ReturnItemCollectionMetrics.value
            )
        )

    if dafny_input.ConditionalOperator.is_Some:
        output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionalOperator(
                dafny_input.ConditionalOperator.value
            )
        )

    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    return output


def com_amazonaws_dynamodb_PutItemOutput(dafny_input):
    output = {}
    if dafny_input.Attributes.is_Some:
        output["Attributes"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Attributes.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    if dafny_input.ItemCollectionMetrics.is_Some:
        output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemCollectionMetrics(
                dafny_input.ItemCollectionMetrics.value
            )
        )

    return output


def com_amazonaws_dynamodb_Select(dafny_input):
    # Convert Select
    if isinstance(dafny_input, Select_ALL__ATTRIBUTES):
        return "ALL_ATTRIBUTES"

    elif isinstance(dafny_input, Select_ALL__PROJECTED__ATTRIBUTES):
        return "ALL_PROJECTED_ATTRIBUTES"

    elif isinstance(dafny_input, Select_SPECIFIC__ATTRIBUTES):
        return "SPECIFIC_ATTRIBUTES"

    elif isinstance(dafny_input, Select_COUNT):
        return "COUNT"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_Condition(dafny_input):
    output = {}
    if dafny_input.AttributeValueList.is_Some:
        output["AttributeValueList"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                list_element
            )
            for list_element in dafny_input.AttributeValueList.value
        ]

    output["ComparisonOperator"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ComparisonOperator(
            dafny_input.ComparisonOperator
        )
    )
    return output


def com_amazonaws_dynamodb_QueryInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.Select.is_Some:
        output["Select"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Select(
                dafny_input.Select.value
            )
        )

    if dafny_input.AttributesToGet.is_Some:
        output["AttributesToGet"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.AttributesToGet.value
        ]

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    if dafny_input.KeyConditions.is_Some:
        output["KeyConditions"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Condition(
                value
            )
            for (key, value) in dafny_input.KeyConditions.value.items
        }

    if dafny_input.QueryFilter.is_Some:
        output["QueryFilter"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Condition(
                value
            )
            for (key, value) in dafny_input.QueryFilter.value.items
        }

    if dafny_input.ConditionalOperator.is_Some:
        output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionalOperator(
                dafny_input.ConditionalOperator.value
            )
        )

    if dafny_input.ScanIndexForward.is_Some:
        output["ScanIndexForward"] = dafny_input.ScanIndexForward.value

    if dafny_input.ExclusiveStartKey.is_Some:
        output["ExclusiveStartKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExclusiveStartKey.value.items
        }

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ProjectionExpression.is_Some:
        output["ProjectionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ProjectionExpression.value
        ).decode("utf-16-be")

    if dafny_input.FilterExpression.is_Some:
        output["FilterExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FilterExpression.value
        ).decode("utf-16-be")

    if dafny_input.KeyConditionExpression.is_Some:
        output["KeyConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KeyConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    return output


def com_amazonaws_dynamodb_QueryOutput(dafny_input):
    output = {}
    if dafny_input.Items.is_Some:
        output["Items"] = [
            {
                b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                    "utf-16-be"
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in list_element.items
            }
            for list_element in dafny_input.Items.value
        ]

    if dafny_input.Count.is_Some:
        output["Count"] = dafny_input.Count.value

    if dafny_input.ScannedCount.is_Some:
        output["ScannedCount"] = dafny_input.ScannedCount.value

    if dafny_input.LastEvaluatedKey.is_Some:
        output["LastEvaluatedKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.LastEvaluatedKey.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_RestoreTableFromBackupInput(dafny_input):
    output = {}
    output["TargetTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TargetTableName
    ).decode("utf-16-be")
    output["BackupArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.BackupArn
    ).decode("utf-16-be")
    if dafny_input.BillingModeOverride.is_Some:
        output["BillingModeOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingModeOverride.value
            )
        )

    if dafny_input.GlobalSecondaryIndexOverride.is_Some:
        output["GlobalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexOverride.value
        ]

    if dafny_input.LocalSecondaryIndexOverride.is_Some:
        output["LocalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.LocalSecondaryIndexOverride.value
        ]

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    if dafny_input.SSESpecificationOverride.is_Some:
        output["SSESpecificationOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSESpecification(
                dafny_input.SSESpecificationOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_RestoreTableFromBackupOutput(dafny_input):
    output = {}
    if dafny_input.TableDescription.is_Some:
        output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.TableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_RestoreTableToPointInTimeInput(dafny_input):
    output = {}
    if dafny_input.SourceTableArn.is_Some:
        output["SourceTableArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.SourceTableArn.value
        ).decode("utf-16-be")

    if dafny_input.SourceTableName.is_Some:
        output["SourceTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.SourceTableName.value
        ).decode("utf-16-be")

    output["TargetTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TargetTableName
    ).decode("utf-16-be")
    if dafny_input.UseLatestRestorableTime.is_Some:
        output["UseLatestRestorableTime"] = dafny_input.UseLatestRestorableTime.value

    if dafny_input.RestoreDateTime.is_Some:
        output["RestoreDateTime"] = datetime.fromisoformat(
            dafny_input.RestoreDateTime.value.VerbatimString(False)
        )

    if dafny_input.BillingModeOverride.is_Some:
        output["BillingModeOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingModeOverride.value
            )
        )

    if dafny_input.GlobalSecondaryIndexOverride.is_Some:
        output["GlobalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexOverride.value
        ]

    if dafny_input.LocalSecondaryIndexOverride.is_Some:
        output["LocalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.LocalSecondaryIndexOverride.value
        ]

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    if dafny_input.SSESpecificationOverride.is_Some:
        output["SSESpecificationOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSESpecification(
                dafny_input.SSESpecificationOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_RestoreTableToPointInTimeOutput(dafny_input):
    output = {}
    if dafny_input.TableDescription.is_Some:
        output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.TableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_ScanInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.AttributesToGet.is_Some:
        output["AttributesToGet"] = [
            b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode(
                "utf-16-be"
            )
            for list_element in dafny_input.AttributesToGet.value
        ]

    if dafny_input.Limit.is_Some:
        output["Limit"] = dafny_input.Limit.value

    if dafny_input.Select.is_Some:
        output["Select"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Select(
                dafny_input.Select.value
            )
        )

    if dafny_input.ScanFilter.is_Some:
        output["ScanFilter"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Condition(
                value
            )
            for (key, value) in dafny_input.ScanFilter.value.items
        }

    if dafny_input.ConditionalOperator.is_Some:
        output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionalOperator(
                dafny_input.ConditionalOperator.value
            )
        )

    if dafny_input.ExclusiveStartKey.is_Some:
        output["ExclusiveStartKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExclusiveStartKey.value.items
        }

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.TotalSegments.is_Some:
        output["TotalSegments"] = dafny_input.TotalSegments.value

    if dafny_input.Segment.is_Some:
        output["Segment"] = dafny_input.Segment.value

    if dafny_input.ProjectionExpression.is_Some:
        output["ProjectionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ProjectionExpression.value
        ).decode("utf-16-be")

    if dafny_input.FilterExpression.is_Some:
        output["FilterExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.FilterExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    if dafny_input.ConsistentRead.is_Some:
        output["ConsistentRead"] = dafny_input.ConsistentRead.value

    return output


def com_amazonaws_dynamodb_ScanOutput(dafny_input):
    output = {}
    if dafny_input.Items.is_Some:
        output["Items"] = [
            {
                b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                    "utf-16-be"
                ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                    value
                )
                for (key, value) in list_element.items
            }
            for list_element in dafny_input.Items.value
        ]

    if dafny_input.Count.is_Some:
        output["Count"] = dafny_input.Count.value

    if dafny_input.ScannedCount.is_Some:
        output["ScannedCount"] = dafny_input.ScannedCount.value

    if dafny_input.LastEvaluatedKey.is_Some:
        output["LastEvaluatedKey"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.LastEvaluatedKey.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_TagResourceInput(dafny_input):
    output = {}
    output["ResourceArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ResourceArn
    ).decode("utf-16-be")
    output["Tags"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Tag(
            list_element
        )
        for list_element in dafny_input.Tags
    ]
    return output


def com_amazonaws_dynamodb_TransactGetItem(dafny_input):
    output = {}
    output["Get"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Get(
            dafny_input.Get
        )
    )
    return output


def com_amazonaws_dynamodb_Get(dafny_input):
    output = {}
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.ProjectionExpression.is_Some:
        output["ProjectionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ProjectionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    return output


def com_amazonaws_dynamodb_TransactGetItemsInput(dafny_input):
    output = {}
    output["TransactItems"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TransactGetItem(
            list_element
        )
        for list_element in dafny_input.TransactItems
    ]
    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    return output


def com_amazonaws_dynamodb_TransactGetItemsOutput(dafny_input):
    output = {}
    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    if dafny_input.Responses.is_Some:
        output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemResponse(
                list_element
            )
            for list_element in dafny_input.Responses.value
        ]

    return output


def com_amazonaws_dynamodb_TransactWriteItem(dafny_input):
    output = {}
    if dafny_input.ConditionCheck.is_Some:
        output["ConditionCheck"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionCheck(
                dafny_input.ConditionCheck.value
            )
        )

    if dafny_input.Put.is_Some:
        output["Put"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Put(
                dafny_input.Put.value
            )
        )

    if dafny_input.Delete.is_Some:
        output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Delete(
                dafny_input.Delete.value
            )
        )

    if dafny_input.Update.is_Some:
        output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Update(
                dafny_input.Update.value
            )
        )

    return output


def com_amazonaws_dynamodb_ConditionCheck(dafny_input):
    output = {}
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["ConditionExpression"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression
    ).decode("utf-16-be")
    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    if dafny_input.ReturnValuesOnConditionCheckFailure.is_Some:
        output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                dafny_input.ReturnValuesOnConditionCheckFailure.value
            )
        )

    return output


def com_amazonaws_dynamodb_Put(dafny_input):
    output = {}
    output["Item"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Item.items
    }
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    if dafny_input.ReturnValuesOnConditionCheckFailure.is_Some:
        output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                dafny_input.ReturnValuesOnConditionCheckFailure.value
            )
        )

    return output


def com_amazonaws_dynamodb_Delete(dafny_input):
    output = {}
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    if dafny_input.ReturnValuesOnConditionCheckFailure.is_Some:
        output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                dafny_input.ReturnValuesOnConditionCheckFailure.value
            )
        )

    return output


def com_amazonaws_dynamodb_Update(dafny_input):
    output = {}
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    output["UpdateExpression"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.UpdateExpression
    ).decode("utf-16-be")
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    if dafny_input.ReturnValuesOnConditionCheckFailure.is_Some:
        output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                dafny_input.ReturnValuesOnConditionCheckFailure.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(dafny_input):
    # Convert ReturnValuesOnConditionCheckFailure
    if isinstance(dafny_input, ReturnValuesOnConditionCheckFailure_ALL__OLD):
        return "ALL_OLD"

    elif isinstance(dafny_input, ReturnValuesOnConditionCheckFailure_NONE):
        return "NONE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_TransactWriteItemsInput(dafny_input):
    output = {}
    output["TransactItems"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TransactWriteItem(
            list_element
        )
        for list_element in dafny_input.TransactItems
    ]
    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ReturnItemCollectionMetrics.is_Some:
        output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                dafny_input.ReturnItemCollectionMetrics.value
            )
        )

    if dafny_input.ClientRequestToken.is_Some:
        output["ClientRequestToken"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ClientRequestToken.value
        ).decode("utf-16-be")

    return output


def com_amazonaws_dynamodb_TransactWriteItemsOutput(dafny_input):
    output = {}
    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element
            )
            for list_element in dafny_input.ConsumedCapacity.value
        ]

    if dafny_input.ItemCollectionMetrics.is_Some:
        output["ItemCollectionMetrics"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode("utf-16-be"): [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    list_element
                )
                for list_element in value
            ]
            for (key, value) in dafny_input.ItemCollectionMetrics.value.items
        }

    return output


def com_amazonaws_dynamodb_UntagResourceInput(dafny_input):
    output = {}
    output["ResourceArn"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.ResourceArn
    ).decode("utf-16-be")
    output["TagKeys"] = [
        b"".join(ord(c).to_bytes(2, "big") for c in list_element).decode("utf-16-be")
        for list_element in dafny_input.TagKeys
    ]
    return output


def com_amazonaws_dynamodb_PointInTimeRecoverySpecification(dafny_input):
    output = {}
    output["PointInTimeRecoveryEnabled"] = dafny_input.PointInTimeRecoveryEnabled
    return output


def com_amazonaws_dynamodb_UpdateContinuousBackupsInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["PointInTimeRecoverySpecification"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_PointInTimeRecoverySpecification(
            dafny_input.PointInTimeRecoverySpecification
        )
    )
    return output


def com_amazonaws_dynamodb_UpdateContinuousBackupsOutput(dafny_input):
    output = {}
    if dafny_input.ContinuousBackupsDescription.is_Some:
        output["ContinuousBackupsDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                dafny_input.ContinuousBackupsDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_ContributorInsightsAction(dafny_input):
    # Convert ContributorInsightsAction
    if isinstance(dafny_input, ContributorInsightsAction_ENABLE):
        return "ENABLE"

    elif isinstance(dafny_input, ContributorInsightsAction_DISABLE):
        return "DISABLE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_UpdateContributorInsightsInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    output["ContributorInsightsAction"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContributorInsightsAction(
            dafny_input.ContributorInsightsAction
        )
    )
    return output


def com_amazonaws_dynamodb_UpdateContributorInsightsOutput(dafny_input):
    output = {}
    if dafny_input.TableName.is_Some:
        output["TableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.TableName.value
        ).decode("utf-16-be")

    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ContributorInsightsStatus.is_Some:
        output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ContributorInsightsStatus(
                dafny_input.ContributorInsightsStatus.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaUpdate(dafny_input):
    output = {}
    if dafny_input.Create.is_Some:
        output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateReplicaAction(
                dafny_input.Create.value
            )
        )

    if dafny_input.Delete.is_Some:
        output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteReplicaAction(
                dafny_input.Delete.value
            )
        )

    return output


def com_amazonaws_dynamodb_CreateReplicaAction(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_DeleteReplicaAction(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_UpdateGlobalTableInput(dafny_input):
    output = {}
    output["GlobalTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName
    ).decode("utf-16-be")
    output["ReplicaUpdates"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaUpdate(
            list_element
        )
        for list_element in dafny_input.ReplicaUpdates
    ]
    return output


def com_amazonaws_dynamodb_UpdateGlobalTableOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTableDescription.is_Some:
        output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTableDescription(
                dafny_input.GlobalTableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_AutoScalingSettingsUpdate(dafny_input):
    output = {}
    if dafny_input.MinimumUnits.is_Some:
        output["MinimumUnits"] = dafny_input.MinimumUnits.value

    if dafny_input.MaximumUnits.is_Some:
        output["MaximumUnits"] = dafny_input.MaximumUnits.value

    if dafny_input.AutoScalingDisabled.is_Some:
        output["AutoScalingDisabled"] = dafny_input.AutoScalingDisabled.value

    if dafny_input.AutoScalingRoleArn.is_Some:
        output["AutoScalingRoleArn"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.AutoScalingRoleArn.value
        ).decode("utf-16-be")

    if dafny_input.ScalingPolicyUpdate.is_Some:
        output["ScalingPolicyUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingPolicyUpdate(
                dafny_input.ScalingPolicyUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_AutoScalingPolicyUpdate(dafny_input):
    output = {}
    if dafny_input.PolicyName.is_Some:
        output["PolicyName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.PolicyName.value
        ).decode("utf-16-be")

    output["TargetTrackingScalingPolicyConfiguration"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
            dafny_input.TargetTrackingScalingPolicyConfiguration
        )
    )
    return output


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
    dafny_input,
):
    output = {}
    if dafny_input.DisableScaleIn.is_Some:
        output["DisableScaleIn"] = dafny_input.DisableScaleIn.value

    if dafny_input.ScaleInCooldown.is_Some:
        output["ScaleInCooldown"] = dafny_input.ScaleInCooldown.value

    if dafny_input.ScaleOutCooldown.is_Some:
        output["ScaleOutCooldown"] = dafny_input.ScaleOutCooldown.value

    output["TargetValue"] = dafny_input.TargetValue
    return output


def com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    if dafny_input.ProvisionedWriteCapacityUnits.is_Some:
        output["ProvisionedWriteCapacityUnits"] = (
            dafny_input.ProvisionedWriteCapacityUnits.value
        )

    if dafny_input.ProvisionedWriteCapacityAutoScalingSettingsUpdate.is_Some:
        output["ProvisionedWriteCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ProvisionedWriteCapacityAutoScalingSettingsUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaSettingsUpdate(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    if dafny_input.ReplicaProvisionedReadCapacityUnits.is_Some:
        output["ReplicaProvisionedReadCapacityUnits"] = (
            dafny_input.ReplicaProvisionedReadCapacityUnits.value
        )

    if dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate.is_Some:
        output["ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate.value
            )
        )

    if dafny_input.ReplicaGlobalSecondaryIndexSettingsUpdate.is_Some:
        output["ReplicaGlobalSecondaryIndexSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(
                list_element
            )
            for list_element in dafny_input.ReplicaGlobalSecondaryIndexSettingsUpdate.value
        ]

    if dafny_input.ReplicaTableClass.is_Some:
        output["ReplicaTableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.ReplicaTableClass.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    if dafny_input.ProvisionedReadCapacityUnits.is_Some:
        output["ProvisionedReadCapacityUnits"] = (
            dafny_input.ProvisionedReadCapacityUnits.value
        )

    if dafny_input.ProvisionedReadCapacityAutoScalingSettingsUpdate.is_Some:
        output["ProvisionedReadCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ProvisionedReadCapacityAutoScalingSettingsUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsInput(dafny_input):
    output = {}
    output["GlobalTableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName
    ).decode("utf-16-be")
    if dafny_input.GlobalTableBillingMode.is_Some:
        output["GlobalTableBillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.GlobalTableBillingMode.value
            )
        )

    if dafny_input.GlobalTableProvisionedWriteCapacityUnits.is_Some:
        output["GlobalTableProvisionedWriteCapacityUnits"] = (
            dafny_input.GlobalTableProvisionedWriteCapacityUnits.value
        )

    if dafny_input.GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate.is_Some:
        output["GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate.value
            )
        )

    if dafny_input.GlobalTableGlobalSecondaryIndexSettingsUpdate.is_Some:
        output["GlobalTableGlobalSecondaryIndexSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(
                list_element
            )
            for list_element in dafny_input.GlobalTableGlobalSecondaryIndexSettingsUpdate.value
        ]

    if dafny_input.ReplicaSettingsUpdate.is_Some:
        output["ReplicaSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaSettingsUpdate(
                list_element
            )
            for list_element in dafny_input.ReplicaSettingsUpdate.value
        ]

    return output


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsOutput(dafny_input):
    output = {}
    if dafny_input.GlobalTableName.is_Some:
        output["GlobalTableName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.GlobalTableName.value
        ).decode("utf-16-be")

    if dafny_input.ReplicaSettings.is_Some:
        output["ReplicaSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                list_element
            )
            for list_element in dafny_input.ReplicaSettings.value
        ]

    return output


def com_amazonaws_dynamodb_AttributeValueUpdate(dafny_input):
    output = {}
    if dafny_input.Value.is_Some:
        output["Value"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                dafny_input.Value.value
            )
        )

    if dafny_input.Action.is_Some:
        output["Action"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeAction(
                dafny_input.Action.value
            )
        )

    return output


def com_amazonaws_dynamodb_AttributeAction(dafny_input):
    # Convert AttributeAction
    if isinstance(dafny_input, AttributeAction_ADD):
        return "ADD"

    elif isinstance(dafny_input, AttributeAction_PUT):
        return "PUT"

    elif isinstance(dafny_input, AttributeAction_DELETE):
        return "DELETE"

    else:
        raise ValueError("No recognized enum value in enum type: " + dafny_input)


def com_amazonaws_dynamodb_UpdateItemInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["Key"] = {
        b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
            "utf-16-be"
        ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
            value
        )
        for (key, value) in dafny_input.Key.items
    }
    if dafny_input.AttributeUpdates.is_Some:
        output["AttributeUpdates"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValueUpdate(
                value
            )
            for (key, value) in dafny_input.AttributeUpdates.value.items
        }

    if dafny_input.Expected.is_Some:
        output["Expected"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value
            )
            for (key, value) in dafny_input.Expected.value.items
        }

    if dafny_input.ConditionalOperator.is_Some:
        output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConditionalOperator(
                dafny_input.ConditionalOperator.value
            )
        )

    if dafny_input.ReturnValues.is_Some:
        output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnValue(
                dafny_input.ReturnValues.value
            )
        )

    if dafny_input.ReturnConsumedCapacity.is_Some:
        output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                dafny_input.ReturnConsumedCapacity.value
            )
        )

    if dafny_input.ReturnItemCollectionMetrics.is_Some:
        output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                dafny_input.ReturnItemCollectionMetrics.value
            )
        )

    if dafny_input.UpdateExpression.is_Some:
        output["UpdateExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.UpdateExpression.value
        ).decode("utf-16-be")

    if dafny_input.ConditionExpression.is_Some:
        output["ConditionExpression"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.ConditionExpression.value
        ).decode("utf-16-be")

    if dafny_input.ExpressionAttributeNames.is_Some:
        output["ExpressionAttributeNames"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key)
            .decode("utf-16-be"): b"".join(ord(c).to_bytes(2, "big") for c in value)
            .decode("utf-16-be")
            for (key, value) in dafny_input.ExpressionAttributeNames.value.items
        }

    if dafny_input.ExpressionAttributeValues.is_Some:
        output["ExpressionAttributeValues"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.ExpressionAttributeValues.value.items
        }

    return output


def com_amazonaws_dynamodb_UpdateItemOutput(dafny_input):
    output = {}
    if dafny_input.Attributes.is_Some:
        output["Attributes"] = {
            b"".join(ord(c).to_bytes(2, "big") for c in key).decode(
                "utf-16-be"
            ): aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeValue(
                value
            )
            for (key, value) in dafny_input.Attributes.value.items
        }

    if dafny_input.ConsumedCapacity.is_Some:
        output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ConsumedCapacity(
                dafny_input.ConsumedCapacity.value
            )
        )

    if dafny_input.ItemCollectionMetrics.is_Some:
        output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ItemCollectionMetrics(
                dafny_input.ItemCollectionMetrics.value
            )
        )

    return output


def com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(dafny_input):
    output = {}
    if dafny_input.Update.is_Some:
        output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(
                dafny_input.Update.value
            )
        )

    if dafny_input.Create.is_Some:
        output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(
                dafny_input.Create.value
            )
        )

    if dafny_input.Delete.is_Some:
        output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(
                dafny_input.Delete.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    output["ProvisionedThroughput"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
            dafny_input.ProvisionedThroughput
        )
    )
    return output


def com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_KeySchemaElement(
            list_element
        )
        for list_element in dafny_input.KeySchema
    ]
    output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_Projection(
            dafny_input.Projection
        )
    )
    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    return output


def com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ReplicationGroupUpdate(dafny_input):
    output = {}
    if dafny_input.Create.is_Some:
        output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(
                dafny_input.Create.value
            )
        )

    if dafny_input.Update.is_Some:
        output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(
                dafny_input.Update.value
            )
        )

    if dafny_input.Delete.is_Some:
        output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(
                dafny_input.Delete.value
            )
        )

    return output


def com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    if dafny_input.KMSMasterKeyId.is_Some:
        output["KMSMasterKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KMSMasterKeyId.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.TableClassOverride.is_Some:
        output["TableClassOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.TableClassOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    if dafny_input.KMSMasterKeyId.is_Some:
        output["KMSMasterKeyId"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.KMSMasterKeyId.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    if dafny_input.GlobalSecondaryIndexes.is_Some:
        output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexes.value
        ]

    if dafny_input.TableClassOverride.is_Some:
        output["TableClassOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.TableClassOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(dafny_input):
    output = {}
    output["IndexName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.IndexName
    ).decode("utf-16-be")
    if dafny_input.ProvisionedThroughputOverride.is_Some:
        output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                dafny_input.ProvisionedThroughputOverride.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateTableInput(dafny_input):
    output = {}
    if dafny_input.AttributeDefinitions.is_Some:
        output["AttributeDefinitions"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AttributeDefinition(
                list_element
            )
            for list_element in dafny_input.AttributeDefinitions.value
        ]

    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.BillingMode.is_Some:
        output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_BillingMode(
                dafny_input.BillingMode.value
            )
        )

    if dafny_input.ProvisionedThroughput.is_Some:
        output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ProvisionedThroughput(
                dafny_input.ProvisionedThroughput.value
            )
        )

    if dafny_input.GlobalSecondaryIndexUpdates.is_Some:
        output["GlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexUpdates.value
        ]

    if dafny_input.StreamSpecification.is_Some:
        output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_StreamSpecification(
                dafny_input.StreamSpecification.value
            )
        )

    if dafny_input.SSESpecification.is_Some:
        output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_SSESpecification(
                dafny_input.SSESpecification.value
            )
        )

    if dafny_input.ReplicaUpdates.is_Some:
        output["ReplicaUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicationGroupUpdate(
                list_element
            )
            for list_element in dafny_input.ReplicaUpdates.value
        ]

    if dafny_input.TableClass.is_Some:
        output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableClass(
                dafny_input.TableClass.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateTableOutput(dafny_input):
    output = {}
    if dafny_input.TableDescription.is_Some:
        output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableDescription(
                dafny_input.TableDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedWriteCapacityAutoScalingUpdate.is_Some:
        output["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ProvisionedWriteCapacityAutoScalingUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(dafny_input):
    output = {}
    output["RegionName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.RegionName
    ).decode("utf-16-be")
    if dafny_input.ReplicaGlobalSecondaryIndexUpdates.is_Some:
        output["ReplicaGlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(
                list_element
            )
            for list_element in dafny_input.ReplicaGlobalSecondaryIndexUpdates.value
        ]

    if dafny_input.ReplicaProvisionedReadCapacityAutoScalingUpdate.is_Some:
        output["ReplicaProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ReplicaProvisionedReadCapacityAutoScalingUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(dafny_input):
    output = {}
    if dafny_input.IndexName.is_Some:
        output["IndexName"] = b"".join(
            ord(c).to_bytes(2, "big") for c in dafny_input.IndexName.value
        ).decode("utf-16-be")

    if dafny_input.ProvisionedReadCapacityAutoScalingUpdate.is_Some:
        output["ProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ProvisionedReadCapacityAutoScalingUpdate.value
            )
        )

    return output


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingInput(dafny_input):
    output = {}
    if dafny_input.GlobalSecondaryIndexUpdates.is_Some:
        output["GlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(
                list_element
            )
            for list_element in dafny_input.GlobalSecondaryIndexUpdates.value
        ]

    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    if dafny_input.ProvisionedWriteCapacityAutoScalingUpdate.is_Some:
        output["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                dafny_input.ProvisionedWriteCapacityAutoScalingUpdate.value
            )
        )

    if dafny_input.ReplicaUpdates.is_Some:
        output["ReplicaUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(
                list_element
            )
            for list_element in dafny_input.ReplicaUpdates.value
        ]

    return output


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingOutput(dafny_input):
    output = {}
    if dafny_input.TableAutoScalingDescription.is_Some:
        output["TableAutoScalingDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TableAutoScalingDescription(
                dafny_input.TableAutoScalingDescription.value
            )
        )

    return output


def com_amazonaws_dynamodb_TimeToLiveSpecification(dafny_input):
    output = {}
    output["Enabled"] = dafny_input.Enabled
    output["AttributeName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.AttributeName
    ).decode("utf-16-be")
    return output


def com_amazonaws_dynamodb_UpdateTimeToLiveInput(dafny_input):
    output = {}
    output["TableName"] = b"".join(
        ord(c).to_bytes(2, "big") for c in dafny_input.TableName
    ).decode("utf-16-be")
    output["TimeToLiveSpecification"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TimeToLiveSpecification(
            dafny_input.TimeToLiveSpecification
        )
    )
    return output


def com_amazonaws_dynamodb_UpdateTimeToLiveOutput(dafny_input):
    output = {}
    if dafny_input.TimeToLiveSpecification.is_Some:
        output["TimeToLiveSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.dafny_to_aws_sdk.com_amazonaws_dynamodb_TimeToLiveSpecification(
                dafny_input.TimeToLiveSpecification.value
            )
        )

    return output
