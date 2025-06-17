// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;

public class PutCountInput {

  private final String description;

  private final Long count;

  private final String transactionId;

  protected PutCountInput(BuilderImpl builder) {
    this.description = builder.description();
    this.count = builder.count();
    this.transactionId = builder.transactionId();
  }

  public String description() {
    return this.description;
  }

  public Long count() {
    return this.count;
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

    Builder count(Long count);

    Long count();

    Builder transactionId(String transactionId);

    String transactionId();

    PutCountInput build();
  }

  static class BuilderImpl implements Builder {

    protected String description;

    protected Long count;

    protected String transactionId;

    protected BuilderImpl() {}

    protected BuilderImpl(PutCountInput model) {
      this.description = model.description();
      this.count = model.count();
      this.transactionId = model.transactionId();
    }

    public Builder description(String description) {
      this.description = description;
      return this;
    }

    public String description() {
      return this.description;
    }

    public Builder count(Long count) {
      this.count = count;
      return this;
    }

    public Long count() {
      return this.count;
    }

    public Builder transactionId(String transactionId) {
      this.transactionId = transactionId;
      return this;
    }

    public String transactionId() {
      return this.transactionId;
    }

    public PutCountInput build() {
      if (Objects.isNull(this.description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `description`"
        );
      }
      if (Objects.isNull(this.count())) {
        throw new IllegalArgumentException(
          "Missing value for required field `count`"
        );
      }
      return new PutCountInput(this);
    }
  }
}
