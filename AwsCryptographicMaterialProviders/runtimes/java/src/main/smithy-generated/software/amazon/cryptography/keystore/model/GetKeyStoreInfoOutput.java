// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;

/**
 * The configuration information for a Key Store.
 */
public class GetKeyStoreInfoOutput {

  /**
   * An identifier for this Key Store.
   */
  private final String keyStoreId;

  /**
   * The DynamoDB table name that backs this Key Store.
   */
  private final String keyStoreName;

  /**
   * The logical name for this Key Store, which is cryptographically bound to the keys it holds.
   */
  private final String logicalKeyStoreName;

  /**
   * The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  private final List<String> grantTokens;

  /**
   * Configures Key Store's KMS Key ARN restrictions.
   */
  private final KMSConfiguration kmsConfiguration;

  protected GetKeyStoreInfoOutput(BuilderImpl builder) {
    this.keyStoreId = builder.keyStoreId();
    this.keyStoreName = builder.keyStoreName();
    this.logicalKeyStoreName = builder.logicalKeyStoreName();
    this.grantTokens = builder.grantTokens();
    this.kmsConfiguration = builder.kmsConfiguration();
  }

  /**
   * @return An identifier for this Key Store.
   */
  public String keyStoreId() {
    return this.keyStoreId;
  }

  /**
   * @return The DynamoDB table name that backs this Key Store.
   */
  public String keyStoreName() {
    return this.keyStoreName;
  }

  /**
   * @return The logical name for this Key Store, which is cryptographically bound to the keys it holds.
   */
  public String logicalKeyStoreName() {
    return this.logicalKeyStoreName;
  }

  /**
   * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
  }

  /**
   * @return Configures Key Store's KMS Key ARN restrictions.
   */
  public KMSConfiguration kmsConfiguration() {
    return this.kmsConfiguration;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param keyStoreId An identifier for this Key Store.
     */
    Builder keyStoreId(String keyStoreId);

    /**
     * @return An identifier for this Key Store.
     */
    String keyStoreId();

    /**
     * @param keyStoreName The DynamoDB table name that backs this Key Store.
     */
    Builder keyStoreName(String keyStoreName);

    /**
     * @return The DynamoDB table name that backs this Key Store.
     */
    String keyStoreName();

    /**
     * @param logicalKeyStoreName The logical name for this Key Store, which is cryptographically bound to the keys it holds.
     */
    Builder logicalKeyStoreName(String logicalKeyStoreName);

    /**
     * @return The logical name for this Key Store, which is cryptographically bound to the keys it holds.
     */
    String logicalKeyStoreName();

    /**
     * @param grantTokens The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    List<String> grantTokens();

    /**
     * @param kmsConfiguration Configures Key Store's KMS Key ARN restrictions.
     */
    Builder kmsConfiguration(KMSConfiguration kmsConfiguration);

    /**
     * @return Configures Key Store's KMS Key ARN restrictions.
     */
    KMSConfiguration kmsConfiguration();

    GetKeyStoreInfoOutput build();
  }

  static class BuilderImpl implements Builder {

    protected String keyStoreId;

    protected String keyStoreName;

    protected String logicalKeyStoreName;

    protected List<String> grantTokens;

    protected KMSConfiguration kmsConfiguration;

    protected BuilderImpl() {}

    protected BuilderImpl(GetKeyStoreInfoOutput model) {
      this.keyStoreId = model.keyStoreId();
      this.keyStoreName = model.keyStoreName();
      this.logicalKeyStoreName = model.logicalKeyStoreName();
      this.grantTokens = model.grantTokens();
      this.kmsConfiguration = model.kmsConfiguration();
    }

    public Builder keyStoreId(String keyStoreId) {
      this.keyStoreId = keyStoreId;
      return this;
    }

    public String keyStoreId() {
      return this.keyStoreId;
    }

    public Builder keyStoreName(String keyStoreName) {
      this.keyStoreName = keyStoreName;
      return this;
    }

    public String keyStoreName() {
      return this.keyStoreName;
    }

    public Builder logicalKeyStoreName(String logicalKeyStoreName) {
      this.logicalKeyStoreName = logicalKeyStoreName;
      return this;
    }

    public String logicalKeyStoreName() {
      return this.logicalKeyStoreName;
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public Builder kmsConfiguration(KMSConfiguration kmsConfiguration) {
      this.kmsConfiguration = kmsConfiguration;
      return this;
    }

    public KMSConfiguration kmsConfiguration() {
      return this.kmsConfiguration;
    }

    public GetKeyStoreInfoOutput build() {
      if (Objects.isNull(this.keyStoreId())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyStoreId`"
        );
      }
      if (Objects.isNull(this.keyStoreName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyStoreName`"
        );
      }
      if (
        Objects.nonNull(this.keyStoreName()) && this.keyStoreName().length() < 3
      ) {
        throw new IllegalArgumentException(
          "The size of `keyStoreName` must be greater than or equal to 3"
        );
      }
      if (
        Objects.nonNull(this.keyStoreName()) &&
        this.keyStoreName().length() > 255
      ) {
        throw new IllegalArgumentException(
          "The size of `keyStoreName` must be less than or equal to 255"
        );
      }
      if (Objects.isNull(this.logicalKeyStoreName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `logicalKeyStoreName`"
        );
      }
      if (Objects.isNull(this.grantTokens())) {
        throw new IllegalArgumentException(
          "Missing value for required field `grantTokens`"
        );
      }
      if (Objects.isNull(this.kmsConfiguration())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsConfiguration`"
        );
      }
      return new GetKeyStoreInfoOutput(this);
    }
  }
}
