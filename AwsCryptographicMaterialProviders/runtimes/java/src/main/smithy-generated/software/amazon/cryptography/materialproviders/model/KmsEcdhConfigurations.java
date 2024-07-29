// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Allowed configurations when using a KmsEcdhConfiguration
 */
public class KmsEcdhConfigurations {

  /**
   * Inputs for creating a RecipientDiscoveryScheme Configuration. This is a DECRYPT ONLY configuration
   */
  private final RecipientDiscoverySchemeInput RecipientDiscoveryScheme;

  /**
   * Inputs for creating a KmsSenderToStaticRecipient Configuration.
   */
  private final KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient;

  protected KmsEcdhConfigurations(BuilderImpl builder) {
    this.RecipientDiscoveryScheme = builder.RecipientDiscoveryScheme();
    this.KmsSenderToStaticRecipient = builder.KmsSenderToStaticRecipient();
  }

  /**
   * @return Inputs for creating a RecipientDiscoveryScheme Configuration. This is a DECRYPT ONLY configuration
   */
  public RecipientDiscoverySchemeInput RecipientDiscoveryScheme() {
    return this.RecipientDiscoveryScheme;
  }

  /**
   * @return Inputs for creating a KmsSenderToStaticRecipient Configuration.
   */
  public KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient() {
    return this.KmsSenderToStaticRecipient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param RecipientDiscoveryScheme Inputs for creating a RecipientDiscoveryScheme Configuration. This is a DECRYPT ONLY configuration
     */
    Builder RecipientDiscoveryScheme(
      RecipientDiscoverySchemeInput RecipientDiscoveryScheme
    );

    /**
     * @return Inputs for creating a RecipientDiscoveryScheme Configuration. This is a DECRYPT ONLY configuration
     */
    RecipientDiscoverySchemeInput RecipientDiscoveryScheme();

    /**
     * @param KmsSenderToStaticRecipient Inputs for creating a KmsSenderToStaticRecipient Configuration.
     */
    Builder KmsSenderToStaticRecipient(
      KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient
    );

    /**
     * @return Inputs for creating a KmsSenderToStaticRecipient Configuration.
     */
    KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient();

    KmsEcdhConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected RecipientDiscoverySchemeInput RecipientDiscoveryScheme;

    protected KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsEcdhConfigurations model) {
      this.RecipientDiscoveryScheme = model.RecipientDiscoveryScheme();
      this.KmsSenderToStaticRecipient = model.KmsSenderToStaticRecipient();
    }

    public Builder RecipientDiscoveryScheme(
      RecipientDiscoverySchemeInput RecipientDiscoveryScheme
    ) {
      this.RecipientDiscoveryScheme = RecipientDiscoveryScheme;
      return this;
    }

    public RecipientDiscoverySchemeInput RecipientDiscoveryScheme() {
      return this.RecipientDiscoveryScheme;
    }

    public Builder KmsSenderToStaticRecipient(
      KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient
    ) {
      this.KmsSenderToStaticRecipient = KmsSenderToStaticRecipient;
      return this;
    }

    public KmsSenderToStaticRecipientInput KmsSenderToStaticRecipient() {
      return this.KmsSenderToStaticRecipient;
    }

    public KmsEcdhConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KmsEcdhConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KmsEcdhConfigurations(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.RecipientDiscoveryScheme,
        this.KmsSenderToStaticRecipient,
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
