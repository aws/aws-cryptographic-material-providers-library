// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class MutatedBranchKeyItem {

  /**
   * The item type changed. i.e: branch:version:<uuid> or MUTATION_LOCK:<uuid>
   */
  private final String itemType;

  /**
   * Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Lock Created, Mutation Lock Removed.
   */
  private final String description;

  protected MutatedBranchKeyItem(BuilderImpl builder) {
    this.itemType = builder.itemType();
    this.description = builder.description();
  }

  /**
   * @return The item type changed. i.e: branch:version:<uuid> or MUTATION_LOCK:<uuid>
   */
  public String itemType() {
    return this.itemType;
  }

  /**
   * @return Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Lock Created, Mutation Lock Removed.
   */
  public String description() {
    return this.description;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param itemType The item type changed. i.e: branch:version:<uuid> or MUTATION_LOCK:<uuid>
     */
    Builder itemType(String itemType);

    /**
     * @return The item type changed. i.e: branch:version:<uuid> or MUTATION_LOCK:<uuid>
     */
    String itemType();

    /**
     * @param description Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Lock Created, Mutation Lock Removed.
     */
    Builder description(String description);

    /**
     * @return Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Lock Created, Mutation Lock Removed.
     */
    String description();

    MutatedBranchKeyItem build();
  }

  static class BuilderImpl implements Builder {

    protected String itemType;

    protected String description;

    protected BuilderImpl() {}

    protected BuilderImpl(MutatedBranchKeyItem model) {
      this.itemType = model.itemType();
      this.description = model.description();
    }

    public Builder itemType(String itemType) {
      this.itemType = itemType;
      return this;
    }

    public String itemType() {
      return this.itemType;
    }

    public Builder description(String description) {
      this.description = description;
      return this;
    }

    public String description() {
      return this.description;
    }

    public MutatedBranchKeyItem build() {
      if (Objects.isNull(this.itemType())) {
        throw new IllegalArgumentException(
          "Missing value for required field `itemType`"
        );
      }
      if (Objects.isNull(this.description())) {
        throw new IllegalArgumentException(
          "Missing value for required field `description`"
        );
      }
      return new MutatedBranchKeyItem(this);
    }
  }
}
