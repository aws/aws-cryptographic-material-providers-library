// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../../AwsCryptographyPrimitives/Model/AwsCryptographyPrimitivesTypes.dfy"
include "BKSAOperationUtils.dfy"
include "KmsUtils.dfy"

module {:options "/functionSyntax:4" } CreateKeysHV2 {
  // Standard Library Imports
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import opened UInt = StandardLibrary.UInt
  import Time
    // SDK Imports
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
    // Crypto Primitives Imports
  import AtomicPrimitives
    // MPL Imports
  import AwsArnParsing
  import CanonicalEncryptionContext
    // (Branch) Key Store Imports
  import Structure
  import DefaultKeyStorageInterface
  import KMSKeystoreOperations
  import ErrorMessages = KeyStoreErrorMessages
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import KmsArn
    // (Branch) Key Store Admin Imports
  import HvUtils = HierarchicalVersionUtils
  import Types = AwsCryptographyKeyStoreAdminTypes
  import OptUtils = BKSAOperationUtils
  import KmsUtils

  /** Constrains the relationship of the Crypto & KMS client, 
    ensuring they a valid but their histories are separate.
    Also allows us to make claims about the Grant Tokens and kmsConfig. */
  datatype CryptoAndKms = CryptoAndKms(
    kmsConfig: KeyStoreTypes.KMSConfiguration,
    kms: KmsUtils.keyManagerStrat,
    crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) {
    ghost predicate ValidState()
    {
      && kms.ValidState()
      && KMSKeystoreOperations.HasKeyId(kmsConfig)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfig))
      && kms.Modifies !! crypto.Modifies
      && crypto.ValidState()
    }
    ghost const Modifies := multiset(kms.Modifies) + multiset(crypto.Modifies)
  }

  function ConvertKmsErrorToError(
    e: KMSKeystoreOperations.KmsError
  ): Types.Error
  {
    match e {
      // KMS errors ->
      case ComAmazonawsKms(comAmazonawsKms: KMS.Types.Error) =>
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
  method CreateBranchAndBeaconKeys(
    nameonly branchKeyIdentifier: string,
    nameonly encryptionContext: map<string, string>,
    nameonly timestamp: string,
    nameonly branchKeyVersion: string,
    nameonly logicalKeyStoreName: string,
    nameonly kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    nameonly keyManagerAndStorage: OptUtils.KeyManagerAndStorage,
    nameonly hierarchyVersion: KeyStoreTypes.HierarchyVersion
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    requires
      // TODO-HV-2-M? : Support KmsDecryptEncrypt?
      && keyManagerAndStorage.keyManagerStrat.kmsSimple?
      && keyManagerAndStorage.ValidState()
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && hierarchyVersion.v2?
      && 0 < |branchKeyIdentifier|
      && 0 < |branchKeyVersion|
      && forall k <- encryptionContext :: DDB.Types.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
    modifies keyManagerAndStorage.Modifies
    ensures keyManagerAndStorage.ValidState()
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

    // Get crypto client
    var crypto? := HvUtils.ProvideCryptoClient();
    var crypto :- crypto?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e
        )
    );

    // Generate Random Bytes as Plaintext for ACTIVE & Beacon Item's
    // TODO-HV-2-M4 : Improve error messages for generate random failure
    var activePlaintextMaterial? := crypto.GenerateRandomBytes(
      AtomicPrimitives.Types.GenerateRandomBytesInput(length := 32)
    );
    var activePlaintextMaterial :- activePlaintextMaterial?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e
        ));

    var beaconPlaintextMaterial? := crypto.GenerateRandomBytes(
      AtomicPrimitives.Types.GenerateRandomBytesInput(length := 32)
    );
    var beaconPlaintextMaterial :- beaconPlaintextMaterial?.MapFailure(
      e => Types.AwsCryptographyPrimitives(
          AwsCryptographyPrimitives := e));

    var CryptoAndKms := CryptoAndKms(kmsConfiguration, keyManagerAndStorage.keyManagerStrat, crypto);
    var decryptOnlyBKItem :- packAndCallKMS(
      branchKeyContext := decryptOnlyBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext,
      hierarchyVersion := hierarchyVersion
    );

    var activeBKItem :- packAndCallKMS(
      branchKeyContext := activeBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext,
      hierarchyVersion := hierarchyVersion
    );

    var beaconBKItem :- packAndCallKMS(
      branchKeyContext := beaconBranchKeyContext,
      cryptoAndKms := CryptoAndKms,
      material := beaconPlaintextMaterial,
      encryptionContext := encryptionContext,
      hierarchyVersion := hierarchyVersion
    );

    // Write ACTIVE, Version & Beacon Items to storage
    var writeItems? := keyManagerAndStorage.storage.WriteNewEncryptedBranchKey(
      KeyStoreTypes.WriteNewEncryptedBranchKeyInput(
        Active := activeBKItem,
        Version := decryptOnlyBKItem,
        Beacon := beaconBKItem
      )
    );
    var _ :- writeItems?.MapFailure(
      e => Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore:= e
        ));
    // By making this ghost, we avoid the Dafny transpiler emitting in Java etc.
    ghost var storage := keyManagerAndStorage.storage;
    assert |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1;
    ghost var writeEvent := Seq.Last(storage.History.WriteNewEncryptedBranchKey);
    assert
      && writeEvent.output.Success?
      && writeEvent.input.Active == activeBKItem
      && writeEvent.input.Version == decryptOnlyBKItem
      && writeEvent.input.Beacon == beaconBKItem;
    output := Success(
      Types.CreateKeyOutput(
        Identifier := branchKeyIdentifier,
        HierarchyVersion := hierarchyVersion
      ));
  }

  method packAndCallKMS(
    nameonly branchKeyContext: map<string, string>,
    nameonly cryptoAndKms: CryptoAndKms,
    nameonly material: seq<uint8>,
    nameonly encryptionContext: map<string, string>,
    nameonly hierarchyVersion: KeyStoreTypes.HierarchyVersion
  )
    returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires
      && cryptoAndKms.ValidState()
      && Structure.BranchKeyContext?(branchKeyContext)
      && |material| == Structure.AES_256_LENGTH as int
      && KMSKeystoreOperations.AttemptKmsOperation?(cryptoAndKms.kmsConfig, branchKeyContext[Structure.KMS_FIELD])
      && KMSKeystoreOperations.GetKeyId(cryptoAndKms.kmsConfig) == branchKeyContext[Structure.KMS_FIELD]
         // TODO-HV-2-M? : Support KmsDecryptEncrypt?
      && hierarchyVersion.v2?
      && KmsUtils.IsSupportedKeyManagerStrategy(hierarchyVersion, cryptoAndKms.kms)
    modifies cryptoAndKms.Modifies
    // Note: even if the method fails, the clients are ValidState
    ensures cryptoAndKms.ValidState()
    ensures
      // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
      && output.Success? ==>
        && var encryptKmsTuple := KmsUtils.getEncryptKMSTuple(cryptoAndKms.kms);
        && var encryptKmsClient := encryptKmsTuple.kmsClient;
        && var encryptGrantTokens := encryptKmsTuple.grantTokens;
        && |encryptKmsClient.History.Encrypt| == |old(encryptKmsClient.History.Encrypt)| + 1
        && var kmsEvent :=  Seq.Last(encryptKmsClient.History.Encrypt);
        && kmsEvent.output.Success?
        && var kmsInput := kmsEvent.input;
        && KMSKeystoreOperations.Compatible?(cryptoAndKms.kmsConfig, kmsInput.KeyId)
        && |kmsInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
        && kmsInput.EncryptionContext == Some(encryptionContext)
        && kmsInput.GrantTokens == Some(encryptGrantTokens)
        && kmsEvent.output.value.CiphertextBlob.Some?
        && var digest := kmsInput.Plaintext[..Structure.BKC_DIGEST_LENGTH];
        && material == kmsInput.Plaintext[Structure.BKC_DIGEST_LENGTH..]
        && |cryptoAndKms.crypto.History.Digest| == |old(cryptoAndKms.crypto.History.Digest)| + 1
        && var digestEvent := Seq.Last(cryptoAndKms.crypto.History.Digest);
        && digestEvent.output.Success?
        && digestEvent.output.value == digest
        && digestEvent.input.digestAlgorithm == AtomicPrimitives.Types.SHA_384
  {
    var digest? := HvUtils.CreateBKCDigest(branchKeyContext, cryptoAndKms.crypto);
    var digest :- digest?.MapFailure(
      e => Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore:= e));
    var plaintextTuple := HvUtils.PackPlainTextTuple(digest, material);
    var encryptKMSTuple := KmsUtils.getEncryptKMSTuple(cryptoAndKms.kms);
    var wrappedMaterial? := KMSKeystoreOperations.EncryptKey(
      plaintextTuple,
      encryptionContext,
      branchKeyContext[Structure.KMS_FIELD],
      cryptoAndKms.kmsConfig,
      encryptKMSTuple.grantTokens,
      encryptKMSTuple.kmsClient
    );
    var wrappedMaterial :- wrappedMaterial?.MapFailure(e => ConvertKmsErrorToError(e));
    return Success(Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial));
  }
}
