// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

public class WriteInitializeMutationInput {

  /**
   *
   *   The mutated HMAC key used to support searchable encryption.
   *   The cryptographic material is identical to the existing beacon,
   *   but is now authorized with the Mutation's terminal properities.
   */
  private final OverWriteEncryptedHierarchicalKey Beacon;

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
   * If Mutation is non-automic, a commitment is required.
   */
  private final MutationCommitment MutationCommitment;

  /**
   * If Mutation is non-automic, an index is required.
   */
  private final MutationIndex MutationIndex;

  /**
   * If Mutation is being resumed, an overwrite index is required.
   */
  private final OverWriteMutationIndex OverWriteMutationIndex;

  /**
   * List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  private final List<OverWriteEncryptedHierarchicalKey> Versions;

  protected WriteInitializeMutationInput(BuilderImpl builder) {
    this.Beacon = builder.Beacon();
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.MutationCommitment = builder.MutationCommitment();
    this.MutationIndex = builder.MutationIndex();
    this.OverWriteMutationIndex = builder.OverWriteMutationIndex();
    this.Versions = builder.Versions();
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
   * @return If Mutation is non-automic, a commitment is required.
   */
  public MutationCommitment MutationCommitment() {
    return this.MutationCommitment;
  }

  /**
   * @return If Mutation is non-automic, an index is required.
   */
  public MutationIndex MutationIndex() {
    return this.MutationIndex;
  }

  /**
   * @return If Mutation is being resumed, an overwrite index is required.
   */
  public OverWriteMutationIndex OverWriteMutationIndex() {
    return this.OverWriteMutationIndex;
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
     * @param MutationCommitment If Mutation is non-automic, a commitment is required.
     */
    Builder MutationCommitment(MutationCommitment MutationCommitment);

    /**
     * @return If Mutation is non-automic, a commitment is required.
     */
    MutationCommitment MutationCommitment();

    /**
     * @param MutationIndex If Mutation is non-automic, an index is required.
     */
    Builder MutationIndex(MutationIndex MutationIndex);

    /**
     * @return If Mutation is non-automic, an index is required.
     */
    MutationIndex MutationIndex();

    /**
     * @param OverWriteMutationIndex If Mutation is being resumed, an overwrite index is required.
     */
    Builder OverWriteMutationIndex(
      OverWriteMutationIndex OverWriteMutationIndex
    );

    /**
     * @return If Mutation is being resumed, an overwrite index is required.
     */
    OverWriteMutationIndex OverWriteMutationIndex();

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

    protected OverWriteEncryptedHierarchicalKey Beacon;

    protected OverWriteEncryptedHierarchicalKey Active;

    protected EncryptedHierarchicalKey Version;

    protected MutationCommitment MutationCommitment;

    protected MutationIndex MutationIndex;

    protected OverWriteMutationIndex OverWriteMutationIndex;

    protected List<OverWriteEncryptedHierarchicalKey> Versions;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteInitializeMutationInput model) {
      this.Beacon = model.Beacon();
      this.Active = model.Active();
      this.Version = model.Version();
      this.MutationCommitment = model.MutationCommitment();
      this.MutationIndex = model.MutationIndex();
      this.OverWriteMutationIndex = model.OverWriteMutationIndex();
      this.Versions = model.Versions();
    }

    public Builder Beacon(OverWriteEncryptedHierarchicalKey Beacon) {
      this.Beacon = Beacon;
      return this;
    }

    public OverWriteEncryptedHierarchicalKey Beacon() {
      return this.Beacon;
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

    public Builder OverWriteMutationIndex(
      OverWriteMutationIndex OverWriteMutationIndex
    ) {
      this.OverWriteMutationIndex = OverWriteMutationIndex;
      return this;
    }

    public OverWriteMutationIndex OverWriteMutationIndex() {
      return this.OverWriteMutationIndex;
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
