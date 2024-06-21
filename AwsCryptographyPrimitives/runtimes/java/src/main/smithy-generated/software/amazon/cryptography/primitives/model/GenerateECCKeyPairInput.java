// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class GenerateECCKeyPairInput {

  private final ECDHCurveSpec eccCurve;

  protected GenerateECCKeyPairInput(BuilderImpl builder) {
    this.eccCurve = builder.eccCurve();
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
    Builder eccCurve(ECDHCurveSpec eccCurve);

    ECDHCurveSpec eccCurve();

    GenerateECCKeyPairInput build();
  }

  static class BuilderImpl implements Builder {

    protected ECDHCurveSpec eccCurve;

    protected BuilderImpl() {}

    protected BuilderImpl(GenerateECCKeyPairInput model) {
      this.eccCurve = model.eccCurve();
    }

    public Builder eccCurve(ECDHCurveSpec eccCurve) {
      this.eccCurve = eccCurve;
      return this;
    }

    public ECDHCurveSpec eccCurve() {
      return this.eccCurve;
    }

    public GenerateECCKeyPairInput build() {
      if (Objects.isNull(this.eccCurve())) {
        throw new IllegalArgumentException(
          "Missing value for required field `eccCurve`"
        );
      }
      return new GenerateECCKeyPairInput(this);
    }
  }
}
