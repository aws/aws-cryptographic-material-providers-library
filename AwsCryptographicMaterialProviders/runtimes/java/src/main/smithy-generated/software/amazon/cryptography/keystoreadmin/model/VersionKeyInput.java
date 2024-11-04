// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class VersionKeyInput {

  /**
   * The identifier for the Branch Key to be versioned.
   */
  private final String Identifier;

  /**
   * Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  private final KmsAesIdentifier KmsArn;

  /**
   * This configures which Key Management Operations will be used
   *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
   */
  private final KeyManagementStrategy Strategy;

  protected VersionKeyInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.KmsArn = builder.KmsArn();
    this.Strategy = builder.Strategy();
  }

  /**
   * @return The identifier for the Branch Key to be versioned.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
   */
  public KmsAesIdentifier KmsArn() {
    return this.KmsArn;
  }

  /**
   * @return This configures which Key Management Operations will be used
   *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
   */
  public KeyManagementStrategy Strategy() {
    return this.Strategy;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key to be versioned.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to be versioned.
     */
    String Identifier();

    /**
     * @param KmsArn Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    Builder KmsArn(KmsAesIdentifier KmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!
     */
    KmsAesIdentifier KmsArn();

    /**
     * @param Strategy This configures which Key Management Operations will be used
     *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
     */
    Builder Strategy(KeyManagementStrategy Strategy);

    /**
     * @return This configures which Key Management Operations will be used
     *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
     */
    KeyManagementStrategy Strategy();

    VersionKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected KmsAesIdentifier KmsArn;

    protected KeyManagementStrategy Strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(VersionKeyInput model) {
      this.Identifier = model.Identifier();
      this.KmsArn = model.KmsArn();
      this.Strategy = model.Strategy();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder KmsArn(KmsAesIdentifier KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public KmsAesIdentifier KmsArn() {
      return this.KmsArn;
    }

    public Builder Strategy(KeyManagementStrategy Strategy) {
      this.Strategy = Strategy;
      return this;
    }

    public KeyManagementStrategy Strategy() {
      return this.Strategy;
    }

    public VersionKeyInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      return new VersionKeyInput(this);
    }
  }
}
