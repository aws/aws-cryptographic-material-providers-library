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
   * Branch Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   *   At this time, this strategy can only be used with hierarchy-version-1 (HV-1) branch keys for:
   *   - Creating new HV-1 branch keys
   *   - Versioning existing HV-1 branch keys
   */
  private final AwsKms AwsKmsReEncrypt;

  /**
   *
   * Key Store Items are authenticated and re-wrapped via a Decrypt and then Encrypt request.
   * This is two separate requests to Key Management, as compared to one.
   * This is primarily intended for Branch Key Mutations
   * that need to use separate credentials to change
   * the KMS Key that protects a Branch Key.
   *
   * Branch Key Items in the original state
   * will be Decrypted by the Decrypt KMS Client,
   * and then Encrypted to the terminal state
   * via the Encrypt KMS Client.
   *
   * Generation of a new Branch Key Version
   * is done via GenerateDataKeyWithoutPlaintext,
   * and then Decrypt and Encrypt requests against the Encrypt Client.
   */
  private final AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt;

  /**
   * This is the simple option, that uses one KMS Client (and Grant Token list) and supports both hierarchy-versions.
   *   For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by kms:ReEncrypt is used to create branch keys.
   *   For HV-2, kms:GenerateDataKey followed by kms:Encrypt is used to create branch keys.
   *   For HV-1, to validate a branch key item, kms:ReEncrypt is used.
   *   For HV-2, to validate a branch key item, kms:Decrypt un-wraps the branch key context and data key tuple,
   *   and the client verifies the read branch key context against the protected branch key context.
   */
  private final AwsKms AwsKmsSimple;

  protected KeyManagementStrategy(BuilderImpl builder) {
    this.AwsKmsReEncrypt = builder.AwsKmsReEncrypt();
    this.AwsKmsDecryptEncrypt = builder.AwsKmsDecryptEncrypt();
    this.AwsKmsSimple = builder.AwsKmsSimple();
  }

  /**
   * @return Branch Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
   *   executed with the provided Grant Tokens and KMS Client.
   *   This is one request to Key Management, as compared to two.
   *   But only one set of credentials can be used.
   *   At this time, this strategy can only be used with hierarchy-version-1 (HV-1) branch keys for:
   *   - Creating new HV-1 branch keys
   *   - Versioning existing HV-1 branch keys
   */
  public AwsKms AwsKmsReEncrypt() {
    return this.AwsKmsReEncrypt;
  }

  /**
   * @return
   * Key Store Items are authenticated and re-wrapped via a Decrypt and then Encrypt request.
   * This is two separate requests to Key Management, as compared to one.
   * This is primarily intended for Branch Key Mutations
   * that need to use separate credentials to change
   * the KMS Key that protects a Branch Key.
   *
   * Branch Key Items in the original state
   * will be Decrypted by the Decrypt KMS Client,
   * and then Encrypted to the terminal state
   * via the Encrypt KMS Client.
   *
   * Generation of a new Branch Key Version
   * is done via GenerateDataKeyWithoutPlaintext,
   * and then Decrypt and Encrypt requests against the Encrypt Client.
   */
  public AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt() {
    return this.AwsKmsDecryptEncrypt;
  }

  /**
   * @return This is the simple option, that uses one KMS Client (and Grant Token list) and supports both hierarchy-versions.
   *   For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by kms:ReEncrypt is used to create branch keys.
   *   For HV-2, kms:GenerateDataKey followed by kms:Encrypt is used to create branch keys.
   *   For HV-1, to validate a branch key item, kms:ReEncrypt is used.
   *   For HV-2, to validate a branch key item, kms:Decrypt un-wraps the branch key context and data key tuple,
   *   and the client verifies the read branch key context against the protected branch key context.
   */
  public AwsKms AwsKmsSimple() {
    return this.AwsKmsSimple;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param AwsKmsReEncrypt Branch Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     *   At this time, this strategy can only be used with hierarchy-version-1 (HV-1) branch keys for:
     *   - Creating new HV-1 branch keys
     *   - Versioning existing HV-1 branch keys
     */
    Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt);

    /**
     * @return Branch Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
     *   executed with the provided Grant Tokens and KMS Client.
     *   This is one request to Key Management, as compared to two.
     *   But only one set of credentials can be used.
     *   At this time, this strategy can only be used with hierarchy-version-1 (HV-1) branch keys for:
     *   - Creating new HV-1 branch keys
     *   - Versioning existing HV-1 branch keys
     */
    AwsKms AwsKmsReEncrypt();

    /**
     * @param AwsKmsDecryptEncrypt
     * Key Store Items are authenticated and re-wrapped via a Decrypt and then Encrypt request.
     * This is two separate requests to Key Management, as compared to one.
     * This is primarily intended for Branch Key Mutations
     * that need to use separate credentials to change
     * the KMS Key that protects a Branch Key.
     *
     * Branch Key Items in the original state
     * will be Decrypted by the Decrypt KMS Client,
     * and then Encrypted to the terminal state
     * via the Encrypt KMS Client.
     *
     * Generation of a new Branch Key Version
     * is done via GenerateDataKeyWithoutPlaintext,
     * and then Decrypt and Encrypt requests against the Encrypt Client.
     */
    Builder AwsKmsDecryptEncrypt(AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt);

    /**
     * @return
     * Key Store Items are authenticated and re-wrapped via a Decrypt and then Encrypt request.
     * This is two separate requests to Key Management, as compared to one.
     * This is primarily intended for Branch Key Mutations
     * that need to use separate credentials to change
     * the KMS Key that protects a Branch Key.
     *
     * Branch Key Items in the original state
     * will be Decrypted by the Decrypt KMS Client,
     * and then Encrypted to the terminal state
     * via the Encrypt KMS Client.
     *
     * Generation of a new Branch Key Version
     * is done via GenerateDataKeyWithoutPlaintext,
     * and then Decrypt and Encrypt requests against the Encrypt Client.
     */
    AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt();

    /**
     * @param AwsKmsSimple This is the simple option, that uses one KMS Client (and Grant Token list) and supports both hierarchy-versions.
     *   For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by kms:ReEncrypt is used to create branch keys.
     *   For HV-2, kms:GenerateDataKey followed by kms:Encrypt is used to create branch keys.
     *   For HV-1, to validate a branch key item, kms:ReEncrypt is used.
     *   For HV-2, to validate a branch key item, kms:Decrypt un-wraps the branch key context and data key tuple,
     *   and the client verifies the read branch key context against the protected branch key context.
     */
    Builder AwsKmsSimple(AwsKms AwsKmsSimple);

    /**
     * @return This is the simple option, that uses one KMS Client (and Grant Token list) and supports both hierarchy-versions.
     *   For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by kms:ReEncrypt is used to create branch keys.
     *   For HV-2, kms:GenerateDataKey followed by kms:Encrypt is used to create branch keys.
     *   For HV-1, to validate a branch key item, kms:ReEncrypt is used.
     *   For HV-2, to validate a branch key item, kms:Decrypt un-wraps the branch key context and data key tuple,
     *   and the client verifies the read branch key context against the protected branch key context.
     */
    AwsKms AwsKmsSimple();

    KeyManagementStrategy build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms AwsKmsReEncrypt;

    protected AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt;

    protected AwsKms AwsKmsSimple;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyManagementStrategy model) {
      this.AwsKmsReEncrypt = model.AwsKmsReEncrypt();
      this.AwsKmsDecryptEncrypt = model.AwsKmsDecryptEncrypt();
      this.AwsKmsSimple = model.AwsKmsSimple();
    }

    public Builder AwsKmsReEncrypt(AwsKms AwsKmsReEncrypt) {
      this.AwsKmsReEncrypt = AwsKmsReEncrypt;
      return this;
    }

    public AwsKms AwsKmsReEncrypt() {
      return this.AwsKmsReEncrypt;
    }

    public Builder AwsKmsDecryptEncrypt(
      AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt
    ) {
      this.AwsKmsDecryptEncrypt = AwsKmsDecryptEncrypt;
      return this;
    }

    public AwsKmsDecryptEncrypt AwsKmsDecryptEncrypt() {
      return this.AwsKmsDecryptEncrypt;
    }

    public Builder AwsKmsSimple(AwsKms AwsKmsSimple) {
      this.AwsKmsSimple = AwsKmsSimple;
      return this;
    }

    public AwsKms AwsKmsSimple() {
      return this.AwsKmsSimple;
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
      Object[] allValues = {
        this.AwsKmsReEncrypt,
        this.AwsKmsDecryptEncrypt,
        this.AwsKmsSimple,
      };
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
