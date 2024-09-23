// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class GetMutationLockOutput {

  /**
   * If not present, there is no Mutation Lock.
   */
  private final MutationLock mutationLock;

  protected GetMutationLockOutput(BuilderImpl builder) {
    this.mutationLock = builder.mutationLock();
  }

  /**
   * @return If not present, there is no Mutation Lock.
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
     * @param mutationLock If not present, there is no Mutation Lock.
     */
    Builder mutationLock(MutationLock mutationLock);

    /**
     * @return If not present, there is no Mutation Lock.
     */
    MutationLock mutationLock();

    GetMutationLockOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationLock mutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationLockOutput model) {
      this.mutationLock = model.mutationLock();
    }

    public Builder mutationLock(MutationLock mutationLock) {
      this.mutationLock = mutationLock;
      return this;
    }

    public MutationLock mutationLock() {
      return this.mutationLock;
    }

    public GetMutationLockOutput build() {
      return new GetMutationLockOutput(this);
    }
  }
}
