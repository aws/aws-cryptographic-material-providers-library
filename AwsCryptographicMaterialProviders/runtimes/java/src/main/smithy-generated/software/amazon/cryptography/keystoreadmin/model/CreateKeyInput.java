// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;
import java.util.Objects;

public class CreateKeyInput {

  /**
   * The identifier for the created Branch Key.
   */
  private final String branchKeyIdentifier;

  /**
   * Custom encryption context for the Branch Key.
   *   Required if branchKeyIdentifier is set.
   */
  private final Map<String, String> encryptionContext;

  /**
   * Multi-Region or Single Region AWS KMS Key
   *   used to protect the Branch Key, but not aliases!
   */
  private final KMSIdentifier kmsArn;

  /**
   * This configures which Key Management Operations will be used
   *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
   */
  private final KeyManagementStrategy strategy;

  protected CreateKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.encryptionContext = builder.encryptionContext();
    this.kmsArn = builder.kmsArn();
    this.strategy = builder.strategy();
  }

  /**
   * @return The identifier for the created Branch Key.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Custom encryption context for the Branch Key.
   *   Required if branchKeyIdentifier is set.
   */
  public Map<String, String> encryptionContext() {
    return this.encryptionContext;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key
   *   used to protect the Branch Key, but not aliases!
   */
  public KMSIdentifier kmsArn() {
    return this.kmsArn;
  }

  /**
   * @return This configures which Key Management Operations will be used
   *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
   */
  public KeyManagementStrategy strategy() {
    return this.strategy;
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
     * @param encryptionContext Custom encryption context for the Branch Key.
     *   Required if branchKeyIdentifier is set.
     */
    Builder encryptionContext(Map<String, String> encryptionContext);

    /**
     * @return Custom encryption context for the Branch Key.
     *   Required if branchKeyIdentifier is set.
     */
    Map<String, String> encryptionContext();

    /**
     * @param kmsArn Multi-Region or Single Region AWS KMS Key
     *   used to protect the Branch Key, but not aliases!
     */
    Builder kmsArn(KMSIdentifier kmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key
     *   used to protect the Branch Key, but not aliases!
     */
    KMSIdentifier kmsArn();

    /**
     * @param strategy This configures which Key Management Operations will be used
     *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
     */
    Builder strategy(KeyManagementStrategy strategy);

    /**
     * @return This configures which Key Management Operations will be used
     *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
     */
    KeyManagementStrategy strategy();

    CreateKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected Map<String, String> encryptionContext;

    protected KMSIdentifier kmsArn;

    protected KeyManagementStrategy strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.encryptionContext = model.encryptionContext();
      this.kmsArn = model.kmsArn();
      this.strategy = model.strategy();
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

    public Builder kmsArn(KMSIdentifier kmsArn) {
      this.kmsArn = kmsArn;
      return this;
    }

    public KMSIdentifier kmsArn() {
      return this.kmsArn;
    }

    public Builder strategy(KeyManagementStrategy strategy) {
      this.strategy = strategy;
      return this;
    }

    public KeyManagementStrategy strategy() {
      return this.strategy;
    }

    public CreateKeyInput build() {
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      return new CreateKeyInput(this);
    }
  }
}
