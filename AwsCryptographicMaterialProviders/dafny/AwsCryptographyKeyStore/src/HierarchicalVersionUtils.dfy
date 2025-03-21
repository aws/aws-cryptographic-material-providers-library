// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "KMSKeystoreOperations.dfy"
include "KmsArn.dfy"

module HierarchicalVersionUtils {

  import opened StandardLibrary
  import opened Wrappers
  import opened Seq

  import ErrorMessages = KeyStoreErrorMessages
  import Types = AwsCryptographyKeyStoreTypes
  import KMS = ComAmazonawsKmsTypes
  
  import AtomicPrimitives
  import UTF8
  import KMSKeystoreOperations
  import KmsArn
  import Structure
  
  function method GetMdDigestFromEC(
    item: Types.EncryptionContextString
  ) : (output: Types.EncryptionContextString)
  ensures output.Keys == item.Keys - {Structure.TABLE_FIELD}
  ensures forall k :: k in output ==> output[k] == item[k]
  ensures forall k :: k in output ==> k !in {Structure.TABLE_FIELD}
  {
    map k <- item.Keys - {Structure.TABLE_FIELD}
      :: k := item[k]
  }
  
  method GetHV2EC(
    ecStringMap: Types.EncryptionContextString
  ) returns (output: Types.EncryptionContextString)
    ensures Structure.Hv2EncryptionContext?(output)
  {
    var withoutRestrictedField := RemoveRestrictedFields(ecStringMap);
    var items := withoutRestrictedField.Items;
    var newMap: map<string, string> := map[];

    while items != {}
        decreases |items|
    {
        var item :| item in items;
        items := items - { item };
        if (|item.0| >= |Structure.ENCRYPTION_CONTEXT_PREFIX| && item.0[..|Structure.ENCRYPTION_CONTEXT_PREFIX|] == Structure.ENCRYPTION_CONTEXT_PREFIX) {
          var newKey := item.0[|Structure.ENCRYPTION_CONTEXT_PREFIX|..];
          newMap := newMap[newKey := item.1];
        } else {
          newMap := newMap[item.0 := item.1];
        }
    }
    return withoutRestrictedField;
  }

  function method RemoveRestrictedFields(a:map<string, string>) : (output:map<string, string>)
    ensures Structure.Hv2EncryptionContext?(output)
  {
    a - Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
  }

  function method UnstringifyEncryptionContext(stringEncCtx: Types.EncryptionContextString) : (res: Result<Types.EncryptionContext, Types.Error>)
  {
    if |stringEncCtx| == 0 then
        Success(map[])
    else
    var parseResults: map<string, Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>> :=
        map strKey | strKey in stringEncCtx.Keys :: strKey := UnstringifyEncryptionContextPair(strKey, stringEncCtx[strKey]);
    if exists r | r in parseResults.Values :: r.Failure?
    then Failure(
            Types.KeyStoreException(message := "Encryption context contains invalid UTF8")
        )
    else
        assert forall r | r in parseResults.Values :: r.Success?;
        var utf8KeysUnique := forall k, k' | k in parseResults && k' in parseResults
                                :: k != k' ==> parseResults[k].value.0 != parseResults[k'].value.0;
        if !utf8KeysUnique then Failure(Types.KeyStoreException(
                                        message := "Encryption context keys are not unique"))  // this should never happen...
        else Success(map r | r in parseResults.Values :: r.value.0 := r.value.1)
  }

  function method UnstringifyEncryptionContextPair(strKey: string, strValue: string) : (res: Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>)
      ensures (UTF8.Encode(strKey).Success? && UTF8.Encode(strValue).Success?) <==> res.Success?
  {
      var key :- UTF8
                .Encode(strKey)
                .MapFailure(WrapStringToError);
      var value :- UTF8
                  .Encode(strValue)
                  .MapFailure(WrapStringToError);

      Success((key, value))
  }

  function method WrapStringToError(e: string)
    :(ret: Types.Error)
  {
    Types.KeyStoreException( message := e )
  }

  method ProvideCryptoClient(
    // Crypto?: Option<AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient> := None
    Crypto?: Option<AtomicPrimitives.AtomicPrimitivesClient> := None
  )
    returns (output: Result<AtomicPrimitives.AtomicPrimitivesClient, AtomicPrimitives.Types.Error>)
    requires Crypto?.Some? ==> Crypto?.value.ValidState()
    modifies (if Crypto?.Some? then Crypto?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var Crypto: AtomicPrimitives.AtomicPrimitivesClient; //AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient;
    if (Crypto?.None?) {
      Crypto :- AtomicPrimitives.AtomicPrimitives();
    } else {
      Crypto := Crypto?.value;
    }
    // If the customer gave us the Crypto Client, it is fresh
    // If we create the Crypto Client, it is fresh
    assume {:axiom} fresh(Crypto) && fresh(Crypto.Modifies);
    return Success(Crypto);
  }
}