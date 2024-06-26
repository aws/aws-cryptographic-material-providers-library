// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class DecompressPublicKeyInput {

  private final ByteBuffer compressedPublicKey;

  private final ECDHCurveSpec eccCurve;

  protected DecompressPublicKeyInput(BuilderImpl builder) {
    this.compressedPublicKey = builder.compressedPublicKey();
    this.eccCurve = builder.eccCurve();
  }

  public ByteBuffer compressedPublicKey() {
    return this.compressedPublicKey;
  }

  public ECDHCurveSpec eccCurve() {
    return this.eccCurve;
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

    Builder eccCurve(ECDHCurveSpec eccCurve);

    ECDHCurveSpec eccCurve();

    DecompressPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer compressedPublicKey;

    protected ECDHCurveSpec eccCurve;

    protected BuilderImpl() {}

    protected BuilderImpl(DecompressPublicKeyInput model) {
      this.compressedPublicKey = model.compressedPublicKey();
      this.eccCurve = model.eccCurve();
    }

    public Builder compressedPublicKey(ByteBuffer compressedPublicKey) {
      this.compressedPublicKey = compressedPublicKey;
      return this;
    }

    public ByteBuffer compressedPublicKey() {
      return this.compressedPublicKey;
    }

    public Builder eccCurve(ECDHCurveSpec eccCurve) {
      this.eccCurve = eccCurve;
      return this;
    }

    public ECDHCurveSpec eccCurve() {
      return this.eccCurve;
    }

    public DecompressPublicKeyInput build() {
      if (Objects.isNull(this.compressedPublicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `compressedPublicKey`"
        );
      }
      if (Objects.isNull(this.eccCurve())) {
        throw new IllegalArgumentException(
          "Missing value for required field `eccCurve`"
        );
      }
      return new DecompressPublicKeyInput(this);
    }
  }
}
