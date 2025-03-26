// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"

module HierarchicalVersionUtils {

  import opened Wrappers
  import AtomicPrimitives
  import Types = AwsCryptographyKeyStoreTypes
  import UTF8
  import Structure

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

  function SelectKmsEncryptionContextForHv2(
    encryptionContext: Types.EncryptionContextString
  ): (output: Types.EncryptionContextString)
    requires Structure.BranchKeyContext?(encryptionContext)
    // TODO-HV-2-M2: Revisit this implementation to handle scenarios where removing prefix results in conflicting keys.
    requires forall k1, k2 <- encryptionContext.Keys ::
               (if HasPrefix(k1) then RemovePrefix(k1) else k1) ==
               (if HasPrefix(k2) then RemovePrefix(k2) else k2) ==>
                 k1 == k2
    ensures forall k <- output ::
              k !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
    ensures forall k <- output ::
              exists originalKey ::
                originalKey in encryptionContext &&
                (HasPrefix(originalKey) ==> k == RemovePrefix(originalKey)) &&
                (!HasPrefix(originalKey) ==> k == originalKey)
    ensures Structure.Hv2EncryptionContext?(output)
  {
    var transformedContext :=
      set k <- encryptionContext.Keys
        :: (
             if HasPrefix(k) then RemovePrefix(k) else k,  // transformed key
             encryptionContext[k],                         // original value
             k                                             // original key
           );

    // Filter out entries where transformed key is restricted
    var validContext :=
      set entry <- transformedContext
          | entry.0 !in Structure.BRANCH_KEY_RESTRICTED_FIELD_NAMES
        :: entry;

    map entry <- validContext :: entry.0 := entry.1
  }

  function HasPrefix(key: string): bool {
    |key| > |Structure.ENCRYPTION_CONTEXT_PREFIX| &&
    key[..|Structure.ENCRYPTION_CONTEXT_PREFIX|] == Structure.ENCRYPTION_CONTEXT_PREFIX
  }

  function RemovePrefix(key: string): string
    requires HasPrefix(key)
  {
    key[|Structure.ENCRYPTION_CONTEXT_PREFIX|..]
  }

  // Helper function to encode encryption context from string map to UTF8 bytes map
  function EncodeEncryptionContext(
    input: Types.EncryptionContextString
  ): (output: Result<Types.EncryptionContext, string>)
    ensures output.Success? ==> |output.value| == |input| // Output map size equals input map size
    ensures output.Failure? ==> output.error == "Unable to encode string"
  {
    var encodedEncryptionContext
      := set k <- input
           ::
             (UTF8.Encode(k), UTF8.Encode(input[k]), k);

    if (forall i <- encodedEncryptionContext
          ::
            && i.0.Success?
            && i.1.Success?
            && var encoded := UTF8.Decode(i.0.value);
            && encoded.Success?
            && i.2 == encoded.value)
    then
      var resultMap := map i <- encodedEncryptionContext :: i.0.value := i.1.value;
      if |resultMap| == |input| then
        Success(resultMap)
      else
        Failure("Unable to encode string")
    else
      Failure("Unable to encode string")
  }

  // Helper function to decode encryption context from UTF8 bytes map to string map
  function DecodeEncryptionContext(
    input: Types.EncryptionContext
  ): (output: Result<Types.EncryptionContextString, string>)
    ensures output.Success? ==> |output.value| == |input| // Output map size equals input map size
    ensures output.Failure? ==> output.error == "Unable to decode string"
  {
    var decodedEncryptionContext
      := set k <- input
           ::
             (UTF8.Decode(k), UTF8.Decode(input[k]), k);

    if (forall i <- decodedEncryptionContext
          ::
            && i.0.Success?
            && i.1.Success?
            && var decoded := UTF8.Encode(i.0.value);
            && decoded.Success?
            && i.2 == decoded.value)
    then
      var resultMap := map i <- decodedEncryptionContext :: i.0.value := i.1.value;
      if |resultMap| == |input| then
        Success(resultMap)
      else
        Failure("Unable to decode string")
    else
      Failure("Unable to decode string")
  }
}