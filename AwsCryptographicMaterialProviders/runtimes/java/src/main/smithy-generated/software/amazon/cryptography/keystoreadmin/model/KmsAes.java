// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.AwsKms;

/**
 * Include all attributes of an item as Encryption Context
 * in a KMS Encrypt or Decrypt call,
 * effectively signing the attributes.
 */
public class KmsAes {

  private final KmsAesIdentifier KmsAesIdentifier;

  private final AwsKms AwsKms;

  protected KmsAes(BuilderImpl builder) {
    this.KmsAesIdentifier = builder.KmsAesIdentifier();
    this.AwsKms = builder.AwsKms();
  }

  public KmsAesIdentifier KmsAesIdentifier() {
    return this.KmsAesIdentifier;
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
    Builder KmsAesIdentifier(KmsAesIdentifier KmsAesIdentifier);

    KmsAesIdentifier KmsAesIdentifier();

    Builder AwsKms(AwsKms AwsKms);

    AwsKms AwsKms();

    KmsAes build();
  }

  static class BuilderImpl implements Builder {

    protected KmsAesIdentifier KmsAesIdentifier;

    protected AwsKms AwsKms;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsAes model) {
      this.KmsAesIdentifier = model.KmsAesIdentifier();
      this.AwsKms = model.AwsKms();
    }

    public Builder KmsAesIdentifier(KmsAesIdentifier KmsAesIdentifier) {
      this.KmsAesIdentifier = KmsAesIdentifier;
      return this;
    }

    public KmsAesIdentifier KmsAesIdentifier() {
      return this.KmsAesIdentifier;
    }

    public Builder AwsKms(AwsKms AwsKms) {
      this.AwsKms = AwsKms;
      return this;
    }

    public AwsKms AwsKms() {
      return this.AwsKms;
    }

    public KmsAes build() {
      if (Objects.isNull(this.KmsAesIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsAesIdentifier`"
        );
      }
      if (Objects.isNull(this.AwsKms())) {
        throw new IllegalArgumentException(
          "Missing value for required field `AwsKms`"
        );
      }
      return new KmsAes(this);
    }
  }
}
