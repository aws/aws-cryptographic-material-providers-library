// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class QueryForVersionsInput {

  private final ByteBuffer exclusiveStartKey;

  private final String Identifier;

  private final Integer pageSize;

  protected QueryForVersionsInput(BuilderImpl builder) {
    this.exclusiveStartKey = builder.exclusiveStartKey();
    this.Identifier = builder.Identifier();
    this.pageSize = builder.pageSize();
  }

  public ByteBuffer exclusiveStartKey() {
    return this.exclusiveStartKey;
  }

  public String Identifier() {
    return this.Identifier;
  }

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
    Builder exclusiveStartKey(ByteBuffer exclusiveStartKey);

    ByteBuffer exclusiveStartKey();

    Builder Identifier(String Identifier);

    String Identifier();

    Builder pageSize(Integer pageSize);

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
      if (Objects.nonNull(this.pageSize()) && this.pageSize() < 1) {
        throw new IllegalArgumentException(
          "`pageSize` must be greater than or equal to 1"
        );
      }
      return new QueryForVersionsInput(this);
    }
  }
}
