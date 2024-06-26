// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * List of configurations when using a RawEcdhConfiguration
 */
public class RawEcdhConfigurations {

  /**
   * Inputs for creating a StaticDiscoveryRecipient Configuration.
   */
  private final StaticDiscoveryRecipientInput StaticDiscoveryRecipient;

  /**
   * Inputs for creating a StaticSenderStaticRecipient Configuration.
   */
  private final StaticSenderStaticRecipientInput StaticSenderStaticRecipient;

  /**
   * Inputs for creating a EphemeralSenderToStaticRecipient Configuration.
   */
  private final EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient;

  protected RawEcdhConfigurations(BuilderImpl builder) {
    this.StaticDiscoveryRecipient = builder.StaticDiscoveryRecipient();
    this.StaticSenderStaticRecipient = builder.StaticSenderStaticRecipient();
    this.EphemeralSenderToStaticKmsRecipient =
      builder.EphemeralSenderToStaticKmsRecipient();
  }

  /**
   * @return Inputs for creating a StaticDiscoveryRecipient Configuration.
   */
  public StaticDiscoveryRecipientInput StaticDiscoveryRecipient() {
    return this.StaticDiscoveryRecipient;
  }

  /**
   * @return Inputs for creating a StaticSenderStaticRecipient Configuration.
   */
  public StaticSenderStaticRecipientInput StaticSenderStaticRecipient() {
    return this.StaticSenderStaticRecipient;
  }

  /**
   * @return Inputs for creating a EphemeralSenderToStaticRecipient Configuration.
   */
  public EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient() {
    return this.EphemeralSenderToStaticKmsRecipient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param StaticDiscoveryRecipient Inputs for creating a StaticDiscoveryRecipient Configuration.
     */
    Builder StaticDiscoveryRecipient(
      StaticDiscoveryRecipientInput StaticDiscoveryRecipient
    );

    /**
     * @return Inputs for creating a StaticDiscoveryRecipient Configuration.
     */
    StaticDiscoveryRecipientInput StaticDiscoveryRecipient();

    /**
     * @param StaticSenderStaticRecipient Inputs for creating a StaticSenderStaticRecipient Configuration.
     */
    Builder StaticSenderStaticRecipient(
      StaticSenderStaticRecipientInput StaticSenderStaticRecipient
    );

    /**
     * @return Inputs for creating a StaticSenderStaticRecipient Configuration.
     */
    StaticSenderStaticRecipientInput StaticSenderStaticRecipient();

    /**
     * @param EphemeralSenderToStaticKmsRecipient Inputs for creating a EphemeralSenderToStaticRecipient Configuration.
     */
    Builder EphemeralSenderToStaticKmsRecipient(
      EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient
    );

    /**
     * @return Inputs for creating a EphemeralSenderToStaticRecipient Configuration.
     */
    EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient();

    RawEcdhConfigurations build();
  }

  static class BuilderImpl implements Builder {

    protected StaticDiscoveryRecipientInput StaticDiscoveryRecipient;

    protected StaticSenderStaticRecipientInput StaticSenderStaticRecipient;

    protected EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient;

    protected BuilderImpl() {}

    protected BuilderImpl(RawEcdhConfigurations model) {
      this.StaticDiscoveryRecipient = model.StaticDiscoveryRecipient();
      this.StaticSenderStaticRecipient = model.StaticSenderStaticRecipient();
      this.EphemeralSenderToStaticKmsRecipient =
        model.EphemeralSenderToStaticKmsRecipient();
    }

    public Builder StaticDiscoveryRecipient(
      StaticDiscoveryRecipientInput StaticDiscoveryRecipient
    ) {
      this.StaticDiscoveryRecipient = StaticDiscoveryRecipient;
      return this;
    }

    public StaticDiscoveryRecipientInput StaticDiscoveryRecipient() {
      return this.StaticDiscoveryRecipient;
    }

    public Builder StaticSenderStaticRecipient(
      StaticSenderStaticRecipientInput StaticSenderStaticRecipient
    ) {
      this.StaticSenderStaticRecipient = StaticSenderStaticRecipient;
      return this;
    }

    public StaticSenderStaticRecipientInput StaticSenderStaticRecipient() {
      return this.StaticSenderStaticRecipient;
    }

    public Builder EphemeralSenderToStaticKmsRecipient(
      EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient
    ) {
      this.EphemeralSenderToStaticKmsRecipient =
        EphemeralSenderToStaticKmsRecipient;
      return this;
    }

    public EphemeralSenderToStaticRecipientInput EphemeralSenderToStaticKmsRecipient() {
      return this.EphemeralSenderToStaticKmsRecipient;
    }

    public RawEcdhConfigurations build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`RawEcdhConfigurations` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new RawEcdhConfigurations(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.StaticDiscoveryRecipient,
        this.StaticSenderStaticRecipient,
        this.EphemeralSenderToStaticKmsRecipient,
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
