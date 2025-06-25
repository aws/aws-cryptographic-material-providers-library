// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics;

import Wrappers_Compile.Result;
import java.lang.IllegalArgumentException;
import java.util.Objects;
import software.amazon.cryptography.metrics.internaldafny.MetricsClient;
import software.amazon.cryptography.metrics.internaldafny.__default;
import software.amazon.cryptography.metrics.internaldafny.types.Error;
import software.amazon.cryptography.metrics.internaldafny.types.IAwsCryptographicMetricsClient;
import software.amazon.cryptography.metrics.model.CreateMetricsAgentInput;
import software.amazon.cryptography.metrics.model.CreateMetricsAgentOutput;
import software.amazon.cryptography.metrics.model.MetricsConfig;

public class Metrics {

  private final IAwsCryptographicMetricsClient _impl;

  protected Metrics(BuilderImpl builder) {
    MetricsConfig input = builder.MetricsConfig();
    software.amazon.cryptography.metrics.internaldafny.types.MetricsConfig dafnyValue =
      ToDafny.MetricsConfig(input);
    Result<MetricsClient, Error> result = __default.Metrics(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    this._impl = result.dtor_value();
  }

  Metrics(IAwsCryptographicMetricsClient impl) {
    this._impl = impl;
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public CreateMetricsAgentOutput CreateMultiMetricsAgent(
    CreateMetricsAgentInput input
  ) {
    software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentInput dafnyValue =
      ToDafny.CreateMetricsAgentInput(input);
    Result<
      software.amazon.cryptography.metrics.internaldafny.types.CreateMetricsAgentOutput,
      Error
    > result = this._impl.CreateMultiMetricsAgent(dafnyValue);
    if (result.is_Failure()) {
      throw ToNative.Error(result.dtor_error());
    }
    return ToNative.CreateMetricsAgentOutput(result.dtor_value());
  }

  protected IAwsCryptographicMetricsClient impl() {
    return this._impl;
  }

  public interface Builder {
    Builder MetricsConfig(MetricsConfig MetricsConfig);

    MetricsConfig MetricsConfig();

    Metrics build();
  }

  static class BuilderImpl implements Builder {

    protected MetricsConfig MetricsConfig;

    protected BuilderImpl() {}

    public Builder MetricsConfig(MetricsConfig MetricsConfig) {
      this.MetricsConfig = MetricsConfig;
      return this;
    }

    public MetricsConfig MetricsConfig() {
      return this.MetricsConfig;
    }

    public Metrics build() {
      if (Objects.isNull(this.MetricsConfig())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MetricsConfig`"
        );
      }
      return new Metrics(this);
    }
  }
}
