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
    nameonly SystemKey: Types.SystemKey ,
    nameonly DoNotVersion: bool,
    nameonly logicalKeyStoreName: string,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )

  // Ensures:
  // Branch Key ID is set
  // Mutations List is valid
  // logicalKeyStoreName is valid
  function {:vcs_split_on_every_assert} ValidateInitializeMutationInput(
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
    ensures
      && output.Success?
      ==>
        input.SystemKey.trustStorage?
  {
    :- Need(
         input.DoNotVersion == false,
         Types.UnsupportedFeatureException(message := "At this time, DoNotVersion MUST be false.")
       );
    :- Need(
         input.SystemKey.trustStorage?,
         Types.UnsupportedFeatureException(message := "At this time, SystemKey MUST be TrustStorage.")
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

  method {:vcs_split_on_every_assert} InitializeMutation(
    input: InternalInitializeMutationInput
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires ValidateInitializeMutationInput(input).Success?
    requires StateStrucs.ValidMutations?(input.Mutations) // may not need this
    requires input.storage.ValidState() &&
             match input.keyManagerStrategy
             case reEncrypt(km) => km.kmsClient.ValidState() && AwsKmsUtils.GetValidGrantTokens(Some(km.grantTokens)).Success?
             case decryptEncrypt(kmD, kmE) =>
               && kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
               && AwsKmsUtils.GetValidGrantTokens(Some(kmD.grantTokens)).Success?
               && AwsKmsUtils.GetValidGrantTokens(Some(kmE.grantTokens)).Success?
    ensures input.storage.ValidState() &&
            match input.keyManagerStrategy
            case reEncrypt(km) => km.kmsClient.ValidState()
            case decryptEncrypt(kmD, kmE) => kmD.kmsClient.ValidState() && kmE.kmsClient.ValidState()
    modifies
      input.storage.Modifies,
            match input.keyManagerStrategy
            case reEncrypt(km) => km.kmsClient.Modifies
            case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    requires input.keyManagerStrategy.reEncrypt?
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
            + " The Key Store's Storage has become corrupted."
            + " Recommend auditing the Branch Key's items for tampering."
            + " Recommend auditing access to the storage."
            + " To successfully start a new mutation, delete the Mutation Index."
            + " But know that the new mutation will fail if any corrupt items are encountered."
            + " Branch Key ID: " + input.Identifier
            + " \tMutation Index UUID: " + indexUUID));
    }

    if (readItems.MutationCommitment.Some?) {
      resumeMutation? :- CommitmentAndInputMatch(
        internalInput := input,
        commitment := readItems.MutationCommitment.value);
      if (resumeMutation?) {
        output := ResumeMutation(
          commitment := readItems.MutationCommitment.value,
          index := readItems.MutationIndex,
          logicalKeyStoreName := input.logicalKeyStoreName,
          storage := input.storage);
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
    // -= BEGIN Version Active Branch Key
    // --= Validate Active Branch Key
    var verifyActive? := VerifyEncryptedHierarchicalKey(
      item := activeItem,
      keyManagerStrategy := input.keyManagerStrategy
    );
    if (verifyActive?.Fail?) {
      return Failure(
          MutationErrorRefinement.VerifyActiveException(
            branchKeyItem := activeItem,
            error := verifyActive?.error));
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
    var wrappedDecryptOnlyBranchKey? := KMSKeystoreOperations.GenerateKey(
      encryptionContext := decryptOnlyEncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(MutationToApply.Terminal.kmsArn),
      grantTokens := input.keyManagerStrategy.reEncrypt.grantTokens,
      kmsClient := input.keyManagerStrategy.reEncrypt.kmsClient
    );
    var wrappedDecryptOnlyBranchKey :- wrappedDecryptOnlyBranchKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
    var newDecryptOnly := Structure.ConstructEncryptedHierarchicalKey(
      decryptOnlyEncryptionContext,
      wrappedDecryptOnlyBranchKey.CiphertextBlob.value
    );

    var ActiveEncryptionContext := Structure.ActiveBranchKeyEncryptionContext(newDecryptOnly.EncryptionContext);
    var newActive :- ReEncryptHierarchicalKey(
      item := newDecryptOnly,
      originalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := ActiveEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy
    );

    // -= Mutate Beacon Key
    var BeaconEncryptionContext := Structure.ReplaceMutableContext(
      readItems.BeaconItem.EncryptionContext,
      MutationToApply.Terminal.kmsArn,
      MutationToApply.Terminal.customEncryptionContext
    );

    assert readItems.BeaconItem.KmsArn == MutationToApply.Original.kmsArn;
    // TODO-Mutations-GA? :: If the KMS Call fails with access denied,
    // there are several possible causes.
    // 1. `ReEncryptFrom` :: ReEncrypt access to Original is denied
    // 2. `ReEncryptTo` :: ReEncrypt access to Terminal is denied
    var newBeaconKey :- ReEncryptHierarchicalKey(
      item := readItems.BeaconItem,
      originalKmsArn := MutationToApply.Original.kmsArn,
      terminalKmsArn := MutationToApply.Terminal.kmsArn,
      terminalEncryptionContext := BeaconEncryptionContext,
      keyManagerStrategy := input.keyManagerStrategy
    );

    // -= Create Mutation Commitment
    var MutationCommitment :- StateStrucs.SerializeMutationCommitment(MutationToApply);
    // TODO-Mutations-GA :: If resuming a mutation, we will need to serialize the read pageIndex
    var MutationIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, None);

    // -= Write Mutation Commitment, new branch key version, mutated beacon key
    var throwAway2? := input.storage.WriteInitializeMutation(
      KeyStoreTypes.WriteInitializeMutationInput(
        Active := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newActive, Old:=activeItem),
        Version := KeyStoreTypes.WriteInitializeMutationVersion.rotate(rotate:=newDecryptOnly),
        Beacon := KeyStoreTypes.OverWriteEncryptedHierarchicalKey(Item:=newBeaconKey, Old:=readItems.BeaconItem),
        MutationCommitment := MutationCommitment,
        MutationIndex := MutationIndex
      ));
    // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
    // What Condition Check failed? Was the Key Versioned? Or did another M-Commitment get written?
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    var mutatedBranchKeyItems := [
      Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + mutationCommitmentUUID, Description := "Created"),
      Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + mutationCommitmentUUID, Description := "Created"),
      Types.MutatedBranchKeyItem(ItemType := "Active: " + newVersion, Description := "Created"),
      Types.MutatedBranchKeyItem(ItemType := "Decrypt Only: " + newVersion, Description := "Created"),
      Types.MutatedBranchKeyItem(ItemType := "Beacon", Description := "Mutated")
    ];

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

  // Ensures:
  // Mutations Token is valid
  // logicalKeyStoreName is valid
  function ValidateApplyMutationInput(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string,
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  ): (output: Result<Types.ApplyMutationInput, Types.Error>)
    ensures output.Success? ==>
              && |logicalKeyStoreName| > 0
              && ValidateMutationToken(input.MutationToken).Success?
              && input.PageSize.Some?
              ==>
                0 < input.PageSize.value
                && (
                  && (storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
                      && input.PageSize.Some?)
                  ==>
                    input.PageSize.value <= 99)
  {
    var _ :- ValidateMutationToken(input.MutationToken);
    :- Need(|logicalKeyStoreName| > 0,
            Types.KeyStoreAdminException(message := "LogicalKeyStoreName cannot be empty!"));
    :- Need(
         // If the Storage is DDB && a page Size was given
         (storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface && input.PageSize.Some?)
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

  method {:vcs_split_on_every_assert} ApplyMutation(
    input: Types.ApplyMutationInput,
    logicalKeyStoreName: string,
    keyManagerStrategy: KmsUtils.keyManagerStrat,
    storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
    returns (output: Result<Types.ApplyMutationOutput, Types.Error>)
    requires ValidateApplyMutationInput(input, logicalKeyStoreName, storage).Success?
    requires
      && storage.ValidState()
      && keyManagerStrategy.ValidState()
    ensures
      && storage.ValidState()
      && keyManagerStrategy.ValidState()
    modifies
      storage.Modifies,
             match keyManagerStrategy
             case reEncrypt(km) => km.kmsClient.Modifies
             case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    requires keyManagerStrategy.reEncrypt?
  {
    var keyManager := keyManagerStrategy.reEncrypt;

    // -= Fetch Commitment and Index
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
    var Commitment := fetchMutation.MutationCommitment.value;
    var Index := fetchMutation.MutationIndex.value;
    :- Need(
      // If custom storage is really bad
      Commitment.Identifier == Index.Identifier,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Branch Key IDs."
        + " The Storage implementation is wrong, or something terrible has happened to storage."
        + " Token Branch Key ID: " + input.MutationToken.Identifier + ";"
        + " Mutation Commitment Branch Key ID: " + Commitment.Identifier + ";"
        + " Mutation Index Branch Key ID: " + Index.Identifier + ";"
      ));
    :- Need(
      Commitment.UUID == Index.UUID,
      Types.MutationInvalidException(
        message := "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
        + " Branch Key ID: " + input.MutationToken.Identifier + ";"
        + " Mutation Commitment UUID: " + Commitment.UUID + ";"
        + " Mutation Index UUID: " + Index.UUID + ";"
      ));
    var CommitmentAndIndex := StateStrucs.CommitmentAndIndex(
      Commitment := Commitment,
      Index := Index);
    assert CommitmentAndIndex.ValidState();
    // TODO-Mutations-GA :: Use System Key to Verify Commitment and Index
    var MutationToApply :- StateStrucs.DeserializeMutation(CommitmentAndIndex);

    // -= Query for page Size Branch Key Items
    var queryOut? := storage.QueryForVersions(
      Types.AwsCryptographyKeyStoreTypes.QueryForVersionsInput(
        ExclusiveStartKey := MutationToApply.ExclusiveStartKey,
        Identifier := MutationToApply.Identifier,
        PageSize := input.PageSize.UnwrapOr(DEFAULT_APPLY_PAGE_SIZE)));

    var queryOut :- queryOut?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    :- Need(
      || storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
      || (
           forall item <- queryOut.Items ::
             && item.Identifier == input.MutationToken.Identifier
             && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
             && item.Type.HierarchicalSymmetricVersion?
             && item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
         ),
      // TODO-Mutations-FF: Replace this Need with something that can return an ID
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

      // TODO-Mutations-FF: Replace this Need with something that can return an ID
    :- Need(
      forall item <- queryOut.Items :: KmsArn.ValidKmsArn?(item.KmsArn),
      Types.KeyStoreAdminException(
        message := "Malformed Branch Key Item read from Storage.")
    );

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

    var logStatements: seq<Types.MutatedBranchKeyItem> := [];
    var itemsEvaluated := [];
    for versionIndex := 0 to |itemsToProcess|
      // invariant forall item <- itemsToProcess :: item.itemTerminal? || item.itemOriginal?
    {
      var item := itemsToProcess[versionIndex];
      match item {
        case itemTerminal(item) =>
          var verify? := VerifyEncryptedHierarchicalKey(
            item := item,
            keyManagerStrategy:= keyManagerStrategy
          );
          if (verify?.Fail?) {
            return Failure(
                MutationErrorRefinement.VerifyTerminalException(
                  branchKeyItem := item,
                  error := verify?.error));
          }
          logStatements := logStatements
          + [Types.MutatedBranchKeyItem(
               ItemType := "Version (Decrypt Only): " + item.Type.HierarchicalSymmetricVersion.Version,
               Description := " Validated in Terminal")];
        // if item is original, mutate with Failure
        case itemOriginal(item) =>

          var terminalEncryptionContext := Structure.ReplaceMutableContext(
            item.EncryptionContext,
            MutationToApply.Terminal.kmsArn,
            MutationToApply.Terminal.customEncryptionContext
          );

          // TODO-Mutations-GA? :: If the KMS Call fails with access denied,
          // there are several possible causes.
          // 1. `ReEncryptFrom` :: ReEncrypt access to Original is denied
          // 2. `ReEncryptTo` :: ReEncrypt access to Terminal is denied
          var mutatedItem :- ReEncryptHierarchicalKey(
            item := item,
            originalKmsArn := MutationToApply.Original.kmsArn,
            terminalKmsArn := MutationToApply.Terminal.kmsArn,
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

    // Update Index
    var newIndex :- StateStrucs.SerializeMutationIndex(MutationToApply, Some(queryOut.ExclusiveStartKey));
    // Add conditional check on Mutation Commitment & Mutation Token agreement to Write Request
    var writeReq := KeyStoreTypes.WriteMutatedVersionsInput(
      Items := itemsEvaluated,
      MutationCommitment := Commitment,
      MutationIndex := KeyStoreTypes.OverWriteMutationIndex(Index:=newIndex, Old:=Index),
      EndMutation := (|queryOut.ExclusiveStartKey| == 0)
    );

    // -= write to storage ;; MUST write to storage to ensure Terminal in M-Commitment and M-Token agree
    var throwAway2? := storage.WriteMutatedVersions(writeReq);
    var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

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


  function MatchItemToState(
    item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    MutationToApply: StateStrucs.MutationToApply
  ): (output: CheckedItem)
    requires Structure.EncryptedHierarchicalKey?(item)
    requires StateStrucs.MutationToApply?(MutationToApply)
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


  method VerifyEncryptedHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat
  )
    returns (output: Outcome<KMSKeystoreOperations.KmsError>)
    requires keyManagerStrategy.reEncrypt?

    requires Structure.EncryptedHierarchicalKey?(item)
    requires KmsArn.ValidKmsArn?(item.KmsArn)
    requires keyManagerStrategy.ValidState()
    modifies
      match keyManagerStrategy
      case reEncrypt(km) => km.kmsClient.Modifies
      case decryptEncrypt(kmD, kmE) => kmD.kmsClient.Modifies + kmE.kmsClient.Modifies
    ensures keyManagerStrategy.ValidState()
  {
    var throwAway? := KMSKeystoreOperations.ReEncryptKey(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := item.EncryptionContext,
      kmsConfiguration := KeyStoreTypes.kmsKeyArn(item.KmsArn),
      grantTokens := keyManagerStrategy.reEncrypt.grantTokens,
      kmsClient := keyManagerStrategy.reEncrypt.kmsClient
    );

    output := if throwAway?.Success? then
      Pass
    else
      Fail(throwAway?.error);
  }

  method {:isolate_assertions} ReEncryptHierarchicalKey(
    nameonly item: Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey,
    nameonly originalKmsArn: string,
    nameonly terminalKmsArn: string,
    nameonly terminalEncryptionContext: Structure.BranchKeyContext,
    nameonly keyManagerStrategy: KmsUtils.keyManagerStrat
  )
    returns (output: Result<Types.AwsCryptographyKeyStoreTypes.EncryptedHierarchicalKey, Types.Error>)
    requires keyManagerStrategy.reEncrypt?
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
    var wrappedKey? := KMSKeystoreOperations.MutateViaReEncrypt(
      ciphertext := item.CiphertextBlob,
      sourceEncryptionContext := item.EncryptionContext,
      destinationEncryptionContext := terminalEncryptionContext,
      sourceKmsArn := originalKmsArn,
      destinationKmsArn := terminalKmsArn,
      grantTokens := keyManagerStrategy.reEncrypt.grantTokens,
      kmsClient := keyManagerStrategy.reEncrypt.kmsClient
    );

    var wrappedKey :- wrappedKey?
    .MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));

    output := Success(Structure.ConstructEncryptedHierarchicalKey(
                        terminalEncryptionContext,
                        wrappedKey.CiphertextBlob.value
                      ));
  }

  lemma FilterIsEmpty?<T>(f: (T ~> bool), xs: seq<T>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    ensures forall i | 0 <= i < |xs| :: f(xs[i]) ==> xs[i] in Seq.Filter(f, xs)
    ensures |Seq.Filter(f, xs)| == 0 ==> forall i | 0 <= i < |xs| :: !f(xs[i])
  {
    reveal Seq.Filter();
  }

  // Note: Assumes the System Key has already verified
  function CommitmentAndInputMatch(
    nameonly internalInput: InternalInitializeMutationInput,
    nameonly commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<bool, Types.Error>)
  {
    var readMutations :- StateStrucs.DeserializeMutationInput(commitment);
    var givenMutations := internalInput.Mutations;
    Success(readMutations == givenMutations)
  }


  method {:vcs_split_on_every_assert} ResumeMutation(
    nameonly commitment: KeyStoreTypes.MutationCommitment,
    nameonly index: Option<KeyStoreTypes.MutationIndex>,
    nameonly logicalKeyStoreName: string,
    nameonly storage: Types.AwsCryptographyKeyStoreTypes.IKeyStorageInterface
  )
    returns (output: Result<Types.InitializeMutationOutput, Types.Error>)
    requires storage.ValidState()
    ensures storage.ValidState()
    modifies storage.Modifies
    ensures
      output.Success? && index.Some?
      ==>
        index.value.UUID == commitment.UUID
  {
    var mutatedBranchKeyItems := [
      Types.MutatedBranchKeyItem(ItemType := "Mutation Commitment: " + commitment.UUID, Description := "Matched Input")
    ];
    var Flag: Types.InitializeMutationFlag := Types.Resumed();

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
        CiphertextBlob := [0] // TODO-Mutations-GA System Key
      );
      // -= Write Mutation Index, conditioned on Mutation Commitment
      var throwAway2? := storage.WriteMutationIndex(
        KeyStoreTypes.WriteMutationIndexInput(
          MutationCommitment := commitment,
          MutationIndex := newIndex
        ));
      // TODO-Mutations-FF :: Ideally, we would diagnosis the Storage Failure.
      // What Condition Check failed?
      var _ :- throwAway2?.MapFailure(e => Types.Error.AwsCryptographyKeyStore(e));
      mutatedBranchKeyItems := mutatedBranchKeyItems
      + [Types.MutatedBranchKeyItem(ItemType := "Mutation Index: " + commitment.UUID, Description := "Created")];
    } else {
      :- Need(
        index.value.UUID == commitment.UUID,
        Types.MutationInvalidException(
          message := M_ErrorMessages.COMMITMENT_INDEX_UUID_DISAGREE
          + " Branch Key ID: " + commitment.Identifier + ";"
          + " Mutation Commitment UUID: " + commitment.UUID + ";"
          + " Mutation Index UUID: " + index.value.UUID + ";")
      );
      assert index.value.UUID == commitment.UUID;
    }

    var Token := Types.MutationToken(
      Identifier := commitment.Identifier,
      UUID := commitment.UUID,
      CreateTime := commitment.CreateTime);

    return Success(Types.InitializeMutationOutput(
                     MutationToken := Token,
                     MutatedBranchKeyItems := mutatedBranchKeyItems,
                     InitializeMutationFlag := Flag));

  }
}