// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteNewKeyInput {

  private final EncryptedHierarchicalKey Active;

  private final EncryptedHierarchicalKey Version;

  private final EncryptedHierarchicalKey Beacon;

  protected WriteNewKeyInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
  }

  public EncryptedHierarchicalKey Active() {
    return this.Active;
  }

  public EncryptedHierarchicalKey Version() {
    return this.Version;
  }

  public EncryptedHierarchicalKey Beacon() {
    return this.Beacon;
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

    Builder Beacon(EncryptedHierarchicalKey Beacon);

    EncryptedHierarchicalKey Beacon();

    WriteNewKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected EncryptedHierarchicalKey Beacon;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewKeyInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
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

    public Builder Beacon(EncryptedHierarchicalKey Beacon) {
      this.Beacon = Beacon;
      return this;
    }

    public EncryptedHierarchicalKey Beacon() {
      return this.Beacon;
    }

    public WriteNewKeyInput build() {
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
      if (Objects.isNull(this.Beacon())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Beacon`"
        );
      }
      return new WriteNewKeyInput(this);
    }
  }
}
