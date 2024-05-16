# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    BeaconKeyMaterials_BeaconKeyMaterials as DafnyBeaconKeyMaterials,
    BranchKeyMaterials_BranchKeyMaterials as DafnyBranchKeyMaterials,
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    CreateKeyStoreInput_CreateKeyStoreInput as DafnyCreateKeyStoreInput,
    CreateKeyStoreOutput_CreateKeyStoreOutput as DafnyCreateKeyStoreOutput,
    GetActiveBranchKeyInput_GetActiveBranchKeyInput as DafnyGetActiveBranchKeyInput,
    GetActiveBranchKeyOutput_GetActiveBranchKeyOutput as DafnyGetActiveBranchKeyOutput,
    GetBeaconKeyInput_GetBeaconKeyInput as DafnyGetBeaconKeyInput,
    GetBeaconKeyOutput_GetBeaconKeyOutput as DafnyGetBeaconKeyOutput,
    GetBranchKeyVersionInput_GetBranchKeyVersionInput as DafnyGetBranchKeyVersionInput,
    GetBranchKeyVersionOutput_GetBranchKeyVersionOutput as DafnyGetBranchKeyVersionOutput,
    GetKeyStoreInfoOutput_GetKeyStoreInfoOutput as DafnyGetKeyStoreInfoOutput,
    KMSConfiguration_kmsKeyArn,
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
import aws_cryptographic_materialproviders.internaldafny.generated.module_
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes import (
    IDynamoDBClient,
)
import com_amazonaws_dynamodb.internaldafny.generated.module_
from com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes import IKMSClient
import com_amazonaws_kms.internaldafny.generated.module_
from standard_library.internaldafny.generated import UTF8
from standard_library.internaldafny.generated.Wrappers import Option_None, Option_Some


def smithy_api_Unit(native_input):
    return None

def aws_cryptography_keystore_CreateKeyStoreInput(native_input):
    return DafnyCreateKeyStoreInput(
    )

def aws_cryptography_keystore_CreateKeyInput(native_input):
    return DafnyCreateKeyInput(
        branchKeyIdentifier=((Option_Some(Seq(native_input.branch_key_identifier))) if (native_input.branch_key_identifier is not None) else (Option_None())),
        encryptionContext=((Option_Some(Map({UTF8.default__.Encode(Seq(key)).value: UTF8.default__.Encode(Seq(value)).value for (key, value) in native_input.encryption_context.items() }))) if (native_input.encryption_context is not None) else (Option_None())),
    )

def aws_cryptography_keystore_VersionKeyInput(native_input):
    return DafnyVersionKeyInput(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
    )

def aws_cryptography_keystore_GetActiveBranchKeyInput(native_input):
    return DafnyGetActiveBranchKeyInput(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
    )

def aws_cryptography_keystore_GetBranchKeyVersionInput(native_input):
    return DafnyGetBranchKeyVersionInput(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
        branchKeyVersion=Seq(native_input.branch_key_version),
    )

def aws_cryptography_keystore_GetBeaconKeyInput(native_input):
    return DafnyGetBeaconKeyInput(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
    )

def aws_cryptography_keystore_GetKeyStoreInfoOutput(native_input):
    return DafnyGetKeyStoreInfoOutput(
        keyStoreId=Seq(native_input.key_store_id),
        keyStoreName=Seq(native_input.key_store_name),
        logicalKeyStoreName=Seq(native_input.logical_key_store_name),
        grantTokens=Seq([Seq(list_element) for list_element in native_input.grant_tokens]),
        kmsConfiguration=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KMSConfiguration(native_input.kms_configuration),
    )

def aws_cryptography_keystore_KMSConfiguration(native_input):
    if isinstance(native_input, aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsKeyArn):
        KMSConfiguration_union_value = KMSConfiguration_kmsKeyArn(Seq(native_input.value))
    else:
        raise ValueError("No recognized union value in union type: " + str(native_input))

    return KMSConfiguration_union_value

def aws_cryptography_keystore_CreateKeyStoreOutput(native_input):
    return DafnyCreateKeyStoreOutput(
        tableArn=Seq(native_input.table_arn),
    )

def aws_cryptography_keystore_CreateKeyOutput(native_input):
    return DafnyCreateKeyOutput(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
    )

def aws_cryptography_keystore_VersionKeyOutput(native_input):
    return DafnyVersionKeyOutput(
    )

def aws_cryptography_keystore_GetActiveBranchKeyOutput(native_input):
    return DafnyGetActiveBranchKeyOutput(
        branchKeyMaterials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BranchKeyMaterials(native_input.branch_key_materials),
    )

def aws_cryptography_keystore_BranchKeyMaterials(native_input):
    return DafnyBranchKeyMaterials(
        branchKeyIdentifier=Seq(native_input.branch_key_identifier),
        branchKeyVersion=UTF8.default__.Encode(Seq(native_input.branch_key_version)).value,
        encryptionContext=Map({UTF8.default__.Encode(Seq(key)).value: UTF8.default__.Encode(Seq(value)).value for (key, value) in native_input.encryption_context.items() }),
        branchKey=Seq(native_input.branch_key),
    )

def aws_cryptography_keystore_GetBranchKeyVersionOutput(native_input):
    return DafnyGetBranchKeyVersionOutput(
        branchKeyMaterials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BranchKeyMaterials(native_input.branch_key_materials),
    )

def aws_cryptography_keystore_GetBeaconKeyOutput(native_input):
    return DafnyGetBeaconKeyOutput(
        beaconKeyMaterials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_BeaconKeyMaterials(native_input.beacon_key_materials),
    )

def aws_cryptography_keystore_BeaconKeyMaterials(native_input):
    return DafnyBeaconKeyMaterials(
        beaconKeyIdentifier=Seq(native_input.beacon_key_identifier),
        encryptionContext=Map({UTF8.default__.Encode(Seq(key)).value: UTF8.default__.Encode(Seq(value)).value for (key, value) in native_input.encryption_context.items() }),
        beaconKey=((Option_Some(Seq(native_input.beacon_key))) if (native_input.beacon_key is not None) else (Option_None())),
        hmacKeys=((Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input.hmac_keys.items() }))) if (native_input.hmac_keys is not None) else (Option_None())),
    )

def aws_cryptography_keystore_KeyStoreConfig(native_input):
    return DafnyKeyStoreConfig(
        ddbTableName=Seq(native_input.ddb_table_name),
        kmsConfiguration=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KMSConfiguration(native_input.kms_configuration),
        logicalKeyStoreName=Seq(native_input.logical_key_store_name),
        id=((Option_Some(Seq(native_input.id))) if (native_input.id is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in native_input.grant_tokens]))) if (native_input.grant_tokens is not None) else (Option_None())),
        ddbClient=((Option_Some(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DdbClientReference(native_input.ddb_client))) if ((native_input.ddb_client is not None) and (aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_DdbClientReference(native_input.ddb_client) is not None)) else (Option_None())),
        kmsClient=((Option_Some(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KmsClientReference(native_input.kms_client))) if ((native_input.kms_client is not None) and (aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_KmsClientReference(native_input.kms_client) is not None)) else (Option_None())),
    )

def aws_cryptography_keystore_DdbClientReference(native_input):
    import com_amazonaws_dynamodb.internaldafny.generated.KeyStore
    client = com_amazonaws_dynamodb.internaldafny.generated.KeyStore.default__.DynamoDBClient(boto_client = native_input)
    client.value.impl = native_input
    return client.value

def aws_cryptography_keystore_KmsClientReference(native_input):
    import com_amazonaws_kms.internaldafny.generated.KeyStore
    client = com_amazonaws_kms.internaldafny.generated.KeyStore.default__.KMSClient(boto_client = native_input)
    client.value.impl = native_input
    return client.value
