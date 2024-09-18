// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class KeyManagement {

  /**
   * The AWS KMS configuration this Key Store with use to authenticate branch keys.
   */
  private final AwsKms kms;

  protected KeyManagement(BuilderImpl builder) {
    this.kms = builder.kms();
  }

  /**
   * @return The AWS KMS configuration this Key Store with use to authenticate branch keys.
   */
  public AwsKms kms() {
    return this.kms;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kms The AWS KMS configuration this Key Store with use to authenticate branch keys.
     */
    Builder kms(AwsKms kms);

    /**
     * @return The AWS KMS configuration this Key Store with use to authenticate branch keys.
     */
    AwsKms kms();

    KeyManagement build();
  }

  static class BuilderImpl implements Builder {

    protected AwsKms kms;

    protected BuilderImpl() {}

    protected BuilderImpl(KeyManagement model) {
      this.kms = model.kms();
    }

    public Builder kms(AwsKms kms) {
      this.kms = kms;
      return this;
    }

    public AwsKms kms() {
      return this.kms;
    }

    public KeyManagement build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KeyManagement` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KeyManagement(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kms };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
