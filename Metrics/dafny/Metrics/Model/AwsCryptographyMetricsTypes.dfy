// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
module {:extern "software.amazon.cryptography.metrics.internaldafny.types" } AwsCryptographyMetricsTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types

  class IAwsCryptographicMetricsClientCallHistory {
    ghost constructor() {
      CreateTextMetricsAgent := [];
      CreateMultiMetricsAgent := [];
    }
    ghost var CreateTextMetricsAgent: seq<DafnyCallEvent<CreateTextMetricsAgentInput, Result<CreateMetricsAgentOutput, Error>>>
    ghost var CreateMultiMetricsAgent: seq<DafnyCallEvent<CreateMetricsAgentInput, Result<CreateMetricsAgentOutput, Error>>>
  }
  trait {:termination false} IAwsCryptographicMetricsClient
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: IAwsCryptographicMetricsClientCallHistory
    predicate CreateTextMetricsAgentEnsuresPublicly(input: CreateTextMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
    // The public method to be called by library consumers
    method CreateTextMetricsAgent ( input: CreateTextMetricsAgentInput )
      returns (output: Result<CreateMetricsAgentOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateTextMetricsAgent
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.metricsAgent.ValidState()
               && output.value.metricsAgent.Modifies !! {History}
               && fresh(output.value.metricsAgent)
               && fresh ( output.value.metricsAgent.Modifies
                          - Modifies - {History} ) )
      ensures CreateTextMetricsAgentEnsuresPublicly(input, output)
      ensures History.CreateTextMetricsAgent == old(History.CreateTextMetricsAgent) + [DafnyCallEvent(input, output)]

    predicate CreateMultiMetricsAgentEnsuresPublicly(input: CreateMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
    // The public method to be called by library consumers
    method CreateMultiMetricsAgent ( input: CreateMetricsAgentInput )
      returns (output: Result<CreateMetricsAgentOutput, Error>)
      requires
        && ValidState() && ( forall i <- input.metricsAgents ::
                               && i.ValidState()
                               && i.Modifies !! {History}
           )
      modifies Modifies - {History} ,
               (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m) ,
               History`CreateMultiMetricsAgent
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History} ,
                (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m)
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.metricsAgent.ValidState()
               && output.value.metricsAgent.Modifies !! {History}
               && fresh(output.value.metricsAgent)
               && fresh ( output.value.metricsAgent.Modifies
                          - Modifies - {History}
                          - (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m) ) )
      ensures CreateMultiMetricsAgentEnsuresPublicly(input, output)
      ensures History.CreateMultiMetricsAgent == old(History.CreateMultiMetricsAgent) + [DafnyCallEvent(input, output)]

  }
  datatype CreateLoggerOutput = | CreateLoggerOutput (
    nameonly logger: ILogger
  )
  datatype CreateMetricsAgentInput = | CreateMetricsAgentInput (
    nameonly metricsAgents: MetricsAgentList
  )
  datatype CreateMetricsAgentOutput = | CreateMetricsAgentOutput (
    nameonly metricsAgent: IMetricsAgent
  )
  datatype CreateTextLoggerInput = | CreateTextLoggerInput (
    nameonly fileName: Option<string> := Option.None
  )
  datatype CreateTextMetricsAgentInput = | CreateTextMetricsAgentInput (
    nameonly fileName: string
  )
  type MetricsAgentList = seq<IMetricsAgent>
  class IMetricsAgentCallHistory {
    ghost constructor() {
      PutCount := [];
      PutDate := [];
      PutTime := [];
      PutProperty := [];
    }
    ghost var PutCount: seq<DafnyCallEvent<PutCountInput, Result<PutOutput, Error>>>
    ghost var PutDate: seq<DafnyCallEvent<PutDateInput, Result<PutOutput, Error>>>
    ghost var PutTime: seq<DafnyCallEvent<PutTimeInput, Result<PutOutput, Error>>>
    ghost var PutProperty: seq<DafnyCallEvent<PutPropertyInput, Result<PutOutput, Error>>>
  }
  trait {:termination false} IMetricsAgent
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: IMetricsAgentCallHistory
    predicate PutCountEnsuresPublicly(input: PutCountInput , output: Result<PutOutput, Error>)
    // The public method to be called by library consumers
    method PutCount ( input: PutCountInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`PutCount
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutCountEnsuresPublicly(input, output)
      ensures History.PutCount == old(History.PutCount) + [DafnyCallEvent(input, output)]
    {
      output := PutCount' (input);
      History.PutCount := History.PutCount + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method PutCount' ( input: PutCountInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutCountEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate PutDateEnsuresPublicly(input: PutDateInput , output: Result<PutOutput, Error>)
    // The public method to be called by library consumers
    method PutDate ( input: PutDateInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`PutDate
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutDateEnsuresPublicly(input, output)
      ensures History.PutDate == old(History.PutDate) + [DafnyCallEvent(input, output)]
    {
      output := PutDate' (input);
      History.PutDate := History.PutDate + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method PutDate' ( input: PutDateInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutDateEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate PutTimeEnsuresPublicly(input: PutTimeInput , output: Result<PutOutput, Error>)
    // The public method to be called by library consumers
    method PutTime ( input: PutTimeInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`PutTime
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutTimeEnsuresPublicly(input, output)
      ensures History.PutTime == old(History.PutTime) + [DafnyCallEvent(input, output)]
    {
      output := PutTime' (input);
      History.PutTime := History.PutTime + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method PutTime' ( input: PutTimeInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutTimeEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate PutPropertyEnsuresPublicly(input: PutPropertyInput , output: Result<PutOutput, Error>)
    // The public method to be called by library consumers
    method PutProperty ( input: PutPropertyInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`PutProperty
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutPropertyEnsuresPublicly(input, output)
      ensures History.PutProperty == old(History.PutProperty) + [DafnyCallEvent(input, output)]
    {
      output := PutProperty' (input);
      History.PutProperty := History.PutProperty + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method PutProperty' ( input: PutPropertyInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutPropertyEnsuresPublicly(input, output)
      ensures unchanged(History)

  }
  datatype MetricsConfig = | MetricsConfig (

                           )
  class ILoggerCallHistory {
    ghost constructor() {
      Put := [];
      Publish := [];
    }
    ghost var Put: seq<DafnyCallEvent<PutInput, Result<PutOutput, Error>>>
    ghost var Publish: seq<DafnyCallEvent<PublishInput, Result<PublishOutput, Error>>>
  }
  trait {:termination false} ILogger
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: ILoggerCallHistory
    predicate PutEnsuresPublicly(input: PutInput , output: Result<PutOutput, Error>)
    // The public method to be called by library consumers
    method Put ( input: PutInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Put
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutEnsuresPublicly(input, output)
      ensures History.Put == old(History.Put) + [DafnyCallEvent(input, output)]
    {
      output := Put' (input);
      History.Put := History.Put + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method Put' ( input: PutInput )
      returns (output: Result<PutOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PutEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate PublishEnsuresPublicly(input: PublishInput , output: Result<PublishOutput, Error>)
    // The public method to be called by library consumers
    method Publish ( input: PublishInput )
      returns (output: Result<PublishOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`Publish
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PublishEnsuresPublicly(input, output)
      ensures History.Publish == old(History.Publish) + [DafnyCallEvent(input, output)]
    {
      output := Publish' (input);
      History.Publish := History.Publish + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method Publish' ( input: PublishInput )
      returns (output: Result<PublishOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures PublishEnsuresPublicly(input, output)
      ensures unchanged(History)

  }
  datatype PublishInput = | PublishInput (

                          )
  datatype PublishOutput = | PublishOutput (

                           )
  datatype PutCountInput = | PutCountInput (
    nameonly description: string ,
    nameonly count: int64 ,
    nameonly transactionId: Option<string> := Option.None
  )
  datatype PutDateInput = | PutDateInput (
    nameonly description: string ,
    nameonly date: string ,
    nameonly transactionId: Option<string> := Option.None
  )
  datatype PutInput = | PutInput (
    nameonly message: string
  )
  datatype PutOutput = | PutOutput (

                       )
  datatype PutPropertyInput = | PutPropertyInput (
    nameonly description: string ,
    nameonly value: string ,
    nameonly transactionId: Option<string> := Option.None
  )
  datatype PutTimeInput = | PutTimeInput (
    nameonly description: string ,
    nameonly duration: int64 ,
    nameonly transactionId: Option<string> := Option.None
  )
  datatype Error =
      // Local Error structures are listed here
    | MetricsPublishError (
        nameonly message: string
      )
    | MetricsPutError (
        nameonly message: string
      )
    | MetricsServiceError (
        nameonly message: string
      )
      // Any dependent models are listed here

      // The Collection error is used to collect several errors together
      // This is useful when composing OR logic.
      // Consider the following method:
      // 
      // method FN<I, O>(n:I)
      //   returns (res: Result<O, Types.Error>)
      //   ensures A(I).Success? ==> res.Success?
      //   ensures B(I).Success? ==> res.Success?
      //   ensures A(I).Failure? && B(I).Failure? ==> res.Failure?
      // 
      // If either A || B is successful then FN is successful.
      // And if A && B fail then FN will fail.
      // But what information should FN transmit back to the caller?
      // While it may be correct to hide these details from the caller,
      // this can not be the globally correct option.
      // Suppose that A and B can be blocked by different ACLs,
      // and that their representation of I is only eventually consistent.
      // How can the caller distinguish, at a minimum for logging,
      // the difference between the four failure modes?
    // || (!access(A(I)) && !access(B(I)))
    // || (!exit(A(I)) && !exit(B(I)))
    // || (!access(A(I)) && !exit(B(I)))
    // || (!exit(A(I)) && !access(B(I)))
    | CollectionOfErrors(list: seq<Error>, nameonly message: string)
      // The Opaque error, used for native, extern, wrapped or unknown errors
    | Opaque(obj: object)
      // A better Opaque, with a visible string representation.
    | OpaqueWithText(obj: object, objMessage : string)
  type OpaqueError = e: Error | e.Opaque? || e.OpaqueWithText? witness *
  // This dummy subset type is included to make sure Dafny
  // always generates a _ExternBase___default.java class.
  type DummySubsetType = x: int | IsDummySubsetType(x) witness 1
  predicate method IsDummySubsetType(x: int) {
    0 < x
  }

}
abstract module AbstractAwsCryptographyMetricsService
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyMetricsTypes
  import Operations : AbstractAwsCryptographyMetricsOperations
  function method DefaultMetricsConfig(): MetricsConfig
  method Metrics(config: MetricsConfig := DefaultMetricsConfig())
    returns (res: Result<MetricsClient, Error>)
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies)
              && fresh(res.value.History)
              && res.value.ValidState()

  // Helper functions for the benefit of native code to create a Success(client) without referring to Dafny internals
  function method CreateSuccessOfClient(client: IAwsCryptographicMetricsClient): Result<IAwsCryptographicMetricsClient, Error> {
    Success(client)
  }
  function method CreateFailureOfError(error: Error): Result<IAwsCryptographicMetricsClient, Error> {
    Failure(error)
  }
  class MetricsClient extends IAwsCryptographicMetricsClient
  {
    constructor(config: Operations.InternalConfig)
      requires Operations.ValidInternalConfig?(config)
      ensures
        && ValidState()
        && fresh(History)
        && this.config == config
    const config: Operations.InternalConfig
    predicate ValidState()
      ensures ValidState() ==>
                && Operations.ValidInternalConfig?(config)
                && History !in Operations.ModifiesInternalConfig(config)
                && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    predicate CreateTextMetricsAgentEnsuresPublicly(input: CreateTextMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
    {Operations.CreateTextMetricsAgentEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateTextMetricsAgent ( input: CreateTextMetricsAgentInput )
      returns (output: Result<CreateMetricsAgentOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateTextMetricsAgent
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.metricsAgent.ValidState()
               && output.value.metricsAgent.Modifies !! {History}
               && fresh(output.value.metricsAgent)
               && fresh ( output.value.metricsAgent.Modifies
                          - Modifies - {History} ) )
      ensures CreateTextMetricsAgentEnsuresPublicly(input, output)
      ensures History.CreateTextMetricsAgent == old(History.CreateTextMetricsAgent) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateTextMetricsAgent(config, input);
      History.CreateTextMetricsAgent := History.CreateTextMetricsAgent + [DafnyCallEvent(input, output)];
    }

    predicate CreateMultiMetricsAgentEnsuresPublicly(input: CreateMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
    {Operations.CreateMultiMetricsAgentEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateMultiMetricsAgent ( input: CreateMetricsAgentInput )
      returns (output: Result<CreateMetricsAgentOutput, Error>)
      requires
        && ValidState() && ( forall i <- input.metricsAgents ::
                               && i.ValidState()
                               && i.Modifies !! {History}
           )
      modifies Modifies - {History} ,
               (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m) ,
               History`CreateMultiMetricsAgent
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History} ,
                (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m)
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.metricsAgent.ValidState()
               && output.value.metricsAgent.Modifies !! {History}
               && fresh(output.value.metricsAgent)
               && fresh ( output.value.metricsAgent.Modifies
                          - Modifies - {History}
                          - (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m) ) )
      ensures CreateMultiMetricsAgentEnsuresPublicly(input, output)
      ensures History.CreateMultiMetricsAgent == old(History.CreateMultiMetricsAgent) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateMultiMetricsAgent(config, input);
      History.CreateMultiMetricsAgent := History.CreateMultiMetricsAgent + [DafnyCallEvent(input, output)];
    }

  }
}
abstract module AbstractAwsCryptographyMetricsOperations {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyMetricsTypes
  type InternalConfig
  predicate ValidInternalConfig?(config: InternalConfig)
  function ModifiesInternalConfig(config: InternalConfig): set<object>
  predicate CreateTextMetricsAgentEnsuresPublicly(input: CreateTextMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
  // The private method to be refined by the library developer


  method CreateTextMetricsAgent ( config: InternalConfig , input: CreateTextMetricsAgentInput )
    returns (output: Result<CreateMetricsAgentOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
      && ( output.Success? ==>
             && output.value.metricsAgent.ValidState()
             && fresh(output.value.metricsAgent)
             && fresh ( output.value.metricsAgent.Modifies
                        - ModifiesInternalConfig(config) ) )
    ensures CreateTextMetricsAgentEnsuresPublicly(input, output)


  predicate CreateMultiMetricsAgentEnsuresPublicly(input: CreateMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
  // The private method to be refined by the library developer


  method CreateMultiMetricsAgent ( config: InternalConfig , input: CreateMetricsAgentInput )
    returns (output: Result<CreateMetricsAgentOutput, Error>)
    requires
      && ValidInternalConfig?(config) && ( forall i <- input.metricsAgents ::
                                             && i.ValidState()
         )
    modifies ModifiesInternalConfig(config) ,
             (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config) ,
              (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m)
    ensures
      && ValidInternalConfig?(config)
      && ( output.Success? ==>
             && output.value.metricsAgent.ValidState()
             && fresh(output.value.metricsAgent)
             && fresh ( output.value.metricsAgent.Modifies
                        - ModifiesInternalConfig(config)
                        - (set m: object, i | i in input.metricsAgents && m in i.Modifies :: m) ) )
    ensures CreateMultiMetricsAgentEnsuresPublicly(input, output)
}
