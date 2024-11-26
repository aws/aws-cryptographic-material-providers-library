// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "MutationStateStructures.dfy"
include "PrefixUtils.dfy"
include "MutationValidation.dfy"
include "MutationErrorRefinement.dfy"
include "KmsUtils.dfy"
include "MutationIndexUtils.dfy"
include "MutationsConstants.dfy"
include "SystemKey/Handler.dfy"

module {:options "/functionSyntax:4" } Mutations {
  import opened StandardLibrary
  import opened Wrappers
  import opened Seq
  import Time
  import UUID

  import KeyStoreTypes = AwsCryptographyKeyStoreAdminTypes.AwsCryptographyKeyStoreTypes
  import Structure
  import DefaultKeyStorageInterface
  import ErrorMessages = KeyStoreErrorMessages
  import DDB = ComAmazonawsDynamodbTypes
  import KMS = ComAmazonawsKmsTypes
  import UTF8
  import KmsArn
  import KMSKeystoreOperations
  import AwsKmsUtils

  import Types = AwsCryptographyKeyStoreAdminTypes
  import StateStrucs = MutationStateStructures
  import PrefixUtils
  import MutationValidation
  import MutationErrorRefinement
  import KmsUtils
  import MutationIndexUtils
  import M_ErrorMessages = MutationsConstants.ErrorMessages
  import SystemKeyHandler = SystemKey.Handler

  const DEFAULT_APPLY_PAGE_SIZE := 3 as StandardLibrary.UInt.int32

  datatype CheckedItem =
    | itemOriginal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
    | itemTerminal(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)
      // Never describe itemNeither to customers as such.
      // Always use the `UnExecptedStateException`.
    | itemNeither(item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey)

  type OriginalOrTerminal = s:seq<CheckedItem>
    | forall i <- s :: !i.itemNeither?
    witness *

  datatype InternalInitializeMutationInput = | InternalInitializeMutationInput (
    nameonly Identifier: string ,
    nameonly Mutations: Types.Mutations ,
    nameonly SystemKey: KmsUtils.InternalSystemKey ,
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
    }
  }

  predicate ValidateQueryOutResults?(
    input: InternalApplyMutationInput, //Types.ApplyMutationInput,
    queryItems: KeyStoreTypes.QueryForVersionsOutput
  )
  {
    || input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
    || (
         forall item <- queryItems.Items ::
           && item.Identifier == input.MutationToken.Identifier
           && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
           && item.Type.HierarchicalSymmetricVersion?
           && item.EncryptionContext[Structure.TABLE_FIELD] == input.logicalKeyStoreName
           && KmsArn.ValidKmsArn?(item.KmsArn)
       )
  }

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function {:isolate_assertions} ValidateInitializeMutationInput(
    input: InternalInitializeMutationInput
  ): (output: Result<InternalInitializeMutationInput, Types.Error>)
    ensures
      output.Success?
      ==>
        && StateStrucs.ValidMutations?(input.Mutations)
    ensures
      && output.Success?
      && input.Mutations.TerminalKmsArn.Some?
      ==>
        && KmsArn.ValidKmsArn?(input.Mutations.TerminalKmsArn.value)
    ensures
      && output.Success?
      ==>
        input.DoNotVersion == false
  {
    :- Need(
         input.DoNotVersion == false,
         Types.UnsupportedFeatureException(message := "At this time, DoNotVersion MUST be false.")
       );
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
    Success(input)
  }

  method {:isolate_assertions} InitializeMutation(
    input: InternalInitializeMutationInput
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires ValidateInitializeMutationInput(input).Success?
    requires StateStrucs.ValidMutations?(input.Mutations) // may not need this
    requires
      && input.storage.ValidState()
      && match input.keyManagerStrategy {
           case reEncrypt(km) => km.kmsClient.ValidState() && AwsKmsUtils.GetValidGrantTokens(Some(km.grantTokens)).Success?
           case decryptEncrypt(kmD, kmE) =>
             && kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
             && AwsKmsUtils.GetValidGrantTokens(Some(kmD.grantTokens)).Success?
             && AwsKmsUtils.GetValidGrantTokens(Some(kmE.grantTokens)).Success?
         }
      && input.SystemKey.ValidState()
      && input.ValidState()
    ensures
      && input.storage.ValidState()
      && input.SystemKey.ValidState()
      &&
         match input.keyManagerStrategy {
           case reEncrypt(km) => km.kmsClient.ValidState()
           case decryptEncrypt(kmD, kmE) => kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
         }
      && input.ValidState()
    modifies
      input.storage.Modifies,
             match input.keyManagerStrategy {
               case reEncrypt(km) => km.kmsClient.Modifies
               case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
             },
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
      resumeMutation? :- CommitmentAndInputMatch(
        internalInput := input,
        commitment := readItems.MutationCommitment.value);
      if (resumeMutation?) {
        // TODO-SystemKey :: ResumeMutation will validate SystemKey
        output := ResumeMutation(
          commitment := readItems.MutationCommitment.value,
          index := readItems.MutationIndex,
          logicalKeyStoreName := input.logicalKeyStoreName,
          storage := input.storage, // );//,
          SystemKey := input.SystemKey);
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
    }

    assert KmsArn.ValidKmsArn?(activeItem.KmsArn);
    var MutationToApply := StateStrucs.MutationToApply(
      Identifier := input.Identifier,
      Original := StateStrucs.MutableProperties(
        kmsArn := activeItem.KmsArn,
        customEncryptionContext := inferredOriginalEC
      ),
      Terminal := StateStrucs.MutableProperties(
        kmsArn := input.Mutations.TerminalKmsArn.UnwrapOr(activeItem.KmsArn),
        customEncryptionContext := terminalEC?.UnwrapOr(inferredOriginalEC)
      ),
      ExclusiveStartKey := None,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp,
      Input := input.Mutations,
      CommitmentCiphertext := [0], // TODO-Mutations-GA Create Commitment Ciphertext
      IndexCiphertext := [0] // TODO-Mutations-GA Create Index Ciphertext
    );

    assert MutationToApply.Original.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.Terminal.customEncryptionContext.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES;
    assert MutationToApply.ValidState();
    // -= BEGIN Version Active Branch Key
    // --= Validate Active Branch Key
    var verifyActive? := VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );
    if (verifyActive?.Fail?) {
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
        MutationToApply.Original.customEncryptionContext),
      Types.UnexpectedStateException(
        message :=
          "Beacon Item is not in the Original State!"
          + " For Initialize Mutation to succeed, the ACTIVE & Beacon Key MUST be in the original state."
      ));

    // --= Generate New Decrypt Only Branch Key with terminal properties
    var maybeNewVersion := UUID.GenerateUUID();
    var newVersion :- maybeNewVersion
    .MapFailure(e => Types.KeyStoreAdminException(
                    message := "Could not generate UUID for new Decrypt Only. " + e));


    var decryptOnlyEncryptionContext := MutationValidation.DecryptOnlyBranchKeyEncryptionContextForMutation(
      input.Identifier,
      newVersion,
      timestamp,
      input.logicalKeyStoreName,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    // TODO-Mutations-GA? :: If the KMS Call fails with access denied,
    // it indicates that the MPL Consumer does not have access to
    // GenerateDataKeyWithoutPlaintext on the terminal key.
    var newDecryptOnly :- CreateNewTerminalDecryptOnlyBranchKey(
      decryptOnlyEncryptionContext,
      MutationToApply,
      input.keyManagerStrategy
    );

    var ActiveEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(newDecryptOnly.EncryptionContext);

    var newActive :- ReEncryptHierarchicalKey(
      item := newDecryptOnly,
      originalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := ActiveEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );

    // -= Mutate Beacon Key
    var BeaconEncryptionContext := Structure.ReplaceMutableContext(
      readItems.BeaconItem.EncryptionContext,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    assert readItems.BeaconItem.KmsArn == MutationToApply.Original.kmsArn;

    var newBeaconKey :- ReEncryptHierarchicalKey(
      item := readItems.BeaconItem,
      originalKmsArn := MutationToApply.Original.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := BeaconEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy,
      localOperation := "InitializeMutation"
    );

    // -= Create Mutation Commitment & Mutation Index
    var MutationCommitment :- StateStrucs.SerializeMutationCommitment(MutationToApply);
    var MutationIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, None);

    // -= Apply System Key to Commitment & Mutation Index
    var SignedMutationCommitment :- SystemKeyHandler.SignCommitment(MutationCommitment, input.SystemKey);
    var SignedMutationIndex :- SystemKeyHandler.SignIndex(MutationIndex, input.SystemKey);

    // -= Write Mutation Commitment, new branch key version, mutated beacon key
    var throwAway2? := input.storage.WriteInitializeMutation(
      KeyStoreTypes.WriteInitializeMutationInput(
        Active := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newActive, Old:=activeItem),
        Version := KeyStoreTypes.WriteInitializeMutationVersion.rotate(rotate:=newDecryptOnly),
        Beacon := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newBeaconKey, Old:=readItems.BeaconItem),
        MutationCommitment :=  SignedMutationCommitment, // MutationCommitment,
        MutationIndex := SignedMutationIndex // MutationIndex
      ));
    // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Commitment get written?
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var mutatedBranchKeyItems := GetMutatedBranchKeyItems(mutationCommitmentUUID, newVersion);

    var Token := Types.MutationToken(
      Identifier := input.Identifier,
      UUID := mutationCommitmentUUID,
      CreateTime := timestamp);

    var Flag: Types.InitializeMutationFlag := Types.Created();

    return Success(Types.InitializeMutationOutput(
                     MutationToken := Token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));
  }

  function GetMutatedBranchKeyItems(mutationCommitmentUUID: seq<char>, newVersion: seq<char>)
    : (output: seq<Types.MutatedBranchKeyItem>)
  {
    [Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + mutationCommitmentUUID, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + mutationCommitmentUUID, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Active: " + newVersion, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Decrypt Only: " + newVersion, Description := "Created"),
     Types.MutatedBranchKeyItem(ItemType := "Beacon", Description := "Mutated")
    ]
  }

  method {:isolate_assertions} CreateNewTerminalDecryptOnlyBranchKey(
    decryptOnlyEncryptionContext: Structure.BranchKeyContext,
    mutationToApply: StateStrucs.MutationToApply,
    keyManagerStrategy: KmsUtils.keyManagerStrat
  )
    returns (res: Result<KeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires KmsArn.ValidKmsArn?(mutationToApply.Terminal.kmsArn)
    requires KMSKeystoreOperations.AttemptKmsOperation?(
               KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn), decryptOnlyEncryptionContext
             )
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(kms) => kms.kmsClient.Modifies
      case decryptEncrypt(kmsD, kmsE) => kmsD.kmsClient.Modifies + kmsE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
    ensures res.Success? ==>
              && Structure.BranchKeyContext?(res.value.EncryptionContext)
              && Structure.EncryptedHierarchicalKey?(res.value)
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
    }

    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
      encryptionContext := decryptOnlyEncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(mutationToApply.Terminal.kmsArn),
      grantTokens := grantTokens,
      kmsClient := kmsClient
    );
    var wrappedDecryptOnlyBranchKey :- wrappedDecryptOnlyBranchKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var newDecryptOnly := Structure.ConstructEncryptedHierarchicalKey(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );

    :- Need(
      Structure.BRANCH_KEY_TYPE_PREFIX < newDecryptOnly.EncryptionContext[Structure.TYPE_FIELD],
      Types.KeyStoreAdminException(message := "Invalid Branch Key prefix.")
    );

    return Success(newDecryptOnly);
  }

  // Ensures:
  //-= Mutations Token is valid
  //-= logicalKeyStoreName is valid
  //-= PageSize is valid
  function ValidateApplyMutationInput(
    input: InternalApplyMutationInput
  ): (output: Result<InternalApplyMutationInput, Types.Error>)
    ensures output.Success? ==>
              && |input.logicalKeyStoreName| > 0
              && ValidateMutationToken(input.MutationToken).Success?
              && input.PageSize.Some?
              ==>
                0 < input.PageSize.value
                && (
                  && (input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
                      && input.PageSize.Some?)
                  ==>
                    input.PageSize.value <= 99)
  {
    var _ :- ValidateMutationToken(input.MutationToken);
    :- Need(|input.logicalKeyStoreName| > 0,
            Types.KeyStoreAdminException(message := "LogicalKeyStoreName cannot be empty!"));
    :- Need(
         // If the Storage is DDB && a page Size was given
         (input.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface && input.PageSize.Some?)
         ==>
           // then the pageSize MUST be less than or equal to 99
           input.PageSize.value <= 99,
         Types.KeyStoreAdminException(message := "The DynamoDB Key Storage supports a max page size of 99"));
    :- Need(
         // If page Size was given then the pageSize MUST be greater than 0
         input.PageSize.Some? ==> 0 < input.PageSize.value,
         Types.KeyStoreAdminException(message := "The page size MUST be greater than 0."));
    Success(input)
  }

  // Ensures:
  // Branch Key ID is set
  function ValidateMutationToken(
    input: Types.MutationToken
  ): (output: Result<Types.MutationToken, Types.Error>)
    ensures output.Success?
            ==>
              && |input.Identifier| > 0
  {
    :- Need(|input.Identifier| > 0,
            Types.KeyStoreAdminException(message := "Mutation Token's Branch Key Identifier cannot be empty!"));
    Success(input)
  }

  datatype InternalApplyMutationInput = | InternalApplyMutationInput (
    nameonly MutationToken: Types.MutationToken ,
    nameonly PageSize: Option<StandardLibrary.UInt.int32> ,
    nameonly SystemKey: KmsUtils.InternalSystemKey ,
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
    }
  }

  method {:isolate_assertions} ApplyMutation(
    input: InternalApplyMutationInput
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires ValidateApplyMutationInput(input).Success?
    requires input.ValidState()
    ensures input.ValidState()
    modifies
      input.storage.Modifies,
            match input.keyManagerStrategy {
              case reEncrypt(km) => km.kmsClient.Modifies
              case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
            },
            input.SystemKey.Modifies
  {
    // -= Fetch Commitment and Index
    var storage := input.storage;
    var keyManagerStrategy := input.keyManagerStrategy;
    var SystemKey := input.SystemKey;
    // var logicalKeyStoreName := input.logicalKeyStoreName;
    var fetchMutation? := storage.GetMutation(
      Types.AwsCryptographyKeyStoreTypes.GetMutationInput(
        Identifier := input.MutationToken.Identifier));
    var fetchMutation: KeyStoreTypes.GetMutationOutput :- fetchMutation?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

      // -= Validate Commitment and Index
    :- Need(
      fetchMutation.MutationCommitment.Some?,
      Types.MutationInvalidException(
        message := "No Mutation is in-flight for this Branch Key ID " + input.MutationToken.Identifier + " ."
      ));
    :- Need(
      input.MutationToken.UUID == fetchMutation.MutationCommitment.value.UUID,
      Types.MutationInvalidException(
        message := "The Token and the Mutation Commitment read from storage disagree."
        + " This indicates that the Token is for a different Mutation than the one in-flight."
        + " A possible cause is this token is from an earlier Mutation that already finished?"
        + " Branch Key ID: " + input.MutationToken.Identifier + ";"
        + " Mutation Commitment UUID: " + fetchMutation.MutationCommitment.value.UUID + ";"
        + " Token UUID: " + input.MutationToken.UUID + ";"
      ));
    :- Need(
      fetchMutation.MutationIndex.Some?,
      Types.MutationInvalidException(
        message := "No Mutation Index exsists for this in-flight mutation of Branch Key ID " + input.MutationToken.Identifier + " ."
      ));
    var CommitmentAndIndex :- ValidateCommitmentAndIndexStructures(
      input.MutationToken,
      fetchMutation.MutationCommitment.value,
      fetchMutation.MutationIndex.value);

    var commitmentIsVerified :- SystemKeyHandler.VerifyCommitment(CommitmentAndIndex.Commitment, SystemKey);
    :- Need(
      commitmentIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Commitment's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));
    var indexIsVerified :- SystemKeyHandler.VerifyIndex(CommitmentAndIndex.Index, SystemKey);
    :- Need(
      indexIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Index's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));

    var MutationToApply :- StateStrucs.DeserializeMutation(CommitmentAndIndex);

    // -= Query for page Size Branch Key Items
    var queryOut :- QueryForVersionsAndValidate(input, MutationToApply);//logicalKeyStoreName, storage, MutationToApply);

    var queryOutItems := Seq.Map(
      item
      requires Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
      =>
        MatchItemToState(item, MutationToApply),
      queryOut.Items
    );

    var ItemNeither? := (item: CheckedItem) => item.itemNeither?;

    var neitherState? := Seq.Filter(ItemNeither?, queryOutItems);

    :- Need(
      |neitherState?| == 0
    , Types.UnexpectedStateException(
        message := if 0 < |neitherState?| then
          "Item(s) found in an unexpected state: "
          + Join(Seq.Map((i:CheckedItem) => i.item.Identifier, neitherState?), ",")
        else
          "Can't happen"
      ));

    FilterIsEmpty?(ItemNeither?, queryOutItems);
    var itemsToProcess: OriginalOrTerminal := queryOutItems;

    assert forall item <- itemsToProcess ::
        && item.item is KeyStoreTypes.EncryptedHierarchicalKey
        && Structure.EncryptedHierarchicalKey?(item.item)
        && item.item.Type.HierarchicalSymmetricVersion?
        && (item.itemOriginal? ==> item.item.KmsArn == MutationToApply.Original.kmsArn);

    // Process Branch Keys that need to be mutated
    var processedItems? :- ProcessBranchKeysInApplyMutation(itemsToProcess, keyManagerStrategy, MutationToApply);
    var itemsEvaluated := processedItems?.0;
    var logStatements := processedItems?.1;

      // Update Index
    :- Need(
      UTF8.ValidUTF8Seq(queryOut.ExclusiveStartKey),
      Types.KeyStoreAdminException(
        message:="ExclusiveStartKey returned by Key Store's Storage is not valid UTF-8 Byte Sequence."));
    var newIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, Some(queryOut.ExclusiveStartKey));
    var signedNewIndex :- SystemKeyHandler.SignIndex(newIndex, SystemKey);

    var _ :- WriteMutations(
      storage,
      itemsEvaluated,
      CommitmentAndIndex.Commitment,
      newIndex := signedNewIndex,
      oldIndex := CommitmentAndIndex.Index,
      endMutationBool := (|queryOut.ExclusiveStartKey| == 0)
    );

    var Token := Types.MutationToken(
      Identifier := MutationToApply.Identifier,
      UUID := MutationToApply.UUID,
      CreateTime := MutationToApply.CreateTime);

    output := Success(
      Types.ApplyMutationOutput(
        MutationResult :=
          if 0 < |queryOut.ExclusiveStartKey|
          then
            Types.ContinueMutation(Token)
          else
            Types.ApplyMutationResult.CompleteMutation(Types.MutationComplete()),
        MutatedBranchKeyItems := logStatements
      ));
  }

  method WriteMutations(
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface,
    itemsEvaluated: seq<KeyStoreTypes.OverWriteEncryptedHierarchicalKey>,
    commitment: KeyStoreTypes.MutationCommitment,
    nameonly newIndex: KeyStoreTypes.MutationIndex,
    nameonly oldIndex: KeyStoreTypes.MutationIndex,
    nameonly endMutationBool: bool
  ) returns (output: Result<(), Types.Error>)
    requires storage.ValidState()
    modifies storage.Modifies
    ensures storage.ValidState()
    ensures output.Success? ==>
              && |storage.History.WriteMutatedVersions| == |old(storage.History.WriteMutatedVersions)| + 1
              && Seq.Last(storage.History.WriteMutatedVersions).output.Success?
              && var input := Seq.Last(storage.History.WriteMutatedVersions).input;
              && KeyStoreTypes.WriteMutatedVersionsInput(
                Items := itemsEvaluated,
                MutationCommitment := commitment,
                MutationIndex := KeyStoreTypes.OverWriteMutationIndex(Index:=newIndex, Old:=oldIndex),
                EndMutation := endMutationBool
              ) == input
  {
    // Add conditional check on Mutation Commitment & Mutation Token agreement to Write Request
    var writeReq := KeyStoreTypes.WriteMutatedVersionsInput(
      Items := itemsEvaluated,
      MutationCommitment := commitment,
      MutationIndex := KeyStoreTypes.OverWriteMutationIndex(Index:=newIndex, Old:=oldIndex),
      EndMutation := endMutationBool
    );

    // -= write to storage ;; MUST write to storage to ensure Terminal in M-Commitment and M-Token agree
    var throwAway2? := storage.WriteMutatedVersions(writeReq);
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    return Success(());
  }


  method ValidateCommitmentAndIndexStructures(
    token: Types.MutationToken,
    commitment: KeyStoreTypes.MutationCommitment,
    index: KeyStoreTypes.MutationIndex
  )
    returns (output: Result<StateStrucs.CommitmentAndIndex, Types.Error>)
    ensures
      output.Success? ==>
        && commitment.Identifier == index.Identifier == token.Identifier
        && commitment.UUID == index.UUID == token.UUID
    ensures
      && output.Success?
      ==>
        && output.value.ValidState()
        && output.value.ValidUTF8()

  {
    if (commitment.Identifier != index.Identifier || token.Identifier != index.Identifier) {
      return
        Failure(Types.MutationInvalidException(
                  message := "The Token and the Mutation Commitment read from storage disagree."
                  + " This indicates that the Token is for a different Mutation than the one in-flight."
                  + " A possible cause is this token is from an earlier Mutation that already finished?"
                  + " Branch Key ID: " + token.Identifier + ";"
                  + " Mutation Commitment UUID: " + commitment.UUID + ";"
                  + " Token UUID: " + token.UUID + ";"
                ));
    }
    if (commitment.UUID != index.UUID || token.UUID != index.UUID) {
      return
        Failure(Types.MutationInvalidException(
                  message := "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
                  + " Branch Key ID: " + token.Identifier + ";"
                  + " Mutation Commitment UUID: " + commitment.UUID + ";"
                  + " Mutation Index UUID: " + index.UUID + ";"
                ));
    }
    var commitmentAndIndex := StateStrucs.CommitmentAndIndex(commitment, index);
    if (!commitmentAndIndex.ValidUTF8()) {
      return Failure(
          Types.MutationInvalidException(
            message :=
              "The Mutation Commitment and Mutation Index read from storage do not contain valid UTF8 sequences."
              + " Branch Key ID: " + token.Identifier + ";"
              + " Mutation Commitment UUID: " + commitment.UUID + ";"));
    }
    return Success(commitmentAndIndex);
  }

  method QueryForVersionsAndValidate(
    input: InternalApplyMutationInput,
    mutationToApply: StateStrucs.MutationToApply
  ) returns (output: Result<KeyStoreTypes.QueryForVersionsOutput, Types.Error>)
    requires input.ValidState()
    modifies input.storage.Modifies
    ensures input.ValidState()
    ensures output.Success? ==>
              && |input.storage.History.QueryForVersions| == |old(input.storage.History.QueryForVersions)| + 1
              && Seq.Last(input.storage.History.QueryForVersions).output.Success?
              && var queryOutInput := Seq.Last(input.storage.History.QueryForVersions).input;
              && KeyStoreTypes.QueryForVersionsInput(
                ExclusiveStartKey := mutationToApply.ExclusiveStartKey,
                Identifier := mutationToApply.Identifier,
                PageSize := input.PageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)
              ) == queryOutInput
    ensures output.Success? ==>
              && Seq.Last(input.storage.History.QueryForVersions).output.Success?
              && var queryOutOutput := Seq.Last(input.storage.History.QueryForVersions).output.value;
              && output.value == queryOutOutput
              && ValidateQueryOutResults?(input, output.value)
              && forall item <- output.value.Items :: Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
                                                      && forall item <- output.value.Items :: item.Type.HierarchicalSymmetricVersion?
  {
    var queryOut? := input.storage.QueryForVersions(
      Types.AwsCryptographyKeyStoreTypes.QueryForVersionsInput(
        ExclusiveStartKey := mutationToApply.ExclusiveStartKey,
        Identifier := mutationToApply.Identifier,
        PageSize := input.PageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)));

    var queryOut :- queryOut?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    :- Need(
      ValidateQueryOutResults?(input, queryOut),
      // TODO-Mutations-FF: Replace this Need with something that can return an ID
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

    return Success(queryOut);
  }

  method {:isolate_assertions} ProcessBranchKeysInApplyMutation(
    items: OriginalOrTerminal,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    mutationToApply: StateStrucs.MutationToApply
  ) returns (output: Result<(seq<KeyStoreTypes.OverWriteEncryptedHierarchicalKey>, seq<Types.MutatedBranchKeyItem>), Types.Error>)
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
    requires forall item <- items :: item.item is KeyStoreTypes.EncryptedHierarchicalKey
    requires forall item <- items :: item.item.Type.HierarchicalSymmetricVersion?
    requires forall item <- items :: KmsArn.ValidKmsArn?(item.item.KmsArn)
    requires forall item <- items :: Structure.EncryptedHierarchicalKey?(item.item)
    requires forall item <- items :: item.itemOriginal? ==> item.item.KmsArn == mutationToApply.Original.kmsArn
    requires Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! mutationToApply.Terminal.customEncryptionContext.Keys
  {
    var logStatements: seq<Types.MutatedBranchKeyItem> := [];
    var itemsEvaluated := [];

    for versionIndex := 0 to |items|
    {
      var item := items[versionIndex];
      match item {
        case itemTerminal(item) =>
          var verify? := VerifyEncryptedHierarchicalKey(
            item := item,
            keyManagerStrategy := keyManagerStrategy
          );
          if (verify?.Fail?) {
            return Failure(verify?.error);
          }
          logStatements := logStatements
          + [Types.MutatedBranchKeyItem(
               ItemType := "Version (Decrypt Only): " + item.Type.HierarchicalSymmetricVersion.Version,
               Description := " Validated in Terminal")];
        // if item is original, mutate with Failure
        case itemOriginal(item) =>
          var terminalEncryptionContext := Structure.ReplaceMutableContext(
            item.EncryptionContext,
            mutationToApply.Terminal.kmsArn,
            mutationToApply.Terminal.customEncryptionContext
          );

          var mutatedItem :- ReEncryptHierarchicalKey(
            item := item,
            originalKmsArn := mutationToApply.Original.kmsArn,
            terminalKmsArn := mutationToApply.Terminal.kmsArn,
            terminalEncryptionContext := terminalEncryptionContext,
            keyManagerStrategy := keyManagerStrategy
          );
          itemsEvaluated := itemsEvaluated + [
            KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=mutatedItem, Old:=item)
          ];
          logStatements := logStatements
          + [Types.MutatedBranchKeyItem(
               ItemType := "Decrypt Only: " + item.Type.HierarchicalSymmetricVersion.Version,
               Description := " Mutated to Terminal")];
      }
    }
    return Success((itemsEvaluated, logStatements));
  }

  lemma OriginalOrTerminalIsEncryptedHierarchicalKey?(items: OriginalOrTerminal)
    ensures forall item <- items ::
              && (item.itemOriginal? || item.itemTerminal?)
              && item.item is KeyStoreTypes.EncryptedHierarchicalKey
  {}


  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
  ): (output: CheckedItem)
    requires item.Type.HierarchicalSymmetricVersion?
    requires Structure.EncryptedHierarchicalKey?(item)
    requires MutationToApply.ValidState()
    ensures Structure.EncryptedHierarchicalKey?(output.item)
    ensures
      && output.itemOriginal?
      ==>
        && output.item.KmsArn == MutationToApply.Original.kmsArn
    ensures output.item.Type.HierarchicalSymmetricVersion?
  {
    if item.EncryptionContext
       == Structure.ReplaceMutableContext(
            item.EncryptionContext,
            MutationToApply.Original.kmsArn,
            MutationToApply.Original.customEncryptionContext
          ) then
      itemOriginal(item)
    else if item.EncryptionContext
            == Structure.ReplaceMutableContext(
                 item.EncryptionContext,
                 MutationToApply.Terminal.kmsArn,
                 MutationToApply.Terminal.customEncryptionContext
               ) then
      itemTerminal(item)
    else
      itemNeither(item)
  }


  method {:isolate_assertions} VerifyEncryptedHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "ApplyMutation"
  )
    returns (output: Outcome<Types.Error>)

    requires Structure.EncryptedHierarchicalKey?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    requires item.Type.ActiveHierarchicalSymmetricVersion? || item.Type.HierarchicalSymmetricVersion?
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var kmsOperation: string;
    var success?: bool := false;
    var throwAwayError;

    match keyManagerStrategy {
      case reEncrypt(kms) =>
        kmsOperation := "ReEncrypt";
        var throwAway? := KMSKeystoreOperations.ReEncryptKey(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := item.EncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );

        if throwAway?.Success? {
          success? := true;
        } else {
          throwAwayError := throwAway?.error;
        }

      case decryptEncrypt(kmsD, kmsE) =>
        kmsOperation := "Decrypt/Encrypt";
        var throwAway? := KMSKeystoreOperations.VerifyViaDecryptEncryptKey(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := item.EncryptionContext,
          kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
          decryptGrantTokens := kmsD.grantTokens,
          decryptKmsClient := kmsD.kmsClient
        );

        if throwAway?.Success? {
          success? := true;
        } else {
          throwAwayError := throwAway?.error;
        }
    }

    if (
        && !success?
        && item.Type.ActiveHierarchicalSymmetricVersion?
      ) {
      var error := MutationErrorRefinement.VerifyActiveException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Fail(error);
    }

    if (
        && !success?
        && item.Type.HierarchicalSymmetricVersion?
      ) {
      var error := MutationErrorRefinement.VerifyTerminalException(
        branchKeyItem := item,
        error := throwAwayError,
        localOperation := localOperation,
        kmsOperation := kmsOperation);
      return Fail(error);
    }

    assert success?;
    return Pass;
  }

  method {:isolate_assertions} ReEncryptHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly originalKmsArn: string,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly localOperation: string := "ApplyMutation"
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires KMS.IsValid_KeyIdType(terminalKmsArn)
    requires KMSKeystoreOperations.AttemptReEncrypt?(item.EncryptionContext, terminalEncryptionContext)
    requires KmsArn.ValidKmsArn?(originalKmsArn) && KmsArn.ValidKmsArn?(terminalKmsArn)
    requires item.KmsArn == originalKmsArn
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var wrappedKey?;
    match keyManagerStrategy {
      case reEncrypt(kms) =>
        wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
          ciphertext := item.CiphertextBlob,
          sourceEncryptionContext := item.EncryptionContext,
          destinationEncryptionContext := terminalEncryptionContext,
          sourceKmsArn := originalKmsArn,
          destinationKmsArn := terminalKmsArn,
          grantTokens := kms.grantTokens,
          kmsClient := kms.kmsClient
        );
      case decryptEncrypt(kmsD, kmsE) =>
        if (localOperation == "InitializeMutation") {
          // When using the decrypt encrypt strategy, we created the new DecryptOnly with the encrypt client.
          // If we want to reencrypt it for the new active we must do so with only the encrypt client. This means
          // that the encrypt client will perform both the decrypt and encrypt operations. Otherwise we assume that
          // the decrypt client has permissions to decrypt the kms key that we are moving to. This is a wrong assumption.
          wrappedKey? := KMSKeystoreOperations.MutateViaDecryptEncryptOnInitializeMutation(
            ciphertext := item.CiphertextBlob,
            sourceEncryptionContext := item.EncryptionContext,
            destinationEncryptionContext := terminalEncryptionContext,
            sourceKmsArn := originalKmsArn,
            destinationKmsArn := terminalKmsArn,
            grantTokens := kmsE.grantTokens,
            kmsClient := kmsE.kmsClient
          );
        } else {
          wrappedKey? := KMSKeystoreOperations.MutateViaDecryptEncrypt(
            ciphertext := item.CiphertextBlob,
            sourceEncryptionContext := item.EncryptionContext,
            destinationEncryptionContext := terminalEncryptionContext,
            sourceKmsArn := originalKmsArn,
            destinationKmsArn := terminalKmsArn,
            decryptGrantTokens := kmsD.grantTokens,
            decryptKmsClient := kmsD.kmsClient,
            encryptGrantTokens := kmsE.grantTokens,
            encryptKmsClient := kmsE.kmsClient
          );
        }
    }

    // We call this method to create the new Active from the new Decrypt Only
    if (wrappedKey?.Failure? && item.Type.ActiveHierarchicalSymmetricVersion?) {
      var error := MutationErrorRefinement.CreateActiveException(
        branchKeyItem := item,
        error := wrappedKey?.error,
        localOperation := localOperation);
      return Failure(error);
    }
    // We call this method to mutate decryptOnly and the Becon
    if (
        && wrappedKey?.Failure?
        && (item.Type.HierarchicalSymmetricVersion? || item.Type.ActiveHierarchicalSymmetricBeacon?)) {
      var error := MutationErrorRefinement.MutateExceptionParse(
        item := item,
        error := wrappedKey?.error,
        terminalKmsArn := terminalKmsArn,
        localOperation := localOperation);
      return Failure(error);
    }
    // TODO-Mutations-DoNotVersion :: ActiveHierarchicalSymmetricVersion will need to be handled

    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalEncryptionContext,
                        wrappedKey?.value
                      ));
  }


  lemma FilterIsEmpty?<T>(f: (T ~> bool), xs: seq<T>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    ensures forall i | 0 <= i < |xs| :: f(xs[i]) ==> xs[i] in Seq.Filter(f, xs)
    ensures |Seq.Filter(f, xs)| == 0 ==> forall i | 0 <= i < |xs| :: !f(xs[i])
  {
    reveal Seq.Filter();
  }

  function CommitmentAndInputMatch(
    nameonly internalInput: InternalInitializeMutationInput,
    nameonly commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<bool, Types.Error>)
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
    nameonly SystemKey: KmsUtils.InternalSystemKey
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires storage.ValidState() && SystemKey.ValidState()
    ensures storage.ValidState() && SystemKey.ValidState()
    modifies storage.Modifies, SystemKey.Modifies
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
    var commitmentIsVerified :- SystemKeyHandler.VerifyCommitment(commitment, SystemKey);
    :- Need(
      commitmentIsVerified,
      Types.MutationVerificationException(
        message:=
          "Mutation Commitment's failed the System Key's Signature Verification."
          + " This suggests the Key Store's Storage has been tampered with by an un-authorized actor."
          + " Mutation cannot continue. Audit Key Store's Storage's access."
          + " The Mutation will need to be manually restarted."));
    var Token := Types.MutationToken(
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
      var SignedMutationIndex :- SystemKeyHandler.SignIndex(newIndex, SystemKey);
      // -= Write Mutation Index, conditioned on Mutation Commitment
      var throwAway2? := storage.WriteMutationIndex(
        KeyStoreTypes.WriteMutationIndexInput(
          MutationCommitment := commitment,
          MutationIndex := SignedMutationIndex
        ));
      // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
      // What Condition Check failed?
      var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
      mutatedBranchKeyItems := mutatedBranchKeyItems
      + [Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + commitment.UUID, Description := "Created")];
    } else {
      var commitmentAndIndex :- ValidateCommitmentAndIndexStructures(
        Token,
        commitment,
        index.value);
      var indexIsVerified :- SystemKeyHandler.VerifyIndex(commitmentAndIndex.Index, SystemKey);
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
                     MutationToken := Token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));

  }
}
