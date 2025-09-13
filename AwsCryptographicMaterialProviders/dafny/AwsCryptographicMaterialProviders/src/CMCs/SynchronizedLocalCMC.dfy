// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "LocalCMC.dfy"

module {:options "/functionSyntax:4" } {:extern "software.amazon.cryptography.internaldafny.SynchronizedLocalCMC" } SynchronizedLocalCMC {
  import opened Wrappers
  import Types = AwsCryptographyMaterialProvidersTypes
  import LocalCMC

  class {:extern} SynchronizedLocalCMC extends Types.ICryptographicMaterialsCache {

    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies && this in Modifies
    {
      && History in Modifies
      && this in Modifies
    }

    ghost predicate InternalValidState()
      reads this`InternalModifies, InternalModifies
      ensures InternalValidState() ==> History !in InternalModifies
    {
      && History !in InternalModifies
    }

    constructor {:extern} (
      wrapped: LocalCMC.LocalCMC
    )
      ensures
        && ValidState()
        && fresh(this.Modifies)


    ghost predicate GetCacheEntryEnsuresPublicly(input: Types.GetCacheEntryInput, output: Result<Types.GetCacheEntryOutput, Types.Error>)
    {true}

    method {:extern "GetCacheEntry"}  GetCacheEntry'(input: Types.GetCacheEntryInput)
      returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()

      // ensures output.Failure? ==> input.identifier !in cache
      ensures GetCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)

    ghost predicate PutCacheEntryEnsuresPublicly(input: Types.PutCacheEntryInput, output: Result<(), Types.Error>)
    {true}

    method {:extern "PutCacheEntry"} PutCacheEntry' (input: Types.PutCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()

      ensures PutCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)

    ghost predicate DeleteCacheEntryEnsuresPublicly(input: Types.DeleteCacheEntryInput, output: Result<(), Types.Error>)
    {true}

    method {:extern "DeleteCacheEntry"} DeleteCacheEntry'(input: Types.DeleteCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()

      ensures DeleteCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures InternalModifies <= old(InternalModifies)

    ghost predicate UpdateUsageMetadataEnsuresPublicly(input: Types.UpdateUsageMetadataInput, output: Result<(), Types.Error>)
    {true}

    method {:extern "UpdateUsageMetadata"} UpdateUsageMetadata'(input: Types.UpdateUsageMetadataInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()


  }
}
