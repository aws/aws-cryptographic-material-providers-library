// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Outputs for getting a Branch Key's ACTIVE version.
 */
public class GetEncryptedActiveBranchKeyOutput {

  /**
   * The encrypted materials for the ACTIVE Branch Key.
   */
  private final EncryptedHierarchicalKey Item;

  protected GetEncryptedActiveBranchKeyOutput(BuilderImpl builder) {
    this.Item = builder.Item();
  }

  /**
   * @return The encrypted materials for the ACTIVE Branch Key.
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
     * @param Item The encrypted materials for the ACTIVE Branch Key.
     */
    Builder Item(EncryptedHierarchicalKey Item);

    /**
     * @return The encrypted materials for the ACTIVE Branch Key.
     */
    EncryptedHierarchicalKey Item();

    GetEncryptedActiveBranchKeyOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Item;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedActiveBranchKeyOutput model) {
      this.Item = model.Item();
    }

    public Builder Item(EncryptedHierarchicalKey Item) {
      this.Item = Item;
      return this;
    }

    public EncryptedHierarchicalKey Item() {
      return this.Item;
    }

    public GetEncryptedActiveBranchKeyOutput build() {
      if (Objects.isNull(this.Item())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Item`"
        );
      }
      return new GetEncryptedActiveBranchKeyOutput(this);
    }
  }
}
