// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Configures this Keystore's KMS Key ARN restrictions.
 */
public class KMSConfiguration {

  /**
   * Keystore is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MRK) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
   */
  private final String kmsKeyArn;

  /**
   * Keystore is restricted to only this replication of the KMS Multi-Region Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. For Get* Operations, the Keystore compares the configured MRK ARN with the ARN recorded on the Branch Key. If all elements of the ARN are equal except for the Region, the Branch Key is allowed and KMS is called. Otherwise, the Branch Key is denied.
   */
  private final String kmsMRKeyArn;

  protected KMSConfiguration(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.kmsMRKeyArn = builder.kmsMRKeyArn();
  }

  /**
   * @return Keystore is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MRK) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
   */
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return Keystore is restricted to only this replication of the KMS Multi-Region Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. For Get* Operations, the Keystore compares the configured MRK ARN with the ARN recorded on the Branch Key. If all elements of the ARN are equal except for the Region, the Branch Key is allowed and KMS is called. Otherwise, the Branch Key is denied.
   */
  public String kmsMRKeyArn() {
    return this.kmsMRKeyArn;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn Keystore is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MRK) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
     */
    Builder kmsKeyArn(String kmsKeyArn);

    /**
     * @return Keystore is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MRK) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
     */
    String kmsKeyArn();

    /**
     * @param kmsMRKeyArn Keystore is restricted to only this replication of the KMS Multi-Region Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. For Get* Operations, the Keystore compares the configured MRK ARN with the ARN recorded on the Branch Key. If all elements of the ARN are equal except for the Region, the Branch Key is allowed and KMS is called. Otherwise, the Branch Key is denied.
     */
    Builder kmsMRKeyArn(String kmsMRKeyArn);

    /**
     * @return Keystore is restricted to only this replication of the KMS Multi-Region Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. For Get* Operations, the Keystore compares the configured MRK ARN with the ARN recorded on the Branch Key. If all elements of the ARN are equal except for the Region, the Branch Key is allowed and KMS is called. Otherwise, the Branch Key is denied.
     */
    String kmsMRKeyArn();

    KMSConfiguration build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected String kmsMRKeyArn;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSConfiguration model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.kmsMRKeyArn = model.kmsMRKeyArn();
    }

    public Builder kmsKeyArn(String kmsKeyArn) {
      this.kmsKeyArn = kmsKeyArn;
      return this;
    }

    public String kmsKeyArn() {
      return this.kmsKeyArn;
    }

    public Builder kmsMRKeyArn(String kmsMRKeyArn) {
      this.kmsMRKeyArn = kmsMRKeyArn;
      return this;
    }

    public String kmsMRKeyArn() {
      return this.kmsMRKeyArn;
    }

    public KMSConfiguration build() {
      if (Objects.nonNull(this.kmsKeyArn()) && this.kmsKeyArn().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `kmsKeyArn` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.kmsKeyArn()) && this.kmsKeyArn().length() > 2048
      ) {
        throw new IllegalArgumentException(
          "The size of `kmsKeyArn` must be less than or equal to 2048"
        );
      }
      if (
        Objects.nonNull(this.kmsMRKeyArn()) && this.kmsMRKeyArn().length() < 1
      ) {
        throw new IllegalArgumentException(
          "The size of `kmsMRKeyArn` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.kmsMRKeyArn()) &&
        this.kmsMRKeyArn().length() > 2048
      ) {
        throw new IllegalArgumentException(
          "The size of `kmsMRKeyArn` must be less than or equal to 2048"
        );
      }
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KMSConfiguration` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KMSConfiguration(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsKeyArn, this.kmsMRKeyArn };
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
