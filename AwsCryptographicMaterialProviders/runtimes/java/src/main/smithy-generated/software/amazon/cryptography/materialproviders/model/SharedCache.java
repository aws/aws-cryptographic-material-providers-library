// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.materialproviders.CryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;

/**
 * Shared cache across multiple Hierarchical Keyrings.
 */
public class SharedCache {

  /**
   * Shared cache across multiple Hierarchical Keyrings.
   */
  private final ICryptographicMaterialsCache cache;

  protected SharedCache(BuilderImpl builder) {
    this.cache = builder.cache();
  }

  /**
   * @return Shared cache across multiple Hierarchical Keyrings.
   */
  public ICryptographicMaterialsCache cache() {
    return this.cache;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param cache Shared cache across multiple Hierarchical Keyrings.
     */
    Builder cache(ICryptographicMaterialsCache cache);

    /**
     * @return Shared cache across multiple Hierarchical Keyrings.
     */
    ICryptographicMaterialsCache cache();

    SharedCache build();
  }

  static class BuilderImpl implements Builder {

    protected ICryptographicMaterialsCache cache;

    protected BuilderImpl() {}

    protected BuilderImpl(SharedCache model) {
      this.cache = model.cache();
    }

    public Builder cache(ICryptographicMaterialsCache cache) {
      this.cache = CryptographicMaterialsCache.wrap(cache);
      return this;
    }

    public ICryptographicMaterialsCache cache() {
      return this.cache;
    }

    public SharedCache build() {
      if (Objects.isNull(this.cache())) {
        throw new IllegalArgumentException(
          "Missing value for required field `cache`"
        );
      }
      return new SharedCache(this);
    }
  }
}
