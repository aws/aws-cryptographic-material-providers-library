// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../../../AwsCryptographyPrimitives/Model/AwsCryptographyPrimitivesTypes.dfy"

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

  datatype CryptoAndKMS = CryptoAndKMS(
    kmsConfig: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.Types.GrantTokenList,
    kms: KMS.Types.IKMSClient,
    Crypto: AtomicPrimitives.AtomicPrimitivesClient
  ) {
    ghost predicate ValidState()
    {
      && kms.ValidState()
      && KMS.Types.IsValid_GrantTokenList(grantTokens)
      && KMSKeystoreOperations.HasKeyId(kmsConfig)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfig))
      && kms.Modifies !! Crypto.Modifies
      && Crypto.ValidState()
    }
    ghost const Modifies := multiset(kms.Modifies) + multiset(Crypto.Modifies)
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
    branchKeyIdentifier: string,
    encryptionContext: map<string, string>,
    timestamp: string,
    branchKeyVersion: string,
    logicalKeyStoreName: string,
    kmsConfiguration: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.Types.GrantTokenList,
    kmsClient: KMS.Types.IKMSClient,
    storage: KeyStoreTypes.IKeyStorageInterface,
    hierarchyVersion: KeyStoreTypes.HierarchyVersion
  )
    returns (output: Result<Types.CreateKeyOutput, Types.Error>)
    // Generic Stateful pre and post conditions
    requires
      && kmsClient.ValidState()
      && storage.ValidState()
      && kmsClient.Modifies !! storage.Modifies
    modifies multiset(storage.Modifies) + multiset(kmsClient.Modifies)
    ensures
      && storage.ValidState()
      && kmsClient.ValidState()
      && kmsClient.Modifies !! storage.Modifies
    // 
    requires
      && KMSKeystoreOperations.HasKeyId(kmsConfiguration)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfiguration))
      && hierarchyVersion.v2?
      && 0 < |branchKeyIdentifier|
      && 0 < |branchKeyVersion|
      && forall k <- encryptionContext :: DDB.Types.IsValid_AttributeName(Structure.ENCRYPTION_CONTEXT_PREFIX + k)
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

    var CryptoAndKMS := CryptoAndKMS(kmsConfiguration, grantTokens, kmsClient, crypto);
    var decrytOnlyBKItem :- packAndCallKMS(
      branchKeyContext := decryptOnlyBranchKeyContext,
      CryptoAndKMS := CryptoAndKMS,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );

    var activeBKItem :- packAndCallKMS(
      branchKeyContext := activeBranchKeyContext,
      CryptoAndKMS := CryptoAndKMS,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );

    var beaconBKItem :- packAndCallKMS(
      branchKeyContext := beaconBranchKeyContext,
      CryptoAndKMS := CryptoAndKMS,
      material := beaconPlaintextMaterial,
      encryptionContext := encryptionContext
    );

    // Write ACTIVE, Version & Beacon Items to storage
    var writeItems? := storage.WriteNewEncryptedBranchKey(
      KeyStoreTypes.WriteNewEncryptedBranchKeyInput(
        Active := activeBKItem,
        Version := decrytOnlyBKItem,
        Beacon := beaconBKItem
      )
    );
    var _ :- writeItems?.MapFailure(
      e => Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore:= e
        ));

    assert |storage.History.WriteNewEncryptedBranchKey| == |old(storage.History.WriteNewEncryptedBranchKey)| + 1;
    ghost var writeEvent := storage.History.WriteNewEncryptedBranchKey[-1 % |storage.History.WriteNewEncryptedBranchKey|];
    assert
      && writeEvent.output.Success?
      && writeEvent.input.Active == activeBKItem
      && writeEvent.input.Version == decrytOnlyBKItem
      && writeEvent.input.Beacon == beaconBKItem;
    output := Success(
      Types.CreateKeyOutput(
        Identifier := branchKeyIdentifier,
        HierarchyVersion := hierarchyVersion
      ));
  }

  method packAndCallKMS(
    nameonly branchKeyContext: map<string, string>,
    nameonly CryptoAndKMS: CryptoAndKMS,
    nameonly material: seq<uint8>,
    nameonly encryptionContext: map<string, string>
  )
    returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)

    requires CryptoAndKMS.ValidState()
    modifies CryptoAndKMS.Modifies
    ensures CryptoAndKMS.ValidState()

    requires
      && Structure.BranchKeyContext?(branchKeyContext)
      && |material| == Structure.AES_256_LENGTH as int
      && KMSKeystoreOperations.AttemptKmsOperation?(CryptoAndKMS.kmsConfig, branchKeyContext[Structure.KMS_FIELD])
      && KMSKeystoreOperations.GetKeyId(CryptoAndKMS.kmsConfig) == branchKeyContext[Structure.KMS_FIELD]

    // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
    ensures output.Success? ==>
              && |CryptoAndKMS.kms.History.Encrypt| == |old(CryptoAndKMS.kms.History.Encrypt)| + 1
              && var kmsEvent :=  CryptoAndKMS.kms.History.Encrypt[-1 % |CryptoAndKMS.kms.History.Encrypt|];
              && kmsEvent.output.Success?
              && var kmsInput := kmsEvent.input;
              && KMSKeystoreOperations.Compatible?(CryptoAndKMS.kmsConfig, kmsInput.KeyId)
              && |kmsInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
              && kmsInput.EncryptionContext == Some(encryptionContext)
              && kmsInput.GrantTokens == Some(CryptoAndKMS.grantTokens)
              && kmsEvent.output.value.CiphertextBlob.Some?
              && var digest := kmsInput.Plaintext[..Structure.BKC_DIGEST_LENGTH];
              && material == kmsInput.Plaintext[Structure.BKC_DIGEST_LENGTH..]
              && |CryptoAndKMS.Crypto.History.Digest| == |old(CryptoAndKMS.Crypto.History.Digest)| + 1
              && var digestEvent := CryptoAndKMS.Crypto.History.Digest[-1 % |CryptoAndKMS.Crypto.History.Digest|];
              && digestEvent.output.Success?
              && digestEvent.output.value == digest
              && digestEvent.input.digestAlgorithm == AtomicPrimitives.Types.SHA_384
  {
    var digest? := HvUtils.CreateBKCDigest(branchKeyContext, CryptoAndKMS.Crypto);
    var digest :- digest?.MapFailure(
      e => Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore:= e));
    var plaintextTuple := HvUtils.PackPlainTextTuple(digest, material);
    var wrappedMaterial? := KMSKeystoreOperations.EncryptKey(
      plaintextTuple,
      encryptionContext,
      branchKeyContext[Structure.KMS_FIELD],
      CryptoAndKMS.kmsConfig,
      CryptoAndKMS.grantTokens,
      CryptoAndKMS.kms
    );
    var wrappedMaterial :- wrappedMaterial?.MapFailure(e => ConvertKmsErrorToError(e));
    return Success(Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial));
  }
}
