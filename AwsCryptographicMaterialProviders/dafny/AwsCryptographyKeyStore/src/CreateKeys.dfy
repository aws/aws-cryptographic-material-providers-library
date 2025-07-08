// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "DDBKeystoreOperations.dfy"
include "KMSKeystoreOperations.dfy"
include "ErrorMessages.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"

module {:options "/functionSyntax:4" } CreateKeys {
  import opened StandardLibrary
  import opened Wrappers

  import Structure
  import KMSKeystoreOperations
  import DDBKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import AwsArnParsing
  import KmsArn
  import HvUtils = HierarchicalVersionUtils
  import GetKeys

  type material = m: seq<uint8> | |m| == 32 witness *
  datatype BKMaterialPair = | BKMaterialPair(
    nameonly bk: material,
    nameonly beacon: material
  )
  datatype BKCiphertextPair = | BKCiphertextPair(
    nameonly decryptOnly: seq<uint8>,
    nameonly encryptOnly: seq<uint8>
  )

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=implication
  //# To create a branch key, this operation MUST take the following:
  //#
  //# - `branchKeyId`: The identifier
  //# - `encryptionContext`: Additional encryption context to bind to the created keys

  //  - `kmsKeyArn`: KMS key ARN used to create keys
  method {:vcs_split_on_every_assert} CreateBranchAndBeaconKeys(
    branchKeyIdentifier: string,
    customEncryptionContext: map<string, string>,
    timestamp: string,
    branchKeyVersion: string,
    ddbTableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires 0 < |branchKeyIdentifier|
    requires 0 < |branchKeyVersion|
    requires forall k <- customEncryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    requires ddbClient.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires kmsClient.ValidState() && ddbClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# This operation MUST create a [branch key](structures.md#branch-key) and a [beacon key](structures.md#beacon-key) according to
    //# the [Branch Key and Beacon Key Creation](#branch-key-and-beacon-key-creation) section.
    ensures output.Success?
            ==>

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2

              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1

              && var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
                                                       branchKeyIdentifier,
                                                       branchKeyVersion,
                                                       timestamp,
                                                       logicalKeyStoreName,
                                                       KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                                                       Types.HierarchyVersion.v1,
                                                       customEncryptionContext
                                                     );

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#logical-keystore-name
              //= type=implication
              //# The logical keystore name MUST be bound to every created key.
              && decryptOnlyEncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              && WrappedBranchKeyCreation?(
                   Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)),
                   Seq.Last(kmsClient.History.ReEncrypt),
                   kmsClient,
                   kmsConfiguration,
                   grantTokens,
                   decryptOnlyEncryptionContext
                 )

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
              && var beaconKmsInput := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, beaconKmsInput.KeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `NumberOfBytes` MUST be 32.
              && beaconKmsInput.NumberOfBytes == Some(32)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `EncryptionContext` MUST be the [encryption context for beacon keys](#beacon-key-encryption-context).
              && beaconKmsInput.EncryptionContext == Some(Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext))

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# - `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && beaconKmsInput.GrantTokens == Some(grantTokens)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
              //= type=implication
              //# If creation of the keys are successful,
              //# the operation MUST call Amazon DynamoDB TransactWriteItems according to the [write key material](#writing-branch-key-and-beacon-key-to-key-store) section.

              && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Success?
              && var beaconKmsOutput := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value;
              && beaconKmsOutput.CiphertextBlob.Some?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-keystore
              //= type=implication
              //# To add the branch keys and a beacon key to the keystore the
              //# operation MUST call [Amazon DynamoDB API TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html).

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-keystore
              //= type=implication
              //# The call to Amazon DynamoDB TransactWriteItems MUST use the configured Amazon DynamoDB Client to make the call.

              && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-keystore
              //= type=implication
              //# The operation MUST call Amazon DynamoDB TransactWriteItems with a request constructed as follows:
              && var writeNewKey := Seq.Last(ddbClient.History.TransactWriteItems).input;

              && 3 == |writeNewKey.TransactItems|

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-keystore
              //= type=implication
              //# - Every key-value pair of the custom [encryption context](./structures.md#encryption-context-3) that is associated with the branch key
              //# MUST be added with an Attribute Name of `aws-crypto-ec:` + the Key and Attribute Value (S) of the value.
              && (forall k <- customEncryptionContext ::
                    && Structure.ENCRYPTION_CONTEXT_PREFIX + k in decryptOnlyEncryptionContext
                    && decryptOnlyEncryptionContext[Structure.ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k])

              && writeNewKey.TransactItems[0].Put.Some?
              && writeNewKey.TransactItems[0].Put.value.Item
                 == Structure.ToAttributeMap(
                      decryptOnlyEncryptionContext,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
                      //# as the wrapped DECRYPT_ONLY Branch Key.
                      Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.value.CiphertextBlob.value)

              && writeNewKey.TransactItems[1].Put.Some?
              && writeNewKey.TransactItems[1].Put.value.Item
                 == Structure.ToAttributeMap(
                      Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext),
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS ReEncrypt succeeds,
                      //# the operation MUST use the ReEncrypt result `CiphertextBlob`
                      //# as the wrapped ACTIVE Branch Key.
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value)

              && writeNewKey.TransactItems[2].Put.Some?
              && writeNewKey.TransactItems[2].Put.value.Item
                 == Structure.ToAttributeMap(
                      Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext),
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the `CiphertextBlob` as the wrapped Beacon Key.
                      beaconKmsOutput.CiphertextBlob.value)

              && Seq.Last(ddbClient.History.TransactWriteItems).output.Success?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
              //= type=implication
              //# If writing to the keystore succeeds,
              //# the operation MUST return the branch-key-id that maps to both
              //# the branch key and the beacon key.
              && output.value.branchKeyIdentifier == branchKeyIdentifier


    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# Otherwise, this operation MUST yield an error.
    ensures

      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
          && Seq.Last(ddbClient.History.TransactWriteItems).output.Failure?
          ==> output.Failure?)

  {

    var decryptOnlyEncryptionContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      Types.HierarchyVersion.v1,
      customEncryptionContext
    );
    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);
    var beaconEncryptionContext := Structure.BeaconKeyEncryptionContext(decryptOnlyEncryptionContext);

    :- Need(KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyEncryptionContext[Structure.KMS_FIELD]),
            Types.KeyStoreException(message := "Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext in CreateBranchAndBeaconKeys."));
    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.GenerateKey(
      decryptOnlyEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    :- Need(KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeEncryptionContext[Structure.KMS_FIELD]),
            Types.KeyStoreException(message := "Invalid KMS Key ARN configured for ReEncrypt in CreateBranchAndBeaconKeys."));
    var wrappedActiveBranchKey :- KMSKeystoreOperations.ReEncryptKey(
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value,
      decryptOnlyEncryptionContext,
      activeEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    :- Need(KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconEncryptionContext[Structure.KMS_FIELD]),
            Types.KeyStoreException(message := "Invalid KMS Key ARN configured for GenerateDataKeyWithoutPlaintext(beacon key) in CreateBranchAndBeaconKeys."));
    var wrappedBeaconKey :- KMSKeystoreOperations.GenerateKey(
      beaconEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );


    var decryptOnlyBranchKeyItem := Structure.ToAttributeMap(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );
    var activeBranchKeyItem := Structure.ToAttributeMap(
      activeEncryptionContext,
      wrappedActiveBranchKey.CiphertextBlob.value
    );
    var beaconKeyItem := Structure.ToAttributeMap(
      beaconEncryptionContext,
      wrappedBeaconKey.CiphertextBlob.value
    );

    var _ :- DDBKeystoreOperations.WriteNewKeyToStore(
      decryptOnlyBranchKeyItem,
      activeBranchKeyItem,
      beaconKeyItem,
      ddbTableName,
      ddbClient
    );

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := branchKeyIdentifier
      ));
  }

  /* Common KMS Requirements for VersionKey and CreateKey operations. */
  predicate HV2CreateKMSCommon(
    nameonly kmsConfiguration: Types.KMSConfiguration
  ): (output: bool)
    ensures output ==>
              && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
              && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
  {
    && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
    && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
  }

  twostate predicate HV2EncryptionOfBranchKeyAreCorrect(
    nameonly new decryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly new encryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly grantTokens: KMS.GrantTokenList,
    nameonly kmsClient: KMS.IKMSClient,
    nameonly material: seq<uint8>
  )
    reads kmsClient.History
    requires
      && kmsClient.ValidState()
      && HV2CreateKMSCommon(kmsConfiguration := kmsConfiguration)
      && decryptOnlyKMSEnc in kmsClient.History.Encrypt
      && encryptOnlyKMSEnc in kmsClient.History.Encrypt
  {
    var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    && decryptOnlyKMSEnc.output.Success? && encryptOnlyKMSEnc.output.Success?
    && decryptOnlyKMSEnc.input.EncryptionContext == encryptOnlyKMSEnc.input.EncryptionContext == Some(encryptionContext)
    && decryptOnlyKMSEnc.input.KeyId == encryptOnlyKMSEnc.input.KeyId == kmsKeyArn
    && decryptOnlyKMSEnc.input.GrantTokens == encryptOnlyKMSEnc.input.GrantTokens == Some(grantTokens)
    && |decryptOnlyKMSEnc.input.Plaintext| == |encryptOnlyKMSEnc.input.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && decryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == encryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == material
    && decryptOnlyKMSEnc.output.value.CiphertextBlob.Some? && encryptOnlyKMSEnc.output.value.CiphertextBlob.Some?
  }

  twostate predicate HV2GenerationOfBeaconAndBranchKeyAreCorrect(
    nameonly new bkGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly new beaconGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly kmsClient: KMS.IKMSClient
  )
    reads kmsClient.History
    requires
      && kmsClient.ValidState()
      && HV2CreateKMSCommon(
           kmsConfiguration := kmsConfiguration
         )
      && bkGDK in kmsClient.History.GenerateDataKey
      && beaconGDK in kmsClient.History.GenerateDataKey
  {
    var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    && beaconGDK.output.Success? && bkGDK.output.Success?
    && beaconGDK.input.EncryptionContext == bkGDK.input.EncryptionContext == Some(encryptionContext)
    && beaconGDK.input.KeyId == bkGDK.input.KeyId == kmsKeyArn
       // && beaconGDK.input.GrantTokens == bkGDK.input.GrantTokens == Some(grantTokens)
    && beaconGDK.input.NumberOfBytes == bkGDK.input.NumberOfBytes == Some(32)
    && beaconGDK.output.value.Plaintext.Some? && bkGDK.output.value.Plaintext.Some?
    && |beaconGDK.output.value.Plaintext.value| == |bkGDK.output.value.Plaintext.value| == 32
  }

  twostate function HV2AssignmentOfGeneratedMaterial(
    nameonly new bkGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly new beaconGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly kmsClient: KMS.IKMSClient
  ): BKMaterialPair
    reads kmsClient.History
    requires
      && kmsClient.ValidState()
      && HV2CreateKMSCommon(
           kmsConfiguration := kmsConfiguration
         )
      && bkGDK in kmsClient.History.GenerateDataKey
      && beaconGDK in kmsClient.History.GenerateDataKey
      && HV2GenerationOfBeaconAndBranchKeyAreCorrect(
           bkGDK := bkGDK,
           beaconGDK := beaconGDK,
           encryptionContext := encryptionContext,
           kmsConfiguration := kmsConfiguration,
           kmsClient := kmsClient
         )
  {
    BKMaterialPair(
      bk := bkGDK.output.value.Plaintext.value,
      beacon := beaconGDK.output.value.Plaintext.value
    )
  }

  twostate function HV2AssignmentOfEncryptedBranchKey(
    nameonly new decryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly new encryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly grantTokens: KMS.GrantTokenList,
    nameonly kmsClient: KMS.IKMSClient,
    nameonly material: seq<uint8>
  ): BKCiphertextPair
    reads kmsClient.History
    requires
      && kmsClient.ValidState()
      && HV2CreateKMSCommon(
           kmsConfiguration := kmsConfiguration
         )
      && decryptOnlyKMSEnc in kmsClient.History.Encrypt
      && encryptOnlyKMSEnc in kmsClient.History.Encrypt
      && HV2EncryptionOfBranchKeyAreCorrect(
           decryptOnlyKMSEnc := decryptOnlyKMSEnc,
           encryptOnlyKMSEnc := encryptOnlyKMSEnc,
           encryptionContext := encryptionContext,
           kmsConfiguration := kmsConfiguration,
           grantTokens := grantTokens,
           kmsClient := kmsClient,
           material := material
         )
  {
    BKCiphertextPair(
      decryptOnly := decryptOnlyKMSEnc.output.value.CiphertextBlob.value,
      encryptOnly := encryptOnlyKMSEnc.output.value.CiphertextBlob.value
    )
  }

  method {:isolate_assertions} CreateBranchAndBeaconKeysVersion2(
    branchKeyIdentifier: string,
    encryptionContext: map<string, string>,
    timestamp: string,
    branchKeyVersion: string,
    ddbTableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient,
    hierarchyVersion: Types.HierarchyVersion
  )

    returns (output: Result<Types.CreateKeyOutput, Types.Error>)

    requires
      // TODO-HV-2-M4 : BKS Datatype for Crypto, Storage, KMS Tuple
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && hierarchyVersion.v2?
      && 0 < |branchKeyIdentifier|
      && 0 < |branchKeyVersion|
      && forall k <- encryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)

    requires kmsClient.ValidState() && ddbClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()
    // Wrapped BK HV2
    /*
    ensures output.Success? ==>
              && |kmsClient.History.GenerateDataKey| == |old(kmsClient.History.GenerateDataKey)| + 2
                 // Generate Data Key Requests are correct
              && HV2GenerationOfBeaconAndBranchKeyAreCorrect(
                   bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                   beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                   encryptionContext := encryptionContext,
                   kmsConfiguration := kmsConfiguration,
                   kmsClient := kmsClient
                 )
              && var materialPair
                   := HV2AssignmentOfGeneratedMaterial(
                        bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                        beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                        encryptionContext := encryptionContext,
                        kmsConfiguration := kmsConfiguration,
                        kmsClient := kmsClient
                      );
              && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
                 // BK Encrypts are correct
              && HV2EncryptionOfBranchKeyAreCorrect(
                   decryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 3],
                   encryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2],
                   encryptionContext := encryptionContext,
                   kmsConfiguration := kmsConfiguration,
                   grantTokens := grantTokens,
                   kmsClient := kmsClient,
                   material := materialPair.bk
                 )
              && var bkCiphertext
                   := HV2AssignmentOfEncryptedBranchKey(
                        decryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 3],
                        encryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2],
                        encryptionContext := encryptionContext,
                        kmsConfiguration := kmsConfiguration,
                        grantTokens := grantTokens,
                        kmsClient := kmsClient,
                        material := materialPair.bk);
              // Write to Storage is correct
              && var decryptBKC
                := Structure.DecryptOnlyBranchKeyEncryptionContext(
                     branchKeyIdentifier,
                     branchKeyVersion,
                     timestamp,
                     logicalKeyStoreName,
                     KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                     hierarchyVersion,
                     encryptionContext
                   );
              && decryptBKC[Structure.TABLE_FIELD] == logicalKeyStoreName
    // && var activeBKC := Structure.ActiveBranchKeyEncryptionContext(decryptBKC);
    // && |keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey| == |old(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey)| + 1
    // && HV2CreateWriteBK(
    //      writeEvent := Seq.Last(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey),
    //      keyManagerAndStorage := keyManagerAndStorage,
    //      ciphertextPair := bkCiphertext,
    //      activeBKC := activeBKC,
    //      decryptBKC := decryptBKC
    //    )

    // Wrapped Beacon HV2
    ensures output.Success? ==>
              && |kmsClient.History.GenerateDataKey| == |old(kmsClient.History.GenerateDataKey)| + 2
                 // Generate Data Key Requests are correct
              && HV2GenerationOfBeaconAndBranchKeyAreCorrect(
                   bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                   beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                   encryptionContext := encryptionContext,
                   kmsConfiguration := kmsConfiguration,
                   kmsClient := kmsClient
                 )
              && var materialPair
                   := HV2AssignmentOfGeneratedMaterial(
                        bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                        beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                        encryptionContext := encryptionContext,
                        kmsConfiguration := kmsConfiguration,
                        kmsClient := kmsClient
                      );
              // KMS Encrypt is correct
              && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
                 // && HV2EncryptionOfBeaconIsCorrect(
                 //      beaconKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1],
                 //      encryptionContext := encryptionContext,
                 //      kmsConfiguration := kmsConfiguration,
                 //      kmsClient := kmsClient,
                 //      material := materialPair.beacon
                 //    )
                 // && var beaconCiphertext :=
                 //      HV2AssignmentOfEncryptedBeacon(
                 //        beaconKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1],
                 //        encryptionContext := encryptionContext,
                 //        kmsConfiguration := kmsConfiguration,
                 //        kmsClient := kmsClient,
                 //        material := materialPair.beacon
                 //      );
                 // Write to Storage is correct
              && var decryptBKC
                   := Structure.DecryptOnlyBranchKeyEncryptionContext(
                        branchKeyIdentifier,
                        branchKeyVersion,
                        timestamp,
                        logicalKeyStoreName,
                        KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                        hierarchyVersion,
                        encryptionContext
                      );
              && decryptBKC[Structure.TABLE_FIELD] == logicalKeyStoreName
    // && var beaconBKC := Structure.BeaconKeyEncryptionContext(decryptBKC);
    // && |keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey| == |old(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey)| + 1
    // && HV2CreateWriteBeacon(
    //      writeEvent := Seq.Last(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey),
    //      keyManagerAndStorage := keyManagerAndStorage,
    //      ciphertext := beaconCiphertext,
    //      beaconBKC := beaconBKC
    //    )
    */
  {
    // Construct Branch Key Contexts for ACTIVE, Version and Beacon items.
    var decryptOnlyBranchKeyContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      hierarchyVersion,
      encryptionContext
    );
    var activeBranchKeyContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyBranchKeyContext);
    var beaconBranchKeyContext := Structure.BeaconKeyEncryptionContext(decryptOnlyBranchKeyContext);

    // get plaintext data key by calling kms::GenerateDataKey
    var kmsBKMaterialRes :- KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
      encryptionContext := encryptionContext,
      kmsConfiguration := kmsConfiguration,
      grantTokens := grantTokens,
      kmsClient := kmsClient
    );
    var activePlaintextMaterial := kmsBKMaterialRes.Plaintext.value;

    // get beacon key by calling kms::GenerateDataKey
    var kmsBeaconMaterialRes :- KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
      encryptionContext := encryptionContext,
      kmsConfiguration := kmsConfiguration,
      grantTokens := grantTokens,
      kmsClient := kmsClient
    );
    var beaconPlaintextMaterial := kmsBeaconMaterialRes.Plaintext.value;

    // Get crypto client
    var crypto :- HvUtils.ProvideCryptoClient();
    var CryptoAndKms := KMSKeystoreOperations.CryptoAndKms(kmsConfiguration, crypto, grantTokens, kmsClient);

    var decryptOnlyBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := decryptOnlyBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );
    ghost var decryptOnlyKMSEnc := Seq.Last(kmsClient.History.Encrypt);

    var activeBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := activeBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );
    ghost var encryptOnlyKMSEnc := Seq.Last(kmsClient.History.Encrypt);
    ghost var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    assert
      HV2EncryptionOfBranchKeyAreCorrect(
        decryptOnlyKMSEnc := decryptOnlyKMSEnc,
        encryptOnlyKMSEnc := encryptOnlyKMSEnc,
        encryptionContext := encryptionContext,
        kmsConfiguration := kmsConfiguration,
        grantTokens := grantTokens,
        kmsClient := kmsClient,
        material := activePlaintextMaterial
      ) by {
      assert
        && decryptOnlyKMSEnc.output.Success? && encryptOnlyKMSEnc.output.Success?
        && decryptOnlyKMSEnc.input.EncryptionContext == encryptOnlyKMSEnc.input.EncryptionContext == Some(encryptionContext)
        && decryptOnlyKMSEnc.input.KeyId == encryptOnlyKMSEnc.input.KeyId == kmsKeyArn
        && decryptOnlyKMSEnc.input.GrantTokens == encryptOnlyKMSEnc.input.GrantTokens == Some(grantTokens)
        && |decryptOnlyKMSEnc.input.Plaintext| == |encryptOnlyKMSEnc.input.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
        && decryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == encryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == activePlaintextMaterial
        && decryptOnlyKMSEnc.output.value.CiphertextBlob.Some? && encryptOnlyKMSEnc.output.value.CiphertextBlob.Some?;
    }

    var beaconBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := beaconBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := beaconPlaintextMaterial,
      encryptionContext := encryptionContext
    );

    var decryptOnlyItem := Structure.ToAttributeMap(decryptOnlyBranchKeyContext, decryptOnlyBKItem.CiphertextBlob);
    var activeItem := Structure.ToAttributeMap(activeBranchKeyContext, activeBKItem.CiphertextBlob);
    var beaconItem := Structure.ToAttributeMap(beaconBranchKeyContext, beaconBKItem.CiphertextBlob);
    var _ :- DDBKeystoreOperations.WriteNewKeyToStore(
      decryptOnlyItem,
      activeItem,
      beaconItem,
      ddbTableName,
      ddbClient
    );

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := branchKeyIdentifier
      ));
  }

  method VersionActiveBranchKey(
    input: Types.VersionKeyInput,
    timestamp: string,
    branchKeyVersion: string,
    ddbTableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    requires ddbClient.Modifies !! kmsClient.Modifies
    requires kmsClient.ValidState() && ddbClient.ValidState()
    ensures kmsClient.ValidState() && ddbClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures
      && !KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      ==> output.Failure?

  {
    :- Need(
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration)),
      Types.KeyStoreException(
        message := ErrorMessages.DISCOVERY_VERSION_KEY_NOT_SUPPORTED
      )
    );

    :- Need(0 < |input.branchKeyIdentifier|, Types.KeyStoreException(message := ErrorMessages.BRANCH_KEY_ID_NEEDED));

    var active :- DDBKeystoreOperations.GetActiveBranchKeyItem(
      input.branchKeyIdentifier,
      ddbTableName,
      ddbClient
    );

    var hierarchyVersion := active[Structure.HIERARCHY_VERSION].N;

    match hierarchyVersion {
      case "1" =>
        output := VersionActiveBranchKeyVersion1(
          active,
          timestamp,
          branchKeyVersion,
          ddbTableName,
          logicalKeyStoreName,
          kmsConfiguration,
          grantTokens,
          kmsClient,
          ddbClient
        );
      case "2" =>
        output := VersionActiveBranchKeyVersion2(
          active,
          timestamp,
          branchKeyVersion,
          ddbTableName,
          logicalKeyStoreName,
          kmsConfiguration,
          grantTokens,
          kmsClient,
          ddbClient
        );
      case _ =>
        output := Failure(Types.KeyStoreException(
                            message :=
                              "Active Branch Key found with an unsupported hierarchy-version.\n"
                              + "Only hierarchy-version 1 or hierarchy-version 2 are supported.\n"
                              + "Found hierarchy-version " + hierarchyVersion + ".\n"
                          ));
    }
  }

  method VersionActiveBranchKeyVersion1(
    oldActiveItem: Structure.ActiveBranchKeyItem,
    timestamp: string,
    branchKeyVersion: string,
    ddbTableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    // requires 0 < |input.branchKeyIdentifier|
    requires ddbClient.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires kmsClient.ValidState() && ddbClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()

    ensures output.Success?
            ==>
              // //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              // //= type=implication
              // //# VersionKey MUST first get the active version for the branch key from the keystore
              // //# by calling AWS DDB `GetItem`
              // //# using the `branch-key-id` as the Partition Key and `"branch:ACTIVE"` value as the Sort Key.
              // && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
              // && Seq.Last(ddbClient.History.GetItem).input.Key
              //    == map[
              //         Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.branchKeyIdentifier),
              //         Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
              //       ]

              // && Seq.Last(ddbClient.History.GetItem).output.Success?
              // && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
              // && var oldActiveItem := Seq.Last(ddbClient.History.GetItem).output.value.Item.value;
              // && Structure.BranchKeyItem?(oldActiveItem)
              // && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD in oldActiveItem

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The `kms-arn` field of DDB response item MUST be [compatible with](#aws-key-arn-compatibility)
              //# the configured `KMS ARN` in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, Structure.ToBranchKeyContext(oldActiveItem, logicalKeyStoreName)[Structure.KMS_FIELD])

              && Structure.KMS_FIELD in oldActiveItem
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, oldActiveItem[Structure.KMS_FIELD].S)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The values on the AWS DDB response item
              //# MUST be authenticated according to [authenticating a keystore item](#authenticating-a-keystore-item).

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# The operation MUST use the configured `KMS SDK Client` to authenticate the value of the keystore item.
              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 2 // This 2 because we need to wrap the new version

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
              //# with a request constructed as follows:
              && var reEncryptInput := Seq.Last(Seq.DropLast(kmsClient.History.ReEncrypt)).input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `SourceEncryptionContext` MUST be the [encryption context](#encryption-context) constructed above
              && reEncryptInput.SourceEncryptionContext == Some(Structure.ToBranchKeyContext(oldActiveItem, logicalKeyStoreName))

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, reEncryptInput.SourceKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `CiphertextBlob` MUST be the `enc` attribute value on the AWS DDB response item
              && reEncryptInput.CiphertextBlob == oldActiveItem[Structure.BRANCH_KEY_FIELD].B

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `GrantTokens` MUST be the configured [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && reEncryptInput.GrantTokens == Some(grantTokens)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, reEncryptInput.DestinationKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-a-keystore-item
              //= type=implication
              //# - `DestinationEncryptionContext` MUST be the [encryption context](#encryption-context) constructed above
              && reEncryptInput.DestinationEncryptionContext == Some(Structure.ToBranchKeyContext(oldActiveItem, logicalKeyStoreName))

              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1

              && var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
                                                       Structure.ToBranchKeyContext(oldActiveItem, logicalKeyStoreName),
                                                       branchKeyVersion,
                                                       timestamp
                                                     );

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The wrapped Branch Keys, DECRYPT_ONLY and ACTIVE, MUST be created according to [Wrapped Branch Key Creation](#wrapped-branch-key-creation).
              && WrappedBranchKeyCreation?(
                   Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext),
                   Seq.Last(kmsClient.History.ReEncrypt),
                   kmsClient,
                   kmsConfiguration,
                   grantTokens,
                   decryptOnlyEncryptionContext
                 )

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The call to Amazon DynamoDB TransactWriteItems MUST use the configured Amazon DynamoDB Client to make the call.

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# To add the new branch key to the keystore,
              //# the operation MUST call [Amazon DynamoDB API TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html).
              && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The operation MUST call Amazon DynamoDB TransactWriteItems with a request constructed as follows:
              && var writeNewKey := Seq.Last(ddbClient.History.TransactWriteItems).input;

              && 2 == |writeNewKey.TransactItems|

              && writeNewKey.TransactItems[0].Put.Some?
              && writeNewKey.TransactItems[0].Put.value.Item
                 == Structure.ToAttributeMap(
                      decryptOnlyEncryptionContext,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
                      //# as the wrapped DECRYPT_ONLY Branch Key.
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value)

              && writeNewKey.TransactItems[1].Put.Some?
              && writeNewKey.TransactItems[1].Put.value.Item
                 == Structure.ToAttributeMap(
                      Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext),
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS ReEncrypt succeeds,
                      //# the operation MUST use the ReEncrypt result `CiphertextBlob`
                      //# as the wrapped ACTIVE Branch Key.
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value)

              && Seq.Last(ddbClient.History.TransactWriteItems).output.Success?

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# If DDB TransactWriteItems is successful, this operation MUST return a successful response containing no additional data.
              && output == Success(Types.VersionKeyOutput)

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# If the item fails to authenticate this operation MUST fail.
      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# Otherwise, this operation MUST yield an error.

      || (&& |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
          && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 2
          && Seq.Last(kmsClient.History.ReEncrypt).output.Failure?
          ==> output.Failure?)

      || (&& |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
          && Seq.Last(ddbClient.History.TransactWriteItems).output.Failure?
          ==> output.Failure?)

  {
    var oldActiveEncryptionContext := Structure.ToBranchKeyContext(oldActiveItem, logicalKeyStoreName);

    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveEncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );

    var _ :- KMSKeystoreOperations.ReEncryptKey(
      oldActiveItem[Structure.BRANCH_KEY_FIELD].B,
      oldActiveEncryptionContext,
      oldActiveEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      oldActiveEncryptionContext,
      branchKeyVersion,
      timestamp
    );

    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyEncryptionContext[Structure.KMS_FIELD]);

    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.GenerateKey(
      decryptOnlyEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    var wrappedActiveBranchKey :- KMSKeystoreOperations.ReEncryptKey(
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value,
      decryptOnlyEncryptionContext,
      activeEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyBranchKeyItem: Structure.VersionBranchKeyItem := Structure.ToAttributeMap(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );
    var activeBranchKeyItem: Structure.ActiveBranchKeyItem := Structure.ToAttributeMap(
      activeEncryptionContext,
      wrappedActiveBranchKey.CiphertextBlob.value
    );

    var _ :- DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      decryptOnlyBranchKeyItem,
      activeBranchKeyItem,
      ddbTableName,
      ddbClient
    );

    assert && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1;

    output := Success(Types.VersionKeyOutput());
  }

  method {:isolate_assertions} VersionActiveBranchKeyVersion2(
    oldActiveItem: Structure.ActiveBranchKeyItem,
    timestamp: string,
    branchKeyVersion: string,
    ddbTableName: DDB.TableName,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    // requires Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
    requires KmsArn.ValidKmsArn?(oldActiveItem[Structure.KMS_FIELD].S)
    requires ddbClient.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires kmsClient.ValidState() && ddbClient.ValidState()
    modifies ddbClient.Modifies, kmsClient.Modifies
    ensures ddbClient.ValidState() && kmsClient.ValidState()
    /*
    ensures output.Success?
            ==>
              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem[Structure.KMS_FIELD].S)
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, oldActiveItem[Structure.KMS_FIELD].S)

              && |kmsClient.History.GenerateDataKey| == |old(kmsClient.History.GenerateDataKey)| + 1 // for the new active
              && |kmsClient.History.Decrypt| == |old(kmsClient.History.Decrypt)| + 1 // for decrypting the current active
              && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 2 // for encrypting the new active and encrypting the old active into the version

              && old(kmsClient.History.GenerateDataKey) < kmsClient.History.GenerateDataKey
              && old(kmsClient.History.Decrypt) < kmsClient.History.Decrypt
              && old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt

              && var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
              && HvUtils.IsValidHV2EC?(oldActiveItem.EncryptionContext)
              && var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(oldActiveItem.EncryptionContext);
              && var gdkEvent := Seq.Last(kmsClient.History.GenerateDataKey);
              && var gdkInput := gdkEvent.input;
              && var gdkOutput := gdkEvent.output;
              && KMS.GenerateDataKeyRequest(
                   KeyId := kmsKeyArn,
                   NumberOfBytes := Some(32),
                   EncryptionContext := Some(ecToKMS),
                   GrantTokens := Some(grantTokens)
                 ) == gdkInput
              && gdkOutput.Success?
              && gdkOutput.value.Plaintext.Some?
              && var newActiveMaterial := gdkOutput.value.Plaintext.value;

              && KMS.IsValid_CiphertextType(oldActiveItem.CiphertextBlob)
              && var kmsArnFromStorage := oldActiveItem.KmsArn;
              && var decryptOutput := Seq.Last(kmsClient.History.Decrypt).output;
              && KMSKeystoreOperations.AwsKmsBranchKeyDecryptionForHV2?(
                   oldActiveItem.CiphertextBlob,
                   ecToKMS,
                   kmsArnFromStorage,
                   kmsConfiguration,
                   grantTokens,
                   kmsClient,
                   Seq.Last(kmsClient.History.Decrypt)
                 )
              && decryptOutput.Success?
              && var oldActiveMaterial := decryptOutput.value.Plaintext.value[Structure.BKC_DIGEST_LENGTH..];

              && WrappedBranchKeyVersionV2?(
                   kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1],
                   kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2],
                   newActiveMaterial,
                   oldActiveMaterial,
                   kmsClient,
                   kmsConfiguration,
                   grantTokens,
                   ecToKMS
                 )

              && var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
                                                       oldActiveItem.EncryptionContext,
                                                       branchKeyVersion,
                                                       timestamp
                                                     );
              && var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);
              && |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item
                 == Structure.ConstructEncryptedHierarchicalKey(
                      activeEncryptionContext,
                      kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1].output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version
                 == Structure.ConstructEncryptedHierarchicalKey(
                      decryptOnlyEncryptionContext,
                      kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2].output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item.KmsArn == oldActiveItem.KmsArn
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version.KmsArn == oldActiveItem.KmsArn

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Success?

              && output == Success(Types.VersionKeyOutput)
              */
  {
    var activeItem := Structure.ToEncryptedHierarchicalKey(oldActiveItem, logicalKeyStoreName);

    :- Need(
      HvUtils.IsValidHV2EC?(activeItem.EncryptionContext),
      Types.BranchKeyCiphertextException(
        message := ErrorMessages.INVALID_EC_FOUND
      )
    );
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem[Structure.KMS_FIELD].S)
      && KMSKeystoreOperations.GetKeyId(kmsConfiguration) == oldActiveItem[Structure.KMS_FIELD].S,
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );

    var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(activeItem.EncryptionContext);

    // var keyManagerStrategy := KmsUtils.keyManagerStrat.kmsSimple(
    //   kmsSimple := KmsUtils.KMSTuple(kmsClient := kmsClient, grantTokens := grantTokens)
    // );
    // var keyManagerAndStorage := KmsUtils.KeyManagerAndStorage(
    //   storage := storage,
    //   keyManagerStrat := keyManagerStrategy
    // );

    var newActivePlaintextMaterial :- KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
      encryptionContext := ecToKMS,
      kmsConfiguration := kmsConfiguration,
      grantTokens := grantTokens,
      kmsClient := kmsClient
    );

    // Get crypto client
    var crypto :- HvUtils.ProvideCryptoClient();

    // we decrypt the oldActiveItem to get the ciphertext and then
    // we encrypt it to a versioned key
    var oldActiveItemPlaintext :- GetKeys.DecryptAndValidateKeyForHV2(
      activeItem.EncryptionContext, // encryptionContext
      oldActiveItem[Structure.BRANCH_KEY_FIELD].B,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      activeItem.EncryptionContext,
      branchKeyVersion,
      timestamp
    );
    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);


    var CryptoAndKms := KMSKeystoreOperations.CryptoAndKms(kmsConfiguration, crypto, grantTokens, kmsClient);
    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := decryptOnlyEncryptionContext,
      cryptoAndKms := CryptoAndKms,
      material := oldActiveItemPlaintext,
      encryptionContext := ecToKMS
    );

    var wrappedActiveBranchKey :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := activeEncryptionContext,
      cryptoAndKms := CryptoAndKms,
      material := newActivePlaintextMaterial.Plaintext.value,
      encryptionContext := ecToKMS
    );

    var decryptOnlyItemMap := Structure.ToAttributeMap(decryptOnlyEncryptionContext, wrappedDecryptOnlyBranchKey.CiphertextBlob);
    var activeItemMap := Structure.ToAttributeMap(activeEncryptionContext, wrappedActiveBranchKey.CiphertextBlob);

    var _ :- DDBKeystoreOperations.WriteNewBranchKeyVersionToKeystore(
      decryptOnlyItemMap,
      activeItemMap,
      ddbTableName,
      ddbClient
    );

    output := Success(Types.VersionKeyOutput());
  }

  ghost predicate WrappedBranchKeyCreation?(
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
    generateHistory: KMS.DafnyCallEvent<KMS.GenerateDataKeyWithoutPlaintextRequest, Result<KMS.GenerateDataKeyWithoutPlaintextResponse, KMS.Error>>,
    reEncryptHistory: KMS.DafnyCallEvent<KMS.ReEncryptRequest, Result<KMS.ReEncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    decryptOnlyEncryptionContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires Structure.BranchKeyContext?(decryptOnlyEncryptionContext)
    requires Structure.BRANCH_KEY_TYPE_PREFIX < decryptOnlyEncryptionContext[Structure.TYPE_FIELD]

    // Ideally this be in "the things I added"
    // But I don't know how to express that yet.

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
    requires generateHistory in kmsClient.History.GenerateDataKeyWithoutPlaintext
    requires reEncryptHistory in kmsClient.History.ReEncrypt
  {

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
    && var decryptOnlyKmsInput := generateHistory.input;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `KeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, decryptOnlyKmsInput.KeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `NumberOfBytes` MUST be 32.
    && decryptOnlyKmsInput.NumberOfBytes == Some(32)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `EncryptionContext` MUST be the [DECRYPT_ONLY encryption context for branch keys](#decrypt_only-encryption-context).
    && decryptOnlyKmsInput.EncryptionContext == Some(decryptOnlyEncryptionContext)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - GenerateDataKeyWithoutPlaintext `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && decryptOnlyKmsInput.GrantTokens == Some(grantTokens)

    && generateHistory.output.Success?
    && generateHistory.output.value.CiphertextBlob.Some?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
    //# with a request constructed as follows:
    && var activeInput := reEncryptHistory.input;

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, activeInput.SourceKeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, activeInput.DestinationKeyId)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - ReEncrypt `GrantTokens` MUST be this keystore's [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    && activeInput.GrantTokens == Some(grantTokens)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `CiphertextBlob` MUST be the wrapped DECRYPT_ONLY Branch Key.
    && activeInput.CiphertextBlob == generateHistory.output.value.CiphertextBlob.value

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `SourceEncryptionContext` MUST be the [DECRYPT_ONLY encryption context for branch keys](#decrypt_only-encryption-context).
    && activeInput.SourceEncryptionContext == Some(decryptOnlyEncryptionContext)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `DestinationEncryptionContext` MUST be the [ACTIVE encryption context for branch keys](#active-encryption-context).
    && activeInput.DestinationEncryptionContext == Some(Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext))

    && reEncryptHistory.output.Success?
    && reEncryptHistory.output.value.CiphertextBlob.Some?

  }

}
