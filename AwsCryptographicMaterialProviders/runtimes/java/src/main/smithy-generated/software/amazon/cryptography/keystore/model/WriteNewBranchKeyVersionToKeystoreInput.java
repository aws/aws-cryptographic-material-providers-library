// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteNewBranchKeyVersionToKeystoreInput {

  private final EncryptedHierarchicalKey Active;

  private final EncryptedHierarchicalKey Version;

  private final EncryptedHierarchicalKey oldActive;

  protected WriteNewBranchKeyVersionToKeystoreInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.oldActive = builder.oldActive();
  }

  public EncryptedHierarchicalKey Active() {
    return this.Active;
  }

  public EncryptedHierarchicalKey Version() {
    return this.Version;
  }

  public EncryptedHierarchicalKey oldActive() {
    return this.oldActive;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder Active(EncryptedHierarchicalKey Active);

    EncryptedHierarchicalKey Active();

    Builder Version(EncryptedHierarchicalKey Version);

    EncryptedHierarchicalKey Version();

    Builder oldActive(EncryptedHierarchicalKey oldActive);

    EncryptedHierarchicalKey oldActive();

    WriteNewBranchKeyVersionToKeystoreInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected EncryptedHierarchicalKey oldActive;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewBranchKeyVersionToKeystoreInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.oldActive = model.oldActive();
    }

    public Builder Active(EncryptedHierarchicalKey Active) {
      this.Active = Active;
      return this;
    }

    public EncryptedHierarchicalKey Active() {
      return this.Active;
    }

    public Builder Version(EncryptedHierarchicalKey Version) {
      this.Version = Version;
      return this;
    }

    public EncryptedHierarchicalKey Version() {
      return this.Version;
    }

    public Builder oldActive(EncryptedHierarchicalKey oldActive) {
      this.oldActive = oldActive;
      return this;
    }

    public EncryptedHierarchicalKey oldActive() {
      return this.oldActive;
    }

    public WriteNewBranchKeyVersionToKeystoreInput build() {
      if (Objects.isNull(this.Active())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Active`"
        );
      }
      if (Objects.isNull(this.Version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Version`"
        );
      }
      if (Objects.isNull(this.oldActive())) {
        throw new IllegalArgumentException(
          "Missing value for required field `oldActive`"
        );
      }
      return new WriteNewBranchKeyVersionToKeystoreInput(this);
    }
  }
}
