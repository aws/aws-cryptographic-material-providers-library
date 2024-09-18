// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteMutationIndexInput {

  /**
   * Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationCommitment MutationCommitment;

  /**
   * Information of an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  protected WriteMutationIndexInput(BuilderImpl builder) {
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return Information of an in-flight Mutation of a Branch Key.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param MutationCommitment Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationCommitment(MutationCommitment MutationCommitment);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationCommitment MutationCommitment();

    /**
     * @param MutationIndex Information of an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information of an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    WriteMutationIndexInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteMutationIndexInput model) {
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder MutationCommitment(MutationCommitment MutationCommitment) {
      this.MutationCommitment = MutationCommitment;
      return this;
    }

    public MutationCommitment MutationCommitment() {
      return this.MutationCommitment;
    }

    public Builder MutationIndex(MutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public MutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public WriteMutationIndexInput build() {
      if (Objects.isNull(this.MutationCommitment())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationCommitment`"
        );
      }
      if (Objects.isNull(this.MutationIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationIndex`"
        );
      }
      return new WriteMutationIndexInput(this);
    }
  }
}
