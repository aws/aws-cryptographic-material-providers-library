// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class QueryForVersionsInput {

  /**
   * Optional.
   *   If set, Query will start at this index and read forward.
   *   Otherwise, Query will start at the indexes begining.
   *   The Default Storage is DDB;
   *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  private final ByteBuffer exclusiveStartKey;

  /**
   * The Identifier of the Branch Key.
   */
  private final String Identifier;

  /**
   * The maximum read items.
   */
  private final Integer pageSize;

  protected QueryForVersionsInput(BuilderImpl builder) {
    this.exclusiveStartKey = builder.exclusiveStartKey();
    this.Identifier = builder.Identifier();
    this.pageSize = builder.pageSize();
  }

  /**
   * @return Optional.
   *   If set, Query will start at this index and read forward.
   *   Otherwise, Query will start at the indexes begining.
   *   The Default Storage is DDB;
   *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
   *   Note: While the Default Storage is DDB,
   *   the Key Store transforms the exclusiveStartKey into an opaque representation.
   */
  public ByteBuffer exclusiveStartKey() {
    return this.exclusiveStartKey;
  }

  /**
   * @return The Identifier of the Branch Key.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The maximum read items.
   */
  public Integer pageSize() {
    return this.pageSize;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param exclusiveStartKey Optional.
     *   If set, Query will start at this index and read forward.
     *   Otherwise, Query will start at the indexes begining.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    Builder exclusiveStartKey(ByteBuffer exclusiveStartKey);

    /**
     * @return Optional.
     *   If set, Query will start at this index and read forward.
     *   Otherwise, Query will start at the indexes begining.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    ByteBuffer exclusiveStartKey();

    /**
     * @param Identifier The Identifier of the Branch Key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Identifier of the Branch Key.
     */
    String Identifier();

    /**
     * @param pageSize The maximum read items.
     */
    Builder pageSize(Integer pageSize);

    /**
     * @return The maximum read items.
     */
    Integer pageSize();

    QueryForVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer exclusiveStartKey;

    protected String Identifier;

    protected Integer pageSize;

    protected BuilderImpl() {}

    protected BuilderImpl(QueryForVersionsInput model) {
      this.exclusiveStartKey = model.exclusiveStartKey();
      this.Identifier = model.Identifier();
      this.pageSize = model.pageSize();
    }

    public Builder exclusiveStartKey(ByteBuffer exclusiveStartKey) {
      this.exclusiveStartKey = exclusiveStartKey;
      return this;
    }

    public ByteBuffer exclusiveStartKey() {
      return this.exclusiveStartKey;
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder pageSize(Integer pageSize) {
      this.pageSize = pageSize;
      return this;
    }

    public Integer pageSize() {
      return this.pageSize;
    }

    public QueryForVersionsInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.pageSize())) {
        throw new IllegalArgumentException(
          "Missing value for required field `pageSize`"
        );
      }
      return new QueryForVersionsInput(this);
    }
  }
}
