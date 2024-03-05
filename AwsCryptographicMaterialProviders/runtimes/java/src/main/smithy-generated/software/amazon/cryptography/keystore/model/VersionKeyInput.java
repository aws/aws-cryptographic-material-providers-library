// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

/**
 * Inputs for versioning a Branch Key.
 */
public class VersionKeyInput {

  /**
   * The identifier for the Branch Key to be versioned.
   */
  private final String branchKeyIdentifier;

  /**
   * A List of Grant Tokens to include in KMS requests for Branch Key Versioning. This augments the list on the Key Store.
   */
  private final List<String> grantTokens;

  protected VersionKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.grantTokens = builder.grantTokens();
  }

  /**
   * @return The identifier for the Branch Key to be versioned.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return A List of Grant Tokens to include in KMS requests for Branch Key Versioning. This augments the list on the Key Store.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the Branch Key to be versioned.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the Branch Key to be versioned.
     */
    String branchKeyIdentifier();

    /**
     * @param grantTokens A List of Grant Tokens to include in KMS requests for Branch Key Versioning. This augments the list on the Key Store.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return A List of Grant Tokens to include in KMS requests for Branch Key Versioning. This augments the list on the Key Store.
     */
    List<String> grantTokens();

    VersionKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected List<String> grantTokens;

    protected BuilderImpl() {}

    protected BuilderImpl(VersionKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.grantTokens = model.grantTokens();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public VersionKeyInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      return new VersionKeyInput(this);
    }
  }
}
