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
  private final EncryptedHierarchicalKey active;

  /**
   *
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   */
  private final EncryptedHierarchicalKey oldActive;

  /**
   *
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  private final EncryptedHierarchicalKey version;

  /**
   *
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properities.
   */
  private final EncryptedHierarchicalKey beacon;

  /**
   * Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock mutationLock;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.active = builder.active();
    this.oldActive = builder.oldActive();
    this.version = builder.version();
    this.beacon = builder.beacon();
    this.mutationLock = builder.mutationLock();
  }

  /**
   * @return
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  public EncryptedHierarchicalKey active() {
    return this.active;
  }

  /**
   * @return
   *   The previous active version.
   *   This key should be used as an optimistic lock on the new version.
   *   This means that when updating the current active record
   *   the existing active record should be equal to this value.
   */
  public EncryptedHierarchicalKey oldActive() {
    return this.oldActive;
  }

  /**
   * @return
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  public EncryptedHierarchicalKey version() {
    return this.version;
  }

  /**
   * @return
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properities.
   */
  public EncryptedHierarchicalKey beacon() {
    return this.beacon;
  }

  /**
   * @return Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
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
    /**
     * @param active
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    Builder active(EncryptedHierarchicalKey active);

    /**
     * @return
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    EncryptedHierarchicalKey active();

    /**
     * @param oldActive
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     */
    Builder oldActive(EncryptedHierarchicalKey oldActive);

    /**
     * @return
     *   The previous active version.
     *   This key should be used as an optimistic lock on the new version.
     *   This means that when updating the current active record
     *   the existing active record should be equal to this value.
     */
    EncryptedHierarchicalKey oldActive();

    /**
     * @param version
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    Builder version(EncryptedHierarchicalKey version);

    /**
     * @return
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    EncryptedHierarchicalKey version();

    /**
     * @param beacon
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properities.
     */
    Builder beacon(EncryptedHierarchicalKey beacon);

    /**
     * @return
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properities.
     */
    EncryptedHierarchicalKey beacon();

    /**
     * @param mutationLock Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder mutationLock(MutationLock mutationLock);

    /**
     * @return Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock mutationLock();

    WriteInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected EncryptedHierarchicalKey active;

    protected EncryptedHierarchicalKey oldActive;

    protected EncryptedHierarchicalKey version;

    protected EncryptedHierarchicalKey beacon;

    protected MutationLock mutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
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

    public WriteInitializeMutationInput build() {
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
      return new WriteInitializeMutationInput(this);
    }
  }
}
