// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Keyring.dfy"
include "../Materials.dfy"
include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"

include "RawAESKeyring.dfy"
include "RawECDHKeyring.dfy"
include "RawRSAKeyring.dfy"
include "AwsKms/AwsKmsDiscoveryKeyring.dfy"
include "AwsKms/AwsKmsEcdhKeyring.dfy"
include "AwsKms/AwsKmsHierarchicalKeyring.dfy"
include "AwsKms/AwsKmsKeyring.dfy"
include "AwsKms/AwsKmsMrkDiscoveryKeyring.dfy"
include "AwsKms/AwsKmsMrkKeyring.dfy"
include "AwsKms/AwsKmsRsaKeyring.dfy"

module {:options "-functionSyntax:4"} MultiKeyring {
  import opened StandardLibrary
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyMaterialProvidersTypes
  import Keyring
  import Materials
  import UTF8
  import Seq

  // Rust traits do not have extensive runtime dependency information.
  // This means that in Rust you cannot know that one trait also implements another trait.
  // This is problematic because in Dafny this is trivial,
  // and given how we set up our keyrings and CMMs
  // it is very convenient.
  // By checking `keyring: Types.IKeyring is Keyring.VerifiableInterface`
  // the MultiKeyring can do less work.
  // Because it can prove, via Dafny that some work has already been done.
  // However the above cannot be currently compiled into Rust.
  // This means that to offer this we need to check a different way.
  // The workaround for now is to use list of all know verified keyrings.
  import RawAESKeyring
  import RawECDHKeyring
  import RawRSAKeyring
  import AwsKmsDiscoveryKeyring
  import AwsKmsEcdhKeyring
  import AwsKmsHierarchicalKeyring
  import AwsKmsKeyring
  import AwsKmsMrkDiscoveryKeyring
  import AwsKmsMrkKeyring
  import AwsKmsRsaKeyring

  predicate Verified?(keyring: Types.IKeyring)
    : (outcome: bool)
    ensures outcome ==> keyring is Keyring.VerifiableInterface
  {
    || keyring is RawAESKeyring.RawAESKeyring
    || keyring is RawECDHKeyring.RawEcdhKeyring
    || keyring is RawRSAKeyring.RawRSAKeyring
    || keyring is AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
    || keyring is AwsKmsEcdhKeyring.AwsKmsEcdhKeyring
    || keyring is AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring
    || keyring is AwsKmsKeyring.AwsKmsKeyring
    || keyring is AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring
    || keyring is AwsKmsMrkKeyring.AwsKmsMrkKeyring
    || keyring is AwsKmsRsaKeyring.AwsKmsRsaKeyring
  }


  class MultiKeyring
    extends
      Keyring.VerifiableInterface,
      Types.IKeyring
  {

    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && (generatorKeyring.Some? ==>
            && History !in generatorKeyring.value.Modifies
            && generatorKeyring.value.ValidState()
            && generatorKeyring.value.Modifies <= Modifies)
      && (forall k
            | k in childKeyrings
            ::
              && History !in k.Modifies
              && k.ValidState()
              && k.Modifies <= Modifies)
      && (generatorKeyring.None? ==> 0 < |childKeyrings|)
    }

    const generatorKeyring: Option<Types.IKeyring>
    const childKeyrings: seq<Types.IKeyring>

    constructor (
      generatorKeyring: Option<Types.IKeyring>,
      childKeyrings: seq<Types.IKeyring>
    )
      //= aws-encryption-sdk-specification/framework/multi-keyring.md#inputs
      //= type=implication
      //# On keyring initialization, a keyring MUST define at least one of the
      //# following:
      requires generatorKeyring.Some? || |childKeyrings| > 0

      requires
        && (generatorKeyring.Some? ==> generatorKeyring.value.ValidState())
        && forall k <- childKeyrings :: k.ValidState()

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#generator-keyring
      //= type=implication
      //# If the list of [child keyrings](#child-keyrings) is empty, a [generator
      //# keyring](#generator-keyring) MUST be defined for the keyring.
      requires |childKeyrings| == 0 ==> generatorKeyring.Some?

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#child-keyrings
      //= type=implication
      //# If this keyring does not have a [generator keyring](#generator-keyring),
      //# this list MUST NOT be empty.
      requires generatorKeyring.None? ==> |childKeyrings| > 0

      ensures this.generatorKeyring == generatorKeyring
      ensures this.childKeyrings == childKeyrings
      ensures
        && ValidState()
        && fresh(this)
        && fresh(History)
        && fresh(Modifies - GatherModifies(generatorKeyring, childKeyrings))
    {
      this.generatorKeyring := generatorKeyring;
      this.childKeyrings := childKeyrings;
      History := new Types.IKeyringCallHistory();
      Modifies := {History} + GatherModifies(generatorKeyring, childKeyrings);

      new; // Tells Dafny everything has been initialized after this point

      assert && History in Modifies;
      assert && (generatorKeyring.Some? ==>
                   && History !in generatorKeyring.value.Modifies
                   && generatorKeyring.value.ValidState()
                   && generatorKeyring.value.Modifies <= Modifies);
      assert && (forall k
                   | k in childKeyrings
                   ::
                     && History !in k.Modifies
                     && k.ValidState()
                     && k.Modifies <= Modifies);
    }

    ghost predicate OnEncryptEnsuresPublicly (
      input: Types.OnEncryptInput ,
      output: Result<Types.OnEncryptOutput, Types.Error> )
      : (outcome: bool)
      ensures
        outcome ==>
          output.Success?
          ==>
            && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.materials)
            && Materials.ValidEncryptionMaterialsTransition(
                 input.materials,
                 output.value.materials
               )
    {
      output.Success?
      ==>
        && Materials.EncryptionMaterialsHasPlaintextDataKey(output.value.materials)
        && Materials.ValidEncryptionMaterialsTransition(
             input.materials,
             output.value.materials
           )
    }
    //= aws-encryption-sdk-specification/framework/multi-keyring.md#generator-keyring
    //= type=implication
    //# This keyring MUST implement the [Generate Data Key](keyring-
    //# interface.md#generate-data-key) behavior during [OnEncrypt](keyring-
    //# interface.md#onencrypt).
    method OnEncrypt'(input: Types.OnEncryptInput)
      returns (res: Result<Types.OnEncryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnEncryptEnsuresPublicly(input, res)
      ensures unchanged(History)

      ensures res.Success?
              ==>
                && Materials.ValidEncryptionMaterialsTransition(
                  input.materials,
                  res.value.materials
                )

      ensures res.Success? ==>
                //= aws-encryption-sdk-specification/framework/multi-keyring.md#generator-keyring
                //= type=implication
                //# This means that this keyring MUST return
                //# [encryption materials](structures.md#encryption-materials) containing
                //# a plaintext data key on [OnEncrypt](keyring-interface.md#onencrypt).
                && res.value.materials.plaintextDataKey.Some?

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
      //= type=implication
      //# If this keyring does not have a [generator keyring](#generator-keyring),
      //# and the input [encryption materials](structures.md#encryption-
      //# materials) does not include a plaintext data key, OnEncrypt MUST
      //# fail.
      ensures
        && this.generatorKeyring.None?
        && input.materials.plaintextDataKey.None?
        ==> res.Failure?

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
      //= type=implication
      //# - If the input encryption materials already include a plaintext data
      //# key, OnEncrypt MUST fail.
      ensures
        && this.generatorKeyring.Some?
        && input.materials.plaintextDataKey.Some?
        ==> res.Failure?
    {

      // We could also frame this as "Need", but I found an "if" statement more clearly matches the
      // requirement in the spec ("If this keyring does not have a generator keyring
      // and the input encryption materials does not include a plaintext data key")
      if this.generatorKeyring.None? && input.materials.plaintextDataKey.None? {
        var exception := "Need either a generator keyring or input encryption materials which contain a plaintext data key";
        return Failure(Types.AwsCryptographicMaterialProvidersException( message := exception));
      }

      var returnMaterials := input.materials;

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
      //# If this keyring has a generator keyring, this keyring MUST first
      //# generate a plaintext data key using the generator keyring:
      if this.generatorKeyring.Some? {
        :- Need(input.materials.plaintextDataKey.None?,
                Types.AwsCryptographicMaterialProvidersException( message := "This multi keyring has a generator but provided Encryption Materials already contain plaintext data key"));

        //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
        //# - This keyring MUST first call the generator keyring's OnEncrypt
        //# using the input encryption materials as input.
        var onEncryptOutput := this.generatorKeyring.value.OnEncrypt(input);

          //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
          //# - If the generator keyring fails OnEncrypt, this OnEncrypt MUST also
          //# fail.
        :- Need(onEncryptOutput.Success?,
                if onEncryptOutput.Failure? then onEncryptOutput.error else Types.AwsCryptographicMaterialProvidersException( message := "Unexpected failure. Input to Need is !Success.") );


        // For Dafny these are trivial statements
        // because they implement a trait that ensures this.
        // However not all CMM/keyrings are Dafny CMM/keyrings.
        // Customers can create custom CMM/keyrings.
        if !(
            || Verified?(generatorKeyring.value)
            || generatorKeyring.value is MultiKeyring
          ) {
          //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
          //# - If the generator keyring returns encryption materials missing a
          //# plaintext data key, OnEncrypt MUST fail.
          :- Need(
            Materials.EncryptionMaterialsHasPlaintextDataKey(onEncryptOutput.value.materials),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Could not retrieve materials required for encryption"));

          :- Need(Materials.ValidEncryptionMaterialsTransition(input.materials, onEncryptOutput.value.materials),
                  Types.AwsCryptographicMaterialProvidersException( message := "Generator keyring returned invalid encryption materials"));
        }

        returnMaterials := onEncryptOutput.value.materials;
      }

      SequenceIsSafeBecauseItIsInMemory(this.childKeyrings);
      for i : uint64 := 0 to |this.childKeyrings| as uint64
        invariant 0 == i && this.generatorKeyring.None? ==> returnMaterials == input.materials
        invariant 0 < i || this.generatorKeyring.Some?  ==>
            && Materials.ValidEncryptionMaterialsTransition(input.materials, returnMaterials)
            && Materials.EncryptionMaterialsHasPlaintextDataKey(returnMaterials)
        invariant returnMaterials.plaintextDataKey.Some?
        invariant unchanged(History)
        invariant i as nat < |this.childKeyrings| ==> this.childKeyrings[i].Modifies <= Modifies
      {
        var onEncryptInput := Types.OnEncryptInput(materials := returnMaterials);
        var child: Types.IKeyring := this.childKeyrings[i];

        //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
        //# Next, for each [keyring](keyring-interface.md) in this keyring's list
        //# of [child keyrings](#child-keyrings), the keyring MUST call [OnEncrypt]
        //# (keyring-interface.md#onencrypt).
        var onEncryptOutput := child.OnEncrypt(onEncryptInput);

          //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
          //# If the child keyring's [OnEncrypt](keyring-
          //# interface.md#onencrypt) fails, this OnEncrypt MUST also fail.
        :- Need(onEncryptOutput.Success?,
                Types.AwsCryptographicMaterialProvidersException( message := "Child keyring failed to encrypt plaintext data key"));

        // For Dafny these are trivial statements
        // because they implement a trait that ensures this.
        // However not all CMM/keyrings are Dafny CMM/keyrings.
        // Customers can create custom CMM/keyrings.
        if !(
            || Verified?(child)
            || child is MultiKeyring
          ) {
          // We have to explicitly check for this because our child and generator keyrings are of type
          // IKeyring, rather than VerifiableKeyring.
          // If we knew we would always have VerifiableKeyrings, we would get this for free.
          // However, we want to support customer implementations of keyrings which may or may
          // not perform valid transitions.

          :- Need(
            Materials.EncryptionMaterialsHasPlaintextDataKey(onEncryptOutput.value.materials),
            Types.AwsCryptographicMaterialProvidersException(
              message := "Could not retrieve materials required for encryption"));

          :- Need(Materials.ValidEncryptionMaterialsTransition(returnMaterials, onEncryptOutput.value.materials),
                  Types.AwsCryptographicMaterialProvidersException( message := "Child keyring performed invalid transition on encryption materials"));
        }

        returnMaterials := onEncryptOutput.value.materials;
      }

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#onencrypt
      //# If all previous [OnEncrypt](keyring-interface.md#onencrypt) calls
      //# succeeded, this keyring MUST return the [encryption materials]
      //# (structures.md#encryption-materials) returned by the last OnEncrypt
      //# call.
      return Success(Types.OnEncryptOutput(materials := returnMaterials));
    }

    ghost predicate OnDecryptEnsuresPublicly ( input: Types.OnDecryptInput , output: Result<Types.OnDecryptOutput, Types.Error> )
      : (outcome: bool)
      ensures
        outcome ==>
          output.Success?
          ==>
            && Materials.DecryptionMaterialsTransitionIsValid(
              input.materials,
              output.value.materials
            )
    {
      output.Success?
      ==>
        && Materials.DecryptionMaterialsTransitionIsValid(
          input.materials,
          output.value.materials
        )
    }
    /*
     * OnDecrypt
     */
    method OnDecrypt'(input: Types.OnDecryptInput)
      returns (res: Result<Types.OnDecryptOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures OnDecryptEnsuresPublicly(input, res)
      ensures unchanged(History)
      ensures res.Success?
              ==>
                && Materials.DecryptionMaterialsTransitionIsValid(
                  input.materials,
                  res.value.materials
                )

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
      //= type=implication
      //# If the decryption materials already contain a plaintext data key, the
      //# keyring MUST fail and MUST NOT modify the [decryption materials]
      //# (structures.md#decryption-materials).
      // The "MUST NOT modify" clause is true because objects are immutable in Dafny.
      ensures Materials.DecryptionMaterialsWithPlaintextDataKey(input.materials) ==> res.Failure?
    {
      // We won't actually be returning these materials, but it's useful to have a reference to them
      // for proving things (for example, proving we never enter a state where we get a plaintext data
      // key from a child keyring and DON'T return it)
      var materials := input.materials;

      :- Need(Materials.DecryptionMaterialsWithoutPlaintextDataKey(input.materials),
              Types.AwsCryptographicMaterialProvidersException( message := "Keyring received decryption materials that already contain a plaintext data key."));

      // Failure messages will be collected here
      var failures : seq<Types.Error> := [];

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
      //# Otherwise, OnDecrypt MUST first attempt to decrypt the [encrypted data
      //# keys](structures.md#encrypted-data-keys-1) in the input [decryption
      //# materials](structures.md#decryption-materials) using its [generator
      //# keyring](#generator-keyring).
      if this.generatorKeyring.Some? {
        var result := AttemptDecryptDataKey(this.generatorKeyring.value, input);

        if result.Success? {
          if result.value.materials.plaintextDataKey.Some? {
            return Success(result.value);
          }
        } else {
          failures := failures + [result.error];
        }
      }

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
      //# If the generator keyring is unable to
      //# decrypt the materials, the multi-keyring MUST attempt to decrypt
      //# using its child keyrings, until one either succeeds in decryption or
      //# all have failed.
      SequenceIsSafeBecauseItIsInMemory(this.childKeyrings);
      for j : uint64 := 0 to |this.childKeyrings| as uint64
        invariant Materials.DecryptionMaterialsWithoutPlaintextDataKey(materials)
        invariant unchanged(History)
      {

        //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
        //# For each [keyring](keyring-interface.md) to be used for decryption,
        //# the multi-keyring MUST call that keyring's [OnDecrypt](keyring-
        //# interface.md#ondecrypt) using the unmodified [decryption materials]
        //# (structures.md#decryption-materials) and the input [encrypted data key]
        //# (structures.md#encrypted-data-key) list.
        var result := AttemptDecryptDataKey(this.childKeyrings[j], input);

        if result.Success? {
          //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
          //# If [OnDecrypt](keyring-
          //# interface.md#ondecrypt) returns [decryption materials]
          //# (structures.md#decryption-materials) containing a plaintext data key,
          //# the multi-keyring MUST immediately return the modified decryption
          //# materials.
          // We don't explicitly check for "containing a plaintext data key"
          // because AttemptDecryptDataKey has a post-condition ensuring that
          // if the call is successful, the result has a plaintext data key
          return Success(result.value);
        } else {
          //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
          //# If the child keyring's OnDecrypt call fails, the multi-
          //# keyring MUST collect the error and continue to the next keyring, if
          //# any.
          failures := failures + [result.error];
        }
      }

      //= aws-encryption-sdk-specification/framework/multi-keyring.md#ondecrypt
      //# If, after calling [OnDecrypt](keyring-interface.md#ondecrypt) on every
      //# [child keyring](#child-keyrings) (and possibly the [generator keyring]
      //# (#generator-keyring)), the [decryption materials](structures.md#decryption-
      //# materials) still do not contain a plaintext data key, OnDecrypt MUST
      //# return a failure message containing the collected failure messages
      //# from the child keyrings.
      // Note that the annotation says this should only happen if there is no
      // plaintext data key. From our proofs above (the loop invariant of
      // DecryptionMaterialsWithoutPlaintextDataKey), we know that the *only*
      // way to get to this place is if there is no plaintext data key, so we
      // omit the 'if' statement checking for it.
      var combinedResult := Types.CollectionOfErrors( list := failures,
                                                      message := "No Configured Keyring was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.");
      return Failure(combinedResult);
    }
  }

  method AttemptDecryptDataKey(keyring: Types.IKeyring, input: Types.OnDecryptInput)
    returns (res: Result<Types.OnDecryptOutput, Types.Error>)
    requires keyring.ValidState()
    modifies keyring.Modifies
    ensures keyring.ValidState()
    ensures res.Success?
            ==> && res.value.materials.plaintextDataKey.Some?
                && Materials.DecryptionMaterialsTransitionIsValid(input.materials, res.value.materials)
  {
    var output :- keyring.OnDecrypt(input);

    // For Dafny these are trivial statements
    // because they implement a trait that ensures this.
    // However not all CMM/keyrings are Dafny CMM/keyrings.
    // Customers can create custom CMM/keyrings.
    if !(
        || Verified?(keyring)
        || keyring is MultiKeyring
      ) {
      :- Need(
        Materials.DecryptionMaterialsTransitionIsValid(input.materials, output.materials),
        Types.AwsCryptographicMaterialProvidersException( message := "Keyring performed invalid material transition")
      );
    }
    return Success(output);
  }

  // This is a helper to gather
  // all the `Modifies` sets together
  // for Dafny.
  // Makes the code in the constructor
  // a little more readable.
  ghost function GatherModifies(
    generatorKeyring: Option<Types.IKeyring>,
    childKeyrings: seq<Types.IKeyring>
  ):
    (mod: set<object>)
  {
    (
      set m: object, k: Types.IKeyring
        |
        && k in childKeyrings
        && m in k.Modifies
        :: m
    )
    + (
      if generatorKeyring.Some? then
        generatorKeyring.value.Modifies
      else
        {}
    )
  }
}
