// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Inputs for creating a KmsPrivateKeyToStaticPublicKey Configuration.
 */
public class KmsPrivateKeyToStaticPublicKeyInput {

  /**
   * AWS KMS Key Identifier belonging to the sender.
   */
  private final String senderKmsIdentifier;

  /**
   * Sender Public Key. This is the raw public ECC key in DER format that belongs to the senderKmsIdentifier.
   */
  private final ByteBuffer senderPublicKey;

  /**
   * Recipient Public Key. This MUST be a raw public ECC key in DER format.
   */
  private final ByteBuffer recipientPublicKey;

  protected KmsPrivateKeyToStaticPublicKeyInput(BuilderImpl builder) {
    this.senderKmsIdentifier = builder.senderKmsIdentifier();
    this.senderPublicKey = builder.senderPublicKey();
    this.recipientPublicKey = builder.recipientPublicKey();
  }

  /**
   * @return AWS KMS Key Identifier belonging to the sender.
   */
  public String senderKmsIdentifier() {
    return this.senderKmsIdentifier;
  }

  /**
   * @return Sender Public Key. This is the raw public ECC key in DER format that belongs to the senderKmsIdentifier.
   */
  public ByteBuffer senderPublicKey() {
    return this.senderPublicKey;
  }

  /**
   * @return Recipient Public Key. This MUST be a raw public ECC key in DER format.
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
     * @param senderKmsIdentifier AWS KMS Key Identifier belonging to the sender.
     */
    Builder senderKmsIdentifier(String senderKmsIdentifier);

    /**
     * @return AWS KMS Key Identifier belonging to the sender.
     */
    String senderKmsIdentifier();

    /**
     * @param senderPublicKey Sender Public Key. This is the raw public ECC key in DER format that belongs to the senderKmsIdentifier.
     */
    Builder senderPublicKey(ByteBuffer senderPublicKey);

    /**
     * @return Sender Public Key. This is the raw public ECC key in DER format that belongs to the senderKmsIdentifier.
     */
    ByteBuffer senderPublicKey();

    /**
     * @param recipientPublicKey Recipient Public Key. This MUST be a raw public ECC key in DER format.
     */
    Builder recipientPublicKey(ByteBuffer recipientPublicKey);

    /**
     * @return Recipient Public Key. This MUST be a raw public ECC key in DER format.
     */
    ByteBuffer recipientPublicKey();

    KmsPrivateKeyToStaticPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String senderKmsIdentifier;

    protected ByteBuffer senderPublicKey;

    protected ByteBuffer recipientPublicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsPrivateKeyToStaticPublicKeyInput model) {
      this.senderKmsIdentifier = model.senderKmsIdentifier();
      this.senderPublicKey = model.senderPublicKey();
      this.recipientPublicKey = model.recipientPublicKey();
    }

    public Builder senderKmsIdentifier(String senderKmsIdentifier) {
      this.senderKmsIdentifier = senderKmsIdentifier;
      return this;
    }

    public String senderKmsIdentifier() {
      return this.senderKmsIdentifier;
    }

    public Builder senderPublicKey(ByteBuffer senderPublicKey) {
      this.senderPublicKey = senderPublicKey;
      return this;
    }

    public ByteBuffer senderPublicKey() {
      return this.senderPublicKey;
    }

    public Builder recipientPublicKey(ByteBuffer recipientPublicKey) {
      this.recipientPublicKey = recipientPublicKey;
      return this;
    }

    public ByteBuffer recipientPublicKey() {
      return this.recipientPublicKey;
    }

    public KmsPrivateKeyToStaticPublicKeyInput build() {
      if (Objects.isNull(this.senderKmsIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `senderKmsIdentifier`"
        );
      }
      if (Objects.isNull(this.recipientPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `recipientPublicKey`"
        );
      }
      return new KmsPrivateKeyToStaticPublicKeyInput(this);
    }
  }
}
