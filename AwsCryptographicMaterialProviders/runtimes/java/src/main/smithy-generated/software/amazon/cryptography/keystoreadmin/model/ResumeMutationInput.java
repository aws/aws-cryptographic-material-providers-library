// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class ResumeMutationInput {

  /**
   * The identifier for the Branch Key.
   */
  private final String branchKeyIdentifier;

  /**
   * Describes the original mutable branch key properities.
   *   All members of the input MUST be supplied,
   *   or the operation will return an exception.
   */
  private final MutableBranchKeyProperities original;

  /**
   * Describes the terminal mutable branch key properities.
   *   All members of the input MUST be supplied,
   *   or the operation will return an exception.
   */
  private final MutableBranchKeyProperities terminal;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   */
  private final KeyManagementStrategy strategy;

  protected ResumeMutationInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.original = builder.original();
    this.terminal = builder.terminal();
    this.strategy = builder.strategy();
  }

  /**
   * @return The identifier for the Branch Key.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Describes the original mutable branch key properities.
   *   All members of the input MUST be supplied,
   *   or the operation will return an exception.
   */
  public MutableBranchKeyProperities original() {
    return this.original;
  }

  /**
   * @return Describes the terminal mutable branch key properities.
   *   All members of the input MUST be supplied,
   *   or the operation will return an exception.
   */
  public MutableBranchKeyProperities terminal() {
    return this.terminal;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   */
  public KeyManagementStrategy strategy() {
    return this.strategy;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the Branch Key.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the Branch Key.
     */
    String branchKeyIdentifier();

    /**
     * @param original Describes the original mutable branch key properities.
     *   All members of the input MUST be supplied,
     *   or the operation will return an exception.
     */
    Builder original(MutableBranchKeyProperities original);

    /**
     * @return Describes the original mutable branch key properities.
     *   All members of the input MUST be supplied,
     *   or the operation will return an exception.
     */
    MutableBranchKeyProperities original();

    /**
     * @param terminal Describes the terminal mutable branch key properities.
     *   All members of the input MUST be supplied,
     *   or the operation will return an exception.
     */
    Builder terminal(MutableBranchKeyProperities terminal);

    /**
     * @return Describes the terminal mutable branch key properities.
     *   All members of the input MUST be supplied,
     *   or the operation will return an exception.
     */
    MutableBranchKeyProperities terminal();

    /**
     * @param strategy Optional. Defaults to reEncrypt with a default KMS Client.
     */
    Builder strategy(KeyManagementStrategy strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     */
    KeyManagementStrategy strategy();

    ResumeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected MutableBranchKeyProperities original;

    protected MutableBranchKeyProperities terminal;

    protected KeyManagementStrategy strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(ResumeMutationInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.original = model.original();
      this.terminal = model.terminal();
      this.strategy = model.strategy();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder original(MutableBranchKeyProperities original) {
      this.original = original;
      return this;
    }

    public MutableBranchKeyProperities original() {
      return this.original;
    }

    public Builder terminal(MutableBranchKeyProperities terminal) {
      this.terminal = terminal;
      return this;
    }

    public MutableBranchKeyProperities terminal() {
      return this.terminal;
    }

    public Builder strategy(KeyManagementStrategy strategy) {
      this.strategy = strategy;
      return this;
    }

    public KeyManagementStrategy strategy() {
      return this.strategy;
    }

    public ResumeMutationInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.original())) {
        throw new IllegalArgumentException(
          "Missing value for required field `original`"
        );
      }
      if (Objects.isNull(this.terminal())) {
        throw new IllegalArgumentException(
          "Missing value for required field `terminal`"
        );
      }
      return new ResumeMutationInput(this);
    }
  }
}
