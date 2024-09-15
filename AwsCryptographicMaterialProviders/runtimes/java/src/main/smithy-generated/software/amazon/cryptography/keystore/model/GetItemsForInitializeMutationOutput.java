// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class GetItemsForInitializeMutationOutput {

  /**
   * The materials for the Branch Key.
   */
  private final EncryptedHierarchicalKey activeItem;

  /**
   * The materials for the Beacon Key.
   */
  private final EncryptedHierarchicalKey beaconItem;

  /**
   * The Mutation Lock, if it exists.
   */
  private final MutationLock mutationLock;

  protected GetItemsForInitializeMutationOutput(BuilderImpl builder) {
    this.activeItem = builder.activeItem();
    this.beaconItem = builder.beaconItem();
    this.mutationLock = builder.mutationLock();
  }

  /**
   * @return The materials for the Branch Key.
   */
  public EncryptedHierarchicalKey activeItem() {
    return this.activeItem;
  }

  /**
   * @return The materials for the Beacon Key.
   */
  public EncryptedHierarchicalKey beaconItem() {
    return this.beaconItem;
  }

  /**
   * @return The Mutation Lock, if it exists.
   */
  public MutationLock mutationLock() {
    return this.mutationLock;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param activeItem The materials for the Branch Key.
     */
    Builder activeItem(EncryptedHierarchicalKey activeItem);

    /**
     * @return The materials for the Branch Key.
     */
    EncryptedHierarchicalKey activeItem();

    /**
     * @param beaconItem The materials for the Beacon Key.
     */
    Builder beaconItem(EncryptedHierarchicalKey beaconItem);

    /**
     * @return The materials for the Beacon Key.
     */
    EncryptedHierarchicalKey beaconItem();

    /**
     * @param mutationLock The Mutation Lock, if it exists.
     */
    Builder mutationLock(MutationLock mutationLock);

    /**
     * @return The Mutation Lock, if it exists.
     */
    MutationLock mutationLock();

    GetItemsForInitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey activeItem;

    protected EncryptedHierarchicalKey beaconItem;

    protected MutationLock mutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(GetItemsForInitializeMutationOutput model) {
      this.activeItem = model.activeItem();
      this.beaconItem = model.beaconItem();
      this.mutationLock = model.mutationLock();
    }

    public Builder activeItem(EncryptedHierarchicalKey activeItem) {
      this.activeItem = activeItem;
      return this;
    }

    public EncryptedHierarchicalKey activeItem() {
      return this.activeItem;
    }

    public Builder beaconItem(EncryptedHierarchicalKey beaconItem) {
      this.beaconItem = beaconItem;
      return this;
    }

    public EncryptedHierarchicalKey beaconItem() {
      return this.beaconItem;
    }

    public Builder mutationLock(MutationLock mutationLock) {
      this.mutationLock = mutationLock;
      return this;
    }

    public MutationLock mutationLock() {
      return this.mutationLock;
    }

    public GetItemsForInitializeMutationOutput build() {
      if (Objects.isNull(this.activeItem())) {
        throw new IllegalArgumentException(
          "Missing value for required field `activeItem`"
        );
      }
      if (Objects.isNull(this.beaconItem())) {
        throw new IllegalArgumentException(
          "Missing value for required field `beaconItem`"
        );
      }
      return new GetItemsForInitializeMutationOutput(this);
    }
  }
}
