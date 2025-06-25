// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;

public class PutPropertyInput {

  private final String description;

  private final String value;

  private final String transactionId;

  protected PutPropertyInput(BuilderImpl builder) {
    this.description = builder.description();
    this.value = builder.value();
    this.transactionId = builder.transactionId();
  }

  public String description() {
    return this.description;
  }

  public String value() {
    return this.value;
  }

  public String transactionId() {
    return this.transactionId;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder description(String description);

    String description();

    Builder value(String value);

    String value();

    Builder transactionId(String transactionId);

    String transactionId();

    PutPropertyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String description;

    protected String value;

    protected String transactionId;

    protected BuilderImpl() {}

    protected BuilderImpl(PutPropertyInput model) {
      this.description = model.description();
      this.value = model.value();
      this.transactionId = model.transactionId();
    }

    public Builder description(String description) {
      this.description = description;
      return this;
    }

    public String description() {
      return this.description;
    }

    public Builder value(String value) {
      this.value = value;
      return this;
    }

    public String value() {
      return this.value;
    }

    public Builder transactionId(String transactionId) {
      this.transactionId = transactionId;
      return this;
    }

    public String transactionId() {
      return this.transactionId;
    }

    public PutPropertyInput build() {
      if (Objects.isNull(this.description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `description`"
        );
      }
      if (Objects.isNull(this.value())) {
        throw new IllegalArgumentException(
          "Missing value for required field `value`"
        );
      }
      return new PutPropertyInput(this);
    }
  }
}
