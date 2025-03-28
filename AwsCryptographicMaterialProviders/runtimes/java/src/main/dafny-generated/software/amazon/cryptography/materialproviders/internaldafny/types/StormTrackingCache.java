// Class StormTrackingCache
// Dafny class StormTrackingCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class StormTrackingCache {
  public int _entryCapacity;
  public Wrappers_Compile.Option<java.lang.Integer> _entryPruningTailSize;
  public int _gracePeriod;
  public int _graceInterval;
  public int _fanOut;
  public int _inFlightTTL;
  public int _sleepMilli;
  public Wrappers_Compile.Option<TimeUnits> _timeUnits;
  public StormTrackingCache (int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize, int gracePeriod, int graceInterval, int fanOut, int inFlightTTL, int sleepMilli, Wrappers_Compile.Option<TimeUnits> timeUnits) {
    this._entryCapacity = entryCapacity;
    this._entryPruningTailSize = entryPruningTailSize;
    this._gracePeriod = gracePeriod;
    this._graceInterval = graceInterval;
    this._fanOut = fanOut;
    this._inFlightTTL = inFlightTTL;
    this._sleepMilli = sleepMilli;
    this._timeUnits = timeUnits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StormTrackingCache o = (StormTrackingCache)other;
    return true && this._entryCapacity == o._entryCapacity && java.util.Objects.equals(this._entryPruningTailSize, o._entryPruningTailSize) && this._gracePeriod == o._gracePeriod && this._graceInterval == o._graceInterval && this._fanOut == o._fanOut && this._inFlightTTL == o._inFlightTTL && this._sleepMilli == o._sleepMilli && java.util.Objects.equals(this._timeUnits, o._timeUnits);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._entryCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._entryPruningTailSize);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._gracePeriod);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._graceInterval);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._fanOut);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._inFlightTTL);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._sleepMilli);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._timeUnits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.StormTrackingCache.StormTrackingCache");
    s.append("(");
    s.append(this._entryCapacity);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._entryPruningTailSize));
    s.append(", ");
    s.append(this._gracePeriod);
    s.append(", ");
    s.append(this._graceInterval);
    s.append(", ");
    s.append(this._fanOut);
    s.append(", ");
    s.append(this._inFlightTTL);
    s.append(", ");
    s.append(this._sleepMilli);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._timeUnits));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<StormTrackingCache> _TYPE = dafny.TypeDescriptor.<StormTrackingCache>referenceWithInitializer(StormTrackingCache.class, () -> StormTrackingCache.Default());
  public static dafny.TypeDescriptor<StormTrackingCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<StormTrackingCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final StormTrackingCache theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create(0, Wrappers_Compile.Option.<java.lang.Integer>Default(CountingNumber._typeDescriptor()), 0, 0, 0, 0, 0, Wrappers_Compile.Option.<TimeUnits>Default(TimeUnits._typeDescriptor()));
  public static StormTrackingCache Default() {
    return theDefault;
  }
  public static StormTrackingCache create(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize, int gracePeriod, int graceInterval, int fanOut, int inFlightTTL, int sleepMilli, Wrappers_Compile.Option<TimeUnits> timeUnits) {
    return new StormTrackingCache(entryCapacity, entryPruningTailSize, gracePeriod, graceInterval, fanOut, inFlightTTL, sleepMilli, timeUnits);
  }
  public static StormTrackingCache create_StormTrackingCache(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize, int gracePeriod, int graceInterval, int fanOut, int inFlightTTL, int sleepMilli, Wrappers_Compile.Option<TimeUnits> timeUnits) {
    return create(entryCapacity, entryPruningTailSize, gracePeriod, graceInterval, fanOut, inFlightTTL, sleepMilli, timeUnits);
  }
  public boolean is_StormTrackingCache() { return true; }
  public int dtor_entryCapacity() {
    return this._entryCapacity;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_entryPruningTailSize() {
    return this._entryPruningTailSize;
  }
  public int dtor_gracePeriod() {
    return this._gracePeriod;
  }
  public int dtor_graceInterval() {
    return this._graceInterval;
  }
  public int dtor_fanOut() {
    return this._fanOut;
  }
  public int dtor_inFlightTTL() {
    return this._inFlightTTL;
  }
  public int dtor_sleepMilli() {
    return this._sleepMilli;
  }
  public Wrappers_Compile.Option<TimeUnits> dtor_timeUnits() {
    return this._timeUnits;
  }
}
