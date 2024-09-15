// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;
import java.util.Objects;

/**
 *
 * Define the Mutatable Properities of a Branch Key.
 * As of v1.7.0, the Mutable Properities are:
 * - The KmsArn protecting the Branch Key
 * - The custom encryption context of a Branch Key
 */
public class MutableBranchKeyProperities {

  /**
   * The KmsArn protecting the Branch Key.
   */
  private final String kmsArn;

  /**
   * The custom Encryption Context authenicated with this Branch Key.
   */
  private final Map<String, String> customEncryptionContext;

  protected MutableBranchKeyProperities(BuilderImpl builder) {
    this.kmsArn = builder.kmsArn();
    this.customEncryptionContext = builder.customEncryptionContext();
  }

  /**
   * @return The KmsArn protecting the Branch Key.
   */
  public String kmsArn() {
    return this.kmsArn;
  }

  /**
   * @return The custom Encryption Context authenicated with this Branch Key.
   */
  public Map<String, String> customEncryptionContext() {
    return this.customEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsArn The KmsArn protecting the Branch Key.
     */
    Builder kmsArn(String kmsArn);

    /**
     * @return The KmsArn protecting the Branch Key.
     */
    String kmsArn();

    /**
     * @param customEncryptionContext The custom Encryption Context authenicated with this Branch Key.
     */
    Builder customEncryptionContext(
      Map<String, String> customEncryptionContext
    );

    /**
     * @return The custom Encryption Context authenicated with this Branch Key.
     */
    Map<String, String> customEncryptionContext();

    MutableBranchKeyProperities build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsArn;

    protected Map<String, String> customEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(MutableBranchKeyProperities model) {
      this.kmsArn = model.kmsArn();
      this.customEncryptionContext = model.customEncryptionContext();
    }

    public Builder kmsArn(String kmsArn) {
      this.kmsArn = kmsArn;
      return this;
    }

    public String kmsArn() {
      return this.kmsArn;
    }

    public Builder customEncryptionContext(
      Map<String, String> customEncryptionContext
    ) {
      this.customEncryptionContext = customEncryptionContext;
      return this;
    }

    public Map<String, String> customEncryptionContext() {
      return this.customEncryptionContext;
    }

    public MutableBranchKeyProperities build() {
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      if (Objects.isNull(this.customEncryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `customEncryptionContext`"
        );
      }
      return new MutableBranchKeyProperities(this);
    }
  }
}
