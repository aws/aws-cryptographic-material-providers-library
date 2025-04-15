# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

import aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter
from copy import deepcopy


def com_amazonaws_dynamodb_BatchExecuteStatementInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Statements"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchStatementRequest(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["Statements"]
    ]
    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_BatchStatementRequest(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Statement"] = this_structure["Statement"]
    if "Parameters" in this_structure:
        transformed_output["Parameters"] = [
            item_handler(list_element) for list_element in this_structure["Parameters"]
        ]

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReturnConsumedCapacity(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_BatchExecuteStatementOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Responses" in this_structure:
        transformed_output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchStatementResponse(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Responses"]
        ]

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_BatchStatementResponse(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Error" in this_structure:
        transformed_output["Error"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchStatementError(
                this_structure["Error"], item_handler, condition_handler
            )
        )

    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "Item" in this_structure:
        transformed_output["Item"] = {
            key: item_handler(value) for (key, value) in this_structure["Item"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_ConsumedCapacity(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "CapacityUnits" in this_structure:
        transformed_output["CapacityUnits"] = this_structure["CapacityUnits"]

    if "ReadCapacityUnits" in this_structure:
        transformed_output["ReadCapacityUnits"] = this_structure["ReadCapacityUnits"]

    if "WriteCapacityUnits" in this_structure:
        transformed_output["WriteCapacityUnits"] = this_structure["WriteCapacityUnits"]

    if "Table" in this_structure:
        transformed_output["Table"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Capacity(
                this_structure["Table"], item_handler, condition_handler
            )
        )

    if "LocalSecondaryIndexes" in this_structure:
        transformed_output["LocalSecondaryIndexes"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Capacity(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["LocalSecondaryIndexes"].items()
        }

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Capacity(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["GlobalSecondaryIndexes"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_BatchStatementError(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Code" in this_structure:
        transformed_output["Code"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(
                this_structure["Code"], item_handler, condition_handler
            )
        )

    if "Message" in this_structure:
        transformed_output["Message"] = this_structure["Message"]

    if "Item" in this_structure:
        transformed_output["Item"] = {
            key: item_handler(value) for (key, value) in this_structure["Item"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_Capacity(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "ReadCapacityUnits" in this_structure:
        transformed_output["ReadCapacityUnits"] = this_structure["ReadCapacityUnits"]

    if "WriteCapacityUnits" in this_structure:
        transformed_output["WriteCapacityUnits"] = this_structure["WriteCapacityUnits"]

    if "CapacityUnits" in this_structure:
        transformed_output["CapacityUnits"] = this_structure["CapacityUnits"]

    return transformed_output


def com_amazonaws_dynamodb_BatchStatementErrorCodeEnum(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_BatchGetItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RequestItems"] = {
        key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeysAndAttributes(
            value, item_handler, condition_handler
        )
        for (key, value) in this_structure["RequestItems"].items()
    }
    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_KeysAndAttributes(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Keys"] = [
        {key: item_handler(value) for (key, value) in list_element.items()}
        for list_element in this_structure["Keys"]
    ]
    if "AttributesToGet" in this_structure:
        transformed_output["AttributesToGet"] = [
            list_element for list_element in this_structure["AttributesToGet"]
        ]

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    if "ProjectionExpression" in this_structure:
        transformed_output["ProjectionExpression"] = this_structure[
            "ProjectionExpression"
        ]

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_BatchGetItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Responses" in this_structure:
        transformed_output["Responses"] = {
            key: [
                {key: item_handler(value) for (key, value) in list_element.items()}
                for list_element in value
            ]
            for (key, value) in this_structure["Responses"].items()
        }

    if "UnprocessedKeys" in this_structure:
        transformed_output["UnprocessedKeys"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeysAndAttributes(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["UnprocessedKeys"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_BatchWriteItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RequestItems"] = {
        key: [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_WriteRequest(
                list_element, item_handler, condition_handler
            )
            for list_element in value
        ]
        for (key, value) in this_structure["RequestItems"].items()
    }
    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ReturnItemCollectionMetrics" in this_structure:
        transformed_output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                this_structure["ReturnItemCollectionMetrics"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_WriteRequest(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "PutRequest" in this_structure:
        transformed_output["PutRequest"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PutRequest(
                this_structure["PutRequest"], item_handler, condition_handler
            )
        )

    if "DeleteRequest" in this_structure:
        transformed_output["DeleteRequest"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteRequest(
                this_structure["DeleteRequest"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_PutRequest(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Item"] = {
        key: item_handler(value) for (key, value) in this_structure["Item"].items()
    }
    return transformed_output


def com_amazonaws_dynamodb_DeleteRequest(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    return transformed_output


def com_amazonaws_dynamodb_BatchWriteItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "UnprocessedItems" in this_structure:
        transformed_output["UnprocessedItems"] = {
            key: [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_WriteRequest(
                    list_element, item_handler, condition_handler
                )
                for list_element in value
            ]
            for (key, value) in this_structure["UnprocessedItems"].items()
        }

    if "ItemCollectionMetrics" in this_structure:
        transformed_output["ItemCollectionMetrics"] = {
            key: [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    list_element, item_handler, condition_handler
                )
                for list_element in value
            ]
            for (key, value) in this_structure["ItemCollectionMetrics"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ItemCollectionMetrics(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ItemCollectionKey" in this_structure:
        transformed_output["ItemCollectionKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ItemCollectionKey"].items()
        }

    if "SizeEstimateRangeGB" in this_structure:
        transformed_output["SizeEstimateRangeGB"] = [
            list_element for list_element in this_structure["SizeEstimateRangeGB"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_CreateBackupInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["BackupName"] = this_structure["BackupName"]
    return transformed_output


def com_amazonaws_dynamodb_CreateBackupOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BackupDetails" in this_structure:
        transformed_output["BackupDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupDetails(
                this_structure["BackupDetails"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_BackupDetails(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["BackupArn"] = this_structure["BackupArn"]
    transformed_output["BackupName"] = this_structure["BackupName"]
    if "BackupSizeBytes" in this_structure:
        transformed_output["BackupSizeBytes"] = this_structure["BackupSizeBytes"]

    transformed_output["BackupStatus"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupStatus(
            this_structure["BackupStatus"], item_handler, condition_handler
        )
    )
    transformed_output["BackupType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupType(
            this_structure["BackupType"], item_handler, condition_handler
        )
    )
    transformed_output["BackupCreationDateTime"] = this_structure[
        "BackupCreationDateTime"
    ]
    if "BackupExpiryDateTime" in this_structure:
        transformed_output["BackupExpiryDateTime"] = this_structure[
            "BackupExpiryDateTime"
        ]

    return transformed_output


def com_amazonaws_dynamodb_BackupStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_BackupType(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_CreateGlobalTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]
    transformed_output["ReplicationGroup"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Replica(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["ReplicationGroup"]
    ]
    return transformed_output


def com_amazonaws_dynamodb_Replica(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "RegionName" in this_structure:
        transformed_output["RegionName"] = this_structure["RegionName"]

    return transformed_output


def com_amazonaws_dynamodb_CreateGlobalTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableDescription" in this_structure:
        transformed_output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTableDescription(
                this_structure["GlobalTableDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GlobalTableDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ReplicationGroup" in this_structure:
        transformed_output["ReplicationGroup"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicationGroup"]
        ]

    if "GlobalTableArn" in this_structure:
        transformed_output["GlobalTableArn"] = this_structure["GlobalTableArn"]

    if "CreationDateTime" in this_structure:
        transformed_output["CreationDateTime"] = this_structure["CreationDateTime"]

    if "GlobalTableStatus" in this_structure:
        transformed_output["GlobalTableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTableStatus(
                this_structure["GlobalTableStatus"], item_handler, condition_handler
            )
        )

    if "GlobalTableName" in this_structure:
        transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]

    return transformed_output


def com_amazonaws_dynamodb_ReplicaDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "RegionName" in this_structure:
        transformed_output["RegionName"] = this_structure["RegionName"]

    if "ReplicaStatus" in this_structure:
        transformed_output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaStatus(
                this_structure["ReplicaStatus"], item_handler, condition_handler
            )
        )

    if "ReplicaStatusDescription" in this_structure:
        transformed_output["ReplicaStatusDescription"] = this_structure[
            "ReplicaStatusDescription"
        ]

    if "ReplicaStatusPercentProgress" in this_structure:
        transformed_output["ReplicaStatusPercentProgress"] = this_structure[
            "ReplicaStatusPercentProgress"
        ]

    if "KMSMasterKeyId" in this_structure:
        transformed_output["KMSMasterKeyId"] = this_structure["KMSMasterKeyId"]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughputOverride(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "ReplicaInaccessibleDateTime" in this_structure:
        transformed_output["ReplicaInaccessibleDateTime"] = this_structure[
            "ReplicaInaccessibleDateTime"
        ]

    if "ReplicaTableClassSummary" in this_structure:
        transformed_output["ReplicaTableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClassSummary(
                this_structure["ReplicaTableClassSummary"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GlobalTableStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ReplicaStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ProvisionedThroughputOverride(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ReadCapacityUnits" in this_structure:
        transformed_output["ReadCapacityUnits"] = this_structure["ReadCapacityUnits"]

    return transformed_output


def com_amazonaws_dynamodb_OnDemandThroughputOverride(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "MaxReadRequestUnits" in this_structure:
        transformed_output["MaxReadRequestUnits"] = this_structure[
            "MaxReadRequestUnits"
        ]

    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughputOverride(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TableClassSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableClass" in this_structure:
        transformed_output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["TableClass"], item_handler, condition_handler
            )
        )

    if "LastUpdateDateTime" in this_structure:
        transformed_output["LastUpdateDateTime"] = this_structure["LastUpdateDateTime"]

    return transformed_output


def com_amazonaws_dynamodb_TableClass(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_CreateTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["AttributeDefinitions"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeDefinition(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["AttributeDefinitions"]
    ]
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    if "LocalSecondaryIndexes" in this_structure:
        transformed_output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["LocalSecondaryIndexes"]
        ]

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "BillingMode" in this_structure:
        transformed_output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingMode"], item_handler, condition_handler
            )
        )

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "StreamSpecification" in this_structure:
        transformed_output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_StreamSpecification(
                this_structure["StreamSpecification"], item_handler, condition_handler
            )
        )

    if "SSESpecification" in this_structure:
        transformed_output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSESpecification(
                this_structure["SSESpecification"], item_handler, condition_handler
            )
        )

    if "Tags" in this_structure:
        transformed_output["Tags"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Tag(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Tags"]
        ]

    if "TableClass" in this_structure:
        transformed_output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["TableClass"], item_handler, condition_handler
            )
        )

    if "DeletionProtectionEnabled" in this_structure:
        transformed_output["DeletionProtectionEnabled"] = this_structure[
            "DeletionProtectionEnabled"
        ]

    if "ResourcePolicy" in this_structure:
        transformed_output["ResourcePolicy"] = this_structure["ResourcePolicy"]

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AttributeDefinition(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["AttributeName"] = this_structure["AttributeName"]
    transformed_output["AttributeType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ScalarAttributeType(
            this_structure["AttributeType"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_KeySchemaElement(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["AttributeName"] = this_structure["AttributeName"]
    transformed_output["KeyType"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeyType(
            this_structure["KeyType"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_LocalSecondaryIndex(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    transformed_output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
            this_structure["Projection"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_GlobalSecondaryIndex(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    transformed_output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
            this_structure["Projection"], item_handler, condition_handler
        )
    )
    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_BillingMode(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ProvisionedThroughput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ReadCapacityUnits"] = this_structure["ReadCapacityUnits"]
    transformed_output["WriteCapacityUnits"] = this_structure["WriteCapacityUnits"]
    return transformed_output


def com_amazonaws_dynamodb_StreamSpecification(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["StreamEnabled"] = this_structure["StreamEnabled"]
    if "StreamViewType" in this_structure:
        transformed_output["StreamViewType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_StreamViewType(
                this_structure["StreamViewType"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_SSESpecification(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Enabled" in this_structure:
        transformed_output["Enabled"] = this_structure["Enabled"]

    if "SSEType" in this_structure:
        transformed_output["SSEType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSEType(
                this_structure["SSEType"], item_handler, condition_handler
            )
        )

    if "KMSMasterKeyId" in this_structure:
        transformed_output["KMSMasterKeyId"] = this_structure["KMSMasterKeyId"]

    return transformed_output


def com_amazonaws_dynamodb_Tag(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = this_structure["Key"]
    transformed_output["Value"] = this_structure["Value"]
    return transformed_output


def com_amazonaws_dynamodb_OnDemandThroughput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "MaxReadRequestUnits" in this_structure:
        transformed_output["MaxReadRequestUnits"] = this_structure[
            "MaxReadRequestUnits"
        ]

    if "MaxWriteRequestUnits" in this_structure:
        transformed_output["MaxWriteRequestUnits"] = this_structure[
            "MaxWriteRequestUnits"
        ]

    return transformed_output


def com_amazonaws_dynamodb_ScalarAttributeType(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_KeyType(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_Projection(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "ProjectionType" in this_structure:
        transformed_output["ProjectionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProjectionType(
                this_structure["ProjectionType"], item_handler, condition_handler
            )
        )

    if "NonKeyAttributes" in this_structure:
        transformed_output["NonKeyAttributes"] = [
            list_element for list_element in this_structure["NonKeyAttributes"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_StreamViewType(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_SSEType(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ProjectionType(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_CreateTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableDescription" in this_structure:
        transformed_output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["TableDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TableDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "AttributeDefinitions" in this_structure:
        transformed_output["AttributeDefinitions"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeDefinition(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["AttributeDefinitions"]
        ]

    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "KeySchema" in this_structure:
        transformed_output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KeySchema"]
        ]

    if "TableStatus" in this_structure:
        transformed_output["TableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableStatus(
                this_structure["TableStatus"], item_handler, condition_handler
            )
        )

    if "CreationDateTime" in this_structure:
        transformed_output["CreationDateTime"] = this_structure["CreationDateTime"]

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "TableSizeBytes" in this_structure:
        transformed_output["TableSizeBytes"] = this_structure["TableSizeBytes"]

    if "ItemCount" in this_structure:
        transformed_output["ItemCount"] = this_structure["ItemCount"]

    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "TableId" in this_structure:
        transformed_output["TableId"] = this_structure["TableId"]

    if "BillingModeSummary" in this_structure:
        transformed_output["BillingModeSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingModeSummary(
                this_structure["BillingModeSummary"], item_handler, condition_handler
            )
        )

    if "LocalSecondaryIndexes" in this_structure:
        transformed_output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_LocalSecondaryIndexDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["LocalSecondaryIndexes"]
        ]

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "StreamSpecification" in this_structure:
        transformed_output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_StreamSpecification(
                this_structure["StreamSpecification"], item_handler, condition_handler
            )
        )

    if "LatestStreamLabel" in this_structure:
        transformed_output["LatestStreamLabel"] = this_structure["LatestStreamLabel"]

    if "LatestStreamArn" in this_structure:
        transformed_output["LatestStreamArn"] = this_structure["LatestStreamArn"]

    if "GlobalTableVersion" in this_structure:
        transformed_output["GlobalTableVersion"] = this_structure["GlobalTableVersion"]

    if "Replicas" in this_structure:
        transformed_output["Replicas"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Replicas"]
        ]

    if "RestoreSummary" in this_structure:
        transformed_output["RestoreSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_RestoreSummary(
                this_structure["RestoreSummary"], item_handler, condition_handler
            )
        )

    if "SSEDescription" in this_structure:
        transformed_output["SSEDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSEDescription(
                this_structure["SSEDescription"], item_handler, condition_handler
            )
        )

    if "ArchivalSummary" in this_structure:
        transformed_output["ArchivalSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ArchivalSummary(
                this_structure["ArchivalSummary"], item_handler, condition_handler
            )
        )

    if "TableClassSummary" in this_structure:
        transformed_output["TableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClassSummary(
                this_structure["TableClassSummary"], item_handler, condition_handler
            )
        )

    if "DeletionProtectionEnabled" in this_structure:
        transformed_output["DeletionProtectionEnabled"] = this_structure[
            "DeletionProtectionEnabled"
        ]

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TableStatus(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ProvisionedThroughputDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "LastIncreaseDateTime" in this_structure:
        transformed_output["LastIncreaseDateTime"] = this_structure[
            "LastIncreaseDateTime"
        ]

    if "LastDecreaseDateTime" in this_structure:
        transformed_output["LastDecreaseDateTime"] = this_structure[
            "LastDecreaseDateTime"
        ]

    if "NumberOfDecreasesToday" in this_structure:
        transformed_output["NumberOfDecreasesToday"] = this_structure[
            "NumberOfDecreasesToday"
        ]

    if "ReadCapacityUnits" in this_structure:
        transformed_output["ReadCapacityUnits"] = this_structure["ReadCapacityUnits"]

    if "WriteCapacityUnits" in this_structure:
        transformed_output["WriteCapacityUnits"] = this_structure["WriteCapacityUnits"]

    return transformed_output


def com_amazonaws_dynamodb_BillingModeSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BillingMode" in this_structure:
        transformed_output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingMode"], item_handler, condition_handler
            )
        )

    if "LastUpdateToPayPerRequestDateTime" in this_structure:
        transformed_output["LastUpdateToPayPerRequestDateTime"] = this_structure[
            "LastUpdateToPayPerRequestDateTime"
        ]

    return transformed_output


def com_amazonaws_dynamodb_LocalSecondaryIndexDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "KeySchema" in this_structure:
        transformed_output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KeySchema"]
        ]

    if "Projection" in this_structure:
        transformed_output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
                this_structure["Projection"], item_handler, condition_handler
            )
        )

    if "IndexSizeBytes" in this_structure:
        transformed_output["IndexSizeBytes"] = this_structure["IndexSizeBytes"]

    if "ItemCount" in this_structure:
        transformed_output["ItemCount"] = this_structure["ItemCount"]

    if "IndexArn" in this_structure:
        transformed_output["IndexArn"] = this_structure["IndexArn"]

    return transformed_output


def com_amazonaws_dynamodb_GlobalSecondaryIndexDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "KeySchema" in this_structure:
        transformed_output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KeySchema"]
        ]

    if "Projection" in this_structure:
        transformed_output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
                this_structure["Projection"], item_handler, condition_handler
            )
        )

    if "IndexStatus" in this_structure:
        transformed_output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_IndexStatus(
                this_structure["IndexStatus"], item_handler, condition_handler
            )
        )

    if "Backfilling" in this_structure:
        transformed_output["Backfilling"] = this_structure["Backfilling"]

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputDescription(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "IndexSizeBytes" in this_structure:
        transformed_output["IndexSizeBytes"] = this_structure["IndexSizeBytes"]

    if "ItemCount" in this_structure:
        transformed_output["ItemCount"] = this_structure["ItemCount"]

    if "IndexArn" in this_structure:
        transformed_output["IndexArn"] = this_structure["IndexArn"]

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_RestoreSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "SourceBackupArn" in this_structure:
        transformed_output["SourceBackupArn"] = this_structure["SourceBackupArn"]

    if "SourceTableArn" in this_structure:
        transformed_output["SourceTableArn"] = this_structure["SourceTableArn"]

    transformed_output["RestoreDateTime"] = this_structure["RestoreDateTime"]
    transformed_output["RestoreInProgress"] = this_structure["RestoreInProgress"]
    return transformed_output


def com_amazonaws_dynamodb_SSEDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Status" in this_structure:
        transformed_output["Status"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSEStatus(
                this_structure["Status"], item_handler, condition_handler
            )
        )

    if "SSEType" in this_structure:
        transformed_output["SSEType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSEType(
                this_structure["SSEType"], item_handler, condition_handler
            )
        )

    if "KMSMasterKeyArn" in this_structure:
        transformed_output["KMSMasterKeyArn"] = this_structure["KMSMasterKeyArn"]

    if "InaccessibleEncryptionDateTime" in this_structure:
        transformed_output["InaccessibleEncryptionDateTime"] = this_structure[
            "InaccessibleEncryptionDateTime"
        ]

    return transformed_output


def com_amazonaws_dynamodb_ArchivalSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ArchivalDateTime" in this_structure:
        transformed_output["ArchivalDateTime"] = this_structure["ArchivalDateTime"]

    if "ArchivalReason" in this_structure:
        transformed_output["ArchivalReason"] = this_structure["ArchivalReason"]

    if "ArchivalBackupArn" in this_structure:
        transformed_output["ArchivalBackupArn"] = this_structure["ArchivalBackupArn"]

    return transformed_output


def com_amazonaws_dynamodb_IndexStatus(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_SSEStatus(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DeleteBackupInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["BackupArn"] = this_structure["BackupArn"]
    return transformed_output


def com_amazonaws_dynamodb_DeleteBackupOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BackupDescription" in this_structure:
        transformed_output["BackupDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupDescription(
                this_structure["BackupDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_BackupDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BackupDetails" in this_structure:
        transformed_output["BackupDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupDetails(
                this_structure["BackupDetails"], item_handler, condition_handler
            )
        )

    if "SourceTableDetails" in this_structure:
        transformed_output["SourceTableDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SourceTableDetails(
                this_structure["SourceTableDetails"], item_handler, condition_handler
            )
        )

    if "SourceTableFeatureDetails" in this_structure:
        transformed_output["SourceTableFeatureDetails"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SourceTableFeatureDetails(
                this_structure["SourceTableFeatureDetails"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_SourceTableDetails(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["TableId"] = this_structure["TableId"]
    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "TableSizeBytes" in this_structure:
        transformed_output["TableSizeBytes"] = this_structure["TableSizeBytes"]

    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    transformed_output["TableCreationDateTime"] = this_structure[
        "TableCreationDateTime"
    ]
    transformed_output["ProvisionedThroughput"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
            this_structure["ProvisionedThroughput"], item_handler, condition_handler
        )
    )
    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    if "ItemCount" in this_structure:
        transformed_output["ItemCount"] = this_structure["ItemCount"]

    if "BillingMode" in this_structure:
        transformed_output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingMode"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_SourceTableFeatureDetails(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "LocalSecondaryIndexes" in this_structure:
        transformed_output["LocalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_LocalSecondaryIndexInfo(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["LocalSecondaryIndexes"]
        ]

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "StreamDescription" in this_structure:
        transformed_output["StreamDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_StreamSpecification(
                this_structure["StreamDescription"], item_handler, condition_handler
            )
        )

    if "TimeToLiveDescription" in this_structure:
        transformed_output["TimeToLiveDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TimeToLiveDescription(
                this_structure["TimeToLiveDescription"], item_handler, condition_handler
            )
        )

    if "SSEDescription" in this_structure:
        transformed_output["SSEDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSEDescription(
                this_structure["SSEDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_LocalSecondaryIndexInfo(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "KeySchema" in this_structure:
        transformed_output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KeySchema"]
        ]

    if "Projection" in this_structure:
        transformed_output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
                this_structure["Projection"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GlobalSecondaryIndexInfo(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "KeySchema" in this_structure:
        transformed_output["KeySchema"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KeySchema"]
        ]

    if "Projection" in this_structure:
        transformed_output["Projection"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
                this_structure["Projection"], item_handler, condition_handler
            )
        )

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TimeToLiveDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TimeToLiveStatus" in this_structure:
        transformed_output["TimeToLiveStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TimeToLiveStatus(
                this_structure["TimeToLiveStatus"], item_handler, condition_handler
            )
        )

    if "AttributeName" in this_structure:
        transformed_output["AttributeName"] = this_structure["AttributeName"]

    return transformed_output


def com_amazonaws_dynamodb_TimeToLiveStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DeleteItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    if "Expected" in this_structure:
        transformed_output["Expected"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["Expected"].items()
        }

    if "ConditionalOperator" in this_structure:
        transformed_output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionalOperator(
                this_structure["ConditionalOperator"], item_handler, condition_handler
            )
        )

    if "ReturnValues" in this_structure:
        transformed_output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValue(
                this_structure["ReturnValues"], item_handler, condition_handler
            )
        )

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ReturnItemCollectionMetrics" in this_structure:
        transformed_output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                this_structure["ReturnItemCollectionMetrics"],
                item_handler,
                condition_handler,
            )
        )

    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExpectedAttributeValue(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Value" in this_structure:
        transformed_output["Value"] = item_handler(this_structure["Value"])

    if "Exists" in this_structure:
        transformed_output["Exists"] = this_structure["Exists"]

    if "ComparisonOperator" in this_structure:
        transformed_output["ComparisonOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ComparisonOperator(
                this_structure["ComparisonOperator"], item_handler, condition_handler
            )
        )

    if "AttributeValueList" in this_structure:
        transformed_output["AttributeValueList"] = [
            item_handler(list_element)
            for list_element in this_structure["AttributeValueList"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ConditionalOperator(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ReturnValue(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ComparisonOperator(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DeleteItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Attributes" in this_structure:
        transformed_output["Attributes"] = {
            key: item_handler(value)
            for (key, value) in this_structure["Attributes"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    if "ItemCollectionMetrics" in this_structure:
        transformed_output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemCollectionMetrics(
                this_structure["ItemCollectionMetrics"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DeleteResourcePolicyInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    if "ExpectedRevisionId" in this_structure:
        transformed_output["ExpectedRevisionId"] = this_structure["ExpectedRevisionId"]

    return transformed_output


def com_amazonaws_dynamodb_DeleteResourcePolicyOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "RevisionId" in this_structure:
        transformed_output["RevisionId"] = this_structure["RevisionId"]

    return transformed_output


def com_amazonaws_dynamodb_DeleteTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DeleteTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableDescription" in this_structure:
        transformed_output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["TableDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DescribeBackupInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["BackupArn"] = this_structure["BackupArn"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeBackupOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BackupDescription" in this_structure:
        transformed_output["BackupDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupDescription(
                this_structure["BackupDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DescribeContinuousBackupsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeContinuousBackupsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ContinuousBackupsDescription" in this_structure:
        transformed_output["ContinuousBackupsDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                this_structure["ContinuousBackupsDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ContinuousBackupsDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ContinuousBackupsStatus"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContinuousBackupsStatus(
            this_structure["ContinuousBackupsStatus"], item_handler, condition_handler
        )
    )
    if "PointInTimeRecoveryDescription" in this_structure:
        transformed_output["PointInTimeRecoveryDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PointInTimeRecoveryDescription(
                this_structure["PointInTimeRecoveryDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ContinuousBackupsStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_PointInTimeRecoveryDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "PointInTimeRecoveryStatus" in this_structure:
        transformed_output["PointInTimeRecoveryStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PointInTimeRecoveryStatus(
                this_structure["PointInTimeRecoveryStatus"],
                item_handler,
                condition_handler,
            )
        )

    if "EarliestRestorableDateTime" in this_structure:
        transformed_output["EarliestRestorableDateTime"] = this_structure[
            "EarliestRestorableDateTime"
        ]

    if "LatestRestorableDateTime" in this_structure:
        transformed_output["LatestRestorableDateTime"] = this_structure[
            "LatestRestorableDateTime"
        ]

    return transformed_output


def com_amazonaws_dynamodb_PointInTimeRecoveryStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DescribeContributorInsightsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    return transformed_output


def com_amazonaws_dynamodb_DescribeContributorInsightsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ContributorInsightsRuleList" in this_structure:
        transformed_output["ContributorInsightsRuleList"] = [
            list_element
            for list_element in this_structure["ContributorInsightsRuleList"]
        ]

    if "ContributorInsightsStatus" in this_structure:
        transformed_output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContributorInsightsStatus(
                this_structure["ContributorInsightsStatus"],
                item_handler,
                condition_handler,
            )
        )

    if "LastUpdateDateTime" in this_structure:
        transformed_output["LastUpdateDateTime"] = this_structure["LastUpdateDateTime"]

    if "FailureException" in this_structure:
        transformed_output["FailureException"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_FailureException(
                this_structure["FailureException"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ContributorInsightsStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_FailureException(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExceptionName" in this_structure:
        transformed_output["ExceptionName"] = this_structure["ExceptionName"]

    if "ExceptionDescription" in this_structure:
        transformed_output["ExceptionDescription"] = this_structure[
            "ExceptionDescription"
        ]

    return transformed_output


def com_amazonaws_dynamodb_DescribeEndpointsRequest(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    return transformed_output


def com_amazonaws_dynamodb_DescribeEndpointsResponse(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Endpoints"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Endpoint(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["Endpoints"]
    ]
    return transformed_output


def com_amazonaws_dynamodb_Endpoint(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Address"] = this_structure["Address"]
    transformed_output["CachePeriodInMinutes"] = this_structure["CachePeriodInMinutes"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeExportInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ExportArn"] = this_structure["ExportArn"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeExportOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportDescription" in this_structure:
        transformed_output["ExportDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportDescription(
                this_structure["ExportDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExportDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportArn" in this_structure:
        transformed_output["ExportArn"] = this_structure["ExportArn"]

    if "ExportStatus" in this_structure:
        transformed_output["ExportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportStatus(
                this_structure["ExportStatus"], item_handler, condition_handler
            )
        )

    if "StartTime" in this_structure:
        transformed_output["StartTime"] = this_structure["StartTime"]

    if "EndTime" in this_structure:
        transformed_output["EndTime"] = this_structure["EndTime"]

    if "ExportManifest" in this_structure:
        transformed_output["ExportManifest"] = this_structure["ExportManifest"]

    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "TableId" in this_structure:
        transformed_output["TableId"] = this_structure["TableId"]

    if "ExportTime" in this_structure:
        transformed_output["ExportTime"] = this_structure["ExportTime"]

    if "ClientToken" in this_structure:
        transformed_output["ClientToken"] = this_structure["ClientToken"]

    if "S3Bucket" in this_structure:
        transformed_output["S3Bucket"] = this_structure["S3Bucket"]

    if "S3BucketOwner" in this_structure:
        transformed_output["S3BucketOwner"] = this_structure["S3BucketOwner"]

    if "S3Prefix" in this_structure:
        transformed_output["S3Prefix"] = this_structure["S3Prefix"]

    if "S3SseAlgorithm" in this_structure:
        transformed_output["S3SseAlgorithm"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_S3SseAlgorithm(
                this_structure["S3SseAlgorithm"], item_handler, condition_handler
            )
        )

    if "S3SseKmsKeyId" in this_structure:
        transformed_output["S3SseKmsKeyId"] = this_structure["S3SseKmsKeyId"]

    if "FailureCode" in this_structure:
        transformed_output["FailureCode"] = this_structure["FailureCode"]

    if "FailureMessage" in this_structure:
        transformed_output["FailureMessage"] = this_structure["FailureMessage"]

    if "ExportFormat" in this_structure:
        transformed_output["ExportFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportFormat(
                this_structure["ExportFormat"], item_handler, condition_handler
            )
        )

    if "BilledSizeBytes" in this_structure:
        transformed_output["BilledSizeBytes"] = this_structure["BilledSizeBytes"]

    if "ItemCount" in this_structure:
        transformed_output["ItemCount"] = this_structure["ItemCount"]

    if "ExportType" in this_structure:
        transformed_output["ExportType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportType(
                this_structure["ExportType"], item_handler, condition_handler
            )
        )

    if "IncrementalExportSpecification" in this_structure:
        transformed_output["IncrementalExportSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_IncrementalExportSpecification(
                this_structure["IncrementalExportSpecification"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExportStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_S3SseAlgorithm(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ExportFormat(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ExportType(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_IncrementalExportSpecification(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportFromTime" in this_structure:
        transformed_output["ExportFromTime"] = this_structure["ExportFromTime"]

    if "ExportToTime" in this_structure:
        transformed_output["ExportToTime"] = this_structure["ExportToTime"]

    if "ExportViewType" in this_structure:
        transformed_output["ExportViewType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportViewType(
                this_structure["ExportViewType"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExportViewType(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DescribeGlobalTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeGlobalTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableDescription" in this_structure:
        transformed_output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTableDescription(
                this_structure["GlobalTableDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeGlobalTableSettingsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableName" in this_structure:
        transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]

    if "ReplicaSettings" in this_structure:
        transformed_output["ReplicaSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaSettings"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ReplicaSettingsDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    if "ReplicaStatus" in this_structure:
        transformed_output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaStatus(
                this_structure["ReplicaStatus"], item_handler, condition_handler
            )
        )

    if "ReplicaBillingModeSummary" in this_structure:
        transformed_output["ReplicaBillingModeSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingModeSummary(
                this_structure["ReplicaBillingModeSummary"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaProvisionedReadCapacityUnits" in this_structure:
        transformed_output["ReplicaProvisionedReadCapacityUnits"] = this_structure[
            "ReplicaProvisionedReadCapacityUnits"
        ]

    if "ReplicaProvisionedReadCapacityAutoScalingSettings" in this_structure:
        transformed_output["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ReplicaProvisionedReadCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaProvisionedWriteCapacityUnits" in this_structure:
        transformed_output["ReplicaProvisionedWriteCapacityUnits"] = this_structure[
            "ReplicaProvisionedWriteCapacityUnits"
        ]

    if "ReplicaProvisionedWriteCapacityAutoScalingSettings" in this_structure:
        transformed_output["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ReplicaProvisionedWriteCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaGlobalSecondaryIndexSettings" in this_structure:
        transformed_output["ReplicaGlobalSecondaryIndexSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaGlobalSecondaryIndexSettings"]
        ]

    if "ReplicaTableClassSummary" in this_structure:
        transformed_output["ReplicaTableClassSummary"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClassSummary(
                this_structure["ReplicaTableClassSummary"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingSettingsDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "MinimumUnits" in this_structure:
        transformed_output["MinimumUnits"] = this_structure["MinimumUnits"]

    if "MaximumUnits" in this_structure:
        transformed_output["MaximumUnits"] = this_structure["MaximumUnits"]

    if "AutoScalingDisabled" in this_structure:
        transformed_output["AutoScalingDisabled"] = this_structure[
            "AutoScalingDisabled"
        ]

    if "AutoScalingRoleArn" in this_structure:
        transformed_output["AutoScalingRoleArn"] = this_structure["AutoScalingRoleArn"]

    if "ScalingPolicies" in this_structure:
        transformed_output["ScalingPolicies"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingPolicyDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ScalingPolicies"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    if "IndexStatus" in this_structure:
        transformed_output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_IndexStatus(
                this_structure["IndexStatus"], item_handler, condition_handler
            )
        )

    if "ProvisionedReadCapacityUnits" in this_structure:
        transformed_output["ProvisionedReadCapacityUnits"] = this_structure[
            "ProvisionedReadCapacityUnits"
        ]

    if "ProvisionedReadCapacityAutoScalingSettings" in this_structure:
        transformed_output["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ProvisionedReadCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ProvisionedWriteCapacityUnits" in this_structure:
        transformed_output["ProvisionedWriteCapacityUnits"] = this_structure[
            "ProvisionedWriteCapacityUnits"
        ]

    if "ProvisionedWriteCapacityAutoScalingSettings" in this_structure:
        transformed_output["ProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ProvisionedWriteCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingPolicyDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "PolicyName" in this_structure:
        transformed_output["PolicyName"] = this_structure["PolicyName"]

    if "TargetTrackingScalingPolicyConfiguration" in this_structure:
        transformed_output["TargetTrackingScalingPolicyConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
                this_structure["TargetTrackingScalingPolicyConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "DisableScaleIn" in this_structure:
        transformed_output["DisableScaleIn"] = this_structure["DisableScaleIn"]

    if "ScaleInCooldown" in this_structure:
        transformed_output["ScaleInCooldown"] = this_structure["ScaleInCooldown"]

    if "ScaleOutCooldown" in this_structure:
        transformed_output["ScaleOutCooldown"] = this_structure["ScaleOutCooldown"]

    transformed_output["TargetValue"] = this_structure["TargetValue"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeImportInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ImportArn"] = this_structure["ImportArn"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeImportOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ImportTableDescription"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportTableDescription(
            this_structure["ImportTableDescription"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_ImportTableDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ImportArn" in this_structure:
        transformed_output["ImportArn"] = this_structure["ImportArn"]

    if "ImportStatus" in this_structure:
        transformed_output["ImportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportStatus(
                this_structure["ImportStatus"], item_handler, condition_handler
            )
        )

    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "TableId" in this_structure:
        transformed_output["TableId"] = this_structure["TableId"]

    if "ClientToken" in this_structure:
        transformed_output["ClientToken"] = this_structure["ClientToken"]

    if "S3BucketSource" in this_structure:
        transformed_output["S3BucketSource"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_S3BucketSource(
                this_structure["S3BucketSource"], item_handler, condition_handler
            )
        )

    if "ErrorCount" in this_structure:
        transformed_output["ErrorCount"] = this_structure["ErrorCount"]

    if "CloudWatchLogGroupArn" in this_structure:
        transformed_output["CloudWatchLogGroupArn"] = this_structure[
            "CloudWatchLogGroupArn"
        ]

    if "InputFormat" in this_structure:
        transformed_output["InputFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputFormat(
                this_structure["InputFormat"], item_handler, condition_handler
            )
        )

    if "InputFormatOptions" in this_structure:
        transformed_output["InputFormatOptions"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputFormatOptions(
                this_structure["InputFormatOptions"], item_handler, condition_handler
            )
        )

    if "InputCompressionType" in this_structure:
        transformed_output["InputCompressionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputCompressionType(
                this_structure["InputCompressionType"], item_handler, condition_handler
            )
        )

    if "TableCreationParameters" in this_structure:
        transformed_output["TableCreationParameters"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableCreationParameters(
                this_structure["TableCreationParameters"],
                item_handler,
                condition_handler,
            )
        )

    if "StartTime" in this_structure:
        transformed_output["StartTime"] = this_structure["StartTime"]

    if "EndTime" in this_structure:
        transformed_output["EndTime"] = this_structure["EndTime"]

    if "ProcessedSizeBytes" in this_structure:
        transformed_output["ProcessedSizeBytes"] = this_structure["ProcessedSizeBytes"]

    if "ProcessedItemCount" in this_structure:
        transformed_output["ProcessedItemCount"] = this_structure["ProcessedItemCount"]

    if "ImportedItemCount" in this_structure:
        transformed_output["ImportedItemCount"] = this_structure["ImportedItemCount"]

    if "FailureCode" in this_structure:
        transformed_output["FailureCode"] = this_structure["FailureCode"]

    if "FailureMessage" in this_structure:
        transformed_output["FailureMessage"] = this_structure["FailureMessage"]

    return transformed_output


def com_amazonaws_dynamodb_ImportStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_S3BucketSource(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "S3BucketOwner" in this_structure:
        transformed_output["S3BucketOwner"] = this_structure["S3BucketOwner"]

    transformed_output["S3Bucket"] = this_structure["S3Bucket"]
    if "S3KeyPrefix" in this_structure:
        transformed_output["S3KeyPrefix"] = this_structure["S3KeyPrefix"]

    return transformed_output


def com_amazonaws_dynamodb_InputFormat(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_InputFormatOptions(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Csv" in this_structure:
        transformed_output["Csv"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CsvOptions(
                this_structure["Csv"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_InputCompressionType(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_TableCreationParameters(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["AttributeDefinitions"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeDefinition(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["AttributeDefinitions"]
    ]
    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    if "BillingMode" in this_structure:
        transformed_output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingMode"], item_handler, condition_handler
            )
        )

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    if "SSESpecification" in this_structure:
        transformed_output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSESpecification(
                this_structure["SSESpecification"], item_handler, condition_handler
            )
        )

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_CsvOptions(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "Delimiter" in this_structure:
        transformed_output["Delimiter"] = this_structure["Delimiter"]

    if "HeaderList" in this_structure:
        transformed_output["HeaderList"] = [
            list_element for list_element in this_structure["HeaderList"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeKinesisStreamingDestinationOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "KinesisDataStreamDestinations" in this_structure:
        transformed_output["KinesisDataStreamDestinations"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KinesisDataStreamDestination(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["KinesisDataStreamDestinations"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_KinesisDataStreamDestination(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "StreamArn" in this_structure:
        transformed_output["StreamArn"] = this_structure["StreamArn"]

    if "DestinationStatus" in this_structure:
        transformed_output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DestinationStatus(
                this_structure["DestinationStatus"], item_handler, condition_handler
            )
        )

    if "DestinationStatusDescription" in this_structure:
        transformed_output["DestinationStatusDescription"] = this_structure[
            "DestinationStatusDescription"
        ]

    if "ApproximateCreationDateTimePrecision" in this_structure:
        transformed_output["ApproximateCreationDateTimePrecision"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ApproximateCreationDateTimePrecision(
                this_structure["ApproximateCreationDateTimePrecision"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DestinationStatus(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ApproximateCreationDateTimePrecision(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_DescribeLimitsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    return transformed_output


def com_amazonaws_dynamodb_DescribeLimitsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "AccountMaxReadCapacityUnits" in this_structure:
        transformed_output["AccountMaxReadCapacityUnits"] = this_structure[
            "AccountMaxReadCapacityUnits"
        ]

    if "AccountMaxWriteCapacityUnits" in this_structure:
        transformed_output["AccountMaxWriteCapacityUnits"] = this_structure[
            "AccountMaxWriteCapacityUnits"
        ]

    if "TableMaxReadCapacityUnits" in this_structure:
        transformed_output["TableMaxReadCapacityUnits"] = this_structure[
            "TableMaxReadCapacityUnits"
        ]

    if "TableMaxWriteCapacityUnits" in this_structure:
        transformed_output["TableMaxWriteCapacityUnits"] = this_structure[
            "TableMaxWriteCapacityUnits"
        ]

    return transformed_output


def com_amazonaws_dynamodb_DescribeTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Table" in this_structure:
        transformed_output["Table"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["Table"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeTableReplicaAutoScalingOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableAutoScalingDescription" in this_structure:
        transformed_output["TableAutoScalingDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableAutoScalingDescription(
                this_structure["TableAutoScalingDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TableAutoScalingDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "TableStatus" in this_structure:
        transformed_output["TableStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableStatus(
                this_structure["TableStatus"], item_handler, condition_handler
            )
        )

    if "Replicas" in this_structure:
        transformed_output["Replicas"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaAutoScalingDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Replicas"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ReplicaAutoScalingDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "RegionName" in this_structure:
        transformed_output["RegionName"] = this_structure["RegionName"]

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "ReplicaProvisionedReadCapacityAutoScalingSettings" in this_structure:
        transformed_output["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ReplicaProvisionedReadCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaProvisionedWriteCapacityAutoScalingSettings" in this_structure:
        transformed_output["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ReplicaProvisionedWriteCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaStatus" in this_structure:
        transformed_output["ReplicaStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaStatus(
                this_structure["ReplicaStatus"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingDescription(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "IndexStatus" in this_structure:
        transformed_output["IndexStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_IndexStatus(
                this_structure["IndexStatus"], item_handler, condition_handler
            )
        )

    if "ProvisionedReadCapacityAutoScalingSettings" in this_structure:
        transformed_output["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ProvisionedReadCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    if "ProvisionedWriteCapacityAutoScalingSettings" in this_structure:
        transformed_output["ProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsDescription(
                this_structure["ProvisionedWriteCapacityAutoScalingSettings"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DescribeTimeToLiveInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    return transformed_output


def com_amazonaws_dynamodb_DescribeTimeToLiveOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TimeToLiveDescription" in this_structure:
        transformed_output["TimeToLiveDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TimeToLiveDescription(
                this_structure["TimeToLiveDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["StreamArn"] = this_structure["StreamArn"]
    if "EnableKinesisStreamingConfiguration" in this_structure:
        transformed_output["EnableKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingConfiguration(
                this_structure["EnableKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_EnableKinesisStreamingConfiguration(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ApproximateCreationDateTimePrecision" in this_structure:
        transformed_output["ApproximateCreationDateTimePrecision"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ApproximateCreationDateTimePrecision(
                this_structure["ApproximateCreationDateTimePrecision"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DisableKinesisStreamingDestinationOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "StreamArn" in this_structure:
        transformed_output["StreamArn"] = this_structure["StreamArn"]

    if "DestinationStatus" in this_structure:
        transformed_output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DestinationStatus(
                this_structure["DestinationStatus"], item_handler, condition_handler
            )
        )

    if "EnableKinesisStreamingConfiguration" in this_structure:
        transformed_output["EnableKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingConfiguration(
                this_structure["EnableKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["StreamArn"] = this_structure["StreamArn"]
    if "EnableKinesisStreamingConfiguration" in this_structure:
        transformed_output["EnableKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingConfiguration(
                this_structure["EnableKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_EnableKinesisStreamingDestinationOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "StreamArn" in this_structure:
        transformed_output["StreamArn"] = this_structure["StreamArn"]

    if "DestinationStatus" in this_structure:
        transformed_output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DestinationStatus(
                this_structure["DestinationStatus"], item_handler, condition_handler
            )
        )

    if "EnableKinesisStreamingConfiguration" in this_structure:
        transformed_output["EnableKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_EnableKinesisStreamingConfiguration(
                this_structure["EnableKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExecuteStatementInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Statement"] = this_structure["Statement"]
    if "Parameters" in this_structure:
        transformed_output["Parameters"] = [
            item_handler(list_element) for list_element in this_structure["Parameters"]
        ]

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExecuteStatementOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Items" in this_structure:
        transformed_output["Items"] = [
            {key: item_handler(value) for (key, value) in list_element.items()}
            for list_element in this_structure["Items"]
        ]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    if "LastEvaluatedKey" in this_structure:
        transformed_output["LastEvaluatedKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["LastEvaluatedKey"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_ExecuteTransactionInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TransactStatements"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ParameterizedStatement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["TransactStatements"]
    ]
    if "ClientRequestToken" in this_structure:
        transformed_output["ClientRequestToken"] = this_structure["ClientRequestToken"]

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ParameterizedStatement(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Statement"] = this_structure["Statement"]
    if "Parameters" in this_structure:
        transformed_output["Parameters"] = [
            item_handler(list_element) for list_element in this_structure["Parameters"]
        ]

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExecuteTransactionOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Responses" in this_structure:
        transformed_output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemResponse(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Responses"]
        ]

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ItemResponse(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Item" in this_structure:
        transformed_output["Item"] = {
            key: item_handler(value) for (key, value) in this_structure["Item"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_ExportTableToPointInTimeInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableArn"] = this_structure["TableArn"]
    if "ExportTime" in this_structure:
        transformed_output["ExportTime"] = this_structure["ExportTime"]

    if "ClientToken" in this_structure:
        transformed_output["ClientToken"] = this_structure["ClientToken"]

    transformed_output["S3Bucket"] = this_structure["S3Bucket"]
    if "S3BucketOwner" in this_structure:
        transformed_output["S3BucketOwner"] = this_structure["S3BucketOwner"]

    if "S3Prefix" in this_structure:
        transformed_output["S3Prefix"] = this_structure["S3Prefix"]

    if "S3SseAlgorithm" in this_structure:
        transformed_output["S3SseAlgorithm"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_S3SseAlgorithm(
                this_structure["S3SseAlgorithm"], item_handler, condition_handler
            )
        )

    if "S3SseKmsKeyId" in this_structure:
        transformed_output["S3SseKmsKeyId"] = this_structure["S3SseKmsKeyId"]

    if "ExportFormat" in this_structure:
        transformed_output["ExportFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportFormat(
                this_structure["ExportFormat"], item_handler, condition_handler
            )
        )

    if "ExportType" in this_structure:
        transformed_output["ExportType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportType(
                this_structure["ExportType"], item_handler, condition_handler
            )
        )

    if "IncrementalExportSpecification" in this_structure:
        transformed_output["IncrementalExportSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_IncrementalExportSpecification(
                this_structure["IncrementalExportSpecification"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ExportTableToPointInTimeOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportDescription" in this_structure:
        transformed_output["ExportDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportDescription(
                this_structure["ExportDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GetItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    if "AttributesToGet" in this_structure:
        transformed_output["AttributesToGet"] = [
            list_element for list_element in this_structure["AttributesToGet"]
        ]

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ProjectionExpression" in this_structure:
        transformed_output["ProjectionExpression"] = this_structure[
            "ProjectionExpression"
        ]

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_GetItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Item" in this_structure:
        transformed_output["Item"] = {
            key: item_handler(value) for (key, value) in this_structure["Item"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GetResourcePolicyInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    return transformed_output


def com_amazonaws_dynamodb_GetResourcePolicyOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Policy" in this_structure:
        transformed_output["Policy"] = this_structure["Policy"]

    if "RevisionId" in this_structure:
        transformed_output["RevisionId"] = this_structure["RevisionId"]

    return transformed_output


def com_amazonaws_dynamodb_ImportTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ClientToken" in this_structure:
        transformed_output["ClientToken"] = this_structure["ClientToken"]

    transformed_output["S3BucketSource"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_S3BucketSource(
            this_structure["S3BucketSource"], item_handler, condition_handler
        )
    )
    transformed_output["InputFormat"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputFormat(
            this_structure["InputFormat"], item_handler, condition_handler
        )
    )
    if "InputFormatOptions" in this_structure:
        transformed_output["InputFormatOptions"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputFormatOptions(
                this_structure["InputFormatOptions"], item_handler, condition_handler
            )
        )

    if "InputCompressionType" in this_structure:
        transformed_output["InputCompressionType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputCompressionType(
                this_structure["InputCompressionType"], item_handler, condition_handler
            )
        )

    transformed_output["TableCreationParameters"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableCreationParameters(
            this_structure["TableCreationParameters"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_ImportTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ImportTableDescription"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportTableDescription(
            this_structure["ImportTableDescription"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_ListBackupsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    if "TimeRangeLowerBound" in this_structure:
        transformed_output["TimeRangeLowerBound"] = this_structure[
            "TimeRangeLowerBound"
        ]

    if "TimeRangeUpperBound" in this_structure:
        transformed_output["TimeRangeUpperBound"] = this_structure[
            "TimeRangeUpperBound"
        ]

    if "ExclusiveStartBackupArn" in this_structure:
        transformed_output["ExclusiveStartBackupArn"] = this_structure[
            "ExclusiveStartBackupArn"
        ]

    if "BackupType" in this_structure:
        transformed_output["BackupType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupTypeFilter(
                this_structure["BackupType"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_BackupTypeFilter(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_ListBackupsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "BackupSummaries" in this_structure:
        transformed_output["BackupSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupSummary(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["BackupSummaries"]
        ]

    if "LastEvaluatedBackupArn" in this_structure:
        transformed_output["LastEvaluatedBackupArn"] = this_structure[
            "LastEvaluatedBackupArn"
        ]

    return transformed_output


def com_amazonaws_dynamodb_BackupSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "TableId" in this_structure:
        transformed_output["TableId"] = this_structure["TableId"]

    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "BackupArn" in this_structure:
        transformed_output["BackupArn"] = this_structure["BackupArn"]

    if "BackupName" in this_structure:
        transformed_output["BackupName"] = this_structure["BackupName"]

    if "BackupCreationDateTime" in this_structure:
        transformed_output["BackupCreationDateTime"] = this_structure[
            "BackupCreationDateTime"
        ]

    if "BackupExpiryDateTime" in this_structure:
        transformed_output["BackupExpiryDateTime"] = this_structure[
            "BackupExpiryDateTime"
        ]

    if "BackupStatus" in this_structure:
        transformed_output["BackupStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupStatus(
                this_structure["BackupStatus"], item_handler, condition_handler
            )
        )

    if "BackupType" in this_structure:
        transformed_output["BackupType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BackupType(
                this_structure["BackupType"], item_handler, condition_handler
            )
        )

    if "BackupSizeBytes" in this_structure:
        transformed_output["BackupSizeBytes"] = this_structure["BackupSizeBytes"]

    return transformed_output


def com_amazonaws_dynamodb_ListContributorInsightsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    if "MaxResults" in this_structure:
        transformed_output["MaxResults"] = this_structure["MaxResults"]

    return transformed_output


def com_amazonaws_dynamodb_ListContributorInsightsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ContributorInsightsSummaries" in this_structure:
        transformed_output["ContributorInsightsSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContributorInsightsSummary(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ContributorInsightsSummaries"]
        ]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ContributorInsightsSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ContributorInsightsStatus" in this_structure:
        transformed_output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContributorInsightsStatus(
                this_structure["ContributorInsightsStatus"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ListExportsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "MaxResults" in this_structure:
        transformed_output["MaxResults"] = this_structure["MaxResults"]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ListExportsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportSummaries" in this_structure:
        transformed_output["ExportSummaries"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportSummary(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ExportSummaries"]
        ]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ExportSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExportArn" in this_structure:
        transformed_output["ExportArn"] = this_structure["ExportArn"]

    if "ExportStatus" in this_structure:
        transformed_output["ExportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportStatus(
                this_structure["ExportStatus"], item_handler, condition_handler
            )
        )

    if "ExportType" in this_structure:
        transformed_output["ExportType"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExportType(
                this_structure["ExportType"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ListGlobalTablesInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExclusiveStartGlobalTableName" in this_structure:
        transformed_output["ExclusiveStartGlobalTableName"] = this_structure[
            "ExclusiveStartGlobalTableName"
        ]

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    if "RegionName" in this_structure:
        transformed_output["RegionName"] = this_structure["RegionName"]

    return transformed_output


def com_amazonaws_dynamodb_ListGlobalTablesOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTables" in this_structure:
        transformed_output["GlobalTables"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTable(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalTables"]
        ]

    if "LastEvaluatedGlobalTableName" in this_structure:
        transformed_output["LastEvaluatedGlobalTableName"] = this_structure[
            "LastEvaluatedGlobalTableName"
        ]

    return transformed_output


def com_amazonaws_dynamodb_GlobalTable(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableName" in this_structure:
        transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]

    if "ReplicationGroup" in this_structure:
        transformed_output["ReplicationGroup"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Replica(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicationGroup"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_ListImportsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "PageSize" in this_structure:
        transformed_output["PageSize"] = this_structure["PageSize"]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ListImportsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ImportSummaryList" in this_structure:
        transformed_output["ImportSummaryList"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportSummary(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ImportSummaryList"]
        ]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ImportSummary(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ImportArn" in this_structure:
        transformed_output["ImportArn"] = this_structure["ImportArn"]

    if "ImportStatus" in this_structure:
        transformed_output["ImportStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ImportStatus(
                this_structure["ImportStatus"], item_handler, condition_handler
            )
        )

    if "TableArn" in this_structure:
        transformed_output["TableArn"] = this_structure["TableArn"]

    if "S3BucketSource" in this_structure:
        transformed_output["S3BucketSource"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_S3BucketSource(
                this_structure["S3BucketSource"], item_handler, condition_handler
            )
        )

    if "CloudWatchLogGroupArn" in this_structure:
        transformed_output["CloudWatchLogGroupArn"] = this_structure[
            "CloudWatchLogGroupArn"
        ]

    if "InputFormat" in this_structure:
        transformed_output["InputFormat"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_InputFormat(
                this_structure["InputFormat"], item_handler, condition_handler
            )
        )

    if "StartTime" in this_structure:
        transformed_output["StartTime"] = this_structure["StartTime"]

    if "EndTime" in this_structure:
        transformed_output["EndTime"] = this_structure["EndTime"]

    return transformed_output


def com_amazonaws_dynamodb_ListTablesInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ExclusiveStartTableName" in this_structure:
        transformed_output["ExclusiveStartTableName"] = this_structure[
            "ExclusiveStartTableName"
        ]

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    return transformed_output


def com_amazonaws_dynamodb_ListTablesOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableNames" in this_structure:
        transformed_output["TableNames"] = [
            list_element for list_element in this_structure["TableNames"]
        ]

    if "LastEvaluatedTableName" in this_structure:
        transformed_output["LastEvaluatedTableName"] = this_structure[
            "LastEvaluatedTableName"
        ]

    return transformed_output


def com_amazonaws_dynamodb_ListTagsOfResourceInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_ListTagsOfResourceOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Tags" in this_structure:
        transformed_output["Tags"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Tag(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Tags"]
        ]

    if "NextToken" in this_structure:
        transformed_output["NextToken"] = this_structure["NextToken"]

    return transformed_output


def com_amazonaws_dynamodb_PutItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["Item"] = {
        key: item_handler(value) for (key, value) in this_structure["Item"].items()
    }
    if "Expected" in this_structure:
        transformed_output["Expected"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["Expected"].items()
        }

    if "ReturnValues" in this_structure:
        transformed_output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValue(
                this_structure["ReturnValues"], item_handler, condition_handler
            )
        )

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ReturnItemCollectionMetrics" in this_structure:
        transformed_output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                this_structure["ReturnItemCollectionMetrics"],
                item_handler,
                condition_handler,
            )
        )

    if "ConditionalOperator" in this_structure:
        transformed_output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionalOperator(
                this_structure["ConditionalOperator"], item_handler, condition_handler
            )
        )

    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_PutItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Attributes" in this_structure:
        transformed_output["Attributes"] = {
            key: item_handler(value)
            for (key, value) in this_structure["Attributes"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    if "ItemCollectionMetrics" in this_structure:
        transformed_output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemCollectionMetrics(
                this_structure["ItemCollectionMetrics"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_PutResourcePolicyInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    transformed_output["Policy"] = this_structure["Policy"]
    if "ExpectedRevisionId" in this_structure:
        transformed_output["ExpectedRevisionId"] = this_structure["ExpectedRevisionId"]

    if "ConfirmRemoveSelfResourceAccess" in this_structure:
        transformed_output["ConfirmRemoveSelfResourceAccess"] = this_structure[
            "ConfirmRemoveSelfResourceAccess"
        ]

    return transformed_output


def com_amazonaws_dynamodb_PutResourcePolicyOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "RevisionId" in this_structure:
        transformed_output["RevisionId"] = this_structure["RevisionId"]

    return transformed_output


def com_amazonaws_dynamodb_QueryInput(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "Select" in this_structure:
        transformed_output["Select"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Select(
                this_structure["Select"], item_handler, condition_handler
            )
        )

    if "AttributesToGet" in this_structure:
        transformed_output["AttributesToGet"] = [
            list_element for list_element in this_structure["AttributesToGet"]
        ]

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    if "KeyConditions" in this_structure:
        transformed_output["KeyConditions"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Condition(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["KeyConditions"].items()
        }

    if "QueryFilter" in this_structure:
        transformed_output["QueryFilter"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Condition(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["QueryFilter"].items()
        }

    if "ConditionalOperator" in this_structure:
        transformed_output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionalOperator(
                this_structure["ConditionalOperator"], item_handler, condition_handler
            )
        )

    if "ScanIndexForward" in this_structure:
        transformed_output["ScanIndexForward"] = this_structure["ScanIndexForward"]

    if "ExclusiveStartKey" in this_structure:
        transformed_output["ExclusiveStartKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExclusiveStartKey"].items()
        }

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ProjectionExpression" in this_structure:
        transformed_output["ProjectionExpression"] = this_structure[
            "ProjectionExpression"
        ]

    if "FilterExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "FilterExpression", this_structure
        )
        transformed_output["FilterExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "KeyConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "KeyConditionExpression", this_structure
        )
        transformed_output["KeyConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_Select(this_structure, item_handler, condition_handler):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_Condition(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "AttributeValueList" in this_structure:
        transformed_output["AttributeValueList"] = [
            item_handler(list_element)
            for list_element in this_structure["AttributeValueList"]
        ]

    transformed_output["ComparisonOperator"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ComparisonOperator(
            this_structure["ComparisonOperator"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_QueryOutput(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "Items" in this_structure:
        transformed_output["Items"] = [
            {key: item_handler(value) for (key, value) in list_element.items()}
            for list_element in this_structure["Items"]
        ]

    if "Count" in this_structure:
        transformed_output["Count"] = this_structure["Count"]

    if "ScannedCount" in this_structure:
        transformed_output["ScannedCount"] = this_structure["ScannedCount"]

    if "LastEvaluatedKey" in this_structure:
        transformed_output["LastEvaluatedKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["LastEvaluatedKey"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_RestoreTableFromBackupInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TargetTableName"] = this_structure["TargetTableName"]
    transformed_output["BackupArn"] = this_structure["BackupArn"]
    if "BillingModeOverride" in this_structure:
        transformed_output["BillingModeOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingModeOverride"], item_handler, condition_handler
            )
        )

    if "GlobalSecondaryIndexOverride" in this_structure:
        transformed_output["GlobalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexOverride"]
        ]

    if "LocalSecondaryIndexOverride" in this_structure:
        transformed_output["LocalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["LocalSecondaryIndexOverride"]
        ]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "SSESpecificationOverride" in this_structure:
        transformed_output["SSESpecificationOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSESpecification(
                this_structure["SSESpecificationOverride"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_RestoreTableFromBackupOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableDescription" in this_structure:
        transformed_output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["TableDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_RestoreTableToPointInTimeInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "SourceTableArn" in this_structure:
        transformed_output["SourceTableArn"] = this_structure["SourceTableArn"]

    if "SourceTableName" in this_structure:
        transformed_output["SourceTableName"] = this_structure["SourceTableName"]

    transformed_output["TargetTableName"] = this_structure["TargetTableName"]
    if "UseLatestRestorableTime" in this_structure:
        transformed_output["UseLatestRestorableTime"] = this_structure[
            "UseLatestRestorableTime"
        ]

    if "RestoreDateTime" in this_structure:
        transformed_output["RestoreDateTime"] = this_structure["RestoreDateTime"]

    if "BillingModeOverride" in this_structure:
        transformed_output["BillingModeOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingModeOverride"], item_handler, condition_handler
            )
        )

    if "GlobalSecondaryIndexOverride" in this_structure:
        transformed_output["GlobalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexOverride"]
        ]

    if "LocalSecondaryIndexOverride" in this_structure:
        transformed_output["LocalSecondaryIndexOverride"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_LocalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["LocalSecondaryIndexOverride"]
        ]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "SSESpecificationOverride" in this_structure:
        transformed_output["SSESpecificationOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSESpecification(
                this_structure["SSESpecificationOverride"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_RestoreTableToPointInTimeOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableDescription" in this_structure:
        transformed_output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["TableDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ScanInput(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "AttributesToGet" in this_structure:
        transformed_output["AttributesToGet"] = [
            list_element for list_element in this_structure["AttributesToGet"]
        ]

    if "Limit" in this_structure:
        transformed_output["Limit"] = this_structure["Limit"]

    if "Select" in this_structure:
        transformed_output["Select"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Select(
                this_structure["Select"], item_handler, condition_handler
            )
        )

    if "ScanFilter" in this_structure:
        transformed_output["ScanFilter"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Condition(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["ScanFilter"].items()
        }

    if "ConditionalOperator" in this_structure:
        transformed_output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionalOperator(
                this_structure["ConditionalOperator"], item_handler, condition_handler
            )
        )

    if "ExclusiveStartKey" in this_structure:
        transformed_output["ExclusiveStartKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExclusiveStartKey"].items()
        }

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "TotalSegments" in this_structure:
        transformed_output["TotalSegments"] = this_structure["TotalSegments"]

    if "Segment" in this_structure:
        transformed_output["Segment"] = this_structure["Segment"]

    if "ProjectionExpression" in this_structure:
        transformed_output["ProjectionExpression"] = this_structure[
            "ProjectionExpression"
        ]

    if "FilterExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "FilterExpression", this_structure
        )
        transformed_output["FilterExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ConsistentRead" in this_structure:
        transformed_output["ConsistentRead"] = this_structure["ConsistentRead"]

    return transformed_output


def com_amazonaws_dynamodb_ScanOutput(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    if "Items" in this_structure:
        transformed_output["Items"] = [
            {key: item_handler(value) for (key, value) in list_element.items()}
            for list_element in this_structure["Items"]
        ]

    if "Count" in this_structure:
        transformed_output["Count"] = this_structure["Count"]

    if "ScannedCount" in this_structure:
        transformed_output["ScannedCount"] = this_structure["ScannedCount"]

    if "LastEvaluatedKey" in this_structure:
        transformed_output["LastEvaluatedKey"] = {
            key: item_handler(value)
            for (key, value) in this_structure["LastEvaluatedKey"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TagResourceInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    transformed_output["Tags"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Tag(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["Tags"]
    ]
    return transformed_output


def com_amazonaws_dynamodb_TransactGetItemsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TransactItems"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactGetItem(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["TransactItems"]
    ]
    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TransactGetItem(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Get"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Get(
            this_structure["Get"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_Get(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    transformed_output["TableName"] = this_structure["TableName"]
    if "ProjectionExpression" in this_structure:
        transformed_output["ProjectionExpression"] = this_structure[
            "ProjectionExpression"
        ]

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_TransactGetItemsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    if "Responses" in this_structure:
        transformed_output["Responses"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemResponse(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["Responses"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_TransactWriteItemsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TransactItems"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TransactWriteItem(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["TransactItems"]
    ]
    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ReturnItemCollectionMetrics" in this_structure:
        transformed_output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                this_structure["ReturnItemCollectionMetrics"],
                item_handler,
                condition_handler,
            )
        )

    if "ClientRequestToken" in this_structure:
        transformed_output["ClientRequestToken"] = this_structure["ClientRequestToken"]

    return transformed_output


def com_amazonaws_dynamodb_TransactWriteItem(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ConditionCheck" in this_structure:
        transformed_output["ConditionCheck"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionCheck(
                this_structure["ConditionCheck"], item_handler, condition_handler
            )
        )

    if "Put" in this_structure:
        transformed_output["Put"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Put(
                this_structure["Put"], item_handler, condition_handler
            )
        )

    if "Delete" in this_structure:
        transformed_output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Delete(
                this_structure["Delete"], item_handler, condition_handler
            )
        )

    if "Update" in this_structure:
        transformed_output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Update(
                this_structure["Update"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ConditionCheck(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    transformed_output["TableName"] = this_structure["TableName"]
    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_Put(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Item"] = {
        key: item_handler(value) for (key, value) in this_structure["Item"].items()
    }
    transformed_output["TableName"] = this_structure["TableName"]
    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_Delete(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    transformed_output["TableName"] = this_structure["TableName"]
    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_Update(this_structure, item_handler, condition_handler):
    transformed_output = deepcopy(this_structure)
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    transformed_output["UpdateExpression"] = this_structure["UpdateExpression"]
    transformed_output["TableName"] = this_structure["TableName"]
    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_TransactWriteItemsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ConsumedCapacity"]
        ]

    if "ItemCollectionMetrics" in this_structure:
        transformed_output["ItemCollectionMetrics"] = {
            key: [
                aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemCollectionMetrics(
                    list_element, item_handler, condition_handler
                )
                for list_element in value
            ]
            for (key, value) in this_structure["ItemCollectionMetrics"].items()
        }

    return transformed_output


def com_amazonaws_dynamodb_UntagResourceInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["ResourceArn"] = this_structure["ResourceArn"]
    transformed_output["TagKeys"] = [
        list_element for list_element in this_structure["TagKeys"]
    ]
    return transformed_output


def com_amazonaws_dynamodb_UpdateContinuousBackupsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["PointInTimeRecoverySpecification"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_PointInTimeRecoverySpecification(
            this_structure["PointInTimeRecoverySpecification"],
            item_handler,
            condition_handler,
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_PointInTimeRecoverySpecification(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["PointInTimeRecoveryEnabled"] = this_structure[
        "PointInTimeRecoveryEnabled"
    ]
    return transformed_output


def com_amazonaws_dynamodb_UpdateContinuousBackupsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ContinuousBackupsDescription" in this_structure:
        transformed_output["ContinuousBackupsDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContinuousBackupsDescription(
                this_structure["ContinuousBackupsDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateContributorInsightsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    transformed_output["ContributorInsightsAction"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContributorInsightsAction(
            this_structure["ContributorInsightsAction"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_ContributorInsightsAction(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_UpdateContributorInsightsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ContributorInsightsStatus" in this_structure:
        transformed_output["ContributorInsightsStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ContributorInsightsStatus(
                this_structure["ContributorInsightsStatus"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateGlobalTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]
    transformed_output["ReplicaUpdates"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaUpdate(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["ReplicaUpdates"]
    ]
    return transformed_output


def com_amazonaws_dynamodb_ReplicaUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Create" in this_structure:
        transformed_output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateReplicaAction(
                this_structure["Create"], item_handler, condition_handler
            )
        )

    if "Delete" in this_structure:
        transformed_output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteReplicaAction(
                this_structure["Delete"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_CreateReplicaAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    return transformed_output


def com_amazonaws_dynamodb_DeleteReplicaAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    return transformed_output


def com_amazonaws_dynamodb_UpdateGlobalTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableDescription" in this_structure:
        transformed_output["GlobalTableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTableDescription(
                this_structure["GlobalTableDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]
    if "GlobalTableBillingMode" in this_structure:
        transformed_output["GlobalTableBillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["GlobalTableBillingMode"],
                item_handler,
                condition_handler,
            )
        )

    if "GlobalTableProvisionedWriteCapacityUnits" in this_structure:
        transformed_output["GlobalTableProvisionedWriteCapacityUnits"] = this_structure[
            "GlobalTableProvisionedWriteCapacityUnits"
        ]

    if "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate" in this_structure:
        transformed_output[
            "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"
        ] = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
            this_structure[
                "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"
            ],
            item_handler,
            condition_handler,
        )

    if "GlobalTableGlobalSecondaryIndexSettingsUpdate" in this_structure:
        transformed_output["GlobalTableGlobalSecondaryIndexSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure[
                "GlobalTableGlobalSecondaryIndexSettingsUpdate"
            ]
        ]

    if "ReplicaSettingsUpdate" in this_structure:
        transformed_output["ReplicaSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaSettingsUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaSettingsUpdate"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "MinimumUnits" in this_structure:
        transformed_output["MinimumUnits"] = this_structure["MinimumUnits"]

    if "MaximumUnits" in this_structure:
        transformed_output["MaximumUnits"] = this_structure["MaximumUnits"]

    if "AutoScalingDisabled" in this_structure:
        transformed_output["AutoScalingDisabled"] = this_structure[
            "AutoScalingDisabled"
        ]

    if "AutoScalingRoleArn" in this_structure:
        transformed_output["AutoScalingRoleArn"] = this_structure["AutoScalingRoleArn"]

    if "ScalingPolicyUpdate" in this_structure:
        transformed_output["ScalingPolicyUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingPolicyUpdate(
                this_structure["ScalingPolicyUpdate"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GlobalTableGlobalSecondaryIndexSettingsUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    if "ProvisionedWriteCapacityUnits" in this_structure:
        transformed_output["ProvisionedWriteCapacityUnits"] = this_structure[
            "ProvisionedWriteCapacityUnits"
        ]

    if "ProvisionedWriteCapacityAutoScalingSettingsUpdate" in this_structure:
        transformed_output["ProvisionedWriteCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ProvisionedWriteCapacityAutoScalingSettingsUpdate"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReplicaSettingsUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    if "ReplicaProvisionedReadCapacityUnits" in this_structure:
        transformed_output["ReplicaProvisionedReadCapacityUnits"] = this_structure[
            "ReplicaProvisionedReadCapacityUnits"
        ]

    if "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate" in this_structure:
        transformed_output[
            "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"
        ] = aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
            this_structure["ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"],
            item_handler,
            condition_handler,
        )

    if "ReplicaGlobalSecondaryIndexSettingsUpdate" in this_structure:
        transformed_output["ReplicaGlobalSecondaryIndexSettingsUpdate"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure[
                "ReplicaGlobalSecondaryIndexSettingsUpdate"
            ]
        ]

    if "ReplicaTableClass" in this_structure:
        transformed_output["ReplicaTableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["ReplicaTableClass"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingPolicyUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "PolicyName" in this_structure:
        transformed_output["PolicyName"] = this_structure["PolicyName"]

    transformed_output["TargetTrackingScalingPolicyConfiguration"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
            this_structure["TargetTrackingScalingPolicyConfiguration"],
            item_handler,
            condition_handler,
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexSettingsUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    if "ProvisionedReadCapacityUnits" in this_structure:
        transformed_output["ProvisionedReadCapacityUnits"] = this_structure[
            "ProvisionedReadCapacityUnits"
        ]

    if "ProvisionedReadCapacityAutoScalingSettingsUpdate" in this_structure:
        transformed_output["ProvisionedReadCapacityAutoScalingSettingsUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ProvisionedReadCapacityAutoScalingSettingsUpdate"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "DisableScaleIn" in this_structure:
        transformed_output["DisableScaleIn"] = this_structure["DisableScaleIn"]

    if "ScaleInCooldown" in this_structure:
        transformed_output["ScaleInCooldown"] = this_structure["ScaleInCooldown"]

    if "ScaleOutCooldown" in this_structure:
        transformed_output["ScaleOutCooldown"] = this_structure["ScaleOutCooldown"]

    transformed_output["TargetValue"] = this_structure["TargetValue"]
    return transformed_output


def com_amazonaws_dynamodb_UpdateGlobalTableSettingsOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalTableName" in this_structure:
        transformed_output["GlobalTableName"] = this_structure["GlobalTableName"]

    if "ReplicaSettings" in this_structure:
        transformed_output["ReplicaSettings"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaSettingsDescription(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaSettings"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_UpdateItemInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["Key"] = {
        key: item_handler(value) for (key, value) in this_structure["Key"].items()
    }
    if "AttributeUpdates" in this_structure:
        transformed_output["AttributeUpdates"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeValueUpdate(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["AttributeUpdates"].items()
        }

    if "Expected" in this_structure:
        transformed_output["Expected"] = {
            key: aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ExpectedAttributeValue(
                value, item_handler, condition_handler
            )
            for (key, value) in this_structure["Expected"].items()
        }

    if "ConditionalOperator" in this_structure:
        transformed_output["ConditionalOperator"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConditionalOperator(
                this_structure["ConditionalOperator"], item_handler, condition_handler
            )
        )

    if "ReturnValues" in this_structure:
        transformed_output["ReturnValues"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValue(
                this_structure["ReturnValues"], item_handler, condition_handler
            )
        )

    if "ReturnConsumedCapacity" in this_structure:
        transformed_output["ReturnConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnConsumedCapacity(
                this_structure["ReturnConsumedCapacity"],
                item_handler,
                condition_handler,
            )
        )

    if "ReturnItemCollectionMetrics" in this_structure:
        transformed_output["ReturnItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnItemCollectionMetrics(
                this_structure["ReturnItemCollectionMetrics"],
                item_handler,
                condition_handler,
            )
        )

    if "UpdateExpression" in this_structure:
        transformed_output["UpdateExpression"] = this_structure["UpdateExpression"]

    if "ConditionExpression" in this_structure:
        condition_expression, attribute_names, attribute_values = condition_handler(
            "ConditionExpression", this_structure
        )
        transformed_output["ConditionExpression"] = condition_expression
        if len(attribute_names) > 0:
            this_structure.setdefault("ExpressionAttributeNames", {}).update(
                attribute_names
            )
        if len(attribute_values) > 0:
            this_structure.setdefault("ExpressionAttributeValues", {}).update(
                attribute_values
            )

    if "ExpressionAttributeNames" in this_structure:
        transformed_output["ExpressionAttributeNames"] = {
            key: value
            for (key, value) in this_structure["ExpressionAttributeNames"].items()
        }

    if "ExpressionAttributeValues" in this_structure:
        transformed_output["ExpressionAttributeValues"] = {
            key: item_handler(value)
            for (key, value) in this_structure["ExpressionAttributeValues"].items()
        }

    if "ReturnValuesOnConditionCheckFailure" in this_structure:
        transformed_output["ReturnValuesOnConditionCheckFailure"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReturnValuesOnConditionCheckFailure(
                this_structure["ReturnValuesOnConditionCheckFailure"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AttributeValueUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Value" in this_structure:
        transformed_output["Value"] = item_handler(this_structure["Value"])

    if "Action" in this_structure:
        transformed_output["Action"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeAction(
                this_structure["Action"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_AttributeAction(
    this_structure, item_handler, condition_handler
):
    # Always return input enum
    return this_structure


def com_amazonaws_dynamodb_UpdateItemOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Attributes" in this_structure:
        transformed_output["Attributes"] = {
            key: item_handler(value)
            for (key, value) in this_structure["Attributes"].items()
        }

    if "ConsumedCapacity" in this_structure:
        transformed_output["ConsumedCapacity"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ConsumedCapacity(
                this_structure["ConsumedCapacity"], item_handler, condition_handler
            )
        )

    if "ItemCollectionMetrics" in this_structure:
        transformed_output["ItemCollectionMetrics"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ItemCollectionMetrics(
                this_structure["ItemCollectionMetrics"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateKinesisStreamingDestinationInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["StreamArn"] = this_structure["StreamArn"]
    if "UpdateKinesisStreamingConfiguration" in this_structure:
        transformed_output["UpdateKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateKinesisStreamingConfiguration(
                this_structure["UpdateKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateKinesisStreamingConfiguration(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "ApproximateCreationDateTimePrecision" in this_structure:
        transformed_output["ApproximateCreationDateTimePrecision"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ApproximateCreationDateTimePrecision(
                this_structure["ApproximateCreationDateTimePrecision"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateKinesisStreamingDestinationOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableName" in this_structure:
        transformed_output["TableName"] = this_structure["TableName"]

    if "StreamArn" in this_structure:
        transformed_output["StreamArn"] = this_structure["StreamArn"]

    if "DestinationStatus" in this_structure:
        transformed_output["DestinationStatus"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DestinationStatus(
                this_structure["DestinationStatus"], item_handler, condition_handler
            )
        )

    if "UpdateKinesisStreamingConfiguration" in this_structure:
        transformed_output["UpdateKinesisStreamingConfiguration"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateKinesisStreamingConfiguration(
                this_structure["UpdateKinesisStreamingConfiguration"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateTableInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "AttributeDefinitions" in this_structure:
        transformed_output["AttributeDefinitions"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AttributeDefinition(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["AttributeDefinitions"]
        ]

    transformed_output["TableName"] = this_structure["TableName"]
    if "BillingMode" in this_structure:
        transformed_output["BillingMode"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_BillingMode(
                this_structure["BillingMode"], item_handler, condition_handler
            )
        )

    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "GlobalSecondaryIndexUpdates" in this_structure:
        transformed_output["GlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexUpdates"]
        ]

    if "StreamSpecification" in this_structure:
        transformed_output["StreamSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_StreamSpecification(
                this_structure["StreamSpecification"], item_handler, condition_handler
            )
        )

    if "SSESpecification" in this_structure:
        transformed_output["SSESpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_SSESpecification(
                this_structure["SSESpecification"], item_handler, condition_handler
            )
        )

    if "ReplicaUpdates" in this_structure:
        transformed_output["ReplicaUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicationGroupUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaUpdates"]
        ]

    if "TableClass" in this_structure:
        transformed_output["TableClass"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["TableClass"], item_handler, condition_handler
            )
        )

    if "DeletionProtectionEnabled" in this_structure:
        transformed_output["DeletionProtectionEnabled"] = this_structure[
            "DeletionProtectionEnabled"
        ]

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_GlobalSecondaryIndexUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Update" in this_structure:
        transformed_output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(
                this_structure["Update"], item_handler, condition_handler
            )
        )

    if "Create" in this_structure:
        transformed_output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(
                this_structure["Create"], item_handler, condition_handler
            )
        )

    if "Delete" in this_structure:
        transformed_output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(
                this_structure["Delete"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReplicationGroupUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "Create" in this_structure:
        transformed_output["Create"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(
                this_structure["Create"], item_handler, condition_handler
            )
        )

    if "Update" in this_structure:
        transformed_output["Update"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(
                this_structure["Update"], item_handler, condition_handler
            )
        )

    if "Delete" in this_structure:
        transformed_output["Delete"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(
                this_structure["Delete"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateGlobalSecondaryIndexAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_CreateGlobalSecondaryIndexAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    transformed_output["KeySchema"] = [
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_KeySchemaElement(
            list_element, item_handler, condition_handler
        )
        for list_element in this_structure["KeySchema"]
    ]
    transformed_output["Projection"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_Projection(
            this_structure["Projection"], item_handler, condition_handler
        )
    )
    if "ProvisionedThroughput" in this_structure:
        transformed_output["ProvisionedThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughput(
                this_structure["ProvisionedThroughput"], item_handler, condition_handler
            )
        )

    if "OnDemandThroughput" in this_structure:
        transformed_output["OnDemandThroughput"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughput(
                this_structure["OnDemandThroughput"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DeleteGlobalSecondaryIndexAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    return transformed_output


def com_amazonaws_dynamodb_CreateReplicationGroupMemberAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    if "KMSMasterKeyId" in this_structure:
        transformed_output["KMSMasterKeyId"] = this_structure["KMSMasterKeyId"]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughputOverride(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "TableClassOverride" in this_structure:
        transformed_output["TableClassOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["TableClassOverride"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateReplicationGroupMemberAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    if "KMSMasterKeyId" in this_structure:
        transformed_output["KMSMasterKeyId"] = this_structure["KMSMasterKeyId"]

    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughputOverride(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "GlobalSecondaryIndexes" in this_structure:
        transformed_output["GlobalSecondaryIndexes"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexes"]
        ]

    if "TableClassOverride" in this_structure:
        transformed_output["TableClassOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableClass(
                this_structure["TableClassOverride"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_DeleteReplicationGroupMemberAction(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndex(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["IndexName"] = this_structure["IndexName"]
    if "ProvisionedThroughputOverride" in this_structure:
        transformed_output["ProvisionedThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ProvisionedThroughputOverride(
                this_structure["ProvisionedThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    if "OnDemandThroughputOverride" in this_structure:
        transformed_output["OnDemandThroughputOverride"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_OnDemandThroughputOverride(
                this_structure["OnDemandThroughputOverride"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateTableOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableDescription" in this_structure:
        transformed_output["TableDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableDescription(
                this_structure["TableDescription"], item_handler, condition_handler
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "GlobalSecondaryIndexUpdates" in this_structure:
        transformed_output["GlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["GlobalSecondaryIndexUpdates"]
        ]

    transformed_output["TableName"] = this_structure["TableName"]
    if "ProvisionedWriteCapacityAutoScalingUpdate" in this_structure:
        transformed_output["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ProvisionedWriteCapacityAutoScalingUpdate"],
                item_handler,
                condition_handler,
            )
        )

    if "ReplicaUpdates" in this_structure:
        transformed_output["ReplicaUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaUpdates"]
        ]

    return transformed_output


def com_amazonaws_dynamodb_GlobalSecondaryIndexAutoScalingUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ProvisionedWriteCapacityAutoScalingUpdate" in this_structure:
        transformed_output["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ProvisionedWriteCapacityAutoScalingUpdate"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReplicaAutoScalingUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["RegionName"] = this_structure["RegionName"]
    if "ReplicaGlobalSecondaryIndexUpdates" in this_structure:
        transformed_output["ReplicaGlobalSecondaryIndexUpdates"] = [
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(
                list_element, item_handler, condition_handler
            )
            for list_element in this_structure["ReplicaGlobalSecondaryIndexUpdates"]
        ]

    if "ReplicaProvisionedReadCapacityAutoScalingUpdate" in this_structure:
        transformed_output["ReplicaProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ReplicaProvisionedReadCapacityAutoScalingUpdate"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_ReplicaGlobalSecondaryIndexAutoScalingUpdate(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "IndexName" in this_structure:
        transformed_output["IndexName"] = this_structure["IndexName"]

    if "ProvisionedReadCapacityAutoScalingUpdate" in this_structure:
        transformed_output["ProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_AutoScalingSettingsUpdate(
                this_structure["ProvisionedReadCapacityAutoScalingUpdate"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateTableReplicaAutoScalingOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TableAutoScalingDescription" in this_structure:
        transformed_output["TableAutoScalingDescription"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TableAutoScalingDescription(
                this_structure["TableAutoScalingDescription"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output


def com_amazonaws_dynamodb_UpdateTimeToLiveInput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["TableName"] = this_structure["TableName"]
    transformed_output["TimeToLiveSpecification"] = (
        aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TimeToLiveSpecification(
            this_structure["TimeToLiveSpecification"], item_handler, condition_handler
        )
    )
    return transformed_output


def com_amazonaws_dynamodb_TimeToLiveSpecification(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    transformed_output["Enabled"] = this_structure["Enabled"]
    transformed_output["AttributeName"] = this_structure["AttributeName"]
    return transformed_output


def com_amazonaws_dynamodb_UpdateTimeToLiveOutput(
    this_structure, item_handler, condition_handler
):
    transformed_output = deepcopy(this_structure)
    if "TimeToLiveSpecification" in this_structure:
        transformed_output["TimeToLiveSpecification"] = (
            aws_cryptography_internal_dynamodb.smithygenerated.com_amazonaws_dynamodb.aws_sdk_format_converter.com_amazonaws_dynamodb_TimeToLiveSpecification(
                this_structure["TimeToLiveSpecification"],
                item_handler,
                condition_handler,
            )
        )

    return transformed_output
