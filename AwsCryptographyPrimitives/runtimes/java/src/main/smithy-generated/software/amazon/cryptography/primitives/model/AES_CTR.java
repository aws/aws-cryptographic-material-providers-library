// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.primitives.model;

import java.util.Objects;

public class AES_CTR {

  private final Integer keyLength;

  private final Integer nonceLength;

  protected AES_CTR(BuilderImpl builder) {
    this.keyLength = builder.keyLength();
    this.nonceLength = builder.nonceLength();
  }

  public Integer keyLength() {
    return this.keyLength;
  }

  public Integer nonceLength() {
    return this.nonceLength;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder keyLength(Integer keyLength);

    Integer keyLength();

    Builder nonceLength(Integer nonceLength);

    Integer nonceLength();

    AES_CTR build();
  }

  static class BuilderImpl implements Builder {

    protected Integer keyLength;

    protected Integer nonceLength;

    protected BuilderImpl() {}

    protected BuilderImpl(AES_CTR model) {
      this.keyLength = model.keyLength();
      this.nonceLength = model.nonceLength();
    }

    public Builder keyLength(Integer keyLength) {
      this.keyLength = keyLength;
      return this;
    }

    public Integer keyLength() {
      return this.keyLength;
    }

    public Builder nonceLength(Integer nonceLength) {
      this.nonceLength = nonceLength;
      return this;
    }

    public Integer nonceLength() {
      return this.nonceLength;
    }

    public AES_CTR build() {
      if (Objects.isNull(this.keyLength())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyLength`"
        );
      }
      if (Objects.nonNull(this.keyLength()) && this.keyLength() < 1) {
        throw new IllegalArgumentException(
          "`keyLength` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.keyLength()) && this.keyLength() > 32) {
        throw new IllegalArgumentException(
          "`keyLength` must be less than or equal to 32."
        );
      }
      if (Objects.isNull(this.nonceLength())) {
        throw new IllegalArgumentException(
          "Missing value for required field `nonceLength`"
        );
      }
      if (Objects.nonNull(this.nonceLength()) && this.nonceLength() < 0) {
        throw new IllegalArgumentException(
          "`nonceLength` must be greater than or equal to 0"
        );
      }
      if (Objects.nonNull(this.nonceLength()) && this.nonceLength() > 255) {
        throw new IllegalArgumentException(
          "`nonceLength` must be less than or equal to 255."
        );
      }
      return new AES_CTR(this);
    }
  }
}
