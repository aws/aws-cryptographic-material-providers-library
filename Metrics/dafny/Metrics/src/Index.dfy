// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "AwsCryptographyMetricsOperations.dfy"

module {:extern "software.amazon.cryptography.metrics.internaldafny" } Metrics refines AbstractAwsCryptographyMetricsService {
  import Operations = AwsCryptographyMetricsOperations

  function method DefaultMetricsLoggerConfig(): MetricsLoggerConfig 
  {
    MetricsLoggerConfig()
  }

  method MetricsLogger(config: MetricsLoggerConfig)
    returns (res: Result<MetricsLoggerClient, Error>)
    ensures res.Success? ==>
              && res.value is MetricsLoggerClient
  {
    var logger := new MetricsLoggerClient(
      Operations.Config(
        MetricsLoggerConfig := config
    ));
    return Success(logger);
  }

  class MetricsLoggerClient... {

    predicate ValidState()
    {
      && Operations.ValidInternalConfig?(config)
      && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    }

    constructor(config: Operations.InternalConfig)
    {
      this.config := config;
      History := new IAwsCryptographicMetricsClientCallHistory();
      Modifies := Operations.ModifiesInternalConfig(config) + {History};
    }
  }
}
