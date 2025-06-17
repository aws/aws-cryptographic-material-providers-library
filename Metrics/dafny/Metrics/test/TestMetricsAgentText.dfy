// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"

module TestMetricsAgentText {
  import opened Wrappers
  import Types = AwsCryptographyMetricsTypes
  import Metrics
  import UUID

  method {:test} TestCreateTextMetricsAgent()
  {
    var metrics :- expect Metrics.MetricsLogger();

    var fileName :- expect UUID.GenerateUUID();
    assume {:axiom} metrics.ValidState();

    var metricAgent := metrics.CreateTextMetricsAgent(
      Types.CreateTextMetricsAgentInput(
        fileName := fileName
      )
    );
  }
}
