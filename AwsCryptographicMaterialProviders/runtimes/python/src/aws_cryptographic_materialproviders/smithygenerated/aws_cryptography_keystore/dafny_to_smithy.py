# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes import (
    KMSConfiguration_discovery,
    KMSConfiguration_kmsKeyArn,
    KMSConfiguration_kmsMRKeyArn,
    KMSConfiguration_mrDiscovery,
)
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models
from standard_library.internaldafny.generated import UTF8


def smithy_api_Unit():
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.Unit(
    )

def aws_cryptography_keystore_CreateKeyStoreInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyStoreInput(
    )

def aws_cryptography_keystore_CreateKeyInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyInput(
        branch_key_identifier=(dafny_input.branchKeyIdentifier.value.VerbatimString(False)) if (dafny_input.branchKeyIdentifier.is_Some) else None,
        encryption_context=({''.join(UTF8.default__.Decode(key).value.Elements): ''.join(UTF8.default__.Decode(value).value.Elements) for (key, value) in dafny_input.encryptionContext.value.items }) if (dafny_input.encryptionContext.is_Some) else None,
    )

def aws_cryptography_keystore_VersionKeyInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.VersionKeyInput(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
    )

def aws_cryptography_keystore_GetActiveBranchKeyInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetActiveBranchKeyInput(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
    )

def aws_cryptography_keystore_GetBranchKeyVersionInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBranchKeyVersionInput(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
        branch_key_version=dafny_input.branchKeyVersion.VerbatimString(False),
    )

def aws_cryptography_keystore_GetBeaconKeyInput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBeaconKeyInput(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
    )

def aws_cryptography_keystore_KMSConfiguration(dafny_input):
    # Convert KMSConfiguration
    if isinstance(dafny_input, KMSConfiguration_kmsKeyArn):
        KMSConfiguration_union_value = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsKeyArn(dafny_input.kmsKeyArn.VerbatimString(False))
    elif isinstance(dafny_input, KMSConfiguration_kmsMRKeyArn):
        KMSConfiguration_union_value = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationKmsMRKeyArn(dafny_input.kmsMRKeyArn.VerbatimString(False))
    elif isinstance(dafny_input, KMSConfiguration_discovery):
        KMSConfiguration_union_value = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationDiscovery(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_Discovery(dafny_input.discovery))
    elif isinstance(dafny_input, KMSConfiguration_mrDiscovery):
        KMSConfiguration_union_value = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.KMSConfigurationMrDiscovery(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_MRDiscovery(dafny_input.mrDiscovery))
    else:
        raise ValueError("No recognized union value in union type: " + str(dafny_input))

    return KMSConfiguration_union_value

def aws_cryptography_keystore_Discovery(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.Discovery(
    )

def aws_cryptography_keystore_MRDiscovery(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.MRDiscovery(
        region=dafny_input.region.VerbatimString(False),
    )

def aws_cryptography_keystore_GetKeyStoreInfoOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetKeyStoreInfoOutput(
        key_store_id=dafny_input.keyStoreId.VerbatimString(False),
        key_store_name=dafny_input.keyStoreName.VerbatimString(False),
        logical_key_store_name=dafny_input.logicalKeyStoreName.VerbatimString(False),
        grant_tokens=[list_element.VerbatimString(False) for list_element in dafny_input.grantTokens],
        kms_configuration=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KMSConfiguration(dafny_input.kmsConfiguration),
    )

def aws_cryptography_keystore_CreateKeyStoreOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyStoreOutput(
        table_arn=dafny_input.tableArn.VerbatimString(False),
    )

def aws_cryptography_keystore_CreateKeyOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyOutput(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
    )

def aws_cryptography_keystore_VersionKeyOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.VersionKeyOutput(
    )

def aws_cryptography_keystore_BranchKeyMaterials(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.BranchKeyMaterials(
        branch_key_identifier=dafny_input.branchKeyIdentifier.VerbatimString(False),
        branch_key_version=''.join(UTF8.default__.Decode(dafny_input.branchKeyVersion).value.Elements),
        encryption_context={''.join(UTF8.default__.Decode(key).value.Elements): ''.join(UTF8.default__.Decode(value).value.Elements) for (key, value) in dafny_input.encryptionContext.items },
        branch_key=bytes(dafny_input.branchKey),
    )

def aws_cryptography_keystore_GetActiveBranchKeyOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetActiveBranchKeyOutput(
        branch_key_materials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BranchKeyMaterials(dafny_input.branchKeyMaterials),
    )

def aws_cryptography_keystore_GetBranchKeyVersionOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBranchKeyVersionOutput(
        branch_key_materials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BranchKeyMaterials(dafny_input.branchKeyMaterials),
    )

def aws_cryptography_keystore_BeaconKeyMaterials(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.BeaconKeyMaterials(
        beacon_key_identifier=dafny_input.beaconKeyIdentifier.VerbatimString(False),
        encryption_context={''.join(UTF8.default__.Decode(key).value.Elements): ''.join(UTF8.default__.Decode(value).value.Elements) for (key, value) in dafny_input.encryptionContext.items },
        beacon_key=(bytes(dafny_input.beaconKey.value)) if (dafny_input.beaconKey.is_Some) else None,
        hmac_keys=({key.VerbatimString(False): bytes(value) for (key, value) in dafny_input.hmacKeys.value.items }) if (dafny_input.hmacKeys.is_Some) else None,
    )

def aws_cryptography_keystore_GetBeaconKeyOutput(dafny_input):
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBeaconKeyOutput(
        beacon_key_materials=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_BeaconKeyMaterials(dafny_input.beaconKeyMaterials),
    )

def aws_cryptography_keystore_DdbClientReference(dafny_input):
    return dafny_input._impl

def aws_cryptography_keystore_KmsClientReference(dafny_input):
    return dafny_input._impl

def aws_cryptography_keystore_KeyStoreConfig(dafny_input):
    # Deferred import of .config to avoid circular dependency
    import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.config
    return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.config.KeyStoreConfig(
        ddb_table_name=dafny_input.ddbTableName.VerbatimString(False),
        kms_configuration=aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KMSConfiguration(dafny_input.kmsConfiguration),
        logical_key_store_name=dafny_input.logicalKeyStoreName.VerbatimString(False),
        id=(dafny_input.id.value.VerbatimString(False)) if (dafny_input.id.is_Some) else None,
        grant_tokens=([list_element.VerbatimString(False) for list_element in dafny_input.grantTokens.value]) if (dafny_input.grantTokens.is_Some) else None,
        ddb_client=(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_DdbClientReference(dafny_input.ddbClient.UnwrapOr(None))) if (dafny_input.ddbClient.UnwrapOr(None) is not None) else None,
        kms_client=(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_KmsClientReference(dafny_input.kmsClient.UnwrapOr(None))) if (dafny_input.kmsClient.UnwrapOr(None) is not None) else None,
    )
