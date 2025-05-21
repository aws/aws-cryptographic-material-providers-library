// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * Inputs for creating a KmsPublicKeyDiscovery Configuration. This is a DECRYPT ONLY configuration.
 */
public class KmsPublicKeyDiscoveryInput {

  /**
   * AWS KMS key identifier belonging to the recipient.
   */
  private final String recipientKmsIdentifier;

  protected KmsPublicKeyDiscoveryInput(BuilderImpl builder) {
    this.recipientKmsIdentifier = builder.recipientKmsIdentifier();
  }

  /**
   * @return AWS KMS key identifier belonging to the recipient.
   */
  public String recipientKmsIdentifier() {
    return this.recipientKmsIdentifier;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param recipientKmsIdentifier AWS KMS key identifier belonging to the recipient.
     */
    Builder recipientKmsIdentifier(String recipientKmsIdentifier);

    /**
     * @return AWS KMS key identifier belonging to the recipient.
     */
    String recipientKmsIdentifier();

    KmsPublicKeyDiscoveryInput build();
  }

  static class BuilderImpl implements Builder {

    protected String recipientKmsIdentifier;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsPublicKeyDiscoveryInput model) {
      this.recipientKmsIdentifier = model.recipientKmsIdentifier();
    }

    public Builder recipientKmsIdentifier(String recipientKmsIdentifier) {
      this.recipientKmsIdentifier = recipientKmsIdentifier;
      return this;
    }

    public String recipientKmsIdentifier() {
      return this.recipientKmsIdentifier;
    }

    public KmsPublicKeyDiscoveryInput build() {
      if (Objects.isNull(this.recipientKmsIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientKmsIdentifier`"
        );
      }
      return new KmsPublicKeyDiscoveryInput(this);
    }
  }
}
