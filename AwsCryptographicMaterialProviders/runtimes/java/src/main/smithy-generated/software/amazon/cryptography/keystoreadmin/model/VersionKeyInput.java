// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class VersionKeyInput {

  /**
   * The identifier for the Branch Key to be versioned.
   */
  private final String branchKeyIdentifier;

  /**
   * Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  private final KMSIdentifier kmsArn;

  /**
   * This configures which Key Management Operations will be used
   *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
   */
  private final KeyManagementStrategy strategy;

  protected VersionKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.kmsArn = builder.kmsArn();
    this.strategy = builder.strategy();
  }

  /**
   * @return The identifier for the Branch Key to be versioned.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
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
     * @param branchKeyIdentifier The identifier for the Branch Key to be versioned.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the Branch Key to be versioned.
     */
    String branchKeyIdentifier();

    /**
     * @param kmsArn Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    Builder kmsArn(KMSIdentifier kmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
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

    VersionKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected KMSIdentifier kmsArn;

    protected KeyManagementStrategy strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(VersionKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
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

    public VersionKeyInput build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      return new VersionKeyInput(this);
    }
  }
}
