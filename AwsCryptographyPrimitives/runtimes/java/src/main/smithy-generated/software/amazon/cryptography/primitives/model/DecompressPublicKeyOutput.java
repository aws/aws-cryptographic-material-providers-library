// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class DecompressPublicKeyOutput {
  private final ECCPublicKey publicKey;

  protected DecompressPublicKeyOutput(BuilderImpl builder) {
    this.publicKey = builder.publicKey();
  }

  public ECCPublicKey publicKey() {
    return this.publicKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder publicKey(ECCPublicKey publicKey);

    ECCPublicKey publicKey();

    DecompressPublicKeyOutput build();
  }

  static class BuilderImpl implements Builder {
    protected ECCPublicKey publicKey;

    protected BuilderImpl() {
    }

    protected BuilderImpl(DecompressPublicKeyOutput model) {
      this.publicKey = model.publicKey();
    }

    public Builder publicKey(ECCPublicKey publicKey) {
      this.publicKey = publicKey;
      return this;
    }

    public ECCPublicKey publicKey() {
      return this.publicKey;
    }

    public DecompressPublicKeyOutput build() {
      if (Objects.isNull(this.publicKey()))  {
        throw new IllegalArgumentException("Missing value for required field `publicKey`");
      }
      return new DecompressPublicKeyOutput(this);
    }
  }
}
