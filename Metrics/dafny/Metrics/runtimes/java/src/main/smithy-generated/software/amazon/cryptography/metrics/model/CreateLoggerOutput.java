// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;
import software.amazon.cryptography.metrics.ILogger;
import software.amazon.cryptography.metrics.Logger;

public class CreateLoggerOutput {

  private final ILogger logger;

  protected CreateLoggerOutput(BuilderImpl builder) {
    this.logger = builder.logger();
  }

  public ILogger logger() {
    return this.logger;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder logger(ILogger logger);

    ILogger logger();

    CreateLoggerOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ILogger logger;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateLoggerOutput model) {
      this.logger = model.logger();
    }

    public Builder logger(ILogger logger) {
      this.logger = Logger.wrap(logger);
      return this;
    }

    public ILogger logger() {
      return this.logger;
    }

    public CreateLoggerOutput build() {
      if (Objects.isNull(this.logger())) {
        throw new IllegalArgumentException(
          "Missing value for required field `logger`"
        );
      }
      return new CreateLoggerOutput(this);
    }
  }
}
