// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class WriteInitializeMutationInput {

  /**
   *
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properties.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  private final OverWriteEncryptedHierarchicalKey Active;

  /**
   *
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properties.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  private final WriteInitializeMutationVersion Version;

  /**
   *
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properties.
   */
  private final OverWriteEncryptedHierarchicalKey Beacon;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationCommitment MutationCommitment;

  /**
   * Information of an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
  }

  /**
   * @return
   *   The active representation of this branch key,
   *   generated with the Mutation's terminal properties.
   *   The plain-text cryptographic material of the Active must be the same as the Version.
   */
  public OverWriteEncryptedHierarchicalKey Active() {
    return this.Active;
  }

  /**
   * @return
   *   The decrypt representation of this branch key version,
   *   generated with the Mutation's terminal properties.
   *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
   */
  public WriteInitializeMutationVersion Version() {
    return this.Version;
  }

  /**
   * @return
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properties.
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
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return Information of an in-flight Mutation of a Branch Key.
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
     *   generated with the Mutation's terminal properties.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    Builder Active(OverWriteEncryptedHierarchicalKey Active);

    /**
     * @return
     *   The active representation of this branch key,
     *   generated with the Mutation's terminal properties.
     *   The plain-text cryptographic material of the Active must be the same as the Version.
     */
    OverWriteEncryptedHierarchicalKey Active();

    /**
     * @param Version
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properties.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    Builder Version(WriteInitializeMutationVersion Version);

    /**
     * @return
     *   The decrypt representation of this branch key version,
     *   generated with the Mutation's terminal properties.
     *   The plain-text cryptographic material of the `Version` must be the same as the `Active`.
     */
    WriteInitializeMutationVersion Version();

    /**
     * @param Beacon
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properties.
     */
    Builder Beacon(OverWriteEncryptedHierarchicalKey Beacon);

    /**
     * @return
     *   The mutated HMAC key used to support searchable encryption.
     *   The cryptographic material is identical to the existing beacon,
     *   but is now authorized with the Mutation's terminal properties.
     */
    OverWriteEncryptedHierarchicalKey Beacon();

    /**
     * @param MutationCommitment Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationCommitment(MutationCommitment MutationCommitment);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationCommitment MutationCommitment();

    /**
     * @param MutationIndex Information of an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information of an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    WriteInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected OverWriteEncryptedHierarchicalKey Active;

    protected WriteInitializeMutationVersion Version;

    protected OverWriteEncryptedHierarchicalKey Beacon;

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
    }

    public Builder Active(OverWriteEncryptedHierarchicalKey Active) {
      this.Active = Active;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey Active() {
      return this.Active;
    }

    public Builder Version(WriteInitializeMutationVersion Version) {
      this.Version = Version;
      return this;
    }

    public WriteInitializeMutationVersion Version() {
      return this.Version;
    }

    public Builder Beacon(OverWriteEncryptedHierarchicalKey Beacon) {
      this.Beacon = Beacon;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey Beacon() {
      return this.Beacon;
    }

    public Builder MutationCommitment(MutationCommitment MutationCommitment) {
      this.MutationCommitment = MutationCommitment;
      return this;
    }

    public MutationCommitment MutationCommitment() {
      return this.MutationCommitment;
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
      if (Objects.isNull(this.MutationCommitment())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationCommitment`"
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
