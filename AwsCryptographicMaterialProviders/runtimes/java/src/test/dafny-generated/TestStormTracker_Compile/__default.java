// Class __default
// Dafny class __default compiled into Java
package TestStormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Materials MakeMat(dafny.DafnySequence<? extends java.lang.Byte> data) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Materials.create_BranchKey(software.amazon.cryptography.keystore.internaldafny.types.BranchKeyMaterials.create(dafny.DafnySequence.asString("spoo"), data, dafny.DafnyMap.fromElements(), data));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput MakeGet(dafny.DafnySequence<? extends java.lang.Byte> data) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryInput.create(data, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput MakeDel(dafny.DafnySequence<? extends java.lang.Byte> data) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.DeleteCacheEntryInput.create(data);
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput MakePut(dafny.DafnySequence<? extends java.lang.Byte> data, long expiryTime)
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput.create(data, __default.MakeMat(data), (long) 123456789L, dafny.DafnyEuclidean.EuclideanDivision(expiryTime, (long) 1000L), Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput MakeGetOutput(dafny.DafnySequence<? extends java.lang.Byte> data, long expiryTime)
  {
    return software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput.create(__default.MakeMat(data), (long) 123456789L, dafny.DafnyEuclidean.EuclideanDivision(expiryTime, (long) 1000L), 1, 0);
  }
  public static void StormTrackerBasics()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(StormTracker_Compile.__default.DefaultStorm());
    _0_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.abc()), (long) 10000L);
    _1_valueOrError0 = _out0;
    if (!(!((_1_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(96,15): " + java.lang.String.valueOf(_1_valueOrError0));
    }
    StormTracker_Compile.CacheState _2_res;
    _2_res = (_1_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_2_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(97,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.abc()), (long) 10000L);
    _3_valueOrError1 = _out1;
    if (!(!((_3_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(98,11): " + java.lang.String.valueOf(_3_valueOrError1));
    }
    _2_res = (_3_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_2_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(99,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).PutCacheEntry(__default.MakePut(__default.abc(), (long) 10000L));
    _4_valueOrError2 = _out2;
    if (!(!((_4_valueOrError2).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(100,16): " + java.lang.String.valueOf(_4_valueOrError2));
    }
    dafny.Tuple0 _5_res2;
    _5_res2 = (_4_valueOrError2).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).PutCacheEntry(__default.MakePut(__default.cde(), (long) 10000L));
    _6_valueOrError3 = _out3;
    if (!(!((_6_valueOrError3).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(101,12): " + java.lang.String.valueOf(_6_valueOrError3));
    }
    _5_res2 = (_6_valueOrError3).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.abc()), (long) 11000L);
    _7_valueOrError4 = _out4;
    if (!(!((_7_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + java.lang.String.valueOf(_7_valueOrError4));
    }
    _2_res = (_7_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_2_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.abc()), (long) 11000L);
    _8_valueOrError5 = _out5;
    if (!(!((_8_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(109,11): " + java.lang.String.valueOf(_8_valueOrError5));
    }
    _2_res = (_8_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_2_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(110,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_res3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetCacheEntry(__default.MakeGet(__default.abc()));
    _9_res3 = _out6;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_0_st).GetCacheEntry(__default.MakeGet(__default.abc()));
    _9_res3 = _out7;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_res4;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_0_st).GetFromCache(__default.MakeGet(__default.abc()));
    _10_res4 = _out8;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_0_st).GetFromCache(__default.MakeGet(__default.abc()));
    _10_res4 = _out9;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_res5;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_0_st).DeleteCacheEntry(__default.MakeDel(__default.abc()));
    _11_res5 = _out10;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_0_st).DeleteCacheEntry(__default.MakeDel(__default.abc()));
    _11_res5 = _out11;
  }
  public static void StormTrackerFanOut()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed10 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let5_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed10));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let5_0, boxed11 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed11));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed12 -> {
          int _pat_let6_0 = ((int)(java.lang.Object)(boxed12));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let6_0, boxed13 -> {
            int _2_dt__update_hfanOut_h0 = ((int)(java.lang.Object)(boxed13));
            return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_1_dt__update__tmp_h0).dtor_entryCapacity(), (_1_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).dtor_gracePeriod(), (_1_dt__update__tmp_h0).dtor_graceInterval(), _2_dt__update_hfanOut_h0, (_1_dt__update__tmp_h0).dtor_inFlightTTL(), (_1_dt__update__tmp_h0).dtor_sleepMilli(), (_1_dt__update__tmp_h0).dtor_timeUnits());
          }
          )));
        }
        )));
      }
      )));
    }
    ))));
    _0_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _3_valueOrError0 = _out0;
    if (!(!((_3_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(124,15): " + java.lang.String.valueOf(_3_valueOrError0));
    }
    StormTracker_Compile.CacheState _4_res;
    _4_res = (_3_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.two()), (long) 10000L);
    _5_valueOrError1 = _out1;
    if (!(!((_5_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,11): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    _4_res = (_5_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.three()), (long) 10000L);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,11): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    _4_res = (_6_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.four()), (long) 10000L);
    _7_valueOrError3 = _out3;
    if (!(!((_7_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,11): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    _4_res = (_7_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void StormTrackerPruneTTL()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed14 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let7_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed14));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let7_0, boxed15 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed15));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(5, boxed16 -> {
          int _pat_let8_0 = ((int)(java.lang.Object)(boxed16));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let8_0, boxed17 -> {
            int _2_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed17));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed18 -> {
              int _pat_let9_0 = ((int)(java.lang.Object)(boxed18));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let9_0, boxed19 -> {
                int _3_dt__update_hfanOut_h0 = ((int)(java.lang.Object)(boxed19));
                return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed20 -> {
                  int _pat_let10_0 = ((int)(java.lang.Object)(boxed20));
                  return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let10_0, boxed21 -> {
                    int _4_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed21));
                    return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_1_dt__update__tmp_h0).dtor_entryCapacity(), (_1_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).dtor_gracePeriod(), _4_dt__update_hgraceInterval_h0, _3_dt__update_hfanOut_h0, _2_dt__update_hinFlightTTL_h0, (_1_dt__update__tmp_h0).dtor_sleepMilli(), (_1_dt__update__tmp_h0).dtor_timeUnits());
                  }
                  )));
                }
                )));
              }
              )));
            }
            )));
          }
          )));
        }
        )));
      }
      )));
    }
    ))));
    _0_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _5_valueOrError0 = _out0;
    if (!(!((_5_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(137,15): " + java.lang.String.valueOf(_5_valueOrError0));
    }
    StormTracker_Compile.CacheState _6_res;
    _6_res = (_5_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(138,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.two()), (long) 10000L);
    _7_valueOrError1 = _out1;
    if (!(!((_7_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(139,11): " + java.lang.String.valueOf(_7_valueOrError1));
    }
    _6_res = (_7_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(140,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.three()), (long) 10000L);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(141,11): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    _6_res = (_8_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(142,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.four()), (long) 10000L);
    _9_valueOrError3 = _out3;
    if (!(!((_9_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(143,11): " + java.lang.String.valueOf(_9_valueOrError3));
    }
    _6_res = (_9_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(144,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.four()), (long) 10001L);
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,11): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    _6_res = (_10_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.four()), (long) 10003L);
    _11_valueOrError5 = _out5;
    if (!(!((_11_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + java.lang.String.valueOf(_11_valueOrError5));
    }
    _6_res = (_11_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError6 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.four()), (long) 11000L);
    _12_valueOrError6 = _out6;
    if (!(!((_12_valueOrError6).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(152,11): " + java.lang.String.valueOf(_12_valueOrError6));
    }
    _6_res = (_12_valueOrError6).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(153,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void StormTrackerGraceInterval()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed22 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let11_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed22));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let11_0, boxed23 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed23));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed24 -> {
          int _pat_let12_0 = ((int)(java.lang.Object)(boxed24));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let12_0, boxed25 -> {
            int _2_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed25));
            return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_1_dt__update__tmp_h0).dtor_entryCapacity(), (_1_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).dtor_gracePeriod(), _2_dt__update_hgraceInterval_h0, (_1_dt__update__tmp_h0).dtor_fanOut(), (_1_dt__update__tmp_h0).dtor_inFlightTTL(), (_1_dt__update__tmp_h0).dtor_sleepMilli(), (_1_dt__update__tmp_h0).dtor_timeUnits());
          }
          )));
        }
        )));
      }
      )));
    }
    ))));
    _0_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _3_valueOrError0 = _out0;
    if (!(!((_3_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(159,15): " + java.lang.String.valueOf(_3_valueOrError0));
    }
    StormTracker_Compile.CacheState _4_res;
    _4_res = (_3_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(160,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _5_valueOrError1 = _out1;
    if (!(!((_5_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(161,11): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    _4_res = (_5_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(162,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10001L);
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(163,11): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    _4_res = (_6_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(164,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10002L);
    _7_valueOrError3 = _out3;
    if (!(!((_7_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(165,11): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    _4_res = (_7_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(166,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10003L);
    _8_valueOrError4 = _out4;
    if (!(!((_8_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(167,11): " + java.lang.String.valueOf(_8_valueOrError4));
    }
    _4_res = (_8_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(168,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void FullStormTrackerGraceInterval()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed26 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let13_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed26));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let13_0, boxed27 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed27));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(5, boxed28 -> {
          int _pat_let14_0 = ((int)(java.lang.Object)(boxed28));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let14_0, boxed29 -> {
            int _2_dt__update_hgracePeriod_h0 = ((int)(java.lang.Object)(boxed29));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed30 -> {
              int _pat_let15_0 = ((int)(java.lang.Object)(boxed30));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let15_0, boxed31 -> {
                int _3_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed31));
                return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(2, boxed32 -> {
                  int _pat_let16_0 = ((int)(java.lang.Object)(boxed32));
                  return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let16_0, boxed33 -> {
                    int _4_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed33));
                    return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_1_dt__update__tmp_h0).dtor_entryCapacity(), (_1_dt__update__tmp_h0).dtor_entryPruningTailSize(), _2_dt__update_hgracePeriod_h0, _4_dt__update_hgraceInterval_h0, (_1_dt__update__tmp_h0).dtor_fanOut(), _3_dt__update_hinFlightTTL_h0, (_1_dt__update__tmp_h0).dtor_sleepMilli(), (_1_dt__update__tmp_h0).dtor_timeUnits());
                  }
                  )));
                }
                )));
              }
              )));
            }
            )));
          }
          )));
        }
        )));
      }
      )));
    }
    ))));
    _0_st = _nw0;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).PutCacheEntry(__default.MakePut(__default.one(), (long) 10000L));
    _5_valueOrError0 = _out0;
    if (!(!((_5_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(178,13): " + java.lang.String.valueOf(_5_valueOrError0));
    }
    dafny.Tuple0 _6___v0;
    _6___v0 = (_5_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 5L)));
    _7_valueOrError1 = _out1;
    if (!(!((_7_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(180,15): " + java.lang.String.valueOf(_7_valueOrError1));
    }
    StormTracker_Compile.CacheState _8_res;
    _8_res = (_7_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(181,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 5L)));
    _9_valueOrError2 = _out2;
    if (!(!((_9_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(182,11): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    _8_res = (_9_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(183,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 4L)));
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(184,11): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    _8_res = (_10_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(185,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 3L)));
    _11_valueOrError4 = _out4;
    if (!(!((_11_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(186,11): " + java.lang.String.valueOf(_11_valueOrError4));
    }
    _8_res = (_11_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(187,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 2L)));
    _12_valueOrError5 = _out5;
    if (!(!((_12_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(188,11): " + java.lang.String.valueOf(_12_valueOrError5));
    }
    _8_res = (_12_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(189,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError6 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 1L)));
    _13_valueOrError6 = _out6;
    if (!(!((_13_valueOrError6).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(190,11): " + java.lang.String.valueOf(_13_valueOrError6));
    }
    _8_res = (_13_valueOrError6).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(191,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError7 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 1L)));
    _14_valueOrError7 = _out7;
    if (!(!((_14_valueOrError7).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(192,11): " + java.lang.String.valueOf(_14_valueOrError7));
    }
    _8_res = (_14_valueOrError7).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(193,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError8 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) - ((long) 0L)));
    _15_valueOrError8 = _out8;
    if (!(!((_15_valueOrError8).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(194,11): " + java.lang.String.valueOf(_15_valueOrError8));
    }
    _8_res = (_15_valueOrError8).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(196,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError9 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) (long) (((long) 11000L) + ((long) 1L)));
    _16_valueOrError9 = _out9;
    if (!(!((_16_valueOrError9).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(197,11): " + java.lang.String.valueOf(_16_valueOrError9));
    }
    _8_res = (_16_valueOrError9).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(199,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void StormTrackerGracePeriod()
  {
    software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _0_config;
    _0_config = StormTracker_Compile.__default.DefaultStorm();
    long _1_expiryTime;
    _1_expiryTime = (long) 100100L;
    long _2_beforeGracePeriod;
    _2_beforeGracePeriod = (long) (long) (((long) (long) ((_1_expiryTime) - (((long) ((_0_config).dtor_gracePeriod()))))) - ((long) 1000L));
    long _3_insideGracePeriod;
    _3_insideGracePeriod = (long) (long) (((long) (long) ((_1_expiryTime) - (((long) ((_0_config).dtor_gracePeriod()))))) + ((long) 1L));
    StormTracker_Compile.StormTracker _4_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(_0_config);
    _4_st = _nw0;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_4_st).PutCacheEntry(__default.MakePut(__default.one(), _1_expiryTime));
    _5_valueOrError0 = _out0;
    if (!(!((_5_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(214,16): " + java.lang.String.valueOf(_5_valueOrError0));
    }
    dafny.Tuple0 _6_res2;
    _6_res2 = (_5_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_4_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), _2_beforeGracePeriod);
    _7_valueOrError1 = _out1;
    if (!(!((_7_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(216,15): " + java.lang.String.valueOf(_7_valueOrError1));
    }
    StormTracker_Compile.CacheState _8_res;
    _8_res = (_7_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(217,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_4_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), _3_insideGracePeriod);
    _9_valueOrError2 = _out2;
    if (!(!((_9_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(218,11): " + java.lang.String.valueOf(_9_valueOrError2));
    }
    _8_res = (_9_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(219,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_4_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), _3_insideGracePeriod);
    _10_valueOrError3 = _out3;
    if (!(!((_10_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(220,11): " + java.lang.String.valueOf(_10_valueOrError3));
    }
    _8_res = (_10_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(221,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void EmptyStormTrackerTLLAndInterval()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed34 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let17_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed34));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let17_0, boxed35 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed35));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed36 -> {
          int _pat_let18_0 = ((int)(java.lang.Object)(boxed36));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let18_0, boxed37 -> {
            int _2_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed37));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(2, boxed38 -> {
              int _pat_let19_0 = ((int)(java.lang.Object)(boxed38));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let19_0, boxed39 -> {
                int _3_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed39));
                return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_1_dt__update__tmp_h0).dtor_entryCapacity(), (_1_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_1_dt__update__tmp_h0).dtor_gracePeriod(), _3_dt__update_hgraceInterval_h0, (_1_dt__update__tmp_h0).dtor_fanOut(), _2_dt__update_hinFlightTTL_h0, (_1_dt__update__tmp_h0).dtor_sleepMilli(), (_1_dt__update__tmp_h0).dtor_timeUnits());
              }
              )));
            }
            )));
          }
          )));
        }
        )));
      }
      )));
    }
    ))));
    _0_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _4_valueOrError0 = _out0;
    if (!(!((_4_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(232,15): " + java.lang.String.valueOf(_4_valueOrError0));
    }
    StormTracker_Compile.CacheState _5_res;
    _5_res = (_4_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(233,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10000L);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(234,11): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    _5_res = (_6_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(235,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10001L);
    _7_valueOrError2 = _out2;
    if (!(!((_7_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(236,11): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    _5_res = (_7_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(237,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10002L);
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(238,11): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    _5_res = (_8_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(239,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10002L);
    _9_valueOrError4 = _out4;
    if (!(!((_9_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(240,11): " + java.lang.String.valueOf(_9_valueOrError4));
    }
    _5_res = (_9_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(241,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(__default.one()), (long) 10003L);
    _10_valueOrError5 = _out5;
    if (!(!((_10_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(242,11): " + java.lang.String.valueOf(_10_valueOrError5));
    }
    _5_res = (_10_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(243,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> abc()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 97, (byte) 98, (byte) 99);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> cde()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 99, (byte) 100, (byte) 101);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> one()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 111, (byte) 110, (byte) 101);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> two()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 116, (byte) 119, (byte) 111);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> three()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 116, (byte) 104, (byte) 114, (byte) 101, (byte) 101);
    return _0_s;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> four()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_s = dafny.DafnySequence.<java.lang.Byte> of((byte) 102, (byte) 111, (byte) 117, (byte) 114);
    return _0_s;
  }
  @Override
  public java.lang.String toString() {
    return "TestStormTracker._default";
  }
}
