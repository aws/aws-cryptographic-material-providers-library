// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;
import software.amazon.cryptography.metrics.IMetricsAgent;
import software.amazon.cryptography.metrics.MetricsAgent;

public class CreateMetricsAgentOutput {

  private final IMetricsAgent metricsAgent;

  protected CreateMetricsAgentOutput(BuilderImpl builder) {
    this.metricsAgent = builder.metricsAgent();
  }

  public IMetricsAgent metricsAgent() {
    return this.metricsAgent;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder metricsAgent(IMetricsAgent metricsAgent);

    IMetricsAgent metricsAgent();

    CreateMetricsAgentOutput build();
  }

  static class BuilderImpl implements Builder {

    protected IMetricsAgent metricsAgent;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateMetricsAgentOutput model) {
      this.metricsAgent = model.metricsAgent();
    }

    public Builder metricsAgent(IMetricsAgent metricsAgent) {
      this.metricsAgent = MetricsAgent.wrap(metricsAgent);
      return this;
    }

    public IMetricsAgent metricsAgent() {
      return this.metricsAgent;
    }

    public CreateMetricsAgentOutput build() {
      if (Objects.isNull(this.metricsAgent())) {
        throw new IllegalArgumentException(
          "Missing value for required field `metricsAgent`"
        );
      }
      return new CreateMetricsAgentOutput(this);
    }
  }
}
