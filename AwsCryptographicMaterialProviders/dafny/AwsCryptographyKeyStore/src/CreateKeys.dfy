// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "DefaultKeyStorageInterface.dfy"
include "KMSKeystoreOperations.dfy"
include "KeyStoreErrorMessages.dfy"
include "GetKeys.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "KmsArn.dfy"
include "HierarchicalVersionUtils.dfy"
include "KmsUtils.dfy"

module {:options "/functionSyntax:4" } CreateKeys {
  import opened StandardLibrary
  import opened Wrappers
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import AtomicPrimitives
  import GetKeys
  import HvUtils = HierarchicalVersionUtils
  import AwsArnParsing
  import KmsArn
  import KmsUtils
  import Time
  import UUID

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=implication
  //# To create a branch key, this operation MUST take the following:
  //#
  //# - `branchKeyId`: The identifier
  //# - `encryptionContext`: Additional encryption context to bind to the created keys
  method CreateBranchAndBeaconKeys(
    branchKeyIdentifier: string,
    customEncryptionContext: map<string, string>,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires 0 < |branchKeyIdentifier|
    requires 0 < |branchKeyVersion|
    requires forall k <- customEncryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# This operation MUST create a [branch key](structures.md#branch-key) and a [beacon key](structures.md#beacon-key) according to
    //# the [Branch Key and Beacon Key Creation](#branch-key-and-beacon-key-creation) section.
    ensures output.Success?
            ==>

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
              // The second call is for the beacon key, the first call is the decrypt only. See Seq.Last(Seq.DropLast(
              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
              && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
              && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

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

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
              //= type=implication
              //# Any additionally attributes in the EncryptionContext
              //# of the [encrypted hierarchical key](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be added to the encryption context.
              && (forall k <- customEncryptionContext
                    ::
                      && Structure.ENCRYPTION_CONTEXT_PREFIX + k in decryptOnlyEncryptionContext
                      && decryptOnlyEncryptionContext[Structure.ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k])

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
              //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
              && var beaconKmsRequest := Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext);

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
              //= type=implication
              //# The operation MUST call AWS KMS GenerateDataKeyWithoutPlaintext with a request constructed as follows:
              && var beaconKmsInput := beaconKmsRequest.input;

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

              && beaconKmsRequest.output.Success?
              && beaconKmsRequest.output.value.CiphertextBlob.Some?

              && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Active
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS ReEncrypt succeeds,
                      //# the operation MUST use the ReEncrypt result `CiphertextBlob`
                      //# as the wrapped ACTIVE Branch Key.
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Version
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).input.EncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the GenerateDataKeyWithoutPlaintext result `CiphertextBlob`
                      //# as the wrapped DECRYPT_ONLY Branch Key.
                      Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Beacon
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
                      //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
                      //= type=implication
                      //# If the call to AWS KMS GenerateDataKeyWithoutPlaintext succeeds,
                      //# the operation MUST use the `CiphertextBlob` as the wrapped Beacon Key.
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If creation of the keys are successful,
    //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [WriteNewEncryptedBranchKey](./key-store/key-storage.md#writenewencryptedbranchkey) with these 3 [EncryptedHierarchicalKeys](./key-store/key-storage.md#encryptedhierarchicalkey).
    ensures
      && output.Success?
      && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 2
      && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 1
      && Seq.Last(Seq.DropLast(kmsClient.History.GenerateDataKeyWithoutPlaintext)).output.Success?
      && Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.Success?
      && Seq.Last(kmsClient.History.ReEncrypt).output.Success?
      ==>
        && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# If writing to the keystore succeeds,
    //# the operation MUST return the branch-key-id that maps to both
    //# the branch key and the beacon key.
    ensures
      && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
      && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?
      ==>
        && output.Success?
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

      || (&& |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Failure?
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

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyEncryptionContext[Structure.KMS_FIELD]);
    var wrappedDecryptOnlyBranchKey :- KMSKeystoreOperations.GenerateKey(
      decryptOnlyEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeEncryptionContext[Structure.KMS_FIELD]);
    var wrappedActiveBranchKey :- KMSKeystoreOperations.ReEncryptKey(
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value,
      decryptOnlyEncryptionContext,
      activeEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconEncryptionContext[Structure.KMS_FIELD]);
    var wrappedBeaconKey :- KMSKeystoreOperations.GenerateKey(
      beaconEncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var _ :- storage.WriteNewEncryptedBranchKey(
      Types.WriteNewEncryptedBranchKeyInput(
        Active := Structure.ConstructEncryptedHierarchicalKey(
          activeEncryptionContext,
          wrappedActiveBranchKey.CiphertextBlob.value
        ),
        Version := Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyEncryptionContext,
          wrappedDecryptOnlyBranchKey.CiphertextBlob.value
        ),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(
          beaconEncryptionContext,
          wrappedBeaconKey.CiphertextBlob.value
        )
      )
    );

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := branchKeyIdentifier
      ));
  }

  type material = m: seq<uint8> | |m| == 32 witness *
  datatype BKMaterialPair = | BKMaterialPair(
    nameonly bk: material,
    nameonly beacon: material
  )

  twostate predicate GenerateBranchAndBeaconMaterial2KMS(
    nameonly new bkGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly new beaconGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage
  )
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && bkGDK in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.GenerateDataKey
      && beaconGDK in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.GenerateDataKey
  {
    var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    && beaconGDK.output.Success? && bkGDK.output.Success?
    && beaconGDK.input.EncryptionContext == bkGDK.input.EncryptionContext == Some(encryptionContext)
    && beaconGDK.input.KeyId == bkGDK.input.KeyId == kmsKeyArn
    && beaconGDK.input.GrantTokens == bkGDK.input.GrantTokens == Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
    && beaconGDK.input.NumberOfBytes == bkGDK.input.NumberOfBytes == Some(32)
    && beaconGDK.output.value.Plaintext.Some? && bkGDK.output.value.Plaintext.Some?
    && |beaconGDK.output.value.Plaintext.value| == |bkGDK.output.value.Plaintext.value| == 32
  }

  twostate function GenerateBranchAndBeaconMaterial2(
    nameonly new bkGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly new beaconGDK: KMS.DafnyCallEvent<KMS.GenerateDataKeyRequest, Result<KMS.GenerateDataKeyResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage
  ): BKMaterialPair
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && bkGDK in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.GenerateDataKey
      && beaconGDK in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.GenerateDataKey
      && GenerateBranchAndBeaconMaterial2KMS(
           bkGDK := bkGDK,
           beaconGDK := beaconGDK,
           encryptionContext := encryptionContext,
           kmsConfiguration := kmsConfiguration,
           keyManagerAndStorage := keyManagerAndStorage
         )
  {
    BKMaterialPair(
      bk := bkGDK.output.value.Plaintext.value,
      beacon := beaconGDK.output.value.Plaintext.value
    )
  }

  twostate predicate HV2EncryptBKKMS(
    nameonly new decryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly new encryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly material: seq<uint8>
  )
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && decryptOnlyKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
      && encryptOnlyKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
  {
    && var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    && decryptOnlyKMSEnc.output.Success? && encryptOnlyKMSEnc.output.Success?
    && decryptOnlyKMSEnc.input.EncryptionContext == encryptOnlyKMSEnc.input.EncryptionContext == Some(encryptionContext)
    && decryptOnlyKMSEnc.input.KeyId == encryptOnlyKMSEnc.input.KeyId == kmsKeyArn
    && decryptOnlyKMSEnc.input.GrantTokens == encryptOnlyKMSEnc.input.GrantTokens == Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
    && |decryptOnlyKMSEnc.input.Plaintext| == |encryptOnlyKMSEnc.input.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && decryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == encryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == material
    && decryptOnlyKMSEnc.output.value.CiphertextBlob.Some? && encryptOnlyKMSEnc.output.value.CiphertextBlob.Some?
  }

  datatype BKCiphertextPair = | BKCiphertextPair(
    nameonly decryptOnly: seq<uint8>,
    nameonly encryptOnly: seq<uint8>
  )

  twostate function HV2EncryptBK(
    nameonly new decryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly new encryptOnlyKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly material: seq<uint8>
  ): BKCiphertextPair
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && decryptOnlyKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
      && encryptOnlyKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
      && HV2EncryptBKKMS(
           decryptOnlyKMSEnc := decryptOnlyKMSEnc,
           encryptOnlyKMSEnc := encryptOnlyKMSEnc,
           encryptionContext := encryptionContext,
           kmsConfiguration := kmsConfiguration,
           keyManagerAndStorage := keyManagerAndStorage,
           material := material
         )
  {
    BKCiphertextPair(
      decryptOnly := decryptOnlyKMSEnc.output.value.CiphertextBlob.value,
      encryptOnly := encryptOnlyKMSEnc.output.value.CiphertextBlob.value
    )
  }

  twostate predicate HV2CreateWriteBK(
    nameonly new writeEvent: Types.DafnyCallEvent<Types.WriteNewEncryptedBranchKeyInput, Result<Types.WriteNewEncryptedBranchKeyOutput, Types.Error>>,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly ciphertextPair: BKCiphertextPair,
    nameonly activeBKC: map<string, string>,
    nameonly decryptBKC: map<string, string>
  )
    reads keyManagerAndStorage.storage.History
    requires
      && writeEvent in keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey
      && Structure.BranchKeyContext?(activeBKC)
      && Structure.BranchKeyContext?(decryptBKC)
  {
    && writeEvent.input.Active
       == Structure.ConstructEncryptedHierarchicalKey(
            activeBKC,
            ciphertextPair.encryptOnly
          )
    && writeEvent.input.Version
       == Structure.ConstructEncryptedHierarchicalKey(
            decryptBKC,
            ciphertextPair.decryptOnly
          )
    && writeEvent.output.Success?
  }

  twostate predicate HV2EncryptBeaconKMS(
    nameonly new beaconKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly material: seq<uint8>
  )
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && beaconKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
  {
    && var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    && beaconKMSEnc.output.Success?
    && beaconKMSEnc.input.EncryptionContext == Some(encryptionContext)
    && beaconKMSEnc.input.KeyId == kmsKeyArn
    && beaconKMSEnc.input.GrantTokens == Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
    && |beaconKMSEnc.input.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && beaconKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == material
    && beaconKMSEnc.output.value.CiphertextBlob.Some?
  }

  twostate function HV2EncryptBeacon(
    nameonly new beaconKMSEnc: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    nameonly encryptionContext: map<string, string>,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly material: seq<uint8>
  ): seq<uint8>
    reads keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History
    requires
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && beaconKMSEnc in keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt
      && HV2EncryptBeaconKMS(
           beaconKMSEnc := beaconKMSEnc,
           encryptionContext := encryptionContext,
           kmsConfiguration := kmsConfiguration,
           keyManagerAndStorage := keyManagerAndStorage,
           material := material
         )
  {
    beaconKMSEnc.output.value.CiphertextBlob.value
  }

  twostate predicate HV2CreateWriteBeacon(
    nameonly new writeEvent: Types.DafnyCallEvent<Types.WriteNewEncryptedBranchKeyInput, Result<Types.WriteNewEncryptedBranchKeyOutput, Types.Error>>,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly ciphertext: seq<uint8>,
    nameonly beaconBKC: map<string, string>
  )
    reads keyManagerAndStorage.storage.History
    requires
      && writeEvent in keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey
      && Structure.BranchKeyContext?(beaconBKC)
  {
    && writeEvent.input.Beacon
       == Structure.ConstructEncryptedHierarchicalKey(
            beaconBKC,
            ciphertext
          )
    && writeEvent.output.Success?
  }

  method {:isolate_assertions} CreateBranchAndBeaconKeysVersion2(
    nameonly branchKeyIdentifier: string,
    nameonly encryptionContext: map<string, string>,
    nameonly timestamp: string,
    nameonly branchKeyVersion: string,
    nameonly logicalKeyStoreName: string,
    nameonly kmsConfiguration: Types.KMSConfiguration,
    nameonly keyManagerAndStorage: KmsUtils.KeyManagerAndStorage,
    nameonly hierarchyVersion: Types.HierarchyVersion
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)

    requires
      // TODO-HV-2-M4 : BKS Datatype for Crypto, Storage, KMS Tuple
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && hierarchyVersion.v2?
      && 0 < |branchKeyIdentifier|
      && 0 < |branchKeyVersion|
      && forall k <- encryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)

    requires keyManagerAndStorage.ValidState()
    modifies keyManagerAndStorage.Modifies
    ensures keyManagerAndStorage.ValidState()

    // Wrapped BK HV2
    ensures
      output.Success?
      ==>
        && var kmsClient := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient;
        && |kmsClient.History.GenerateDataKey| == |old(kmsClient.History.GenerateDataKey)| + 2
           // Generate Data Key Requests are correct
        && GenerateBranchAndBeaconMaterial2KMS(
             bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
             beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
             encryptionContext := encryptionContext,
             kmsConfiguration := kmsConfiguration,
             keyManagerAndStorage := keyManagerAndStorage
           )
        && var materialPair
             := GenerateBranchAndBeaconMaterial2(
                  bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                  beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                  encryptionContext := encryptionContext,
                  kmsConfiguration := kmsConfiguration,
                  keyManagerAndStorage := keyManagerAndStorage
                );
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
           // BK Encrypts are correct
        && HV2EncryptBKKMS(
             decryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 3],
             encryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2],
             encryptionContext := encryptionContext,
             kmsConfiguration := kmsConfiguration,
             keyManagerAndStorage := keyManagerAndStorage,
             material := materialPair.bk
           )
        && var bkCiphertext
             := HV2EncryptBK(
                  decryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 3],
                  encryptOnlyKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 2],
                  encryptionContext := encryptionContext,
                  kmsConfiguration := kmsConfiguration,
                  keyManagerAndStorage := keyManagerAndStorage,
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
        && var activeBKC := Structure.ActiveBranchKeyEncryptionContext(decryptBKC);
        && |keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey| == |old(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey)| + 1
        && HV2CreateWriteBK(
             writeEvent := Seq.Last(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey),
             keyManagerAndStorage := keyManagerAndStorage,
             ciphertextPair := bkCiphertext,
             activeBKC := activeBKC,
             decryptBKC := decryptBKC
           )

    // Wrapped Beacon HV2
    ensures
      output.Success?
      ==>
        && var kmsClient := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient;
        && |kmsClient.History.GenerateDataKey| == |old(kmsClient.History.GenerateDataKey)| + 2
           // Generate Data Key Requests are correct
        && GenerateBranchAndBeaconMaterial2KMS(
             bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
             beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
             encryptionContext := encryptionContext,
             kmsConfiguration := kmsConfiguration,
             keyManagerAndStorage := keyManagerAndStorage
           )
        && var materialPair
             := GenerateBranchAndBeaconMaterial2(
                  bkGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| -2],
                  beaconGDK := kmsClient.History.GenerateDataKey[|kmsClient.History.GenerateDataKey| - 1],
                  encryptionContext := encryptionContext,
                  kmsConfiguration := kmsConfiguration,
                  keyManagerAndStorage := keyManagerAndStorage
                );
        // KMS Encrypt is correct
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
        && HV2EncryptBeaconKMS(
             beaconKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1],
             encryptionContext := encryptionContext,
             kmsConfiguration := kmsConfiguration,
             keyManagerAndStorage := keyManagerAndStorage,
             material := materialPair.beacon
           )
        && var beaconCiphertext :=
             HV2EncryptBeacon(
               beaconKMSEnc := kmsClient.History.Encrypt[|kmsClient.History.Encrypt| - 1],
               encryptionContext := encryptionContext,
               kmsConfiguration := kmsConfiguration,
               keyManagerAndStorage := keyManagerAndStorage,
               material := materialPair.beacon
             );
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
        && var beaconBKC := Structure.BeaconKeyEncryptionContext(decryptBKC);
        && |keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey| == |old(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey)| + 1
        && HV2CreateWriteBeacon(
             writeEvent := Seq.Last(keyManagerAndStorage.storage.History.WriteNewEncryptedBranchKey),
             keyManagerAndStorage := keyManagerAndStorage,
             ciphertext := beaconCiphertext,
             beaconBKC := beaconBKC
           )
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
      grantTokens := keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens,
      kmsClient := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient
    );
    var activePlaintextMaterial := kmsBKMaterialRes.Plaintext.value;

    // get beacon key by calling kms::GenerateDataKey
    var kmsBeaconMaterialRes :- KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
      encryptionContext := encryptionContext,
      kmsConfiguration := kmsConfiguration,
      grantTokens := keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens,
      kmsClient := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient
    );
    var beaconPlaintextMaterial := kmsBeaconMaterialRes.Plaintext.value;

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    var crypto :- crypto?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e
        )
    );

    var CryptoAndKms := KMSKeystoreOperations.CryptoAndKms(kmsConfiguration, keyManagerAndStorage.keyManagerStrat, crypto);
    ghost var kms := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient;

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyBranchKeyContext[Structure.KMS_FIELD]);
    var decryptOnlyBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := decryptOnlyBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );
    ghost var decryptOnlyKMSEnc := Seq.Last(keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeBranchKeyContext[Structure.KMS_FIELD]);
    var activeBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := activeBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );
    ghost var encryptOnlyKMSEnc := Seq.Last(keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient.History.Encrypt);
    ghost var kmsKeyArn := KMSKeystoreOperations.GetKeyId(kmsConfiguration);
    assert
      HV2EncryptBKKMS(
        decryptOnlyKMSEnc := decryptOnlyKMSEnc,
        encryptOnlyKMSEnc := encryptOnlyKMSEnc,
        encryptionContext := encryptionContext,
        kmsConfiguration := kmsConfiguration,
        keyManagerAndStorage := keyManagerAndStorage,
        material := activePlaintextMaterial
      ) by {
      assert
        && decryptOnlyKMSEnc.output.Success? && encryptOnlyKMSEnc.output.Success?
        && decryptOnlyKMSEnc.input.EncryptionContext == encryptOnlyKMSEnc.input.EncryptionContext == Some(encryptionContext)
        && decryptOnlyKMSEnc.input.KeyId == encryptOnlyKMSEnc.input.KeyId == kmsKeyArn
        && decryptOnlyKMSEnc.input.GrantTokens == encryptOnlyKMSEnc.input.GrantTokens == Some(keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens)
        && |decryptOnlyKMSEnc.input.Plaintext| == |encryptOnlyKMSEnc.input.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
        && decryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == encryptOnlyKMSEnc.input.Plaintext[Structure.BKC_DIGEST_LENGTH..] == activePlaintextMaterial
        && decryptOnlyKMSEnc.output.value.CiphertextBlob.Some? && encryptOnlyKMSEnc.output.value.CiphertextBlob.Some?;
    }

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconBranchKeyContext[Structure.KMS_FIELD]);
    var beaconBKItem :- KMSKeystoreOperations.packAndCallKMS(
      branchKeyContext := beaconBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := beaconPlaintextMaterial,
      encryptionContext := encryptionContext
    );

    // Write ACTIVE, Version & Beacon Items to storage
    var _ :- keyManagerAndStorage.storage.WriteNewEncryptedBranchKey(
      Types.WriteNewEncryptedBranchKeyInput(
        Active := activeBKItem,
        Version := decryptOnlyBKItem,
        Beacon := beaconBKItem
      )
    );

    output := Success(
      Types.CreateKeyOutput(
        branchKeyIdentifier := branchKeyIdentifier
      ));
  }

  method VersionActiveBranchKey(
    input: Types.VersionKeyInput,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    keyManagerAndStorage: KmsUtils.KeyManagerAndStorage
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires keyManagerAndStorage.ValidState()
    requires keyManagerAndStorage.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (keyManagerAndStorage.storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    modifies keyManagerAndStorage.Modifies
    ensures keyManagerAndStorage.ValidState()
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

    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreException(message := e));

    var maybeBranchKeyVersion := UUID.GenerateUUID();
    var branchKeyVersion :- maybeBranchKeyVersion
    .MapFailure(e => Types.KeyStoreException(message := e));

    var oldActiveItem :- fetchActiveItem(input.branchKeyIdentifier, keyManagerAndStorage.storage, logicalKeyStoreName);
    var hierarchyVersion := oldActiveItem.EncryptionContext[Structure.HIERARCHY_VERSION];

    match hierarchyVersion {
      case "1" =>
        :- Need(
          keyManagerAndStorage.keyManagerStrat.reEncrypt? || keyManagerAndStorage.keyManagerStrat.kmsSimple?,
          Types.KeyStoreException(message := ErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_VERSION)
        );
        var kmsTuple := KmsUtils.getEncryptKMSTuple(keyManagerAndStorage.keyManagerStrat);
        output := VersionActiveBranchKeyVersion1(
          oldActiveItem,
          timestamp,
          branchKeyVersion,
          logicalKeyStoreName,
          kmsConfiguration,
          kmsTuple.grantTokens,
          kmsTuple.kmsClient,
          keyManagerAndStorage.storage
        );
      case "2" =>
        :- Need(
          keyManagerAndStorage.keyManagerStrat.kmsSimple?,
          Types.KeyStoreException(message := ErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_VERSION_HV_2)
        );
        var kmsTuple := KmsUtils.getEncryptKMSTuple(keyManagerAndStorage.keyManagerStrat);
        output := VersionActiveBranchKeyVersion2(
          oldActiveItem,
          timestamp,
          branchKeyVersion,
          logicalKeyStoreName,
          kmsConfiguration,
          kmsTuple.grantTokens,
          kmsTuple.kmsClient,
          keyManagerAndStorage.storage
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
    oldActiveItem: Types.EncryptedHierarchicalKey,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    requires Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    ensures |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)|

    ensures output.Success?
            ==>
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The `KmsArn` of the [EncryptedHierarchicalKey](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be [compatible with](#aws-key-arn-compatibility)
              //# the configured `KMS ARN` in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD])
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, oldActiveItem.KmsArn)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The [EncryptedHierarchicalKey](./key-store/key-storage.md#encryptedhierarchicalkey)
              //# MUST be authenticated according to [authenticating a keystore item](#authenticating-an-encryptedhierarchicalkey).

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# The operation MUST use the configured `KMS SDK Client` to authenticate the value of the keystore item.
              && |kmsClient.History.ReEncrypt| == |old(kmsClient.History.ReEncrypt)| + 2 // This 2 because we need to wrap the new version

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# The operation MUST call [AWS KMS API ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html)
              //# with a request constructed as follows:
              && var reEncryptInput := Seq.Last(Seq.DropLast(kmsClient.History.ReEncrypt)).input;

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `SourceEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.SourceEncryptionContext == Some(oldActiveItem.EncryptionContext)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `SourceKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.OptCompatible?(kmsConfiguration, reEncryptInput.SourceKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `CiphertextBlob` MUST be the `CiphertextBlob` attribute value on the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.CiphertextBlob == oldActiveItem.CiphertextBlob

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `GrantTokens` MUST be the configured [grant tokens](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
              && reEncryptInput.GrantTokens == Some(grantTokens)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `DestinationKeyId` MUST be [compatible with](#aws-key-arn-compatibility) the configured KMS Key in the [AWS KMS Configuration](#aws-kms-configuration) for this keystore.
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, reEncryptInput.DestinationKeyId)

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#authenticating-an-encryptedhierarchicalkey
              //= type=implication
              //# - `DestinationEncryptionContext` MUST be the [encryption context](#encryption-context) of the EncryptedHierarchicalKey to be authenticated
              && reEncryptInput.DestinationEncryptionContext == Some(oldActiveItem.EncryptionContext)

              && |kmsClient.History.GenerateDataKeyWithoutPlaintext| == |old(kmsClient.History.GenerateDataKeyWithoutPlaintext)| + 1
              && old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
              && old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

              && var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
                                                       oldActiveItem.EncryptionContext,
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

              && |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# If creation of the keys are successful,
              //# then the key store MUST call the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
              //# [WriteNewEncryptedBranchKeyVersion](./key-store/key-storage.md##writenewencryptedbranchkeyversion)
              //# with these 2 [EncryptedHierarchicalKeys](./key-store/key-storage.md##encryptedhierarchicalkey).
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.ReEncrypt).input.DestinationEncryptionContext.value,
                      Seq.Last(kmsClient.History.ReEncrypt).output.value.CiphertextBlob.value
                    )

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version
                 == Structure.ConstructEncryptedHierarchicalKey(
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).input.EncryptionContext.value,
                      Seq.Last(kmsClient.History.GenerateDataKeyWithoutPlaintext).output.value.CiphertextBlob.value
                    )

              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# The `kms-arn` stored in the table MUST NOT change as a result of this operation,
              //# even if the KeyStore is configured with a `KMS MRKey ARN` that does not exactly match the stored ARN.
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Active.Item.KmsArn == oldActiveItem.KmsArn
              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).input.Version.KmsArn == oldActiveItem.KmsArn

              && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Success?


              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# If the [WriteNewEncryptedBranchKeyVersion](./key-store/key-storage.md#writenewencryptedbranchkeyversion) is successful,
              //# this operation MUST return a successful response containing no additional data.
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

      || (&& |storage.History.WriteNewEncryptedBranchKeyVersion| == |old(storage.History.WriteNewEncryptedBranchKeyVersion)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKeyVersion).output.Failure?
          ==> output.Failure?)

  {
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD]),
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );

    var _ :- KMSKeystoreOperations.ReEncryptKey(
      oldActiveItem.CiphertextBlob,
      oldActiveItem.EncryptionContext,
      oldActiveItem.EncryptionContext,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      oldActiveItem.EncryptionContext,
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

    var active := Structure.ConstructEncryptedHierarchicalKey(
      activeEncryptionContext,
      wrappedActiveBranchKey.CiphertextBlob.value
    );
    var overWrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := active,
      Old := oldActiveItem
    );

    var _ :- storage.WriteNewEncryptedBranchKeyVersion(
      Types.WriteNewEncryptedBranchKeyVersionInput(
        Active := overWrite,
        Version :=  Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyEncryptionContext,
          wrappedDecryptOnlyBranchKey.CiphertextBlob.value
        )
      )
    );

    output := Success(Types.VersionKeyOutput());
  }

  method {:isolate_assertions} VersionActiveBranchKeyVersion2(
    oldActiveItem: Types.EncryptedHierarchicalKey,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: Types.IKeyStorageInterface
  )
    returns (output: Result<Types.VersionKeyOutput, Types.Error>)
    requires 0 < |branchKeyVersion|
    requires Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
    requires KmsArn.ValidKmsArn?(oldActiveItem.KmsArn)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()
    ensures output.Success?
            ==>
              && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD])
              && KMSKeystoreOperations.Compatible?(kmsConfiguration, oldActiveItem.KmsArn)

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
  {
    :- Need(
      HvUtils.IsValidHV2EC?(oldActiveItem.EncryptionContext),
      Types.BranchKeyCiphertextException(
        message := ErrorMessages.INVALID_EC_FOUND
      )
    );
    :- Need(
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, oldActiveItem.EncryptionContext[Structure.KMS_FIELD])
      && KMSKeystoreOperations.GetKeyId(kmsConfiguration) == oldActiveItem.EncryptionContext[Structure.KMS_FIELD],
      Types.KeyStoreException(
        message := ErrorMessages.VERSION_KEY_KMS_KEY_ARN_DISAGREEMENT)
    );

    var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(oldActiveItem.EncryptionContext);

    var keyManagerStrategy := KmsUtils.keyManagerStrat.kmsSimple(
      kmsSimple := KmsUtils.KMSTuple(kmsClient := kmsClient, grantTokens := grantTokens)
    );
    var keyManagerAndStorage := KmsUtils.KeyManagerAndStorage(
      storage := storage,
      keyManagerStrat := keyManagerStrategy
    );

    var newActivePlaintextMaterial :- KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
      encryptionContext := ecToKMS,
      kmsConfiguration := kmsConfiguration,
      grantTokens := keyManagerAndStorage.keyManagerStrat.kmsSimple.grantTokens,
      kmsClient := keyManagerAndStorage.keyManagerStrat.kmsSimple.kmsClient
    );

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    var crypto :- crypto?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e
        )
    );

    // we decrypt the oldActiveItem to get the ciphertext and then
    // we encrypt it to a versioned key
    var oldActiveItemPlaintext :- GetKeys.DecryptAndValidateKeyForHV2(
      oldActiveItem,
      kmsConfiguration,
      grantTokens,
      kmsClient
    );

    var decryptOnlyEncryptionContext := Structure.NewVersionFromActiveBranchKeyEncryptionContext(
      oldActiveItem.EncryptionContext,
      branchKeyVersion,
      timestamp
    );
    var activeEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext);


    var CryptoAndKms := KMSKeystoreOperations.CryptoAndKms(kmsConfiguration, keyManagerStrategy, crypto);
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

    var overWrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := wrappedActiveBranchKey,
      Old := oldActiveItem
    );


    var _ :- storage.WriteNewEncryptedBranchKeyVersion(
      Types.WriteNewEncryptedBranchKeyVersionInput(
        Active := overWrite,
        Version := wrappedDecryptOnlyBranchKey
      )
    );

    output := Success(Types.VersionKeyOutput());
  }

  twostate predicate WrappedBranchKeyCreation?(
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The operation MUST call [AWS KMS API GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html).
    new generateHistory: KMS.DafnyCallEvent<KMS.GenerateDataKeyWithoutPlaintextRequest, Result<KMS.GenerateDataKeyWithoutPlaintextResponse, KMS.Error>>,
    new reEncryptHistory: KMS.DafnyCallEvent<KMS.ReEncryptRequest, Result<KMS.ReEncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    decryptOnlyEncryptionContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))


    // The history elements are "the things I added"
    requires old(kmsClient.History.GenerateDataKeyWithoutPlaintext) < kmsClient.History.GenerateDataKeyWithoutPlaintext
    requires old(kmsClient.History.ReEncrypt) < kmsClient.History.ReEncrypt

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# The call to AWS KMS GenerateDataKeyWithoutPlaintext MUST use the configured AWS KMS client to make the call.
    requires
      && generateHistory in kmsClient.History.GenerateDataKeyWithoutPlaintext[|old(kmsClient.History.GenerateDataKeyWithoutPlaintext)|..]
      && reEncryptHistory in kmsClient.History.ReEncrypt[|old(kmsClient.History.ReEncrypt)|..]
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
    && Structure.BranchKeyContext?(decryptOnlyEncryptionContext)
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

    && Structure.BRANCH_KEY_TYPE_PREFIX < decryptOnlyEncryptionContext[Structure.TYPE_FIELD]
    && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#wrapped-branch-key-creation
    //= type=implication
    //# - `DestinationEncryptionContext` MUST be the [ACTIVE encryption context for branch keys](#active-encryption-context).
    && activeInput.DestinationEncryptionContext == Some(Structure.ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext))

    && reEncryptHistory.output.Success?
    && reEncryptHistory.output.value.CiphertextBlob.Some?

  }

  twostate predicate WrappedBranchKeyVersionV2?(
    new activeOnlyEncryptHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    new versionedEncryptHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    newActiveMaterial: seq<uint8>,
    oldActiveMaterial: seq<uint8>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: Types.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    encryptionContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt

    requires
      && activeOnlyEncryptHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
      && versionedEncryptHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
  {
    && var versionedInput := versionedEncryptHistory.input;
    && |versionedInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && versionedInput.Plaintext[Structure.BKC_DIGEST_LENGTH..] == oldActiveMaterial
    && versionedInput.EncryptionContext == Some(encryptionContext)
    && versionedInput.GrantTokens == Some(grantTokens)

    && var activeInput := activeOnlyEncryptHistory.input;
    && |activeInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && activeInput.Plaintext[Structure.BKC_DIGEST_LENGTH..] == newActiveMaterial
    && activeInput.EncryptionContext == Some(encryptionContext)
    && activeInput.GrantTokens == Some(grantTokens)

    && versionedEncryptHistory.output.Success?
    && versionedEncryptHistory.output.value.CiphertextBlob.Some?

    && activeOnlyEncryptHistory.output.Success?
    && activeOnlyEncryptHistory.output.value.CiphertextBlob.Some?
  }

  method fetchActiveItem(
    branchKeyId: string,
    storage: Types.IKeyStorageInterface,
    logicalKeyStoreName: string
  )
    returns (output: Result<Types.EncryptedHierarchicalKey, Types.Error>)
    requires 0 < |branchKeyId|
    requires storage.ValidState()
    requires storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
             ==>
               logicalKeyStoreName == (storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName
    modifies storage.Modifies
    ensures storage.ValidState()
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
    //= type=implication
    //# VersionKey MUST first get the active version for the branch key from the keystore
    //# by calling the configured [KeyStorage interface's](./key-store/key-storage.md#interface)
    //# [GetEncryptedActiveBranchKey](./key-store/key-storage.md#getencryptedactivebranchkey)
    //# using the `branch-key-id`.
    ensures
      && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
      && var getEncryptedActiveBranchKeyInput := Seq.Last(storage.History.GetEncryptedActiveBranchKey).input;
      && branchKeyId == getEncryptedActiveBranchKeyInput.Identifier
    ensures output.Success? ==>
              && |storage.History.GetEncryptedActiveBranchKey| == |old(storage.History.GetEncryptedActiveBranchKey)| + 1
              && Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.Success?
              && var oldActiveItem := Seq.Last(storage.History.GetEncryptedActiveBranchKey).output.value.Item;
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
              //= type=implication
              //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have the requested `branch-key-id`.
              && oldActiveItem.Identifier == branchKeyId
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
                 //= type=implication
                 //# VersionKey MUST verify that the returned EncryptedHierarchicalKey is an ActiveHierarchicalSymmetricVersion.
              && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
                 //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
                 //= type=implication
                 //# VersionKey MUST verify that the returned EncryptedHierarchicalKey MUST have a logical table name equal to the configured logical table name.
              && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
    ensures output.Success? ==>
              && Structure.ActiveHierarchicalSymmetricKey?(output.value)
              && KmsArn.ValidKmsArn?(output.value.KmsArn)
  {
    var getEncryptedActiveBranchKeyOutput :- storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := branchKeyId
      ));
    var oldActiveItem := getEncryptedActiveBranchKeyOutput.Item;

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && oldActiveItem.Identifier == branchKeyId
           && Structure.ActiveHierarchicalSymmetricKey?(oldActiveItem)
           && oldActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );
    :- Need(
      KmsArn.ValidKmsArn?(oldActiveItem.KmsArn),
      Types.KeyStoreException(
        message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
    );

    return Success(oldActiveItem);
  }

}
