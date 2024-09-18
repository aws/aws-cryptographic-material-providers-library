// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Outputs for getting a Beacon Key
 */
public class GetEncryptedBeaconKeyOutput {

  /**
   * The materials for the Beacon Key.
   */
  private final EncryptedHierarchicalKey Item;

  protected GetEncryptedBeaconKeyOutput(BuilderImpl builder) {
    this.Item = builder.Item();
  }

  /**
   * @return The materials for the Beacon Key.
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
     * @param Item The materials for the Beacon Key.
     */
    Builder Item(EncryptedHierarchicalKey Item);

    /**
     * @return The materials for the Beacon Key.
     */
    EncryptedHierarchicalKey Item();

    GetEncryptedBeaconKeyOutput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Item;

    protected BuilderImpl() {}

    protected BuilderImpl(GetEncryptedBeaconKeyOutput model) {
      this.Item = model.Item();
    }

    public Builder Item(EncryptedHierarchicalKey Item) {
      this.Item = Item;
      return this;
    }

    public EncryptedHierarchicalKey Item() {
      return this.Item;
    }

    public GetEncryptedBeaconKeyOutput build() {
      if (Objects.isNull(this.Item())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Item`"
        );
      }
      return new GetEncryptedBeaconKeyOutput(this);
    }
  }
}
