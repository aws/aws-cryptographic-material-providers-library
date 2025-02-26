// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

import java.util.Objects;

/**
 * A cache that is safe for use in a multi threaded environment,
 * and tries to prevent redundant or overly parallel backend calls.
 */
public class StormTrackingCache {

  /**
   * Maximum number of entries cached.
   */
  private final Integer entryCapacity;

  /**
   * Number of entries to prune at a time.
   */
  private final Integer entryPruningTailSize;

  /**
   * How much time before expiration should an attempt be made to refresh the materials.
   *   If zero, use a simple cache with no storm tracking.
   */
  private final Integer gracePeriod;

  /**
   * How much time between attempts to refresh the materials.
   */
  private final Integer graceInterval;

  /**
   * How many simultaneous attempts to refresh the materials.
   */
  private final Integer fanOut;

  /**
   * How much time until an attempt to refresh the materials should be forgotten.
   */
  private final Integer inFlightTTL;

  /**
   * How many milliseconds should a thread sleep if fanOut is exceeded.
   */
  private final Integer sleepMilli;

  /**
   * The time unit for gracePeriod, graceInterval, and inFlightTTL.
   *   The default is seconds.
   *   If this is set to milliseconds, then these values will be treated as milliseconds.
   */
  private final TimeUnits timeUnits;

  protected StormTrackingCache(BuilderImpl builder) {
    this.entryCapacity = builder.entryCapacity();
    this.entryPruningTailSize = builder.entryPruningTailSize();
    this.gracePeriod = builder.gracePeriod();
    this.graceInterval = builder.graceInterval();
    this.fanOut = builder.fanOut();
    this.inFlightTTL = builder.inFlightTTL();
    this.sleepMilli = builder.sleepMilli();
    this.timeUnits = builder.timeUnits();
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

  /**
   * @return How much time before expiration should an attempt be made to refresh the materials.
   *   If zero, use a simple cache with no storm tracking.
   */
  public Integer gracePeriod() {
    return this.gracePeriod;
  }

  /**
   * @return How much time between attempts to refresh the materials.
   */
  public Integer graceInterval() {
    return this.graceInterval;
  }

  /**
   * @return How many simultaneous attempts to refresh the materials.
   */
  public Integer fanOut() {
    return this.fanOut;
  }

  /**
   * @return How much time until an attempt to refresh the materials should be forgotten.
   */
  public Integer inFlightTTL() {
    return this.inFlightTTL;
  }

  /**
   * @return How many milliseconds should a thread sleep if fanOut is exceeded.
   */
  public Integer sleepMilli() {
    return this.sleepMilli;
  }

  /**
   * @return The time unit for gracePeriod, graceInterval, and inFlightTTL.
   *   The default is seconds.
   *   If this is set to milliseconds, then these values will be treated as milliseconds.
   */
  public TimeUnits timeUnits() {
    return this.timeUnits;
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

    /**
     * @param gracePeriod How much time before expiration should an attempt be made to refresh the materials.
     *   If zero, use a simple cache with no storm tracking.
     */
    Builder gracePeriod(Integer gracePeriod);

    /**
     * @return How much time before expiration should an attempt be made to refresh the materials.
     *   If zero, use a simple cache with no storm tracking.
     */
    Integer gracePeriod();

    /**
     * @param graceInterval How much time between attempts to refresh the materials.
     */
    Builder graceInterval(Integer graceInterval);

    /**
     * @return How much time between attempts to refresh the materials.
     */
    Integer graceInterval();

    /**
     * @param fanOut How many simultaneous attempts to refresh the materials.
     */
    Builder fanOut(Integer fanOut);

    /**
     * @return How many simultaneous attempts to refresh the materials.
     */
    Integer fanOut();

    /**
     * @param inFlightTTL How much time until an attempt to refresh the materials should be forgotten.
     */
    Builder inFlightTTL(Integer inFlightTTL);

    /**
     * @return How much time until an attempt to refresh the materials should be forgotten.
     */
    Integer inFlightTTL();

    /**
     * @param sleepMilli How many milliseconds should a thread sleep if fanOut is exceeded.
     */
    Builder sleepMilli(Integer sleepMilli);

    /**
     * @return How many milliseconds should a thread sleep if fanOut is exceeded.
     */
    Integer sleepMilli();

    /**
     * @param timeUnits The time unit for gracePeriod, graceInterval, and inFlightTTL.
     *   The default is seconds.
     *   If this is set to milliseconds, then these values will be treated as milliseconds.
     */
    Builder timeUnits(TimeUnits timeUnits);

    /**
     * @return The time unit for gracePeriod, graceInterval, and inFlightTTL.
     *   The default is seconds.
     *   If this is set to milliseconds, then these values will be treated as milliseconds.
     */
    TimeUnits timeUnits();

    StormTrackingCache build();
  }

  static class BuilderImpl implements Builder {

    protected Integer entryCapacity;

    protected Integer entryPruningTailSize;

    protected Integer gracePeriod;

    protected Integer graceInterval;

    protected Integer fanOut;

    protected Integer inFlightTTL;

    protected Integer sleepMilli;

    protected TimeUnits timeUnits;

    protected BuilderImpl() {}

    protected BuilderImpl(StormTrackingCache model) {
      this.entryCapacity = model.entryCapacity();
      this.entryPruningTailSize = model.entryPruningTailSize();
      this.gracePeriod = model.gracePeriod();
      this.graceInterval = model.graceInterval();
      this.fanOut = model.fanOut();
      this.inFlightTTL = model.inFlightTTL();
      this.sleepMilli = model.sleepMilli();
      this.timeUnits = model.timeUnits();
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

    public Builder gracePeriod(Integer gracePeriod) {
      this.gracePeriod = gracePeriod;
      return this;
    }

    public Integer gracePeriod() {
      return this.gracePeriod;
    }

    public Builder graceInterval(Integer graceInterval) {
      this.graceInterval = graceInterval;
      return this;
    }

    public Integer graceInterval() {
      return this.graceInterval;
    }

    public Builder fanOut(Integer fanOut) {
      this.fanOut = fanOut;
      return this;
    }

    public Integer fanOut() {
      return this.fanOut;
    }

    public Builder inFlightTTL(Integer inFlightTTL) {
      this.inFlightTTL = inFlightTTL;
      return this;
    }

    public Integer inFlightTTL() {
      return this.inFlightTTL;
    }

    public Builder sleepMilli(Integer sleepMilli) {
      this.sleepMilli = sleepMilli;
      return this;
    }

    public Integer sleepMilli() {
      return this.sleepMilli;
    }

    public Builder timeUnits(TimeUnits timeUnits) {
      this.timeUnits = timeUnits;
      return this;
    }

    public TimeUnits timeUnits() {
      return this.timeUnits;
    }

    public StormTrackingCache build() {
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
      if (Objects.isNull(this.gracePeriod())) {
        throw new IllegalArgumentException(
          "Missing value for required field `gracePeriod`"
        );
      }
      if (Objects.nonNull(this.gracePeriod()) && this.gracePeriod() < 1) {
        throw new IllegalArgumentException(
          "`gracePeriod` must be greater than or equal to 1"
        );
      }
      if (Objects.isNull(this.graceInterval())) {
        throw new IllegalArgumentException(
          "Missing value for required field `graceInterval`"
        );
      }
      if (Objects.nonNull(this.graceInterval()) && this.graceInterval() < 1) {
        throw new IllegalArgumentException(
          "`graceInterval` must be greater than or equal to 1"
        );
      }
      if (Objects.isNull(this.fanOut())) {
        throw new IllegalArgumentException(
          "Missing value for required field `fanOut`"
        );
      }
      if (Objects.nonNull(this.fanOut()) && this.fanOut() < 1) {
        throw new IllegalArgumentException(
          "`fanOut` must be greater than or equal to 1"
        );
      }
      if (Objects.isNull(this.inFlightTTL())) {
        throw new IllegalArgumentException(
          "Missing value for required field `inFlightTTL`"
        );
      }
      if (Objects.nonNull(this.inFlightTTL()) && this.inFlightTTL() < 1) {
        throw new IllegalArgumentException(
          "`inFlightTTL` must be greater than or equal to 1"
        );
      }
      if (Objects.isNull(this.sleepMilli())) {
        throw new IllegalArgumentException(
          "Missing value for required field `sleepMilli`"
        );
      }
      if (Objects.nonNull(this.sleepMilli()) && this.sleepMilli() < 1) {
        throw new IllegalArgumentException(
          "`sleepMilli` must be greater than or equal to 1"
        );
      }
      return new StormTrackingCache(this);
    }
  }
}
