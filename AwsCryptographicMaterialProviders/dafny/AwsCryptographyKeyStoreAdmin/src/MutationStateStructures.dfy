// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
include "../../../../libraries/src/Collections/Sets/Sets.dfy"
include "../../../../libraries/src/Collections/Maps/Maps.dfy"
include "../../../../libraries/src/JSON/API.dfy"
include "../../../../libraries/src/JSON/Errors.dfy"
include "../../../../libraries/src/JSON/Values.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"

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

  import CanonicalEncryptionContext
  import Base64

  import JSON = JSON.API
  import JSONErrors = JSON.Errors
  import JSONValues = JSON.Values

  const MUTABLE_PROPERTY_COUNT: int := 2
  const MUTABLE_PROPERTY_COUNT_str := "2"
  // Ensures
  // - if KMS ARN, Valid KMS ARN
  // - if EC, Valid non-empty EC
  // - non-empty
  predicate ValidMutations?(
    input: Types.Mutations
  )
  {
    && (input.terminalKmsArn.Some? ==> KmsArn.ValidKmsArn?(input.terminalKmsArn.value))
    && (input.terminalEncryptionContext.Some? ==>
          && |input.terminalEncryptionContext.value| > 0
          &&  forall k <- input.terminalEncryptionContext.value ::
               && |k| > 0 && |input.terminalEncryptionContext.value[k]| > 0
                  // && |Structure.SelectCustomEncryptionContextAsString(input.terminalEncryptionContext.value)| == 0
               && input.terminalEncryptionContext.value.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES)
    && !(input.terminalKmsArn.None? && input.terminalEncryptionContext.None?)
  }

  datatype MutableProperties = | MutableProperties (
    // nameonly kmsArn: KeyStoreTypes.KMSConfiguration,
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
      := JSONValues.Object([
                             ("aws-crypto-ec", EncryptionContextStringToJSON(MutationToApply.Original.customEncryptionContext)),
                             ("kms-arn", JSONValues.JSON.String(MutationToApply.Original.kmsArn))
                           ]);
    var TerminalJson
      := JSONValues.Object([
                             ("aws-crypto-ec", EncryptionContextStringToJSON(MutationToApply.Terminal.customEncryptionContext)),
                             ("kms-arn", JSONValues.JSON.String(MutationToApply.Terminal.kmsArn))
                           ]);

    var originalBytes :- JSON.Serialize(OriginalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could JSON Serialize state: original properties. " + e.ToString()));
    var terminalBytes :- JSON.Serialize(TerminalJson).MapFailure(
                           (e: JSONErrors.SerializationError)
                           => Types.KeyStoreAdminException(
                               message := "Could JSON Serialize state: terminal properties. " + e.ToString()));
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

  const ERROR_PRFX := "Serialized State properties is malformed!"

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

  function MutablePropertiesJson?(
    MutableProperties: JSONValues.JSON
  ): (output: Outcome<Types.Error>)
  {
    :- NeedOutcome(
         MutableProperties.Object? && |MutableProperties.obj| == 2,
         () => Types.KeyStoreAdminException( message := "WIP")
       );
    :- NeedOutcome(
         MutableProperties.obj[0].0 == "aws-crypto-ec",
         () => Types.KeyStoreAdminException( message := "WIP")
       );
    :- NeedOutcome(
         MutableProperties.obj[1].0 == "kms-arn",
         () => Types.KeyStoreAdminException( message := "WIP")
       );
    :- NeedOutcome(
         MutableProperties.obj[0].1.Object?,
         () => Types.KeyStoreAdminException( message := "WIP")
       );
    :- NeedOutcome(
         MutableProperties.obj[1].1.String?,
         () => Types.KeyStoreAdminException( message := "WIP")
       );
    :- NeedOutcome(
         KmsArn.ValidKmsArn?(MutableProperties.obj[1].1.str),
         () => Types.KeyStoreAdminException( message := "WIP")
       );

    var EncryptionContext := MutableProperties.obj[0].1;
    :- NeedOutcome(
         forall p <- EncryptionContext.obj :: p.1.String?,
         () => Types.KeyStoreAdminException( message := "WIP")
       );

    var EncryptionContextKeys := set p <- EncryptionContext.obj :: p.0;
    :- NeedOutcome(
         |EncryptionContextKeys| == |EncryptionContext.obj|,
         () => Types.KeyStoreAdminException( message := "WIP")
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
