// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.nio.ByteBuffer;
import java.util.Map;
import java.util.Objects;

public class EncryptedHierarchicalKey {

  private final String Identifier;

  private final BranchKeyType Type;

  private final String CreateTime;

  private final String KmsArn;

  private final Map<String, String> EncryptionContext;

  private final ByteBuffer CiphertextBlob;

  protected EncryptedHierarchicalKey(BuilderImpl builder) {
    this.Identifier = builder.Identifier();
    this.Type = builder.Type();
    this.CreateTime = builder.CreateTime();
    this.KmsArn = builder.KmsArn();
    this.EncryptionContext = builder.EncryptionContext();
    this.CiphertextBlob = builder.CiphertextBlob();
  }

  public String Identifier() {
    return this.Identifier;
  }

  public BranchKeyType Type() {
    return this.Type;
  }

  public String CreateTime() {
    return this.CreateTime;
  }

  public String KmsArn() {
    return this.KmsArn;
  }

  public Map<String, String> EncryptionContext() {
    return this.EncryptionContext;
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
    Builder Identifier(String Identifier);

    String Identifier();

    Builder Type(BranchKeyType Type);

    BranchKeyType Type();

    Builder CreateTime(String CreateTime);

    String CreateTime();

    Builder KmsArn(String KmsArn);

    String KmsArn();

    Builder EncryptionContext(Map<String, String> EncryptionContext);

    Map<String, String> EncryptionContext();

    Builder CiphertextBlob(ByteBuffer CiphertextBlob);

    ByteBuffer CiphertextBlob();

    EncryptedHierarchicalKey build();
  }

  static class BuilderImpl implements Builder {

    protected String Identifier;

    protected BranchKeyType Type;

    protected String CreateTime;

    protected String KmsArn;

    protected Map<String, String> EncryptionContext;

    protected ByteBuffer CiphertextBlob;

    protected BuilderImpl() {}

    protected BuilderImpl(EncryptedHierarchicalKey model) {
      this.Identifier = model.Identifier();
      this.Type = model.Type();
      this.CreateTime = model.CreateTime();
      this.KmsArn = model.KmsArn();
      this.EncryptionContext = model.EncryptionContext();
      this.CiphertextBlob = model.CiphertextBlob();
    }

    public Builder Identifier(String Identifier) {
      this.Identifier = Identifier;
      return this;
    }

    public String Identifier() {
      return this.Identifier;
    }

    public Builder Type(BranchKeyType Type) {
      this.Type = Type;
      return this;
    }

    public BranchKeyType Type() {
      return this.Type;
    }

    public Builder CreateTime(String CreateTime) {
      this.CreateTime = CreateTime;
      return this;
    }

    public String CreateTime() {
      return this.CreateTime;
    }

    public Builder KmsArn(String KmsArn) {
      this.KmsArn = KmsArn;
      return this;
    }

    public String KmsArn() {
      return this.KmsArn;
    }

    public Builder EncryptionContext(Map<String, String> EncryptionContext) {
      this.EncryptionContext = EncryptionContext;
      return this;
    }

    public Map<String, String> EncryptionContext() {
      return this.EncryptionContext;
    }

    public Builder CiphertextBlob(ByteBuffer CiphertextBlob) {
      this.CiphertextBlob = CiphertextBlob;
      return this;
    }

    public ByteBuffer CiphertextBlob() {
      return this.CiphertextBlob;
    }

    public EncryptedHierarchicalKey build() {
      if (Objects.isNull(this.Identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Identifier`"
        );
      }
      if (Objects.isNull(this.Type())) {
        throw new IllegalArgumentException(
          "Missing value for required field `Type`"
        );
      }
      if (Objects.isNull(this.CreateTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CreateTime`"
        );
      }
      if (Objects.isNull(this.KmsArn())) {
        throw new IllegalArgumentException(
          "Missing value for required field `KmsArn`"
        );
      }
      if (Objects.isNull(this.EncryptionContext())) {
        throw new IllegalArgumentException(
          "Missing value for required field `EncryptionContext`"
        );
      }
      if (Objects.isNull(this.CiphertextBlob())) {
        throw new IllegalArgumentException(
          "Missing value for required field `CiphertextBlob`"
        );
      }
      return new EncryptedHierarchicalKey(this);
    }
  }
}
