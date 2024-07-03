// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class DeriveSharedSecretOutput {
  private final ByteBuffer sharedSecret;

  protected DeriveSharedSecretOutput(BuilderImpl builder) {
    this.sharedSecret = builder.sharedSecret();
  }

  public ByteBuffer sharedSecret() {
    return this.sharedSecret;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder sharedSecret(ByteBuffer sharedSecret);

    ByteBuffer sharedSecret();

    DeriveSharedSecretOutput build();
  }

  static class BuilderImpl implements Builder {
    protected ByteBuffer sharedSecret;

    protected BuilderImpl() {
    }

    protected BuilderImpl(DeriveSharedSecretOutput model) {
      this.sharedSecret = model.sharedSecret();
    }

    public Builder sharedSecret(ByteBuffer sharedSecret) {
      this.sharedSecret = sharedSecret;
      return this;
    }

    public ByteBuffer sharedSecret() {
      return this.sharedSecret;
    }

    public DeriveSharedSecretOutput build() {
      if (Objects.isNull(this.sharedSecret()))  {
        throw new IllegalArgumentException("Missing value for required field `sharedSecret`");
      }
      return new DeriveSharedSecretOutput(this);
    }
  }
}
