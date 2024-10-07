// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class GetMutationLockOutput {

  /**
   * If not present, there is no Mutation Lock.
   */
  private final MutationLock MutationLock;

  protected GetMutationLockOutput(BuilderImpl builder) {
    this.MutationLock = builder.MutationLock();
  }

  /**
   * @return If not present, there is no Mutation Lock.
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
     * @param MutationLock If not present, there is no Mutation Lock.
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return If not present, there is no Mutation Lock.
     */
    MutationLock MutationLock();

    GetMutationLockOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationLock MutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationLockOutput model) {
      this.MutationLock = model.MutationLock();
    }

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public GetMutationLockOutput build() {
      return new GetMutationLockOutput(this);
    }
  }
}
