// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetItemsForInitializeMutationOutput {

  /**
   * The materials for the Branch Key.
   */
  private final EncryptedHierarchicalKey ActiveItem;

  /**
   * The materials for the Beacon Key.
   */
  private final EncryptedHierarchicalKey BeaconItem;

  /**
   * The Mutation Commitment, if it exists.
   */
  private final MutationCommitment MutationCommitment;

  /**
   * A Mutation Index, if it exists.
   */
  private final MutationIndex MutationIndex;

  protected GetItemsForInitializeMutationOutput(BuilderImpl builder) {
    this.ActiveItem = builder.ActiveItem();
    this.BeaconItem = builder.BeaconItem();
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
  }

  /**
   * @return The materials for the Branch Key.
   */
  public EncryptedHierarchicalKey ActiveItem() {
    return this.ActiveItem;
  }

  /**
   * @return The materials for the Beacon Key.
   */
  public EncryptedHierarchicalKey BeaconItem() {
    return this.BeaconItem;
  }

  /**
   * @return The Mutation Commitment, if it exists.
   */
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return A Mutation Index, if it exists.
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
     * @param ActiveItem The materials for the Branch Key.
     */
    Builder ActiveItem(EncryptedHierarchicalKey ActiveItem);

    /**
     * @return The materials for the Branch Key.
     */
    EncryptedHierarchicalKey ActiveItem();

    /**
     * @param BeaconItem The materials for the Beacon Key.
     */
    Builder BeaconItem(EncryptedHierarchicalKey BeaconItem);

    /**
     * @return The materials for the Beacon Key.
     */
    EncryptedHierarchicalKey BeaconItem();

    /**
     * @param MutationCommitment The Mutation Commitment, if it exists.
     */
    Builder MutationCommitment(MutationCommitment MutationCommitment);

    /**
     * @return The Mutation Commitment, if it exists.
     */
    MutationCommitment MutationCommitment();

    /**
     * @param MutationIndex A Mutation Index, if it exists.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return A Mutation Index, if it exists.
     */
    MutationIndex MutationIndex();

    GetItemsForInitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey ActiveItem;

    protected EncryptedHierarchicalKey BeaconItem;

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(GetItemsForInitializeMutationOutput model) {
      this.ActiveItem = model.ActiveItem();
      this.BeaconItem = model.BeaconItem();
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder ActiveItem(EncryptedHierarchicalKey ActiveItem) {
      this.ActiveItem = ActiveItem;
      return this;
    }

    public EncryptedHierarchicalKey ActiveItem() {
      return this.ActiveItem;
    }

    public Builder BeaconItem(EncryptedHierarchicalKey BeaconItem) {
      this.BeaconItem = BeaconItem;
      return this;
    }

    public EncryptedHierarchicalKey BeaconItem() {
      return this.BeaconItem;
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

    public GetItemsForInitializeMutationOutput build() {
      if (Objects.isNull(this.ActiveItem())) {
        throw new IllegalArgumentException(
          "Missing value for required field `ActiveItem`"
        );
      }
      if (Objects.isNull(this.BeaconItem())) {
        throw new IllegalArgumentException(
          "Missing value for required field `BeaconItem`"
        );
      }
      return new GetItemsForInitializeMutationOutput(this);
    }
  }
}
