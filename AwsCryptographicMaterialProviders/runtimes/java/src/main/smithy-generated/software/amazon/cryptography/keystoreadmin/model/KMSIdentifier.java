// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;

public class KMSIdentifier {

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
  private final String kmsKeyArn;

  /**
   * If an MRK ARN is provided,
   *   and the persisted Branch Key holds an MRK ARN,
   *   then those two ARNs may differ in region,
   *   although they must be otherwise equal.
   *   If either ARN is not an MRK ARN, then
   *   kmsMRKeyArn behaves exactly as kmsKeyArn.
   */
  private final String kmsMRKeyArn;

  protected KMSIdentifier(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.kmsMRKeyArn = builder.kmsMRKeyArn();
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
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return If an MRK ARN is provided,
   *   and the persisted Branch Key holds an MRK ARN,
   *   then those two ARNs may differ in region,
   *   although they must be otherwise equal.
   *   If either ARN is not an MRK ARN, then
   *   kmsMRKeyArn behaves exactly as kmsKeyArn.
   */
  public String kmsMRKeyArn() {
    return this.kmsMRKeyArn;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn Key Store is restricted to only this KMS Key ARN.
     *   If a different KMS Key ARN is encountered
     *   when creating, versioning, or getting a Branch Key or Beacon Key,
     *   KMS is never called and an exception is thrown.
     *   While a Multi-Region Key (MKR) may be provided,
     *   the whole ARN, including the Region,
     *   is persisted in Branch Keys and
     *   MUST strictly equal this value to be considered valid.
     */
    Builder kmsKeyArn(String kmsKeyArn);

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
    String kmsKeyArn();

    /**
     * @param kmsMRKeyArn If an MRK ARN is provided,
     *   and the persisted Branch Key holds an MRK ARN,
     *   then those two ARNs may differ in region,
     *   although they must be otherwise equal.
     *   If either ARN is not an MRK ARN, then
     *   kmsMRKeyArn behaves exactly as kmsKeyArn.
     */
    Builder kmsMRKeyArn(String kmsMRKeyArn);

    /**
     * @return If an MRK ARN is provided,
     *   and the persisted Branch Key holds an MRK ARN,
     *   then those two ARNs may differ in region,
     *   although they must be otherwise equal.
     *   If either ARN is not an MRK ARN, then
     *   kmsMRKeyArn behaves exactly as kmsKeyArn.
     */
    String kmsMRKeyArn();

    KMSIdentifier build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected String kmsMRKeyArn;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSIdentifier model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.kmsMRKeyArn = model.kmsMRKeyArn();
    }

    public Builder kmsKeyArn(String kmsKeyArn) {
      this.kmsKeyArn = kmsKeyArn;
      return this;
    }

    public String kmsKeyArn() {
      return this.kmsKeyArn;
    }

    public Builder kmsMRKeyArn(String kmsMRKeyArn) {
      this.kmsMRKeyArn = kmsMRKeyArn;
      return this;
    }

    public String kmsMRKeyArn() {
      return this.kmsMRKeyArn;
    }

    public KMSIdentifier build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KMSIdentifier` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KMSIdentifier(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsKeyArn, this.kmsMRKeyArn };
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
