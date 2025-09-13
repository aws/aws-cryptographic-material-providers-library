// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "StormTracker.dfy"

module {:options "/functionSyntax:4" } {:extern "software.amazon.cryptography.internaldafny.StormTrackingCMC" } StormTrackingCMC {
  import opened Wrappers
  import Types = AwsCryptographyMaterialProvidersTypes
  import StormTracker

  class {:extern} StormTrackingCMC extends Types.ICryptographicMaterialsCache {

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
      wrapped: StormTracker.StormTracker
    )
      ensures
        && ValidState()
        && InternalValidState()
        && fresh(this.Modifies)
        && fresh(this.InternalModifies)


    ghost predicate GetCacheEntryEnsuresPublicly(input: Types.GetCacheEntryInput, output: Result<Types.GetCacheEntryOutput, Types.Error>)
    {true}

    method {:extern "GetCacheEntry"}  GetCacheEntry'(input: Types.GetCacheEntryInput)
      returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
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

  // The next two functions are for the benefit of the extern implementation to call,
  // avoiding direct references to generic datatype constructors
  // since their calling pattern is different between different versions of Dafny
  // (i.e. after 4.2, explicit type descriptors are required).

  function CreateGetCacheEntrySuccess(output: Types.GetCacheEntryOutput): Result<Types.GetCacheEntryOutput, Types.Error> {
    Success(output)
  }

  function CreateGetCacheEntryFailure(error: Types.Error): Result<Types.GetCacheEntryOutput, Types.Error> {
    Failure(error)
  }
}
