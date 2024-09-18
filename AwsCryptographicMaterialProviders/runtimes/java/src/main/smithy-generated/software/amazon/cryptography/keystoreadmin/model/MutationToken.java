// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class MutationToken {

  /**
   * The identifier for the Branch Key being mutated.
   */
  private final String Identifier;

  /**
   * UUID of the Mutation.
   */
  private final String UUID;

  /**
   * ISO 8601 time when the mutation was initialized.
   */
  private final String CreateTime;

  protected MutationToken(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.UUID = builder.UUID();
    this.CreateTime = builder.CreateTime();
  }

  /**
   * @return The identifier for the Branch Key being mutated.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return UUID of the Mutation.
   */
  public String UUID() {
    return this.UUID;
  }

  /**
   * @return ISO 8601 time when the mutation was initialized.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key being mutated.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key being mutated.
     */
    String Identifier();

    /**
     * @param UUID UUID of the Mutation.
     */
    Builder UUID(String UUID);

    /**
     * @return UUID of the Mutation.
     */
    String UUID();

    /**
     * @param CreateTime ISO 8601 time when the mutation was initialized.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return ISO 8601 time when the mutation was initialized.
     */
    String CreateTime();

    MutationToken build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected String UUID;

    protected String CreateTime;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationToken model) {
      this.Identifier = model.Identifier();
      this.UUID = model.UUID();
      this.CreateTime = model.CreateTime();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder UUID(String UUID) {
      this.UUID = UUID;
      return this;
    }

    public String UUID() {
      return this.UUID;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public MutationToken build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.UUID())) {
        throw new IllegalArgumentException(
          "Missing value for required field `UUID`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      return new MutationToken(this);
    }
  }
}
