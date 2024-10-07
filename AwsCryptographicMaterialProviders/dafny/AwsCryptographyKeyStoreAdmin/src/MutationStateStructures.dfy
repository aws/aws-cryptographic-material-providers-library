// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../../../libraries/src/Collections/Sets/Sets.dfy"
include "../../../../libraries/src/Collections/Maps/Maps.dfy"
include "../../../../libraries/src/JSON/API.dfy"
include "../../../../libraries/src/JSON/Errors.dfy"
include "../../../../libraries/src/JSON/Values.dfy"

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
    ExclusiveStartKey: Option<seq<uint8>> := Option.None ,
    UUID: Option<string> := Option.None
  )

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


  function SerializeMutableBranchKeyProperties(
    MutationToApply: MutationToApply
  ): (output: Result<Types.MutationToken, Types.Error>)
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

    var originalBytes :- JSON.Serialize(OriginalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize state: original properties. " + e.ToString()));
    var terminalBytes :- JSON.Serialize(TerminalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could not JSON Serialize state: terminal properties. " + e.ToString()));
    Success(
      Types.MutationToken(
        Identifier := MutationToApply.Identifier,
        Original := originalBytes,
        Terminal := terminalBytes,
        ExclusiveStartKey := MutationToApply.ExclusiveStartKey,
        UUID := MutationToApply.UUID,
        CreateTime := MutationToApply.CreateTime
      ))
  }

  function DeserializeMutationToken(
    Token: Types.MutationToken
  )
    : (output: Result<MutationToApply, Types.Error>)
    ensures output.Success? ==> MutationToApply?(output.value)
  {
    var OriginalJson :- JSON.Deserialize(Token.Original).MapFailure(
                          (e: JSONErrors.DeserializationError)
                          => Types.KeyStoreAdminException(
                              message := "Could not JSON Deserialize state: original properties. " + e.ToString()));

    var TerminalJson :- JSON.Deserialize(Token.Terminal).MapFailure(
                          (e: JSONErrors.DeserializationError)
                          => Types.KeyStoreAdminException(
                              message := "Could not JSON Deserialize state: terminal properties. " + e.ToString()));

    :- MutablePropertiesJson?(OriginalJson);
    :- MutablePropertiesJson?(TerminalJson);

    Success(
      MutationToApply(
        Identifier := Token.Identifier,
        Original := MutableProperties(
          kmsArn := OriginalJson.obj[1].1.str,
          customEncryptionContext := JSONToEncryptionContextString(OriginalJson.obj[0].1)
        ),
        Terminal := MutableProperties(
          kmsArn := TerminalJson.obj[1].1.str,
          customEncryptionContext := JSONToEncryptionContextString(TerminalJson.obj[0].1)
        ),
        ExclusiveStartKey := Token.ExclusiveStartKey,
        UUID := Token.UUID,
        CreateTime := Token.CreateTime
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
