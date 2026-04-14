// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Outputs for computing a cache identifier.
 */
public class GetCacheIdentifierOutput {

  /**
   * The computed cache entry identifier.
   */
  private final ByteBuffer identifier;

  protected GetCacheIdentifierOutput(BuilderImpl builder) {
    this.identifier = builder.identifier();
  }

  /**
   * @return The computed cache entry identifier.
   */
  public ByteBuffer identifier() {
    return this.identifier;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param identifier The computed cache entry identifier.
     */
    Builder identifier(ByteBuffer identifier);

    /**
     * @return The computed cache entry identifier.
     */
    ByteBuffer identifier();

    GetCacheIdentifierOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer identifier;

    protected BuilderImpl() {}

    protected BuilderImpl(GetCacheIdentifierOutput model) {
      this.identifier = model.identifier();
    }

    public Builder identifier(ByteBuffer identifier) {
      this.identifier = identifier;
      return this;
    }

    public ByteBuffer identifier() {
      return this.identifier;
    }

    public GetCacheIdentifierOutput build() {
      if (Objects.isNull(this.identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `identifier`"
        );
      }
      return new GetCacheIdentifierOutput(this);
    }
  }
}
