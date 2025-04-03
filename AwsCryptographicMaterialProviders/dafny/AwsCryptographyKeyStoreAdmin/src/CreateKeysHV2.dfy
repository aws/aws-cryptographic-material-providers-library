// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../../AwsCryptographyPrimitives/Model/AwsCryptographyPrimitivesTypes.dfy"
include "../../AwsCryptographyKeyStore/src/Structure.dfy"
include "../../AwsCryptographyKeyStore/src/DefaultKeyStorageInterface.dfy"
include "../../AwsCryptographyKeyStore/src/KMSKeystoreOperations.dfy"
include "../../AwsCryptographyKeyStore/src/ErrorMessages.dfy"
include "../../AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographyKeyStore/src/KmsArn.dfy"
include "SystemKey/ContentHandler.dfy"

// TODO-HV-2-M1: WIP
module {:options "/functionSyntax:4" } CreateKeysHV2 {
  // TODO-HV-2-M1-FF: Group imports according to libraries
  import opened StandardLibrary
  import opened Wrappers
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages

  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import Types = AwsCryptographyKeyStoreAdminTypes
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import AwsArnParsing
  import KmsArn
  import AtomicPrimitives
  import CanonicalEncryptionContext
  import Time
  import HvUtils = HierarchicalVersionUtils
  import CryptoTypes = AwsCryptographyPrimitivesTypes
  import ContentHandler = SystemKey.ContentHandler

  function ConvertKmsErrorToError(
    e: KMSKeystoreOperations.KmsError
  ): Types.Error
  {
    match e {
      // KMS errors ->
      case ComAmazonawsKms(comAmazonawsKms: KMS.Error) =>
        Types.ComAmazonawsKms(
          ComAmazonawsKms := comAmazonawsKms
        )
      case KeyManagementException(msg) =>
        Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore := e
        )
      case BranchKeyCiphertextException(msg) =>
        Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore := e
        )
    }
  }

  // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
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
    kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    kmsClient: KMS.IKMSClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    hierarchyVersion: KeyStoreTypes.HierarchyVersion
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires 0 < |branchKeyIdentifier|
    requires 0 < |branchKeyVersion|
    requires forall k <- customEncryptionContext :: DDB.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    requires storage.Modifies !! kmsClient.Modifies
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires hierarchyVersion.v2?

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# This operation MUST create a [branch key](structures.md#branch-key) and a [beacon key](structures.md#beacon-key) according to
    //# the [Branch Key and Beacon Key Creation](#branch-key-and-beacon-key-creation) section.
    ensures
      output.Success?
      ==>
        && |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
        && old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt
           // Use negative indexing to select correct KMS Encrypt calls ("-i % |seq|" is effectively negative indexing)
           // The first request we made is for the new DecryptOnly BKI
        && var kmsEncryptRequestForDecryptOnlyBKI := kmsClient.History.Encrypt[-3 % |kmsClient.History.Encrypt|];
        // The second request we made is for the new ACTIVE BKI
        && var kmsEncryptRequestForActiveBKI := kmsClient.History.Encrypt[-2 % |kmsClient.History.Encrypt|];
        // The third and last request we made is for the new Beacon BKI
        && var kmsEncryptRequestForBeaconBKI := kmsClient.History.Encrypt[-1 % |kmsClient.History.Encrypt|];
        && kmsEncryptRequestForDecryptOnlyBKI.output.Success?
        && kmsEncryptRequestForActiveBKI.output.Success?
        && kmsEncryptRequestForBeaconBKI.output.Success?
           // TODO-HV-2-M1-FF: Refactor EncryptionContext usage into BranchKeyContext
        && var decryptOnlyBranchKeyContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
                                                branchKeyIdentifier,
                                                branchKeyVersion,
                                                timestamp,
                                                logicalKeyStoreName,
                                                KMSKeystoreOperations.GetKeyId(kmsConfiguration),
                                                hierarchyVersion,
                                                customEncryptionContext
                                              );

        //= aws-encryption-sdk-specification/framework/branch-key-store.md#logical-keystore-name
        //= type=implication
        //# The logical keystore name MUST be bound to every created key.
        && decryptOnlyBranchKeyContext[Structure.TABLE_FIELD] == logicalKeyStoreName

        //= aws-encryption-sdk-specification/framework/branch-key-store.md#encryption-context
        //= type=implication
        //# Any additionally attributes in the EncryptionContext
        //# of the [encrypted hierarchical key](./key-store/key-storage.md#encryptedhierarchicalkey)
        //# MUST be added to the encryption context.
        && (forall k <- customEncryptionContext
              ::
                && Structure.ENCRYPTION_CONTEXT_PREFIX + k in decryptOnlyBranchKeyContext
                && decryptOnlyBranchKeyContext[Structure.ENCRYPTION_CONTEXT_PREFIX + k] == customEncryptionContext[k])

        && WrappedBranchKeyCreationHV2?(
             kmsEncryptRequestForDecryptOnlyBKI,
             kmsEncryptRequestForActiveBKI,
             kmsClient,
             kmsConfiguration,
             grantTokens,
             customEncryptionContext,
             decryptOnlyBranchKeyContext
           )

        && WrappedBeaconKeyCreationHV2?(
             kmsEncryptRequestForBeaconBKI,
             kmsClient,
             kmsConfiguration,
             grantTokens,
             customEncryptionContext,
             decryptOnlyBranchKeyContext
           )

        && |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
           //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
           //= type=implication
           //# If writing to the keystore succeeds,
           //# the operation MUST return the branch-key-id that maps to both
           //# the branch key and the beacon key.
        && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Active
           == Structure.ConstructEncryptedHierarchicalKey(
                Structure.ActiveBranchKeyEncryptionContext(decryptOnlyBranchKeyContext),
                kmsEncryptRequestForActiveBKI.output.value.CiphertextBlob.value
              )
        && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Version
           == Structure.ConstructEncryptedHierarchicalKey(
                decryptOnlyBranchKeyContext,
                kmsEncryptRequestForDecryptOnlyBKI.output.value.CiphertextBlob.value
              )
        && Seq.Last(storage.History.WriteNewEncryptedBranchKey).input.Beacon
           == Structure.ConstructEncryptedHierarchicalKey(
                Structure.BeaconKeyEncryptionContext(decryptOnlyBranchKeyContext),
                kmsEncryptRequestForBeaconBKI.output.value.CiphertextBlob.value
              )

        && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Success?
        && output.value.Identifier == branchKeyIdentifier

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
    //= type=implication
    //# Otherwise, this operation MUST yield an error.
    ensures
      // TODO-HV-2-FOLLOW : Is there another way to represent this? This is also not nearly all the possible failrues...
      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 1
          && Seq.Last(kmsClient.History.Encrypt).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 2
          && Seq.Last(Seq.DropLast(kmsClient.History.Encrypt)).output.Failure?
          ==> output.Failure?)

      || (&& |kmsClient.History.Encrypt| == |old(kmsClient.History.Encrypt)| + 3
          && Seq.Last(Seq.DropLast(Seq.DropLast(kmsClient.History.Encrypt))).output.Failure?
          ==> output.Failure?)

      || (&& |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1
          && Seq.Last(storage.History.WriteNewEncryptedBranchKey).output.Failure?
          ==> output.Failure?)

  {
    // Construct Branch Key Contexts for ACTIVE, Version and Beacon items.
    var decryptOnlyBranchKeyContext := Structure.DecryptOnlyBranchKeyEncryptionContext(
      branchKeyIdentifier,
      branchKeyVersion,
      timestamp,
      logicalKeyStoreName,
      KMSKeystoreOperations.GetKeyId(kmsConfiguration),
      hierarchyVersion,
      customEncryptionContext
    );
    assert decryptOnlyBranchKeyContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2;
    var activeBranchKeyContext := Structure.ActiveBranchKeyEncryptionContext(decryptOnlyBranchKeyContext);
    var beaconBranchKeyContext := Structure.BeaconKeyEncryptionContext(decryptOnlyBranchKeyContext);

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    var crypto :- crypto?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e
        )
    );

    // Create SHA-384 digests for Branch Key Context's
    var decryptOnlyDigest? := HvUtils.CreateBKCDigest(decryptOnlyBranchKeyContext, crypto);
    var decryptOnlyDigest :- decryptOnlyDigest?.MapFailure(e => Types.AwsCryptographyKeyStore(
                                                               AwsCryptographyKeyStore:= e
                                                             ));
    var activeDigest? := HvUtils.CreateBKCDigest(activeBranchKeyContext, crypto);
    var activeDigest :- activeDigest?.MapFailure(e => Types.AwsCryptographyKeyStore(
                                                     AwsCryptographyKeyStore:= e
                                                   ));
    var beaconDigest? := HvUtils.CreateBKCDigest(beaconBranchKeyContext, crypto);
    var beaconDigest :- beaconDigest?.MapFailure(e => Types.AwsCryptographyKeyStore(
                                                     AwsCryptographyKeyStore:= e
                                                   ));

    // Generate Random Bytes as Plaintext for ACTIVE & Beacon Item's
    // TODO-HV-2-M4 : Improve error messages for generate random failure
    var activePlaintextMaterial? := crypto.GenerateRandomBytes(
      CryptoTypes.GenerateRandomBytesInput(length := 32)
    );
    var activePlaintextMaterial :- activePlaintextMaterial?.MapFailure(e => Types.AwsCryptographyPrimitives(
                                                                           AwsCryptographyPrimitives := e
                                                                         ));

    var beaconPlaintextMaterial? := crypto.GenerateRandomBytes(
      CryptoTypes.GenerateRandomBytesInput(length := 32)
    );
    var beaconPlaintextMaterial :- beaconPlaintextMaterial?.MapFailure(e => Types.AwsCryptographyPrimitives(
                                                                           AwsCryptographyPrimitives := e
                                                                         ));

    // Pack BKC Digest & Plaintext
    var activePlaintextTuple := HvUtils.PackPlainTextTuple(activeDigest, activePlaintextMaterial);
    var decryptOnlyPlaintextTuple := HvUtils.PackPlainTextTuple(decryptOnlyDigest, activePlaintextMaterial);
    var beaconPlaintextTuple := HvUtils.PackPlainTextTuple(beaconDigest, beaconPlaintextMaterial);

    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, decryptOnlyBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.EncryptKey(
      decryptOnlyPlaintextTuple,
      customEncryptionContext,
      decryptOnlyBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    var wrappedDecryptOnlyBranchKey :- wrappedDecryptOnlyBranchKey?.MapFailure(e => ConvertKmsErrorToError(e));
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, activeBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedActiveBranchKey? := KMSKeystoreOperations.EncryptKey(
      activePlaintextTuple,
      customEncryptionContext,
      activeBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    var wrappedActiveBranchKey :- wrappedActiveBranchKey?.MapFailure(e => ConvertKmsErrorToError(e));
    assert KMSKeystoreOperations.AttemptKmsOperation?(kmsConfiguration, beaconBranchKeyContext[Structure.KMS_FIELD]);
    var wrappedBeaconKey? := KMSKeystoreOperations.EncryptKey(
      beaconPlaintextTuple,
      customEncryptionContext,
      beaconBranchKeyContext[Structure.KMS_FIELD],
      kmsConfiguration,
      grantTokens,
      kmsClient
    );
    var wrappedBeaconKey :- wrappedBeaconKey?.MapFailure(e => ConvertKmsErrorToError(e));
    // Write ACTIVE, Version & Beacon Items to storage
    var writeItems? := storage.WriteNewEncryptedBranchKey(
      KeyStoreTypes.WriteNewEncryptedBranchKeyInput(
        Active := Structure.ConstructEncryptedHierarchicalKey(
          activeBranchKeyContext,
          wrappedActiveBranchKey
        ),
        Version := Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyBranchKeyContext,
          wrappedDecryptOnlyBranchKey
        ),
        Beacon := Structure.ConstructEncryptedHierarchicalKey(
          beaconBranchKeyContext,
          wrappedBeaconKey
        )
      )
    );
    var _ :- writeItems?
    .MapFailure(e => Types.AwsCryptographyKeyStore(
                    AwsCryptographyKeyStore:= e
                  ));

    output := Success(
      Types.CreateKeyOutput(
        Identifier := branchKeyIdentifier,
        HierarchyVersion := hierarchyVersion
      ));
  }

  twostate predicate WrappedBranchKeyCreationHV2?(
    new decryptOnlyHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    new activeHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    customEncryptionContext:  map<string, string>,
    decryptOnlyBranchKeyContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))

    requires old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt

    // requires
    //   && decryptOnlyHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
    //   && activeHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
  {
    // Verify the KMS request to create the decrypt-only ciphertext was constructed correctly
    && var decryptOnlyInput := decryptOnlyHistory.input;
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, decryptOnlyInput.KeyId)
    && |decryptOnlyInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int // HV2 uses 80 bytes (48 for digest + 32 for key)
    && decryptOnlyInput.EncryptionContext == Some(customEncryptionContext)
    && decryptOnlyInput.GrantTokens == Some(grantTokens)
    && decryptOnlyHistory.output.Success?
    && decryptOnlyHistory.output.value.CiphertextBlob.Some?
    && decryptOnlyHistory.output.value.KeyId.Some?
    && decryptOnlyHistory.output.value.KeyId.value == KMSKeystoreOperations.GetKeyId(kmsConfiguration)

    // Verify the KMS request to create the ACTIVE ciphertext was constructed correctly
    && var activeInput := activeHistory.input;
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, activeInput.KeyId)
    && |activeInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && activeInput.EncryptionContext == Some(customEncryptionContext)
    && activeInput.GrantTokens == Some(grantTokens)
    && activeHistory.output.Success?
    && activeHistory.output.value.CiphertextBlob.Some?
    && activeHistory.output.value.KeyId.Some?
    && activeHistory.output.value.KeyId.value == KMSKeystoreOperations.GetKeyId(kmsConfiguration)

    // Verify branch key context  relationships
    && Structure.BranchKeyContext?(decryptOnlyBranchKeyContext)
    && Structure.BRANCH_KEY_TYPE_PREFIX < decryptOnlyBranchKeyContext[Structure.TYPE_FIELD]
    && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyBranchKeyContext
    && decryptOnlyBranchKeyContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2
  }

  twostate predicate WrappedBeaconKeyCreationHV2?(
    new beaconHistory: KMS.DafnyCallEvent<KMS.EncryptRequest, Result<KMS.EncryptResponse, KMS.Error>>,
    kmsClient: KMS.IKMSClient,
    kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.GrantTokenList,
    customEncryptionContext:  map<string, string>,
    decryptOnlyBranchKeyContext: map<string, string>
  )
    reads kmsClient.History
    requires KMSKeystoreOperations.HasKeyId(kmsConfiguration) && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
    requires Structure.BranchKeyContext?(decryptOnlyBranchKeyContext)
    requires old(kmsClient.History.Encrypt) < kmsClient.History.Encrypt
    requires beaconHistory in kmsClient.History.Encrypt[|old(kmsClient.History.Encrypt)|..]
  {
    // Verify the KMS request to create the Beacon ciphertext was constructed correctly
    && var beaconInput := beaconHistory.input;
    && KMSKeystoreOperations.Compatible?(kmsConfiguration, beaconInput.KeyId)
    && |beaconInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
    && beaconInput.EncryptionContext == Some(customEncryptionContext)
    && beaconInput.GrantTokens == Some(grantTokens)
    && beaconHistory.output.Success?
    && beaconHistory.output.value.CiphertextBlob.Some?
    && beaconHistory.output.value.KeyId.Some?
    && beaconHistory.output.value.KeyId.value == KMSKeystoreOperations.GetKeyId(kmsConfiguration)

    // Verify branch key context for beacon
    && Structure.BRANCH_KEY_TYPE_PREFIX < decryptOnlyBranchKeyContext[Structure.TYPE_FIELD]
    && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyBranchKeyContext
    && decryptOnlyBranchKeyContext[Structure.HIERARCHY_VERSION] == Structure.HIERARCHY_VERSION_VALUE_2
  }
}
