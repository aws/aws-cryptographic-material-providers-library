// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class KmsSymmetricKeyArn {

  /**
   * Key Store is restricted to only this KMS Key ARN.
   *   If a different KMS Key ARN is encountered
   *   when creating, versioning, or getting a Branch Key or Beacon Key,
   *   KMS is never called and an exception is thrown.
   *   While a Multi-Region Key (MKR) may be provided,
   *   the whole ARN, including the Region,
   *   is persisted in Branch Keys and
   *   MUST strictly equal this value to be considered valid.
   */
  private final String KmsKeyArn;

  protected KmsSymmetricKeyArn(BuilderImpl builder) {
    this.KmsKeyArn = builder.KmsKeyArn();
  }

  /**
   * @return Key Store is restricted to only this KMS Key ARN.
   *   If a different KMS Key ARN is encountered
   *   when creating, versioning, or getting a Branch Key or Beacon Key,
   *   KMS is never called and an exception is thrown.
   *   While a Multi-Region Key (MKR) may be provided,
   *   the whole ARN, including the Region,
   *   is persisted in Branch Keys and
   *   MUST strictly equal this value to be considered valid.
   */
  public String KmsKeyArn() {
    return this.KmsKeyArn;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KmsKeyArn Key Store is restricted to only this KMS Key ARN.
     *   If a different KMS Key ARN is encountered
     *   when creating, versioning, or getting a Branch Key or Beacon Key,
     *   KMS is never called and an exception is thrown.
     *   While a Multi-Region Key (MKR) may be provided,
     *   the whole ARN, including the Region,
     *   is persisted in Branch Keys and
     *   MUST strictly equal this value to be considered valid.
     */
    Builder KmsKeyArn(String KmsKeyArn);

    /**
     * @return Key Store is restricted to only this KMS Key ARN.
     *   If a different KMS Key ARN is encountered
     *   when creating, versioning, or getting a Branch Key or Beacon Key,
     *   KMS is never called and an exception is thrown.
     *   While a Multi-Region Key (MKR) may be provided,
     *   the whole ARN, including the Region,
     *   is persisted in Branch Keys and
     *   MUST strictly equal this value to be considered valid.
     */
    String KmsKeyArn();

    KmsSymmetricKeyArn build();
  }

  static class BuilderImpl implements Builder {

    protected String KmsKeyArn;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsSymmetricKeyArn model) {
      this.KmsKeyArn = model.KmsKeyArn();
    }

    public Builder KmsKeyArn(String KmsKeyArn) {
      this.KmsKeyArn = KmsKeyArn;
      return this;
    }

    public String KmsKeyArn() {
      return this.KmsKeyArn;
    }

    public KmsSymmetricKeyArn build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KmsSymmetricKeyArn` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KmsSymmetricKeyArn(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.KmsKeyArn };
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
