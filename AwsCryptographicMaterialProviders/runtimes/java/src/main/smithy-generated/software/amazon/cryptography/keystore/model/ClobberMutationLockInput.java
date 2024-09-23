// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class ClobberMutationLockInput {

  /**
   * Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock mutationLock;

  protected ClobberMutationLockInput(BuilderImpl builder) {
    this.mutationLock = builder.mutationLock();
  }

  /**
   * @return Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  public MutationLock mutationLock() {
    return this.mutationLock;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param mutationLock Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder mutationLock(MutationLock mutationLock);

    /**
     * @return Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock mutationLock();

    ClobberMutationLockInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationLock mutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(ClobberMutationLockInput model) {
      this.mutationLock = model.mutationLock();
    }

    public Builder mutationLock(MutationLock mutationLock) {
      this.mutationLock = mutationLock;
      return this;
    }

    public MutationLock mutationLock() {
      return this.mutationLock;
    }

    public ClobberMutationLockInput build() {
      if (Objects.isNull(this.mutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutationLock`"
        );
      }
      return new ClobberMutationLockInput(this);
    }
  }
}
