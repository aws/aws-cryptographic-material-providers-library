// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * To avoid information loss, overwrites to any item in the Key Store
 * are done conditioned on the old value.
 */
public class OverWriteMutationIndex {

  /**
   * Information of an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex Index;

  /**
   * The previous item. Used to construct an optimistic lock for the overwrite.
   */
  private final MutationIndex Old;

  protected OverWriteMutationIndex(BuilderImpl builder) {
    this.Index = builder.Index();
    this.Old = builder.Old();
  }

  /**
   * @return Information of an in-flight Mutation of a Branch Key.
   */
  public MutationIndex Index() {
    return this.Index;
  }

  /**
   * @return The previous item. Used to construct an optimistic lock for the overwrite.
   */
  public MutationIndex Old() {
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
     * @param Index Information of an in-flight Mutation of a Branch Key.
     */
    Builder Index(MutationIndex Index);

    /**
     * @return Information of an in-flight Mutation of a Branch Key.
     */
    MutationIndex Index();

    /**
     * @param Old The previous item. Used to construct an optimistic lock for the overwrite.
     */
    Builder Old(MutationIndex Old);

    /**
     * @return The previous item. Used to construct an optimistic lock for the overwrite.
     */
    MutationIndex Old();

    OverWriteMutationIndex build();
  }

  static class BuilderImpl implements Builder {

    protected MutationIndex Index;

    protected MutationIndex Old;

    protected BuilderImpl() {}

    protected BuilderImpl(OverWriteMutationIndex model) {
      this.Index = model.Index();
      this.Old = model.Old();
    }

    public Builder Index(MutationIndex Index) {
      this.Index = Index;
      return this;
    }

    public MutationIndex Index() {
      return this.Index;
    }

    public Builder Old(MutationIndex Old) {
      this.Old = Old;
      return this;
    }

    public MutationIndex Old() {
      return this.Old;
    }

    public OverWriteMutationIndex build() {
      if (Objects.isNull(this.Index())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Index`"
        );
      }
      if (Objects.isNull(this.Old())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Old`"
        );
      }
      return new OverWriteMutationIndex(this);
    }
  }
}
