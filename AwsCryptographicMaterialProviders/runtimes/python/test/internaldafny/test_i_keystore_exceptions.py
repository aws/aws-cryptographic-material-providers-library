# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Test keystore exception handling examples."""
import pytest
import uuid
import boto3

from aws_cryptographic_material_providers.keystore.client import KeyStore
from aws_cryptographic_material_providers.keystore.config import KeyStoreConfig
from aws_cryptographic_material_providers.keystore.models import (
    CreateKeyInput,
    KMSConfigurationKmsKeyArn,
)
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors import (
    ComAmazonawsKms,
    ComAmazonawsDynamodb
)

pytestmark = [pytest.mark.examples]

BRANCH_KEY_ID = "test_transaction_canceled_exception_branch_id"
# Constants for test configuration
TEST_TABLE_NAME = "KeyStoreDdbTable"
TEST_KMS_KEY_ARN = "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126"
# KMS key ARN without kms:GenerateDataKeyWithoutPlaintext permission
KMS_KEY_ARN_WITHOUT_PERMISSIONS = "arn:aws:kms:us-west-2:370957321024:key/da179005-1c04-4b91-a103-ee43b9a707e6"


def test_kms_permission_exception():
    """This test verifies that the smithy-python properly handles `OpaqueWithText` exception from KMS."""
    try:
        keystore: KeyStore = KeyStore(
            KeyStoreConfig(
                ddb_table_name=TEST_TABLE_NAME,
                kms_configuration=KMSConfigurationKmsKeyArn(KMS_KEY_ARN_WITHOUT_PERMISSIONS),
                logical_key_store_name=TEST_TABLE_NAME,
                kms_client=boto3.client("kms"),
                ddb_client=boto3.client("dynamodb"),
            )
        )

        # Attempt to create a key - this should fail due to KMS permissions
        branch_key_id = keystore.create_key(CreateKeyInput()).branch_key_identifier
        pytest.fail("Expected ComAmazonawsKms exception, but no exception was raised")
    except ComAmazonawsKms as ex:
        assert "ClientError" in str(ex)


def test_transaction_canceled_exception():
    """This test verifies that attempting to create an already configured branch key ID, throws a TransactionCanceledException."""
    # Create AWS clients
    ddb_client = boto3.client('dynamodb')
    kms_client = boto3.client('kms')
    
    # Branch Key ID is pre-configured in the table for this test
    branch_key_id = "test_transaction_canceled_exception_branch_id"
    
    # Initialize KeyStore
    keystore = KeyStore(
        KeyStoreConfig(
            ddb_table_name=TEST_TABLE_NAME,
            kms_configuration=KMSConfigurationKmsKeyArn(TEST_KMS_KEY_ARN),
            logical_key_store_name=TEST_TABLE_NAME,
            kms_client=boto3.client("kms"),
            ddb_client=boto3.client("dynamodb"),
        )
    )
    
    # Attempt to create the branch key again with same branch key id, which should fail with TransactionCanceledException
    try:
        create_input = CreateKeyInput(branch_key_identifier=branch_key_id, encryption_context={'Robbie': 'is a Dog'})
        keystore.create_key(create_input)
        pytest.fail("Expected TransactionCanceledException but no exception was raised")
    except ComAmazonawsDynamodb as e:
        assert "Transaction cancelled" in str(e), f"Expected TransactionCanceledException but got: {e}"
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")