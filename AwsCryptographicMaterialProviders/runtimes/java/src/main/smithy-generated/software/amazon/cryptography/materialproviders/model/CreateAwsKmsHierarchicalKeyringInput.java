// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.materialproviders.BranchKeyIdSupplier;
import software.amazon.cryptography.materialproviders.IBranchKeyIdSupplier;

/**
 * Inputs for creating a Hierarchical Keyring.
 */
public class CreateAwsKmsHierarchicalKeyringInput {

  /**
   * The identifier for the single Branch Key responsible for wrapping and unwrapping the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
   */
  private final String branchKeyId;

  /**
   * A Branch Key Supplier which determines what Branch Key to use to wrap and unwrap the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
   */
  private final IBranchKeyIdSupplier branchKeyIdSupplier;

  /**
   * The Key Store which contains the Branch Key(s) responsible for wrapping and unwrapping data keys.
   */
  private final KeyStore keyStore;

  /**
   * How many seconds the Branch Key material is allowed to be reused within the local cache before it is re-retrieved from Amazon DynamoDB and re-authenticated with AWS KMS.
   */
  private final long ttlSeconds;

  /**
   * Which type of local cache to use.
   */
  private final CacheType cache;

  /**
   * Shared cache across multiple Hierarchical Keyrings. For every Hierarchical Keyring, one out the `cache` or `sharedCache` parameter MUST be set, not both. If both parameters are set, an exception will be thrown. If neither of the two parameters are set, a DefaultCache is initialized to be used with the Hierarchical Keyring with entryCapacity = 1000.
   */
  private final CacheType sharedCache;

  protected CreateAwsKmsHierarchicalKeyringInput(BuilderImpl builder) {
    this.branchKeyId = builder.branchKeyId();
    this.branchKeyIdSupplier = builder.branchKeyIdSupplier();
    this.keyStore = builder.keyStore();
    this.ttlSeconds = builder.ttlSeconds();
    this.cache = builder.cache();
    this.sharedCache = builder.sharedCache();
  }

  /**
   * @return The identifier for the single Branch Key responsible for wrapping and unwrapping the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
   */
  public String branchKeyId() {
    return this.branchKeyId;
  }

  /**
   * @return A Branch Key Supplier which determines what Branch Key to use to wrap and unwrap the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
   */
  public IBranchKeyIdSupplier branchKeyIdSupplier() {
    return this.branchKeyIdSupplier;
  }

  /**
   * @return The Key Store which contains the Branch Key(s) responsible for wrapping and unwrapping data keys.
   */
  public KeyStore keyStore() {
    return this.keyStore;
  }

  /**
   * @return How many seconds the Branch Key material is allowed to be reused within the local cache before it is re-retrieved from Amazon DynamoDB and re-authenticated with AWS KMS.
   */
  public long ttlSeconds() {
    return this.ttlSeconds;
  }

  /**
   * @return Which type of local cache to use.
   */
  public CacheType cache() {
    return this.cache;
  }

  /**
   * @return Shared cache across multiple Hierarchical Keyrings. For every Hierarchical Keyring, one out the `cache` or `sharedCache` parameter MUST be set, not both. If both parameters are set, an exception will be thrown. If neither of the two parameters are set, a DefaultCache is initialized to be used with the Hierarchical Keyring with entryCapacity = 1000.
   */
  public CacheType sharedCache() {
    return this.sharedCache;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param branchKeyId The identifier for the single Branch Key responsible for wrapping and unwrapping the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
     */
    Builder branchKeyId(String branchKeyId);

    /**
     * @return The identifier for the single Branch Key responsible for wrapping and unwrapping the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
     */
    String branchKeyId();

    /**
     * @param branchKeyIdSupplier A Branch Key Supplier which determines what Branch Key to use to wrap and unwrap the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
     */
    Builder branchKeyIdSupplier(IBranchKeyIdSupplier branchKeyIdSupplier);

    /**
     * @return A Branch Key Supplier which determines what Branch Key to use to wrap and unwrap the data key. Either a Branch Key ID or Branch Key Supplier must be specified.
     */
    IBranchKeyIdSupplier branchKeyIdSupplier();

    /**
     * @param keyStore The Key Store which contains the Branch Key(s) responsible for wrapping and unwrapping data keys.
     */
    Builder keyStore(KeyStore keyStore);

    /**
     * @return The Key Store which contains the Branch Key(s) responsible for wrapping and unwrapping data keys.
     */
    KeyStore keyStore();

    /**
     * @param ttlSeconds How many seconds the Branch Key material is allowed to be reused within the local cache before it is re-retrieved from Amazon DynamoDB and re-authenticated with AWS KMS.
     */
    Builder ttlSeconds(long ttlSeconds);

    /**
     * @return How many seconds the Branch Key material is allowed to be reused within the local cache before it is re-retrieved from Amazon DynamoDB and re-authenticated with AWS KMS.
     */
    long ttlSeconds();

    /**
     * @param cache Which type of local cache to use.
     */
    Builder cache(CacheType cache);

    /**
     * @return Which type of local cache to use.
     */
    CacheType cache();

    /**
     * @param sharedCache Shared cache across multiple Hierarchical Keyrings. For every Hierarchical Keyring, one out the `cache` or `sharedCache` parameter MUST be set, not both. If both parameters are set, an exception will be thrown. If neither of the two parameters are set, a DefaultCache is initialized to be used with the Hierarchical Keyring with entryCapacity = 1000.
     */
    Builder sharedCache(CacheType sharedCache);

    /**
     * @return Shared cache across multiple Hierarchical Keyrings. For every Hierarchical Keyring, one out the `cache` or `sharedCache` parameter MUST be set, not both. If both parameters are set, an exception will be thrown. If neither of the two parameters are set, a DefaultCache is initialized to be used with the Hierarchical Keyring with entryCapacity = 1000.
     */
    CacheType sharedCache();

    CreateAwsKmsHierarchicalKeyringInput build();
  }

  static class BuilderImpl implements Builder {

    protected String branchKeyId;

    protected IBranchKeyIdSupplier branchKeyIdSupplier;

    protected KeyStore keyStore;

    protected long ttlSeconds;

    private boolean _ttlSecondsSet = false;

    protected CacheType cache;

    protected CacheType sharedCache;

    protected BuilderImpl() {}

    protected BuilderImpl(CreateAwsKmsHierarchicalKeyringInput model) {
      this.branchKeyId = model.branchKeyId();
      this.branchKeyIdSupplier = model.branchKeyIdSupplier();
      this.keyStore = model.keyStore();
      this.ttlSeconds = model.ttlSeconds();
      this._ttlSecondsSet = true;
      this.cache = model.cache();
      this.sharedCache = model.sharedCache();
    }

    public Builder branchKeyId(String branchKeyId) {
      this.branchKeyId = branchKeyId;
      return this;
    }

    public String branchKeyId() {
      return this.branchKeyId;
    }

    public Builder branchKeyIdSupplier(
      IBranchKeyIdSupplier branchKeyIdSupplier
    ) {
      this.branchKeyIdSupplier = BranchKeyIdSupplier.wrap(branchKeyIdSupplier);
      return this;
    }

    public IBranchKeyIdSupplier branchKeyIdSupplier() {
      return this.branchKeyIdSupplier;
    }

    public Builder keyStore(KeyStore keyStore) {
      this.keyStore = keyStore;
      return this;
    }

    public KeyStore keyStore() {
      return this.keyStore;
    }

    public Builder ttlSeconds(long ttlSeconds) {
      this.ttlSeconds = ttlSeconds;
      this._ttlSecondsSet = true;
      return this;
    }

    public long ttlSeconds() {
      return this.ttlSeconds;
    }

    public Builder cache(CacheType cache) {
      this.cache = cache;
      return this;
    }

    public CacheType cache() {
      return this.cache;
    }

    public Builder sharedCache(CacheType sharedCache) {
      this.sharedCache = sharedCache;
      return this;
    }

    public CacheType sharedCache() {
      return this.sharedCache;
    }

    public CreateAwsKmsHierarchicalKeyringInput build() {
      if (Objects.isNull(this.keyStore())) {
        throw new IllegalArgumentException(
          "Missing value for required field `keyStore`"
        );
      }
      if (!this._ttlSecondsSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `ttlSeconds`"
        );
      }
      if (this._ttlSecondsSet && this.ttlSeconds() < 0) {
        throw new IllegalArgumentException(
          "`ttlSeconds` must be greater than or equal to 0"
        );
      }
      return new CreateAwsKmsHierarchicalKeyringInput(this);
    }
  }
}
