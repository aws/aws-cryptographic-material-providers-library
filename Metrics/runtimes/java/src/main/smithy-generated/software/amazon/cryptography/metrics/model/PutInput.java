// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;

public class PutInput {

  private final String message;

  protected PutInput(BuilderImpl builder) {
    this.message = builder.message();
  }

  public String message() {
    return this.message;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder message(String message);

    String message();

    PutInput build();
  }

  static class BuilderImpl implements Builder {

    protected String message;

    protected BuilderImpl() {}

    protected BuilderImpl(PutInput model) {
      this.message = model.message();
    }

    public Builder message(String message) {
      this.message = message;
      return this;
    }

    public String message() {
      return this.message;
    }

    public PutInput build() {
      if (Objects.isNull(this.message())) {
        throw new IllegalArgumentException(
          "Missing value for required field `message`"
        );
      }
      return new PutInput(this);
    }
  }
}
