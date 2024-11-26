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
 * As of v1.9.0, a Mutation can either:
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
  private final String TerminalKmsArn;

  /**
   * ReEncrypt all Items of the Branch Key
   *   to be authorized with this custom encryption context.
   *   An empty Encryption Context is not allowed.
   */
  private final Map<String, String> TerminalEncryptionContext;

  protected Mutations(BuilderImpl builder) {
    this.TerminalKmsArn = builder.TerminalKmsArn();
    this.TerminalEncryptionContext = builder.TerminalEncryptionContext();
  }

  /**
   * @return ReEncrypt all Items of the Branch Key
   *   to be authorized by this
   *   AWS Key Management Service Key.
   *   A Multi-Region or Single Region AWS KMS Key are permitted,
   *   but not aliases!
   */
  public String TerminalKmsArn() {
    return this.TerminalKmsArn;
  }

  /**
   * @return ReEncrypt all Items of the Branch Key
   *   to be authorized with this custom encryption context.
   *   An empty Encryption Context is not allowed.
   */
  public Map<String, String> TerminalEncryptionContext() {
    return this.TerminalEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param TerminalKmsArn ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    Builder TerminalKmsArn(String TerminalKmsArn);

    /**
     * @return ReEncrypt all Items of the Branch Key
     *   to be authorized by this
     *   AWS Key Management Service Key.
     *   A Multi-Region or Single Region AWS KMS Key are permitted,
     *   but not aliases!
     */
    String TerminalKmsArn();

    /**
     * @param TerminalEncryptionContext ReEncrypt all Items of the Branch Key
     *   to be authorized with this custom encryption context.
     *   An empty Encryption Context is not allowed.
     */
    Builder TerminalEncryptionContext(
      Map<String, String> TerminalEncryptionContext
    );

    /**
     * @return ReEncrypt all Items of the Branch Key
     *   to be authorized with this custom encryption context.
     *   An empty Encryption Context is not allowed.
     */
    Map<String, String> TerminalEncryptionContext();

    Mutations build();
  }

  static class BuilderImpl implements Builder {

    protected String TerminalKmsArn;

    protected Map<String, String> TerminalEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(Mutations model) {
      this.TerminalKmsArn = model.TerminalKmsArn();
      this.TerminalEncryptionContext = model.TerminalEncryptionContext();
    }

    public Builder TerminalKmsArn(String TerminalKmsArn) {
      this.TerminalKmsArn = TerminalKmsArn;
      return this;
    }

    public String TerminalKmsArn() {
      return this.TerminalKmsArn;
    }

    public Builder TerminalEncryptionContext(
      Map<String, String> TerminalEncryptionContext
    ) {
      this.TerminalEncryptionContext = TerminalEncryptionContext;
      return this;
    }

    public Map<String, String> TerminalEncryptionContext() {
      return this.TerminalEncryptionContext;
    }

    public Mutations build() {
      return new Mutations(this);
    }
  }
}
