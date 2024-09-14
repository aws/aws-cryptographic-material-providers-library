// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteItemsForInitializeMutationInput {

  private final EncryptedHierarchicalKey active;

  private final EncryptedHierarchicalKey oldActive;

  private final EncryptedHierarchicalKey version;

  private final EncryptedHierarchicalKey beacon;

  private final MutationLock mutationLock;

  protected WriteItemsForInitializeMutationInput(BuilderImpl builder) {
    this.active = builder.active();
    this.oldActive = builder.oldActive();
    this.version = builder.version();
    this.beacon = builder.beacon();
    this.mutationLock = builder.mutationLock();
  }

  public EncryptedHierarchicalKey active() {
    return this.active;
  }

  public EncryptedHierarchicalKey oldActive() {
    return this.oldActive;
  }

  public EncryptedHierarchicalKey version() {
    return this.version;
  }

  public EncryptedHierarchicalKey beacon() {
    return this.beacon;
  }

  public MutationLock mutationLock() {
    return this.mutationLock;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder active(EncryptedHierarchicalKey active);

    EncryptedHierarchicalKey active();

    Builder oldActive(EncryptedHierarchicalKey oldActive);

    EncryptedHierarchicalKey oldActive();

    Builder version(EncryptedHierarchicalKey version);

    EncryptedHierarchicalKey version();

    Builder beacon(EncryptedHierarchicalKey beacon);

    EncryptedHierarchicalKey beacon();

    Builder mutationLock(MutationLock mutationLock);

    MutationLock mutationLock();

    WriteItemsForInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey active;

    protected EncryptedHierarchicalKey oldActive;

    protected EncryptedHierarchicalKey version;

    protected EncryptedHierarchicalKey beacon;

    protected MutationLock mutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteItemsForInitializeMutationInput model) {
      this.active = model.active();
      this.oldActive = model.oldActive();
      this.version = model.version();
      this.beacon = model.beacon();
      this.mutationLock = model.mutationLock();
    }

    public Builder active(EncryptedHierarchicalKey active) {
      this.active = active;
      return this;
    }

    public EncryptedHierarchicalKey active() {
      return this.active;
    }

    public Builder oldActive(EncryptedHierarchicalKey oldActive) {
      this.oldActive = oldActive;
      return this;
    }

    public EncryptedHierarchicalKey oldActive() {
      return this.oldActive;
    }

    public Builder version(EncryptedHierarchicalKey version) {
      this.version = version;
      return this;
    }

    public EncryptedHierarchicalKey version() {
      return this.version;
    }

    public Builder beacon(EncryptedHierarchicalKey beacon) {
      this.beacon = beacon;
      return this;
    }

    public EncryptedHierarchicalKey beacon() {
      return this.beacon;
    }

    public Builder mutationLock(MutationLock mutationLock) {
      this.mutationLock = mutationLock;
      return this;
    }

    public MutationLock mutationLock() {
      return this.mutationLock;
    }

    public WriteItemsForInitializeMutationInput build() {
      if (Objects.isNull(this.active())) {
        throw new IllegalArgumentException(
          "Missing value for required field `active`"
        );
      }
      if (Objects.isNull(this.oldActive())) {
        throw new IllegalArgumentException(
          "Missing value for required field `oldActive`"
        );
      }
      if (Objects.isNull(this.version())) {
        throw new IllegalArgumentException(
          "Missing value for required field `version`"
        );
      }
      if (Objects.isNull(this.beacon())) {
        throw new IllegalArgumentException(
          "Missing value for required field `beacon`"
        );
      }
      if (Objects.isNull(this.mutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutationLock`"
        );
      }
      return new WriteItemsForInitializeMutationInput(this);
    }
  }
}
