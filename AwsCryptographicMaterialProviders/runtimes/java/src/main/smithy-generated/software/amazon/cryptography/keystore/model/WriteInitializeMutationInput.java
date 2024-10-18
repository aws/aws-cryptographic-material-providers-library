// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
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
  private final MutationCommitment MutationCommitment;

  /**
   * Information on an in-flight Mutation of a Branch Key.
   */
  private final MutationIndex MutationIndex;

  /**
   * List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  private final List<OverWriteEncryptedHierarchicalKey> Versions;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
    this.Versions = builder.Versions();
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
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return Information on an in-flight Mutation of a Branch Key.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  /**
   * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  public List<OverWriteEncryptedHierarchicalKey> Versions() {
    return this.Versions;
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
     * @param MutationIndex Information on an in-flight Mutation of a Branch Key.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return Information on an in-flight Mutation of a Branch Key.
     */
    MutationIndex MutationIndex();

    /**
     * @param Versions List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    Builder Versions(List<OverWriteEncryptedHierarchicalKey> Versions);

    /**
     * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    List<OverWriteEncryptedHierarchicalKey> Versions();

    WriteInitializeMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected OverWriteEncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected OverWriteEncryptedHierarchicalKey Beacon;

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected List<OverWriteEncryptedHierarchicalKey> Versions;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
      this.Versions = model.Versions();
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

    public Builder Versions(List<OverWriteEncryptedHierarchicalKey> Versions) {
      this.Versions = Versions;
      return this;
    }

    public List<OverWriteEncryptedHierarchicalKey> Versions() {
      return this.Versions;
    }

    public WriteInitializeMutationInput build() {
      if (Objects.isNull(this.Beacon())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Beacon`"
        );
      }
      if (Objects.isNull(this.Versions())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Versions`"
        );
      }
      return new WriteInitializeMutationInput(this);
    }
  }
}
