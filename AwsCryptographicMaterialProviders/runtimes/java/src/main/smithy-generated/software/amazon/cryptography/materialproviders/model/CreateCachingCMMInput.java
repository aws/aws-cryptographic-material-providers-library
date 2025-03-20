// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.materialproviders.CryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.CryptographicMaterialsManager;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsManager;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.Keyring;

/**
 * Inputs for creating a Caching Cryptographic Materials Manager.
 */
public class CreateCachingCMMInput {
  /**
   * The Cryptographic Materials Cache the Caching Cryptographic Materials Manager will use to cache requests.
   */
  private final ICryptographicMaterialsCache underlyingCMC;

  /**
   * Sets the maximum lifetime for entries in the cache, for both encrypt and decrypt operations. When the specified amount of time passes after initial creation of the entry, the entry will be considered unusable, and the next operation will incur a cache miss.
   */
  private final int cacheLimitTtlSeconds;

  /**
   * The Cryptographic Materials Manager that the created Caching Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.
   */
  private final ICryptographicMaterialsManager underlyingCMM;

  /**
   * The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Caching CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.
   */
  private final IKeyring keyring;

  /**
   * Sets the partition ID for this CMM. By default, two CMMs will never use each other's cache entries. This helps ensure that CMMs with different delegates won't incorrectly use each other's encrypt and decrypt results. However, in certain special circumstances it can be useful to share entries between different CMMs - for example, if the backing CMM is constructed based on some parameters that depend on the operation, you may wish for delegates constructed with the same parameters to share the same partition. To accomplish this, set the same partition ID and backing cache on both CMMs; entries cached from one of these CMMs can then be used by the other. This should only be done with careful consideration and verification that the CMM delegates are equivalent for your application's purposes. By default, the partition ID is set to a random UUID to avoid any collisions.
   */
  private final String partitionKey;

  /**
   * Sets the maximum number of plaintext bytes that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^63 - 1. If this limit is set to zero, keys can only be cached if they are used for zero-length messages.
   */
  private final long limitBytes;

  /**
   * Sets the maximum number of individual messages that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^32. This is also the maximum accepted value.
   */
  private final int limitMessages;

  protected CreateCachingCMMInput(BuilderImpl builder) {
    this.underlyingCMC = builder.underlyingCMC();
    this.cacheLimitTtlSeconds = builder.cacheLimitTtlSeconds();
    this.underlyingCMM = builder.underlyingCMM();
    this.keyring = builder.keyring();
    this.partitionKey = builder.partitionKey();
    this.limitBytes = builder.limitBytes();
    this.limitMessages = builder.limitMessages();
  }

  /**
   * @return The Cryptographic Materials Cache the Caching Cryptographic Materials Manager will use to cache requests.
   */
  public ICryptographicMaterialsCache underlyingCMC() {
    return this.underlyingCMC;
  }

  /**
   * @return Sets the maximum lifetime for entries in the cache, for both encrypt and decrypt operations. When the specified amount of time passes after initial creation of the entry, the entry will be considered unusable, and the next operation will incur a cache miss.
   */
  public int cacheLimitTtlSeconds() {
    return this.cacheLimitTtlSeconds;
  }

  /**
   * @return The Cryptographic Materials Manager that the created Caching Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.
   */
  public ICryptographicMaterialsManager underlyingCMM() {
    return this.underlyingCMM;
  }

  /**
   * @return The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Caching CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.
   */
  public IKeyring keyring() {
    return this.keyring;
  }

  /**
   * @return Sets the partition ID for this CMM. By default, two CMMs will never use each other's cache entries. This helps ensure that CMMs with different delegates won't incorrectly use each other's encrypt and decrypt results. However, in certain special circumstances it can be useful to share entries between different CMMs - for example, if the backing CMM is constructed based on some parameters that depend on the operation, you may wish for delegates constructed with the same parameters to share the same partition. To accomplish this, set the same partition ID and backing cache on both CMMs; entries cached from one of these CMMs can then be used by the other. This should only be done with careful consideration and verification that the CMM delegates are equivalent for your application's purposes. By default, the partition ID is set to a random UUID to avoid any collisions.
   */
  public String partitionKey() {
    return this.partitionKey;
  }

  /**
   * @return Sets the maximum number of plaintext bytes that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^63 - 1. If this limit is set to zero, keys can only be cached if they are used for zero-length messages.
   */
  public long limitBytes() {
    return this.limitBytes;
  }

  /**
   * @return Sets the maximum number of individual messages that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^32. This is also the maximum accepted value.
   */
  public int limitMessages() {
    return this.limitMessages;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param underlyingCMC The Cryptographic Materials Cache the Caching Cryptographic Materials Manager will use to cache requests.
     */
    Builder underlyingCMC(ICryptographicMaterialsCache underlyingCMC);

    /**
     * @return The Cryptographic Materials Cache the Caching Cryptographic Materials Manager will use to cache requests.
     */
    ICryptographicMaterialsCache underlyingCMC();

    /**
     * @param cacheLimitTtlSeconds Sets the maximum lifetime for entries in the cache, for both encrypt and decrypt operations. When the specified amount of time passes after initial creation of the entry, the entry will be considered unusable, and the next operation will incur a cache miss.
     */
    Builder cacheLimitTtlSeconds(int cacheLimitTtlSeconds);

    /**
     * @return Sets the maximum lifetime for entries in the cache, for both encrypt and decrypt operations. When the specified amount of time passes after initial creation of the entry, the entry will be considered unusable, and the next operation will incur a cache miss.
     */
    int cacheLimitTtlSeconds();

    /**
     * @param underlyingCMM The Cryptographic Materials Manager that the created Caching Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.
     */
    Builder underlyingCMM(ICryptographicMaterialsManager underlyingCMM);

    /**
     * @return The Cryptographic Materials Manager that the created Caching Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.
     */
    ICryptographicMaterialsManager underlyingCMM();

    /**
     * @param keyring The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Caching CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.
     */
    Builder keyring(IKeyring keyring);

    /**
     * @return The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Caching CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.
     */
    IKeyring keyring();

    /**
     * @param partitionKey Sets the partition ID for this CMM. By default, two CMMs will never use each other's cache entries. This helps ensure that CMMs with different delegates won't incorrectly use each other's encrypt and decrypt results. However, in certain special circumstances it can be useful to share entries between different CMMs - for example, if the backing CMM is constructed based on some parameters that depend on the operation, you may wish for delegates constructed with the same parameters to share the same partition. To accomplish this, set the same partition ID and backing cache on both CMMs; entries cached from one of these CMMs can then be used by the other. This should only be done with careful consideration and verification that the CMM delegates are equivalent for your application's purposes. By default, the partition ID is set to a random UUID to avoid any collisions.
     */
    Builder partitionKey(String partitionKey);

    /**
     * @return Sets the partition ID for this CMM. By default, two CMMs will never use each other's cache entries. This helps ensure that CMMs with different delegates won't incorrectly use each other's encrypt and decrypt results. However, in certain special circumstances it can be useful to share entries between different CMMs - for example, if the backing CMM is constructed based on some parameters that depend on the operation, you may wish for delegates constructed with the same parameters to share the same partition. To accomplish this, set the same partition ID and backing cache on both CMMs; entries cached from one of these CMMs can then be used by the other. This should only be done with careful consideration and verification that the CMM delegates are equivalent for your application's purposes. By default, the partition ID is set to a random UUID to avoid any collisions.
     */
    String partitionKey();

    /**
     * @param limitBytes Sets the maximum number of plaintext bytes that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^63 - 1. If this limit is set to zero, keys can only be cached if they are used for zero-length messages.
     */
    Builder limitBytes(long limitBytes);

    /**
     * @return Sets the maximum number of plaintext bytes that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^63 - 1. If this limit is set to zero, keys can only be cached if they are used for zero-length messages.
     */
    long limitBytes();

    /**
     * @param limitMessages Sets the maximum number of individual messages that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^32. This is also the maximum accepted value.
     */
    Builder limitMessages(int limitMessages);

    /**
     * @return Sets the maximum number of individual messages that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^32. This is also the maximum accepted value.
     */
    int limitMessages();

    CreateCachingCMMInput build();
  }

  static class BuilderImpl implements Builder {
    protected ICryptographicMaterialsCache underlyingCMC;

    protected int cacheLimitTtlSeconds;

    private boolean _cacheLimitTtlSecondsSet = false;

    protected ICryptographicMaterialsManager underlyingCMM;

    protected IKeyring keyring;

    protected String partitionKey;

    protected long limitBytes;

    private boolean _limitBytesSet = false;

    protected int limitMessages;

    private boolean _limitMessagesSet = false;

    protected BuilderImpl() {
    }

    protected BuilderImpl(CreateCachingCMMInput model) {
      this.underlyingCMC = model.underlyingCMC();
      this.cacheLimitTtlSeconds = model.cacheLimitTtlSeconds();
      this._cacheLimitTtlSecondsSet = true;
      this.underlyingCMM = model.underlyingCMM();
      this.keyring = model.keyring();
      this.partitionKey = model.partitionKey();
      this.limitBytes = model.limitBytes();
      this._limitBytesSet = true;
      this.limitMessages = model.limitMessages();
      this._limitMessagesSet = true;
    }

    public Builder underlyingCMC(ICryptographicMaterialsCache underlyingCMC) {
      this.underlyingCMC = CryptographicMaterialsCache.wrap(underlyingCMC);
      return this;
    }

    public ICryptographicMaterialsCache underlyingCMC() {
      return this.underlyingCMC;
    }

    public Builder cacheLimitTtlSeconds(int cacheLimitTtlSeconds) {
      this.cacheLimitTtlSeconds = cacheLimitTtlSeconds;
      this._cacheLimitTtlSecondsSet = true;
      return this;
    }

    public int cacheLimitTtlSeconds() {
      return this.cacheLimitTtlSeconds;
    }

    public Builder underlyingCMM(ICryptographicMaterialsManager underlyingCMM) {
      this.underlyingCMM = CryptographicMaterialsManager.wrap(underlyingCMM);
      return this;
    }

    public ICryptographicMaterialsManager underlyingCMM() {
      return this.underlyingCMM;
    }

    public Builder keyring(IKeyring keyring) {
      this.keyring = Keyring.wrap(keyring);
      return this;
    }

    public IKeyring keyring() {
      return this.keyring;
    }

    public Builder partitionKey(String partitionKey) {
      this.partitionKey = partitionKey;
      return this;
    }

    public String partitionKey() {
      return this.partitionKey;
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

    public CreateCachingCMMInput build() {
      if (Objects.isNull(this.underlyingCMC()))  {
        throw new IllegalArgumentException("Missing value for required field `underlyingCMC`");
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
      return new CreateCachingCMMInput(this);
    }
  }
}
