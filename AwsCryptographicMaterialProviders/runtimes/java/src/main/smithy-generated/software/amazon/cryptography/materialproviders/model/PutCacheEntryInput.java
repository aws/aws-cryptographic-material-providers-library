// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class PutCacheEntryInput {

  private final ByteBuffer identifier;

  private final Materials materials;

  private final Long creationTime;

  private final Long expiryTime;

  private final Integer messagesUsed;

  private final Integer bytesUsed;

  protected PutCacheEntryInput(BuilderImpl builder) {
    this.identifier = builder.identifier();
    this.materials = builder.materials();
    this.creationTime = builder.creationTime();
    this.expiryTime = builder.expiryTime();
    this.messagesUsed = builder.messagesUsed();
    this.bytesUsed = builder.bytesUsed();
  }

  public ByteBuffer identifier() {
    return this.identifier;
  }

  public Materials materials() {
    return this.materials;
  }

  public Long creationTime() {
    return this.creationTime;
  }

  public Long expiryTime() {
    return this.expiryTime;
  }

  public Integer messagesUsed() {
    return this.messagesUsed;
  }

  public Integer bytesUsed() {
    return this.bytesUsed;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder identifier(ByteBuffer identifier);

    ByteBuffer identifier();

    Builder materials(Materials materials);

    Materials materials();

    Builder creationTime(Long creationTime);

    Long creationTime();

    Builder expiryTime(Long expiryTime);

    Long expiryTime();

    Builder messagesUsed(Integer messagesUsed);

    Integer messagesUsed();

    Builder bytesUsed(Integer bytesUsed);

    Integer bytesUsed();

    PutCacheEntryInput build();
  }

  static class BuilderImpl implements Builder {

    protected ByteBuffer identifier;

    protected Materials materials;

    protected Long creationTime;

    protected Long expiryTime;

    protected Integer messagesUsed;

    protected Integer bytesUsed;

    protected BuilderImpl() {}

    protected BuilderImpl(PutCacheEntryInput model) {
      this.identifier = model.identifier();
      this.materials = model.materials();
      this.creationTime = model.creationTime();
      this.expiryTime = model.expiryTime();
      this.messagesUsed = model.messagesUsed();
      this.bytesUsed = model.bytesUsed();
    }

    public Builder identifier(ByteBuffer identifier) {
      this.identifier = identifier;
      return this;
    }

    public ByteBuffer identifier() {
      return this.identifier;
    }

    public Builder materials(Materials materials) {
      this.materials = materials;
      return this;
    }

    public Materials materials() {
      return this.materials;
    }

    public Builder creationTime(Long creationTime) {
      this.creationTime = creationTime;
      return this;
    }

    public Long creationTime() {
      return this.creationTime;
    }

    public Builder expiryTime(Long expiryTime) {
      this.expiryTime = expiryTime;
      return this;
    }

    public Long expiryTime() {
      return this.expiryTime;
    }

    public Builder messagesUsed(Integer messagesUsed) {
      this.messagesUsed = messagesUsed;
      return this;
    }

    public Integer messagesUsed() {
      return this.messagesUsed;
    }

    public Builder bytesUsed(Integer bytesUsed) {
      this.bytesUsed = bytesUsed;
      return this;
    }

    public Integer bytesUsed() {
      return this.bytesUsed;
    }

    public PutCacheEntryInput build() {
      if (Objects.isNull(this.identifier())) {
        throw new IllegalArgumentException(
          "Missing value for required field `identifier`"
        );
      }
      if (Objects.isNull(this.materials())) {
        throw new IllegalArgumentException(
          "Missing value for required field `materials`"
        );
      }
      if (Objects.isNull(this.creationTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `creationTime`"
        );
      }
      if (Objects.nonNull(this.creationTime()) && this.creationTime() < 0) {
        throw new IllegalArgumentException(
          "`creationTime` must be greater than or equal to 0"
        );
      }
      if (Objects.isNull(this.expiryTime())) {
        throw new IllegalArgumentException(
          "Missing value for required field `expiryTime`"
        );
      }
      if (Objects.nonNull(this.expiryTime()) && this.expiryTime() < 0) {
        throw new IllegalArgumentException(
          "`expiryTime` must be greater than or equal to 0"
        );
      }
      if (Objects.nonNull(this.messagesUsed()) && this.messagesUsed() < 0) {
        throw new IllegalArgumentException(
          "`messagesUsed` must be greater than or equal to 0"
        );
      }
      if (Objects.nonNull(this.bytesUsed()) && this.bytesUsed() < 0) {
        throw new IllegalArgumentException(
          "`bytesUsed` must be greater than or equal to 0"
        );
      }
      return new PutCacheEntryInput(this);
    }
  }
}
