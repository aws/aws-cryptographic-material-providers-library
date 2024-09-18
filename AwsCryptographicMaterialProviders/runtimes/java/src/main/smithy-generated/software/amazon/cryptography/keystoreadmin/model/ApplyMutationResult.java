// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class ApplyMutationResult {

  /**
   * Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
   */
  private final MutationToken continueMutation;

  /**
   * All items have been mutated; the Mutation Lock has been removed. The mutation is complete.
   */
  private final MutationComplete completeMutation;

  protected ApplyMutationResult(BuilderImpl builder) {
    this.continueMutation = builder.continueMutation();
    this.completeMutation = builder.completeMutation();
  }

  /**
   * @return Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
   */
  public MutationToken continueMutation() {
    return this.continueMutation;
  }

  /**
   * @return All items have been mutated; the Mutation Lock has been removed. The mutation is complete.
   */
  public MutationComplete completeMutation() {
    return this.completeMutation;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param continueMutation Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
     */
    Builder continueMutation(MutationToken continueMutation);

    /**
     * @return Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
     */
    MutationToken continueMutation();

    /**
     * @param completeMutation All items have been mutated; the Mutation Lock has been removed. The mutation is complete.
     */
    Builder completeMutation(MutationComplete completeMutation);

    /**
     * @return All items have been mutated; the Mutation Lock has been removed. The mutation is complete.
     */
    MutationComplete completeMutation();

    ApplyMutationResult build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken continueMutation;

    protected MutationComplete completeMutation;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationResult model) {
      this.continueMutation = model.continueMutation();
      this.completeMutation = model.completeMutation();
    }

    public Builder continueMutation(MutationToken continueMutation) {
      this.continueMutation = continueMutation;
      return this;
    }

    public MutationToken continueMutation() {
      return this.continueMutation;
    }

    public Builder completeMutation(MutationComplete completeMutation) {
      this.completeMutation = completeMutation;
      return this;
    }

    public MutationComplete completeMutation() {
      return this.completeMutation;
    }

    public ApplyMutationResult build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`ApplyMutationResult` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new ApplyMutationResult(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.continueMutation, this.completeMutation };
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
