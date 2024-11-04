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
  private final OverWriteEncryptedHierarchicalKey Active;

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
  private final OverWriteEncryptedHierarchicalKey Beacon;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock MutationLock;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
    this.MutationLock = builder.MutationLock();
    this.MutationIndex = builder.MutationIndex();
  }

  /**
   * @return
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properities.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  public OverWriteEncryptedHierarchicalKey Active() {
    return this.Active;
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
  public OverWriteEncryptedHierarchicalKey Beacon() {
    return this.Beacon;
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  public MutationLock MutationLock() {
    return this.MutationLock;
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
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
    Builder Active(OverWriteEncryptedHierarchicalKey Active);

    /**
     * @return
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properities.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    OverWriteEncryptedHierarchicalKey Active();

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
    Builder Beacon(OverWriteEncryptedHierarchicalKey Beacon);

    /**
     * @return
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properities.
     */
    OverWriteEncryptedHierarchicalKey Beacon();

    /**
     * @param MutationLock Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock MutationLock();

    /**
     * @param MutationIndex Information on an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    WriteInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected OverWriteEncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected OverWriteEncryptedHierarchicalKey Beacon;

    protected MutationLock MutationLock;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
      this.MutationLock = model.MutationLock();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder Active(OverWriteEncryptedHierarchicalKey Active) {
      this.Active = Active;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey Active() {
      return this.Active;
    }

    public Builder Version(EncryptedHierarchicalKey Version) {
      this.Version = Version;
      return this;
    }

    public EncryptedHierarchicalKey Version() {
      return this.Version;
    }

    public Builder Beacon(OverWriteEncryptedHierarchicalKey Beacon) {
      this.Beacon = Beacon;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey Beacon() {
      return this.Beacon;
    }

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public Builder MutationIndex(MutationIndex MutationIndex) {
      this.MutationIndex = MutationIndex;
      return this;
    }

    public MutationIndex MutationIndex() {
      return this.MutationIndex;
    }

    public WriteInitializeMutationInput build() {
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
      if (Objects.isNull(this.MutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationLock`"
        );
      }
      if (Objects.isNull(this.MutationIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationIndex`"
        );
      }
      return new WriteInitializeMutationInput(this);
    }
  }
}
