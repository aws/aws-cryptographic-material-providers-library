// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * To avoid information loss, overwrites to a EncryptedHierarchicalKey
 * are done conditioned on the old value.
 */
public class OverWriteEncryptedHierarchicalKey {

  /**
   * Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
   */
  private final EncryptedHierarchicalKey Item;

  /**
   * The previous item. Used to construct an optimistic lock for the overwrite.
   */
  private final EncryptedHierarchicalKey Old;

  protected OverWriteEncryptedHierarchicalKey(BuilderImpl builder) {
    this.Item = builder.Item();
    this.Old = builder.Old();
  }

  /**
   * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
   */
  public EncryptedHierarchicalKey Item() {
    return this.Item;
  }

  /**
   * @return The previous item. Used to construct an optimistic lock for the overwrite.
   */
  public EncryptedHierarchicalKey Old() {
    return this.Old;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Item Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    Builder Item(EncryptedHierarchicalKey Item);

    /**
     * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    EncryptedHierarchicalKey Item();

    /**
     * @param Old The previous item. Used to construct an optimistic lock for the overwrite.
     */
    Builder Old(EncryptedHierarchicalKey Old);

    /**
     * @return The previous item. Used to construct an optimistic lock for the overwrite.
     */
    EncryptedHierarchicalKey Old();

    OverWriteEncryptedHierarchicalKey build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Item;

    protected EncryptedHierarchicalKey Old;

    protected BuilderImpl() {}

    protected BuilderImpl(OverWriteEncryptedHierarchicalKey model) {
      this.Item = model.Item();
      this.Old = model.Old();
    }

    public Builder Item(EncryptedHierarchicalKey Item) {
      this.Item = Item;
      return this;
    }

    public EncryptedHierarchicalKey Item() {
      return this.Item;
    }

    public Builder Old(EncryptedHierarchicalKey Old) {
      this.Old = Old;
      return this;
    }

    public EncryptedHierarchicalKey Old() {
      return this.Old;
    }

    public OverWriteEncryptedHierarchicalKey build() {
      if (Objects.isNull(this.Item())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Item`"
        );
      }
      if (Objects.isNull(this.Old())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Old`"
        );
      }
      return new OverWriteEncryptedHierarchicalKey(this);
    }
  }
}
