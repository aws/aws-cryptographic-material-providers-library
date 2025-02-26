// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * The best choice for most situations. Probably a StormTrackingCache.
 */
public class DefaultCache {

  /**
   * Maximum number of entries cached.
   */
  private final Integer entryCapacity;

  protected DefaultCache(BuilderImpl builder) {
    this.entryCapacity = builder.entryCapacity();
  }

  /**
   * @return Maximum number of entries cached.
   */
  public Integer entryCapacity() {
    return this.entryCapacity;
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

    DefaultCache build();
  }

  static class BuilderImpl implements Builder {

    protected Integer entryCapacity;

    protected BuilderImpl() {}

    protected BuilderImpl(DefaultCache model) {
      this.entryCapacity = model.entryCapacity();
    }

    public Builder entryCapacity(Integer entryCapacity) {
      this.entryCapacity = entryCapacity;
      return this;
    }

    public Integer entryCapacity() {
      return this.entryCapacity;
    }

    public DefaultCache build() {
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
      return new DefaultCache(this);
    }
  }
}
