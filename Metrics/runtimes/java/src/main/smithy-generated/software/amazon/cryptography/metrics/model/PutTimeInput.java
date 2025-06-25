// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.util.Objects;

public class PutTimeInput {

  private final String description;

  private final Long duration;

  private final String transactionId;

  protected PutTimeInput(BuilderImpl builder) {
    this.description = builder.description();
    this.duration = builder.duration();
    this.transactionId = builder.transactionId();
  }

  public String description() {
    return this.description;
  }

  public Long duration() {
    return this.duration;
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

    Builder duration(Long duration);

    Long duration();

    Builder transactionId(String transactionId);

    String transactionId();

    PutTimeInput build();
  }

  static class BuilderImpl implements Builder {

    protected String description;

    protected Long duration;

    protected String transactionId;

    protected BuilderImpl() {}

    protected BuilderImpl(PutTimeInput model) {
      this.description = model.description();
      this.duration = model.duration();
      this.transactionId = model.transactionId();
    }

    public Builder description(String description) {
      this.description = description;
      return this;
    }

    public String description() {
      return this.description;
    }

    public Builder duration(Long duration) {
      this.duration = duration;
      return this;
    }

    public Long duration() {
      return this.duration;
    }

    public Builder transactionId(String transactionId) {
      this.transactionId = transactionId;
      return this;
    }

    public String transactionId() {
      return this.transactionId;
    }

    public PutTimeInput build() {
      if (Objects.isNull(this.description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `description`"
        );
      }
      if (Objects.isNull(this.duration())) {
        throw new IllegalArgumentException(
          "Missing value for required field `duration`"
        );
      }
      return new PutTimeInput(this);
    }
  }
}
