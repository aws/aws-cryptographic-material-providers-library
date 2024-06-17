// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.primitives.model.ECDHCurveSpec;

/**
 * Inputs for creating a raw ECDH Keyring.
 */
public class CreateRawEcdhKeyringInput {

  /**
   * The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
   */
  private final RawEcdhStaticConfigurations KeyAgreementScheme;

  /**
   * The the curve on which the points for the sender's private and recipient's public key lie.
   */
  private final ECDHCurveSpec curveSpec;

  protected CreateRawEcdhKeyringInput(BuilderImpl builder) {
    this.KeyAgreementScheme = builder.KeyAgreementScheme();
    this.curveSpec = builder.curveSpec();
  }

  /**
   * @return The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
   */
  public RawEcdhStaticConfigurations KeyAgreementScheme() {
    return this.KeyAgreementScheme;
  }

  /**
   * @return The the curve on which the points for the sender's private and recipient's public key lie.
   */
  public ECDHCurveSpec curveSpec() {
    return this.curveSpec;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KeyAgreementScheme The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
     */
    Builder KeyAgreementScheme(RawEcdhStaticConfigurations KeyAgreementScheme);

    /**
     * @return The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
     */
    RawEcdhStaticConfigurations KeyAgreementScheme();

    /**
     * @param curveSpec The the curve on which the points for the sender's private and recipient's public key lie.
     */
    Builder curveSpec(ECDHCurveSpec curveSpec);

    /**
     * @return The the curve on which the points for the sender's private and recipient's public key lie.
     */
    ECDHCurveSpec curveSpec();

    CreateRawEcdhKeyringInput build();
  }

  static class BuilderImpl implements Builder {

    protected RawEcdhStaticConfigurations KeyAgreementScheme;

    protected ECDHCurveSpec curveSpec;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateRawEcdhKeyringInput model) {
      this.KeyAgreementScheme = model.KeyAgreementScheme();
      this.curveSpec = model.curveSpec();
    }

    public Builder KeyAgreementScheme(
      RawEcdhStaticConfigurations KeyAgreementScheme
    ) {
      this.KeyAgreementScheme = KeyAgreementScheme;
      return this;
    }

    public RawEcdhStaticConfigurations KeyAgreementScheme() {
      return this.KeyAgreementScheme;
    }

    public Builder curveSpec(ECDHCurveSpec curveSpec) {
      this.curveSpec = curveSpec;
      return this;
    }

    public ECDHCurveSpec curveSpec() {
      return this.curveSpec;
    }

    public CreateRawEcdhKeyringInput build() {
      if (Objects.isNull(this.KeyAgreementScheme())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KeyAgreementScheme`"
        );
      }
      if (Objects.isNull(this.curveSpec())) {
        throw new IllegalArgumentException(
          "Missing value for required field `curveSpec`"
        );
      }
      return new CreateRawEcdhKeyringInput(this);
    }
  }
}
