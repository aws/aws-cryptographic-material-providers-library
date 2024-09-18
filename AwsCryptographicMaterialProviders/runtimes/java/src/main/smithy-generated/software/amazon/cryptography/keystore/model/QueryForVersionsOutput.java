// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.List;
import java.util.Objects;

public class QueryForVersionsOutput {

  /**
   * If none-empty, Query did not finish searching storage.
   *   Next Query should resume from here.
   *   The Default Storage is DDB;
   *   see Amazon DynamoDB's definition of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  private final ByteBuffer ExclusiveStartKey;

  /**
   * Up to pageSize list of version (decrypt only) items of a Branch Key.
   */
  private final List<EncryptedHierarchicalKey> Items;

  protected QueryForVersionsOutput(BuilderImpl builder) {
    this.ExclusiveStartKey = builder.ExclusiveStartKey();
    this.Items = builder.Items();
  }

  /**
   * @return If none-empty, Query did not finish searching storage.
   *   Next Query should resume from here.
   *   The Default Storage is DDB;
   *   see Amazon DynamoDB's definition of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  public ByteBuffer ExclusiveStartKey() {
    return this.ExclusiveStartKey;
  }

  /**
   * @return Up to pageSize list of version (decrypt only) items of a Branch Key.
   */
  public List<EncryptedHierarchicalKey> Items() {
    return this.Items;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param ExclusiveStartKey If none-empty, Query did not finish searching storage.
     *   Next Query should resume from here.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's definition of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    Builder ExclusiveStartKey(ByteBuffer ExclusiveStartKey);

    /**
     * @return If none-empty, Query did not finish searching storage.
     *   Next Query should resume from here.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's definition of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    ByteBuffer ExclusiveStartKey();

    /**
     * @param Items Up to pageSize list of version (decrypt only) items of a Branch Key.
     */
    Builder Items(List<EncryptedHierarchicalKey> Items);

    /**
     * @return Up to pageSize list of version (decrypt only) items of a Branch Key.
     */
    List<EncryptedHierarchicalKey> Items();

    QueryForVersionsOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer ExclusiveStartKey;

    protected List<EncryptedHierarchicalKey> Items;

    protected BuilderImpl() {}

    protected BuilderImpl(QueryForVersionsOutput model) {
      this.ExclusiveStartKey = model.ExclusiveStartKey();
      this.Items = model.Items();
    }

    public Builder ExclusiveStartKey(ByteBuffer ExclusiveStartKey) {
      this.ExclusiveStartKey = ExclusiveStartKey;
      return this;
    }

    public ByteBuffer ExclusiveStartKey() {
      return this.ExclusiveStartKey;
    }

    public Builder Items(List<EncryptedHierarchicalKey> Items) {
      this.Items = Items;
      return this;
    }

    public List<EncryptedHierarchicalKey> Items() {
      return this.Items;
    }

    public QueryForVersionsOutput build() {
      if (Objects.isNull(this.ExclusiveStartKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `ExclusiveStartKey`"
        );
      }
      if (Objects.isNull(this.Items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Items`"
        );
      }
      return new QueryForVersionsOutput(this);
    }
  }
}
