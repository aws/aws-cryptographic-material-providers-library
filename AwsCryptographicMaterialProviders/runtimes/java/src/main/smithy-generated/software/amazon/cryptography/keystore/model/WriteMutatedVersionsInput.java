// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

public class WriteMutatedVersionsInput {

  /**
   * List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  private final List<OverWriteEncryptedHierarchicalKey> Items;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationCommitment MutationCommitment;

  /**
   * Write Mutation Index allows Operations to either create or update the Index.
   */
  private final WriteMutationIndex MutationIndex;

  private final Boolean EndMutation;

  protected WriteMutatedVersionsInput(BuilderImpl builder) {
    this.Items = builder.Items();
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
    this.EndMutation = builder.EndMutation();
  }

  /**
   * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  public List<OverWriteEncryptedHierarchicalKey> Items() {
    return this.Items;
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
   * @return Write Mutation Index allows Operations to either create or update the Index.
   */
  public WriteMutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  public Boolean EndMutation() {
    return this.EndMutation;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Items List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    Builder Items(List<OverWriteEncryptedHierarchicalKey> Items);

    /**
     * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    List<OverWriteEncryptedHierarchicalKey> Items();

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
     * @param MutationIndex Write Mutation Index allows Operations to either create or update the Index.
     */
    Builder MutationIndex(WriteMutationIndex MutationIndex);

    /**
     * @return Write Mutation Index allows Operations to either create or update the Index.
     */
    WriteMutationIndex MutationIndex();

    Builder EndMutation(Boolean EndMutation);

    Boolean EndMutation();

    WriteMutatedVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected List<OverWriteEncryptedHierarchicalKey> Items;

    protected MutationCommitment MutationCommitment;

    protected WriteMutationIndex MutationIndex;

    protected Boolean EndMutation;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteMutatedVersionsInput model) {
      this.Items = model.Items();
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
      this.EndMutation = model.EndMutation();
    }

    public Builder Items(List<OverWriteEncryptedHierarchicalKey> Items) {
      this.Items = Items;
      return this;
    }

    public List<OverWriteEncryptedHierarchicalKey> Items() {
      return this.Items;
    }

    public Builder MutationCommitment(MutationCommitment MutationCommitment) {
      this.MutationCommitment = MutationCommitment;
      return this;
    }

    public MutationCommitment MutationCommitment() {
      return this.MutationCommitment;
    }

    public Builder MutationIndex(WriteMutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public WriteMutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public Builder EndMutation(Boolean EndMutation) {
      this.EndMutation = EndMutation;
      return this;
    }

    public Boolean EndMutation() {
      return this.EndMutation;
    }

    public WriteMutatedVersionsInput build() {
      if (Objects.isNull(this.Items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Items`"
        );
      }
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
      if (Objects.isNull(this.EndMutation())) {
        throw new IllegalArgumentException(
          "Missing value for required field `EndMutation`"
        );
      }
      return new WriteMutatedVersionsInput(this);
    }
  }
}
