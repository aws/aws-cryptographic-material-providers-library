// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviderstestvectorkeys.model;

import java.nio.ByteBuffer;
import java.util.Objects;

public class CachingCMM {
  private final KeyDescription underlying;

  private final int cacheLimitTtlSeconds;

  private final long limitBytes;

  private final int limitMessages;

  /**
   * The entry identifier for get. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
   */
  private final ByteBuffer getEntryIdentifier;

  /**
   * The entry identifier for put. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
   */
  private final ByteBuffer putEntryIdentifier;

  protected CachingCMM(BuilderImpl builder) {
    this.underlying = builder.underlying();
    this.cacheLimitTtlSeconds = builder.cacheLimitTtlSeconds();
    this.limitBytes = builder.limitBytes();
    this.limitMessages = builder.limitMessages();
    this.getEntryIdentifier = builder.getEntryIdentifier();
    this.putEntryIdentifier = builder.putEntryIdentifier();
  }

  public KeyDescription underlying() {
    return this.underlying;
  }

  public int cacheLimitTtlSeconds() {
    return this.cacheLimitTtlSeconds;
  }

  public long limitBytes() {
    return this.limitBytes;
  }

  public int limitMessages() {
    return this.limitMessages;
  }

  /**
   * @return The entry identifier for get. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
   */
  public ByteBuffer getEntryIdentifier() {
    return this.getEntryIdentifier;
  }

  /**
   * @return The entry identifier for put. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
   */
  public ByteBuffer putEntryIdentifier() {
    return this.putEntryIdentifier;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder underlying(KeyDescription underlying);

    KeyDescription underlying();

    Builder cacheLimitTtlSeconds(int cacheLimitTtlSeconds);

    int cacheLimitTtlSeconds();

    Builder limitBytes(long limitBytes);

    long limitBytes();

    Builder limitMessages(int limitMessages);

    int limitMessages();

    /**
     * @param getEntryIdentifier The entry identifier for get. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
     */
    Builder getEntryIdentifier(ByteBuffer getEntryIdentifier);

    /**
     * @return The entry identifier for get. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
     */
    ByteBuffer getEntryIdentifier();

    /**
     * @param putEntryIdentifier The entry identifier for put. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
     */
    Builder putEntryIdentifier(ByteBuffer putEntryIdentifier);

    /**
     * @return The entry identifier for put. The cache entry values are set on creation. Use the limits on the CMM to control behavior.
     */
    ByteBuffer putEntryIdentifier();

    CachingCMM build();
  }

  static class BuilderImpl implements Builder {
    protected KeyDescription underlying;

    protected int cacheLimitTtlSeconds;

    private boolean _cacheLimitTtlSecondsSet = false;

    protected long limitBytes;

    private boolean _limitBytesSet = false;

    protected int limitMessages;

    private boolean _limitMessagesSet = false;

    protected ByteBuffer getEntryIdentifier;

    protected ByteBuffer putEntryIdentifier;

    protected BuilderImpl() {
    }

    protected BuilderImpl(CachingCMM model) {
      this.underlying = model.underlying();
      this.cacheLimitTtlSeconds = model.cacheLimitTtlSeconds();
      this._cacheLimitTtlSecondsSet = true;
      this.limitBytes = model.limitBytes();
      this._limitBytesSet = true;
      this.limitMessages = model.limitMessages();
      this._limitMessagesSet = true;
      this.getEntryIdentifier = model.getEntryIdentifier();
      this.putEntryIdentifier = model.putEntryIdentifier();
    }

    public Builder underlying(KeyDescription underlying) {
      this.underlying = underlying;
      return this;
    }

    public KeyDescription underlying() {
      return this.underlying;
    }

    public Builder cacheLimitTtlSeconds(int cacheLimitTtlSeconds) {
      this.cacheLimitTtlSeconds = cacheLimitTtlSeconds;
      this._cacheLimitTtlSecondsSet = true;
      return this;
    }

    public int cacheLimitTtlSeconds() {
      return this.cacheLimitTtlSeconds;
    }

    public Builder limitBytes(long limitBytes) {
      this.limitBytes = limitBytes;
      this._limitBytesSet = true;
      return this;
    }

    public long limitBytes() {
      return this.limitBytes;
    }

    public Builder limitMessages(int limitMessages) {
      this.limitMessages = limitMessages;
      this._limitMessagesSet = true;
      return this;
    }

    public int limitMessages() {
      return this.limitMessages;
    }

    public Builder getEntryIdentifier(ByteBuffer getEntryIdentifier) {
      this.getEntryIdentifier = getEntryIdentifier;
      return this;
    }

    public ByteBuffer getEntryIdentifier() {
      return this.getEntryIdentifier;
    }

    public Builder putEntryIdentifier(ByteBuffer putEntryIdentifier) {
      this.putEntryIdentifier = putEntryIdentifier;
      return this;
    }

    public ByteBuffer putEntryIdentifier() {
      return this.putEntryIdentifier;
    }

    public CachingCMM build() {
      if (Objects.isNull(this.underlying()))  {
        throw new IllegalArgumentException("Missing value for required field `underlying`");
      }
      if (!this._cacheLimitTtlSecondsSet) {
        throw new IllegalArgumentException("Missing value for required field `cacheLimitTtlSeconds`");
      }
      if (this._cacheLimitTtlSecondsSet && this.cacheLimitTtlSeconds() < 0) {
        throw new IllegalArgumentException("`cacheLimitTtlSeconds` must be greater than or equal to 0");
      }
      if (this._limitBytesSet && this.limitBytes() < 0) {
        throw new IllegalArgumentException("`limitBytes` must be greater than or equal to 0");
      }
      if (this._limitMessagesSet && this.limitMessages() < 0) {
        throw new IllegalArgumentException("`limitMessages` must be greater than or equal to 0");
      }
      return new CachingCMM(this);
    }
  }
}
