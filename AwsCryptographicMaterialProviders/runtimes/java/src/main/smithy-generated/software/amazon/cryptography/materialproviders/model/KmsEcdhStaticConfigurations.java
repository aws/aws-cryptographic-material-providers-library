// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Allowed configurations when using KmsEcdhStaticConfigurations.
 */
public class KmsEcdhStaticConfigurations {

  /**
   * Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.
   */
  private final KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery;

  /**
   * Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
   */
  private final KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey;

  protected KmsEcdhStaticConfigurations(BuilderImpl builder) {
    this.KmsPublicKeyDiscovery = builder.KmsPublicKeyDiscovery();
    this.KmsPrivateKeyToStaticPublicKey =
      builder.KmsPrivateKeyToStaticPublicKey();
  }

  /**
   * @return Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.
   */
  public KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery() {
    return this.KmsPublicKeyDiscovery;
  }

  /**
   * @return Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
   */
  public KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey() {
    return this.KmsPrivateKeyToStaticPublicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KmsPublicKeyDiscovery Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.
     */
    Builder KmsPublicKeyDiscovery(
      KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery
    );

    /**
     * @return Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.
     */
    KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery();

    /**
     * @param KmsPrivateKeyToStaticPublicKey Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
     */
    Builder KmsPrivateKeyToStaticPublicKey(
      KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey
    );

    /**
     * @return Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
     */
    KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey();

    KmsEcdhStaticConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery;

    protected KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsEcdhStaticConfigurations model) {
      this.KmsPublicKeyDiscovery = model.KmsPublicKeyDiscovery();
      this.KmsPrivateKeyToStaticPublicKey =
        model.KmsPrivateKeyToStaticPublicKey();
    }

    public Builder KmsPublicKeyDiscovery(
      KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery
    ) {
      this.KmsPublicKeyDiscovery = KmsPublicKeyDiscovery;
      return this;
    }

    public KmsPublicKeyDiscoveryInput KmsPublicKeyDiscovery() {
      return this.KmsPublicKeyDiscovery;
    }

    public Builder KmsPrivateKeyToStaticPublicKey(
      KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey
    ) {
      this.KmsPrivateKeyToStaticPublicKey = KmsPrivateKeyToStaticPublicKey;
      return this;
    }

    public KmsPrivateKeyToStaticPublicKeyInput KmsPrivateKeyToStaticPublicKey() {
      return this.KmsPrivateKeyToStaticPublicKey;
    }

    public KmsEcdhStaticConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KmsEcdhStaticConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KmsEcdhStaticConfigurations(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.KmsPublicKeyDiscovery,
        this.KmsPrivateKeyToStaticPublicKey,
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
