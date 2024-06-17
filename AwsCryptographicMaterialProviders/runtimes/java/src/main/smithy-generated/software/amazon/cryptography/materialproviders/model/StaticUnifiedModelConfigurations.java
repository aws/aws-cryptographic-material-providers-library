// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Supported configurations for the StaticUnifiedModel Key Agreement Scheme
 */
public class StaticUnifiedModelConfigurations {

  /**
   * Allowed configurations when using a KmsEcdhConfiguration
   */
  private final KmsEcdhConfigurations AWS_KMS_ECDH;

  /**
   * List of configurations when using a RawEcdhConfiguration
   */
  private final RawEcdhConfigurations RAW_ECDH;

  protected StaticUnifiedModelConfigurations(BuilderImpl builder) {
    this.AWS_KMS_ECDH = builder.AWS_KMS_ECDH();
    this.RAW_ECDH = builder.RAW_ECDH();
  }

  /**
   * @return Allowed configurations when using a KmsEcdhConfiguration
   */
  public KmsEcdhConfigurations AWS_KMS_ECDH() {
    return this.AWS_KMS_ECDH;
  }

  /**
   * @return List of configurations when using a RawEcdhConfiguration
   */
  public RawEcdhConfigurations RAW_ECDH() {
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
     * @param AWS_KMS_ECDH Allowed configurations when using a KmsEcdhConfiguration
     */
    Builder AWS_KMS_ECDH(KmsEcdhConfigurations AWS_KMS_ECDH);

    /**
     * @return Allowed configurations when using a KmsEcdhConfiguration
     */
    KmsEcdhConfigurations AWS_KMS_ECDH();

    /**
     * @param RAW_ECDH List of configurations when using a RawEcdhConfiguration
     */
    Builder RAW_ECDH(RawEcdhConfigurations RAW_ECDH);

    /**
     * @return List of configurations when using a RawEcdhConfiguration
     */
    RawEcdhConfigurations RAW_ECDH();

    StaticUnifiedModelConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected KmsEcdhConfigurations AWS_KMS_ECDH;

    protected RawEcdhConfigurations RAW_ECDH;

    protected BuilderImpl() {}

    protected BuilderImpl(StaticUnifiedModelConfigurations model) {
      this.AWS_KMS_ECDH = model.AWS_KMS_ECDH();
      this.RAW_ECDH = model.RAW_ECDH();
    }

    public Builder AWS_KMS_ECDH(KmsEcdhConfigurations AWS_KMS_ECDH) {
      this.AWS_KMS_ECDH = AWS_KMS_ECDH;
      return this;
    }

    public KmsEcdhConfigurations AWS_KMS_ECDH() {
      return this.AWS_KMS_ECDH;
    }

    public Builder RAW_ECDH(RawEcdhConfigurations RAW_ECDH) {
      this.RAW_ECDH = RAW_ECDH;
      return this;
    }

    public RawEcdhConfigurations RAW_ECDH() {
      return this.RAW_ECDH;
    }

    public StaticUnifiedModelConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`StaticUnifiedModelConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new StaticUnifiedModelConfigurations(this);
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
