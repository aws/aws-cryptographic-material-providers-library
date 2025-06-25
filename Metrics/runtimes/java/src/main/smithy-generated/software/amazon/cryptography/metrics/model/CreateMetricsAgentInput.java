// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.List;
import java.util.Objects;
import software.amazon.cryptography.metrics.IMetricsAgent;

public class CreateMetricsAgentInput {

  private final List<IMetricsAgent> metricsAgents;

  protected CreateMetricsAgentInput(BuilderImpl builder) {
    this.metricsAgents = builder.metricsAgents();
  }

  public List<IMetricsAgent> metricsAgents() {
    return this.metricsAgents;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder metricsAgents(List<IMetricsAgent> metricsAgents);

    List<IMetricsAgent> metricsAgents();

    CreateMetricsAgentInput build();
  }

  static class BuilderImpl implements Builder {

    protected List<IMetricsAgent> metricsAgents;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateMetricsAgentInput model) {
      this.metricsAgents = model.metricsAgents();
    }

    public Builder metricsAgents(List<IMetricsAgent> metricsAgents) {
      this.metricsAgents = metricsAgents;
      return this;
    }

    public List<IMetricsAgent> metricsAgents() {
      return this.metricsAgents;
    }

    public CreateMetricsAgentInput build() {
      if (Objects.isNull(this.metricsAgents())) {
        throw new IllegalArgumentException(
          "Missing value for required field `metricsAgents`"
        );
      }
      return new CreateMetricsAgentInput(this);
    }
  }
}
