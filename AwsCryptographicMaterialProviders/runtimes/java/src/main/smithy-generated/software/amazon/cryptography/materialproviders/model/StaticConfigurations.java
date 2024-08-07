// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Supported configurations for the StaticConfiguration Key Agreement Scheme.
 */
public class StaticConfigurations {

  /**
   * Allowed configurations when using KmsEcdhStaticConfigurations.
   */
  private final KmsEcdhStaticConfigurations AWS_KMS_ECDH;

  /**
   * List of configurations when using RawEcdhStaticConfigurations.
   */
  private final RawEcdhStaticConfigurations RAW_ECDH;

  protected StaticConfigurations(BuilderImpl builder) {
    this.AWS_KMS_ECDH = builder.AWS_KMS_ECDH();
    this.RAW_ECDH = builder.RAW_ECDH();
  }

  /**
   * @return Allowed configurations when using KmsEcdhStaticConfigurations.
   */
  public KmsEcdhStaticConfigurations AWS_KMS_ECDH() {
    return this.AWS_KMS_ECDH;
  }

  /**
   * @return List of configurations when using RawEcdhStaticConfigurations.
   */
  public RawEcdhStaticConfigurations RAW_ECDH() {
    return this.RAW_ECDH;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param AWS_KMS_ECDH Allowed configurations when using KmsEcdhStaticConfigurations.
     */
    Builder AWS_KMS_ECDH(KmsEcdhStaticConfigurations AWS_KMS_ECDH);

    /**
     * @return Allowed configurations when using KmsEcdhStaticConfigurations.
     */
    KmsEcdhStaticConfigurations AWS_KMS_ECDH();

    /**
     * @param RAW_ECDH List of configurations when using RawEcdhStaticConfigurations.
     */
    Builder RAW_ECDH(RawEcdhStaticConfigurations RAW_ECDH);

    /**
     * @return List of configurations when using RawEcdhStaticConfigurations.
     */
    RawEcdhStaticConfigurations RAW_ECDH();

    StaticConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected KmsEcdhStaticConfigurations AWS_KMS_ECDH;

    protected RawEcdhStaticConfigurations RAW_ECDH;

    protected BuilderImpl() {}

    protected BuilderImpl(StaticConfigurations model) {
      this.AWS_KMS_ECDH = model.AWS_KMS_ECDH();
      this.RAW_ECDH = model.RAW_ECDH();
    }

    public Builder AWS_KMS_ECDH(KmsEcdhStaticConfigurations AWS_KMS_ECDH) {
      this.AWS_KMS_ECDH = AWS_KMS_ECDH;
      return this;
    }

    public KmsEcdhStaticConfigurations AWS_KMS_ECDH() {
      return this.AWS_KMS_ECDH;
    }

    public Builder RAW_ECDH(RawEcdhStaticConfigurations RAW_ECDH) {
      this.RAW_ECDH = RAW_ECDH;
      return this;
    }

    public RawEcdhStaticConfigurations RAW_ECDH() {
      return this.RAW_ECDH;
    }

    public StaticConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`StaticConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new StaticConfigurations(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.AWS_KMS_ECDH, this.RAW_ECDH };
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
