// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class KMSConfiguration {

  /**
   * Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid. As such, this is really a Single Region Key restriction.
   */
  private final String kmsKeyArn;

  /**
   * The Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic to supported with this configuration; only the region configured on the KMS Client will be used. Thus, if a Multi-Region Key is encountered, and the region in the encountered ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
   */
  private final Discovery discovery;

  protected KMSConfiguration(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.discovery = builder.discovery();
  }

  /**
   * @return Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid. As such, this is really a Single Region Key restriction.
   */
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return The Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic to supported with this configuration; only the region configured on the KMS Client will be used. Thus, if a Multi-Region Key is encountered, and the region in the encountered ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
   */
  public Discovery discovery() {
    return this.discovery;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid. As such, this is really a Single Region Key restriction.
     */
    Builder kmsKeyArn(String kmsKeyArn);

    /**
     * @return Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid. As such, this is really a Single Region Key restriction.
     */
    String kmsKeyArn();

    /**
     * @param discovery The Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic to supported with this configuration; only the region configured on the KMS Client will be used. Thus, if a Multi-Region Key is encountered, and the region in the encountered ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
     */
    Builder discovery(Discovery discovery);

    /**
     * @return The Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic to supported with this configuration; only the region configured on the KMS Client will be used. Thus, if a Multi-Region Key is encountered, and the region in the encountered ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.
     */
    Discovery discovery();

    KMSConfiguration build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected Discovery discovery;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSConfiguration model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.discovery = model.discovery();
    }

    public Builder kmsKeyArn(String kmsKeyArn) {
      this.kmsKeyArn = kmsKeyArn;
      return this;
    }

    public String kmsKeyArn() {
      return this.kmsKeyArn;
    }

    public Builder discovery(Discovery discovery) {
      this.discovery = discovery;
      return this;
    }

    public Discovery discovery() {
      return this.discovery;
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
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KMSConfiguration` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KMSConfiguration(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsKeyArn, this.discovery };
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
