// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class ApplyMutationResult {

  /**
   * Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
   */
  private final MutationToken ContinueMutation;

  /**
   * All items have been mutated. The mutation is complete.
   */
  private final MutationComplete CompleteMutation;

  protected ApplyMutationResult(BuilderImpl builder) {
    this.ContinueMutation = builder.ContinueMutation();
    this.CompleteMutation = builder.CompleteMutation();
  }

  /**
   * @return Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
   */
  public MutationToken ContinueMutation() {
    return this.ContinueMutation;
  }

  /**
   * @return All items have been mutated. The mutation is complete.
   */
  public MutationComplete CompleteMutation() {
    return this.CompleteMutation;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ContinueMutation Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
     */
    Builder ContinueMutation(MutationToken ContinueMutation);

    /**
     * @return Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.
     */
    MutationToken ContinueMutation();

    /**
     * @param CompleteMutation All items have been mutated. The mutation is complete.
     */
    Builder CompleteMutation(MutationComplete CompleteMutation);

    /**
     * @return All items have been mutated. The mutation is complete.
     */
    MutationComplete CompleteMutation();

    ApplyMutationResult build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken ContinueMutation;

    protected MutationComplete CompleteMutation;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationResult model) {
      this.ContinueMutation = model.ContinueMutation();
      this.CompleteMutation = model.CompleteMutation();
    }

    public Builder ContinueMutation(MutationToken ContinueMutation) {
      this.ContinueMutation = ContinueMutation;
      return this;
    }

    public MutationToken ContinueMutation() {
      return this.ContinueMutation;
    }

    public Builder CompleteMutation(MutationComplete CompleteMutation) {
      this.CompleteMutation = CompleteMutation;
      return this;
    }

    public MutationComplete CompleteMutation() {
      return this.CompleteMutation;
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
      Object[] allValues = { this.ContinueMutation, this.CompleteMutation };
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
