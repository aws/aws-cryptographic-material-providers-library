// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "MetricsAgent.dfy"

module {:options "-functionSyntax:4"} MultiMetricsAgent {
  import opened StandardLibrary
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyMetricsTypes
  import UTF8
  import Seq
  import MetricsAgent

  class MultiMetricsAgent
    extends
      MetricsAgent.VerifiableInterface,
      Types.IMetricsAgent
  {
    ghost predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && (forall m
            | m in metricsAgents
            ::
              && History !in m.Modifies
              && m.ValidState()
              && m.Modifies <= Modifies)
    }
    
    const metricsAgents: seq<Types.IMetricsAgent>

    constructor (
      metricsAgents: seq<Types.IMetricsAgent>
    )
      requires |metricsAgents| > 0
      requires
        && forall m <- metricsAgents :: m.ValidState()

      ensures this.metricsAgents == metricsAgents
      ensures
        && ValidState()
        && fresh(this)
        && fresh(History)
        && fresh(Modifies - GatherModifies(metricsAgents))
    {
      this.metricsAgents := metricsAgents;
      History := new Types.IMetricsAgentCallHistory();
      Modifies := {History} + GatherModifies(metricsAgents);

      new; // Tells Dafny everything has been initialized after this point

      assert && History in Modifies;
      assert && (forall k
                   | k in metricsAgents
                   ::
                     && History !in k.Modifies
                     && k.ValidState()
                     && k.Modifies <= Modifies);
    }
    
    ghost predicate PutCountEnsuresPublicly(input: Types.PutCountInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Failure?
    }
    
    method PutCount' ( input: Types.PutCountInput )
      returns (output: Result<Types.PutOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutCountEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      return Failure(Types.MetricsServiceError(message := "E")); 
    }

    ghost predicate PutDateEnsuresPublicly(input: Types.PutDateInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Failure?
    }
    
    method PutDate' ( input: Types.PutDateInput )
      returns (output: Result<Types.PutOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutDateEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      return Failure(Types.MetricsServiceError(message := "E")); 
    }
    
    ghost predicate PutTimeEnsuresPublicly(input: Types.PutTimeInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Failure?
    }
    
    method PutTime' ( input: Types.PutTimeInput )
      returns (output: Result<Types.PutOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutTimeEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      return Failure(Types.MetricsServiceError(message := "E")); 
    }

    ghost predicate PutPropertyEnsuresPublicly(input: Types.PutPropertyInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Failure?
    }
    method PutProperty' ( input: Types.PutPropertyInput )
      returns (output: Result<Types.PutOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutPropertyEnsuresPublicly(input, output)
      ensures unchanged(History)
      {
        return Failure(Types.MetricsServiceError(message := "E")); 
      }
    
    // This is a helper to gather
    // all the `Modifies` sets together
    // for Dafny.
    // Makes the code in the constructor
    // a little more readable.
    ghost function GatherModifies(
      metricsAgents: seq<Types.IMetricsAgent>
    ):
      (mod: set<object>)
    {
      (
        set o: object, m: Types.IMetricsAgent
          |
          && m in metricsAgents
          && o in m.Modifies
          :: o
      )
    }
  }
}
