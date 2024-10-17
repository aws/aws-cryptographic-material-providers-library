// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 *
 * The information required to atomically write a new version for an existing branch key into a key store.
 * The identifiers for all keys passed should be the same.
 */
public class WriteNewEncryptedBranchKeyVersionInput {

  /**
   *
   *   The new active version to be written to the key store.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   *
   */
  private final EncryptedHierarchicalKey Active;

  /**
   *
   *   The decrypt representation of this branch key version.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   *
   */
  private final EncryptedHierarchicalKey Version;

  /**
   *
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   *
   */
  private final EncryptedHierarchicalKey OldActive;

  protected WriteNewEncryptedBranchKeyVersionInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.OldActive = builder.OldActive();
  }

  /**
   * @return
   *   The new active version to be written to the key store.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   *
   */
  public EncryptedHierarchicalKey Active() {
    return this.Active;
  }

  /**
   * @return
   *   The decrypt representation of this branch key version.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   *
   */
  public EncryptedHierarchicalKey Version() {
    return this.Version;
  }

  /**
   * @return
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   *
   */
  public EncryptedHierarchicalKey OldActive() {
    return this.OldActive;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Active
     *   The new active version to be written to the key store.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     *
     */
    Builder Active(EncryptedHierarchicalKey Active);

    /**
     * @return
     *   The new active version to be written to the key store.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     *
     */
    EncryptedHierarchicalKey Active();

    /**
     * @param Version
     *   The decrypt representation of this branch key version.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     *
     */
    Builder Version(EncryptedHierarchicalKey Version);

    /**
     * @return
     *   The decrypt representation of this branch key version.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     *
     */
    EncryptedHierarchicalKey Version();

    /**
     * @param OldActive
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     *
     */
    Builder OldActive(EncryptedHierarchicalKey OldActive);

    /**
     * @return
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     *
     */
    EncryptedHierarchicalKey OldActive();

    WriteNewEncryptedBranchKeyVersionInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected EncryptedHierarchicalKey OldActive;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewEncryptedBranchKeyVersionInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.OldActive = model.OldActive();
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

    public Builder OldActive(EncryptedHierarchicalKey OldActive) {
      this.OldActive = OldActive;
      return this;
    }

    public EncryptedHierarchicalKey OldActive() {
      return this.OldActive;
    }

    public WriteNewEncryptedBranchKeyVersionInput build() {
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
      if (Objects.isNull(this.OldActive())) {
        throw new IllegalArgumentException(
          "Missing value for required field `OldActive`"
        );
      }
      return new WriteNewEncryptedBranchKeyVersionInput(this);
    }
  }
}
