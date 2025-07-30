# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Test create key store key example."""
import pytest

import boto3
from aws_cryptographic_material_providers.keystore.client import KeyStore
from aws_cryptographic_material_providers.keystore.config import KeyStoreConfig
from aws_cryptographic_material_providers.keystore.models import (
    CreateKeyInput,
    KMSConfigurationKmsKeyArn,
)
from aws_cryptographic_material_providers.smithygenerated.aws_cryptography_keystore.errors import ComAmazonawsKms

pytestmark = [pytest.mark.examples]


def test_create_keystore_key():
    """This test verifies that the smithy-python properly handles `OpaqueWithText` exception from SDK dependencies."""

    # KMS key ARN without kms:GenerateDataKeyWithoutPlaintext permission to create `hierarchy-version-1` branch key.
    kmsArnForHV2 = "arn:aws:kms:us-west-2:370957321024:key/da179005-1c04-4b91-a103-ee43b9a707e6"

    try:
        # Attempt to create a key - this should fail due to KMS permissions
        keystore_create_key(
            key_store_table_name="KeyStoreDdbTable", 
            logical_key_store_name="KeyStoreDdbTable", 
            kms_key_arn=kmsArnForHV2
        )
        pytest.fail("Expected ComAmazonawsKms exception, but no exception was raised")
    except ComAmazonawsKms as ex:
        assert "ClientError" in str(ex)


def keystore_create_key(key_store_table_name: str, logical_key_store_name: str, kms_key_arn: str) -> str:
    """Create a new branch key and beacon key in our KeyStore."""
    # 1. Configure your KeyStore resource.
    #    This SHOULD be the same configuration that was used to create the DDB table
    #    in the "Create KeyStore Table Example".
    keystore: KeyStore = KeyStore(
        KeyStoreConfig(
            ddb_table_name=key_store_table_name,
            kms_configuration=KMSConfigurationKmsKeyArn(kms_key_arn),
            logical_key_store_name=logical_key_store_name,
            kms_client=boto3.client("kms"),
            ddb_client=boto3.client("dynamodb"),
        )
    )

    # 2. Create a new branch key and beacon key in our KeyStore.
    #    Both the branch key and the beacon key will share an Id.
    #    This creation is eventually consistent.
    branch_key_id = keystore.create_key(CreateKeyInput()).branch_key_identifier

    return branch_key_id
