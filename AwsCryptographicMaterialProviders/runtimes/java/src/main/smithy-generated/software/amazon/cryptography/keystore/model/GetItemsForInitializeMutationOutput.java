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
   * The Mutation Lock, if it exists.
   */
  private final MutationLock MutationLock;

  protected GetItemsForInitializeMutationOutput(BuilderImpl builder) {
    this.ActiveItem = builder.ActiveItem();
    this.BeaconItem = builder.BeaconItem();
    this.MutationLock = builder.MutationLock();
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
   * @return The Mutation Lock, if it exists.
   */
  public MutationLock MutationLock() {
    return this.MutationLock;
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
     * @param MutationLock The Mutation Lock, if it exists.
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return The Mutation Lock, if it exists.
     */
    MutationLock MutationLock();

    GetItemsForInitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey ActiveItem;

    protected EncryptedHierarchicalKey BeaconItem;

    protected MutationLock MutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(GetItemsForInitializeMutationOutput model) {
      this.ActiveItem = model.ActiveItem();
      this.BeaconItem = model.BeaconItem();
      this.MutationLock = model.MutationLock();
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

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
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
