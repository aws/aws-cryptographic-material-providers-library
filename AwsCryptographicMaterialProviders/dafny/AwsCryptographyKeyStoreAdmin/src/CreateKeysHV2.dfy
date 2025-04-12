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

  // TODO-HV-2-GA : We need to refactor BKSA and probably BKS to have a CryptoClient so we can make statements
  // about the history of the SHA requests.
  // lemma assumeSHAIsInjective(
  //   messageADigestEvent: CryptoTypes.DafnyCallEvent<CryptoTypes.DigestInput, Result<seq<uint8>, CryptoTypes.Error>>,
  //   messageBDigestEvent: CryptoTypes.DafnyCallEvent<CryptoTypes.DigestInput, Result<seq<uint8>, CryptoTypes.Error>>
  // )
  // {
  //   assume {:axiom}
  //     && messageADigestEvent.output.Success?
  //     && messageBDigestEvent.output.Success?
  //     ==>
  //       (messageADigestEvent.input.message != messageBDigestEvent.input.message
  //        <==>
  //        messageADigestEvent.output.value != messageBDigestEvent.output.value);
  // }

  // TODO-HV-2-GA: Update Specification for HV-2 Branch Key Creation
  //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
  //= type=implication
  //# To create a branch key, this operation MUST take the following:
  //#
  //# - `branchKeyId`: The identifier
  //# - `encryptionContext`: Additional encryption context to bind to the created keys
  method {:isolate_assertions} CreateBranchAndBeaconKeys(
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

    requires kmsClient.ValidState() && storage.ValidState()
    modifies storage.Modifies, kmsClient.Modifies
    ensures storage.ValidState() && kmsClient.ValidState()

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

    // Generate Random Bytes as Plaintext for ACTIVE & Beacon Item's
    // TODO-HV-2-M4 : Improve error messages for generate random failure
    var activePlaintextMaterial? := crypto.GenerateRandomBytes(
      AtomicPrimitives.Types.GenerateRandomBytesInput(length := 32)
    );
    var activePlaintextMaterial
      :-
      activePlaintextMaterial?.MapFailure(
        e => Types.AwsCryptographyPrimitives(
            AwsCryptographyPrimitives := e
          ));

    var beaconPlaintextMaterial? := crypto.GenerateRandomBytes(
      AtomicPrimitives.Types.GenerateRandomBytesInput(length := 32)
    );
    var beaconPlaintextMaterial
      :-
      beaconPlaintextMaterial?.MapFailure(
        e => Types.AwsCryptographyPrimitives(
            AwsCryptographyPrimitives := e));

    var kmsThings := KMSThings(kmsConfiguration, grantTokens, kmsClient);
    var decrytOnlyBKItem :- packAndCallKMS(
      branchKeyContext := decryptOnlyBranchKeyContext,
      kmsThings := kmsThings,
      Crypto := crypto,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );

    var activeBKItem :- packAndCallKMS(
      branchKeyContext := activeBranchKeyContext,
      kmsThings := kmsThings,
      Crypto := crypto,
      material := activePlaintextMaterial,
      encryptionContext := encryptionContext
    );

    var beaconBKItem :- packAndCallKMS(
      branchKeyContext := beaconBranchKeyContext,
      kmsThings := kmsThings,
      Crypto := crypto,
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

  datatype KMSThings = KMSThings(
    kmsConfig: KeyStoreTypes.KMSConfiguration,
    grantTokens: KMS.Types.GrantTokenList,
    kmsClient: KMS.Types.IKMSClient
  ) {
    ghost predicate ValidState()
    {
      && kmsClient.ValidState()
      && KMS.Types.IsValid_GrantTokenList(grantTokens)
      && KMSKeystoreOperations.HasKeyId(kmsConfig)
      && KmsArn.ValidKmsArn?(KMSKeystoreOperations.GetKeyId(kmsConfig))
    }
    ghost const Modifies := kmsClient.Modifies
  }

  method packAndCallKMS(
    nameonly branchKeyContext: map<string, string>,
    nameonly kmsThings: KMSThings,
    nameonly Crypto: AtomicPrimitives.AtomicPrimitivesClient,
    nameonly material: seq<uint8>,
    nameonly encryptionContext: map<string, string>
  )
    returns (output: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)

    requires kmsThings.ValidState() && Crypto.ValidState()
    modifies kmsThings.Modifies, Crypto.Modifies
    ensures kmsThings.ValidState() && Crypto.ValidState()

    requires
      && Structure.BranchKeyContext?(branchKeyContext)
      && |material| == Structure.AES_256_LENGTH as int
      && KMSKeystoreOperations.AttemptKmsOperation?(kmsThings.kmsConfig, branchKeyContext[Structure.KMS_FIELD])
      && KMSKeystoreOperations.GetKeyId(kmsThings.kmsConfig) == branchKeyContext[Structure.KMS_FIELD]

    ensures output.Success? ==>
              && old(kmsThings.kmsClient.History.Encrypt) < kmsThings.kmsClient.History.Encrypt
              && |kmsThings.kmsClient.History.Encrypt| == |old(kmsThings.kmsClient.History.Encrypt)| + 1
              && var kmsEvent :=  kmsThings.kmsClient.History.Encrypt[-1 % |kmsThings.kmsClient.History.Encrypt|];
              && kmsEvent.output.Success?
              && var kmsInput := kmsEvent.input;
              && KMSKeystoreOperations.Compatible?(kmsThings.kmsConfig, kmsInput.KeyId)
              && |kmsInput.Plaintext| == (Structure.BKC_DIGEST_LENGTH + Structure.AES_256_LENGTH) as int
              && kmsInput.EncryptionContext == Some(encryptionContext)
              && kmsInput.GrantTokens == Some(kmsThings.grantTokens)
              && kmsEvent.output.value.CiphertextBlob.Some?
    // TODO-HV-2-FOLLOW : Formal Verification of this has taken me too many hours
    // && var digest := kmsInput.Plaintext[..Structure.BKC_DIGEST_LENGTH];
    // && |Crypto.History.Digest| == |old(Crypto.History.Digest)| + 1
    // && var digestEvent := Crypto.History.Digest[-1 % |Crypto.History.Digest|];
    // && digestEvent.output.Success?
    // && digestEvent.output.value == digest
  {
    var digest? := HvUtils.CreateBKCDigest(branchKeyContext, Crypto);
    var digest :- digest?.MapFailure(
      e => Types.AwsCryptographyKeyStore(
          AwsCryptographyKeyStore:= e));
    assert |Crypto.History.Digest| == |old(Crypto.History.Digest)| + 1;
    ghost var CryptoHistLen := |Crypto.History.Digest|;
    ghost var digestEvent := Crypto.History.Digest[-1 % |Crypto.History.Digest|];
    var plaintextTuple := HvUtils.PackPlainTextTuple(digest, material);
    var wrappedMaterial? := KMSKeystoreOperations.EncryptKey(
      plaintextTuple,
      encryptionContext,
      branchKeyContext[Structure.KMS_FIELD],
      kmsThings.kmsConfig,
      kmsThings.grantTokens,
      kmsThings.kmsClient
    );
    var wrappedMaterial :- wrappedMaterial?.MapFailure(e => ConvertKmsErrorToError(e));
    // assert |Crypto.History.Digest| == CryptoHistLen by
    // { assume {:axiom} |Crypto.History.Digest| == CryptoHistLen;}
    ghost var kmsEvent :=  kmsThings.kmsClient.History.Encrypt[-1 % |kmsThings.kmsClient.History.Encrypt|];
    assert
      && kmsEvent.output.Success?
      && ghost var digest := kmsEvent.input.Plaintext[..Structure.BKC_DIGEST_LENGTH];
         && digestEvent.output.value == digest;
    return Success(Structure.ConstructEncryptedHierarchicalKey(branchKeyContext, wrappedMaterial));
  }
}
