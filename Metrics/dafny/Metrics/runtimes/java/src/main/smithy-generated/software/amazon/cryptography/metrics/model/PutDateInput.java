// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.metrics.model;

import java.time.Instant;
import java.util.Objects;

public class PutDateInput {

  private final String description;

  private final Instant date;

  private final String transactionId;

  protected PutDateInput(BuilderImpl builder) {
    this.description = builder.description();
    this.date = builder.date();
    this.transactionId = builder.transactionId();
  }

  public String description() {
    return this.description;
  }

  public Instant date() {
    return this.date;
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

    Builder date(Instant date);

    Instant date();

    Builder transactionId(String transactionId);

    String transactionId();

    PutDateInput build();
  }

  static class BuilderImpl implements Builder {

    protected String description;

    protected Instant date;

    protected String transactionId;

    protected BuilderImpl() {}

    protected BuilderImpl(PutDateInput model) {
      this.description = model.description();
      this.date = model.date();
      this.transactionId = model.transactionId();
    }

    public Builder description(String description) {
      this.description = description;
      return this;
    }

    public String description() {
      return this.description;
    }

    public Builder date(Instant date) {
      this.date = date;
      return this;
    }

    public Instant date() {
      return this.date;
    }

    public Builder transactionId(String transactionId) {
      this.transactionId = transactionId;
      return this;
    }

    public String transactionId() {
      return this.transactionId;
    }

    public PutDateInput build() {
      if (Objects.isNull(this.description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `description`"
        );
      }
      if (Objects.isNull(this.date())) {
        throw new IllegalArgumentException(
          "Missing value for required field `date`"
        );
      }
      return new PutDateInput(this);
    }
  }
}
