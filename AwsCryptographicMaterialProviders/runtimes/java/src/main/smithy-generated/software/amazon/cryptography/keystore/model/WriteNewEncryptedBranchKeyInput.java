// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 *
 * The information required to atomically write an a new branch key into a key store.
 * The identifiers for all keys passed should be the same.
 */
public class WriteNewEncryptedBranchKeyInput {

  /**
   *
   *   The active representation of this branch key.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   *
   */
  private final EncryptedHierarchicalKey Active;

  /**
   *
   *   The decrypt representation of this branch key.
   *   The plain-text cryptographic material of the Version must be the same as the Active.
   *
   */
  private final EncryptedHierarchicalKey Version;

  /**
   *
   *   An HMAC key used to support searchable encryption.
   *   This should be a different cryptographic material from the other two.
   *
   */
  private final EncryptedHierarchicalKey Beacon;

  protected WriteNewEncryptedBranchKeyInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
  }

  /**
   * @return
   *   The active representation of this branch key.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   *
   */
  public EncryptedHierarchicalKey Active() {
    return this.Active;
  }

  /**
   * @return
   *   The decrypt representation of this branch key.
   *   The plain-text cryptographic material of the Version must be the same as the Active.
   *
   */
  public EncryptedHierarchicalKey Version() {
    return this.Version;
  }

  /**
   * @return
   *   An HMAC key used to support searchable encryption.
   *   This should be a different cryptographic material from the other two.
   *
   */
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
    /**
     * @param Active
     *   The active representation of this branch key.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     *
     */
    Builder Active(EncryptedHierarchicalKey Active);

    /**
     * @return
     *   The active representation of this branch key.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     *
     */
    EncryptedHierarchicalKey Active();

    /**
     * @param Version
     *   The decrypt representation of this branch key.
     *   The plain-text cryptographic material of the Version must be the same as the Active.
     *
     */
    Builder Version(EncryptedHierarchicalKey Version);

    /**
     * @return
     *   The decrypt representation of this branch key.
     *   The plain-text cryptographic material of the Version must be the same as the Active.
     *
     */
    EncryptedHierarchicalKey Version();

    /**
     * @param Beacon
     *   An HMAC key used to support searchable encryption.
     *   This should be a different cryptographic material from the other two.
     *
     */
    Builder Beacon(EncryptedHierarchicalKey Beacon);

    /**
     * @return
     *   An HMAC key used to support searchable encryption.
     *   This should be a different cryptographic material from the other two.
     *
     */
    EncryptedHierarchicalKey Beacon();

    WriteNewEncryptedBranchKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected EncryptedHierarchicalKey Beacon;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteNewEncryptedBranchKeyInput model) {
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

    public WriteNewEncryptedBranchKeyInput build() {
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
      return new WriteNewEncryptedBranchKeyInput(this);
    }
  }
}
