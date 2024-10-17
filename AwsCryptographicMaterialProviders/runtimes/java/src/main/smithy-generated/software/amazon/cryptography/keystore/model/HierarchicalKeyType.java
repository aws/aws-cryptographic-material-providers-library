// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Describes the key that an encrypted blob represents.
 */
public class HierarchicalKeyType {

  /**
   * The version the active branch key. This version is used to encrypt messages.
   */
  private final ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion;

  /**
   * The version for a decrypt only branch key type. These are used to decrypt messages. For every ACTIVE that has ever been, there exists a Version.
   */
  private final HierarchicalSymmetric HierarchicalSymmetricVersion;

  /**
   * The information regarding a symmetric beacon key.
   */
  private final ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon;

  protected HierarchicalKeyType(BuilderImpl builder) {
    this.ActiveHierarchicalSymmetricVersion =
      builder.ActiveHierarchicalSymmetricVersion();
    this.HierarchicalSymmetricVersion = builder.HierarchicalSymmetricVersion();
    this.ActiveHierarchicalSymmetricBeacon =
      builder.ActiveHierarchicalSymmetricBeacon();
  }

  /**
   * @return The version the active branch key. This version is used to encrypt messages.
   */
  public ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion() {
    return this.ActiveHierarchicalSymmetricVersion;
  }

  /**
   * @return The version for a decrypt only branch key type. These are used to decrypt messages. For every ACTIVE that has ever been, there exists a Version.
   */
  public HierarchicalSymmetric HierarchicalSymmetricVersion() {
    return this.HierarchicalSymmetricVersion;
  }

  /**
   * @return The information regarding a symmetric beacon key.
   */
  public ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon() {
    return this.ActiveHierarchicalSymmetricBeacon;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ActiveHierarchicalSymmetricVersion The version the active branch key. This version is used to encrypt messages.
     */
    Builder ActiveHierarchicalSymmetricVersion(
      ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion
    );

    /**
     * @return The version the active branch key. This version is used to encrypt messages.
     */
    ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion();

    /**
     * @param HierarchicalSymmetricVersion The version for a decrypt only branch key type. These are used to decrypt messages. For every ACTIVE that has ever been, there exists a Version.
     */
    Builder HierarchicalSymmetricVersion(
      HierarchicalSymmetric HierarchicalSymmetricVersion
    );

    /**
     * @return The version for a decrypt only branch key type. These are used to decrypt messages. For every ACTIVE that has ever been, there exists a Version.
     */
    HierarchicalSymmetric HierarchicalSymmetricVersion();

    /**
     * @param ActiveHierarchicalSymmetricBeacon The information regarding a symmetric beacon key.
     */
    Builder ActiveHierarchicalSymmetricBeacon(
      ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon
    );

    /**
     * @return The information regarding a symmetric beacon key.
     */
    ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon();

    HierarchicalKeyType build();
  }

  static class BuilderImpl implements Builder {

    protected ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion;

    protected HierarchicalSymmetric HierarchicalSymmetricVersion;

    protected ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon;

    protected BuilderImpl() {}

    protected BuilderImpl(HierarchicalKeyType model) {
      this.ActiveHierarchicalSymmetricVersion =
        model.ActiveHierarchicalSymmetricVersion();
      this.HierarchicalSymmetricVersion = model.HierarchicalSymmetricVersion();
      this.ActiveHierarchicalSymmetricBeacon =
        model.ActiveHierarchicalSymmetricBeacon();
    }

    public Builder ActiveHierarchicalSymmetricVersion(
      ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion
    ) {
      this.ActiveHierarchicalSymmetricVersion =
        ActiveHierarchicalSymmetricVersion;
      return this;
    }

    public ActiveHierarchicalSymmetric ActiveHierarchicalSymmetricVersion() {
      return this.ActiveHierarchicalSymmetricVersion;
    }

    public Builder HierarchicalSymmetricVersion(
      HierarchicalSymmetric HierarchicalSymmetricVersion
    ) {
      this.HierarchicalSymmetricVersion = HierarchicalSymmetricVersion;
      return this;
    }

    public HierarchicalSymmetric HierarchicalSymmetricVersion() {
      return this.HierarchicalSymmetricVersion;
    }

    public Builder ActiveHierarchicalSymmetricBeacon(
      ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon
    ) {
      this.ActiveHierarchicalSymmetricBeacon =
        ActiveHierarchicalSymmetricBeacon;
      return this;
    }

    public ActiveHierarchicalSymmetricBeacon ActiveHierarchicalSymmetricBeacon() {
      return this.ActiveHierarchicalSymmetricBeacon;
    }

    public HierarchicalKeyType build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`HierarchicalKeyType` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new HierarchicalKeyType(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.ActiveHierarchicalSymmetricVersion,
        this.HierarchicalSymmetricVersion,
        this.ActiveHierarchicalSymmetricBeacon,
      };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
