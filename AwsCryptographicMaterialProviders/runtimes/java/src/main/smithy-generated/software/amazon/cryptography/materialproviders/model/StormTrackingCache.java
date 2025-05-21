// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviders.model;

/**
 * A cache that is safe for use in a multi threaded environment,
 * and tries to prevent redundant or overly parallel backend calls.
 */
public class StormTrackingCache {

  /**
   * Maximum number of entries cached.
   */
  private final int entryCapacity;

  /**
   * Number of entries to prune at a time.
   */
  private final int entryPruningTailSize;

  /**
   * How much time before expiration should an attempt be made to refresh the materials.
   *   If zero, use a simple cache with no storm tracking.
   */
  private final int gracePeriod;

  /**
   * How much time between attempts to refresh the materials.
   */
  private final int graceInterval;

  /**
   * How many simultaneous attempts to refresh the materials.
   */
  private final int fanOut;

  /**
   * How much time until an attempt to refresh the materials should be forgotten.
   */
  private final int inFlightTTL;

  /**
   * How many milliseconds should a thread sleep if fanOut is exceeded.
   */
  private final int sleepMilli;

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
  public int entryCapacity() {
    return this.entryCapacity;
  }

  /**
   * @return Number of entries to prune at a time.
   */
  public int entryPruningTailSize() {
    return this.entryPruningTailSize;
  }

  /**
   * @return How much time before expiration should an attempt be made to refresh the materials.
   *   If zero, use a simple cache with no storm tracking.
   */
  public int gracePeriod() {
    return this.gracePeriod;
  }

  /**
   * @return How much time between attempts to refresh the materials.
   */
  public int graceInterval() {
    return this.graceInterval;
  }

  /**
   * @return How many simultaneous attempts to refresh the materials.
   */
  public int fanOut() {
    return this.fanOut;
  }

  /**
   * @return How much time until an attempt to refresh the materials should be forgotten.
   */
  public int inFlightTTL() {
    return this.inFlightTTL;
  }

  /**
   * @return How many milliseconds should a thread sleep if fanOut is exceeded.
   */
  public int sleepMilli() {
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
    Builder entryCapacity(int entryCapacity);

    /**
     * @return Maximum number of entries cached.
     */
    int entryCapacity();

    /**
     * @param entryPruningTailSize Number of entries to prune at a time.
     */
    Builder entryPruningTailSize(int entryPruningTailSize);

    /**
     * @return Number of entries to prune at a time.
     */
    int entryPruningTailSize();

    /**
     * @param gracePeriod How much time before expiration should an attempt be made to refresh the materials.
     *   If zero, use a simple cache with no storm tracking.
     */
    Builder gracePeriod(int gracePeriod);

    /**
     * @return How much time before expiration should an attempt be made to refresh the materials.
     *   If zero, use a simple cache with no storm tracking.
     */
    int gracePeriod();

    /**
     * @param graceInterval How much time between attempts to refresh the materials.
     */
    Builder graceInterval(int graceInterval);

    /**
     * @return How much time between attempts to refresh the materials.
     */
    int graceInterval();

    /**
     * @param fanOut How many simultaneous attempts to refresh the materials.
     */
    Builder fanOut(int fanOut);

    /**
     * @return How many simultaneous attempts to refresh the materials.
     */
    int fanOut();

    /**
     * @param inFlightTTL How much time until an attempt to refresh the materials should be forgotten.
     */
    Builder inFlightTTL(int inFlightTTL);

    /**
     * @return How much time until an attempt to refresh the materials should be forgotten.
     */
    int inFlightTTL();

    /**
     * @param sleepMilli How many milliseconds should a thread sleep if fanOut is exceeded.
     */
    Builder sleepMilli(int sleepMilli);

    /**
     * @return How many milliseconds should a thread sleep if fanOut is exceeded.
     */
    int sleepMilli();

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

    protected int entryCapacity;

    private boolean _entryCapacitySet = false;

    protected int entryPruningTailSize;

    private boolean _entryPruningTailSizeSet = false;

    protected int gracePeriod;

    private boolean _gracePeriodSet = false;

    protected int graceInterval;

    private boolean _graceIntervalSet = false;

    protected int fanOut;

    private boolean _fanOutSet = false;

    protected int inFlightTTL;

    private boolean _inFlightTTLSet = false;

    protected int sleepMilli;

    private boolean _sleepMilliSet = false;

    protected TimeUnits timeUnits;

    protected BuilderImpl() {}

    protected BuilderImpl(StormTrackingCache model) {
      this.entryCapacity = model.entryCapacity();
      this._entryCapacitySet = true;
      this.entryPruningTailSize = model.entryPruningTailSize();
      this._entryPruningTailSizeSet = true;
      this.gracePeriod = model.gracePeriod();
      this._gracePeriodSet = true;
      this.graceInterval = model.graceInterval();
      this._graceIntervalSet = true;
      this.fanOut = model.fanOut();
      this._fanOutSet = true;
      this.inFlightTTL = model.inFlightTTL();
      this._inFlightTTLSet = true;
      this.sleepMilli = model.sleepMilli();
      this._sleepMilliSet = true;
      this.timeUnits = model.timeUnits();
    }

    public Builder entryCapacity(int entryCapacity) {
      this.entryCapacity = entryCapacity;
      this._entryCapacitySet = true;
      return this;
    }

    public int entryCapacity() {
      return this.entryCapacity;
    }

    public Builder entryPruningTailSize(int entryPruningTailSize) {
      this.entryPruningTailSize = entryPruningTailSize;
      this._entryPruningTailSizeSet = true;
      return this;
    }

    public int entryPruningTailSize() {
      return this.entryPruningTailSize;
    }

    public Builder gracePeriod(int gracePeriod) {
      this.gracePeriod = gracePeriod;
      this._gracePeriodSet = true;
      return this;
    }

    public int gracePeriod() {
      return this.gracePeriod;
    }

    public Builder graceInterval(int graceInterval) {
      this.graceInterval = graceInterval;
      this._graceIntervalSet = true;
      return this;
    }

    public int graceInterval() {
      return this.graceInterval;
    }

    public Builder fanOut(int fanOut) {
      this.fanOut = fanOut;
      this._fanOutSet = true;
      return this;
    }

    public int fanOut() {
      return this.fanOut;
    }

    public Builder inFlightTTL(int inFlightTTL) {
      this.inFlightTTL = inFlightTTL;
      this._inFlightTTLSet = true;
      return this;
    }

    public int inFlightTTL() {
      return this.inFlightTTL;
    }

    public Builder sleepMilli(int sleepMilli) {
      this.sleepMilli = sleepMilli;
      this._sleepMilliSet = true;
      return this;
    }

    public int sleepMilli() {
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
      if (!this._entryCapacitySet) {
        throw new IllegalArgumentException(
          "Missing value for required field `entryCapacity`"
        );
      }
      if (this._entryCapacitySet && this.entryCapacity() < 1) {
        throw new IllegalArgumentException(
          "`entryCapacity` must be greater than or equal to 1"
        );
      }
      if (this._entryPruningTailSizeSet && this.entryPruningTailSize() < 1) {
        throw new IllegalArgumentException(
          "`entryPruningTailSize` must be greater than or equal to 1"
        );
      }
      if (!this._gracePeriodSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `gracePeriod`"
        );
      }
      if (this._gracePeriodSet && this.gracePeriod() < 1) {
        throw new IllegalArgumentException(
          "`gracePeriod` must be greater than or equal to 1"
        );
      }
      if (!this._graceIntervalSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `graceInterval`"
        );
      }
      if (this._graceIntervalSet && this.graceInterval() < 1) {
        throw new IllegalArgumentException(
          "`graceInterval` must be greater than or equal to 1"
        );
      }
      if (!this._fanOutSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `fanOut`"
        );
      }
      if (this._fanOutSet && this.fanOut() < 1) {
        throw new IllegalArgumentException(
          "`fanOut` must be greater than or equal to 1"
        );
      }
      if (!this._inFlightTTLSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `inFlightTTL`"
        );
      }
      if (this._inFlightTTLSet && this.inFlightTTL() < 1) {
        throw new IllegalArgumentException(
          "`inFlightTTL` must be greater than or equal to 1"
        );
      }
      if (!this._sleepMilliSet) {
        throw new IllegalArgumentException(
          "Missing value for required field `sleepMilli`"
        );
      }
      if (this._sleepMilliSet && this.sleepMilli() < 1) {
        throw new IllegalArgumentException(
          "`sleepMilli` must be greater than or equal to 1"
        );
      }
      return new StormTrackingCache(this);
    }
  }
}
