// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetItemsForInitializeMutationInput {

  /**
   * The Branch Key to Mutate.
   */
  private final String Identifier;

  protected GetItemsForInitializeMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The Branch Key to Mutate.
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
     * @param Identifier The Branch Key to Mutate.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Branch Key to Mutate.
     */
    String Identifier();

    GetItemsForInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetItemsForInitializeMutationInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetItemsForInitializeMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetItemsForInitializeMutationInput(this);
    }
  }
}
