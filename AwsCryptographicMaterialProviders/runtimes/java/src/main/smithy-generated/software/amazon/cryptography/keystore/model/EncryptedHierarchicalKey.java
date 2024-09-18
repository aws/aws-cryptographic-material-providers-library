// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Map;
import java.util.Objects;

/**
 * Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.
 */
public class EncryptedHierarchicalKey {

  /**
   * The identifier for this encrypted key.
   */
  private final String Identifier;

  /**
   * The type of encrypted key.
   */
  private final HierarchicalKeyType Type;

  /**
   * The create time as an ISO 8061 UTC string.
   */
  private final String CreateTime;

  /**
   * The KMS ARN which protects this encrypted key.
   */
  private final String KmsArn;

  /**
   * The encryption context needed to decrypt this encrypted key. This includes the user the provided custom encryption context, as well as the other Branch Key attributes.
   */
  private final Map<String, String> EncryptionContext;

  /**
   * The ciphertext for this encrypted key.
   */
  private final ByteBuffer CiphertextBlob;

  protected EncryptedHierarchicalKey(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Type = builder.Type();
    this.CreateTime = builder.CreateTime();
    this.KmsArn = builder.KmsArn();
    this.EncryptionContext = builder.EncryptionContext();
    this.CiphertextBlob = builder.CiphertextBlob();
  }

  /**
   * @return The identifier for this encrypted key.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The type of encrypted key.
   */
  public HierarchicalKeyType Type() {
    return this.Type;
  }

  /**
   * @return The create time as an ISO 8061 UTC string.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  /**
   * @return The KMS ARN which protects this encrypted key.
   */
  public String KmsArn() {
    return this.KmsArn;
  }

  /**
   * @return The encryption context needed to decrypt this encrypted key. This includes the user the provided custom encryption context, as well as the other Branch Key attributes.
   */
  public Map<String, String> EncryptionContext() {
    return this.EncryptionContext;
  }

  /**
   * @return The ciphertext for this encrypted key.
   */
  public ByteBuffer CiphertextBlob() {
    return this.CiphertextBlob;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for this encrypted key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for this encrypted key.
     */
    String Identifier();

    /**
     * @param Type The type of encrypted key.
     */
    Builder Type(HierarchicalKeyType Type);

    /**
     * @return The type of encrypted key.
     */
    HierarchicalKeyType Type();

    /**
     * @param CreateTime The create time as an ISO 8061 UTC string.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return The create time as an ISO 8061 UTC string.
     */
    String CreateTime();

    /**
     * @param KmsArn The KMS ARN which protects this encrypted key.
     */
    Builder KmsArn(String KmsArn);

    /**
     * @return The KMS ARN which protects this encrypted key.
     */
    String KmsArn();

    /**
     * @param EncryptionContext The encryption context needed to decrypt this encrypted key. This includes the user the provided custom encryption context, as well as the other Branch Key attributes.
     */
    Builder EncryptionContext(Map<String, String> EncryptionContext);

    /**
     * @return The encryption context needed to decrypt this encrypted key. This includes the user the provided custom encryption context, as well as the other Branch Key attributes.
     */
    Map<String, String> EncryptionContext();

    /**
     * @param CiphertextBlob The ciphertext for this encrypted key.
     */
    Builder CiphertextBlob(ByteBuffer CiphertextBlob);

    /**
     * @return The ciphertext for this encrypted key.
     */
    ByteBuffer CiphertextBlob();

    EncryptedHierarchicalKey build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected HierarchicalKeyType Type;

    protected String CreateTime;

    protected String KmsArn;

    protected Map<String, String> EncryptionContext;

    protected ByteBuffer CiphertextBlob;

    protected BuilderImpl() {}

    protected BuilderImpl(EncryptedHierarchicalKey model) {
      this.Identifier = model.Identifier();
      this.Type = model.Type();
      this.CreateTime = model.CreateTime();
      this.KmsArn = model.KmsArn();
      this.EncryptionContext = model.EncryptionContext();
      this.CiphertextBlob = model.CiphertextBlob();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Type(HierarchicalKeyType Type) {
      this.Type = Type;
      return this;
    }

    public HierarchicalKeyType Type() {
      return this.Type;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public Builder KmsArn(String KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public String KmsArn() {
      return this.KmsArn;
    }

    public Builder EncryptionContext(Map<String, String> EncryptionContext) {
      this.EncryptionContext = EncryptionContext;
      return this;
    }

    public Map<String, String> EncryptionContext() {
      return this.EncryptionContext;
    }

    public Builder CiphertextBlob(ByteBuffer CiphertextBlob) {
      this.CiphertextBlob = CiphertextBlob;
      return this;
    }

    public ByteBuffer CiphertextBlob() {
      return this.CiphertextBlob;
    }

    public EncryptedHierarchicalKey build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Type())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Type`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      if (Objects.isNull(this.EncryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `EncryptionContext`"
        );
      }
      if (Objects.isNull(this.CiphertextBlob())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CiphertextBlob`"
        );
      }
      return new EncryptedHierarchicalKey(this);
    }
  }
}
