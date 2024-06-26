// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class ParsePublicKeyInput {

  private final ByteBuffer publicKey;

  protected ParsePublicKeyInput(BuilderImpl builder) {
    this.publicKey = builder.publicKey();
  }

  public ByteBuffer publicKey() {
    return this.publicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder publicKey(ByteBuffer publicKey);

    ByteBuffer publicKey();

    ParsePublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer publicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(ParsePublicKeyInput model) {
      this.publicKey = model.publicKey();
    }

    public Builder publicKey(ByteBuffer publicKey) {
      this.publicKey = publicKey;
      return this;
    }

    public ByteBuffer publicKey() {
      return this.publicKey;
    }

    public ParsePublicKeyInput build() {
      if (Objects.isNull(this.publicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `publicKey`"
        );
      }
      return new ParsePublicKeyInput(this);
    }
  }
}
