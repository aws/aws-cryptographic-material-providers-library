// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteInitializeMutationInput {

  /**
   *
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  private final EncryptedHierarchicalKey Active;

  /**
   *
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   */
  private final EncryptedHierarchicalKey OldActive;

  /**
   *
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  private final EncryptedHierarchicalKey Version;

  /**
   *
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properities.
   */
  private final EncryptedHierarchicalKey Beacon;

  /**
   * Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock MutationLock;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.OldActive = builder.OldActive();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
    this.MutationLock = builder.MutationLock();
  }

  /**
   * @return
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  public EncryptedHierarchicalKey Active() {
    return this.Active;
  }

  /**
   * @return
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   */
  public EncryptedHierarchicalKey OldActive() {
    return this.OldActive;
  }

  /**
   * @return
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  public EncryptedHierarchicalKey Version() {
    return this.Version;
  }

  /**
   * @return
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properities.
   */
  public EncryptedHierarchicalKey Beacon() {
    return this.Beacon;
  }

  /**
   * @return Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  public MutationLock MutationLock() {
    return this.MutationLock;
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
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    Builder Active(EncryptedHierarchicalKey Active);

    /**
     * @return
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    EncryptedHierarchicalKey Active();

    /**
     * @param OldActive
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     */
    Builder OldActive(EncryptedHierarchicalKey OldActive);

    /**
     * @return
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     */
    EncryptedHierarchicalKey OldActive();

    /**
     * @param Version
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    Builder Version(EncryptedHierarchicalKey Version);

    /**
     * @return
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    EncryptedHierarchicalKey Version();

    /**
     * @param Beacon
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properities.
     */
    Builder Beacon(EncryptedHierarchicalKey Beacon);

    /**
     * @return
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properities.
     */
    EncryptedHierarchicalKey Beacon();

    /**
     * @param MutationLock Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock MutationLock();

    WriteInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey OldActive;

    protected EncryptedHierarchicalKey Version;

    protected EncryptedHierarchicalKey Beacon;

    protected MutationLock MutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
      this.Active = model.Active();
      this.OldActive = model.OldActive();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
      this.MutationLock = model.MutationLock();
    }

    public Builder Active(EncryptedHierarchicalKey Active) {
      this.Active = Active;
      return this;
    }

    public EncryptedHierarchicalKey Active() {
      return this.Active;
    }

    public Builder OldActive(EncryptedHierarchicalKey OldActive) {
      this.OldActive = OldActive;
      return this;
    }

    public EncryptedHierarchicalKey OldActive() {
      return this.OldActive;
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

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public WriteInitializeMutationInput build() {
      if (Objects.isNull(this.Active())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Active`"
        );
      }
      if (Objects.isNull(this.OldActive())) {
        throw new IllegalArgumentException(
          "Missing value for required field `OldActive`"
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
      if (Objects.isNull(this.MutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationLock`"
        );
      }
      return new WriteInitializeMutationInput(this);
    }
  }
}
