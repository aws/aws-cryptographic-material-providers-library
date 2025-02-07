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
  private final MutationToken MutationToken;

  /**
   * Details what items of the Branch Key ID were changed on this invocation.
   */
  private final List<MutatedBranchKeyItem> MutatedBranchKeyItems;

  private final InitializeMutationFlag InitializeMutationFlag;

  private final String LastModifiedTime;

  protected InitializeMutationOutput(BuilderImpl builder) {
    this.MutationToken = builder.MutationToken();
    this.MutatedBranchKeyItems = builder.MutatedBranchKeyItems();
    this.InitializeMutationFlag = builder.InitializeMutationFlag();
    this.LastModifiedTime = builder.LastModifiedTime();
  }

  /**
   * @return Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
   */
  public MutationToken MutationToken() {
    return this.MutationToken;
  }

  /**
   * @return Details what items of the Branch Key ID were changed on this invocation.
   */
  public List<MutatedBranchKeyItem> MutatedBranchKeyItems() {
    return this.MutatedBranchKeyItems;
  }

  public InitializeMutationFlag InitializeMutationFlag() {
    return this.InitializeMutationFlag;
  }

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
    /**
     * @param MutationToken Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
     */
    Builder MutationToken(MutationToken MutationToken);

    /**
     * @return Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.
     */
    MutationToken MutationToken();

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

    Builder InitializeMutationFlag(
      InitializeMutationFlag InitializeMutationFlag
    );

    InitializeMutationFlag InitializeMutationFlag();

    Builder LastModifiedTime(String LastModifiedTime);

    String LastModifiedTime();

    InitializeMutationOutput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken MutationToken;

    protected List<MutatedBranchKeyItem> MutatedBranchKeyItems;

    protected InitializeMutationFlag InitializeMutationFlag;

    protected String LastModifiedTime;

    protected BuilderImpl() {}

    protected BuilderImpl(InitializeMutationOutput model) {
      this.MutationToken = model.MutationToken();
      this.MutatedBranchKeyItems = model.MutatedBranchKeyItems();
      this.InitializeMutationFlag = model.InitializeMutationFlag();
      this.LastModifiedTime = model.LastModifiedTime();
    }

    public Builder MutationToken(MutationToken MutationToken) {
      this.MutationToken = MutationToken;
      return this;
    }

    public MutationToken MutationToken() {
      return this.MutationToken;
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

    public Builder InitializeMutationFlag(
      InitializeMutationFlag InitializeMutationFlag
    ) {
      this.InitializeMutationFlag = InitializeMutationFlag;
      return this;
    }

    public InitializeMutationFlag InitializeMutationFlag() {
      return this.InitializeMutationFlag;
    }

    public Builder LastModifiedTime(String LastModifiedTime) {
      this.LastModifiedTime = LastModifiedTime;
      return this;
    }

    public String LastModifiedTime() {
      return this.LastModifiedTime;
    }

    public InitializeMutationOutput build() {
      if (Objects.isNull(this.MutationToken())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationToken`"
        );
      }
      if (Objects.isNull(this.MutatedBranchKeyItems())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutatedBranchKeyItems`"
        );
      }
      if (Objects.isNull(this.InitializeMutationFlag())) {
        throw new IllegalArgumentException(
          "Missing value for required field `InitializeMutationFlag`"
        );
      }
      return new InitializeMutationOutput(this);
    }
  }
}
