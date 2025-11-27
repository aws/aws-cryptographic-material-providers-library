// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Map;
import java.util.Objects;

public class BranchKeyMaterials {

  private final String branchKeyIdentifier;

  private final String branchKeyVersion;

  private final Map<String, String> encryptionContext;

  private final ByteBuffer branchKey;

  /**
   * The AWS KMS Key ARN used to protect this Branch Key.
   */
  private final String kmsArn;

  /**
   * Timestamp in ISO 8601 format in UTC, to microsecond precision, that this Branch Key Item's Material was generated.
   */
  private final String createTime;

  /**
   * Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.
   */
  private final HierarchyVersion hierarchyVersion;

  protected BranchKeyMaterials(BuilderImpl builder) {
    this.branchKeyIdentifier = builder.branchKeyIdentifier();
    this.branchKeyVersion = builder.branchKeyVersion();
    this.encryptionContext = builder.encryptionContext();
    this.branchKey = builder.branchKey();
    this.kmsArn = builder.kmsArn();
    this.createTime = builder.createTime();
    this.hierarchyVersion = builder.hierarchyVersion();
  }

  public String branchKeyIdentifier() {
    return this.branchKeyIdentifier;
  }

  public String branchKeyVersion() {
    return this.branchKeyVersion;
  }

  public Map<String, String> encryptionContext() {
    return this.encryptionContext;
  }

  public ByteBuffer branchKey() {
    return this.branchKey;
  }

  /**
   * @return The AWS KMS Key ARN used to protect this Branch Key.
   */
  public String kmsArn() {
    return this.kmsArn;
  }

  /**
   * @return Timestamp in ISO 8601 format in UTC, to microsecond precision, that this Branch Key Item's Material was generated.
   */
  public String createTime() {
    return this.createTime;
  }

  /**
   * @return Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.
   */
  public HierarchyVersion hierarchyVersion() {
    return this.hierarchyVersion;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder branchKeyIdentifier(String branchKeyIdentifier);

    String branchKeyIdentifier();

    Builder branchKeyVersion(String branchKeyVersion);

    String branchKeyVersion();

    Builder encryptionContext(Map<String, String> encryptionContext);

    Map<String, String> encryptionContext();

    Builder branchKey(ByteBuffer branchKey);

    ByteBuffer branchKey();

    /**
     * @param kmsArn The AWS KMS Key ARN used to protect this Branch Key.
     */
    Builder kmsArn(String kmsArn);

    /**
     * @return The AWS KMS Key ARN used to protect this Branch Key.
     */
    String kmsArn();

    /**
     * @param createTime Timestamp in ISO 8601 format in UTC, to microsecond precision, that this Branch Key Item's Material was generated.
     */
    Builder createTime(String createTime);

    /**
     * @return Timestamp in ISO 8601 format in UTC, to microsecond precision, that this Branch Key Item's Material was generated.
     */
    String createTime();

    /**
     * @param hierarchyVersion Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.
     */
    Builder hierarchyVersion(HierarchyVersion hierarchyVersion);

    /**
     * @return Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.
     */
    HierarchyVersion hierarchyVersion();

    BranchKeyMaterials build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyIdentifier;

    protected String branchKeyVersion;

    protected Map<String, String> encryptionContext;

    protected ByteBuffer branchKey;

    protected String kmsArn;

    protected String createTime;

    protected HierarchyVersion hierarchyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(BranchKeyMaterials model) {
      this.branchKeyIdentifier = model.branchKeyIdentifier();
      this.branchKeyVersion = model.branchKeyVersion();
      this.encryptionContext = model.encryptionContext();
      this.branchKey = model.branchKey();
      this.kmsArn = model.kmsArn();
      this.createTime = model.createTime();
      this.hierarchyVersion = model.hierarchyVersion();
    }

    public Builder branchKeyIdentifier(String branchKeyIdentifier) {
      this.branchKeyIdentifier = branchKeyIdentifier;
      return this;
    }

    public String branchKeyIdentifier() {
      return this.branchKeyIdentifier;
    }

    public Builder branchKeyVersion(String branchKeyVersion) {
      this.branchKeyVersion = branchKeyVersion;
      return this;
    }

    public String branchKeyVersion() {
      return this.branchKeyVersion;
    }

    public Builder encryptionContext(Map<String, String> encryptionContext) {
      this.encryptionContext = encryptionContext;
      return this;
    }

    public Map<String, String> encryptionContext() {
      return this.encryptionContext;
    }

    public Builder branchKey(ByteBuffer branchKey) {
      this.branchKey = branchKey;
      return this;
    }

    public ByteBuffer branchKey() {
      return this.branchKey;
    }

    public Builder kmsArn(String kmsArn) {
      this.kmsArn = kmsArn;
      return this;
    }

    public String kmsArn() {
      return this.kmsArn;
    }

    public Builder createTime(String createTime) {
      this.createTime = createTime;
      return this;
    }

    public String createTime() {
      return this.createTime;
    }

    public Builder hierarchyVersion(HierarchyVersion hierarchyVersion) {
      this.hierarchyVersion = hierarchyVersion;
      return this;
    }

    public HierarchyVersion hierarchyVersion() {
      return this.hierarchyVersion;
    }

    public BranchKeyMaterials build() {
      if (Objects.isNull(this.branchKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.branchKeyVersion())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKeyVersion`"
        );
      }
      if (Objects.isNull(this.encryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `encryptionContext`"
        );
      }
      if (Objects.isNull(this.branchKey())) {
        throw new IllegalArgumentException(
          "Missing value for required field `branchKey`"
        );
      }
      if (Objects.isNull(this.kmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `kmsArn`"
        );
      }
      if (Objects.nonNull(this.kmsArn()) && this.kmsArn().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `kmsArn` must be greater than or equal to 1"
        );
      }
      if (Objects.nonNull(this.kmsArn()) && this.kmsArn().length() > 2048) {
        throw new IllegalArgumentException(
          "The size of `kmsArn` must be less than or equal to 2048"
        );
      }
      if (Objects.isNull(this.createTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `createTime`"
        );
      }
      if (Objects.isNull(this.hierarchyVersion())) {
        throw new IllegalArgumentException(
          "Missing value for required field `hierarchyVersion`"
        );
      }
      return new BranchKeyMaterials(this);
    }
  }
}
