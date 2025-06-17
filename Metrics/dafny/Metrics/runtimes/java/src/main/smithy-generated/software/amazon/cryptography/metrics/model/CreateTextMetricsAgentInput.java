// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;

public class CreateTextMetricsAgentInput {

  private final String fileName;

  protected CreateTextMetricsAgentInput(BuilderImpl builder) {
    this.fileName = builder.fileName();
  }

  public String fileName() {
    return this.fileName;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder fileName(String fileName);

    String fileName();

    CreateTextMetricsAgentInput build();
  }

  static class BuilderImpl implements Builder {

    protected String fileName;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateTextMetricsAgentInput model) {
      this.fileName = model.fileName();
    }

    public Builder fileName(String fileName) {
      this.fileName = fileName;
      return this;
    }

    public String fileName() {
      return this.fileName;
    }

    public CreateTextMetricsAgentInput build() {
      if (Objects.isNull(this.fileName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `fileName`"
        );
      }
      return new CreateTextMetricsAgentInput(this);
    }
  }
}
