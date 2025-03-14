// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.List;
import java.util.Objects;

public class ApplyMutationOutput {

  private final ApplyMutationResult MutationResult;

  /**
   * Details what items of the Branch Key ID were changed on this invocation.
   */
  private final List<MutatedBranchKeyItem> MutatedBranchKeyItems;

  /**
   * ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
   */
  private final String LastModifiedTime;

  protected ApplyMutationOutput(BuilderImpl builder) {
    this.MutationResult = builder.MutationResult();
    this.MutatedBranchKeyItems = builder.MutatedBranchKeyItems();
    this.LastModifiedTime = builder.LastModifiedTime();
  }

  public ApplyMutationResult MutationResult() {
    return this.MutationResult;
  }

  /**
   * @return Details what items of the Branch Key ID were changed on this invocation.
   */
  public List<MutatedBranchKeyItem> MutatedBranchKeyItems() {
    return this.MutatedBranchKeyItems;
  }

  /**
   * @return ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
   */
  public String LastModifiedTime() {
    return this.LastModifiedTime;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder MutationResult(ApplyMutationResult MutationResult);

    ApplyMutationResult MutationResult();

    /**
     * @param MutatedBranchKeyItems Details what items of the Branch Key ID were changed on this invocation.
     */
    Builder MutatedBranchKeyItems(
      List<MutatedBranchKeyItem> MutatedBranchKeyItems
    );

    /**
     * @return Details what items of the Branch Key ID were changed on this invocation.
     */
    List<MutatedBranchKeyItem> MutatedBranchKeyItems();

    /**
     * @param LastModifiedTime ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
     */
    Builder LastModifiedTime(String LastModifiedTime);

    /**
     * @return ISO 8601 timestamp of last time the Mutation was Initialized or Applied.
     */
    String LastModifiedTime();

    ApplyMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ApplyMutationResult MutationResult;

    protected List<MutatedBranchKeyItem> MutatedBranchKeyItems;

    protected String LastModifiedTime;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationOutput model) {
      this.MutationResult = model.MutationResult();
      this.MutatedBranchKeyItems = model.MutatedBranchKeyItems();
      this.LastModifiedTime = model.LastModifiedTime();
    }

    public Builder MutationResult(ApplyMutationResult MutationResult) {
      this.MutationResult = MutationResult;
      return this;
    }

    public ApplyMutationResult MutationResult() {
      return this.MutationResult;
    }

    public Builder MutatedBranchKeyItems(
      List<MutatedBranchKeyItem> MutatedBranchKeyItems
    ) {
      this.MutatedBranchKeyItems = MutatedBranchKeyItems;
      return this;
    }

    public List<MutatedBranchKeyItem> MutatedBranchKeyItems() {
      return this.MutatedBranchKeyItems;
    }

    public Builder LastModifiedTime(String LastModifiedTime) {
      this.LastModifiedTime = LastModifiedTime;
      return this;
    }

    public String LastModifiedTime() {
      return this.LastModifiedTime;
    }

    public ApplyMutationOutput build() {
      if (Objects.isNull(this.MutationResult())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationResult`"
        );
      }
      if (Objects.isNull(this.MutatedBranchKeyItems())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutatedBranchKeyItems`"
        );
      }
      if (Objects.isNull(this.LastModifiedTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `LastModifiedTime`"
        );
      }
      return new ApplyMutationOutput(this);
    }
  }
}
