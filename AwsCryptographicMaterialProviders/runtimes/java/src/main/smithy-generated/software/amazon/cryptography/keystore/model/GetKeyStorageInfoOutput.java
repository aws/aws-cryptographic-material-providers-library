// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Output containing information about the underlying storage.
 */
public class GetKeyStorageInfoOutput {

  /**
   * The name of the physical resource used for storage.
   */
  private final String Name;

  /**
   * The Logical Key Store Name associated with this Storage.
   */
  private final String LogicalName;

  protected GetKeyStorageInfoOutput(BuilderImpl builder) {
    this.Name = builder.Name();
    this.LogicalName = builder.LogicalName();
  }

  /**
   * @return The name of the physical resource used for storage.
   */
  public String Name() {
    return this.Name;
  }

  /**
   * @return The Logical Key Store Name associated with this Storage.
   */
  public String LogicalName() {
    return this.LogicalName;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Name The name of the physical resource used for storage.
     */
    Builder Name(String Name);

    /**
     * @return The name of the physical resource used for storage.
     */
    String Name();

    /**
     * @param LogicalName The Logical Key Store Name associated with this Storage.
     */
    Builder LogicalName(String LogicalName);

    /**
     * @return The Logical Key Store Name associated with this Storage.
     */
    String LogicalName();

    GetKeyStorageInfoOutput build();
  }

  static class BuilderImpl implements Builder {

    protected String Name;

    protected String LogicalName;

    protected BuilderImpl() {}

    protected BuilderImpl(GetKeyStorageInfoOutput model) {
      this.Name = model.Name();
      this.LogicalName = model.LogicalName();
    }

    public Builder Name(String Name) {
      this.Name = Name;
      return this;
    }

    public String Name() {
      return this.Name;
    }

    public Builder LogicalName(String LogicalName) {
      this.LogicalName = LogicalName;
      return this;
    }

    public String LogicalName() {
      return this.LogicalName;
    }

    public GetKeyStorageInfoOutput build() {
      if (Objects.isNull(this.Name())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Name`"
        );
      }
      if (Objects.isNull(this.LogicalName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `LogicalName`"
        );
      }
      return new GetKeyStorageInfoOutput(this);
    }
  }
}
