// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import software.amazon.cryptography.keystore.model.AwsKms;

/**
 * For HV-2, plain-text data keys (PDKs) are created by kms:GenerateRandom.
 * The additional authenticated data (AAD) and the PDK are protected by kms:Encrypt.
 * To validate a Branch Key item, kms:Decrypt un-wraps the AAD-PDK tuple, and the client verifies the AAD.
 */
public class AwsKmsForHierarchyVersionTwo {

  /**
   * The KMS Client (and Grant Tokens) used to generate the plain-text data key.
   */
  private final AwsKms generateRandom;

  /**
   * The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items.
   */
  private final AwsKms encrypt;

  /**
   * The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
   */
  private final AwsKms decrypt;

  protected AwsKmsForHierarchyVersionTwo(BuilderImpl builder) {
    this.generateRandom = builder.generateRandom();
    this.encrypt = builder.encrypt();
    this.decrypt = builder.decrypt();
  }

  /**
   * @return The KMS Client (and Grant Tokens) used to generate the plain-text data key.
   */
  public AwsKms generateRandom() {
    return this.generateRandom;
  }

  /**
   * @return The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items.
   */
  public AwsKms encrypt() {
    return this.encrypt;
  }

  /**
   * @return The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
   */
  public AwsKms decrypt() {
    return this.decrypt;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param generateRandom The KMS Client (and Grant Tokens) used to generate the plain-text data key.
     */
    Builder generateRandom(AwsKms generateRandom);

    /**
     * @return The KMS Client (and Grant Tokens) used to generate the plain-text data key.
     */
    AwsKms generateRandom();

    /**
     * @param encrypt The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items.
     */
    Builder encrypt(AwsKms encrypt);

    /**
     * @return The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items.
     */
    AwsKms encrypt();

    /**
     * @param decrypt The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
     */
    Builder decrypt(AwsKms decrypt);

    /**
     * @return The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
     */
    AwsKms decrypt();

    AwsKmsForHierarchyVersionTwo build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms generateRandom;

    protected AwsKms encrypt;

    protected AwsKms decrypt;

    protected BuilderImpl() {}

    protected BuilderImpl(AwsKmsForHierarchyVersionTwo model) {
      this.generateRandom = model.generateRandom();
      this.encrypt = model.encrypt();
      this.decrypt = model.decrypt();
    }

    public Builder generateRandom(AwsKms generateRandom) {
      this.generateRandom = generateRandom;
      return this;
    }

    public AwsKms generateRandom() {
      return this.generateRandom;
    }

    public Builder encrypt(AwsKms encrypt) {
      this.encrypt = encrypt;
      return this;
    }

    public AwsKms encrypt() {
      return this.encrypt;
    }

    public Builder decrypt(AwsKms decrypt) {
      this.decrypt = decrypt;
      return this;
    }

    public AwsKms decrypt() {
      return this.decrypt;
    }

    public AwsKmsForHierarchyVersionTwo build() {
      return new AwsKmsForHierarchyVersionTwo(this);
    }
  }
}
