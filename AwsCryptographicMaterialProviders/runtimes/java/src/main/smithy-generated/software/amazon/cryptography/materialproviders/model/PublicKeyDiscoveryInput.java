// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Inputs for creating a PublicKeyDiscovery Configuration.
 */
public class PublicKeyDiscoveryInput {

  /**
   * The sender's private key. MUST be PEM encoded.
   */
  private final ByteBuffer recipientStaticPrivateKey;

  protected PublicKeyDiscoveryInput(BuilderImpl builder) {
    this.recipientStaticPrivateKey = builder.recipientStaticPrivateKey();
  }

  /**
   * @return The sender's private key. MUST be PEM encoded.
   */
  public ByteBuffer recipientStaticPrivateKey() {
    return this.recipientStaticPrivateKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param recipientStaticPrivateKey The sender's private key. MUST be PEM encoded.
     */
    Builder recipientStaticPrivateKey(ByteBuffer recipientStaticPrivateKey);

    /**
     * @return The sender's private key. MUST be PEM encoded.
     */
    ByteBuffer recipientStaticPrivateKey();

    PublicKeyDiscoveryInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer recipientStaticPrivateKey;

    protected BuilderImpl() {}

    protected BuilderImpl(PublicKeyDiscoveryInput model) {
      this.recipientStaticPrivateKey = model.recipientStaticPrivateKey();
    }

    public Builder recipientStaticPrivateKey(
      ByteBuffer recipientStaticPrivateKey
    ) {
      this.recipientStaticPrivateKey = recipientStaticPrivateKey;
      return this;
    }

    public ByteBuffer recipientStaticPrivateKey() {
      return this.recipientStaticPrivateKey;
    }

    public PublicKeyDiscoveryInput build() {
      if (Objects.isNull(this.recipientStaticPrivateKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientStaticPrivateKey`"
        );
      }
      return new PublicKeyDiscoveryInput(this);
    }
  }
}
