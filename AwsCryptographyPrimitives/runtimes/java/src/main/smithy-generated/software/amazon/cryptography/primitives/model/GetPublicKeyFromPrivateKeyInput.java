// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class GetPublicKeyFromPrivateKeyInput {
  private final ECDHCurveSpec eccCurve;

  private final ECCPrivateKey privateKey;

  protected GetPublicKeyFromPrivateKeyInput(BuilderImpl builder) {
    this.eccCurve = builder.eccCurve();
    this.privateKey = builder.privateKey();
  }

  public ECDHCurveSpec eccCurve() {
    return this.eccCurve;
  }

  public ECCPrivateKey privateKey() {
    return this.privateKey;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder eccCurve(ECDHCurveSpec eccCurve);

    ECDHCurveSpec eccCurve();

    Builder privateKey(ECCPrivateKey privateKey);

    ECCPrivateKey privateKey();

    GetPublicKeyFromPrivateKeyInput build();
  }

  static class BuilderImpl implements Builder {
    protected ECDHCurveSpec eccCurve;

    protected ECCPrivateKey privateKey;

    protected BuilderImpl() {
    }

    protected BuilderImpl(GetPublicKeyFromPrivateKeyInput model) {
      this.eccCurve = model.eccCurve();
      this.privateKey = model.privateKey();
    }

    public Builder eccCurve(ECDHCurveSpec eccCurve) {
      this.eccCurve = eccCurve;
      return this;
    }

    public ECDHCurveSpec eccCurve() {
      return this.eccCurve;
    }

    public Builder privateKey(ECCPrivateKey privateKey) {
      this.privateKey = privateKey;
      return this;
    }

    public ECCPrivateKey privateKey() {
      return this.privateKey;
    }

    public GetPublicKeyFromPrivateKeyInput build() {
      if (Objects.isNull(this.eccCurve()))  {
        throw new IllegalArgumentException("Missing value for required field `eccCurve`");
      }
      if (Objects.isNull(this.privateKey()))  {
        throw new IllegalArgumentException("Missing value for required field `privateKey`");
      }
      return new GetPublicKeyFromPrivateKeyInput(this);
    }
  }
}
