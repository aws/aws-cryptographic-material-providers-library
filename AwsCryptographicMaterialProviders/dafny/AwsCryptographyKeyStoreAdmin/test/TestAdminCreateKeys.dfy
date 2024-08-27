// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"

module {:options "/functionSyntax:4" } TestAdminCreateKeys {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultEncryptedKeyStore
  import opened Wrappers
  import opened Fixtures
  import UUID
  import CleanupItems

  method {:test} TestCreateBranchAndBeaconKeys()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var storage := new DefaultEncryptedKeyStore.DynamoDBEncryptedKeyStore(
      ddbTableName := branchKeyStoreName,
      ddbClient := ddbClient,
      logicalKeyStoreName := logicalKeyStoreName
    );
    var keyStoreAdminConfig := Types.KeyStoreAdminConfig(
      logicalKeyStoreName := logicalKeyStoreName,
      storage := KeyStoreTypes.Storage.custom(storage)
    );
    var underTest :- expect KeyStoreAdmin.KeyStoreAdmin(keyStoreAdminConfig);
    var keyId := Types.KMSIdentifier.kmsKeyArn(keyArn);
    var branchKeyId :- expect underTest.CreateKey(Types.CreateKeyInput(
                                                    branchKeyIdentifier := None,
                                                    encryptionContext := None,
                                                    kmsArn := Types.KMSIdentifier.kmsKeyArn(keyArn),
                                                    kmsClient := kmsClient
                                                  ));

    var keyStoreConfig := KeyStoreTypes.KeyStoreConfig(
      id := None,
      kmsConfiguration := KeyStoreTypes.KMSConfiguration.kmsKeyArn(keyArn),
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        KeyStoreTypes.ddb(
          KeyStoreTypes.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        KeyStoreTypes.kms(
          KeyStoreTypes.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    // TODO: The rest of this is a copy/paste from KeyStore/test/TestCreateKeys.dfy
    // We should abstract and consolidate
    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      KeyStoreTypes.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var activeResult :- expect keyStore.GetActiveBranchKey(
      KeyStoreTypes.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var branchKeyVersion :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        branchKeyVersion := branchKeyVersion
      ));

    var encryptedActive :- expect keyStore.config.storage.GetEncryptedActiveBranchKey(
      KeyStoreTypes.GetEncryptedActiveBranchKeyInput(
        Identifier := branchKeyId.branchKeyIdentifier
      )
    );

    var encryptedVersion :- expect keyStore.config.storage.GetEncryptedBranchKeyVersion(
      KeyStoreTypes.GetEncryptedBranchKeyVersionInput(
        Identifier := branchKeyId.branchKeyIdentifier,
        Version := encryptedActive.Item.Type.ActiveHierarchicalSymmetricVersion
      )
    );

    var encryptedBeacon :- expect keyStore.config.storage.GetEncryptedBeaconKey(
      KeyStoreTypes.GetEncryptedBeaconKeyInput(
        Identifier := branchKeyId.branchKeyIdentifier
      )
    );

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    expect ISO8601?(encryptedActive.Item.CreateTime);
    expect ISO8601?(encryptedVersion.Item.CreateTime);
    expect ISO8601?(encryptedBeacon.Item.CreateTime);

    // Since this process uses a read DDB table,
    // the number of records will forever increase.
    // To avoid this, remove the items.
    CleanupItems.DeleteVersion(branchKeyId.branchKeyIdentifier, branchKeyVersion, ddbClient);
    CleanupItems.DeleteActive(branchKeyId.branchKeyIdentifier, ddbClient);

    expect beaconKeyResult.beaconKeyMaterials.beaconKey.Some?;
    expect |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;
    expect versionResult.branchKeyMaterials.branchKey == activeResult.branchKeyMaterials.branchKey;
    expect versionResult.branchKeyMaterials.branchKeyIdentifier
        == activeResult.branchKeyMaterials.branchKeyIdentifier
        == beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier;
    expect versionResult.branchKeyMaterials.branchKeyVersion == activeResult.branchKeyMaterials.branchKeyVersion;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=test
    //# If no branch key id is provided,
    //# then this operation MUST create a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    //# to be used as the branch key id.
    var idByteUUID :- expect UUID.ToByteArray(activeResult.branchKeyMaterials.branchKeyIdentifier);
    var idRoundTrip :- expect UUID.FromByteArray(idByteUUID);
    expect idRoundTrip == activeResult.branchKeyMaterials.branchKeyIdentifier;


    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var versionString :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionByteUUID :- expect UUID.ToByteArray(versionString);
    var versionRoundTrip :- expect UUID.FromByteArray(versionByteUUID);
    expect versionRoundTrip == versionString;
  }

  predicate ISO8601?(
    CreateTime: string
  )
  {
    // “YYYY-MM-DDTHH:mm:ss.ssssssZ“
    && |CreateTime| == 27
    && CreateTime[4] == '-'
    && CreateTime[7] == '-'
    && CreateTime[10] == 'T'
    && CreateTime[13] == ':'
    && CreateTime[16] == ':'
    && CreateTime[19] == '.'
    && CreateTime[26] == 'Z'
  }
}
