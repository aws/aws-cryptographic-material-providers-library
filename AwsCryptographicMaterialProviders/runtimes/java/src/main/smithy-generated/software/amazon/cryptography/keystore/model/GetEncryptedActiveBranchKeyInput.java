// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Get the ACTIVE version for a particular Branch Key.
 */
public class GetEncryptedActiveBranchKeyInput {

  /**
   * The identifier for the Branch Key to get the ACTIVE version for.
   */
  private final String Identifier;

  protected GetEncryptedActiveBranchKeyInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
  }

  /**
   * @return The identifier for the Branch Key to get the ACTIVE version for.
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
     * @param Identifier The identifier for the Branch Key to get the ACTIVE version for.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to get the ACTIVE version for.
     */
    String Identifier();

    GetEncryptedActiveBranchKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedActiveBranchKeyInput model) {
      this.Identifier = model.Identifier();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public GetEncryptedActiveBranchKeyInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      return new GetEncryptedActiveBranchKeyInput(this);
    }
  }
}
