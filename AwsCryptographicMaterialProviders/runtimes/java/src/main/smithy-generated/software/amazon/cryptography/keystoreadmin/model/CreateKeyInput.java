// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;
import java.util.Objects;
import software.amazon.awssdk.services.kms.KmsClient;

public class CreateKeyInput {

  /**
   * The identifier for the created Branch Key.
   */
  private final String branchKeyIdentifier;

  /**
   * Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
   */
  private final Map<String, String> encryptionContext;

  /**
   * Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  private final String kmsArn;

  /**
   * The KMS client this Key Store uses to call AWS KMS.
   */
  private final KmsClient kmsClient;

  protected CreateKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.encryptionContext = builder.encryptionContext();
    this.kmsArn = builder.kmsArn();
    this.kmsClient = builder.kmsClient();
  }

  /**
   * @return The identifier for the created Branch Key.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
   */
  public Map<String, String> encryptionContext() {
    return this.encryptionContext;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  public String kmsArn() {
    return this.kmsArn;
  }

  /**
   * @return The KMS client this Key Store uses to call AWS KMS.
   */
  public KmsClient kmsClient() {
    return this.kmsClient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the created Branch Key.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the created Branch Key.
     */
    String branchKeyIdentifier();

    /**
     * @param encryptionContext Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
     */
    Builder encryptionContext(Map<String, String> encryptionContext);

    /**
     * @return Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
     */
    Map<String, String> encryptionContext();

    /**
     * @param kmsArn Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    Builder kmsArn(String kmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    String kmsArn();

    /**
     * @param kmsClient The KMS client this Key Store uses to call AWS KMS.
     */
    Builder kmsClient(KmsClient kmsClient);

    /**
     * @return The KMS client this Key Store uses to call AWS KMS.
     */
    KmsClient kmsClient();

    CreateKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected Map<String, String> encryptionContext;

    protected String kmsArn;

    protected KmsClient kmsClient;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.encryptionContext = model.encryptionContext();
      this.kmsArn = model.kmsArn();
      this.kmsClient = model.kmsClient();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder encryptionContext(Map<String, String> encryptionContext) {
      this.encryptionContext = encryptionContext;
      return this;
    }

    public Map<String, String> encryptionContext() {
      return this.encryptionContext;
    }

    public Builder kmsArn(String kmsArn) {
      this.kmsArn = kmsArn;
      return this;
    }

    public String kmsArn() {
      return this.kmsArn;
    }

    public Builder kmsClient(KmsClient kmsClient) {
      this.kmsClient = kmsClient;
      return this;
    }

    public KmsClient kmsClient() {
      return this.kmsClient;
    }

    public CreateKeyInput build() {
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      if (Objects.isNull(this.kmsClient())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsClient`"
        );
      }
      return new CreateKeyInput(this);
    }
  }
}
