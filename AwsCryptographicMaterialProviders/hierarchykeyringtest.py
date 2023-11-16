import aws_cryptography_keystore.smithygenerated.client
from aws_cryptography_keystore.smithygenerated.models import GetActiveBranchKeyInput, KMSConfigurationKmsKeyArn
from aws_cryptography_keystore.smithygenerated.config import KeyStoreConfig


import boto3
kms_client = boto3.client("kms")
ddb_client = boto3.client("dynamodb")

config = KeyStoreConfig(
ddb_table_name="KeyStoreDdbTable",
kms_configuration=KMSConfigurationKmsKeyArn(value="arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"),
logical_key_store_name="KeyStoreDdbTable",
id="",
grant_tokens=[],
ddb_client=ddb_client,
kms_client=kms_client
)

keystore_client = aws_cryptography_keystore.smithygenerated.client.KeyStore(config)

import aws_cryptography_materialproviders.smithygenerated.client
c = aws_cryptography_materialproviders.smithygenerated.client.AwsCryptographicMaterialProviders()

from aws_cryptography_materialproviders.smithygenerated.models import CreateAwsKmsHierarchicalKeyringInput, CacheTypeNo, NoCache

input = CreateAwsKmsHierarchicalKeyringInput(
branch_key_id="2c583585-5770-467d-8f59-b346d0ed1994",
branch_key_id_supplier=None,
key_store=keystore_client,
ttl_seconds=600,
cache=CacheTypeNo(NoCache())
)

import asyncio
asyncio.run(c.create_aws_kms_hierarchical_keyring(input))
