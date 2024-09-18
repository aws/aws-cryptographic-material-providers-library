// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.AwsKms;

/**
 * Items of non-cryptographic material nature are protected by KMS.
 * This is done by including all attributes of an item as Encryption Context
 * in a KMS Encrypt or Decrypt call,
 * effectively signing the attributes.
 */
public class KmsSymmetricEncryption {

  private final KmsSymmetricKeyArn KmsArn;

  private final AwsKms AwsKms;

  protected KmsSymmetricEncryption(BuilderImpl builder) {
    this.KmsArn = builder.KmsArn();
    this.AwsKms = builder.AwsKms();
  }

  public KmsSymmetricKeyArn KmsArn() {
    return this.KmsArn;
  }

  public AwsKms AwsKms() {
    return this.AwsKms;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder KmsArn(KmsSymmetricKeyArn KmsArn);

    KmsSymmetricKeyArn KmsArn();

    Builder AwsKms(AwsKms AwsKms);

    AwsKms AwsKms();

    KmsSymmetricEncryption build();
  }

  static class BuilderImpl implements Builder {

    protected KmsSymmetricKeyArn KmsArn;

    protected AwsKms AwsKms;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsSymmetricEncryption model) {
      this.KmsArn = model.KmsArn();
      this.AwsKms = model.AwsKms();
    }

    public Builder KmsArn(KmsSymmetricKeyArn KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public KmsSymmetricKeyArn KmsArn() {
      return this.KmsArn;
    }

    public Builder AwsKms(AwsKms AwsKms) {
      this.AwsKms = AwsKms;
      return this;
    }

    public AwsKms AwsKms() {
      return this.AwsKms;
    }

    public KmsSymmetricEncryption build() {
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      if (Objects.isNull(this.AwsKms())) {
        throw new IllegalArgumentException(
          "Missing value for required field `AwsKms`"
        );
      }
      return new KmsSymmetricEncryption(this);
    }
  }
}
