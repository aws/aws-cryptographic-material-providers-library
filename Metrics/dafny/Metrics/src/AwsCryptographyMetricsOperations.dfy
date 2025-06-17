// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "MetricsAgentText.dfy"

module AwsCryptographyMetricsOperations refines AbstractAwsCryptographyMetricsOperations {
  import UUID
  import MetricsAgentText

  datatype Config = Config()
  type InternalConfig = Config
  
  predicate ValidInternalConfig?(config: InternalConfig)
  {true}

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {{}}

  predicate CreateTextMetricsAgentEnsuresPublicly(input: CreateTextMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
  {true}

  method {:axiom} CreateTextMetricsAgent(config: InternalConfig, input: CreateTextMetricsAgentInput)
    returns (output: Result<CreateMetricsAgentOutput, Error>)
  {
    :- Need(
      |input.fileName| > 0,
      Error.MetricsServiceError(message := "Log FileName length MUST be greater than 0.")
    );
    var logger := new MetricsAgentText.TextLogger(input.fileName);
  
    return Success(CreateMetricsAgentOutput(metricsAgent := logger)); 
  }
}