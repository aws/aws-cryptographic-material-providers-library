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
   *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  private final ByteBuffer PageIndex;

  /**
   * Up to pageSize list of version (decrypt only) items of a Branch Key.
   */
  private final List<EncryptedHierarchicalKey> Items;

  protected QueryForVersionsOutput(BuilderImpl builder) {
    this.PageIndex = builder.PageIndex();
    this.Items = builder.Items();
  }

  /**
   * @return If none-empty, Query did not finish searching storage.
   *   Next Query should resume from here.
   *   The Default Storage is DDB;
   *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  public ByteBuffer PageIndex() {
    return this.PageIndex;
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
     * @param PageIndex If none-empty, Query did not finish searching storage.
     *   Next Query should resume from here.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    Builder PageIndex(ByteBuffer PageIndex);

    /**
     * @return If none-empty, Query did not finish searching storage.
     *   Next Query should resume from here.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    ByteBuffer PageIndex();

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

    protected ByteBuffer PageIndex;

    protected List<EncryptedHierarchicalKey> Items;

    protected BuilderImpl() {}

    protected BuilderImpl(QueryForVersionsOutput model) {
      this.PageIndex = model.PageIndex();
      this.Items = model.Items();
    }

    public Builder PageIndex(ByteBuffer PageIndex) {
      this.PageIndex = PageIndex;
      return this;
    }

    public ByteBuffer PageIndex() {
      return this.PageIndex;
    }

    public Builder Items(List<EncryptedHierarchicalKey> Items) {
      this.Items = Items;
      return this;
    }

    public List<EncryptedHierarchicalKey> Items() {
      return this.Items;
    }

    public QueryForVersionsOutput build() {
      if (Objects.isNull(this.PageIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `PageIndex`"
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
