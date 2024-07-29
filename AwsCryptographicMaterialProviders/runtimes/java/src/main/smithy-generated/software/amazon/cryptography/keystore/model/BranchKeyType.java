// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class BranchKeyType {

  private final String ActiveHierarchicalSymmetricVersion;

  private final String HierarchicalSymmetricVersion;

  private final ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon;

  protected BranchKeyType(BuilderImpl builder) {
    this.ActiveHierarchicalSymmetricVersion =
      builder.ActiveHierarchicalSymmetricVersion();
    this.HierarchicalSymmetricVersion = builder.HierarchicalSymmetricVersion();
    this.ActiveHierarchicalSymmetricBeacon =
      builder.ActiveHierarchicalSymmetricBeacon();
  }

  public String ActiveHierarchicalSymmetricVersion() {
    return this.ActiveHierarchicalSymmetricVersion;
  }

  public String HierarchicalSymmetricVersion() {
    return this.HierarchicalSymmetricVersion;
  }

  public ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon() {
    return this.ActiveHierarchicalSymmetricBeacon;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder ActiveHierarchicalSymmetricVersion(
      String ActiveHierarchicalSymmetricVersion
    );

    String ActiveHierarchicalSymmetricVersion();

    Builder HierarchicalSymmetricVersion(String HierarchicalSymmetricVersion);

    String HierarchicalSymmetricVersion();

    Builder ActiveHierarchicalSymmetricBeacon(
      ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon
    );

    ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon();

    BranchKeyType build();
  }

  static class BuilderImpl implements Builder {

    protected String ActiveHierarchicalSymmetricVersion;

    protected String HierarchicalSymmetricVersion;

    protected ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon;

    protected BuilderImpl() {}

    protected BuilderImpl(BranchKeyType model) {
      this.ActiveHierarchicalSymmetricVersion =
        model.ActiveHierarchicalSymmetricVersion();
      this.HierarchicalSymmetricVersion = model.HierarchicalSymmetricVersion();
      this.ActiveHierarchicalSymmetricBeacon =
        model.ActiveHierarchicalSymmetricBeacon();
    }

    public Builder ActiveHierarchicalSymmetricVersion(
      String ActiveHierarchicalSymmetricVersion
    ) {
      this.ActiveHierarchicalSymmetricVersion =
        ActiveHierarchicalSymmetricVersion;
      return this;
    }

    public String ActiveHierarchicalSymmetricVersion() {
      return this.ActiveHierarchicalSymmetricVersion;
    }

    public Builder HierarchicalSymmetricVersion(
      String HierarchicalSymmetricVersion
    ) {
      this.HierarchicalSymmetricVersion = HierarchicalSymmetricVersion;
      return this;
    }

    public String HierarchicalSymmetricVersion() {
      return this.HierarchicalSymmetricVersion;
    }

    public Builder ActiveHierarchicalSymmetricBeacon(
      ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon
    ) {
      this.ActiveHierarchicalSymmetricBeacon =
        ActiveHierarchicalSymmetricBeacon;
      return this;
    }

    public ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon() {
      return this.ActiveHierarchicalSymmetricBeacon;
    }

    public BranchKeyType build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`BranchKeyType` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new BranchKeyType(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.ActiveHierarchicalSymmetricVersion,
        this.HierarchicalSymmetricVersion,
        this.ActiveHierarchicalSymmetricBeacon,
      };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
