// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Information for the active symmetric branch key.
 */
public class ActiveHierarchicalSymmetric {

  /**
   * The version of this active key.
   */
  private final String Version;

  protected ActiveHierarchicalSymmetric(BuilderImpl builder) {
    this.Version = builder.Version();
  }

  /**
   * @return The version of this active key.
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
     * @param Version The version of this active key.
     */
    Builder Version(String Version);

    /**
     * @return The version of this active key.
     */
    String Version();

    ActiveHierarchicalSymmetric build();
  }

  static class BuilderImpl implements Builder {

    protected String Version;

    protected BuilderImpl() {}

    protected BuilderImpl(ActiveHierarchicalSymmetric model) {
      this.Version = model.Version();
    }

    public Builder Version(String Version) {
      this.Version = Version;
      return this;
    }

    public String Version() {
      return this.Version;
    }

    public ActiveHierarchicalSymmetric build() {
      if (Objects.isNull(this.Version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Version`"
        );
      }
      return new ActiveHierarchicalSymmetric(this);
    }
  }
}
