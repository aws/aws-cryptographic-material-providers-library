// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import software.amazon.cryptography.keystore.model.AwsKms;

public class AwsKmsDecryptEncrypt {

  /**
   * The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
   */
  private final AwsKms decrypt;

  /**
   * The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
   *      and to Generate new Cryptographic Material.
   */
  private final AwsKms encrypt;

  protected AwsKmsDecryptEncrypt(BuilderImpl builder) {
    this.decrypt = builder.decrypt();
    this.encrypt = builder.encrypt();
  }

  /**
   * @return The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
   */
  public AwsKms decrypt() {
    return this.decrypt;
  }

  /**
   * @return The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
   *      and to Generate new Cryptographic Material.
   */
  public AwsKms encrypt() {
    return this.encrypt;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param decrypt The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
     */
    Builder decrypt(AwsKms decrypt);

    /**
     * @return The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.
     */
    AwsKms decrypt();

    /**
     * @param encrypt The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
     *      and to Generate new Cryptographic Material.
     */
    Builder encrypt(AwsKms encrypt);

    /**
     * @return The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
     *      and to Generate new Cryptographic Material.
     */
    AwsKms encrypt();

    AwsKmsDecryptEncrypt build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms decrypt;

    protected AwsKms encrypt;

    protected BuilderImpl() {}

    protected BuilderImpl(AwsKmsDecryptEncrypt model) {
      this.decrypt = model.decrypt();
      this.encrypt = model.encrypt();
    }

    public Builder decrypt(AwsKms decrypt) {
      this.decrypt = decrypt;
      return this;
    }

    public AwsKms decrypt() {
      return this.decrypt;
    }

    public Builder encrypt(AwsKms encrypt) {
      this.encrypt = encrypt;
      return this;
    }

    public AwsKms encrypt() {
      return this.encrypt;
    }

    public AwsKmsDecryptEncrypt build() {
      return new AwsKmsDecryptEncrypt(this);
    }
  }
}
