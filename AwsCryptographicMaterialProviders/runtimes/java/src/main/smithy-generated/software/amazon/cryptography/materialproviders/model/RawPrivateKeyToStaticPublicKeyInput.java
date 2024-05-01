// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Inputs for creating a RawPrivateKeyToStaticPublicKey Configuration.
 */
public class RawPrivateKeyToStaticPublicKeyInput {

  /**
   * The sender's private key
   */
  private final ByteBuffer senderStaticPrivateKey;

  /**
   * The recipient's public key
   */
  private final ByteBuffer recipientPublicKey;

  protected RawPrivateKeyToStaticPublicKeyInput(BuilderImpl builder) {
    this.senderStaticPrivateKey = builder.senderStaticPrivateKey();
    this.recipientPublicKey = builder.recipientPublicKey();
  }

  /**
   * @return The sender's private key
   */
  public ByteBuffer senderStaticPrivateKey() {
    return this.senderStaticPrivateKey;
  }

  /**
   * @return The recipient's public key
   */
  public ByteBuffer recipientPublicKey() {
    return this.recipientPublicKey;
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

    /**
     * @param recipientPublicKey The recipient's public key
     */
    Builder recipientPublicKey(ByteBuffer recipientPublicKey);

    /**
     * @return The recipient's public key
     */
    ByteBuffer recipientPublicKey();

    RawPrivateKeyToStaticPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer senderStaticPrivateKey;

    protected ByteBuffer recipientPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(RawPrivateKeyToStaticPublicKeyInput model) {
      this.senderStaticPrivateKey = model.senderStaticPrivateKey();
      this.recipientPublicKey = model.recipientPublicKey();
    }

    public Builder senderStaticPrivateKey(ByteBuffer senderStaticPrivateKey) {
      this.senderStaticPrivateKey = senderStaticPrivateKey;
      return this;
    }

    public ByteBuffer senderStaticPrivateKey() {
      return this.senderStaticPrivateKey;
    }

    public Builder recipientPublicKey(ByteBuffer recipientPublicKey) {
      this.recipientPublicKey = recipientPublicKey;
      return this;
    }

    public ByteBuffer recipientPublicKey() {
      return this.recipientPublicKey;
    }

    public RawPrivateKeyToStaticPublicKeyInput build() {
      if (Objects.isNull(this.senderStaticPrivateKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderStaticPrivateKey`"
        );
      }
      if (Objects.isNull(this.recipientPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientPublicKey`"
        );
      }
      return new RawPrivateKeyToStaticPublicKeyInput(this);
    }
  }
}
