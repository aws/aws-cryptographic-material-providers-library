// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class CompressPublicKeyOutput {
  private final ByteBuffer compressedPublicKey;

  protected CompressPublicKeyOutput(BuilderImpl builder) {
    this.compressedPublicKey = builder.compressedPublicKey();
  }

  public ByteBuffer compressedPublicKey() {
    return this.compressedPublicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder compressedPublicKey(ByteBuffer compressedPublicKey);

    ByteBuffer compressedPublicKey();

    CompressPublicKeyOutput build();
  }

  static class BuilderImpl implements Builder {
    protected ByteBuffer compressedPublicKey;

    protected BuilderImpl() {
    }

    protected BuilderImpl(CompressPublicKeyOutput model) {
      this.compressedPublicKey = model.compressedPublicKey();
    }

    public Builder compressedPublicKey(ByteBuffer compressedPublicKey) {
      this.compressedPublicKey = compressedPublicKey;
      return this;
    }

    public ByteBuffer compressedPublicKey() {
      return this.compressedPublicKey;
    }

    public CompressPublicKeyOutput build() {
      if (Objects.isNull(this.compressedPublicKey()))  {
        throw new IllegalArgumentException("Missing value for required field `compressedPublicKey`");
      }
      return new CompressPublicKeyOutput(this);
    }
  }
}
