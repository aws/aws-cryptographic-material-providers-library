// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class DescribeMutationInput {

  /**
   * The identifier for the Branch Key.
   */
  private final String Identifier;

  protected DescribeMutationInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The identifier for the Branch Key.
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
     * @param Identifier The identifier for the Branch Key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key.
     */
    String Identifier();

    DescribeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(DescribeMutationInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public DescribeMutationInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new DescribeMutationInput(this);
    }
  }
}
