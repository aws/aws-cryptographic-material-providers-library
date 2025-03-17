// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Objects;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;

public class KeyStoreConfig {

  /**
   * Configures Key Store's KMS Key ARN restrictions.
   */
  private final KMSConfiguration kmsConfiguration;

  /**
   * The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.
   */
  private final String logicalKeyStoreName;

  /**
   * The key management configuration for this Key Store.
   */
  private final KeyManagement keyManagement;

  /**
   * The DynamoDB table name that backs this Key Store.
   */
  private final String ddbTableName;

  /**
   * An identifier for this Key Store.
   */
  private final String id;

  /**
   * The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  private final List<String> grantTokens;

  /**
   * The storage configuration for this Key Store.
   */
  private final Storage storage;

  /**
   * The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  private final DynamoDbClient ddbClient;

  /**
   * The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  private final KmsClient kmsClient;

  protected KeyStoreConfig(BuilderImpl builder) {
    this.kmsConfiguration = builder.kmsConfiguration();
    this.logicalKeyStoreName = builder.logicalKeyStoreName();
    this.keyManagement = builder.keyManagement();
    this.ddbTableName = builder.ddbTableName();
    this.id = builder.id();
    this.grantTokens = builder.grantTokens();
    this.storage = builder.storage();
    this.ddbClient = builder.ddbClient();
    this.kmsClient = builder.kmsClient();
  }

  /**
   * @return Configures Key Store's KMS Key ARN restrictions.
   */
  public KMSConfiguration kmsConfiguration() {
    return this.kmsConfiguration;
  }

  /**
   * @return The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.
   */
  public String logicalKeyStoreName() {
    return this.logicalKeyStoreName;
  }

  /**
   * @return The key management configuration for this Key Store.
   */
  public KeyManagement keyManagement() {
    return this.keyManagement;
  }

  /**
   * @return The DynamoDB table name that backs this Key Store.
   */
  public String ddbTableName() {
    return this.ddbTableName;
  }

  /**
   * @return An identifier for this Key Store.
   */
  public String id() {
    return this.id;
  }

  /**
   * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
  }

  /**
   * @return The storage configuration for this Key Store.
   */
  public Storage storage() {
    return this.storage;
  }

  /**
   * @return The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  public DynamoDbClient ddbClient() {
    return this.ddbClient;
  }

  /**
   * @return The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  public KmsClient kmsClient() {
    return this.kmsClient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsConfiguration Configures Key Store's KMS Key ARN restrictions.
     */
    Builder kmsConfiguration(KMSConfiguration kmsConfiguration);

    /**
     * @return Configures Key Store's KMS Key ARN restrictions.
     */
    KMSConfiguration kmsConfiguration();

    /**
     * @param logicalKeyStoreName The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.
     */
    Builder logicalKeyStoreName(String logicalKeyStoreName);

    /**
     * @return The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.
     */
    String logicalKeyStoreName();

    /**
     * @param keyManagement The key management configuration for this Key Store.
     */
    Builder keyManagement(KeyManagement keyManagement);

    /**
     * @return The key management configuration for this Key Store.
     */
    KeyManagement keyManagement();

    /**
     * @param ddbTableName The DynamoDB table name that backs this Key Store.
     */
    Builder ddbTableName(String ddbTableName);

    /**
     * @return The DynamoDB table name that backs this Key Store.
     */
    String ddbTableName();

    /**
     * @param id An identifier for this Key Store.
     */
    Builder id(String id);

    /**
     * @return An identifier for this Key Store.
     */
    String id();

    /**
     * @param grantTokens The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.
     */
    List<String> grantTokens();

    /**
     * @param storage The storage configuration for this Key Store.
     */
    Builder storage(Storage storage);

    /**
     * @return The storage configuration for this Key Store.
     */
    Storage storage();

    /**
     * @param ddbClient The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    Builder ddbClient(DynamoDbClient ddbClient);

    /**
     * @return The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    DynamoDbClient ddbClient();

    /**
     * @param kmsClient The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    Builder kmsClient(KmsClient kmsClient);

    /**
     * @return The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    KmsClient kmsClient();

    KeyStoreConfig build();
  }

  static class BuilderImpl implements Builder {

    protected KMSConfiguration kmsConfiguration;

    protected String logicalKeyStoreName;

    protected KeyManagement keyManagement;

    protected String ddbTableName;

    protected String id;

    protected List<String> grantTokens;

    protected Storage storage;

    protected DynamoDbClient ddbClient;

    protected KmsClient kmsClient;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyStoreConfig model) {
      this.kmsConfiguration = model.kmsConfiguration();
      this.logicalKeyStoreName = model.logicalKeyStoreName();
      this.keyManagement = model.keyManagement();
      this.ddbTableName = model.ddbTableName();
      this.id = model.id();
      this.grantTokens = model.grantTokens();
      this.storage = model.storage();
      this.ddbClient = model.ddbClient();
      this.kmsClient = model.kmsClient();
    }

    public Builder kmsConfiguration(KMSConfiguration kmsConfiguration) {
      this.kmsConfiguration = kmsConfiguration;
      return this;
    }

    public KMSConfiguration kmsConfiguration() {
      return this.kmsConfiguration;
    }

    public Builder logicalKeyStoreName(String logicalKeyStoreName) {
      this.logicalKeyStoreName = logicalKeyStoreName;
      return this;
    }

    public String logicalKeyStoreName() {
      return this.logicalKeyStoreName;
    }

    public Builder keyManagement(KeyManagement keyManagement) {
      this.keyManagement = keyManagement;
      return this;
    }

    public KeyManagement keyManagement() {
      return this.keyManagement;
    }

    public Builder ddbTableName(String ddbTableName) {
      this.ddbTableName = ddbTableName;
      return this;
    }

    public String ddbTableName() {
      return this.ddbTableName;
    }

    public Builder id(String id) {
      this.id = id;
      return this;
    }

    public String id() {
      return this.id;
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public Builder storage(Storage storage) {
      this.storage = storage;
      return this;
    }

    public Storage storage() {
      return this.storage;
    }

    public Builder ddbClient(DynamoDbClient ddbClient) {
      this.ddbClient = ddbClient;
      return this;
    }

    public DynamoDbClient ddbClient() {
      return this.ddbClient;
    }

    public Builder kmsClient(KmsClient kmsClient) {
      this.kmsClient = kmsClient;
      return this;
    }

    public KmsClient kmsClient() {
      return this.kmsClient;
    }

    public KeyStoreConfig build() {
      if (Objects.isNull(this.kmsConfiguration())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsConfiguration`"
        );
      }
      if (Objects.isNull(this.logicalKeyStoreName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `logicalKeyStoreName`"
        );
      }
      if (
        Objects.nonNull(this.ddbTableName()) && this.ddbTableName().length() < 3
      ) {
        throw new IllegalArgumentException(
          "The size of `ddbTableName` must be greater than or equal to 3"
        );
      }
      if (
        Objects.nonNull(this.ddbTableName()) &&
        this.ddbTableName().length() > 255
      ) {
        throw new IllegalArgumentException(
          "The size of `ddbTableName` must be less than or equal to 255"
        );
      }
      return new KeyStoreConfig(this);
    }
  }
}
