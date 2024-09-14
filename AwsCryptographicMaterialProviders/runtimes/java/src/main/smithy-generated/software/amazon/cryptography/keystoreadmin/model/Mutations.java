// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Map;

/**
 *
 * Define the Mutation in terms of the final, or end state, value for a particular Branch Key attribute.
 * The original value will be REPLACED with this value.
 * As of v1.7.0, a Mutation can either:
 * - replace the KmsArn
 * - replace the custom encryption context
 * - replace both the KmsArn and the custom encryption context
 */
public class Mutations {

  /**
   * ReEncrypt all Items of the Branch Key to be authorized by this AWS Key Management Service Key. A Multi-Region or Single Region AWS KMS Key are permitted, but not aliases!
   */
  private final String finalKmsArn;

  /**
   * ReEncrypt all Items of the Branch Key to be authorized with this custom encryption context. An empty Encyrption Context is not allowed.
   */
  private final Map<String, String> finalEncryptionContext;

  protected Mutations(BuilderImpl builder) {
    this.finalKmsArn = builder.finalKmsArn();
    this.finalEncryptionContext = builder.finalEncryptionContext();
  }

  /**
   * @return ReEncrypt all Items of the Branch Key to be authorized by this AWS Key Management Service Key. A Multi-Region or Single Region AWS KMS Key are permitted, but not aliases!
   */
  public String finalKmsArn() {
    return this.finalKmsArn;
  }

  /**
   * @return ReEncrypt all Items of the Branch Key to be authorized with this custom encryption context. An empty Encyrption Context is not allowed.
   */
  public Map<String, String> finalEncryptionContext() {
    return this.finalEncryptionContext;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param finalKmsArn ReEncrypt all Items of the Branch Key to be authorized by this AWS Key Management Service Key. A Multi-Region or Single Region AWS KMS Key are permitted, but not aliases!
     */
    Builder finalKmsArn(String finalKmsArn);

    /**
     * @return ReEncrypt all Items of the Branch Key to be authorized by this AWS Key Management Service Key. A Multi-Region or Single Region AWS KMS Key are permitted, but not aliases!
     */
    String finalKmsArn();

    /**
     * @param finalEncryptionContext ReEncrypt all Items of the Branch Key to be authorized with this custom encryption context. An empty Encyrption Context is not allowed.
     */
    Builder finalEncryptionContext(Map<String, String> finalEncryptionContext);

    /**
     * @return ReEncrypt all Items of the Branch Key to be authorized with this custom encryption context. An empty Encyrption Context is not allowed.
     */
    Map<String, String> finalEncryptionContext();

    Mutations build();
  }

  static class BuilderImpl implements Builder {

    protected String finalKmsArn;

    protected Map<String, String> finalEncryptionContext;

    protected BuilderImpl() {}

    protected BuilderImpl(Mutations model) {
      this.finalKmsArn = model.finalKmsArn();
      this.finalEncryptionContext = model.finalEncryptionContext();
    }

    public Builder finalKmsArn(String finalKmsArn) {
      this.finalKmsArn = finalKmsArn;
      return this;
    }

    public String finalKmsArn() {
      return this.finalKmsArn;
    }

    public Builder finalEncryptionContext(
      Map<String, String> finalEncryptionContext
    ) {
      this.finalEncryptionContext = finalEncryptionContext;
      return this;
    }

    public Map<String, String> finalEncryptionContext() {
      return this.finalEncryptionContext;
    }

    public Mutations build() {
      return new Mutations(this);
    }
  }
}
