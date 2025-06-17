// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "MetricsAgent.dfy"


module MetricsAgentText {
  import opened Types = AwsCryptographyMetricsTypes
  import opened Wrappers
  import opened StandardLibrary.UInt
  import MetricsAgent

  class TextLogger
    extends MetricsAgent.VerifiableInterface
  {
    const fileName: string

    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
    }

    constructor {:extern} {:axiom} (
      fileName: string
    )
      requires |fileName| > 0
      ensures ValidState()
      ensures fresh (Modifies) && fresh(History) 
    {
      this.fileName := fileName;
      History := new Types.IMetricsAgentCallHistory();
      Modifies := {History};
    }

    predicate PutCountEnsuresPublicly(input: Types.PutCountInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Success?
    }
    
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
    {
      var _ := ExternPutCount(
        input.description,
        input.count,
        input.transactionId
      );

      return Success(PutOutput());
    }

    predicate PutDateEnsuresPublicly(input: Types.PutDateInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Success?
    }
    
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
    {
      var _ := ExternPutDate(
        input.description,
        input.date,
        input.transactionId
      );
      return Success(PutOutput());
    }
    
    predicate PutTimeEnsuresPublicly(input: Types.PutTimeInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Success?
    }
    
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
    {
      var _ := ExternPutTime(
        input.description,
        input.duration,
        input.transactionId
      );
      return Success(PutOutput());
    }

    predicate PutPropertyEnsuresPublicly(input: Types.PutPropertyInput , output: Result<Types.PutOutput, Types.Error>)
      : (outcome: bool)
    {
      && output.Success?
    }
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
      {
        var _ := ExternPutProperty(
          input.description,
          input.value,
          input.transactionId
        );
        return Success(PutOutput());
      }
  }

  // Externs
  method {:extern "MetricsAgent.TextLogger", "PutCount"} ExternPutCount(
    description: string ,
    count: int64 ,
    transactionId: Option<string> := Option.None
  ) returns (res: bool)
  
  method {:extern "MetricsAgent.TextLogger", "PutDate"} ExternPutDate(
    description: string ,
    date: string ,
    transactionId: Option<string> := Option.None
  ) returns (res: bool)
  
  method {:extern "MetricsAgent.TextLogger", "PutTime"} ExternPutTime(
    description: string ,
    duration: int64 ,
    transactionId: Option<string> := Option.None
  ) returns (res: bool)
  
  method {:extern "MetricsAgent.TextLogger", "PutProperty"} ExternPutProperty(
    description: string ,
    value: string ,
    transactionId: Option<string> := Option.None
  ) returns (res: bool)

}