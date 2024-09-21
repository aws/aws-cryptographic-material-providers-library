// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.List;
import java.util.Objects;

public class ApplyMutationOutput {

  private final ApplyMutationResult result;

  /**
   * Details what items of the Branch Key ID were changed on this invocation.
   */
  private final List<MutatedBranchKeyItem> mutatedBranchKeyItems;

  protected ApplyMutationOutput(BuilderImpl builder) {
    this.result = builder.result();
    this.mutatedBranchKeyItems = builder.mutatedBranchKeyItems();
  }

  public ApplyMutationResult result() {
    return this.result;
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
    Builder result(ApplyMutationResult result);

    ApplyMutationResult result();

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

    ApplyMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ApplyMutationResult result;

    protected List<MutatedBranchKeyItem> mutatedBranchKeyItems;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationOutput model) {
      this.result = model.result();
      this.mutatedBranchKeyItems = model.mutatedBranchKeyItems();
    }

    public Builder result(ApplyMutationResult result) {
      this.result = result;
      return this;
    }

    public ApplyMutationResult result() {
      return this.result;
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

    public ApplyMutationOutput build() {
      if (Objects.isNull(this.result())) {
        throw new IllegalArgumentException(
          "Missing value for required field `result`"
        );
      }
      if (Objects.isNull(this.mutatedBranchKeyItems())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutatedBranchKeyItems`"
        );
      }
      return new ApplyMutationOutput(this);
    }
  }
}
