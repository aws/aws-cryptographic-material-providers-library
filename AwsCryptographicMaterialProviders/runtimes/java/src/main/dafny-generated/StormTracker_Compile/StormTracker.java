// Class StormTracker
// Dafny class StormTracker compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StormTracker {
  public StormTracker() {
    this.wrapped = null;
    this.inFlight = null;
    this.gracePeriod = 0L;
    this.graceInterval = 0L;
    this.fanOut = 0L;
    this.inFlightTTL = 0L;
    this.lastPrune = 0L;
    this.sleepMilli = 0L;
  }
  public LocalCMC_Compile.LocalCMC wrapped;
  public DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, java.lang.Long> inFlight;
  public long gracePeriod;
  public long graceInterval;
  public long fanOut;
  public long inFlightTTL;
  public long lastPrune;
  public long sleepMilli;
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache cache)
  {
    long _0_gracePeriod = 0L;
    long _1_graceInterval = 0L;
    long _2_inFlightTTL = 0L;
    if ((((cache).dtor_timeUnits()).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits.create_Seconds())).is_Seconds()) {
      _0_gracePeriod = (long) (long) ((((long) ((cache).dtor_gracePeriod()))) * ((long) 1000L));
      _1_graceInterval = (long) (long) ((((long) ((cache).dtor_graceInterval()))) * ((long) 1000L));
      _2_inFlightTTL = (long) (long) ((((long) ((cache).dtor_inFlightTTL()))) * ((long) 1000L));
    } else {
      _0_gracePeriod = ((long) ((cache).dtor_gracePeriod()));
      _1_graceInterval = ((long) ((cache).dtor_graceInterval()));
      _2_inFlightTTL = ((long) ((cache).dtor_inFlightTTL()));
    }
    LocalCMC_Compile.LocalCMC _nw0 = new LocalCMC_Compile.LocalCMC();
    _nw0.__ctor(((long) ((cache).dtor_entryCapacity())), ((long) (((cache).dtor_entryPruningTailSize()).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.CountingNumber._typeDescriptor(), 1))));
    (this).wrapped = _nw0;
    DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, java.lang.Long> _nw1 = new DafnyLibraries.MutableMap<dafny.DafnySequence<? extends java.lang.Byte>, java.lang.Long>(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.PositiveLong._typeDescriptor());
    (this).inFlight = _nw1;
    (this).gracePeriod = _0_gracePeriod;
    (this).graceInterval = _1_graceInterval;
    (this).fanOut = ((long) ((cache).dtor_fanOut()));
    (this).inFlightTTL = _2_inFlightTTL;
    (this).sleepMilli = ((long) ((cache).dtor_sleepMilli()));
    (this).lastPrune = (long) 0L;
  }
  public boolean FanOutReached(long now)
  {
    boolean res = false;
    (this).PruneInFlight(now);
    res = (this.fanOut) <= (((this.inFlight).Size()).longValue());
    return res;
  }
  public long AddLong(long x, long y)
  {
    if ((x) < ((long) (long) (((StandardLibrary_mUInt_Compile.__default.INT64__MAX__LIMIT()).longValue()) - (y)))) {
      return (long) (long) ((x) + (y));
    } else {
      return (StandardLibrary_mUInt_Compile.__default.INT64__MAX__LIMIT()).longValue();
    }
  }
  public boolean GracePeriod_q(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput result, long now)
  {
    return (((result).dtor_expiryTime()) < ((long) 9223372036854775L)) && (((long) (long) (((long) (long) (((result).dtor_expiryTime()) * ((long) 1000L))) - (this.gracePeriod))) <= (now));
  }
  public CacheState CheckInFlight(dafny.DafnySequence<? extends java.lang.Byte> identifier, software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput result, long now)
  {
    CacheState output = CacheState.Default();
    if(true) {
      boolean _0_fanOutReached;
      boolean _out0;
      _out0 = (this).FanOutReached(now);
      _0_fanOutReached = _out0;
      if (_0_fanOutReached) {
        output = CacheState.create_Full(result);
        return output;
      } else if (!((this).GracePeriod_q(result, now))) {
        output = CacheState.create_Full(result);
        return output;
      } else {
        if ((this.inFlight).HasKey(identifier)) {
          long _1_entry;
          _1_entry = (this.inFlight).Select(identifier);
          if (((this).AddLong(_1_entry, this.graceInterval)) > (now)) {
            output = CacheState.create_Full(result);
            return output;
          }
        }
        (this.inFlight).Put(identifier, now);
        output = CacheState.create_EmptyFetch();
        return output;
      }
    }
    return output;
  }
  public void PruneInFlight(long now)
  {
    if ((((this.inFlight).Size()).longValue()) < (this.fanOut)) {
      return;
    }
    if (((long) (long) ((now) - ((long) 1000L))) < (this.lastPrune)) {
      return;
    }
    (this).lastPrune = now;
    dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_keySet;
    _0_keySet = (this.inFlight).Keys();
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_keys;
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> _out0;
    _out0 = SortedSets.__default.<dafny.DafnySequence<? extends java.lang.Byte>>SetToSequence(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _0_keySet);
    _1_keys = _out0;
    long _hi0 = (long) (_1_keys).cardinalityInt();
    for (long _2_i = (long) 0L; java.lang.Long.compareUnsigned(_2_i, _hi0) < 0; _2_i++) {
      long _3_v;
      _3_v = (this.inFlight).Select(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_1_keys).select(dafny.Helpers.unsignedToInt(_2_i)))));
      if ((now) >= ((this).AddLong(_3_v, this.inFlightTTL))) {
        (this.inFlight).Remove(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_1_keys).select(dafny.Helpers.unsignedToInt(_2_i)))));
      }
    }
  }
  public CacheState CheckNewEntry(dafny.DafnySequence<? extends java.lang.Byte> identifier, long now)
  {
    CacheState output = CacheState.Default();
    boolean _0_fanOutReached;
    boolean _out0;
    _out0 = (this).FanOutReached(now);
    _0_fanOutReached = _out0;
    if (_0_fanOutReached) {
      output = CacheState.create_EmptyWait();
      return output;
    } else if ((this.inFlight).HasKey(identifier)) {
      long _1_entry;
      _1_entry = (this.inFlight).Select(identifier);
      if ((now) < ((this).AddLong(_1_entry, this.graceInterval))) {
        output = CacheState.create_EmptyWait();
        return output;
      }
    }
    (this.inFlight).Put(identifier, now);
    output = CacheState.create_EmptyFetch();
    return output;
  }
  public Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetFromCacheWithTime(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input, long now)
  {
    Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), CacheState.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_result;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this.wrapped).GetCacheEntryWithTime(input, dafny.DafnyEuclidean.EuclideanDivision(now, (long) 1000L));
      _0_result = _out0;
      if ((_0_result).is_Success()) {
        CacheState _1_newResult;
        CacheState _out1;
        _out1 = (this).CheckInFlight((input).dtor_identifier(), (_0_result).dtor_value(), now);
        _1_newResult = _out1;
        output = Wrappers_Compile.Result.<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _1_newResult);
        return output;
      } else if (((_0_result).dtor_error()).is_EntryDoesNotExist()) {
        CacheState _2_newResult;
        CacheState _out2;
        _out2 = (this).CheckNewEntry((input).dtor_identifier(), now);
        _2_newResult = _out2;
        output = Wrappers_Compile.Result.<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _2_newResult);
        return output;
      } else {
        output = Wrappers_Compile.Result.<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_0_result).dtor_error());
        return output;
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetFromCache(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input)
  {
    Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), CacheState.Default());
    if(true) {
      long _0_now;
      long _out0;
      _out0 = Time.__default.CurrentRelativeTimeMilli();
      _0_now = _out0;
      Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = (this).GetFromCacheWithTime(input, _0_now);
      output = _out1;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_result;
      Wrappers_Compile.Result<CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this).GetFromCache(input);
      _0_result = _out0;
      if ((_0_result).is_Failure()) {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_0_result).dtor_error());
        return output;
      } else if (((_0_result).dtor_value()).is_Full()) {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_0_result).dtor_value()).dtor_data());
        return output;
      } else {
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_EntryDoesNotExist(dafny.DafnySequence.asString("Entry does not exist")));
        return output;
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> PutCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      (this.inFlight).Remove((input).dtor_identifier());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this.wrapped).PutCacheEntry_k(input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DeleteCacheEntry(software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      (this.inFlight).Remove((input).dtor_identifier());
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this.wrapped).DeleteCacheEntry_k(input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> UpdateUsageMetadata(software.amazon.cryptography.materialproviders.internaldafny.types.UpdateUsageMetadataInput input)
  {
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (this.wrapped).UpdateUsageMetadata_k(input);
      output = _out0;
    }
    return output;
  }
  private static final dafny.TypeDescriptor<StormTracker> _TYPE = dafny.TypeDescriptor.<StormTracker>referenceWithInitializer(StormTracker.class, () -> (StormTracker) null);
  public static dafny.TypeDescriptor<StormTracker> _typeDescriptor() {
    return (dafny.TypeDescriptor<StormTracker>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "StormTracker.StormTracker";
  }
}
