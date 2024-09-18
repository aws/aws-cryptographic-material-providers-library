// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.AwsKms;

/**
 * This configures which Key Management Operations will be used
 *    AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.
 */
public class KeyManagementStrategy {

  /**
   * Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   */
  private final AwsKms AwsKmsReEncrypt;

  protected KeyManagementStrategy(BuilderImpl builder) {
    this.AwsKmsReEncrypt = builder.AwsKmsReEncrypt();
  }

  /**
   * @return Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   */
  public AwsKms AwsKmsReEncrypt() {
    return this.AwsKmsReEncrypt;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param AwsKmsReEncrypt Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     */
    Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt);

    /**
     * @return Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     */
    AwsKms AwsKmsReEncrypt();

    KeyManagementStrategy build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms AwsKmsReEncrypt;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyManagementStrategy model) {
      this.AwsKmsReEncrypt = model.AwsKmsReEncrypt();
    }

    public Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt) {
      this.AwsKmsReEncrypt = AwsKmsReEncrypt;
      return this;
    }

    public AwsKms AwsKmsReEncrypt() {
      return this.AwsKmsReEncrypt;
    }

    public KeyManagementStrategy build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KeyManagementStrategy` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KeyManagementStrategy(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.AwsKmsReEncrypt };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
