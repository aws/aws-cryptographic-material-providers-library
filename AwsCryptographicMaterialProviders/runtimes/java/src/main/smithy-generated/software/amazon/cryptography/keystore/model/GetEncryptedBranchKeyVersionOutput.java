// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Outputs for getting a version of a Branch Key.
 */
public class GetEncryptedBranchKeyVersionOutput {

  /**
   * The materials for the Branch Key.
   */
  private final EncryptedHierarchicalKey Item;

  protected GetEncryptedBranchKeyVersionOutput(BuilderImpl builder) {
    this.Item = builder.Item();
  }

  /**
   * @return The materials for the Branch Key.
   */
  public EncryptedHierarchicalKey Item() {
    return this.Item;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Item The materials for the Branch Key.
     */
    Builder Item(EncryptedHierarchicalKey Item);

    /**
     * @return The materials for the Branch Key.
     */
    EncryptedHierarchicalKey Item();

    GetEncryptedBranchKeyVersionOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Item;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedBranchKeyVersionOutput model) {
      this.Item = model.Item();
    }

    public Builder Item(EncryptedHierarchicalKey Item) {
      this.Item = Item;
      return this;
    }

    public EncryptedHierarchicalKey Item() {
      return this.Item;
    }

    public GetEncryptedBranchKeyVersionOutput build() {
      if (Objects.isNull(this.Item())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Item`"
        );
      }
      return new GetEncryptedBranchKeyVersionOutput(this);
    }
  }
}
