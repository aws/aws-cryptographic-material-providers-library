// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class GenerateECCKeyPairOutput {

  private final ECDHCurveSpec eccCurve;

  private final ECCPrivateKey privateKey;

  private final ECCPublicKey publicKey;

  protected GenerateECCKeyPairOutput(BuilderImpl builder) {
    this.eccCurve = builder.eccCurve();
    this.privateKey = builder.privateKey();
    this.publicKey = builder.publicKey();
  }

  public ECDHCurveSpec eccCurve() {
    return this.eccCurve;
  }

  public ECCPrivateKey privateKey() {
    return this.privateKey;
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
    Builder eccCurve(ECDHCurveSpec eccCurve);

    ECDHCurveSpec eccCurve();

    Builder privateKey(ECCPrivateKey privateKey);

    ECCPrivateKey privateKey();

    Builder publicKey(ECCPublicKey publicKey);

    ECCPublicKey publicKey();

    GenerateECCKeyPairOutput build();
  }

  static class BuilderImpl implements Builder {

    protected ECDHCurveSpec eccCurve;

    protected ECCPrivateKey privateKey;

    protected ECCPublicKey publicKey;

    protected BuilderImpl() {}

    protected BuilderImpl(GenerateECCKeyPairOutput model) {
      this.eccCurve = model.eccCurve();
      this.privateKey = model.privateKey();
      this.publicKey = model.publicKey();
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

    public Builder publicKey(ECCPublicKey publicKey) {
      this.publicKey = publicKey;
      return this;
    }

    public ECCPublicKey publicKey() {
      return this.publicKey;
    }

    public GenerateECCKeyPairOutput build() {
      if (Objects.isNull(this.eccCurve())) {
        throw new IllegalArgumentException(
          "Missing value for required field `eccCurve`"
        );
      }
      if (Objects.isNull(this.privateKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `privateKey`"
        );
      }
      if (Objects.isNull(this.publicKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `publicKey`"
        );
      }
      return new GenerateECCKeyPairOutput(this);
    }
  }
}
