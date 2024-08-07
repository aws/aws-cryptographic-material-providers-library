// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class ECCPublicKey {

  private final ByteBuffer der;

  protected ECCPublicKey(BuilderImpl builder) {
    this.der = builder.der();
  }

  public ByteBuffer der() {
    return this.der;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder der(ByteBuffer der);

    ByteBuffer der();

    ECCPublicKey build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer der;

    protected BuilderImpl() {}

    protected BuilderImpl(ECCPublicKey model) {
      this.der = model.der();
    }

    public Builder der(ByteBuffer der) {
      this.der = der;
      return this;
    }

    public ByteBuffer der() {
      return this.der;
    }

    public ECCPublicKey build() {
      if (Objects.isNull(this.der())) {
        throw new IllegalArgumentException(
          "Missing value for required field `der`"
        );
      }
      return new ECCPublicKey(this);
    }
  }
}
