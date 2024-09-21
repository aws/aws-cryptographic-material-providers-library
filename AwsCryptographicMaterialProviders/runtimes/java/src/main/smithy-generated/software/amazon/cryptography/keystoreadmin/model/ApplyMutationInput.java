// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class ApplyMutationInput {

  private final MutationToken mutationToken;

  /**
   * For Default DynamoDB Table Storage, the maximum page size is 99.
   *   At most, Apply Mutation will mutate pageSize Items.
   *   Note that, at least for Storage:DynamoDBTable,
   *   an additional "item" is consumed by the Mutation Lock verification.
   *   Thus, if the pageSize is 24, 25 requests will be sent in the Transact Write Request.
   */
  private final Integer pageSize;

  /**
   * Optional. Defaults to reEncrypt with a default KMS Client.
   */
  private final KeyManagementStrategy strategy;

  protected ApplyMutationInput(BuilderImpl builder) {
    this.mutationToken = builder.mutationToken();
    this.pageSize = builder.pageSize();
    this.strategy = builder.strategy();
  }

  public MutationToken mutationToken() {
    return this.mutationToken;
  }

  /**
   * @return For Default DynamoDB Table Storage, the maximum page size is 99.
   *   At most, Apply Mutation will mutate pageSize Items.
   *   Note that, at least for Storage:DynamoDBTable,
   *   an additional "item" is consumed by the Mutation Lock verification.
   *   Thus, if the pageSize is 24, 25 requests will be sent in the Transact Write Request.
   */
  public Integer pageSize() {
    return this.pageSize;
  }

  /**
   * @return Optional. Defaults to reEncrypt with a default KMS Client.
   */
  public KeyManagementStrategy strategy() {
    return this.strategy;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder mutationToken(MutationToken mutationToken);

    MutationToken mutationToken();

    /**
     * @param pageSize For Default DynamoDB Table Storage, the maximum page size is 99.
     *   At most, Apply Mutation will mutate pageSize Items.
     *   Note that, at least for Storage:DynamoDBTable,
     *   an additional "item" is consumed by the Mutation Lock verification.
     *   Thus, if the pageSize is 24, 25 requests will be sent in the Transact Write Request.
     */
    Builder pageSize(Integer pageSize);

    /**
     * @return For Default DynamoDB Table Storage, the maximum page size is 99.
     *   At most, Apply Mutation will mutate pageSize Items.
     *   Note that, at least for Storage:DynamoDBTable,
     *   an additional "item" is consumed by the Mutation Lock verification.
     *   Thus, if the pageSize is 24, 25 requests will be sent in the Transact Write Request.
     */
    Integer pageSize();

    /**
     * @param strategy Optional. Defaults to reEncrypt with a default KMS Client.
     */
    Builder strategy(KeyManagementStrategy strategy);

    /**
     * @return Optional. Defaults to reEncrypt with a default KMS Client.
     */
    KeyManagementStrategy strategy();

    ApplyMutationInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationToken mutationToken;

    protected Integer pageSize;

    protected KeyManagementStrategy strategy;

    protected BuilderImpl() {}

    protected BuilderImpl(ApplyMutationInput model) {
      this.mutationToken = model.mutationToken();
      this.pageSize = model.pageSize();
      this.strategy = model.strategy();
    }

    public Builder mutationToken(MutationToken mutationToken) {
      this.mutationToken = mutationToken;
      return this;
    }

    public MutationToken mutationToken() {
      return this.mutationToken;
    }

    public Builder pageSize(Integer pageSize) {
      this.pageSize = pageSize;
      return this;
    }

    public Integer pageSize() {
      return this.pageSize;
    }

    public Builder strategy(KeyManagementStrategy strategy) {
      this.strategy = strategy;
      return this;
    }

    public KeyManagementStrategy strategy() {
      return this.strategy;
    }

    public ApplyMutationInput build() {
      if (Objects.isNull(this.mutationToken())) {
        throw new IllegalArgumentException(
          "Missing value for required field `mutationToken`"
        );
      }
      return new ApplyMutationInput(this);
    }
  }
}
