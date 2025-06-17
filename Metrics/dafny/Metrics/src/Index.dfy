// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMetricsTypes.dfy"
include "AwsCryptographyMetricsOperations.dfy"

module {:extern "software.amazon.cryptography.metrics.internaldafny" } Metrics refines AbstractAwsCryptographyMetricsService {
  import Operations = AwsCryptographyMetricsOperations

  function method DefaultMetricsConfig(): MetricsConfig 
  {
    MetricsConfig
  }

  method MetricsLogger()
    returns (res: Result<MetricsClient, Error>)
    ensures res.Success? ==>
              && res.value is MetricsClient
  {
    var logger := new MetricsClient(Operations.Config());
    return Success(logger);
  }

  class MetricsClient... {

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
