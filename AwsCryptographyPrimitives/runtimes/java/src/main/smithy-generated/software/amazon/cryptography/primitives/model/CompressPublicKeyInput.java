// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class CompressPublicKeyInput {
  private final ECCPublicKey publicKey;

  private final ECDHCurveSpec eccCurve;

  protected CompressPublicKeyInput(BuilderImpl builder) {
    this.publicKey = builder.publicKey();
    this.eccCurve = builder.eccCurve();
  }

  public ECCPublicKey publicKey() {
    return this.publicKey;
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
    Builder publicKey(ECCPublicKey publicKey);

    ECCPublicKey publicKey();

    Builder eccCurve(ECDHCurveSpec eccCurve);

    ECDHCurveSpec eccCurve();

    CompressPublicKeyInput build();
  }

  static class BuilderImpl implements Builder {
    protected ECCPublicKey publicKey;

    protected ECDHCurveSpec eccCurve;

    protected BuilderImpl() {
    }

    protected BuilderImpl(CompressPublicKeyInput model) {
      this.publicKey = model.publicKey();
      this.eccCurve = model.eccCurve();
    }

    public Builder publicKey(ECCPublicKey publicKey) {
      this.publicKey = publicKey;
      return this;
    }

    public ECCPublicKey publicKey() {
      return this.publicKey;
    }

    public Builder eccCurve(ECDHCurveSpec eccCurve) {
      this.eccCurve = eccCurve;
      return this;
    }

    public ECDHCurveSpec eccCurve() {
      return this.eccCurve;
    }

    public CompressPublicKeyInput build() {
      if (Objects.isNull(this.publicKey()))  {
        throw new IllegalArgumentException("Missing value for required field `publicKey`");
      }
      if (Objects.isNull(this.eccCurve()))  {
        throw new IllegalArgumentException("Missing value for required field `eccCurve`");
      }
      return new CompressPublicKeyInput(this);
    }
  }
}
