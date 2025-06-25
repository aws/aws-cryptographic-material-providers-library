// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "MetricsAgentText.dfy"
include "MultiMetricsAgent.dfy"

module AwsCryptographyMetricsOperations refines AbstractAwsCryptographyMetricsOperations {
  import opened StandardLibrary.MemoryMath
  
  import UUID
  import MetricsAgentText
  import MultiMetricsAgent

  datatype Config = Config()
  type InternalConfig = Config
  
  predicate ValidInternalConfig?(config: InternalConfig)
  {true}

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {{}}
  
  predicate CreateMultiMetricsAgentEnsuresPublicly(input: CreateMetricsAgentInput , output: Result<CreateMetricsAgentOutput, Error>)
  {true}

  method CreateMultiMetricsAgent(config: InternalConfig, input: CreateMetricsAgentInput)
    returns (output: Result<CreateMetricsAgentOutput, Error>)
  {
    SequenceIsSafeBecauseItIsInMemory(input.metricsAgents);
    :- Need(|input.metricsAgents| as uint64 > 0,
            Types.MetricsServiceError(
              message := "Configuration Error: MUST provide at least one MetricsAgent"));

    var metricsAgent := new MultiMetricsAgent.MultiMetricsAgent(input.metricsAgents);
  
    return Success(CreateMetricsAgentOutput(metricsAgent := metricsAgent));
  }
}