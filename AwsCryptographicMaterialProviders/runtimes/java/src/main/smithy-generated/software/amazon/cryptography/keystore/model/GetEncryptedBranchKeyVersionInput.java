// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Inputs for getting a version of a Branch Key.
 */
public class GetEncryptedBranchKeyVersionInput {

  /**
   * The identifier for the Branch Key to get a particular version for.
   */
  private final String Identifier;

  /**
   * The version to get.
   */
  private final String Version;

  protected GetEncryptedBranchKeyVersionInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Version = builder.Version();
  }

  /**
   * @return The identifier for the Branch Key to get a particular version for.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The version to get.
   */
  public String Version() {
    return this.Version;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key to get a particular version for.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to get a particular version for.
     */
    String Identifier();

    /**
     * @param Version The version to get.
     */
    Builder Version(String Version);

    /**
     * @return The version to get.
     */
    String Version();

    GetEncryptedBranchKeyVersionInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected String Version;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedBranchKeyVersionInput model) {
      this.Identifier = model.Identifier();
      this.Version = model.Version();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Version(String Version) {
      this.Version = Version;
      return this;
    }

    public String Version() {
      return this.Version;
    }

    public GetEncryptedBranchKeyVersionInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Version`"
        );
      }
      return new GetEncryptedBranchKeyVersionInput(this);
    }
  }
}
