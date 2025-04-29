// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "PrefixUtils.dfy"
include "KeyStoreAdminHelpers.dfy"
include "MutationIndexUtils.dfy"
include "SystemKey/Handler.dfy"
include "Mutations.dfy"
include "MutationErrorRefinement.dfy"
include "KeyStoreAdminErrorMessages.dfy"
include "CommitmentAndIndex.dfy"

module {:options "/functionSyntax:4" } InternalInitializeMutation {
  // StandardLibrary Imports
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import Time
  import UUID
  import UTF8
    // KMS & MPL Imports
  import KMS = ComAmazonawsKmsTypes
  import AwsKmsUtils
  import AtomicPrimitives
    // KeyStore Imports
  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import HvUtils = HierarchicalVersionUtils
  import Structure
  import DefaultKeyStorageInterface
  import KeyStoreErrorMessages
  import KmsArn
  import KMSKeystoreOperations
  import HVUtils = HierarchicalVersionUtils
  import KmsUtils
    // KeyStoreAdmin Imports
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdminHelpers
  import StateStrucs = MutationStateStructures
  import PrefixUtils
  import MutationIndexUtils
  import SystemKeyHandler = SystemKey.Handler
  import Mutations
  import MutationErrorRefinement
  import KeyStoreAdminErrorMessages
  import CommitmentAndIndex

  datatype InternalInitializeMutationInput = | InternalInitializeMutationInput (
    nameonly Identifier: string ,
    nameonly Mutations: Types.Mutations ,
    nameonly SystemKey: KeyStoreAdminHelpers.InternalSystemKey ,
    nameonly DoNotVersion: bool,
    nameonly logicalKeyStoreName: string,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
  {
    ghost predicate ValidState()
    {
      && SystemKey.ValidState()
      && keyManagerStrategy.ValidState()
      && storage.ValidState()
      && SystemKey.Modifies !! keyManagerStrategy.Modifies !! storage.Modifies
      && (!Mutations.TerminalHierarchyVersion.Some? || KmsUtils.IsSupportedKeyManagerStrategy(Mutations.TerminalHierarchyVersion.value, keyManagerStrategy))
    }
  }

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function {:isolate_assertions} ValidateInitializeMutationInput(
    input: InternalInitializeMutationInput
  ): (output: Result<InternalInitializeMutationInput, Types.Error>)
    requires input.ValidState()
    ensures
      output.Success?
      ==>
        && StateStrucs.ValidMutations?(input.Mutations)
        && 0 < |input.Identifier|
        && output.value.ValidState()
    ensures
      && output.Success?
      && input.Mutations.TerminalKmsArn.Some?
      ==>
        && KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)
    ensures
      && input.Mutations.TerminalHierarchyVersion.Some?
      && input.Mutations.TerminalHierarchyVersion.value.v1?
      ==> output.Failure?
  {
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Branch Key Identifier cannot be empty!"));
    var terminalEC := input.Mutations.TerminalEncryptionContext.UnwrapOr(map[]);
    :- Need(
         terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
         Types.KeyStoreAdminException(
           message := "The terminal encryption context provided includes a key that is reserved for Crypto Tools library."));

    // Dafny struggles with Map operations; but Dafny will filter the keys of a map by a condition.
    // Thus, to ensure that there are no keys in the input that are already prefixed,
    // we count the number of keys that are NOT prefixed,
    // and assert that the number of keys that are NOT prefixed
    // is equal to the total number of keys.
    var filterByPrefix := PrefixUtils.FilterMapForKeysThatDoNotBeginWithPrefix(
                            prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
                            aMap := terminalEC);
    :- Need(
         |filterByPrefix| == |terminalEC|,
         Types.KeyStoreAdminException(
           message :=
             "The terminal encryption context provided includes one or more keys that start with `"
             + Structure.ENCRYPTION_CONTEXT_PREFIX + "`."
             + " The Key Store will always add this prefix to provided encryption context."
             + " To avoid unintended double prefixing,"
             + " the Key Store forbids custom Encryption Context keys from starting with this prefix."
             + " Ensure the encryption context provided does not include these values."));

    :- Need(
         && (input.Mutations.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)),
         Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
       );
    :- Need(StateStrucs.ValidMutations?(input.Mutations),
            Types.KeyStoreAdminException(
              message := "Mutations parameter is invalid; If Encryption Context is given, it cannot be empty or have empty values."));
    // TODO-HV-2-M4: Support TerminalHV1? but don't support downgrading from hv-2 to hv-1.
    :- Need(
         !IsMutationsTerminalHV1?(input.Mutations),
         Types.UnsupportedFeatureException(message := KeyStoreAdminErrorMessages.NO_MUTATE_TO_HV_1));
    Success(input)
  }

  predicate IsMutationsTerminalHV1?(mutations: Types.Mutations)
  {
    mutations.TerminalHierarchyVersion.Some? && mutations.TerminalHierarchyVersion.value.v1?
  }

  method {:isolate_assertions} InitializeMutation(
    input: InternalInitializeMutationInput
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires StateStrucs.ValidMutations?(input.Mutations) // may not need this
    requires
      && input.storage.ValidState()
      && input.keyManagerStrategy.ValidState()
      && input.SystemKey.ValidState()
      && input.ValidState()
    requires
      && ValidateInitializeMutationInput(input).Success?
    ensures
      && input.storage.ValidState()
      && input.SystemKey.ValidState()
      && input.keyManagerStrategy.ValidState()
      && input.ValidState()
    modifies
      input.storage.Modifies,
             input.keyManagerStrategy.Modifies,
             input.SystemKey.Modifies
  {
    var resumeMutation? := false;

    // Fetch Active Branch Key & Beacon Key & Mutation Lock
    var readItems? := input.storage.GetItemsForInitializeMutation(
      Types.AwsCryptographyKeyStoreTypes.GetItemsForInitializeMutationInput(Identifier := input.Identifier));
    var readItems :- readItems?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    if (readItems.MutationCommitment.None? && readItems.MutationIndex.Some?) {
      var indexUUID := readItems.MutationIndex.value.UUID;
      return Failure(
          Types.MutationInvalidException(
            message := "Found a Mutation Index but no Mutation Commitment."
            + " The Key Store's Storage, for this Branch Key, has become corrupted."
            + " Recommend auditing the Branch Key's items for tampering."
            + " Recommend auditing access to the storage."
            + " To successfully start a new mutation, delete the Mutation Index."
            + " But know that the new mutation will fail if any corrupt items are encountered."
            + "\nBranch Key ID: " + input.Identifier + ";"
            + " Mutation Index UUID: " + indexUUID));
    }

    if (readItems.MutationCommitment.Some?) {
      :- Need(
        CommitmentAndIndex.ValidCommitment?(readItems.MutationCommitment.value),
        Types.AwsCryptographyKeyStore(
          // We decided that Storage would not care about the Byte Structure of MUTATION_COMMITMENT's attributes.
          // But I think a Storage Exception makes sense for a corrupted item.
          AwsCryptographyKeyStore := KeyStoreTypes.KeyStorageException(
            message := "Mutation Commitment read from Storage is invalid or corrupted."
            + " Recommend auditing the Branch Key's items for tampering."
            + " Recommend auditing access to the storage."
            + " To successfully start a new mutation, delete the Mutation Commitment."
            + " But know that the new mutation will fail if any corrupt items are encountered."
            + "\nBranch Key ID: " + input.Identifier + ";"
            + " Mutation Commitment UUID: " + readItems.MutationCommitment.value.UUID)));
      resumeMutation? :- CommitmentAndInputMatch(
        internalInput := input,
        commitment := readItems.MutationCommitment.value);
      if (resumeMutation?) {
        output := ResumeMutation(
          commitment := readItems.MutationCommitment.value,
          index := readItems.MutationIndex,
          logicalKeyStoreName := input.logicalKeyStoreName,
          storage := input.storage,
          systemKey := input.SystemKey);
        return output;
      }
      return Failure(
          Types.MutationConflictException(
            message :=
              "A Mutation is already in-flight!"
              + " The in-flight Mutation was created with a different Input."
              + " Complete the in-flight before starting a new one. "
              + " If you need to resume the in-flight Mutation,"
              + " provide identical input to InitializeMutation."
              + " DescribeMutation can be used to retrieve the verbatim input."
              + " MutationCommitment UUID: " + readItems.MutationCommitment.value.UUID
              + " CreatedOn: " + readItems.MutationCommitment.value.CreateTime
              + " BranchKeyID: " + input.Identifier
          ));
    }

    var activeItem := readItems.ActiveItem;

    :- Need(
      || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.ActiveItem.Identifier == input.Identifier
           && Structure.ActiveHierarchicalSymmetricKey?(readItems.ActiveItem)
           && readItems.ActiveItem.EncryptionContext[Structure.TABLE_FIELD] == input.logicalKeyStoreName
           && KmsArn.ValidKmsArn?(activeItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Active Branch Key Item read from storage is malformed!")
    );
    var isTerminalHv2 := input.Mutations.TerminalHierarchyVersion.Some? &&
                         input.Mutations.TerminalHierarchyVersion.value.v2?;
    :- Need(
      !isTerminalHv2 || HvUtils.HasUniqueTransformedKeys?(readItems.ActiveItem.EncryptionContext),
      Types.KeyStoreAdminException(
        message :=
          KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
      )
    );
    :- Need(
      || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && readItems.BeaconItem.Identifier == input.Identifier
           && Structure.ActiveHierarchicalSymmetricBeaconKey?(readItems.BeaconItem)
           && readItems.BeaconItem.EncryptionContext[Structure.TABLE_FIELD] == input.logicalKeyStoreName
           && KmsArn.ValidKmsArn?(readItems.BeaconItem.KmsArn)
         ),
      Types.KeyStoreAdminException(
        message := "Beacon Branch Key Item read from storage is malformed!")
    );

      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
    :- Need(
      && (input.Mutations.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)),
      Types.KeyStoreAdminException(message := "The terminal KMS ARN is invalid. Note that Aliases are not allowed.")
    );

    // timestamp is for the new Active & Decrypt Only AND for the Mutation Commitment
    var timestamp? := Time.GetCurrentTimeStamp();
    var timestamp :- timestamp?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate a timestamp: " + e));

    var mutationCommitmentUUID? := UUID.GenerateUUID();
    var mutationCommitmentUUID :- mutationCommitmentUUID?
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for Mutation Commitment. " + e));

    var inferredOriginalEC
      := map k <- activeItem.EncryptionContext
                  // This pull everything that is not in our restricted list.
             | k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
      :: k := activeItem.EncryptionContext[k];

    // To Preserve Unexpected/un-modeled Attributes.
    // We need to copy them from inferredOriginalEC to terminalEC.
    // Which means we need to select those members without a prefix,
    // and copy them over to terminal.
    var unexpectedEC := PrefixUtils.FilterMapForKeysThatDoNotBeginWithPrefix(
      prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
      aMap := inferredOriginalEC
    );
    assert unexpectedEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;

    var terminalEC?: Option<KeyStoreTypes.EncryptionContextString> := None;
    if (input.Mutations.TerminalEncryptionContext.Some?) {

      var terminalEC := PrefixUtils.AddingPrefixToKeysOfMapDoesNotCreateCollisions(
        prefix := Structure.ENCRYPTION_CONTEXT_PREFIX,
        aMap := input.Mutations.TerminalEncryptionContext.value
      ) + unexpectedEC;
      // ValidateInitializeMutationInput SHOULD take care of this Need, but Dafny is struggling
      // TODO-Mutations-FF : Replace runtime check with Lemma.
      // See https://github.com/aws/aws-cryptographic-material-providers-library/pull/750#discussion_r1777654751
      :- Need(
        terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES,
        Types.KeyStoreAdminException(message:="Terminal Encryption Context contains a reserved word!")
      );
      terminalEC? := Some(terminalEC);
      assert terminalEC.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
      :- Need(
        && (!isTerminalHv2 || HvUtils.HasUniqueTransformedKeys?(terminalEC)),
        Types.KeyStoreAdminException(
          message := KeyStoreErrorMessages.NOT_UNIQUE_TERMINAL_EC_AND_EXISTING_ATTRIBUTE
        )
      );
    }

    assert KmsArn.ValidKmsArn?(activeItem.KmsArn);
    var inferredOriginalHV: KeyStoreTypes.HierarchyVersion
      :=
      Structure.StringToHierarchyVersion(activeItem.EncryptionContext[Structure.HIERARCHY_VERSION]);
    var MutationToApply := StateStrucs.MutationToApply(
      Identifier := input.Identifier,
      Original := StateStrucs.MutableProperties(
        kmsArn := activeItem.KmsArn,
        customEncryptionContext := inferredOriginalEC,
        hierarchyVersion := inferredOriginalHV
      ),
      Terminal := StateStrucs.MutableProperties(
        kmsArn := input.Mutations.TerminalKmsArn.UnwrapOr(activeItem.KmsArn),
        customEncryptionContext := terminalEC?.UnwrapOr(inferredOriginalEC),
        hierarchyVersion := input.Mutations.TerminalHierarchyVersion.UnwrapOr(inferredOriginalHV)
      ),
      ExclusiveStartKey := None,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp,
      Input := input.Mutations,
      CommitmentCiphertext := [0], // TODO-Mutations-GA Create Commitment Ciphertext
      IndexCiphertext := [0] // TODO-Mutations-GA Create Index Ciphertext
    );
    :- Need(
      KmsUtils.IsSupportedKeyManagerStrategy(MutationToApply.Terminal.hierarchyVersion, input.keyManagerStrategy),
      Types.UnsupportedFeatureException(
        message :=
          KeyStoreAdminErrorMessages.UNSUPPORTED_KEY_MANAGEMENT_STRATEGY
      )
    );

    assert MutationToApply.Original.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.Terminal.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.ValidState();

    // --= Validate Active Branch Key
    var verifyActive? := Mutations.VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation",
      mutationToApply := MutationToApply
    );
    if (verifyActive?.Failure?) {
      return Failure(verifyActive?.error);
    }

      // -= Assert Beacon Key is in Original
    :- Need(
      readItems.BeaconItem.KmsArn == MutationToApply.Original.kmsArn,
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not encrypted with the same KMS Key as ACTIVE!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST have the same KMS-ARN and Custom Encryption Context!"
      ));
    :- Need(
      readItems.BeaconItem.EncryptionContext
      ==
      Structure.ReplaceMutableContext(
        readItems.BeaconItem.EncryptionContext,
        readItems.BeaconItem.KmsArn,
        MutationToApply.Original.customEncryptionContext,
        MutationToApply.Original.hierarchyVersion),
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not in the Original State!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST be in the original state."
      ));


    var initializeMutationActiveInput := InitializeMutationActiveInput(
      input := input,
      activeItem := activeItem,
      mutationToApply := MutationToApply,
      timestamp := timestamp);
    assert initializeMutationActiveInput.ValidState();
    var initializeMutationActiveOutput :- InitializeMutationActive(initializeMutationActiveInput);

    // -= Mutate Beacon Key
    var newBeaconKey :- Mutations.MutateItem(readItems.BeaconItem, MutationToApply, input.keyManagerStrategy, "InitializeMutation", false);

    // -= Create Mutation Commitment & Mutation Index
    var MutationCommitment :- StateStrucs.SerializeMutationCommitment(MutationToApply);
    var MutationIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, None);

    // -= Apply System Key to Commitment & Mutation Index
    var SignedMutationCommitment :- SystemKeyHandler.SignCommitment(MutationCommitment, input.SystemKey);
    var SignedMutationIndex :- SystemKeyHandler.SignIndex(MutationIndex, input.SystemKey);

    // -= Write Mutation Commitment, new branch key version, mutated beacon key
    var throwAway2? := input.storage.WriteInitializeMutation(
      KeyStoreTypes.WriteInitializeMutationInput(
        Active := initializeMutationActiveOutput.writeActive,
        Version := initializeMutationActiveOutput.writeVersion,
        Beacon := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newBeaconKey, Old:=readItems.BeaconItem),
        MutationCommitment :=  SignedMutationCommitment,
        MutationIndex := SignedMutationIndex
      ));
    // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Commitment get written?
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var logStatements :=
      [
        Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + mutationCommitmentUUID, Description := "Created"),
        Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + mutationCommitmentUUID, Description := "Created")
      ]
      + initializeMutationActiveOutput.logStatements
      + [Types.MutatedBranchKeyItem(ItemType := "Beacon", Description := "Mutated")];

    var Token := Types.MutationToken(
      Identifier := input.Identifier,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp);

    var Flag: Types.InitializeMutationFlag := Types.Created();

    return Success(Types.InitializeMutationOutput(
                     MutationToken := Token,
                     MutatedBranchKeyItems := logStatements,
                     InitializeMutationFlag := Flag));
  }

  method {:isolate_assertions} CreateNewTerminalDecryptOnlyBranchKey(
    decryptOnlyEncryptionContext: Structure.BranchKeyContext,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat
  )
    returns (res: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires KmsArn.ValidKmsArn?(mutationToApply.Terminal.kmsArn)
    requires KMSKeystoreOperations.AttemptKmsOperation?(
               KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn), decryptOnlyEncryptionContext[Structure.KMS_FIELD]
             )
    requires keyManagerStrategy.ValidState()
    requires KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, keyManagerStrategy)
    modifies keyManagerStrategy.Modifies
    ensures keyManagerStrategy.ValidState()
    ensures res.Success? ==>
              && Structure.BranchKeyContext?(res.value.EncryptionContext)
              && Structure.EncryptedHierarchicalKeyFromStorage?(res.value)
              && res.value.KmsArn == KMSKeystoreOperations.GetKeyId(KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn))
              && Structure.BRANCH_KEY_TYPE_PREFIX < res.value.EncryptionContext[Structure.TYPE_FIELD]
              && Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD !in decryptOnlyEncryptionContext
  {
    var grantTokens: KMS.GrantTokenList;
    var kmsClient: KMS.IKMSClient;
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        grantTokens := kms.grantTokens;
        kmsClient := kms.kmsClient;
      case decryptEncrypt(kmsD, kmsE) =>
        grantTokens := kmsE.grantTokens;
        kmsClient := kmsE.kmsClient;
      case kmsSimple(kms) =>
        grantTokens := kms.grantTokens;
        kmsClient := kms.kmsClient;
    }

    var newDecryptOnly : KeyStoreTypes.EncryptedHierarchicalKey;
    match mutationToApply.Terminal.hierarchyVersion {
      case v1 =>
        var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
          encryptionContext := decryptOnlyEncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn),
          grantTokens := grantTokens,
          kmsClient := kmsClient
        );

        if (wrappedDecryptOnlyBranchKey?.Failure?) {
          var error := MutationErrorRefinement.GenerateNewActiveException(
            identifier := decryptOnlyEncryptionContext[Structure.BRANCH_KEY_IDENTIFIER_FIELD],
            kmsArn := mutationToApply.Terminal.kmsArn,
            error := wrappedDecryptOnlyBranchKey?.error);
          return Failure(error);
        }
        
        newDecryptOnly := Structure.ConstructEncryptedHierarchicalKey(
          decryptOnlyEncryptionContext,
          wrappedDecryptOnlyBranchKey?.value.CiphertextBlob.value
        );

      case v2 =>
        if !HvUtils.HasUniqueTransformedKeys?(decryptOnlyEncryptionContext) {
          return Failure(Types.Error.AwsCryptographyKeyStore(
                            KeyStoreTypes.BranchKeyCiphertextException(
                          message := KeyStoreErrorMessages.NOT_UNIQUE_BRANCH_KEY_CONTEXT_KEYS
                        )));
        }
        // var ecToKMS := HvUtils.SelectKmsEncryptionContextForHv2(decryptOnlyEncryptionContext);

        var plaintextMaterial? := KMSKeystoreOperations.GetPlaintextDataKeyViaGenerateDataKey(
          branchKeyContext := decryptOnlyEncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn),
          grantTokens := grantTokens,
          kmsClient := kmsClient
        );
        
        if (plaintextMaterial?.Failure?) {
          var error := MutationErrorRefinement.GenerateNewActiveException(
            identifier := decryptOnlyEncryptionContext[Structure.BRANCH_KEY_IDENTIFIER_FIELD],
            kmsArn := mutationToApply.Terminal.kmsArn,
            error := plaintextMaterial?.error);
          return Failure(error);
        }
        
        // Get crypto client
        var crypto? := HvUtils.ProvideCryptoClient();
        var crypto :- crypto?.MapFailure(
          e => Types.AwsCryptographyPrimitives(
              AwsCryptographyPrimitives := e
            )
        );

        var kmsSimpleStrategy := KmsUtils.keyManagerStrat.kmsSimple(
          kmsSimple := KmsUtils.KMSTuple(kmsClient := kmsClient, grantTokens := grantTokens
        ));

        var CryptoAndKms := KMSKeystoreOperations.CryptoAndKms(
          KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn),
          kmsSimpleStrategy,
          crypto
        );
        // var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.packAndCallKMS(
        //   branchKeyContext := decryptOnlyEncryptionContext,
        //   cryptoAndKms := CryptoAndKms,
        //   material := plaintextMaterial?.value.Plaintext.value,
        //   encryptionContext := ecToKMS
        // );
        
        // if (wrappedDecryptOnlyBranchKey?.Failure?) {
        //   var error := MutationErrorRefinement.GenerateNewActiveException(
        //     identifier := decryptOnlyEncryptionContext[Structure.BRANCH_KEY_IDENTIFIER_FIELD],
        //     kmsArn := mutationToApply.Terminal.kmsArn,
        //     error := wrappedDecryptOnlyBranchKey?.error);
        //   return Failure(error);
        // }
    }


    // :- Need(
    //   Structure.BRANCH_KEY_TYPE_PREFIX < newDecryptOnly.EncryptionContext[Structure.TYPE_FIELD],
    //   Types.KeyStoreAdminException(message := "Invalid Branch Key prefix.")
    // );

    // return Success(newDecryptOnly);
    return Failure(Types.KeyStoreAdminException(
        message := "Mutation Commitment's Input is not a Valid UTF-8 Byte sequence."));
  }

  function CommitmentAndInputMatch(
    nameonly internalInput: InternalInitializeMutationInput,
    nameonly commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<bool, Types.Error>)
    requires 0 < |commitment.UUID| && 0 < |commitment.Identifier|
    requires UTF8.ValidUTF8Seq(commitment.Input)
  {
    var readMutations :- StateStrucs.DeserializeMutationInput(commitment);
    var givenMutations := internalInput.Mutations;
    Success(readMutations == givenMutations)
  }

  method {:isolate_assertions} ResumeMutation(
    nameonly commitment: KeyStoreTypes.MutationCommitment,
    nameonly index: Option<KeyStoreTypes.MutationIndex>,
    nameonly logicalKeyStoreName: string,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface,
    nameonly systemKey: KeyStoreAdminHelpers.InternalSystemKey
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires storage.ValidState() && systemKey.ValidState()
    ensures storage.ValidState() && systemKey.ValidState()
    modifies storage.Modifies, systemKey.Modifies
    ensures
      output.Success? && index.Some?
      ==>
        index.value.UUID == commitment.UUID
  {
    var mutatedBranchKeyItems := [
      Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + commitment.UUID, Description := "Matched Input")
    ];
    var Flag: Types.InitializeMutationFlag := Types.Resumed();
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Original),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Original is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Terminal),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Terminal is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && UTF8.ValidUTF8Seq(commitment.Input),
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Input is not a Valid UTF-8 Byte sequence."));
    :- Need(
      && 0 < |commitment.Identifier|,
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's Identifier cannot be empty."));
    :- Need(
      && 0 < |commitment.UUID|,
      Types.KeyStoreAdminException(
        message := "Mutation Commitment's UUID cannot be empty."));
    var commitmentIsVerified :- SystemKeyHandler.VerifyCommitment(commitment, systemKey);
    :- Need(
      commitmentIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Commitment's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));
    var token := Types.MutationToken(
      Identifier := commitment.Identifier,
      UUID := commitment.UUID,
      CreateTime := commitment.CreateTime);

    if (index.None?) {
      Flag := Types.ResumedWithoutIndex();
      var timestamp? := Time.GetCurrentTimeStamp();
      var timestamp :- timestamp?
      .MapFailure(e => Types.KeyStoreAdminException(
                      message := "Could not generate a timestamp: " + e));
      var newIndex := KeyStoreTypes.MutationIndex(
        Identifier := commitment.Identifier,
        PageIndex := MutationIndexUtils.ExclusiveStartKeyToPageIndex(None),
        UUID := commitment.UUID,
        CreateTime := timestamp,
        CiphertextBlob := [0] // [0] is a temporary place holder, but we should fix this by creating an internal type
      );
      var signedMutationIndex :- SystemKeyHandler.SignIndex(newIndex, systemKey);
      assert CommitmentAndIndex.ValidIndex?(signedMutationIndex);
      // -= Write Mutation Index, conditioned on Mutation Commitment
      var throwAway2? := storage.WriteMutationIndex(
        KeyStoreTypes.WriteMutationIndexInput(
          MutationCommitment := commitment,
          MutationIndex := signedMutationIndex
        ));
      // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
      // What Condition Check failed?
      var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
      mutatedBranchKeyItems := mutatedBranchKeyItems
      + [Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + commitment.UUID, Description := "Created")];
    } else {
      var commitmentAndIndex := CommitmentAndIndex.CommitmentAndIndex(commitment, index.value);
      :- CommitmentAndIndex.MutationItemsValidIDs(commitmentAndIndex);
      :- CommitmentAndIndex.MutationItemsValidUTF8(commitmentAndIndex);
      var indexIsVerified :- SystemKeyHandler.VerifyIndex(commitmentAndIndex.index, systemKey);
      :- Need(
        indexIsVerified,
        Types.MutationVerificationException(
          message:=
            "Mutation Index's failed the System Key's Signature Verification."
            + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
            + " Mutation cannot continue. Audit Key Store's Storage's access."
            + " The Mutation will need to be manually restarted."));
    }

    return Success(Types.InitializeMutationOutput(
                     MutationToken := token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));

  }

  datatype InitializeMutationActiveInput =
    | InitializeMutationActiveInput (
        nameonly input: InternalInitializeMutationInput,
        nameonly activeItem: KeyStoreTypes.EncryptedHierarchicalKey,
        nameonly mutationToApply: StateStrucs.MutationToApply,
        nameonly timestamp: string
      )
  {
    ghost predicate ValidState()
    {
      && input.ValidState()
      && activeItem.Type.ActiveHierarchicalSymmetricVersion?
      && mutationToApply.ValidState()
      && 0 < |timestamp|
      && 0 < |input.Identifier|
      && activeItem.KmsArn == mutationToApply.Original.kmsArn
      && Structure.EncryptedHierarchicalKeyFromStorage?(activeItem)
      && KmsUtils.IsSupportedKeyManagerStrategy(mutationToApply.Terminal.hierarchyVersion, input.keyManagerStrategy)
    }

    ghost const Modifies :=
      input.keyManagerStrategy.ModifiesMultiSet
      + multiset(input.SystemKey.Modifies)
      + multiset(input.storage.Modifies)
  }

  datatype InitializeMutationActiveOutput =
    | InitializeMutationActiveOutput(
        nameonly writeActive: KeyStoreTypes.OverWriteEncryptedHierarchicalKey,
        nameonly writeVersion: KeyStoreTypes.WriteInitializeMutationVersion,
        nameonly logStatements: seq<Types.MutatedBranchKeyItem>
      )
  {
    ghost predicate ValidState()
    {
      && |logStatements| == 2
    }
  }

  method InitializeMutationActive(
    localInput: InitializeMutationActiveInput
  )
    returns (output: Result<InitializeMutationActiveOutput, Types.Error>)
    requires localInput.ValidState()
    modifies localInput.Modifies
    requires KmsUtils.IsSupportedKeyManagerStrategy(localInput.mutationToApply.Terminal.hierarchyVersion, localInput.input.keyManagerStrategy)
    ensures localInput.ValidState()
    ensures
      && localInput.input.DoNotVersion
      && output.Success?
      ==>
        output.value.writeVersion.mutate?
    ensures
      && !localInput.input.DoNotVersion
      && output.Success?
      ==>
        output.value.writeVersion.rotate?
    ensures output.Success? ==> output.value.ValidState()
  {
    if (localInput.input.DoNotVersion) {
      output := InitializeMutationActiveMutate(localInput);
    } else {
      output := InitializeMutationRotate(localInput);
    }
    return output;
  }

  method InitializeMutationRotate(
    localInput: InitializeMutationActiveInput
  )
    returns (output: Result<InitializeMutationActiveOutput, Types.Error>)
    requires localInput.ValidState()
    modifies localInput.Modifies
    ensures localInput.ValidState()
    requires !localInput.input.DoNotVersion
    requires KmsUtils.IsSupportedKeyManagerStrategy(localInput.mutationToApply.Terminal.hierarchyVersion, localInput.input.keyManagerStrategy)
    ensures
      output.Success?
      ==>
        && output.value.ValidState()
        && output.value.writeVersion.rotate?
        && output.value.logStatements[0].Description == "Rotated"
        && |output.value.logStatements| == 2
  {
    // --= Generate New Decrypt Only Branch Key with terminal properties
    var maybeNewVersion := UUID.GenerateUUID();
    var newVersion :- maybeNewVersion
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for new Decrypt Only. " + e));

    var decryptOnlyEncryptionContext := Mutations.DecryptOnlyBranchKeyEncryptionContextForMutation(
      localInput.input.Identifier,
      newVersion,
      localInput.timestamp,
      localInput.input.logicalKeyStoreName,
      localInput.mutationToApply.Terminal.kmsArn,
      localInput.mutationToApply.Terminal.hierarchyVersion,
      localInput.mutationToApply.Terminal.customEncryptionContext
    );

    // TODO-Mutations-GA? :: If the KMS Call fails with access denied,
    // it indicates that the MPL Consumer does not have access to
    // GenerateDataKeyWithoutPlaintext on the terminal key.
    var newDecryptOnly :- CreateNewTerminalDecryptOnlyBranchKey(
      decryptOnlyEncryptionContext,
      localInput.mutationToApply,
      localInput.input.keyManagerStrategy
    );

    var ActiveEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(newDecryptOnly.EncryptionContext);

    var newActive;
    if (localInput.input.keyManagerStrategy.decryptEncrypt?) {
      newActive :- Mutations.NewActiveItemForDecryptEncrypt(
        item := newDecryptOnly,
        terminalKmsArn := localInput.mutationToApply.Terminal.kmsArn,
        terminalEncryptionContext := ActiveEncryptionContext,
        keyManagerStrategy := localInput.input.keyManagerStrategy,
        localOperation := "InitializeMutation"
      );
    } else {
      var input := Mutations.ReEncryptHierarchicalKeyInput(
        item := newDecryptOnly,
        originalKmsArn := localInput.mutationToApply.Terminal.kmsArn,
        terminalKmsArn := localInput.mutationToApply.Terminal.kmsArn,
        terminalEncryptionContext := ActiveEncryptionContext,
        keyManagerStrategy := localInput.input.keyManagerStrategy
      );
      newActive :- Mutations.ReEncryptHierarchicalKey(
        input := input,
        localOperation := "InitializeMutation",
        createNewActive := true);
    }

    return Success(
        InitializeMutationActiveOutput(
          writeActive := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newActive, Old:=localInput.activeItem),
          writeVersion := KeyStoreTypes.WriteInitializeMutationVersion.rotate(rotate:=newDecryptOnly),
          logStatements := [
            Types.MutatedBranchKeyItem(ItemType := "Active: " + newVersion, Description := "Rotated"),
            Types.MutatedBranchKeyItem(ItemType := "Decrypt Only: " + newVersion, Description := "Created")
          ]
        ));
  }

  method InitializeMutationActiveMutate(
    localInput: InitializeMutationActiveInput
  )
    returns (output: Result<InitializeMutationActiveOutput, Types.Error>)
    requires localInput.ValidState()
    modifies localInput.Modifies
    ensures localInput.ValidState()
    requires localInput.input.DoNotVersion
    requires KmsUtils.IsSupportedKeyManagerStrategy(localInput.mutationToApply.Terminal.hierarchyVersion, localInput.input.keyManagerStrategy)
    ensures
      output.Success?
      ==>
        && output.value.writeVersion.mutate?
        && |output.value.logStatements| == 2
  {
    // Get the Active's Decrypt Only
    var oldVersion := localInput.activeItem.Type.ActiveHierarchicalSymmetricVersion.Version;
    var getOldReq := KeyStoreTypes.GetEncryptedBranchKeyVersionInput(
      Identifier := localInput.input.Identifier,
      Version := oldVersion);
    var getOldRes? := localInput.input.storage.GetEncryptedBranchKeyVersion(getOldReq);
    var getOldRes :- getOldRes?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

      // If custom storage, validate read Decrypt Only
    :- Need(
      || localInput.input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           && Mutations.ValidateItemFromStorage?(
                localInput.input.storage, getOldRes.Item,
                identifier := localInput.input.Identifier,
                logicalName := localInput.input.logicalKeyStoreName)
           && Structure.DecryptOnlyHierarchicalSymmetricKey?(getOldRes.Item)
           && getOldRes.Item.Type.HierarchicalSymmetricVersion?
         ),
      Types.KeyStoreAdminException(
        message := "Version (Decrypt Only) Item read from storage is malformed! Version: "
        + Structure.BRANCH_KEY_TYPE_PREFIX + oldVersion)
    );
    :- Need(
      getOldRes.Item.EncryptionContext[Structure.HIERARCHY_VERSION] == Structure.HierarchyVersionToString(localInput.mutationToApply.Original.hierarchyVersion),
      Types.KeyStoreAdminException(
        message := "The original hiearchical version and the branch key context hiearchical version does not match"
      )
    );

    // Assert Decrypt Only is in Original
    var oldDecrypt := Mutations.MatchItemToState(getOldRes.Item, localInput.mutationToApply);
    :- Need(
      oldDecrypt.itemOriginal?,
      Types.UnexpectedStateException(
        message := "Version (Decrypt Only) Item read from storage is not in the expected original state!"
        + " Version: " + Structure.BRANCH_KEY_TYPE_PREFIX + oldVersion)
    );

    // Mutate the Active
    var newActive :- Mutations.MutateItem(
      localInput.activeItem,
      localInput.mutationToApply,
      localInput.input.keyManagerStrategy,
      "InitializeMutation", false);
    // Mutate the decryptOnly
    var newDecrypt :- Mutations.MutateItem(
      oldDecrypt.item,
      localInput.mutationToApply,
      localInput.input.keyManagerStrategy,
      "InitializeMutation", false);
    var writeVersion := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newDecrypt, Old:=oldDecrypt.item);
    return Success(
        InitializeMutationActiveOutput(
          writeActive := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newActive, Old:=localInput.activeItem),
          writeVersion := KeyStoreTypes.WriteInitializeMutationVersion.mutate(mutate:=writeVersion),
          logStatements := [
            Types.MutatedBranchKeyItem(ItemType := "Active: " + oldVersion, Description := "Mutated"),
            Types.MutatedBranchKeyItem(ItemType := "Decrypt Only: " + oldVersion, Description := "Mutated")
          ]
        ));
  }
}