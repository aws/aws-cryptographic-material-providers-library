// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystoreadmin.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class VersionKeyInput {

  /**
   * The identifier for the Branch Key to be versioned.
   */
  private final String Identifier;

  /**
   * Multi-Region or Single Region AWS KMS Key ARN used to protect the Branch Key, but not aliases!
   */
  private final KmsSymmetricKeyArn KmsArn;

  /**
   * For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or AwsKmsSimple are supported (for now).
   *   For 'hierarchy-version-2' (HV-2), only AwsKmsDecryptEncrypt or AwsKmsSimple are supported.
   */
  private final KeyManagementStrategy Strategy;

  /**
   * The hierarchy-version of a Branch Key;
   *   all items of the same Branch Key SHOULD
   *   have the same hierarchy-version.
   *   The hierarchy-version determines how the Branch Key Store
   *   protects and validates the branch key context (BKC).
   */
  private final HierarchyVersion HierarchyVersion;

  protected VersionKeyInput(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.KmsArn = builder.KmsArn();
    this.Strategy = builder.Strategy();
    this.HierarchyVersion = builder.HierarchyVersion();
  }

  /**
   * @return The identifier for the Branch Key to be versioned.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return Multi-Region or Single Region AWS KMS Key ARN used to protect the Branch Key, but not aliases!
   */
  public KmsSymmetricKeyArn KmsArn() {
    return this.KmsArn;
  }

  /**
   * @return For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or AwsKmsSimple are supported (for now).
   *   For 'hierarchy-version-2' (HV-2), only AwsKmsDecryptEncrypt or AwsKmsSimple are supported.
   */
  public KeyManagementStrategy Strategy() {
    return this.Strategy;
  }

  /**
   * @return The hierarchy-version of a Branch Key;
   *   all items of the same Branch Key SHOULD
   *   have the same hierarchy-version.
   *   The hierarchy-version determines how the Branch Key Store
   *   protects and validates the branch key context (BKC).
   */
  public HierarchyVersion HierarchyVersion() {
    return this.HierarchyVersion;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The identifier for the Branch Key to be versioned.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The identifier for the Branch Key to be versioned.
     */
    String Identifier();

    /**
     * @param KmsArn Multi-Region or Single Region AWS KMS Key ARN used to protect the Branch Key, but not aliases!
     */
    Builder KmsArn(KmsSymmetricKeyArn KmsArn);

    /**
     * @return Multi-Region or Single Region AWS KMS Key ARN used to protect the Branch Key, but not aliases!
     */
    KmsSymmetricKeyArn KmsArn();

    /**
     * @param Strategy For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or AwsKmsSimple are supported (for now).
     *   For 'hierarchy-version-2' (HV-2), only AwsKmsDecryptEncrypt or AwsKmsSimple are supported.
     */
    Builder Strategy(KeyManagementStrategy Strategy);

    /**
     * @return For 'hierarchy-version-1' (HV-1), only AwsKmsReEncrypt or AwsKmsSimple are supported (for now).
     *   For 'hierarchy-version-2' (HV-2), only AwsKmsDecryptEncrypt or AwsKmsSimple are supported.
     */
    KeyManagementStrategy Strategy();

    /**
     * @param HierarchyVersion The hierarchy-version of a Branch Key;
     *   all items of the same Branch Key SHOULD
     *   have the same hierarchy-version.
     *   The hierarchy-version determines how the Branch Key Store
     *   protects and validates the branch key context (BKC).
     */
    Builder HierarchyVersion(HierarchyVersion HierarchyVersion);

    /**
     * @return The hierarchy-version of a Branch Key;
     *   all items of the same Branch Key SHOULD
     *   have the same hierarchy-version.
     *   The hierarchy-version determines how the Branch Key Store
     *   protects and validates the branch key context (BKC).
     */
    HierarchyVersion HierarchyVersion();

    VersionKeyInput build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected KmsSymmetricKeyArn KmsArn;

    protected KeyManagementStrategy Strategy;

    protected HierarchyVersion HierarchyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(VersionKeyInput model) {
      this.Identifier = model.Identifier();
      this.KmsArn = model.KmsArn();
      this.Strategy = model.Strategy();
      this.HierarchyVersion = model.HierarchyVersion();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder KmsArn(KmsSymmetricKeyArn KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public KmsSymmetricKeyArn KmsArn() {
      return this.KmsArn;
    }

    public Builder Strategy(KeyManagementStrategy Strategy) {
      this.Strategy = Strategy;
      return this;
    }

    public KeyManagementStrategy Strategy() {
      return this.Strategy;
    }

    public Builder HierarchyVersion(HierarchyVersion HierarchyVersion) {
      this.HierarchyVersion = HierarchyVersion;
      return this;
    }

    public HierarchyVersion HierarchyVersion() {
      return this.HierarchyVersion;
    }

    public VersionKeyInput build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      return new VersionKeyInput(this);
    }
  }
}
