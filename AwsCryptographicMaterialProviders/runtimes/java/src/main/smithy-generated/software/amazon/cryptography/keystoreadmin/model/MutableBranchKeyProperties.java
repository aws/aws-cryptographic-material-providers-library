// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;
import java.util.Objects;

/**
 *
 * Define the Mutable Properties of a Branch Key.
 * As of v1.9.0, the Mutable Properties are:
 * - The KmsArn protecting the Branch Key
 * - The custom encryption context of a Branch Key
 */
public class MutableBranchKeyProperties {

  /**
   * The KmsArn protecting the Branch Key.
   */
  private final String KmsArn;

  /**
   * The custom Encryption Context authenticated with this Branch Key.
   */
  private final Map<String, String> CustomEncryptionContext;

  protected MutableBranchKeyProperties(BuilderImpl builder) {
    this.KmsArn = builder.KmsArn();
    this.CustomEncryptionContext = builder.CustomEncryptionContext();
  }

  /**
   * @return The KmsArn protecting the Branch Key.
   */
  public String KmsArn() {
    return this.KmsArn;
  }

  /**
   * @return The custom Encryption Context authenticated with this Branch Key.
   */
  public Map<String, String> CustomEncryptionContext() {
    return this.CustomEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param KmsArn The KmsArn protecting the Branch Key.
     */
    Builder KmsArn(String KmsArn);

    /**
     * @return The KmsArn protecting the Branch Key.
     */
    String KmsArn();

    /**
     * @param CustomEncryptionContext The custom Encryption Context authenticated with this Branch Key.
     */
    Builder CustomEncryptionContext(
      Map<String, String> CustomEncryptionContext
    );

    /**
     * @return The custom Encryption Context authenticated with this Branch Key.
     */
    Map<String, String> CustomEncryptionContext();

    MutableBranchKeyProperties build();
  }

  static class BuilderImpl implements Builder {

    protected String KmsArn;

    protected Map<String, String> CustomEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(MutableBranchKeyProperties model) {
      this.KmsArn = model.KmsArn();
      this.CustomEncryptionContext = model.CustomEncryptionContext();
    }

    public Builder KmsArn(String KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public String KmsArn() {
      return this.KmsArn;
    }

    public Builder CustomEncryptionContext(
      Map<String, String> CustomEncryptionContext
    ) {
      this.CustomEncryptionContext = CustomEncryptionContext;
      return this;
    }

    public Map<String, String> CustomEncryptionContext() {
      return this.CustomEncryptionContext;
    }

    public MutableBranchKeyProperties build() {
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      if (Objects.isNull(this.CustomEncryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CustomEncryptionContext`"
        );
      }
      return new MutableBranchKeyProperties(this);
    }
  }
}
