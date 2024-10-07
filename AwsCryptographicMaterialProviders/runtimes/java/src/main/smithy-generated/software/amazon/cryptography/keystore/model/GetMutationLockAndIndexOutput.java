// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class GetMutationLockAndIndexOutput {

  /**
   * Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock MutationLock;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  protected GetMutationLockAndIndexOutput(BuilderImpl builder) {
    this.MutationLock = builder.MutationLock();
    this.MutationIndex = builder.MutationIndex();
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

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
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

    /**
     * @param MutationIndex Information on an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    GetMutationLockAndIndexOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationLock MutationLock;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationLockAndIndexOutput model) {
      this.MutationLock = model.MutationLock();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public Builder MutationIndex(MutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public MutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public GetMutationLockAndIndexOutput build() {
      return new GetMutationLockAndIndexOutput(this);
    }
  }
}
