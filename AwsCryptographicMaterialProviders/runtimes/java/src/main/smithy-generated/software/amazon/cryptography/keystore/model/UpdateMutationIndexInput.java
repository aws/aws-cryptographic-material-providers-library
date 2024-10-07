// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class UpdateMutationIndexInput {

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex OldMutationIndex;

  protected UpdateMutationIndexInput(BuilderImpl builder) {
    this.MutationIndex = builder.MutationIndex();
    this.OldMutationIndex = builder.OldMutationIndex();
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex OldMutationIndex() {
    return this.OldMutationIndex;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param MutationIndex Information on an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    /**
     * @param OldMutationIndex Information on an in-flight Mutation of a Branch Key.
     */
    Builder OldMutationIndex(MutationIndex OldMutationIndex);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex OldMutationIndex();

    UpdateMutationIndexInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationIndex MutationIndex;

    protected MutationIndex OldMutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(UpdateMutationIndexInput model) {
      this.MutationIndex = model.MutationIndex();
      this.OldMutationIndex = model.OldMutationIndex();
    }

    public Builder MutationIndex(MutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public MutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public Builder OldMutationIndex(MutationIndex OldMutationIndex) {
      this.OldMutationIndex = OldMutationIndex;
      return this;
    }

    public MutationIndex OldMutationIndex() {
      return this.OldMutationIndex;
    }

    public UpdateMutationIndexInput build() {
      if (Objects.isNull(this.MutationIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationIndex`"
        );
      }
      if (Objects.isNull(this.OldMutationIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `OldMutationIndex`"
        );
      }
      return new UpdateMutationIndexInput(this);
    }
  }
}
