// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

public class DynamoDBTable {

  /**
   * The DynamoDB table name that backs this Key Store.
   */
  private final String ddbTableName;

  /**
   * The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  private final DynamoDbClient ddbClient;

  protected DynamoDBTable(BuilderImpl builder) {
    this.ddbTableName = builder.ddbTableName();
    this.ddbClient = builder.ddbClient();
  }

  /**
   * @return The DynamoDB table name that backs this Key Store.
   */
  public String ddbTableName() {
    return this.ddbTableName;
  }

  /**
   * @return The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
   */
  public DynamoDbClient ddbClient() {
    return this.ddbClient;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ddbTableName The DynamoDB table name that backs this Key Store.
     */
    Builder ddbTableName(String ddbTableName);

    /**
     * @return The DynamoDB table name that backs this Key Store.
     */
    String ddbTableName();

    /**
     * @param ddbClient The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    Builder ddbClient(DynamoDbClient ddbClient);

    /**
     * @return The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.
     */
    DynamoDbClient ddbClient();

    DynamoDBTable build();
  }

  static class BuilderImpl implements Builder {

    protected String ddbTableName;

    protected DynamoDbClient ddbClient;

    protected BuilderImpl() {}

    protected BuilderImpl(DynamoDBTable model) {
      this.ddbTableName = model.ddbTableName();
      this.ddbClient = model.ddbClient();
    }

    public Builder ddbTableName(String ddbTableName) {
      this.ddbTableName = ddbTableName;
      return this;
    }

    public String ddbTableName() {
      return this.ddbTableName;
    }

    public Builder ddbClient(DynamoDbClient ddbClient) {
      this.ddbClient = ddbClient;
      return this;
    }

    public DynamoDbClient ddbClient() {
      return this.ddbClient;
    }

    public DynamoDBTable build() {
      if (Objects.isNull(this.ddbTableName())) {
        throw new IllegalArgumentException(
          "Missing value for required field `ddbTableName`"
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
      return new DynamoDBTable(this);
    }
  }
}
