// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Inputs for creating a EphemeralPrivateKeyToStaticPublicKey Configuration.
 */
public class EphemeralPrivateKeyToStaticPublicKeyInput {

  /**
   * The recipient's public key. MUST be DER encoded.
   */
  private final ByteBuffer recipientPublicKey;

  protected EphemeralPrivateKeyToStaticPublicKeyInput(BuilderImpl builder) {
    this.recipientPublicKey = builder.recipientPublicKey();
  }

  /**
   * @return The recipient's public key. MUST be DER encoded.
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
     * @param recipientPublicKey The recipient's public key. MUST be DER encoded.
     */
    Builder recipientPublicKey(ByteBuffer recipientPublicKey);

    /**
     * @return The recipient's public key. MUST be DER encoded.
     */
    ByteBuffer recipientPublicKey();

    EphemeralPrivateKeyToStaticPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer recipientPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(EphemeralPrivateKeyToStaticPublicKeyInput model) {
      this.recipientPublicKey = model.recipientPublicKey();
    }

    public Builder recipientPublicKey(ByteBuffer recipientPublicKey) {
      this.recipientPublicKey = recipientPublicKey;
      return this;
    }

    public ByteBuffer recipientPublicKey() {
      return this.recipientPublicKey;
    }

    public EphemeralPrivateKeyToStaticPublicKeyInput build() {
      if (Objects.isNull(this.recipientPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientPublicKey`"
        );
      }
      return new EphemeralPrivateKeyToStaticPublicKeyInput(this);
    }
  }
}
