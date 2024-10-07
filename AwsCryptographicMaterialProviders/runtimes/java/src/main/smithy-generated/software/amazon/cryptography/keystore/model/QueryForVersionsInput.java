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
  private final ByteBuffer PageIndex;

  /**
   * The Identifier of the Branch Key.
   */
  private final String Identifier;

  /**
   * The maximum read items.
   */
  private final Integer PageSize;

  protected QueryForVersionsInput(BuilderImpl builder) {
    this.PageIndex = builder.PageIndex();
    this.Identifier = builder.Identifier();
    this.PageSize = builder.PageSize();
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
  public ByteBuffer PageIndex() {
    return this.PageIndex;
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
  public Integer PageSize() {
    return this.PageSize;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param PageIndex Optional.
     *   If set, Query will start at this index and read forward.
     *   Otherwise, Query will start at the indexes begining.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    Builder PageIndex(ByteBuffer PageIndex);

    /**
     * @return Optional.
     *   If set, Query will start at this index and read forward.
     *   Otherwise, Query will start at the indexes begining.
     *   The Default Storage is DDB;
     *   see Amazon DynamoDB's defination of exclusiveStartKey for details.
     *   Note: While the Default Storage is DDB,
     *   the Key Store transforms the exclusiveStartKey into an opaque representation.
     */
    ByteBuffer PageIndex();

    /**
     * @param Identifier The Identifier of the Branch Key.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Identifier of the Branch Key.
     */
    String Identifier();

    /**
     * @param PageSize The maximum read items.
     */
    Builder PageSize(Integer PageSize);

    /**
     * @return The maximum read items.
     */
    Integer PageSize();

    QueryForVersionsInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer PageIndex;

    protected String Identifier;

    protected Integer PageSize;

    protected BuilderImpl() {}

    protected BuilderImpl(QueryForVersionsInput model) {
      this.PageIndex = model.PageIndex();
      this.Identifier = model.Identifier();
      this.PageSize = model.PageSize();
    }

    public Builder PageIndex(ByteBuffer PageIndex) {
      this.PageIndex = PageIndex;
      return this;
    }

    public ByteBuffer PageIndex() {
      return this.PageIndex;
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder PageSize(Integer PageSize) {
      this.PageSize = PageSize;
      return this;
    }

    public Integer PageSize() {
      return this.PageSize;
    }

    public QueryForVersionsInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.PageSize())) {
        throw new IllegalArgumentException(
          "Missing value for required field `PageSize`"
        );
      }
      return new QueryForVersionsInput(this);
    }
  }
}
