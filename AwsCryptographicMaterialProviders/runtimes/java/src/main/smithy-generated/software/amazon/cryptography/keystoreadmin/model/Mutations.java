// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;

/**
 *
 * Define the Mutation in terms of the terminal, or end state,
 * value for a particular Branch Key property.
 * The original value will be REPLACED with this value.
 * As of v1.7.0, a Mutation can either:
 * - replace the KmsArn protecting the Branch Key
 * - replace the custom encryption context
 * - replace both the KmsArn and the custom encryption context
 */
public class Mutations {

  /**
   * ReEncrypt all Items of the Branch Key
   *   to be authorized by this
   *   AWS Key Management Service Key.
   *   A Multi-Region or Single Region AWS KMS Key are permitted,
   *   but not aliases!
   */
  private final String terminalKmsArn;

  /**
   * ReEncrypt all Items of the Branch Key
   *   to be authorized with this custom encryption context.
   *   An empty Encyrption Context is not allowed.
   */
  private final Map<String, String> terminalEncryptionContext;

  protected Mutations(BuilderImpl builder) {
    this.terminalKmsArn = builder.terminalKmsArn();
    this.terminalEncryptionContext = builder.terminalEncryptionContext();
  }

  /**
   * @return ReEncrypt all Items of the Branch Key
   *   to be authorized by this
   *   AWS Key Management Service Key.
   *   A Multi-Region or Single Region AWS KMS Key are permitted,
   *   but not aliases!
   */
  public String terminalKmsArn() {
    return this.terminalKmsArn;
  }

  /**
   * @return ReEncrypt all Items of the Branch Key
   *   to be authorized with this custom encryption context.
   *   An empty Encyrption Context is not allowed.
   */
  public Map<String, String> terminalEncryptionContext() {
    return this.terminalEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param terminalKmsArn ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    Builder terminalKmsArn(String terminalKmsArn);

    /**
     * @return ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    String terminalKmsArn();

    /**
     * @param terminalEncryptionContext ReEncrypt all Items of the Branch Key
     *   to be authorized with this custom encryption context.
     *   An empty Encyrption Context is not allowed.
     */
    Builder terminalEncryptionContext(
      Map<String, String> terminalEncryptionContext
    );

    /**
     * @return ReEncrypt all Items of the Branch Key
     *   to be authorized with this custom encryption context.
     *   An empty Encyrption Context is not allowed.
     */
    Map<String, String> terminalEncryptionContext();

    Mutations build();
  }

  static class BuilderImpl implements Builder {

    protected String terminalKmsArn;

    protected Map<String, String> terminalEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(Mutations model) {
      this.terminalKmsArn = model.terminalKmsArn();
      this.terminalEncryptionContext = model.terminalEncryptionContext();
    }

    public Builder terminalKmsArn(String terminalKmsArn) {
      this.terminalKmsArn = terminalKmsArn;
      return this;
    }

    public String terminalKmsArn() {
      return this.terminalKmsArn;
    }

    public Builder terminalEncryptionContext(
      Map<String, String> terminalEncryptionContext
    ) {
      this.terminalEncryptionContext = terminalEncryptionContext;
      return this;
    }

    public Map<String, String> terminalEncryptionContext() {
      return this.terminalEncryptionContext;
    }

    public Mutations build() {
      return new Mutations(this);
    }
  }
}
