// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * List of configurations when using RawEcdhStaticConfigurations.
 */
public class RawEcdhStaticConfigurations {

  /**
   * Inputs for creating a PublicKeyDiscovery Configuration.
   */
  private final PublicKeyDiscoveryInput PublicKeyDiscovery;

  /**
   * Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.
   */
  private final RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey;

  /**
   * Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.
   */
  private final EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey;

  protected RawEcdhStaticConfigurations(BuilderImpl builder) {
    this.PublicKeyDiscovery = builder.PublicKeyDiscovery();
    this.RawPrivateKeyToStaticPublicKey =
      builder.RawPrivateKeyToStaticPublicKey();
    this.EphemeralPrivateKeyToStaticPublicKey =
      builder.EphemeralPrivateKeyToStaticPublicKey();
  }

  /**
   * @return Inputs for creating a PublicKeyDiscovery Configuration.
   */
  public PublicKeyDiscoveryInput PublicKeyDiscovery() {
    return this.PublicKeyDiscovery;
  }

  /**
   * @return Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.
   */
  public RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey() {
    return this.RawPrivateKeyToStaticPublicKey;
  }

  /**
   * @return Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.
   */
  public EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey() {
    return this.EphemeralPrivateKeyToStaticPublicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param PublicKeyDiscovery Inputs for creating a PublicKeyDiscovery Configuration.
     */
    Builder PublicKeyDiscovery(PublicKeyDiscoveryInput PublicKeyDiscovery);

    /**
     * @return Inputs for creating a PublicKeyDiscovery Configuration.
     */
    PublicKeyDiscoveryInput PublicKeyDiscovery();

    /**
     * @param RawPrivateKeyToStaticPublicKey Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.
     */
    Builder RawPrivateKeyToStaticPublicKey(
      RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey
    );

    /**
     * @return Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.
     */
    RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey();

    /**
     * @param EphemeralPrivateKeyToStaticPublicKey Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.
     */
    Builder EphemeralPrivateKeyToStaticPublicKey(
      EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey
    );

    /**
     * @return Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.
     */
    EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey();

    RawEcdhStaticConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected PublicKeyDiscoveryInput PublicKeyDiscovery;

    protected RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey;

    protected EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(RawEcdhStaticConfigurations model) {
      this.PublicKeyDiscovery = model.PublicKeyDiscovery();
      this.RawPrivateKeyToStaticPublicKey =
        model.RawPrivateKeyToStaticPublicKey();
      this.EphemeralPrivateKeyToStaticPublicKey =
        model.EphemeralPrivateKeyToStaticPublicKey();
    }

    public Builder PublicKeyDiscovery(
      PublicKeyDiscoveryInput PublicKeyDiscovery
    ) {
      this.PublicKeyDiscovery = PublicKeyDiscovery;
      return this;
    }

    public PublicKeyDiscoveryInput PublicKeyDiscovery() {
      return this.PublicKeyDiscovery;
    }

    public Builder RawPrivateKeyToStaticPublicKey(
      RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey
    ) {
      this.RawPrivateKeyToStaticPublicKey = RawPrivateKeyToStaticPublicKey;
      return this;
    }

    public RawPrivateKeyToStaticPublicKeyInput RawPrivateKeyToStaticPublicKey() {
      return this.RawPrivateKeyToStaticPublicKey;
    }

    public Builder EphemeralPrivateKeyToStaticPublicKey(
      EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey
    ) {
      this.EphemeralPrivateKeyToStaticPublicKey =
        EphemeralPrivateKeyToStaticPublicKey;
      return this;
    }

    public EphemeralPrivateKeyToStaticPublicKeyInput EphemeralPrivateKeyToStaticPublicKey() {
      return this.EphemeralPrivateKeyToStaticPublicKey;
    }

    public RawEcdhStaticConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`RawEcdhStaticConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new RawEcdhStaticConfigurations(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.PublicKeyDiscovery,
        this.RawPrivateKeyToStaticPublicKey,
        this.EphemeralPrivateKeyToStaticPublicKey,
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
