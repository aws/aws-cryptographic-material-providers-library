// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

/**
 * Key Store Admin protects any non-cryptographic
 * items stored with this Key.
 * Using 'KMS Symmetric Encryption' is a best practice,
 * as it prevents actors with only write access to the Key Store's storage
 * from tampering with Mutations.
 * For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.
 */
public class SystemKey {

  /**
   * Items of a non-cryptographic material nature are protected by KMS.
   * This is done by including all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   * As a best practice,
   * this KMS Key should be distinct from those used to protect Branch Keys.
   */
  private final KmsSymmetricEncryption kmsSymmetricEncryption;

  /**
   * The Storage is trusted enough for items of non-cryptographic material nature,
   * even if those items can affect the cryptographic materials.
   * Thus, permissions to modify the Key Store's storage is sufficient
   * to influence the properties of mutations in flight
   * without needing a KMS key permission,
   * which would otherwise be needed to do the same.
   * As an extreme example,
   * an actor with only write access to the storage
   * could modify an in-flight Mutation's terminal KMS Key ARN.
   * Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
   * instead of 'Trust Storage' to ensure that Branch Keys are
   * only modified via actors with KMS key permissions.
   */
  private final TrustStorage trustStorage;

  protected SystemKey(BuilderImpl builder) {
    this.kmsSymmetricEncryption = builder.kmsSymmetricEncryption();
    this.trustStorage = builder.trustStorage();
  }

  /**
   * @return Items of a non-cryptographic material nature are protected by KMS.
   * This is done by including all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   * As a best practice,
   * this KMS Key should be distinct from those used to protect Branch Keys.
   */
  public KmsSymmetricEncryption kmsSymmetricEncryption() {
    return this.kmsSymmetricEncryption;
  }

  /**
   * @return The Storage is trusted enough for items of non-cryptographic material nature,
   * even if those items can affect the cryptographic materials.
   * Thus, permissions to modify the Key Store's storage is sufficient
   * to influence the properties of mutations in flight
   * without needing a KMS key permission,
   * which would otherwise be needed to do the same.
   * As an extreme example,
   * an actor with only write access to the storage
   * could modify an in-flight Mutation's terminal KMS Key ARN.
   * Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
   * instead of 'Trust Storage' to ensure that Branch Keys are
   * only modified via actors with KMS key permissions.
   */
  public TrustStorage trustStorage() {
    return this.trustStorage;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsSymmetricEncryption Items of a non-cryptographic material nature are protected by KMS.
     * This is done by including all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     * As a best practice,
     * this KMS Key should be distinct from those used to protect Branch Keys.
     */
    Builder kmsSymmetricEncryption(
      KmsSymmetricEncryption kmsSymmetricEncryption
    );

    /**
     * @return Items of a non-cryptographic material nature are protected by KMS.
     * This is done by including all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     * As a best practice,
     * this KMS Key should be distinct from those used to protect Branch Keys.
     */
    KmsSymmetricEncryption kmsSymmetricEncryption();

    /**
     * @param trustStorage The Storage is trusted enough for items of non-cryptographic material nature,
     * even if those items can affect the cryptographic materials.
     * Thus, permissions to modify the Key Store's storage is sufficient
     * to influence the properties of mutations in flight
     * without needing a KMS key permission,
     * which would otherwise be needed to do the same.
     * As an extreme example,
     * an actor with only write access to the storage
     * could modify an in-flight Mutation's terminal KMS Key ARN.
     * Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
     * instead of 'Trust Storage' to ensure that Branch Keys are
     * only modified via actors with KMS key permissions.
     */
    Builder trustStorage(TrustStorage trustStorage);

    /**
     * @return The Storage is trusted enough for items of non-cryptographic material nature,
     * even if those items can affect the cryptographic materials.
     * Thus, permissions to modify the Key Store's storage is sufficient
     * to influence the properties of mutations in flight
     * without needing a KMS key permission,
     * which would otherwise be needed to do the same.
     * As an extreme example,
     * an actor with only write access to the storage
     * could modify an in-flight Mutation's terminal KMS Key ARN.
     * Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
     * instead of 'Trust Storage' to ensure that Branch Keys are
     * only modified via actors with KMS key permissions.
     */
    TrustStorage trustStorage();

    SystemKey build();
  }

  static class BuilderImpl implements Builder {

    protected KmsSymmetricEncryption kmsSymmetricEncryption;

    protected TrustStorage trustStorage;

    protected BuilderImpl() {}

    protected BuilderImpl(SystemKey model) {
      this.kmsSymmetricEncryption = model.kmsSymmetricEncryption();
      this.trustStorage = model.trustStorage();
    }

    public Builder kmsSymmetricEncryption(
      KmsSymmetricEncryption kmsSymmetricEncryption
    ) {
      this.kmsSymmetricEncryption = kmsSymmetricEncryption;
      return this;
    }

    public KmsSymmetricEncryption kmsSymmetricEncryption() {
      return this.kmsSymmetricEncryption;
    }

    public Builder trustStorage(TrustStorage trustStorage) {
      this.trustStorage = trustStorage;
      return this;
    }

    public TrustStorage trustStorage() {
      return this.trustStorage;
    }

    public SystemKey build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`SystemKey` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new SystemKey(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsSymmetricEncryption, this.trustStorage };
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
