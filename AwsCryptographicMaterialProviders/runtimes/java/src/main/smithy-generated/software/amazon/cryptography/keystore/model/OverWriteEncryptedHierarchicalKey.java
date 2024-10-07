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
  private final EncryptedHierarchicalKey EncryptedHierarchicalKey;

  /**
   * The previous itme. Used to construct an optimistic lock for the overwrite.
   */
  private final EncryptedHierarchicalKey Old;

  protected OverWriteEncryptedHierarchicalKey(BuilderImpl builder) {
    this.EncryptedHierarchicalKey = builder.EncryptedHierarchicalKey();
    this.Old = builder.Old();
  }

  /**
   * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
   */
  public EncryptedHierarchicalKey EncryptedHierarchicalKey() {
    return this.EncryptedHierarchicalKey;
  }

  /**
   * @return The previous itme. Used to construct an optimistic lock for the overwrite.
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
     * @param EncryptedHierarchicalKey Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    Builder EncryptedHierarchicalKey(
      EncryptedHierarchicalKey EncryptedHierarchicalKey
    );

    /**
     * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    EncryptedHierarchicalKey EncryptedHierarchicalKey();

    /**
     * @param Old The previous itme. Used to construct an optimistic lock for the overwrite.
     */
    Builder Old(EncryptedHierarchicalKey Old);

    /**
     * @return The previous itme. Used to construct an optimistic lock for the overwrite.
     */
    EncryptedHierarchicalKey Old();

    OverWriteEncryptedHierarchicalKey build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey EncryptedHierarchicalKey;

    protected EncryptedHierarchicalKey Old;

    protected BuilderImpl() {}

    protected BuilderImpl(OverWriteEncryptedHierarchicalKey model) {
      this.EncryptedHierarchicalKey = model.EncryptedHierarchicalKey();
      this.Old = model.Old();
    }

    public Builder EncryptedHierarchicalKey(
      EncryptedHierarchicalKey EncryptedHierarchicalKey
    ) {
      this.EncryptedHierarchicalKey = EncryptedHierarchicalKey;
      return this;
    }

    public EncryptedHierarchicalKey EncryptedHierarchicalKey() {
      return this.EncryptedHierarchicalKey;
    }

    public Builder Old(EncryptedHierarchicalKey Old) {
      this.Old = Old;
      return this;
    }

    public EncryptedHierarchicalKey Old() {
      return this.Old;
    }

    public OverWriteEncryptedHierarchicalKey build() {
      if (Objects.isNull(this.EncryptedHierarchicalKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `EncryptedHierarchicalKey`"
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
