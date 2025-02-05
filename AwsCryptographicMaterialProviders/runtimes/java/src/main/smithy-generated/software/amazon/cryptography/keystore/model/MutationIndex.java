// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Objects;

/**
 * Information of an in-flight Mutation of a Branch Key.
 */
public class MutationIndex {

  /**
   * The Branch Key under Mutation.
   */
  private final String Identifier;

  /**
   * The create time as an ISO 8061 UTC string.
   */
  private final String CreateTime;

  /**
   * A unique identifier for the Mutation.
   */
  private final String UUID;

  private final ByteBuffer PageIndex;

  private final String LastModifiedTime;

  private final ByteBuffer CiphertextBlob;

  protected MutationIndex(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.CreateTime = builder.CreateTime();
    this.UUID = builder.UUID();
    this.PageIndex = builder.PageIndex();
    this.LastModifiedTime = builder.LastModifiedTime();
    this.CiphertextBlob = builder.CiphertextBlob();
  }

  /**
   * @return The Branch Key under Mutation.
   */
  public String Identifier() {
    return this.Identifier;
  }

  /**
   * @return The create time as an ISO 8061 UTC string.
   */
  public String CreateTime() {
    return this.CreateTime;
  }

  /**
   * @return A unique identifier for the Mutation.
   */
  public String UUID() {
    return this.UUID;
  }

  public ByteBuffer PageIndex() {
    return this.PageIndex;
  }

  public String LastModifiedTime() {
    return this.LastModifiedTime;
  }

  public ByteBuffer CiphertextBlob() {
    return this.CiphertextBlob;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Identifier The Branch Key under Mutation.
     */
    Builder Identifier(String Identifier);

    /**
     * @return The Branch Key under Mutation.
     */
    String Identifier();

    /**
     * @param CreateTime The create time as an ISO 8061 UTC string.
     */
    Builder CreateTime(String CreateTime);

    /**
     * @return The create time as an ISO 8061 UTC string.
     */
    String CreateTime();

    /**
     * @param UUID A unique identifier for the Mutation.
     */
    Builder UUID(String UUID);

    /**
     * @return A unique identifier for the Mutation.
     */
    String UUID();

    Builder PageIndex(ByteBuffer PageIndex);

    ByteBuffer PageIndex();

    Builder LastModifiedTime(String LastModifiedTime);

    String LastModifiedTime();

    Builder CiphertextBlob(ByteBuffer CiphertextBlob);

    ByteBuffer CiphertextBlob();

    MutationIndex build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected String CreateTime;

    protected String UUID;

    protected ByteBuffer PageIndex;

    protected String LastModifiedTime;

    protected ByteBuffer CiphertextBlob;

    protected BuilderImpl() {}

    protected BuilderImpl(MutationIndex model) {
      this.Identifier = model.Identifier();
      this.CreateTime = model.CreateTime();
      this.UUID = model.UUID();
      this.PageIndex = model.PageIndex();
      this.LastModifiedTime = model.LastModifiedTime();
      this.CiphertextBlob = model.CiphertextBlob();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public Builder UUID(String UUID) {
      this.UUID = UUID;
      return this;
    }

    public String UUID() {
      return this.UUID;
    }

    public Builder PageIndex(ByteBuffer PageIndex) {
      this.PageIndex = PageIndex;
      return this;
    }

    public ByteBuffer PageIndex() {
      return this.PageIndex;
    }

    public Builder LastModifiedTime(String LastModifiedTime) {
      this.LastModifiedTime = LastModifiedTime;
      return this;
    }

    public String LastModifiedTime() {
      return this.LastModifiedTime;
    }

    public Builder CiphertextBlob(ByteBuffer CiphertextBlob) {
      this.CiphertextBlob = CiphertextBlob;
      return this;
    }

    public ByteBuffer CiphertextBlob() {
      return this.CiphertextBlob;
    }

    public MutationIndex build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      if (Objects.isNull(this.UUID())) {
        throw new IllegalArgumentException(
          "Missing value for required field `UUID`"
        );
      }
      if (Objects.isNull(this.PageIndex())) {
        throw new IllegalArgumentException(
          "Missing value for required field `PageIndex`"
        );
      }
      if (Objects.isNull(this.LastModifiedTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `LastModifiedTime`"
        );
      }
      if (Objects.isNull(this.CiphertextBlob())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CiphertextBlob`"
        );
      }
      return new MutationIndex(this);
    }
  }
}
