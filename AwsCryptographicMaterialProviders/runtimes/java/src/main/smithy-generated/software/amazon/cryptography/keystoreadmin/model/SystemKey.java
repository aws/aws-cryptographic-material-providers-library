// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

/**
 * Key Store Admin protects any non-cryptographic
 * items stored with this Key.
 * As of v1.8.0, TrustStorage is the default behavior.
 */
public class SystemKey {

  /**
   * Include all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   */
  private final KmsAes kmsAes;

  /**
   * The Storage is trusted enough
   * for non-cryptographic items.
   */
  private final TrustStorage trustStorage;

  protected SystemKey(BuilderImpl builder) {
    this.kmsAes = builder.kmsAes();
    this.trustStorage = builder.trustStorage();
  }

  /**
   * @return Include all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   */
  public KmsAes kmsAes() {
    return this.kmsAes;
  }

  /**
   * @return The Storage is trusted enough
   * for non-cryptographic items.
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
     * @param kmsAes Include all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     */
    Builder kmsAes(KmsAes kmsAes);

    /**
     * @return Include all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     */
    KmsAes kmsAes();

    /**
     * @param trustStorage The Storage is trusted enough
     * for non-cryptographic items.
     */
    Builder trustStorage(TrustStorage trustStorage);

    /**
     * @return The Storage is trusted enough
     * for non-cryptographic items.
     */
    TrustStorage trustStorage();

    SystemKey build();
  }

  static class BuilderImpl implements Builder {

    protected KmsAes kmsAes;

    protected TrustStorage trustStorage;

    protected BuilderImpl() {}

    protected BuilderImpl(SystemKey model) {
      this.kmsAes = model.kmsAes();
      this.trustStorage = model.trustStorage();
    }

    public Builder kmsAes(KmsAes kmsAes) {
      this.kmsAes = kmsAes;
      return this;
    }

    public KmsAes kmsAes() {
      return this.kmsAes;
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
      Object[] allValues = { this.kmsAes, this.trustStorage };
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
