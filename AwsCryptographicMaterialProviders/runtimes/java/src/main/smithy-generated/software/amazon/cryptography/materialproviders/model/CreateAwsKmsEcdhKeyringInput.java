// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.List;
import java.util.Objects;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.primitives.model.ECDHCurveSpec;

/**
 * Inputs for creating an AWS KMS ECDH Keyring.
 */
public class CreateAwsKmsEcdhKeyringInput {

  /**
   * The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
   */
  private final KmsEcdhStaticConfigurations KeyAgreementScheme;

  /**
   * The named curve that corresponds to the curve on which the sender's private and recipient's public key lie.
   */
  private final ECDHCurveSpec curveSpec;

  /**
   * The KMS Client this Keyring will use to call KMS.
   */
  private final KmsClient kmsClient;

  /**
   * A list of grant tokens to be used when calling KMS.
   */
  private final List<String> grantTokens;

  protected CreateAwsKmsEcdhKeyringInput(BuilderImpl builder) {
    this.KeyAgreementScheme = builder.KeyAgreementScheme();
    this.curveSpec = builder.curveSpec();
    this.kmsClient = builder.kmsClient();
    this.grantTokens = builder.grantTokens();
  }

  /**
   * @return The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
   */
  public KmsEcdhStaticConfigurations KeyAgreementScheme() {
    return this.KeyAgreementScheme;
  }

  /**
   * @return The named curve that corresponds to the curve on which the sender's private and recipient's public key lie.
   */
  public ECDHCurveSpec curveSpec() {
    return this.curveSpec;
  }

  /**
   * @return The KMS Client this Keyring will use to call KMS.
   */
  public KmsClient kmsClient() {
    return this.kmsClient;
  }

  /**
   * @return A list of grant tokens to be used when calling KMS.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
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
    Builder KeyAgreementScheme(KmsEcdhStaticConfigurations KeyAgreementScheme);

    /**
     * @return The Key Agreement Scheme configuration that is responsible for how the shared secret is calculated.
     */
    KmsEcdhStaticConfigurations KeyAgreementScheme();

    /**
     * @param curveSpec The named curve that corresponds to the curve on which the sender's private and recipient's public key lie.
     */
    Builder curveSpec(ECDHCurveSpec curveSpec);

    /**
     * @return The named curve that corresponds to the curve on which the sender's private and recipient's public key lie.
     */
    ECDHCurveSpec curveSpec();

    /**
     * @param kmsClient The KMS Client this Keyring will use to call KMS.
     */
    Builder kmsClient(KmsClient kmsClient);

    /**
     * @return The KMS Client this Keyring will use to call KMS.
     */
    KmsClient kmsClient();

    /**
     * @param grantTokens A list of grant tokens to be used when calling KMS.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return A list of grant tokens to be used when calling KMS.
     */
    List<String> grantTokens();

    CreateAwsKmsEcdhKeyringInput build();
  }

  static class BuilderImpl implements Builder {

    protected KmsEcdhStaticConfigurations KeyAgreementScheme;

    protected ECDHCurveSpec curveSpec;

    protected KmsClient kmsClient;

    protected List<String> grantTokens;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateAwsKmsEcdhKeyringInput model) {
      this.KeyAgreementScheme = model.KeyAgreementScheme();
      this.curveSpec = model.curveSpec();
      this.kmsClient = model.kmsClient();
      this.grantTokens = model.grantTokens();
    }

    public Builder KeyAgreementScheme(
      KmsEcdhStaticConfigurations KeyAgreementScheme
    ) {
      this.KeyAgreementScheme = KeyAgreementScheme;
      return this;
    }

    public KmsEcdhStaticConfigurations KeyAgreementScheme() {
      return this.KeyAgreementScheme;
    }

    public Builder curveSpec(ECDHCurveSpec curveSpec) {
      this.curveSpec = curveSpec;
      return this;
    }

    public ECDHCurveSpec curveSpec() {
      return this.curveSpec;
    }

    public Builder kmsClient(KmsClient kmsClient) {
      this.kmsClient = kmsClient;
      return this;
    }

    public KmsClient kmsClient() {
      return this.kmsClient;
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public CreateAwsKmsEcdhKeyringInput build() {
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
      if (Objects.isNull(this.kmsClient())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsClient`"
        );
      }
      return new CreateAwsKmsEcdhKeyringInput(this);
    }
  }
}
