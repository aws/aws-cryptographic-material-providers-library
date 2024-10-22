// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

/**
 * Key Store Admin protects any non-cryptographic
 * items stored with this Key.
 */
public class SystemKey {

  /**
   * Include all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   */
  private final KmsAes KmsAes;

  /**
   * The Storage is trusted enough
   * for non-cryptographic items.
   */
  private final TrustStorage TrustStorage;

  protected SystemKey(BuilderImpl builder) {
    this.KmsAes = builder.KmsAes();
    this.TrustStorage = builder.TrustStorage();
  }

  /**
   * @return Include all attributes of an item as Encryption Context
   * in a KMS Encrypt or Decrypt call,
   * effectively signing the attributes.
   */
  public KmsAes KmsAes() {
    return this.KmsAes;
  }

  /**
   * @return The Storage is trusted enough
   * for non-cryptographic items.
   */
  public TrustStorage TrustStorage() {
    return this.TrustStorage;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KmsAes Include all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     */
    Builder KmsAes(KmsAes KmsAes);

    /**
     * @return Include all attributes of an item as Encryption Context
     * in a KMS Encrypt or Decrypt call,
     * effectively signing the attributes.
     */
    KmsAes KmsAes();

    /**
     * @param TrustStorage The Storage is trusted enough
     * for non-cryptographic items.
     */
    Builder TrustStorage(TrustStorage TrustStorage);

    /**
     * @return The Storage is trusted enough
     * for non-cryptographic items.
     */
    TrustStorage TrustStorage();

    SystemKey build();
  }

  static class BuilderImpl implements Builder {

    protected KmsAes KmsAes;

    protected TrustStorage TrustStorage;

    protected BuilderImpl() {}

    protected BuilderImpl(SystemKey model) {
      this.KmsAes = model.KmsAes();
      this.TrustStorage = model.TrustStorage();
    }

    public Builder KmsAes(KmsAes KmsAes) {
      this.KmsAes = KmsAes;
      return this;
    }

    public KmsAes KmsAes() {
      return this.KmsAes;
    }

    public Builder TrustStorage(TrustStorage TrustStorage) {
      this.TrustStorage = TrustStorage;
      return this;
    }

    public TrustStorage TrustStorage() {
      return this.TrustStorage;
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
      Object[] allValues = { this.KmsAes, this.TrustStorage };
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
