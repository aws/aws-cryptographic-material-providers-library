// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Map;
import java.util.Objects;

public class BeaconKeyMaterials {

  private final String beaconKeyIdentifier;

  private final Map<String, String> encryptionContext;

  private final ByteBuffer beaconKey;

  private final Map<String, ByteBuffer> hmacKeys;

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

  protected BeaconKeyMaterials(BuilderImpl builder) {
    this.beaconKeyIdentifier = builder.beaconKeyIdentifier();
    this.encryptionContext = builder.encryptionContext();
    this.beaconKey = builder.beaconKey();
    this.hmacKeys = builder.hmacKeys();
    this.kmsArn = builder.kmsArn();
    this.createTime = builder.createTime();
    this.hierarchyVersion = builder.hierarchyVersion();
  }

  public String beaconKeyIdentifier() {
    return this.beaconKeyIdentifier;
  }

  public Map<String, String> encryptionContext() {
    return this.encryptionContext;
  }

  public ByteBuffer beaconKey() {
    return this.beaconKey;
  }

  public Map<String, ByteBuffer> hmacKeys() {
    return this.hmacKeys;
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
    Builder beaconKeyIdentifier(String beaconKeyIdentifier);

    String beaconKeyIdentifier();

    Builder encryptionContext(Map<String, String> encryptionContext);

    Map<String, String> encryptionContext();

    Builder beaconKey(ByteBuffer beaconKey);

    ByteBuffer beaconKey();

    Builder hmacKeys(Map<String, ByteBuffer> hmacKeys);

    Map<String, ByteBuffer> hmacKeys();

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

    BeaconKeyMaterials build();
  }

  static class BuilderImpl implements Builder {

    protected String beaconKeyIdentifier;

    protected Map<String, String> encryptionContext;

    protected ByteBuffer beaconKey;

    protected Map<String, ByteBuffer> hmacKeys;

    protected String kmsArn;

    protected String createTime;

    protected HierarchyVersion hierarchyVersion;

    protected BuilderImpl() {}

    protected BuilderImpl(BeaconKeyMaterials model) {
      this.beaconKeyIdentifier = model.beaconKeyIdentifier();
      this.encryptionContext = model.encryptionContext();
      this.beaconKey = model.beaconKey();
      this.hmacKeys = model.hmacKeys();
      this.kmsArn = model.kmsArn();
      this.createTime = model.createTime();
      this.hierarchyVersion = model.hierarchyVersion();
    }

    public Builder beaconKeyIdentifier(String beaconKeyIdentifier) {
      this.beaconKeyIdentifier = beaconKeyIdentifier;
      return this;
    }

    public String beaconKeyIdentifier() {
      return this.beaconKeyIdentifier;
    }

    public Builder encryptionContext(Map<String, String> encryptionContext) {
      this.encryptionContext = encryptionContext;
      return this;
    }

    public Map<String, String> encryptionContext() {
      return this.encryptionContext;
    }

    public Builder beaconKey(ByteBuffer beaconKey) {
      this.beaconKey = beaconKey;
      return this;
    }

    public ByteBuffer beaconKey() {
      return this.beaconKey;
    }

    public Builder hmacKeys(Map<String, ByteBuffer> hmacKeys) {
      this.hmacKeys = hmacKeys;
      return this;
    }

    public Map<String, ByteBuffer> hmacKeys() {
      return this.hmacKeys;
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

    public BeaconKeyMaterials build() {
      if (Objects.isNull(this.beaconKeyIdentifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `beaconKeyIdentifier`"
        );
      }
      if (Objects.isNull(this.encryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `encryptionContext`"
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
      return new BeaconKeyMaterials(this);
    }
  }
}
