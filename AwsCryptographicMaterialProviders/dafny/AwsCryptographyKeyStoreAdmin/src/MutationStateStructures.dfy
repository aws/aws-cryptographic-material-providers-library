// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../../../libraries/src/JSON/API.dfy"
include "../../../../libraries/src/JSON/Errors.dfy"
include "../../../../libraries/src/JSON/Values.dfy"
include "MutationIndexUtils.dfy"

/** Mutation State Structures describe the Mutable Branch Key Properties that can be changed by Mutaiton. **/
/** Methods here normialize these descriptions so they may be compared. **/
module {:options "/functionSyntax:4" } MutationStateStructures {
  import opened StandardLibrary
  import opened StandardLibrary.UInt
  import opened StandardLibrary.NeedError
  import opened Wrappers
  import opened Seq
  import UTF8
  import String = StandardLibrary.String
  import SortedSets

  import ErrorMessages = KeyStoreErrorMessages
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreOperations = AwsCryptographyKeyStoreOperations
  import KeyStoreTypes = KeyStoreOperations.Types
  import KmsArn
  import Structure
  import HVUtils = HierarchicalVersionUtils

  import JSON = JSON.API
  import JSONErrors = JSON.Errors
  import JSONValues = JSON.Values
  import MutationIndexUtils

  const AWS_CRYPTO_EC := Structure.AWS_CRYPTO_EC
  const KMS_FIELD := Structure.KMS_FIELD
  const HV_FIELD := Structure.HIERARCHY_VERSION
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
    nameonly customEncryptionContext: KeyStoreTypes.EncryptionContextString,
    nameonly hierarchyVersion: KeyStoreTypes.HierarchyVersion
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
  {
    ghost predicate ValidState()
    {
      && 0 < |Identifier|
      && 0 < |UUID|
      && KmsArn.ValidKmsArn?(Original.kmsArn)
      && KmsArn.ValidKmsArn?(Terminal.kmsArn)
      && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! Original.customEncryptionContext.Keys)
      && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! Terminal.customEncryptionContext.Keys)
    }
  }

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
    predicate ValidState()
    {
      && Commitment.Identifier == Index.Identifier
      && 0 < |Commitment.Identifier|
      && Commitment.UUID == Index.UUID
      && 0 < |Commitment.UUID|
    }
    predicate ValidUTF8()
    {
      && UTF8.ValidUTF8Seq(Commitment.Original)
      && UTF8.ValidUTF8Seq(Commitment.Terminal)
      && UTF8.ValidUTF8Seq(Commitment.Input)
      && UTF8.ValidUTF8Seq(Index.PageIndex)
      && 0 < |Commitment.Identifier|
      && 0 < |Index.Identifier|
      && 0 < |Commitment.UUID|
      && 0 < |Index.UUID|
    }
  }

  // Pre-HV-2 Mutations did not track Hierarchy Version;
  // therefore, HV MAY NOT be present in a Mutation Commitment.
  // If HV is not present, we KNOW it is HV1.
  // If HV is present, then it is the third element.
  function MutablePropertiesJsonToHierarhcyVersion(
    deserializedMutableProperties: JSONValues.JSON
  ): (output: KeyStoreTypes.HierarchyVersion)
    requires MutablePropertiesJson?(deserializedMutableProperties).Pass?
  {
    if |deserializedMutableProperties.obj| == 3
    then HVUtils.StringToHierarchyVersion(deserializedMutableProperties.obj[2].1.str)
    else KeyStoreTypes.HierarchyVersion.v1
  }

  // Pre-HV-2 Mutations did not track Hierarchy Version;
  // therefore, HV MAY NOT be present in the Mutation Commitment's Input.
  // If HV is not present, we KNOW the customer could not and did not provide it.
  // If HV key is present, then it is the third element, and is nullable,
  // as a post-HV-2 mutation could mutate the HV.
  function InputMutationsJsonToHierarhcyVersion(
    deserializedInput: JSONValues.JSON
  ): (output: Option<KeyStoreTypes.HierarchyVersion>)
    requires MutablePropertiesJson?(deserializedInput).Pass?
  {
    if |deserializedInput.obj| == 3 && deserializedInput.obj[2].0 == HV_FIELD && deserializedInput.obj[2].1.String?
    then Some(HVUtils.StringToHierarchyVersion(deserializedInput.obj[2].1.str))
    else None
  }

  function EncryptionContextStringToJSON(
    encryptionContext: KeyStoreTypes.EncryptionContextString
  ): (output: JSONValues.JSON)
  {
    var keys := SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, (a, b) => a < b);
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
    var hv: JSONValues.JSON :=
      if Mutations.TerminalHierarchyVersion.Some?
      then JSONValues.JSON.String(HVUtils.HierarchyVersionToString(Mutations.TerminalHierarchyVersion.value))
      else JSONValues.Null;
    // TODO-HV-2-M2 : Ensure that pre-HV-1 Mutation Commitments deserialize
    // such commitments will not have the new HV field
    var inputJson
      := JSONValues.Object([(AWS_CRYPTO_EC, ec), (KMS_FIELD, kms), (HV_FIELD, hv)]);
    inputJson
  }

  // TODO-HV-2-M2 : Ensure that pre-HV-1 Mutation Commitments deserialize
  // such commitments will not have the new HV field
  function InputMutationsFromJson(
    MutationsJson: JSONValues.JSON
  ): (output: Types.Mutations)
    requires MutationsJson.Object? && (|MutationsJson.obj| == 2 || |MutationsJson.obj| == 3)
    requires MutationsJson.obj[0].1.Object? ==>
               (var EncryptionContext := MutationsJson.obj[0].1;
                && (forall p <- EncryptionContext.obj :: p.1.String?)
                && (|set p <- EncryptionContext.obj :: p.0| == |EncryptionContext.obj|))
    requires
      && |MutationsJson.obj| == 3 && MutationsJson.obj[2].1.String?
      ==>
        || MutationsJson.obj[2].1.str == Structure.HIERARCHY_VERSION_VALUE_1
        || MutationsJson.obj[2].1.str == Structure.HIERARCHY_VERSION_VALUE_2
  {
    var ec: Option<KeyStoreTypes.EncryptionContextString> :=
      if MutationsJson.obj[0].1.Object?
      then Some(JSONToEncryptionContextString(MutationsJson.obj[0].1))
      else None;
    var kms: Option<string> :=
      if MutationsJson.obj[1].1.String?
      then Some(MutationsJson.obj[1].1.str)
      else None;
    var hv: Option<KeyStoreTypes.HierarchyVersion> :=
      if |MutationsJson.obj| == 3 && MutationsJson.obj[2].1.String?
      then Some(HVUtils.StringToHierarchyVersion(MutationsJson.obj[2].1.str))
      else None;
    var input
      := Types.Mutations(
           TerminalKmsArn := kms,
           TerminalEncryptionContext := ec,
           TerminalHierarchyVersion := hv);
    input
  }

  function ValidateJSONSerialize(
    jsonByteSeq: seq<uint8>
  ): (output: Result<UTF8.ValidUTF8Bytes, string>)
    ensures
      output.Success?
      ==>
        && UTF8.ValidUTF8Seq(jsonByteSeq)
        && output.value == jsonByteSeq
  {
    if UTF8.ValidUTF8Seq(jsonByteSeq)
    then Success(jsonByteSeq)
    else Failure("Failure to UTF8 Validate results of JSON Serialization.")
  }

  function SerializeMutationCommitment(
    MutationToApply: MutationToApply
  ): (output: Result<KeyStoreTypes.MutationCommitment, Types.Error>)
    requires MutationToApply.ValidState() //MutationToApply?(MutationToApply)
    ensures
      && output.Success?
      ==>
        && UTF8.ValidUTF8Seq(output.value.Original)
        && UTF8.ValidUTF8Seq(output.value.Terminal)
        && UTF8.ValidUTF8Seq(output.value.Input)
        && 0 < |output.value.Identifier|
        && 0 < |output.value.UUID|
  {
    var OriginalJson
      := JSONValues.Object(
           [
             (AWS_CRYPTO_EC, EncryptionContextStringToJSON(MutationToApply.Original.customEncryptionContext)),
             (KMS_FIELD, JSONValues.JSON.String(MutationToApply.Original.kmsArn)),
             (HV_FIELD, JSONValues.JSON.String(HVUtils.HierarchyVersionToString(MutationToApply.Original.hierarchyVersion)))
           ]);
    var TerminalJson
      := JSONValues.Object(
           [
             (AWS_CRYPTO_EC, EncryptionContextStringToJSON(MutationToApply.Terminal.customEncryptionContext)),
             (KMS_FIELD, JSONValues.JSON.String(MutationToApply.Terminal.kmsArn)),
             (HV_FIELD, JSONValues.JSON.String(HVUtils.HierarchyVersionToString(MutationToApply.Terminal.hierarchyVersion)))
           ]);

    var InputJson := InputMutationsToJson(MutationToApply.Input);

    var originalBytes :- JSON.Serialize(OriginalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize original properties. " + e.ToString()));
    var validatedOriginalBytes: UTF8.ValidUTF8Bytes :- ValidateJSONSerialize(originalBytes)
                                                       .MapFailure(
                                                         (e: string) =>
                                                           Types.KeyStoreAdminException(message := "Could not JSON Serialize original properties. " + e));

    var terminalBytes :- JSON.Serialize(TerminalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize terminal properties. " + e.ToString()));
    var validatedTerminalBytes: UTF8.ValidUTF8Bytes :- ValidateJSONSerialize(terminalBytes)
                                                       .MapFailure(
                                                         (e: string) =>
                                                           Types.KeyStoreAdminException(message := "Could not JSON Serialize terminal properties. " + e));

    var inputBytes :- JSON.Serialize(InputJson).MapFailure(
                        (e: JSONErrors.SerializationError)
                        => Types.KeyStoreAdminException(
                            message := "Could not JSON Serialize Input. " + e.ToString()));
    var validatedInputBytes: UTF8.ValidUTF8Bytes :- ValidateJSONSerialize(inputBytes)
                                                    .MapFailure(
                                                      (e: string) =>
                                                        Types.KeyStoreAdminException(message := "Could not JSON Serialize Input. " + e));

    var commitment := KeyStoreTypes.MutationCommitment(
                        Identifier := MutationToApply.Identifier,
                        Original := validatedOriginalBytes, //originalBytes,
                        Terminal := validatedTerminalBytes, //terminalBytes,
                        UUID := MutationToApply.UUID,
                        CreateTime := MutationToApply.CreateTime,
                        CiphertextBlob := MutationToApply.CommitmentCiphertext,
                        Input := validatedInputBytes //inputBytes
                      );
    Success(commitment)
  }

  function SerializeMutationIndex(
    MutationToApply: MutationToApply,
    ExclusiveStartKey: MutationIndexUtils.ExclusiveStartKey
  ): (output: Result<KeyStoreTypes.MutationIndex, Types.Error>)
    requires MutationToApply.ValidState() //MutationToApply?(MutationToApply)
    ensures
      && output.Success?
      ==>
        && UTF8.ValidUTF8Seq(output.value.PageIndex)
        && 0 < |output.value.Identifier|
        && 0 < |output.value.UUID|
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

  // TODO-HV-2-M2 : Ensure that pre-HV-1 Mutation Commitments deserialize
  // such commitments will not have the new HV field
  function DeserializeMutation(
    commitmentAndIndex: CommitmentAndIndex
  ): (output: Result<MutationToApply, Types.Error>)
    requires commitmentAndIndex.ValidState()
    ensures output.Success? ==> output.value.ValidState()
  {
    var commitment := commitmentAndIndex.Commitment;
    var index := commitmentAndIndex.Index;
    var OriginalJson: JSONValues.JSON :- JSON.Deserialize(commitment.Original).MapFailure(
                                           (e: JSONErrors.DeserializationError)
                                           => Types.KeyStoreAdminException(
                                               message := "Could not JSON Deserialize: original properties. " + e.ToString()));

    var TerminalJson: JSONValues.JSON :- JSON.Deserialize(commitment.Terminal).MapFailure(
                                           (e: JSONErrors.DeserializationError)
                                           => Types.KeyStoreAdminException(
                                               message := "Could not JSON Deserialize: terminal properties. " + e.ToString()));
    var InputJson: JSONValues.JSON :- JSON.Deserialize(commitment.Input).MapFailure(
                                        (e: JSONErrors.DeserializationError)
                                        => Types.KeyStoreAdminException(
                                            message := "Could not JSON Deserialize: Input. " + e.ToString()));

    :- MutablePropertiesJson?(OriginalJson);
    :- MutablePropertiesJson?(TerminalJson);
    :- MutationsInputJson?(InputJson);

    :- Need(
         UTF8.ValidUTF8Seq(index.PageIndex),
         Types.KeyStoreAdminException(
           message := "PageIndex (pageIndex) is not a Valid UTF-8 Byte sequence."));

    var OriginalEC := JSONToEncryptionContextString(OriginalJson.obj[0].1);
    :- Need(
         Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! OriginalEC.Keys,
         Types.KeyStoreAdminException(
           message:="Original Properities contain illegal Encryption Context! There are some resereved Encryption Context Keys!"));

    var TerminalEC := JSONToEncryptionContextString(TerminalJson.obj[0].1);
    :- Need(
         Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! TerminalEC.Keys,
         Types.KeyStoreAdminException(
           message:="Terminal Properities contain illegal Encryption Context! There are some resereved Encryption Context Keys!"));

    Success(
      MutationToApply(
        Identifier := commitment.Identifier,
        Original := MutableProperties(
          kmsArn := OriginalJson.obj[1].1.str,
          customEncryptionContext := OriginalEC,
          hierarchyVersion := MutablePropertiesJsonToHierarhcyVersion(OriginalJson)
        ),
        Terminal := MutableProperties(
          kmsArn := TerminalJson.obj[1].1.str,
          customEncryptionContext := TerminalEC,
          hierarchyVersion := MutablePropertiesJsonToHierarhcyVersion(TerminalJson)
        ),
        UUID := commitment.UUID,
        CreateTime := commitment.CreateTime,
        ExclusiveStartKey := MutationIndexUtils.PageIndexToExclusiveStartKey(index.PageIndex),
        CommitmentCiphertext := commitment.CiphertextBlob,
        IndexCiphertext := index.CiphertextBlob,
        Input := InputMutationsFromJson(InputJson)
      ))
  }

  function DeserializeMutationInput(
    commitment: KeyStoreTypes.MutationCommitment
  ): (output: Result<Types.Mutations, Types.Error>)
    requires 0 < |commitment.UUID| && 0 < |commitment.Identifier|
    requires UTF8.ValidUTF8Seq(commitment.Input)
  {
    var InputJson :- JSON.Deserialize(commitment.Input).MapFailure(
                       (e: JSONErrors.DeserializationError)
                       => Types.KeyStoreAdminException(
                           message := "Could not JSON Deserialize: Input. " + e.ToString()));
    :- MutationsInputJson?(InputJson);
    var input := InputMutationsFromJson(InputJson);
    Success(input)
  }

  const ERROR_PRFX := "Serialized State properties is malformed! "

  function MutablePropertiesJson?(
    MutableProperties: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
  {
    :- NeedOutcome(
         MutableProperties.Object? && (|MutableProperties.obj| == 2 || |MutableProperties.obj| == 3),
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "There should be two or three objects.")
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
         |MutableProperties.obj| == 2 || MutableProperties.obj[2].0 == HV_FIELD,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "If there are three objects, the third key MUST be Hierarchy Version.")
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
    :- NeedOutcome(
         |MutableProperties.obj| == 2 || MutableProperties.obj[2].1.String?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + HV_FIELD + "` MUST be a string, if it is present.")
       );
    :- NeedOutcome(
         |MutableProperties.obj| == 2 || HVUtils.StringIsValidHierarchyVersion?(MutableProperties.obj[2].1.str),
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + HV_FIELD + "` that has been deserialized is not '1' or '2'.")
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
             message := "Invalid Mutation Commitment: MUST NOT model Item specific fields!"
           )
       );
    Outcome.Pass
  }

  function MutationsInputJson?(
    DeserializedInput: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
  {
    // Needs/Conditions for the entire object
    :- NeedOutcome(
         DeserializedInput.Object? && (|DeserializedInput.obj| == 2 || |DeserializedInput.obj| == 3),
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "There MUST two or three objects.")
       );
    // Needs/Conditions for the KMS-ARN
    :- NeedOutcome(
         DeserializedInput.obj[1].0 == KMS_FIELD,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "Second Key MUST be KMS ARN.")
       );
    :- NeedOutcome(
         DeserializedInput.obj[1].1.String? || DeserializedInput.obj[1].1.Null?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + KMS_FIELD + "` MUST be a string or Null.")
       );
    // Needs/Conditions for the Hierarchy Version
    :- NeedOutcome(
         |DeserializedInput.obj| == 2 || DeserializedInput.obj[2].0 == HV_FIELD,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "If there is a third key, it MUST be Hierarchy Version.")
       );
    :- NeedOutcome(
         |DeserializedInput.obj| == 2 || (DeserializedInput.obj[2].1.String? || DeserializedInput.obj[2].1.Null?),
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + HV_FIELD + "` MUST be a string or Null.")
       );
    :- NeedOutcome(
         || |DeserializedInput.obj| == 2
         || (
              ( && DeserializedInput.obj[2].1.String?
                && HVUtils.StringIsValidHierarchyVersion?(DeserializedInput.obj[2].1.str)
              ) || DeserializedInput.obj[2].1.Null?),
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + HV_FIELD + "` MUST be a string or Null; if it is a string, it MUST be '1' or '2'.")
       );
    // Needs/Conditions for the Encryption Context
    :- NeedOutcome(
         DeserializedInput.obj[0].0 == AWS_CRYPTO_EC,
         () => Types.KeyStoreAdminException( message := ERROR_PRFX + "First Key MUST be Encryption Context.")
       );
    :- NeedOutcome(
         DeserializedInput.obj[0].1.Object? || DeserializedInput.obj[0].1.Null?,
         () => Types.KeyStoreAdminException(
             message := ERROR_PRFX + "Value for `" + AWS_CRYPTO_EC + "` MUST be an object or Null.")
       );
    NullableEncryptionContextJson?(DeserializedInput.obj[0].1)
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
