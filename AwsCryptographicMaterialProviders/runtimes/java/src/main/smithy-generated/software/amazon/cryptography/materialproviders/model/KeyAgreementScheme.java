// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Supported ECDH Key Agreement Schemes.
 */
public class KeyAgreementScheme {

  /**
   * Supported configurations for the StaticConfiguration Key Agreement Scheme.
   */
  private final StaticConfigurations StaticConfiguration;

  protected KeyAgreementScheme(BuilderImpl builder) {
    this.StaticConfiguration = builder.StaticConfiguration();
  }

  /**
   * @return Supported configurations for the StaticConfiguration Key Agreement Scheme.
   */
  public StaticConfigurations StaticConfiguration() {
    return this.StaticConfiguration;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param StaticConfiguration Supported configurations for the StaticConfiguration Key Agreement Scheme.
     */
    Builder StaticConfiguration(StaticConfigurations StaticConfiguration);

    /**
     * @return Supported configurations for the StaticConfiguration Key Agreement Scheme.
     */
    StaticConfigurations StaticConfiguration();

    KeyAgreementScheme build();
  }

  static class BuilderImpl implements Builder {

    protected StaticConfigurations StaticConfiguration;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyAgreementScheme model) {
      this.StaticConfiguration = model.StaticConfiguration();
    }

    public Builder StaticConfiguration(
      StaticConfigurations StaticConfiguration
    ) {
      this.StaticConfiguration = StaticConfiguration;
      return this;
    }

    public StaticConfigurations StaticConfiguration() {
      return this.StaticConfiguration;
    }

    public KeyAgreementScheme build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KeyAgreementScheme` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KeyAgreementScheme(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.StaticConfiguration };
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
