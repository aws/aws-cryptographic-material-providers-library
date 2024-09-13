// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.List;
import java.util.Objects;

public class QueryForVersionsOutput {

  private final ByteBuffer exclusiveStartKey;

  private final List<EncryptedHierarchicalKey> items;

  protected QueryForVersionsOutput(BuilderImpl builder) {
    this.exclusiveStartKey = builder.exclusiveStartKey();
    this.items = builder.items();
  }

  public ByteBuffer exclusiveStartKey() {
    return this.exclusiveStartKey;
  }

  public List<EncryptedHierarchicalKey> items() {
    return this.items;
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

    Builder items(List<EncryptedHierarchicalKey> items);

    List<EncryptedHierarchicalKey> items();

    QueryForVersionsOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer exclusiveStartKey;

    protected List<EncryptedHierarchicalKey> items;

    protected BuilderImpl() {}

    protected BuilderImpl(QueryForVersionsOutput model) {
      this.exclusiveStartKey = model.exclusiveStartKey();
      this.items = model.items();
    }

    public Builder exclusiveStartKey(ByteBuffer exclusiveStartKey) {
      this.exclusiveStartKey = exclusiveStartKey;
      return this;
    }

    public ByteBuffer exclusiveStartKey() {
      return this.exclusiveStartKey;
    }

    public Builder items(List<EncryptedHierarchicalKey> items) {
      this.items = items;
      return this;
    }

    public List<EncryptedHierarchicalKey> items() {
      return this.items;
    }

    public QueryForVersionsOutput build() {
      if (Objects.isNull(this.exclusiveStartKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `exclusiveStartKey`"
        );
      }
      if (Objects.isNull(this.items())) {
        throw new IllegalArgumentException(
          "Missing value for required field `items`"
        );
      }
      return new QueryForVersionsOutput(this);
    }
  }
}
