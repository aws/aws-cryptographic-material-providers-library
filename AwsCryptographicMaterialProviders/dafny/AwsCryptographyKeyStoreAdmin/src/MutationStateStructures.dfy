// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../../../libraries/src/Collections/Sets/Sets.dfy"
include "../../../../libraries/src/Collections/Maps/Maps.dfy"
include "../../../../libraries/src/JSON/API.dfy"
include "../../../../libraries/src/JSON/Errors.dfy"
include "../../../../libraries/src/JSON/Values.dfy"
include "MutationIndexUtils.dfy"

/** Mutation State Structures describe the Mutable Branch Key Properties that can be changed by Mutaiton. **/
/** Methods here normialize these descriptions so they may be compared. **/
module {:options "/functionSyntax:4" } MutationStateStructures {
  import opened StandardLibrary
  import opened StandardLibrary.UInt
  import opened Wrappers
  import opened Seq
  import UTF8
  import String = StandardLibrary.String
  import Sets
  import Maps
  import SortedSets

  import ErrorMessages = KeyStoreErrorMessages
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = KeyStoreOperations.Types
  import KmsArn
  import Structure

  import JSON = JSON.API
  import JSONErrors = JSON.Errors
  import JSONValues = JSON.Values
  import MutationIndexUtils

  const MUTABLE_PROPERTY_COUNT: int := 2
  const MUTABLE_PROPERTY_COUNT_str := "2"
  const AWS_CRYPTO_EC := Structure.AWS_CRYPTO_EC
  const KMS_FIELD := Structure.KMS_FIELD
  // Ensures
  // - if KMS ARN, Valid KMS ARN
  // - if EC, Valid non-empty EC, & not restricted field names
  // - non-empty
  predicate ValidMutations?(
    input: Types.Mutations
  )
  {
    && (input.TerminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.TerminalKmsArn.value))
    && (input.TerminalEncryptionContext.Some? ==>
          && |input.TerminalEncryptionContext.value| > 0
          &&  forall k <- input.TerminalEncryptionContext.value ::
               && |k| > 0 && |input.TerminalEncryptionContext.value[k]| > 0
               && input.TerminalEncryptionContext.value.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES)
    && !(input.TerminalKmsArn.None? && input.TerminalEncryptionContext.None?)
  }

  datatype MutableProperties = | MutableProperties (
    nameonly kmsArn: validKmsArn,
    nameonly customEncryptionContext: KeyStoreTypes.EncryptionContextString
  )

  type validKmsArn = s:string | KmsArn.ValidKmsArn?(s) witness *

  datatype MutationToApply = | MutationToApply(
    Identifier: string,
    Original: MutableProperties,
    Terminal: MutableProperties,
    CreateTime: string,
    ExclusiveStartKey: MutationIndexUtils.ExclusiveStartKey := Option.None,
    UUID: string,
    Input: Types.Mutations,
    CommitmentCiphertext: seq<uint8>,
    IndexCiphertext: seq<uint8>
  )

  /** The Commitment & Index are persisted to the storage by Initialize. **/
  /** The Commitment & Index are read by Apply. **/
  /** The Index is updated by Apply. **/
  /** Both are deleted when the Mutation is completed by Apply. **/
  datatype CommitmentAndIndex = CommitmentAndIndex(
    Commitment: KeyStoreTypes.MutationCommitment,
    Index: KeyStoreTypes.MutationIndex
  )
  {
    /** The Commitment & Index MUST always have the same Identifier & UUID. **/
    /** They MAY NOT have the same CreateTime. **/
    ghost predicate ValidState()
    {
      && Commitment.Identifier == Index.Identifier
      && Commitment.UUID == Index.UUID
    }
  }

  predicate MutationToApply?(MutationToApply: MutationToApply)
  {
    && KmsArn.ValidKmsArn?(MutationToApply.Original.kmsArn)
    && KmsArn.ValidKmsArn?(MutationToApply.Terminal.kmsArn)
    && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! MutationToApply.Original.customEncryptionContext.Keys)
    && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! MutationToApply.Terminal.customEncryptionContext.Keys)
  }

  function EncryptionContextStringToJSON(
    encryptionContext: KeyStoreTypes.EncryptionContextString
  ): (output: JSONValues.JSON)

  {
    var keys := SortedSets.ComputeSetToSequence(encryptionContext.Keys);

    if |keys| == 0 then
      JSONValues.Object([])
    else
      var KeysAndValues
        := Seq.Map(
             k
             requires k in encryptionContext
             => (k, JSONValues.JSON.String(encryptionContext[k]))
           , keys);
      JSONValues.Object(KeysAndValues)
  }

  function JSONToEncryptionContextString(
    EncryptionContext: JSONValues.JSON
  ): (output: KeyStoreTypes.EncryptionContextString)
    requires EncryptionContext.Object?
    requires forall p <- EncryptionContext.obj :: p.1.String?
    requires |set p <- EncryptionContext.obj :: p.0| == |EncryptionContext.obj|
  {
    LemmaJSONObjectCanConvertToDafnyMap(EncryptionContext);
    map
      i | 0 <= i < |EncryptionContext.obj|
      ::
        EncryptionContext.obj[i].0 := EncryptionContext.obj[i].1.str
  }

  function KmsArnToJSON(
    kmsArn: string
  ): (output: Result<JSONValues.JSON, Types.Error>)
  {
    Success(JSONValues.JSON.String(kmsArn))
  }

  function NeedOutcome<E>(
    condition: bool,
    error: () --> E)
    : (result: Outcome2<E>)
    requires !condition ==> error.requires()
  {
    if condition then Outcome2.Pass else Outcome2.Fail(error())
  }

  datatype Outcome2<E> = Pass | Fail(error: E)
  {
    predicate IsFailure() {
      Fail?
    }
    // Note: PropagateFailure returns a Result, not an Outcome.
    function PropagateFailure(): Outcome<E>
      requires Fail?
    {
      Outcome.Fail(this.error)
    }
    // Note: no Extract method
  }

  function InputMutationsToJson(
    Mutations: Types.Mutations
  ): (output: JSONValues.JSON)
  {
    var ec: JSONValues.JSON :=
      if Mutations.TerminalEncryptionContext.Some?
      then EncryptionContextStringToJSON(Mutations.TerminalEncryptionContext.value)
      else JSONValues.Null;
    var kms: JSONValues.JSON :=
      if Mutations.TerminalKmsArn.Some?
      then JSONValues.JSON.String(Mutations.TerminalKmsArn.value)
      else JSONValues.Null;
    var inputJson
      := JSONValues.Object([(AWS_CRYPTO_EC, ec), (KMS_FIELD, kms)]);
    inputJson
  }

  function InputMutationsFromJson(
    MutationsJson: JSONValues.JSON
  ): (output: Types.Mutations)
    requires MutationsJson.Object? && |MutationsJson.obj| == 2
    requires MutationsJson.obj[0].1.Object? ==>
               (var EncryptionContext := MutationsJson.obj[0].1;
                && (forall p <- EncryptionContext.obj :: p.1.String?)
                && (|set p <- EncryptionContext.obj :: p.0| == |EncryptionContext.obj|))
  {
    var ec: Option<KeyStoreTypes.EncryptionContextString> :=
      if MutationsJson.obj[0].1.Object?
      then Some(JSONToEncryptionContextString(MutationsJson.obj[0].1))
      else None;
    var kms: Option<string> :=
      if MutationsJson.obj[1].1.String?
      then Some(MutationsJson.obj[1].1.str)
      else None;
    var input
      := Types.Mutations(
           TerminalKmsArn := kms,
           TerminalEncryptionContext := ec);
    input
  }

  function DeserializeMutationInput(
    commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<Types.Mutations, Types.Error>)
  {
    var InputJson :- JSON.Deserialize(commitment.Input).MapFailure(
                       (e: JSONErrors.DeserializationError)
                       => Types.KeyStoreAdminException(
                           message := "Could not JSON Deserialize: Input. " + e.ToString()));
    :- MutationsInputJson?(InputJson);
    var input := InputMutationsFromJson(InputJson);
    Success(input)
  }

  function SerializeMutationCommitment(
    MutationToApply: MutationToApply
  ): (output: Result<KeyStoreTypes.MutationCommitment, Types.Error>)
    requires MutationToApply?(MutationToApply)
  {
    var OriginalJson
      := JSONValues.Object(
           [
             (AWS_CRYPTO_EC, EncryptionContextStringToJSON(MutationToApply.Original.customEncryptionContext)),
             (KMS_FIELD, JSONValues.JSON.String(MutationToApply.Original.kmsArn))
           ]);
    var TerminalJson
      := JSONValues.Object(
           [
             (AWS_CRYPTO_EC, EncryptionContextStringToJSON(MutationToApply.Terminal.customEncryptionContext)),
             (KMS_FIELD, JSONValues.JSON.String(MutationToApply.Terminal.kmsArn))
           ]);

    var InputJson := InputMutationsToJson(MutationToApply.Input);

    var originalBytes :- JSON.Serialize(OriginalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize state: original properties. " + e.ToString()));
    var terminalBytes :- JSON.Serialize(TerminalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize state: terminal properties. " + e.ToString()));
    var inputBytes :- JSON.Serialize(InputJson).MapFailure(
                        (e: JSONErrors.SerializationError)
                        => Types.KeyStoreAdminException(
                            message := "Could not JSON Serialize Input. " + e.ToString()));
    var commitment := KeyStoreTypes.MutationCommitment(
                        Identifier := MutationToApply.Identifier,
                        Original := originalBytes,
                        Terminal := terminalBytes,
                        UUID := MutationToApply.UUID,
                        CreateTime := MutationToApply.CreateTime,
                        CiphertextBlob := MutationToApply.CommitmentCiphertext,
                        Input := inputBytes
                      );
    Success(commitment)
  }

  function SerializeMutationIndex(
    MutationToApply: MutationToApply,
    ExclusiveStartKey: MutationIndexUtils.ExclusiveStartKey
  ): (output: Result<KeyStoreTypes.MutationIndex, Types.Error>)
    requires MutationToApply?(MutationToApply)
  {
    var index := KeyStoreTypes.MutationIndex(
                   Identifier := MutationToApply.Identifier,
                   PageIndex := MutationIndexUtils.ExclusiveStartKeyToPageIndex(ExclusiveStartKey),
                   UUID := MutationToApply.UUID,
                   CreateTime := MutationToApply.CreateTime,
                   CiphertextBlob := MutationToApply.IndexCiphertext // TODO-Mutations-GA
                 );
    Success(index)
  }

  function DeserializeMutation(
    commitmentAndIndex: CommitmentAndIndex
  ): (output: Result<MutationToApply, Types.Error>)
    ensures output.Success? ==> MutationToApply?(output.value)
  {
    var commitment := commitmentAndIndex.Commitment;
    var index := commitmentAndIndex.Index;
    var OriginalJson :- JSON.Deserialize(commitment.Original).MapFailure(
                          (e: JSONErrors.DeserializationError)
                          => Types.KeyStoreAdminException(
                              message := "Could not JSON Deserialize: original properties. " + e.ToString()));

    var TerminalJson :- JSON.Deserialize(commitment.Terminal).MapFailure(
                          (e: JSONErrors.DeserializationError)
                          => Types.KeyStoreAdminException(
                              message := "Could not JSON Deserialize: terminal properties. " + e.ToString()));
    var InputJson :- JSON.Deserialize(commitment.Input).MapFailure(
                       (e: JSONErrors.DeserializationError)
                       => Types.KeyStoreAdminException(
                           message := "Could not JSON Deserialize: Input. " + e.ToString()));

    :- MutablePropertiesJson?(OriginalJson);
    :- MutablePropertiesJson?(TerminalJson);
    :- MutationsInputJson?(InputJson);

    Success(
      MutationToApply(
        Identifier := commitment.Identifier,
        Original := MutableProperties(
          kmsArn := OriginalJson.obj[1].1.str,
          customEncryptionContext := JSONToEncryptionContextString(OriginalJson.obj[0].1)
        ),
        Terminal := MutableProperties(
          kmsArn := TerminalJson.obj[1].1.str,
          customEncryptionContext := JSONToEncryptionContextString(TerminalJson.obj[0].1)
        ),
        UUID := commitment.UUID,
        CreateTime := commitment.CreateTime,
        ExclusiveStartKey := MutationIndexUtils.PageIndexToExclusiveStartKey(index.PageIndex),
        CommitmentCiphertext := commitment.CiphertextBlob,
        IndexCiphertext := index.CiphertextBlob,
        Input := InputMutationsFromJson(InputJson)
      ))
  }

  const ERROR_PRFX := "Serialized State properties is malformed! "

  function MutablePropertiesJson?(
    MutableProperties: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
  {
    :- NeedOutcome(
         MutableProperties.Object? && |MutableProperties.obj| == 2,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "There should be two objects.")
       );
    :- NeedOutcome(
         MutableProperties.obj[0].0 == AWS_CRYPTO_EC,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "First Key MUST be Encryption Context.")
       );
    :- NeedOutcome(
         MutableProperties.obj[1].0 == KMS_FIELD,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "Second Key MUST be KMS ARN.")
       );
    :- NeedOutcome(
         MutableProperties.obj[0].1.Object?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + AWS_CRYPTO_EC + "` MUST be an object.")
       );
    :- NeedOutcome(
         MutableProperties.obj[1].1.String?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + KMS_FIELD + "` MUST be a string.")
       );
    :- NeedOutcome(
         KmsArn.ValidKmsArn?(MutableProperties.obj[1].1.str),
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "KMS ARN that has been deserialized is invalid.")
       );

    var EncryptionContext := MutableProperties.obj[0].1;
    :- NeedOutcome(
         forall p <- EncryptionContext.obj :: p.1.String?,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "Member of Encryption Context cannot be deserialized.")
       );

    var EncryptionContextKeys := set p <- EncryptionContext.obj :: p.0;
    :- NeedOutcome(
         |EncryptionContextKeys| == |EncryptionContext.obj|,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Size of Encryption Context keys is not equal to size of Encryption Context values. ")
       );

    :- NeedOutcome(
         Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! EncryptionContextKeys,
         () => Types.KeyStoreAdminException(
             message := "Invalid Mutation Token: MUST NOT model Item specific fields!"
           )
       );

    Outcome.Pass
  }

  function MutationsInputJson?(
    DeserializedMutations: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
  {
    :- NeedOutcome(
         DeserializedMutations.Object? && |DeserializedMutations.obj| == 2,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "There MUST not be more than two objects.")
       );
    :- NeedOutcome(
         DeserializedMutations.obj[0].0 == AWS_CRYPTO_EC,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "First Key MUST be Encryption Context.")
       );
    :- NeedOutcome(
         DeserializedMutations.obj[1].0 == KMS_FIELD,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "Second Key MUST be KMS ARN.")
       );
    :- NeedOutcome(
         DeserializedMutations.obj[0].1.Object? || DeserializedMutations.obj[0].1.Null?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + AWS_CRYPTO_EC + "` MUST be an object or Null.")
       );
    :- NeedOutcome(
         DeserializedMutations.obj[1].1.String? || DeserializedMutations.obj[1].1.Null?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + KMS_FIELD + "` MUST be a string or Null.")
       );

    // For the input, I do not think we care if the KMS ARN is valid
    // :- NeedOutcome(
    //      KmsArn.ValidKmsArn?(DeserializedMutations.obj[1].1.str),
    //      () => Types.KeyStoreAdminException( message := ERROR_PRFX + "KMS ARN that has been deserialized is invalid.")
    //    );
    NullableEncryptionContextJson?(DeserializedMutations.obj[0].1)
  }

  function NullableEncryptionContextJson?(
    NullableEncryptionContext: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
    requires NullableEncryptionContext.Object? || NullableEncryptionContext.Null?
  {
    if NullableEncryptionContext.Null?
    then Outcome.Pass
    else EncryptionContextJson?(NullableEncryptionContext)
  }

  function EncryptionContextJson?(
    EncryptionContextJson: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
    requires EncryptionContextJson.Object?
  {
    :- NeedOutcome(
         forall p <- EncryptionContextJson.obj :: p.1.String?,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "Member of Encryption Context cannot be deserialized.")
       );

    var EncryptionContextKeys := set p <- EncryptionContextJson.obj :: p.0;
    :- NeedOutcome(
         |EncryptionContextKeys| == |EncryptionContextJson.obj|,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Size of Encryption Context keys is not equal to size of Encryption Context values. ")
       );
    :- NeedOutcome(
         Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! EncryptionContextKeys,
         () => Types.KeyStoreAdminException(
             message := "Invalid Mutation Token: MUST NOT model Item specific fields!")
       );
    Outcome.Pass
  }

  // Quality of life proof that a correctly constructed JSON object,
  // will in fact go into a Dafny Map
  lemma LemmaJSONObjectCanConvertToDafnyMap(
    Object: JSONValues.JSON
  )
    requires Object.Object?
    requires |JSONObjectKeysToSet(Object)| == |Object.obj|
    decreases |Object.obj|
    ensures
      && (forall i, j
            :: 0 <= i < j < |Object.obj|
               ==> Object.obj[i].0 != Object.obj[j].0)
  {
    if |Object.obj| == 0 {
    } else {
      assert Object.obj == [Seq.First(Object.obj)] + Seq.DropFirst(Object.obj);
      assert JSONObjectKeysToSet(Object) == {First(Object.obj).0} + JSONObjectKeysToSet(JSONValues.Object(DropFirst(Object.obj)));
      if First(Object.obj) in DropFirst(Object.obj) {
        //   // If there is a duplicate, then we show that |JSONObjectKeysToSet(s)| == |s| cannot hold.
        assert JSONObjectKeysToSet(Object) == JSONObjectKeysToSet(JSONValues.Object(DropFirst(Object.obj)));
        LemmaCardinalityOfSet(JSONValues.Object(DropFirst(Object.obj)));
        assert |JSONObjectKeysToSet(Object)| <= |DropFirst(Object.obj)|;
      } else {
        LemmaCardinalityOfSet(JSONValues.Object(DropFirst(Object.obj)));
        assert |JSONObjectKeysToSet(Object)| == 1 + |JSONObjectKeysToSet(JSONValues.Object(DropFirst(Object.obj)))|;
        LemmaJSONObjectCanConvertToDafnyMap(JSONValues.Object(DropFirst(Object.obj)));
      }
    }
  }

  function JSONObjectKeysToSet(
    Object: JSONValues.JSON
  ): (output: set<string>)
    requires Object.Object?
  {
    set p <- Object.obj :: p.0
  }

  lemma LemmaCardinalityOfSet(Object: JSONValues.JSON)
    requires Object.Object?
    decreases |Object.obj|
    ensures |JSONObjectKeysToSet(Object)| <= |Object.obj|
  {
    if |Object.obj| == 0 {
    } else {
      assert JSONObjectKeysToSet(Object)
          == JSONObjectKeysToSet(JSONValues.Object(DropLast(Object.obj))) + {Last(Object.obj).0};
      LemmaCardinalityOfSet(JSONValues.Object(DropLast(Object.obj)));
    }
  }
}
