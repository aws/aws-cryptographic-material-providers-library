// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetMutationLockInput {

  /**
   * The Branch Key to check for a Mutation Lock.
   */
  private final String Identifier;

  protected GetMutationLockInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The Branch Key to check for a Mutation Lock.
   */
  public String Identifier() {
    return this.Identifier;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The Branch Key to check for a Mutation Lock.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Branch Key to check for a Mutation Lock.
     */
    String Identifier();

    GetMutationLockInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationLockInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetMutationLockInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetMutationLockInput(this);
    }
  }
}
