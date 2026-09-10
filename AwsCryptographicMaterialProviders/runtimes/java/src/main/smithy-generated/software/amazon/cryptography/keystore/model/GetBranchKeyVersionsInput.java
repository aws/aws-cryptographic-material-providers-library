// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Inputs for getting branch key versions.
 */
public class GetBranchKeyVersionsInput {

  /**
   * The identifier of the Branch Key to get versions for.
   */
  private final String branchKeyIdentifier;

  /**
   * The maximum number of versions to retrieve.
   */
  private final Integer count;

  protected GetBranchKeyVersionsInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.count = builder.count();
  }

  /**
   * @return The identifier of the Branch Key to get versions for.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return The maximum number of versions to retrieve.
   */
  public Integer count() {
    return this.count;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier of the Branch Key to get versions for.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier of the Branch Key to get versions for.
     */
    String branchKeyIdentifier();

    /**
     * @param count The maximum number of versions to retrieve.
     */
    Builder count(Integer count);

    /**
     * @return The maximum number of versions to retrieve.
     */
    Integer count();

    GetBranchKeyVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected Integer count;

    protected BuilderImpl() {}

    protected BuilderImpl(GetBranchKeyVersionsInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.count = model.count();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder count(Integer count) {
      this.count = count;
      return this;
    }

    public Integer count() {
      return this.count;
    }

    public GetBranchKeyVersionsInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.count())) {
        throw new IllegalArgumentException(
          "Missing value for required field `count`"
        );
      }
      return new GetBranchKeyVersionsInput(this);
    }
  }
}
