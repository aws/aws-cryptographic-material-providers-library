// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTestVectorKeysTypes.dfy"
include "KeyMaterial.dfy"

module {:options "-functionSyntax:4"} CreateStaticCMCs {
  import opened AwsCryptographyMaterialProvidersTypes
  import opened Wrappers
  import opened StandardLibrary.UInt
  import KeyMaterial
  import Time

  datatype Identifier =
    | GetIdentifier(
        identifier: seq<uint8>
      )
    | PutIdentifier(
        identifier: seq<uint8>
      )
    | Identifiers (
        getIdentifier: seq<uint8>,
        putIdentifier: seq<uint8>
      )

  datatype StaticCMCEntry = StaticCMCEntry (
    materials: Materials,
    identifier: Identifier
  )

  method CreateStaticCMC(
    entry : Option<StaticCMCEntry>
  )
    returns (cmc: ICryptographicMaterialsCache)
    // requires staticKeyMaterial.StaticMaterial?
    ensures
      && cmc.ValidState()
      && fresh(cmc) && fresh(cmc.Modifies)
      && cmc.Modifies == {cmc.History}
      && cmc is StaticCMC
  {
    return new StaticCMC(entry);
  }

  class StaticCMC extends ICryptographicMaterialsCache
  {
    constructor( entry : Option<StaticCMCEntry>)
      ensures
        && ValidState()
        && fresh(History)
        && fresh(Modifies)
    {

      staticEntry := entry;
      History := new ICryptographicMaterialsCacheCallHistory();
      Modifies := {History};
    }

    const staticEntry: Option<StaticCMCEntry>

    function GetIdentifier()
      : Option<seq<uint8>>
    {
      if staticEntry.Some? then
        match staticEntry.value.identifier
        case GetIdentifier(g) => Some(g)
        case Identifiers(g,_) => Some(g)
        case PutIdentifier(_) => Wrappers.None
      else
        Wrappers.None
    }

    function PutIdentifier()
      : Option<seq<uint8>>
    {
      if staticEntry.Some? then
        match staticEntry.value.identifier
        case GetIdentifier(_) => Wrappers.None
        case Identifiers(_,p) => Some(p)
        case PutIdentifier(p) => Some(p)
      else
        Wrappers.None
    }


    ghost predicate ValidState()
      reads this`Modifies, Modifies - {History}
      ensures ValidState() ==> History in Modifies
    {
      && Modifies == {History}
    }

    // These are the supported Static information

    ghost predicate PutCacheEntryEnsuresPublicly(input: PutCacheEntryInput , output: Result<(), Error>)
    {true}

    method PutCacheEntry' ( input: PutCacheEntryInput )
      returns (output: Result<(), Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      var identifier := PutIdentifier();
      if identifier.Some? {
        expect input.identifier == identifier.value;
      }
      output := Success(());
    }

    ghost predicate GetCacheEntryEnsuresPublicly(input: GetCacheEntryInput , output: Result<GetCacheEntryOutput, Error>)
    {true}

    method GetCacheEntry' ( input: GetCacheEntryInput )
      returns (output: Result<GetCacheEntryOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
    {

      var identifier := GetIdentifier();
      if identifier.Some? {
        expect input.identifier == identifier.value;

        var now := Time.GetCurrent();
        var range: BoundedInts.int64 := 10;

        expect 0 < now - range;
        expect now < INT64_MAX_LIMIT as BoundedInts.int64  - range;

        var creationTime := now - range; // always in the past;
        var expiryTime := now + range; // alway in the future;

        output := Success(
          GetCacheEntryOutput(
            materials := staticEntry.value.materials,
            creationTime := creationTime,
            expiryTime := expiryTime,
            messagesUsed := range as BoundedInts.int32,
            bytesUsed := range
          )
        );
      } else {
        output := Failure(EntryDoesNotExist(message := "Entry does not exist"));
      }
    }



    // These are all not supported operations in a static context

    ghost predicate UpdateUsageMetadataEnsuresPublicly(input: UpdateUsageMetadataInput , output: Result<(), Error>)
    {true}

    method UpdateUsageMetadata' ( input: UpdateUsageMetadataInput )
      returns (output: Result<(), Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures UpdateUsageMetadataEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      output := Failure(
        AwsCryptographicMaterialProvidersException(
          message := "UpdateUsageMetadata is not supported for StaticCMC"
        ));
    }

    ghost predicate DeleteCacheEntryEnsuresPublicly(input: DeleteCacheEntryInput , output: Result<(), Error>)
    {true}

    method DeleteCacheEntry' ( input: DeleteCacheEntryInput )
      returns (output: Result<(), Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DeleteCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      output := Failure(
        AwsCryptographicMaterialProvidersException(
          message := "DeleteCacheEntry is not supported for StaticCMC"
        ));
    }

  }
}
