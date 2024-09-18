// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Write Initialize Mutation allows Mutations to either rotate/version or simply mutate the Active.
 */
public class WriteInitializeMutationVersion {

  /**
   * Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
   */
  private final EncryptedHierarchicalKey rotate;

  /**
   * To avoid information loss, overwrites to a EncryptedHierarchicalKey
   * are done conditioned on the old value.
   */
  private final OverWriteEncryptedHierarchicalKey mutate;

  protected WriteInitializeMutationVersion(BuilderImpl builder) {
    this.rotate = builder.rotate();
    this.mutate = builder.mutate();
  }

  /**
   * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
   */
  public EncryptedHierarchicalKey rotate() {
    return this.rotate;
  }

  /**
   * @return To avoid information loss, overwrites to a EncryptedHierarchicalKey
   * are done conditioned on the old value.
   */
  public OverWriteEncryptedHierarchicalKey mutate() {
    return this.mutate;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param rotate Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    Builder rotate(EncryptedHierarchicalKey rotate);

    /**
     * @return Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
     */
    EncryptedHierarchicalKey rotate();

    /**
     * @param mutate To avoid information loss, overwrites to a EncryptedHierarchicalKey
     * are done conditioned on the old value.
     */
    Builder mutate(OverWriteEncryptedHierarchicalKey mutate);

    /**
     * @return To avoid information loss, overwrites to a EncryptedHierarchicalKey
     * are done conditioned on the old value.
     */
    OverWriteEncryptedHierarchicalKey mutate();

    WriteInitializeMutationVersion build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey rotate;

    protected OverWriteEncryptedHierarchicalKey mutate;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationVersion model) {
      this.rotate = model.rotate();
      this.mutate = model.mutate();
    }

    public Builder rotate(EncryptedHierarchicalKey rotate) {
      this.rotate = rotate;
      return this;
    }

    public EncryptedHierarchicalKey rotate() {
      return this.rotate;
    }

    public Builder mutate(OverWriteEncryptedHierarchicalKey mutate) {
      this.mutate = mutate;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey mutate() {
      return this.mutate;
    }

    public WriteInitializeMutationVersion build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`WriteInitializeMutationVersion` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new WriteInitializeMutationVersion(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.rotate, this.mutate };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
