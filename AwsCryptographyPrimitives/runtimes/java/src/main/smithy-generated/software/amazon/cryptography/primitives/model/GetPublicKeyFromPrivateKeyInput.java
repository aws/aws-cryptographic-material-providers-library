// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class GetPublicKeyFromPrivateKeyInput {

  private final ByteBuffer privateKey;

  protected GetPublicKeyFromPrivateKeyInput(BuilderImpl builder) {
    this.privateKey = builder.privateKey();
  }

  public ByteBuffer privateKey() {
    return this.privateKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder privateKey(ByteBuffer privateKey);

    ByteBuffer privateKey();

    GetPublicKeyFromPrivateKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer privateKey;

    protected BuilderImpl() {}

    protected BuilderImpl(GetPublicKeyFromPrivateKeyInput model) {
      this.privateKey = model.privateKey();
    }

    public Builder privateKey(ByteBuffer privateKey) {
      this.privateKey = privateKey;
      return this;
    }

    public ByteBuffer privateKey() {
      return this.privateKey;
    }

    public GetPublicKeyFromPrivateKeyInput build() {
      if (Objects.isNull(this.privateKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `privateKey`"
        );
      }
      return new GetPublicKeyFromPrivateKeyInput(this);
    }
  }
}
