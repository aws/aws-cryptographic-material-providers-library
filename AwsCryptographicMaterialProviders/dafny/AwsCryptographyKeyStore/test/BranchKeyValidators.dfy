// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"

// methods to validate a Get* Branch Key result from the Branch Key Store client
module {:options "/functionSyntax:4" } BranchKeyValidators {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import UTF8
  import UUID
  import Types = AwsCryptographyKeyStoreTypes

  method VerifyGetKeys(
    identifier : string,
    keyStore : Types.IKeyStoreClient,
    storage : Types.IKeyStorageInterface,
    nameonly versionUtf8Bytes?: Option<seq<uint8>> := None,
    nameonly encryptionContext : Types.EncryptionContext := map[]
  )
    requires
      keyStore.ValidState() && storage.ValidState()
    modifies
      keyStore.Modifies, storage.Modifies
    ensures
      keyStore.ValidState() && storage.ValidState()

  {
    var _ := testBeaconKeyHappyCase(
      keyStore := keyStore,
      branchKeyId := identifier,
      encryptionContext := encryptionContext
    );

    var activeResult := testActiveBranchKeyHappyCase(
      keyStore := keyStore,
      branchKeyId := identifier,
      encryptionContext := encryptionContext
    );
    var versionString :- expect UTF8.Decode(activeResult.branchKeyVersion);

    var _ := testBranchKeyVersionHappyCase(
      keyStore := keyStore,
      branchKeyId := identifier,
      branchKeyIdActiveVersion := versionString,
      branchKeyIdActiveVersionUtf8Bytes := activeResult.branchKeyVersion,
      encryptionContext := encryptionContext
    );
    VerifyGetKeysFromStorage(identifier, storage);

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var versionByteUUID :- expect UUID.ToByteArray(versionString);
    var versionRoundTrip :- expect UUID.FromByteArray(versionByteUUID);
    expect versionRoundTrip == versionString;
  }


  method VerifyGetKeysFromStorage(
    identifier : string,
    storage : Types.IKeyStorageInterface
  )
    requires storage.ValidState()
    modifies storage.Modifies
    ensures storage.ValidState()
  {
    var encryptedActiveFromStorage :- expect storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := identifier
      )
    );

    var encryptedBeaconFromStorage :- expect storage.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(
        Identifier := identifier
      )
    );

    expect encryptedActiveFromStorage.Item.Type.ActiveHierarchicalSymmetricVersion?;

    var encryptedVersionFromStorage :- expect storage.GetEncryptedBranchKeyVersion(
      Types.GetEncryptedBranchKeyVersionInput(
        Identifier := identifier,
        Version := encryptedActiveFromStorage.Item.Type.ActiveHierarchicalSymmetricVersion.Version
      )
    );

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    expect ISO8601?(encryptedActiveFromStorage.Item.CreateTime);
    expect ISO8601?(encryptedBeaconFromStorage.Item.CreateTime);
    expect ISO8601?(encryptedVersionFromStorage.Item.CreateTime);
  }

  method testActiveBranchKeyHappyCase(
    keyStore: Types.IKeyStoreClient,
    branchKeyId: string,
    nameonly versionUtf8Bytes?: Option<seq<uint8>> := None,
    nameonly encryptionContext : Types.EncryptionContext := map[]
  ) returns (output: Types.BranchKeyMaterials)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect isValidActiveBranchKeyResult?(activeResult, branchKeyId, encryptionContext, versionUtf8Bytes?);
    return activeResult.branchKeyMaterials;
  }

  method testBranchKeyVersionHappyCase(
    keyStore: Types.IKeyStoreClient,
    branchKeyId: string,
    branchKeyIdActiveVersion: string,
    branchKeyIdActiveVersionUtf8Bytes: seq<uint8>,
    nameonly encryptionContext : Types.EncryptionContext := map[]
  ) returns (output: Types.BranchKeyMaterials)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));
    expect isValidBranchKeyVersionResult?(versionResult, branchKeyId, encryptionContext, branchKeyIdActiveVersionUtf8Bytes);
    return versionResult.branchKeyMaterials;
  }

  method testBeaconKeyHappyCase(
    keyStore: Types.IKeyStoreClient,
    branchKeyId: string,
    nameonly encryptionContext : Types.EncryptionContext := map[]
  ) returns (output: Types.BeaconKeyMaterials)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect isValidBeaconResult?(beaconKeyResult, branchKeyId, encryptionContext);
    return beaconKeyResult.beaconKeyMaterials;
  }

  predicate isValidBeaconResult?(
    beaconKeyResult: Types.GetBeaconKeyOutput,
    branchKeyId: string,
    encryptionContext : Types.EncryptionContext
  ) {
    && beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier == branchKeyId
    && beaconKeyResult.beaconKeyMaterials.beaconKey.Some?
    && |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32
    && beaconKeyResult.beaconKeyMaterials.encryptionContext == encryptionContext
  }

  predicate isValidActiveBranchKeyResult?(
    branchKeyResult: Types.GetActiveBranchKeyOutput,
    branchKeyId: string,
    encryptionContext : Types.EncryptionContext,
    branchKeyIdActiveVersionUtf8Bytes: Option<seq<uint8>>
  )
  {
    && branchKeyResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId
    && (branchKeyIdActiveVersionUtf8Bytes.None? ||
        branchKeyResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes.value)
    && |branchKeyResult.branchKeyMaterials.branchKey| == 32
    && branchKeyResult.branchKeyMaterials.encryptionContext == encryptionContext
  }

  predicate isValidBranchKeyVersionResult?(
    versionResult: Types.GetBranchKeyVersionOutput,
    branchKeyId: string,
    encryptionContext : Types.EncryptionContext,
    branchKeyIdActiveVersionUtf8Bytes: seq<uint8>
  )
  {
    && versionResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId
    && versionResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes
    && |versionResult.branchKeyMaterials.branchKey| == 32
    && versionResult.branchKeyMaterials.encryptionContext == encryptionContext
  }

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=test
  //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
  lemma ISO8601Test()
  {
    assert ISO8601?("2024-08-06T17:23:25.000874Z");
  }

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=test
  //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
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