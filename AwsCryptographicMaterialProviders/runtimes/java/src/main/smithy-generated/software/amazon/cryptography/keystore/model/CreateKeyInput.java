// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.List;
import java.util.Map;
import java.util.Objects;

public class CreateKeyInput {

  /**
   * The identifier for the created Branch Key.
   */
  private final String branchKeyIdentifier;

  /**
   * Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
   */
  private final Map<String, String> encryptionContext;

  /**
   * KMS Key ARN to protect this Branch Key. Required if Key Store's kmsConfiguration is Discovery.
   */
  private final String arn;

  /**
   * A List of Grant Tokens to include in KMS requests for Branch Key Creation. This augments the list on the Key Store.
   */
  private final List<String> grantTokens;

  protected CreateKeyInput(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.encryptionContext = builder.encryptionContext();
    this.arn = builder.arn();
    this.grantTokens = builder.grantTokens();
  }

  /**
   * @return The identifier for the created Branch Key.
   */
  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  /**
   * @return Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
   */
  public Map<String, String> encryptionContext() {
    return this.encryptionContext;
  }

  /**
   * @return KMS Key ARN to protect this Branch Key. Required if Key Store's kmsConfiguration is Discovery.
   */
  public String arn() {
    return this.arn;
  }

  /**
   * @return A List of Grant Tokens to include in KMS requests for Branch Key Creation. This augments the list on the Key Store.
   */
  public List<String> grantTokens() {
    return this.grantTokens;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyIdentifier The identifier for the created Branch Key.
     */
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    /**
     * @return The identifier for the created Branch Key.
     */
    String branchKeyIdentifier();

    /**
     * @param encryptionContext Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
     */
    Builder encryptionContext(Map<String, String> encryptionContext);

    /**
     * @return Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.
     */
    Map<String, String> encryptionContext();

    /**
     * @param arn KMS Key ARN to protect this Branch Key. Required if Key Store's kmsConfiguration is Discovery.
     */
    Builder arn(String arn);

    /**
     * @return KMS Key ARN to protect this Branch Key. Required if Key Store's kmsConfiguration is Discovery.
     */
    String arn();

    /**
     * @param grantTokens A List of Grant Tokens to include in KMS requests for Branch Key Creation. This augments the list on the Key Store.
     */
    Builder grantTokens(List<String> grantTokens);

    /**
     * @return A List of Grant Tokens to include in KMS requests for Branch Key Creation. This augments the list on the Key Store.
     */
    List<String> grantTokens();

    CreateKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected Map<String, String> encryptionContext;

    protected String arn;

    protected List<String> grantTokens;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateKeyInput model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.encryptionContext = model.encryptionContext();
      this.arn = model.arn();
      this.grantTokens = model.grantTokens();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder encryptionContext(Map<String, String> encryptionContext) {
      this.encryptionContext = encryptionContext;
      return this;
    }

    public Map<String, String> encryptionContext() {
      return this.encryptionContext;
    }

    public Builder arn(String arn) {
      this.arn = arn;
      return this;
    }

    public String arn() {
      return this.arn;
    }

    public Builder grantTokens(List<String> grantTokens) {
      this.grantTokens = grantTokens;
      return this;
    }

    public List<String> grantTokens() {
      return this.grantTokens;
    }

    public CreateKeyInput build() {
      if (Objects.nonNull(this.arn()) && this.arn().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `arn` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.arn()) && this.arn().length() > 2048) {
        throw new IllegalArgumentException(
          "The size of `arn` must be less than or equal to 2048"
        );
      }
      return new CreateKeyInput(this);
    }
  }
}
