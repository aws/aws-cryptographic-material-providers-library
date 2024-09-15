// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"
  // include "../Model/AwsCryptographyKeyStoreTypes.dfy"
  // include "ErrorMessages.dfy"
  // include "KmsArn.dfy"
  // include "Structure.dfy"
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
          &&  forall k <- input.terminalEncryptionContext.value :: |k| > 0 && |input.terminalEncryptionContext.value[k]| > 0
                                                                && |Structure.SelectCustomEncryptionContextAsString(input.terminalEncryptionContext.value)| == 0
                                                                && input.terminalEncryptionContext.value.Keys !! Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES)
    && !(input.terminalKmsArn.None? && input.terminalEncryptionContext.None?)
  }

  /** An ordered collection of key, value that is the custom encryption context.*/
  /** The keys are defixed; "aws-crypto-ec:" has been removed, if it was added by the library.*/
  type SortedCustomEncryptionContext = seq<(KeyStoreTypes.Utf8Bytes, KeyStoreTypes.Utf8Bytes)>
  // TODO: witness forall key, value in seq<key, value> <- key[index - 1] < key[index]
  // TODO: witness this has been defixed, i.e: no "aws-crypt-ec"

  // Other documents called this state; I will refactor those
  datatype MutableBranchKeyProperties = | MutableBranchKeyProperties (
    nameonly kmsArn: string,
    nameonly customEncryptionContext: SortedCustomEncryptionContext
  )

  datatype MutableProperties = | MutableProperties (
    nameonly kmsArn: KeyStoreTypes.KMSConfiguration,
    nameonly customEncryptionContext: KeyStoreTypes.EncryptionContextString
  )

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
    && MutationToApply.Original.kmsArn.kmsKeyArn?
    && KmsArn.ValidKmsArn?(MutationToApply.Original.kmsArn.kmsKeyArn)
    && MutationToApply.Terminal.kmsArn.kmsKeyArn?
    && KmsArn.ValidKmsArn?(MutationToApply.Terminal.kmsArn.kmsKeyArn)
    && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! MutationToApply.Original.customEncryptionContext.Keys)
    && (Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES !! MutationToApply.Terminal.customEncryptionContext.Keys)
  }

  // method MutationsToMutableBranchKeyProperties(
  //   input: Types.Mutations,
  //   originalKmsArn: string,
  //   originalEncryptionContext: SortedCustomEncryptionContext
  // )
  //   returns (output: Result<MutableBranchKeyProperties, string>)
  //   requires ValidMutations?(input)
  // {
  //   var kmsArn: string := input.terminalKmsArn.UnwrapOr(originalKmsArn);
  //   var customEncryptionContext: SortedCustomEncryptionContext := originalEncryptionContext;
  //   if (input.terminalEncryptionContext.Some?) {
  //     customEncryptionContext :- CustomEncryptionContextToSortedCustomEncryptionContext(input.terminalEncryptionContext.value);
  //   }
  //   return Success(MutableBranchKeyProperties(
  //                    kmsArn := kmsArn,
  //                    customEncryptionContext := customEncryptionContext));
  // }

  // method ItemProperitiesToMutableBranchKeyProperties(
  //   activeFoo: KeyStoreTypes.EncryptionContextString,
  //   activeKmsArn: string
  // )
  //   returns (inferredOriginal: Result<MutableBranchKeyProperties, string>)
  // {
  //   var sortedEC :- EncrytionContextStringToSortedCustomEncryptionContext(activeFoo);
  //   inferredOriginal := Success(MutableBranchKeyProperties(
  //                                 kmsArn := activeKmsArn,
  //                                 customEncryptionContext := sortedEC));
  //   return inferredOriginal;
  // }

  predicate isCustomECKey?(input: string): (output: bool)
    ensures && output == true ==> |input| > 14
  {
    |input| > 14 && input[0..14] == "aws-crypto-ec:"
  }

  const ENCRYPTION_CONTEXT_PREFIX_UTF8_BYTES: seq<uint8> := [97,119,115,45,99,114,121,112,116,111,45,101,99,58]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=YXdzLWNyeXB0by1lYzo&oenc=65001&oeol=CR

  predicate isEncodedCustomECKey?(input: KeyStoreTypes.Utf8Bytes): (output: bool)
    ensures && output == true ==> |input| > |ENCRYPTION_CONTEXT_PREFIX_UTF8_BYTES|
  {
    |input| > |ENCRYPTION_CONTEXT_PREFIX_UTF8_BYTES| && input[0..|ENCRYPTION_CONTEXT_PREFIX_UTF8_BYTES|] == ENCRYPTION_CONTEXT_PREFIX_UTF8_BYTES
  }

  // TODO: if we made this a unique extern, we could do it in one pass instead of 2
  method CustomEncryptionContextToSortedCustomEncryptionContext(
    input: KeyStoreTypes.EncryptionContext
  )
    returns (output: Result<SortedCustomEncryptionContext, string>)
  {
    var keys: seq<KeyStoreTypes.Utf8Bytes> := SetToOrderedSequence(input.Keys, UInt.UInt8Less);
    var keyIndex: int := 0;
    var sortedEC: seq<(KeyStoreTypes.Utf8Bytes, KeyStoreTypes.Utf8Bytes)> := [];
    var encodedValue: KeyStoreTypes.Utf8Bytes := [];
    var encodedKey: KeyStoreTypes.Utf8Bytes := [];
    while keyIndex < |keys|
    {
      encodedKey := keys[keyIndex];
      encodedValue := input[encodedKey];
      :- Need(!isEncodedCustomECKey?(encodedKey), "Input MUST NOT have keys that begin with \"aws-crypto-ec:\".");
      sortedEC := sortedEC + [(encodedKey, encodedValue)];
      keyIndex := keyIndex + 1;
    }
    return Success(sortedEC);
  }

  // TODO: Refactor into one For loop, instead of 4
  /** From the EC sent to KMS, extract only the custom EC, defix the keys,
     and return a seq<(key, value)> that has been
     binary sorted under UTF-8 encoding of the Keys. */
  // method EncrytionContextStringToSortedCustomEncryptionContext(
  //   input: KeyStoreTypes.EncryptionContextString
  // )
  //   returns (output: Result<SortedCustomEncryptionContext, string>)
  // {
  //   return Failure("Implement me!"); 
  //   // var filteredKeys := Sets.Filter(input.Keys, isCustomECKey?);
  //   // var encodedDefixKeyToStringKeyMap: map<KeyStoreTypes.Utf8Bytes, string> := map[];
  //   // while filteredKeys != {}
  //   //   decreases |filteredKeys|
  //   // {
  //   //   var k: string :| k in filteredKeys;
  //   //   filteredKeys := filteredKeys - {k};
  //   //   assume {:axiom} |k| > 14; //Dafny needs help realizing Prefixed content can be defixed
  //   //   assert |k| > 14;
  //   //   var defixed := k[14..];
  //   //   var encoded :- UTF8.Encode(defixed);
  //   //   encodedDefixKeyToStringKeyMap := encodedDefixKeyToStringKeyMap[encoded := k];
  //   // }
  //   // var keys: seq<KeyStoreTypes.Utf8Bytes> := SetToOrderedSequence(encodedDefixKeyToStringKeyMap.Keys, UInt.UInt8Less);
  //   // var keyIndex: int := 0;
  //   // var sortedEC: seq<(KeyStoreTypes.Utf8Bytes, KeyStoreTypes.Utf8Bytes)> := [];
  //   // var encodedValue: KeyStoreTypes.Utf8Bytes := [];
  //   // var encodedKey: KeyStoreTypes.Utf8Bytes := [];
  //   // var k: string := "";
  //   // var v: string := "";
  //   // while keyIndex < |keys|
  //   // {
  //   //   encodedKey := keys[keyIndex];
  //   //   k := encodedDefixKeyToStringKeyMap[encodedKey];
  //   //   v := Maps.Get(input, k).UnwrapOr("");
  //   //   //TODO: prove k is in input
  //   //   encodedValue :- UTF8.Encode(v);
  //   //   sortedEC := sortedEC + [(keys[keyIndex], encodedValue)];
  //   //   keyIndex := keyIndex + 1;
  //   // }
  //   // return Success(sortedEC);
  // }

  method SortedCustomEncryptionContextToFoo(
    sortedEC: SortedCustomEncryptionContext
  )
    returns (output: Result<KeyStoreTypes.EncryptionContextString, string>)
    ensures output.Success? ==>
              && forall k <- output.value.Keys :: 0 <= |Structure.ENCRYPTION_CONTEXT_PREFIX + k| <= 65535
    // ensures output.Success? ==>
    //   && forall pair <- sortedEC :: UTF8.Decode(pair.0).Success? && UTF8.Decode(pair.1).Success?
  {
    var foo: KeyStoreTypes.EncryptionContextString := map[];
    if (|sortedEC| == 0) {
      return Success(foo);
    }
    var index: int := 0;
    while index < |sortedEC|
      invariant forall k <- foo.Keys :: 0 <= |Structure.ENCRYPTION_CONTEXT_PREFIX + k| <= 65535
      invariant |sortedEC| > index > 0 ==>
                  forall pair <- sortedEC[..index] ::
                    && (UTF8.Decode(pair.0).Success? && UTF8.Decode(pair.1).Success?)
                    && 0 <= |UTF8.Decode(pair.0).value| <= 65521
                    && UTF8.Decode(pair.0).value in foo.Keys
      //&& UTF8.Decode(pair.1).value in foo.Values

      //invariant forall k <- foo.Keys ::
      //  && (UTF8.Encode(k).Success? && UTF8.Encode(foo[k]).Success?)
      //  && ((UTF8.Encode(k).value, UTF8.Encode(foo[k]).value) in sortedEC)
    {
      var k :- UTF8.Decode(sortedEC[index].0)
      .MapFailure(eString => "Could not UTF8 Decode Encryption Context Key. " + eString);
      var v :- UTF8.Decode(sortedEC[index].1)
      .MapFailure(eString => "Could not UTF8 Decode Encryption Context Value. " + eString);
      :- Need(
        0 <= |Structure.ENCRYPTION_CONTEXT_PREFIX + k| <= 65535,
        "Encryption Context Keys MUST be less than 65521. Got key with length " + String.Base10Int2String(|k|) + ". Key: " + k
      );
      foo := foo[k := v];
      index := index + 1;
    }
    return Success(foo);
  }

  function SortedCustomEncryptionContextToJSON(
    sortedEC: SortedCustomEncryptionContext
  ): (output: Result<JSONValues.JSON, Types.Error>)
    // requires |sortedEC| > 0
  {
    var decodedSortedEC
      :- Seq.MapWithResult(
           (ec: (KeyStoreTypes.Utf8Bytes, KeyStoreTypes.Utf8Bytes))
           =>
             var decodedKey
               :- UTF8.Decode(ec.0).MapFailure(
                    e => Types.KeyStoreAdminException(message:="Error during UTF8 decoding of Sorted Custom Encryption Context: " + e));
             var decodedValue
               :- UTF8.Decode(ec.1).MapFailure(
                    e => Types.KeyStoreAdminException(message:="Error during UTF8 decoding of Sorted Custom Encryption Context: " + e));
             Success((decodedKey, JSONValues.JSON.String(decodedValue))),
           sortedEC);

    Success(JSONValues.Object(decodedSortedEC))
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


  // function utf8EncodePair(key: string, value: string):
  //   (res: Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>)
  // {
  //   var utf8Key :- UTF8.Encode(key)
  //                  .MapFailure(e => Types.KeyStoreAdminException( message := e));
  //   var utf8Value :- UTF8.Encode(value)
  //                    .MapFailure(e => Types.KeyStoreAdminException( message := e));

  //   Success((utf8Key, utf8Value))
  // }

  // // TODO: These EncryptionContext methods can be removed once we move to UTF8 strings
  // function utf8EncodeMap(mapStringString: map<string, string>):
  //   (res: Result<KeyStoreTypes.EncryptionContext, Types.Error>)
  // {
  //   if |mapStringString| == 0 then
  //     Success(map[])
  //   else

  //     var encodedResults := map key <- mapStringString :: key := utf8EncodePair(key, mapStringString[key]);
  //     :- Need(forall r <- encodedResults.Values :: r.Success?,
  //             Types.KeyStoreAdminException( message := "String can not be UTF8 Encoded?"));

  //     Success(map r <- encodedResults.Values :: r.value.0 := r.value.1)
  // }

  function SerializeMutableBranchKeyProperties(
    MutationToApply: MutationToApply
  ): (output: Result<Types.MutationToken, Types.Error>)
    requires MutationToApply?(MutationToApply)
  {
    var OriginalJson
      := JSONValues.Object([
                             ("aws-crypto-ec", EncryptionContextStringToJSON(MutationToApply.Original.customEncryptionContext)),
                             ("kms-arn", JSONValues.JSON.String(MutationToApply.Original.kmsArn.kmsKeyArn))
                           ]);
    var TerminalJson
      := JSONValues.Object([
                             ("aws-crypto-ec", EncryptionContextStringToJSON(MutationToApply.Terminal.customEncryptionContext)),
                             ("kms-arn", JSONValues.JSON.String(MutationToApply.Terminal.kmsArn.kmsKeyArn))
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
          kmsArn := KeyStoreTypes.kmsKeyArn(OriginalJson.obj[1].1.str),
          customEncryptionContext := JSONToEncryptionContextString(OriginalJson.obj[0].1)
        ),
        Terminal := MutableProperties(
          kmsArn := KeyStoreTypes.kmsKeyArn(TerminalJson.obj[1].1.str),
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

  function SortedCustomEncryptionContextFromJsonObj(
    decodedSortedEC: seq<(string, JSONValues.JSON)>
  ): (output: Result<SortedCustomEncryptionContext, Types.Error>)
  {
    var sortedEC: SortedCustomEncryptionContext
      :- Seq
         .MapWithResult(
           (ec: (string, JSONValues.JSON))
           =>
             var encodedKey: KeyStoreTypes.Utf8Bytes
               :- UTF8.Encode(ec.0)
                  .MapFailure(
                    e => Types.KeyStoreAdminException(message := "UTF8 Encoding Error while deserializing Mutation Token: " + e));
             :- Need(ec.1.String?,
                     Types.KeyStoreAdminException(message:="Custom Encryption Context should be a JSON String, but is not!"));
             var encodedValue: KeyStoreTypes.Utf8Bytes
               :- UTF8.Encode(ec.1.str).MapFailure(
                    e => Types.KeyStoreAdminException(message := "UTF8 Encoding Error while deserializing Mutation Token: " + e));
             Success((encodedKey, encodedValue)),
           decodedSortedEC);
    Success(sortedEC)
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
