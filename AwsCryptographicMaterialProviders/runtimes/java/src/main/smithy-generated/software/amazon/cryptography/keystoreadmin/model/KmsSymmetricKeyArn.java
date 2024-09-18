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

  /**
   * If an MRK ARN is provided,
   *   and the persisted Branch Key holds an MRK ARN,
   *   then those two ARNs may differ in region,
   *   although they must be otherwise equal.
   *   If either ARN is not an MRK ARN, then
   *   KmsMRKeyArn behaves exactly as kmsKeyArn.
   */
  private final String KmsMRKeyArn;

  protected KmsSymmetricKeyArn(BuilderImpl builder) {
    this.KmsKeyArn = builder.KmsKeyArn();
    this.KmsMRKeyArn = builder.KmsMRKeyArn();
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

  /**
   * @return If an MRK ARN is provided,
   *   and the persisted Branch Key holds an MRK ARN,
   *   then those two ARNs may differ in region,
   *   although they must be otherwise equal.
   *   If either ARN is not an MRK ARN, then
   *   KmsMRKeyArn behaves exactly as kmsKeyArn.
   */
  public String KmsMRKeyArn() {
    return this.KmsMRKeyArn;
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

    /**
     * @param KmsMRKeyArn If an MRK ARN is provided,
     *   and the persisted Branch Key holds an MRK ARN,
     *   then those two ARNs may differ in region,
     *   although they must be otherwise equal.
     *   If either ARN is not an MRK ARN, then
     *   KmsMRKeyArn behaves exactly as kmsKeyArn.
     */
    Builder KmsMRKeyArn(String KmsMRKeyArn);

    /**
     * @return If an MRK ARN is provided,
     *   and the persisted Branch Key holds an MRK ARN,
     *   then those two ARNs may differ in region,
     *   although they must be otherwise equal.
     *   If either ARN is not an MRK ARN, then
     *   KmsMRKeyArn behaves exactly as kmsKeyArn.
     */
    String KmsMRKeyArn();

    KmsSymmetricKeyArn build();
  }

  static class BuilderImpl implements Builder {

    protected String KmsKeyArn;

    protected String KmsMRKeyArn;

    protected BuilderImpl() {}

    protected BuilderImpl(KmsSymmetricKeyArn model) {
      this.KmsKeyArn = model.KmsKeyArn();
      this.KmsMRKeyArn = model.KmsMRKeyArn();
    }

    public Builder KmsKeyArn(String KmsKeyArn) {
      this.KmsKeyArn = KmsKeyArn;
      return this;
    }

    public String KmsKeyArn() {
      return this.KmsKeyArn;
    }

    public Builder KmsMRKeyArn(String KmsMRKeyArn) {
      this.KmsMRKeyArn = KmsMRKeyArn;
      return this;
    }

    public String KmsMRKeyArn() {
      return this.KmsMRKeyArn;
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
      Object[] allValues = { this.KmsKeyArn, this.KmsMRKeyArn };
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
