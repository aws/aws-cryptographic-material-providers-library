// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Information for a specific decrypt only branch key version.
 */
public class HierarchicalSymmetric {

  /**
   * The version of this key.
   */
  private final String Version;

  protected HierarchicalSymmetric(BuilderImpl builder) {
    this.Version = builder.Version();
  }

  /**
   * @return The version of this key.
   */
  public String Version() {
    return this.Version;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Version The version of this key.
     */
    Builder Version(String Version);

    /**
     * @return The version of this key.
     */
    String Version();

    HierarchicalSymmetric build();
  }

  static class BuilderImpl implements Builder {

    protected String Version;

    protected BuilderImpl() {}

    protected BuilderImpl(HierarchicalSymmetric model) {
      this.Version = model.Version();
    }

    public Builder Version(String Version) {
      this.Version = Version;
      return this;
    }

    public String Version() {
      return this.Version;
    }

    public HierarchicalSymmetric build() {
      if (Objects.isNull(this.Version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Version`"
        );
      }
      return new HierarchicalSymmetric(this);
    }
  }
}
