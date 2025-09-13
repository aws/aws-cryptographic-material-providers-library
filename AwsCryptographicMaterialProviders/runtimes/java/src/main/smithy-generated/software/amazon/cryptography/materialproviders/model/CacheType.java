// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;
import software.amazon.cryptography.materialproviders.CryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;

public class CacheType {

  /**
   * The best choice for most situations. Probably a StormTrackingCache.
   */
  private final DefaultCache Default;

  /**
   * Nothing should ever be cached.
   */
  private final NoCache No;

  /**
   * A cache that is NOT safe for use in a multi threaded environment.
   */
  private final SingleThreadedCache SingleThreaded;

  /**
   * A cache that is safe for use in a multi threaded environment, but no extra functionality.
   */
  private final MultiThreadedCache MultiThreaded;

  /**
   * A cache that is safe for use in a multi threaded environment,
   * and tries to prevent redundant or overly parallel backend calls.
   */
  private final StormTrackingCache StormTracking;

  /**
   * Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.
   */
  private final ICryptographicMaterialsCache Shared;

  protected CacheType(BuilderImpl builder) {
    this.Default = builder.Default();
    this.No = builder.No();
    this.SingleThreaded = builder.SingleThreaded();
    this.MultiThreaded = builder.MultiThreaded();
    this.StormTracking = builder.StormTracking();
    this.Shared = builder.Shared();
  }

  /**
   * @return The best choice for most situations. Probably a StormTrackingCache.
   */
  public DefaultCache Default() {
    return this.Default;
  }

  /**
   * @return Nothing should ever be cached.
   */
  public NoCache No() {
    return this.No;
  }

  /**
   * @return A cache that is NOT safe for use in a multi threaded environment.
   */
  public SingleThreadedCache SingleThreaded() {
    return this.SingleThreaded;
  }

  /**
   * @return A cache that is safe for use in a multi threaded environment, but no extra functionality.
   */
  public MultiThreadedCache MultiThreaded() {
    return this.MultiThreaded;
  }

  /**
   * @return A cache that is safe for use in a multi threaded environment,
   * and tries to prevent redundant or overly parallel backend calls.
   */
  public StormTrackingCache StormTracking() {
    return this.StormTracking;
  }

  /**
   * @return Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.
   */
  public ICryptographicMaterialsCache Shared() {
    return this.Shared;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param Default The best choice for most situations. Probably a StormTrackingCache.
     */
    Builder Default(DefaultCache Default);

    /**
     * @return The best choice for most situations. Probably a StormTrackingCache.
     */
    DefaultCache Default();

    /**
     * @param No Nothing should ever be cached.
     */
    Builder No(NoCache No);

    /**
     * @return Nothing should ever be cached.
     */
    NoCache No();

    /**
     * @param SingleThreaded A cache that is NOT safe for use in a multi threaded environment.
     */
    Builder SingleThreaded(SingleThreadedCache SingleThreaded);

    /**
     * @return A cache that is NOT safe for use in a multi threaded environment.
     */
    SingleThreadedCache SingleThreaded();

    /**
     * @param MultiThreaded A cache that is safe for use in a multi threaded environment, but no extra functionality.
     */
    Builder MultiThreaded(MultiThreadedCache MultiThreaded);

    /**
     * @return A cache that is safe for use in a multi threaded environment, but no extra functionality.
     */
    MultiThreadedCache MultiThreaded();

    /**
     * @param StormTracking A cache that is safe for use in a multi threaded environment,
     * and tries to prevent redundant or overly parallel backend calls.
     */
    Builder StormTracking(StormTrackingCache StormTracking);

    /**
     * @return A cache that is safe for use in a multi threaded environment,
     * and tries to prevent redundant or overly parallel backend calls.
     */
    StormTrackingCache StormTracking();

    /**
     * @param Shared Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.
     */
    Builder Shared(ICryptographicMaterialsCache Shared);

    /**
     * @return Shared cache across multiple Hierarchical Keyrings. For this cache type, the user should provide an already constructed CryptographicMaterialsCache to the Hierarchical Keyring at initialization.
     */
    ICryptographicMaterialsCache Shared();

    CacheType build();
  }

  static class BuilderImpl implements Builder {

    protected DefaultCache Default;

    protected NoCache No;

    protected SingleThreadedCache SingleThreaded;

    protected MultiThreadedCache MultiThreaded;

    protected StormTrackingCache StormTracking;

    protected ICryptographicMaterialsCache Shared;

    protected BuilderImpl() {}

    protected BuilderImpl(CacheType model) {
      this.Default = model.Default();
      this.No = model.No();
      this.SingleThreaded = model.SingleThreaded();
      this.MultiThreaded = model.MultiThreaded();
      this.StormTracking = model.StormTracking();
      this.Shared = model.Shared();
    }

    public Builder Default(DefaultCache Default) {
      this.Default = Default;
      return this;
    }

    public DefaultCache Default() {
      return this.Default;
    }

    public Builder No(NoCache No) {
      this.No = No;
      return this;
    }

    public NoCache No() {
      return this.No;
    }

    public Builder SingleThreaded(SingleThreadedCache SingleThreaded) {
      this.SingleThreaded = SingleThreaded;
      return this;
    }

    public SingleThreadedCache SingleThreaded() {
      return this.SingleThreaded;
    }

    public Builder MultiThreaded(MultiThreadedCache MultiThreaded) {
      this.MultiThreaded = MultiThreaded;
      return this;
    }

    public MultiThreadedCache MultiThreaded() {
      return this.MultiThreaded;
    }

    public Builder StormTracking(StormTrackingCache StormTracking) {
      this.StormTracking = StormTracking;
      return this;
    }

    public StormTrackingCache StormTracking() {
      return this.StormTracking;
    }

    public Builder Shared(ICryptographicMaterialsCache Shared) {
      this.Shared = CryptographicMaterialsCache.wrap(Shared);
      return this;
    }

    public ICryptographicMaterialsCache Shared() {
      return this.Shared;
    }

    public CacheType build() {
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`CacheType` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new CacheType(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = {
        this.Default,
        this.No,
        this.SingleThreaded,
        this.MultiThreaded,
        this.StormTracking,
        this.Shared,
      };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
