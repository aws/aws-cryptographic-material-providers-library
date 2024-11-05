// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

public class WriteAtomicMutationInput {

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
   * List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  private final List<OverWriteEncryptedHierarchicalKey> Items;

  protected WriteAtomicMutationInput(BuilderImpl builder) {
    this.Active = builder.Active();
    this.Version = builder.Version();
    this.Beacon = builder.Beacon();
    this.Items = builder.Items();
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
   * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
   */
  public List<OverWriteEncryptedHierarchicalKey> Items() {
    return this.Items;
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
     * @param Items List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    Builder Items(List<OverWriteEncryptedHierarchicalKey> Items);

    /**
     * @return List of version (decrypt only) items of a Branch Key to overwrite conditionally.
     */
    List<OverWriteEncryptedHierarchicalKey> Items();

    WriteAtomicMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected OverWriteEncryptedHierarchicalKey Active;

    protected WriteInitializeMutationVersion Version;

    protected OverWriteEncryptedHierarchicalKey Beacon;

    protected List<OverWriteEncryptedHierarchicalKey> Items;

    protected BuilderImpl() {}

    protected BuilderImpl(WriteAtomicMutationInput model) {
      this.Active = model.Active();
      this.Version = model.Version();
      this.Beacon = model.Beacon();
      this.Items = model.Items();
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

    public Builder Items(List<OverWriteEncryptedHierarchicalKey> Items) {
      this.Items = Items;
      return this;
    }

    public List<OverWriteEncryptedHierarchicalKey> Items() {
      return this.Items;
    }

    public WriteAtomicMutationInput build() {
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
      if (Objects.isNull(this.Items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Items`"
        );
      }
      return new WriteAtomicMutationInput(this);
    }
  }
}
