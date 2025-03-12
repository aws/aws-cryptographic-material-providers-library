// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.primitives.model.DigestAlgorithm;

public class HKDF {

  private final DigestAlgorithm hmac;

  private final Integer saltLength;

  private final Integer inputKeyLength;

  private final Integer outputKeyLength;

  protected HKDF(BuilderImpl builder) {
    this.hmac = builder.hmac();
    this.saltLength = builder.saltLength();
    this.inputKeyLength = builder.inputKeyLength();
    this.outputKeyLength = builder.outputKeyLength();
  }

  public DigestAlgorithm hmac() {
    return this.hmac;
  }

  public Integer saltLength() {
    return this.saltLength;
  }

  public Integer inputKeyLength() {
    return this.inputKeyLength;
  }

  public Integer outputKeyLength() {
    return this.outputKeyLength;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder hmac(DigestAlgorithm hmac);

    DigestAlgorithm hmac();

    Builder saltLength(Integer saltLength);

    Integer saltLength();

    Builder inputKeyLength(Integer inputKeyLength);

    Integer inputKeyLength();

    Builder outputKeyLength(Integer outputKeyLength);

    Integer outputKeyLength();

    HKDF build();
  }

  static class BuilderImpl implements Builder {

    protected DigestAlgorithm hmac;

    protected Integer saltLength;

    protected Integer inputKeyLength;

    protected Integer outputKeyLength;

    protected BuilderImpl() {}

    protected BuilderImpl(HKDF model) {
      this.hmac = model.hmac();
      this.saltLength = model.saltLength();
      this.inputKeyLength = model.inputKeyLength();
      this.outputKeyLength = model.outputKeyLength();
    }

    public Builder hmac(DigestAlgorithm hmac) {
      this.hmac = hmac;
      return this;
    }

    public DigestAlgorithm hmac() {
      return this.hmac;
    }

    public Builder saltLength(Integer saltLength) {
      this.saltLength = saltLength;
      return this;
    }

    public Integer saltLength() {
      return this.saltLength;
    }

    public Builder inputKeyLength(Integer inputKeyLength) {
      this.inputKeyLength = inputKeyLength;
      return this;
    }

    public Integer inputKeyLength() {
      return this.inputKeyLength;
    }

    public Builder outputKeyLength(Integer outputKeyLength) {
      this.outputKeyLength = outputKeyLength;
      return this;
    }

    public Integer outputKeyLength() {
      return this.outputKeyLength;
    }

    public HKDF build() {
      if (Objects.isNull(this.hmac())) {
        throw new IllegalArgumentException(
          "Missing value for required field `hmac`"
        );
      }
      if (Objects.isNull(this.saltLength())) {
        throw new IllegalArgumentException(
          "Missing value for required field `saltLength`"
        );
      }
      if (Objects.nonNull(this.saltLength()) && this.saltLength() < 0) {
        throw new IllegalArgumentException(
          "`saltLength` must be greater than or equal to 0"
        );
      }
      if (Objects.isNull(this.inputKeyLength())) {
        throw new IllegalArgumentException(
          "Missing value for required field `inputKeyLength`"
        );
      }
      if (Objects.nonNull(this.inputKeyLength()) && this.inputKeyLength() < 1) {
        throw new IllegalArgumentException(
          "`inputKeyLength` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.inputKeyLength()) && this.inputKeyLength() > 32
      ) {
        throw new IllegalArgumentException(
          "`inputKeyLength` must be less than or equal to 32."
        );
      }
      if (Objects.isNull(this.outputKeyLength())) {
        throw new IllegalArgumentException(
          "Missing value for required field `outputKeyLength`"
        );
      }
      if (
        Objects.nonNull(this.outputKeyLength()) && this.outputKeyLength() < 1
      ) {
        throw new IllegalArgumentException(
          "`outputKeyLength` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.outputKeyLength()) && this.outputKeyLength() > 32
      ) {
        throw new IllegalArgumentException(
          "`outputKeyLength` must be less than or equal to 32."
        );
      }
      return new HKDF(this);
    }
  }
}
