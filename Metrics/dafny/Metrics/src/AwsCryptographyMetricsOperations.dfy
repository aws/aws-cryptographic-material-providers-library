// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"

module AwsCryptographyMetricsOperations refines AbstractAwsCryptographyMetricsOperations {
  import UUID

  datatype Config = Config(
    nameonly MetricsLoggerConfig: MetricsLoggerConfig
  )
  type InternalConfig = Config
  
  predicate ValidInternalConfig?(config: InternalConfig)
  {true}

  function ModifiesInternalConfig(config: InternalConfig) : set<object>
  {{}}

  predicate CreateTextLoggerEnsuresPublicly(input: CreateTextLoggerInput , output: Result<CreateLoggerOutput, Error>)
  {true}

  method CreateTextLogger(config: InternalConfig, input: CreateTextLoggerInput)
    returns (output: Result<CreateLoggerOutput, Error>)
  {
    var fileName;
    if input.fileName.Some? {
      fileName := input.fileName.value;
    } else {
      var fileName? := UUID.GenerateUUID();
      fileName :- fileName?
      // TODO create a generic error here for failing to create a text logger.
      .MapFailure(e => Types.MetricsPutError(message := e));
    }
    // TODO call the create class to get us a TextLogger
    return Failure(Error.MetricsPutError(message := "E"));
  }
}