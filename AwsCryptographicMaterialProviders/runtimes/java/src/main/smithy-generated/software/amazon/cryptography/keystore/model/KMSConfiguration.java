// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

/**
 * Configures Key Store's KMS Key ARN restrictions.
 */
public class KMSConfiguration {

  /**
   * Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
   */
  private final String kmsKeyArn;

  /**
   * If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those two ARNs may differ in region, although they must be otherwise equal. If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.
   */
  private final String kmsMRKeyArn;

  /**
   * The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic with this configuration; if a Multi-Region Key is encountered, and the region in the ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
   */
  private final Discovery discovery;

  /**
   * The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. If a Multi-Region Key is encountered, the region in the ARN is changed to the configured region.
   */
  private final MRDiscovery mrDiscovery;

  protected KMSConfiguration(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.kmsMRKeyArn = builder.kmsMRKeyArn();
    this.discovery = builder.discovery();
    this.mrDiscovery = builder.mrDiscovery();
  }

  /**
   * @return Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
   */
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those two ARNs may differ in region, although they must be otherwise equal. If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.
   */
  public String kmsMRKeyArn() {
    return this.kmsMRKeyArn;
  }

  /**
   * @return The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic with this configuration; if a Multi-Region Key is encountered, and the region in the ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
   */
  public Discovery discovery() {
    return this.discovery;
  }

  /**
   * @return The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. If a Multi-Region Key is encountered, the region in the ARN is changed to the configured region.
   */
  public MRDiscovery mrDiscovery() {
    return this.mrDiscovery;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
     */
    Builder kmsKeyArn(String kmsKeyArn);

    /**
     * @return Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.
     */
    String kmsKeyArn();

    /**
     * @param kmsMRKeyArn If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those two ARNs may differ in region, although they must be otherwise equal. If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.
     */
    Builder kmsMRKeyArn(String kmsMRKeyArn);

    /**
     * @return If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those two ARNs may differ in region, although they must be otherwise equal. If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.
     */
    String kmsMRKeyArn();

    /**
     * @param discovery The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic with this configuration; if a Multi-Region Key is encountered, and the region in the ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
     */
    Builder discovery(Discovery discovery);

    /**
     * @return The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic with this configuration; if a Multi-Region Key is encountered, and the region in the ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
     */
    Discovery discovery();

    /**
     * @param mrDiscovery The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. If a Multi-Region Key is encountered, the region in the ARN is changed to the configured region.
     */
    Builder mrDiscovery(MRDiscovery mrDiscovery);

    /**
     * @return The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. If a Multi-Region Key is encountered, the region in the ARN is changed to the configured region.
     */
    MRDiscovery mrDiscovery();

    KMSConfiguration build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected String kmsMRKeyArn;

    protected Discovery discovery;

    protected MRDiscovery mrDiscovery;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSConfiguration model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.kmsMRKeyArn = model.kmsMRKeyArn();
      this.discovery = model.discovery();
      this.mrDiscovery = model.mrDiscovery();
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

    public Builder discovery(Discovery discovery) {
      this.discovery = discovery;
      return this;
    }

    public Discovery discovery() {
      return this.discovery;
    }

    public Builder mrDiscovery(MRDiscovery mrDiscovery) {
      this.mrDiscovery = mrDiscovery;
      return this;
    }

    public MRDiscovery mrDiscovery() {
      return this.mrDiscovery;
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
      Object[] allValues = {
        this.kmsKeyArn,
        this.kmsMRKeyArn,
        this.discovery,
        this.mrDiscovery,
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
