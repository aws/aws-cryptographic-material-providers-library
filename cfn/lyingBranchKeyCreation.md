To validate that the MPL protects from Branch Keys lying about the KMS ARN used to encrypt it,
we need to create a "lying Branch Key".

The following commands were used to do so,
with the AWS CLI @ `aws-cli/2.15.60 Python/3.11.9 Darwin/22.6.0 source/x86_64`.

#### Set Common Variables:

```sh
createTime=`printf '%.26sZ\n' $(gdate -u +%FT%H:%M:%S:%N)`
branchKeyId="kms-arn-attribute-is-lying"
kmsArn="arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"
tableName="KeyStoreDdbTable"
type="branch:version:$(uuidgen | tr "[A-Z]" "[a-z]")"
```

#### KMS GenerateDataKeyWithoutPlaintext for DECRYPT_ONLY:

Execute the following, and persist the result as DECRYPT_ONY.json.

```sh
aws kms generate-data-key-without-plaintext \
    --key-id arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126 \
    --number-of-bytes 32 \
    --encryption-context "kms-arn=$kmsArn, branch-key-id=$branchKeyId, hierarchy-version=1, create-time=$createTime, tablename=$tableName, type=$type"
```

#### KMS ReEncrypt for ACTIVE

Execute the following, and persist the result as ACTIVE.json.

Set `cipherText` as the `"CipherTextBlob"` from DECRYPT_ONLY.json.

```sh
typeActive="branch:ACTIVE"
cipherText="<Set `cipherText` as the `"CipherTextBlob"` from DECRYPT_ONLY.json.>"
aws kms re-encrypt \
    --source-key-id arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126 \
    --destination-key-id arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126 \
    --source-encryption-context "kms-arn=$kmsArn, branch-key-id=$branchKeyId, hierarchy-version=1, create-time=$createTime, tablename=$tableName, type=$type" \
    --destination-encryption-context "kms-arn=$kmsArn, branch-key-id=$branchKeyId, hierarchy-version=1, create-time=$createTime, tablename=$tableName, type=$typeActive, version=$type" \
    --ciphertext-blob "$cipherText"
```

#### KMS GenerateDataKeyWithoutPlaintext for Beacon Key

Execute the following, and persist the result as BEACON.json.

```sh
type="beacon:ACTIVE"
aws kms generate-data-key-without-plaintext \
--key-id arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126 \
--number-of-bytes 32 \
--encryption-context "kms-arn=$kmsArn, branch-key-id=$branchKeyId, hierarchy-version=1, create-time=$createTime, tablename=$tableName, type=$type"
```

#### DynamoDB TransactWriteItems

Create a `items.json` file formatted as follows:

```json
[
    {
        "Put": {
            "TableName": "KeyStoreDdbTable",
            "Item": {
                "branch-key-id": {"S": "kms-arn-attribute-is-lying"},
                "type": {"S": <value of "$type">},
                "kms-arn": {"S": "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"},
                "hierarchy-version": {"N": "1"},
                "create-time": {"S": <value of "$createTime"},
                "enc": {"B":  <value of `"CipherTextBlob"` from DECRYPT_ONLY.json>}
            },
            "ConditionExpression" : "attribute_not_exists(#pk)",
            "ExpressionAttributeNames" : {"#pk": "branch-key-id"}
        }
    },
    {
        "Put": {
            "TableName": "KeyStoreDdbTable",
            "Item": {
                "branch-key-id": {"S": "kms-arn-attribute-is-lying"},
                "type": {"S": "branch:ACTIVE"},
                "kms-arn": {"S": "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"},
                "hierarchy-version": {"N": "1"},
                "create-time": {"S": <value of "$createTime"},
                "enc": {"B":  <value of `"CipherTextBlob"` from ACTIVE.json>},
                "version": {"S": <value of "$type">}
            },
            "ConditionExpression" : "attribute_not_exists(#pk)",
            "ExpressionAttributeNames" : {"#pk": "branch-key-id"}
        }
    },
    {
        "Put": {
            "TableName": "KeyStoreDdbTable",
            "Item": {
                "branch-key-id": {"S": "kms-arn-attribute-is-lying"},
                "type": {"S": "beacon:ACTIVE"},
                "kms-arn": {"S": "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8"},
                "hierarchy-version": {"N": "1"},
                "create-time": {"S": <value of "$createTime"},
                "enc": {"B":  <value of `"CipherTextBlob"` from BEACON.json>}
            },
            "ConditionExpression" : "attribute_not_exists(#pk)",
            "ExpressionAttributeNames" : {"#pk": "branch-key-id"}
        }
    }
]
```

Execute the TransactWriteItems request via:
`aws dynamodb transact-write-items file://items.json`.
