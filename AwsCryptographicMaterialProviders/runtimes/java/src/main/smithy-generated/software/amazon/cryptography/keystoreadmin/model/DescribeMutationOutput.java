// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

public class DescribeMutationOutput {

  /**
   *
   *   If present,
   *   pass the Mutation Token to the Apply Mutation
   *   operation to continue the Mutation.
   *   Otherwise, there is no Mutation Lock.
   */
  private final MutationToken mutationToken;

  protected DescribeMutationOutput(BuilderImpl builder) {
    this.mutationToken = builder.mutationToken();
  }

  /**
   * @return
   *   If present,
   *   pass the Mutation Token to the Apply Mutation
   *   operation to continue the Mutation.
   *   Otherwise, there is no Mutation Lock.
   */
  public MutationToken mutationToken() {
    return this.mutationToken;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param mutationToken
     *   If present,
     *   pass the Mutation Token to the Apply Mutation
     *   operation to continue the Mutation.
     *   Otherwise, there is no Mutation Lock.
     */
    Builder mutationToken(MutationToken mutationToken);

    /**
     * @return
     *   If present,
     *   pass the Mutation Token to the Apply Mutation
     *   operation to continue the Mutation.
     *   Otherwise, there is no Mutation Lock.
     */
    MutationToken mutationToken();

    DescribeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken mutationToken;

    protected BuilderImpl() {}

    protected BuilderImpl(DescribeMutationOutput model) {
      this.mutationToken = model.mutationToken();
    }

    public Builder mutationToken(MutationToken mutationToken) {
      this.mutationToken = mutationToken;
      return this;
    }

    public MutationToken mutationToken() {
      return this.mutationToken;
    }

    public DescribeMutationOutput build() {
      return new DescribeMutationOutput(this);
    }
  }
}
