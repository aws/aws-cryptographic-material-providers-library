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
  private final MutationLock MutationLock;

  protected WriteMutatedVersionsInput(BuilderImpl builder) {
    this.Items = builder.Items();
    this.MutationLock = builder.MutationLock();
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
     * @param Items List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    Builder Items(List<OverWriteEncryptedHierarchicalKey> Items);

    /**
     * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    List<OverWriteEncryptedHierarchicalKey> Items();

    /**
     * @param MutationLock Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock MutationLock();

    WriteMutatedVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected List<OverWriteEncryptedHierarchicalKey> Items;

    protected MutationLock MutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteMutatedVersionsInput model) {
      this.Items = model.Items();
      this.MutationLock = model.MutationLock();
    }

    public Builder Items(List<OverWriteEncryptedHierarchicalKey> Items) {
      this.Items = Items;
      return this;
    }

    public List<OverWriteEncryptedHierarchicalKey> Items() {
      return this.Items;
    }

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public WriteMutatedVersionsInput build() {
      if (Objects.isNull(this.Items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Items`"
        );
      }
      if (Objects.isNull(this.MutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationLock`"
        );
      }
      return new WriteMutatedVersionsInput(this);
    }
  }
}
