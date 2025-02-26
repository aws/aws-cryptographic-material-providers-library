// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * A cache that is NOT safe for use in a multi threaded environment.
 */
public class SingleThreadedCache {

  /**
   * Maximum number of entries cached.
   */
  private final Integer entryCapacity;

  /**
   * Number of entries to prune at a time.
   */
  private final Integer entryPruningTailSize;

  protected SingleThreadedCache(BuilderImpl builder) {
    this.entryCapacity = builder.entryCapacity();
    this.entryPruningTailSize = builder.entryPruningTailSize();
  }

  /**
   * @return Maximum number of entries cached.
   */
  public Integer entryCapacity() {
    return this.entryCapacity;
  }

  /**
   * @return Number of entries to prune at a time.
   */
  public Integer entryPruningTailSize() {
    return this.entryPruningTailSize;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param entryCapacity Maximum number of entries cached.
     */
    Builder entryCapacity(Integer entryCapacity);

    /**
     * @return Maximum number of entries cached.
     */
    Integer entryCapacity();

    /**
     * @param entryPruningTailSize Number of entries to prune at a time.
     */
    Builder entryPruningTailSize(Integer entryPruningTailSize);

    /**
     * @return Number of entries to prune at a time.
     */
    Integer entryPruningTailSize();

    SingleThreadedCache build();
  }

  static class BuilderImpl implements Builder {

    protected Integer entryCapacity;

    protected Integer entryPruningTailSize;

    protected BuilderImpl() {}

    protected BuilderImpl(SingleThreadedCache model) {
      this.entryCapacity = model.entryCapacity();
      this.entryPruningTailSize = model.entryPruningTailSize();
    }

    public Builder entryCapacity(Integer entryCapacity) {
      this.entryCapacity = entryCapacity;
      return this;
    }

    public Integer entryCapacity() {
      return this.entryCapacity;
    }

    public Builder entryPruningTailSize(Integer entryPruningTailSize) {
      this.entryPruningTailSize = entryPruningTailSize;
      return this;
    }

    public Integer entryPruningTailSize() {
      return this.entryPruningTailSize;
    }

    public SingleThreadedCache build() {
      if (Objects.isNull(this.entryCapacity())) {
        throw new IllegalArgumentException(
          "Missing value for required field `entryCapacity`"
        );
      }
      if (Objects.nonNull(this.entryCapacity()) && this.entryCapacity() < 1) {
        throw new IllegalArgumentException(
          "`entryCapacity` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.entryPruningTailSize()) &&
        this.entryPruningTailSize() < 1
      ) {
        throw new IllegalArgumentException(
          "`entryPruningTailSize` must be greater than or equal to 1"
        );
      }
      return new SingleThreadedCache(this);
    }
  }
}
