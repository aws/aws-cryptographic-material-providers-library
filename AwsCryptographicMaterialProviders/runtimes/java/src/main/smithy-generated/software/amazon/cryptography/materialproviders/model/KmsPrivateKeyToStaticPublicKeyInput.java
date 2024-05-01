// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
 */
public class KmsPrivateKeyToStaticPublicKeyInput {

  /**
   * AWS KMS Key Identifier belonging to the sender
   */
  private final String senderKmsIdentifier;

  /**
   * Recipient configuration. This can be either a KMS key identifier or a raw public key
   */
  private final KmsRecipientConfiguration recipientConfiguration;

  protected KmsPrivateKeyToStaticPublicKeyInput(BuilderImpl builder) {
    this.senderKmsIdentifier = builder.senderKmsIdentifier();
    this.recipientConfiguration = builder.recipientConfiguration();
  }

  /**
   * @return AWS KMS Key Identifier belonging to the sender
   */
  public String senderKmsIdentifier() {
    return this.senderKmsIdentifier;
  }

  /**
   * @return Recipient configuration. This can be either a KMS key identifier or a raw public key
   */
  public KmsRecipientConfiguration recipientConfiguration() {
    return this.recipientConfiguration;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param senderKmsIdentifier AWS KMS Key Identifier belonging to the sender
     */
    Builder senderKmsIdentifier(String senderKmsIdentifier);

    /**
     * @return AWS KMS Key Identifier belonging to the sender
     */
    String senderKmsIdentifier();

    /**
     * @param recipientConfiguration Recipient configuration. This can be either a KMS key identifier or a raw public key
     */
    Builder recipientConfiguration(
      KmsRecipientConfiguration recipientConfiguration
    );

    /**
     * @return Recipient configuration. This can be either a KMS key identifier or a raw public key
     */
    KmsRecipientConfiguration recipientConfiguration();

    KmsPrivateKeyToStaticPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String senderKmsIdentifier;

    protected KmsRecipientConfiguration recipientConfiguration;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsPrivateKeyToStaticPublicKeyInput model) {
      this.senderKmsIdentifier = model.senderKmsIdentifier();
      this.recipientConfiguration = model.recipientConfiguration();
    }

    public Builder senderKmsIdentifier(String senderKmsIdentifier) {
      this.senderKmsIdentifier = senderKmsIdentifier;
      return this;
    }

    public String senderKmsIdentifier() {
      return this.senderKmsIdentifier;
    }

    public Builder recipientConfiguration(
      KmsRecipientConfiguration recipientConfiguration
    ) {
      this.recipientConfiguration = recipientConfiguration;
      return this;
    }

    public KmsRecipientConfiguration recipientConfiguration() {
      return this.recipientConfiguration;
    }

    public KmsPrivateKeyToStaticPublicKeyInput build() {
      if (Objects.isNull(this.senderKmsIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderKmsIdentifier`"
        );
      }
      if (Objects.isNull(this.recipientConfiguration())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientConfiguration`"
        );
      }
      return new KmsPrivateKeyToStaticPublicKeyInput(this);
    }
  }
}
