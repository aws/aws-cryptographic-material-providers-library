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
   * The sender's private key
   */
  private final ByteBuffer senderStaticPrivateKey;

  protected PublicKeyDiscoveryInput(BuilderImpl builder) {
    this.senderStaticPrivateKey = builder.senderStaticPrivateKey();
  }

  /**
   * @return The sender's private key
   */
  public ByteBuffer senderStaticPrivateKey() {
    return this.senderStaticPrivateKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param senderStaticPrivateKey The sender's private key
     */
    Builder senderStaticPrivateKey(ByteBuffer senderStaticPrivateKey);

    /**
     * @return The sender's private key
     */
    ByteBuffer senderStaticPrivateKey();

    PublicKeyDiscoveryInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer senderStaticPrivateKey;

    protected BuilderImpl() {}

    protected BuilderImpl(PublicKeyDiscoveryInput model) {
      this.senderStaticPrivateKey = model.senderStaticPrivateKey();
    }

    public Builder senderStaticPrivateKey(ByteBuffer senderStaticPrivateKey) {
      this.senderStaticPrivateKey = senderStaticPrivateKey;
      return this;
    }

    public ByteBuffer senderStaticPrivateKey() {
      return this.senderStaticPrivateKey;
    }

    public PublicKeyDiscoveryInput build() {
      if (Objects.isNull(this.senderStaticPrivateKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderStaticPrivateKey`"
        );
      }
      return new PublicKeyDiscoveryInput(this);
    }
  }
}
