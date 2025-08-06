// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "DDBKeystoreOperations.dfy"
include "KMSKeystoreOperations.dfy"
include "ErrorMessages.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"

module GetKeys {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import opened StandardLibrary.UInt

  import Structure
  import KMSKeystoreOperations
  import DDBKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages
  import AtomicPrimitives

  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import KmsArn
  import HvUtils = HierarchicalVersionUtils

  predicate ValidateActiveKeyBranchKeyMaterials(
    item: Structure.BranchKeyContext,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetActiveBranchKeyOutput,
    expectedIdentifier: string
  )
    requires item[Structure.TYPE_FIELD] == Structure.BRANCH_KEY_ACTIVE_TYPE
  {
    && var branchKeyMaterials :=  Structure.ToBranchKeyMaterials(
                                    item,
                                    plainTextKey
                                  );
    && branchKeyMaterials.Success?
    && activeBranchKeyOutput.branchKeyMaterials == branchKeyMaterials.value
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyIdentifier == expectedIdentifier
  }

  predicate ValidateBranchKeyVersionBranchKeyMaterials(
    item: Structure.BranchKeyContext,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetBranchKeyVersionOutput,
    expectedIdentifier: string,
    actualBranchKeyVersion: string
  )
    requires Structure.BRANCH_KEY_TYPE_PREFIX < item[Structure.TYPE_FIELD]
  {
    && var branchKeyMaterials :=  Structure.ToBranchKeyMaterials(
                                    item,
                                    plainTextKey
                                  );
    && branchKeyMaterials.Success?
    && activeBranchKeyOutput.branchKeyMaterials == branchKeyMaterials.value
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyIdentifier == expectedIdentifier
    && UTF8.Encode(actualBranchKeyVersion).Success?
    && activeBranchKeyOutput.branchKeyMaterials.branchKeyVersion == UTF8.Encode(actualBranchKeyVersion).value
  }

  predicate ValidateBeaconKeyMaterials(
    beaconItem: Structure.BranchKeyContext,
    plainTextKey: seq<uint8>,
    activeBranchKeyOutput: Types.GetBeaconKeyOutput,
    expectedIdentifier: string
  )
    requires beaconItem[Structure.TYPE_FIELD] == Structure.BEACON_KEY_TYPE_VALUE
  {
    && var beaconKeyMaterials :=  Structure.ToBeaconKeyMaterials(
                                    beaconItem,
                                    plainTextKey
                                  );
    && beaconKeyMaterials.Success?
    && activeBranchKeyOutput.beaconKeyMaterials == beaconKeyMaterials.value
    && activeBranchKeyOutput.beaconKeyMaterials.beaconKeyIdentifier == expectedIdentifier
  }

  method  {:vcs_split_on_every_assert} GetActiveKeyAndUnwrap(
    input: Types.GetActiveBranchKeyInput,
    tableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.GetActiveBranchKeyOutput, Types.Error>)
    requires ddbClient.Modifies !! kmsClient.Modifies

    requires kmsClient.ValidState() && ddbClient.ValidState()
    requires ddbClient.Modifies !! kmsClient.Modifies
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
      //= type=implication
      //# To get the active version for the branch key id from the keystore
      //# this operation MUST call AWS DDB `GetItem`
      //# using the `branch-key-id` as the Partition Key and `"branch:ACTIVE"` value as the Sort Key.
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
            ]

    ensures output.Success? ==>
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && var activeItem := Seq.Last(ddbClient.History.GetItem).output.value.Item;
              && activeItem.Some?
              && Structure.ActiveBranchKeyItem?(activeItem.value)

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              // = type=implication
              // # GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && activeItem.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == input.branchKeyIdentifier
              && var encryptionContext := Structure.ToBranchKeyContext(activeItem.value, logicalKeyStoreName);

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              // = type=implication
              // # GetActiveBranchKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeItem.value[Structure.KMS_FIELD].S)
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
              // = type=implication
              // # The operation MUST decrypt the EncryptedHierarchicalKey according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.
              && var hv := activeItem.value[Structure.HIERARCHY_VERSION].N;
              && ValidateKmsDecryption(encryptionContext, activeItem.value, kmsConfiguration, grantTokens, kmsClient, hv)
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
                   //= type=implication
                   //# This GetActiveBranchKey MUST construct [branch key materials](./structures.md#branch-key-materials)
                   //# according to [Branch Key Materials From Authenticated Branch Key Context](#branch-key-materials-from-authenticated-branch-key-context).

                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
                   //= type=implication
                   //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
                   && ValidateActiveKeyBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && ValidateActiveKeyBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier)

                 else
                   false

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
      //= type=implication
      //# If the record does not contain the defined fields, this operation MUST fail.
      || (&& |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
          && Seq.Last(ddbClient.History.GetItem).output.Success?
          && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
          && !Structure.ActiveBranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
      //= type=implication
      //# If the branch key fails to decrypt, GetActiveBranchKey MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {
    var branchKeyItem :- DDBKeystoreOperations.GetActiveBranchKeyItem(
      input.branchKeyIdentifier,
      tableName,
      ddbClient
    );

    var encryptionContext := Structure.ToBranchKeyContext(branchKeyItem, logicalKeyStoreName);

    :- Need(
      KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    :- Need(
      KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT)
    );

    var branchKeyPlain :- DecryptBranchKeyItem(
      encryptionContext,
      branchKeyItem,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
      encryptionContext,
      branchKeyPlain
    );

    return Success(Types.GetActiveBranchKeyOutput(
                     branchKeyMaterials := branchKeyMaterials
                   ));

  }

  method GetBranchKeyVersion(
    input: Types.GetBranchKeyVersionInput,
    tableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.GetBranchKeyVersionOutput, Types.Error>)
    requires ddbClient.Modifies !! kmsClient.Modifies

    requires kmsClient.ValidState() && ddbClient.ValidState()
    requires ddbClient.Modifies !! kmsClient.Modifies
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
      //= type=implication
      //# To get a branch key from the keystore this operation MUST call AWS DDB `GetItem`
      //# using the `branch-key-id` as the Partition Key and "branch:version:" + `branchKeyVersion` value as the Sort Key.
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + input.branchKeyVersion)
            ]

    ensures output.Success? ==>
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && var versionItem := Seq.Last(ddbClient.History.GetItem).output.value.Item;
              && versionItem.Some?
              && Structure.VersionBranchKeyItem?(versionItem.value)

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              // = type=implication
              // # GetBranchKeyVersion MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && versionItem.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == input.branchKeyIdentifier
              && var encryptionContext := Structure.ToBranchKeyContext(versionItem.value, logicalKeyStoreName);

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              // = type=implication
              // # GetBranchKeyVersion MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              && var hv := encryptionContext[Structure.HIERARCHY_VERSION];
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
              //= type=implication
              //# The operation MUST decrypt the branch key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.

              && ValidateKmsDecryption(encryptionContext, versionItem.value, kmsConfiguration, grantTokens, kmsClient, hv)

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
                   //= type=implication
                   //# This GetBranchKeyVersion MUST construct [branch key materials](./structures.md#branch-key-materials)
                   //# according to [Branch Key Materials From Authenticated Branch Key Context](#branch-key-materials-from-authenticated-branch-key-context).

                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
                   //= type=implication
                   //# This operation MUST return the constructed [branch key materials](./structures.md#branch-key-materials).
                   ValidateBranchKeyVersionBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier, input.branchKeyVersion)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   ValidateBranchKeyVersionBranchKeyMaterials(encryptionContext, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier, input.branchKeyVersion)
                 else
                   false

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
      //= type=implication
      //# If the record does not contain the defined fields, this operation MUST fail.
      || (&& |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
          && Seq.Last(ddbClient.History.GetItem).output.Success?
          && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
          && !Structure.VersionBranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
      //= type=implication
      //# If the branch key fails to decrypt, this operation MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {

    var branchKeyItem :- DDBKeystoreOperations.GetVersionBranchKeyItem(
      input.branchKeyIdentifier,
      input.branchKeyVersion,
      tableName,
      ddbClient
    );

    var encryptionContext := Structure.ToBranchKeyContext(branchKeyItem, logicalKeyStoreName);

    :- Need(
      KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    :- Need(
      KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := "AWS KMS Key ARN does not match configured value")
    );

    var branchKeyPlain :- DecryptBranchKeyItem(
      encryptionContext,
      branchKeyItem,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var branchKeyMaterials :- Structure.ToBranchKeyMaterials(
      encryptionContext,
      branchKeyPlain
    );

    return Success(Types.GetBranchKeyVersionOutput(
                     branchKeyMaterials := branchKeyMaterials
                   ));
  }

  method DecryptAndValidateKeyForHV2(
    encryptionContext: Structure.EncryptionContextString,
    ciphertextBlob: seq<uint8>,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  ) returns (result: Result<seq<uint8>, Types.Error>)

    requires Structure.BranchKeyContext?(encryptionContext)

    requires HvUtils.IsValidHV2EC?(encryptionContext)

    requires KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD])

    requires KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])

    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    ensures result.Success?
            ==>
              && old(kmsClient.History.Encrypt) == kmsClient.History.Encrypt
              && old(kmsClient.History.GenerateDataKey) == kmsClient.History.GenerateDataKey

              && var kmsArnFromStorage := encryptionContext[Structure.KMS_FIELD];

              && var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(encryptionContext);

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, kmsArnFromStorage)

              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && old(kmsClient.History.Decrypt) < kmsClient.History.Decrypt
              && var kmsKeyArn := KMSKeystoreOperations.GetArn(kmsConfiguration, kmsArnFromStorage);
              && KMS.IsValid_CiphertextType(ciphertextBlob)
              && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV2?(
                   ciphertextBlob,
                   ecToKMS,
                   kmsArnFromStorage,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && result.value == decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..]
  {
    // Get encryption context for KMS

    // branchKeyItemFromStorage.EncryptionContext comes from storage and is not the actual encryption context that is send to KMS.
    // branchKeyItemFromStorage.EncryptionContext contains all the items in the dynamodb table and table name.
    var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(encryptionContext);

    // Decrypt the key using KMS
    var kmsDecryptRes :- KMSKeystoreOperations.DecryptKeyForHv2(
      ciphertextBlob,
      ecToKMS,
      encryptionContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    if (crypto?.Failure?) {
      var e := Types.KeyStoreException(
        message := "Local Cryptography error"
      );
      return Failure(e);
    }

    // Unpack the plaintext tuple
    var (protectedMdDigest, plainTextKey) :=
      HvUtils.UnpackPlainTextTuple(kmsDecryptRes.Plaintext.value);

    // Create and validate BKC digest
    var bkcFromStorage :- HvUtils.CreateBKCDigest(
      encryptionContext,
      crypto?.value
    );

    // Verify the digest matches
    if (bkcFromStorage != protectedMdDigest) {
      var e := Types.BranchKeyCiphertextException(
        message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED
      );
      return Failure(e);
    }

    // Return the plaintext key if all validations pass
    return Success(plainTextKey);
  }


  method {:vcs_split_on_every_assert} GetBeaconKeyAndUnwrap(
    input: Types.GetBeaconKeyInput,
    tableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.GetBeaconKeyOutput, Types.Error>)
    requires ddbClient.Modifies !! kmsClient.Modifies

    requires kmsClient.ValidState() && ddbClient.ValidState()
    requires ddbClient.Modifies !! kmsClient.Modifies
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
      //= type=implication
      //# To get a branch key from the keystore this operation MUST call AWS DDB `GetItem`
      //# using the `branch-key-id` as the Partition Key and "beacon:ACTIVE" value as the Sort Key.
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
            ]

    ensures output.Success? ==>
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && var beaconItem := Seq.Last(ddbClient.History.GetItem).output.value.Item;
              && beaconItem.Some?
              && Structure.BeaconKeyItem?(beaconItem.value)

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              // = type=implication
              // # GetBeaconKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && beaconItem.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == input.branchKeyIdentifier
              && var encryptionContext := Structure.ToBranchKeyContext(beaconItem.value, logicalKeyStoreName);

              // = aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              // = type=implication
              // # GetBeaconKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#discovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#mrdiscovery
              //= type=implication
              //# The Keystore MAY use the KMS Key ARNs already
              //# persisted to the backing DynamoDB table,
              //# provided they are in records created
              //# with an identical Logical Keystore Name.
              && (kmsConfiguration.kmsMRKeyArn? ==> encryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName)

              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
              //= type=implication
              //# The operation MUST decrypt the beacon key according to the [AWS KMS Branch Key Decryption](#aws-kms-branch-key-decryption) section.

              && var hv := encryptionContext[Structure.HIERARCHY_VERSION];

              && ValidateKmsDecryption(encryptionContext, beaconItem.value, kmsConfiguration, grantTokens, kmsClient, hv)

              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;

              && Structure.ToBeaconKeyMaterials(encryptionContext, decryptResponse.Plaintext.value).Success?

              && if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
                   //= type=implication
                   //# This GetBeaconKey MUST construct [beacon key materials](./structures.md#beacon-key-materials) from the decrypted branch key material
                   //# and the `branchKeyId` from the returned `branch-key-id` field.

                   //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
                   //= type=implication
                   //# This operation MUST return the constructed [beacon key materials](./structures.md#beacon-key-materials).
                   && ValidateBeaconKeyMaterials(encryptionContext, decryptResponse.Plaintext.value, output.value, input.branchKeyIdentifier)

                 else if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && ValidateBeaconKeyMaterials(encryptionContext, decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..], output.value, input.branchKeyIdentifier)

                 else
                   false

    ensures

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
      //= type=implication
      //# If the record does not contain the defined fields, this operation MUST fail.
      || (&& |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
          && Seq.Last(ddbClient.History.GetItem).output.Success?
          && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
          && !Structure.BeaconKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
      //= type=implication
      //# If the beacon key fails to decrypt, this operation MUST fail.
      || (&& |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
          && Seq.Last(kmsClient.History.Decrypt).output.Failure?
          ==> output.Failure?)
  {
    var branchKeyItem :- DDBKeystoreOperations.GetBeaconKeyItem(
      input.branchKeyIdentifier,
      tableName,
      ddbClient
    );

    var encryptionContext := Structure.ToBranchKeyContext(branchKeyItem, logicalKeyStoreName);

    :- Need(
      KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := ErrorMessages.RETRIEVED_KEYSTORE_ITEM_INVALID_KMS_ARN)
    );

    :- Need(
      KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException( message := "AWS KMS Key ARN does not match configured value")
    );

    :- Need(
      encryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 ||
      encryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2,
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_HIERARCHY_VERSION
      )
    );

    var branchKeyPlain :- DecryptBranchKeyItem(
      encryptionContext,
      branchKeyItem,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var branchKeyMaterials :- Structure.ToBeaconKeyMaterials(
      encryptionContext,
      branchKeyPlain
    );

    return Success(Types.GetBeaconKeyOutput(
                     beaconKeyMaterials := branchKeyMaterials
                   ));
  }


  predicate AwsKmsBranchKeyDecryption?(
    getItemHistory: DDB.DafnyCallEvent<DDB.GetItemInput, Result<DDB.GetItemOutput, DDB.Error>>,
    decryptHistory: KMS.DafnyCallEvent<KMS.DecryptRequest, Result<KMS.DecryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    logicalKeyStoreName: string
  )
    reads kmsClient.History
    reads ddbClient.History

    requires
      && getItemHistory.output.Success?
      && getItemHistory.output.value.Item.Some?
      && Structure.BranchKeyItem?(getItemHistory.output.value.Item.value)
      && getItemHistory.output.Success?
      && getItemHistory.output.value.Item.Some?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# The operation MUST use the configured `KMS SDK Client` to decrypt the value of the branch key field.
    requires decryptHistory in kmsClient.History.Decrypt
    requires getItemHistory in ddbClient.History.GetItem
  {
    var versionItem := getItemHistory.output.value.Item.value;
    var versionEncryptionContext := Structure.ToBranchKeyContext(versionItem, logicalKeyStoreName);

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# Every key in the constructed [branch key context](#branch-key-context)
    //# except `tableName`
    //# MUST exist as a attribute in the AWS DDB response item.
    && versionEncryptionContext.Keys - {Structure.TABLE_FIELD} < versionItem.Keys

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# Every value in the constructed [branch key context](#branch-key-context)
    //# except the logical table name
    //# MUST equal the value with the same key in the AWS DDB response item.
    && (forall k <- versionEncryptionContext.Keys - {Structure.TABLE_FIELD}
                    // Working around https://github.com/dafny-lang/dafny/issues/4214
                    //  that will make the following fail to compile
                    // :: match k
                    //    case HIERARCHY_VERSION => versionEncryptionContext[Structure.HIERARCHY_VERSION] == versionItem[Structure.HIERARCHY_VERSION].N
                    //    case _ => versionEncryptionContext[k] == versionItem[k].S)
          :: if k == Structure.HIERARCHY_VERSION then
               versionEncryptionContext[Structure.HIERARCHY_VERSION] == versionItem[Structure.HIERARCHY_VERSION].N
             else
               versionEncryptionContext[k] == versionItem[k].S)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# The key `enc` MUST NOT exist in the constructed [branch key context](#branch-key-context).
    && Structure.BRANCH_KEY_FIELD !in  versionEncryptionContext

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the Keystore's [AWS KMS Configuration](#aws-kms-configuration) is `KMS Key ARN` or `KMS MRKey ARN`,
    //# the `kms-arn` field of the DDB response item MUST be
    //# [compatible with](#aws-key-arn-compatibility) the configured KMS Key in
    //# the [AWS KMS Configuration](#aws-kms-configuration) for this keystore,
    //# or the operation MUST fail.
    && (kmsConfiguration.kmsKeyArn? ==> versionItem[Structure.KMS_FIELD].S == kmsConfiguration.kmsKeyArn)
    && (kmsConfiguration.kmsMRKeyArn? ==> KMSKeystoreOperations.MrkMatch(versionItem[Structure.KMS_FIELD].S, kmsConfiguration.kmsMRKeyArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the Keystore's [AWS KMS Configuration](#aws-kms-configuration) is `Discovery` or `MRDiscovery`,
    //# the `kms-arn` field of DDB response item MUST NOT be an Alias
    //# or the operation MUST fail.
    && (kmsConfiguration.discovery? ==> KmsArn.ValidKmsArn?(versionItem[Structure.KMS_FIELD].S))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# When calling [AWS KMS Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html),
    //# the keystore operation MUST call with a request constructed as follows:

    && var decryptRequest := decryptHistory.input;
    && decryptRequest.KeyId.Some?
       //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
       //= type=implication
       //# - `KeyId`, if the KMS Configuration is Discovery, MUST be the `kms-arn` attribute value of the AWS DDB response item.
    && (kmsConfiguration.discovery? ==> decryptRequest.KeyId == Some(versionItem[Structure.KMS_FIELD].S))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# If the KMS Configuration is MRDiscovery, `KeyId` MUST be the `kms-arn` attribute value of the AWS DDB response item, with the region replaced by the configured region.
    && (kmsConfiguration.mrDiscovery? ==> decryptRequest.KeyId == Some(KMSKeystoreOperations.replaceRegion(versionItem[Structure.KMS_FIELD].S, kmsConfiguration.mrDiscovery.region)))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# Otherwise, it MUST BE the Keystore's configured KMS Key.
    && (kmsConfiguration.kmsKeyArn? ==> decryptRequest.KeyId == Some(kmsConfiguration.kmsKeyArn))
    && (kmsConfiguration.kmsMRKeyArn? ==> KMSKeystoreOperations.MrkMatch(decryptRequest.KeyId.value, kmsConfiguration.kmsMRKeyArn))

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `CiphertextBlob` MUST be the `enc` attribute value on the AWS DDB response item
    && decryptRequest.CiphertextBlob == versionItem[Structure.BRANCH_KEY_FIELD].B

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# Every attribute except for `enc` on the AWS DDB response item
    //# MUST be authenticated in the decryption of `enc`

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `EncryptionContext` MUST be the [encryption context from authenticated branch key context](#encryption-context-from-authenticated-branch-key-context)
    && decryptRequest.EncryptionContext == Some(versionEncryptionContext)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-branch-key-decryption
    //= type=implication
    //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && decryptRequest.GrantTokens == Some(grantTokens)

    && decryptHistory.output.Success?
    && decryptHistory.output.value.Plaintext.Some?

  }

  predicate ValidateKmsDecryption(
    encryptionContext : Structure.EncryptionContextString,
    branchKeyItem : Structure.BranchKeyItem,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    hv: string
  )
    requires Structure.BranchKeyContext?(encryptionContext)
    requires 0 < |kmsClient.History.Decrypt|
    reads kmsClient.History
  {
    && ((hv == Structure.HIERARCHY_VERSION_VALUE_1) || (hv == Structure.HIERARCHY_VERSION_VALUE_2))

    && if hv == Structure.HIERARCHY_VERSION_VALUE_2 then

         && HvUtils.IsValidHV2EC?(encryptionContext)

         && var ciphertextBlob := branchKeyItem[Structure.BRANCH_KEY_FIELD].B;

         && var kmsArnFromStorage := encryptionContext[Structure.KMS_FIELD];

         && var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(encryptionContext);

         && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV2?(
           ciphertextBlob,
           ecToKMS,
           kmsArnFromStorage,
           kmsConfiguration,
           grantTokens,
           kmsClient,
           Seq.Last(kmsClient.History.Decrypt)
         )

       else if hv == Structure.HIERARCHY_VERSION_VALUE_1 then
         && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV1?(
           encryptionContext,
           branchKeyItem,
           kmsConfiguration,
           grantTokens,
           kmsClient,
           Seq.Last(kmsClient.History.Decrypt)
         )

       else false
  }

  method DecryptBranchKeyItem(
    encryptionContext : Structure.EncryptionContextString,
    branchKeyItem : Structure.BranchKeyItem,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient
  ) returns (result: Result<seq<uint8>, Types.Error>)
    requires kmsClient.ValidState()
    modifies kmsClient.Modifies
    ensures kmsClient.ValidState()

    requires Structure.BranchKeyContext?(encryptionContext)
    requires KmsArn.ValidKmsArn?(encryptionContext[Structure.KMS_FIELD])
    requires branchKeyItem == Structure.ToAttributeMap(encryptionContext, branchKeyItem[Structure.BRANCH_KEY_FIELD].B)
    requires KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, encryptionContext[Structure.KMS_FIELD])

    ensures result.Success?
            ==>
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1
              && var hv := encryptionContext[Structure.HIERARCHY_VERSION];
              && ValidateKmsDecryption(encryptionContext, branchKeyItem, kmsConfiguration, grantTokens, kmsClient, hv)
              && var decryptResponse := Seq.Last(kmsClient.History.Decrypt).output.value;
              && |result.value| == Structure.AES_256_LENGTH as int
              && if hv == Structure.HIERARCHY_VERSION_VALUE_2 then
                   && HvUtils.IsValidHV2EC?(encryptionContext)
                   && result.value == decryptResponse.Plaintext.value[Structure.BKC_DIGEST_LENGTH..]
                 else
                   && result.value == decryptResponse.Plaintext.value
  {
    if encryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_1 {
      var branchKey :- KMSKeystoreOperations.DecryptKey(
        encryptionContext,
        branchKeyItem,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
      return Success(branchKey.Plaintext.value);
    } else if encryptionContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2 {
      :- Need(
        HvUtils.IsValidHV2EC?(encryptionContext),
        Types.BranchKeyCiphertextException(
          message := ErrorMessages.INVALID_EC_FOUND
        )
      );
      result := DecryptAndValidateKeyForHV2(
        encryptionContext,
        branchKeyItem[Structure.BRANCH_KEY_FIELD].B,
        kmsConfiguration,
        grantTokens,
        kmsClient
      );
    } else {
      return Failure(Types.KeyStoreException(
                       message := ErrorMessages.INVALID_HIERARCHY_VERSION
                     ));
    }
  }
}
