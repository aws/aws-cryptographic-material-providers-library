// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class MutatedBranchKeyItem {

  /**
   * The item type changed. i.e: branch:version:<uuid> or branch:MUTATION_COMMITMENT.
   */
  private final String ItemType;

  /**
   * Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Commitment Created, Mutation Commitment Removed.
   */
  private final String Description;

  protected MutatedBranchKeyItem(BuilderImpl builder) {
    this.ItemType = builder.ItemType();
    this.Description = builder.Description();
  }

  /**
   * @return The item type changed. i.e: branch:version:<uuid> or branch:MUTATION_COMMITMENT.
   */
  public String ItemType() {
    return this.ItemType;
  }

  /**
   * @return Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Commitment Created, Mutation Commitment Removed.
   */
  public String Description() {
    return this.Description;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ItemType The item type changed. i.e: branch:version:<uuid> or branch:MUTATION_COMMITMENT.
     */
    Builder ItemType(String ItemType);

    /**
     * @return The item type changed. i.e: branch:version:<uuid> or branch:MUTATION_COMMITMENT.
     */
    String ItemType();

    /**
     * @param Description Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Commitment Created, Mutation Commitment Removed.
     */
    Builder Description(String Description);

    /**
     * @return Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Commitment Created, Mutation Commitment Removed.
     */
    String Description();

    MutatedBranchKeyItem build();
  }

  static class BuilderImpl implements Builder {

    protected String ItemType;

    protected String Description;

    protected BuilderImpl() {}

    protected BuilderImpl(MutatedBranchKeyItem model) {
      this.ItemType = model.ItemType();
      this.Description = model.Description();
    }

    public Builder ItemType(String ItemType) {
      this.ItemType = ItemType;
      return this;
    }

    public String ItemType() {
      return this.ItemType;
    }

    public Builder Description(String Description) {
      this.Description = Description;
      return this;
    }

    public String Description() {
      return this.Description;
    }

    public MutatedBranchKeyItem build() {
      if (Objects.isNull(this.ItemType())) {
        throw new IllegalArgumentException(
          "Missing value for required field `ItemType`"
        );
      }
      if (Objects.isNull(this.Description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Description`"
        );
      }
      return new MutatedBranchKeyItem(this);
    }
  }
}
