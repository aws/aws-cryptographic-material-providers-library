// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetMutationInput {

  /**
   * The Branch Key to check for a Mutation.
   */
  private final String Identifier;

  protected GetMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The Branch Key to check for a Mutation.
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
     * @param Identifier The Branch Key to check for a Mutation.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Branch Key to check for a Mutation.
     */
    String Identifier();

    GetMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetMutationInput(this);
    }
  }
}
