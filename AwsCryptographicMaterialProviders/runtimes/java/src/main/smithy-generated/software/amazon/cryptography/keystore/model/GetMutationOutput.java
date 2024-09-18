// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

public class GetMutationOutput {

  /**
   * If not present, there is no Mutation.
   */
  private final MutationCommitment MutationCommitment;

  /**
   * If not present, there is no Mutation.
   */
  private final MutationIndex MutationIndex;

  protected GetMutationOutput(BuilderImpl builder) {
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
  }

  /**
   * @return If not present, there is no Mutation.
   */
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return If not present, there is no Mutation.
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
     * @param MutationCommitment If not present, there is no Mutation.
     */
    Builder MutationCommitment(MutationCommitment MutationCommitment);

    /**
     * @return If not present, there is no Mutation.
     */
    MutationCommitment MutationCommitment();

    /**
     * @param MutationIndex If not present, there is no Mutation.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return If not present, there is no Mutation.
     */
    MutationIndex MutationIndex();

    GetMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(GetMutationOutput model) {
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder MutationCommitment(MutationCommitment MutationCommitment) {
      this.MutationCommitment = MutationCommitment;
      return this;
    }

    public MutationCommitment MutationCommitment() {
      return this.MutationCommitment;
    }

    public Builder MutationIndex(MutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public MutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public GetMutationOutput build() {
      return new GetMutationOutput(this);
    }
  }
}
