// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.List;
import java.util.Objects;

public class InitializeMutationOutput {

  /**
   * Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
   */
  private final MutationToken mutationToken;

  /**
   * Details what items of the Branch Key ID were changed on this invocation.
   */
  private final List<MutatedBranchKeyItem> mutatedBranchKeyItems;

  protected InitializeMutationOutput(BuilderImpl builder) {
    this.mutationToken = builder.mutationToken();
    this.mutatedBranchKeyItems = builder.mutatedBranchKeyItems();
  }

  /**
   * @return Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
   */
  public MutationToken mutationToken() {
    return this.mutationToken;
  }

  /**
   * @return Details what items of the Branch Key ID were changed on this invocation.
   */
  public List<MutatedBranchKeyItem> mutatedBranchKeyItems() {
    return this.mutatedBranchKeyItems;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param mutationToken Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
     */
    Builder mutationToken(MutationToken mutationToken);

    /**
     * @return Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
     */
    MutationToken mutationToken();

    /**
     * @param mutatedBranchKeyItems Details what items of the Branch Key ID were changed on this invocation.
     */
    Builder mutatedBranchKeyItems(
      List<MutatedBranchKeyItem> mutatedBranchKeyItems
    );

    /**
     * @return Details what items of the Branch Key ID were changed on this invocation.
     */
    List<MutatedBranchKeyItem> mutatedBranchKeyItems();

    InitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken mutationToken;

    protected List<MutatedBranchKeyItem> mutatedBranchKeyItems;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationOutput model) {
      this.mutationToken = model.mutationToken();
      this.mutatedBranchKeyItems = model.mutatedBranchKeyItems();
    }

    public Builder mutationToken(MutationToken mutationToken) {
      this.mutationToken = mutationToken;
      return this;
    }

    public MutationToken mutationToken() {
      return this.mutationToken;
    }

    public Builder mutatedBranchKeyItems(
      List<MutatedBranchKeyItem> mutatedBranchKeyItems
    ) {
      this.mutatedBranchKeyItems = mutatedBranchKeyItems;
      return this;
    }

    public List<MutatedBranchKeyItem> mutatedBranchKeyItems() {
      return this.mutatedBranchKeyItems;
    }

    public InitializeMutationOutput build() {
      if (Objects.isNull(this.mutationToken())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutationToken`"
        );
      }
      if (Objects.isNull(this.mutatedBranchKeyItems())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutatedBranchKeyItems`"
        );
      }
      return new InitializeMutationOutput(this);
    }
  }
}
