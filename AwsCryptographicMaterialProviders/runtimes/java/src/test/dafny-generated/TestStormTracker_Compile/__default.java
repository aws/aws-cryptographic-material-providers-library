// Class __default
// Dafny class __default compiled into Java
package TestStormTracker_Compile;

import Fixtures_Compile.*;
import TestCreateKeyStore_Compile.*;
import TestLyingBranchKey_Compile.*;
import TestDiscoveryGetKeys_Compile.*;
import TestConfig_Compile.*;
import TestGetKeys_Compile.*;
import CleanupItems_Compile.*;
import TestCreateKeys_Compile.*;
import TestVersionKey_Compile.*;
import TestUtils_Compile.*;
import TestIntermediateKeyWrapping_Compile.*;
import TestErrorMessages_Compile.*;
import TestDefaultClientProvider_Compile.*;
import TestRawECDHKeyring_Compile.*;
import TestRawAESKeyring_Compile.*;
import TestMultiKeyring_Compile.*;
import TestRawRSAKeying_Compile.*;
import TestAwsKmsRsaKeyring_Compile.*;
import TestAwsKmsHierarchicalKeyring_Compile.*;
import TestAwsKmsEcdhKeyring_Compile.*;
import TestAwsKmsEncryptedDataKeyFilter_Compile.*;
import TestLocalCMC_Compile.*;

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
    dafny.DafnySequence<? extends java.lang.Byte> _1_abc;
    _1_abc = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("abc"));
    dafny.DafnySequence<? extends java.lang.Byte> _2_cde;
    _2_cde = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("cde"));
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_1_abc), (long) 10000L);
    _3_valueOrError0 = _out0;
    if (!(!((_3_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(67,15): " + java.lang.String.valueOf(_3_valueOrError0));
    }
    StormTracker_Compile.CacheState _4_res;
    _4_res = (_3_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(68,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_1_abc), (long) 10000L);
    _5_valueOrError1 = _out1;
    if (!(!((_5_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(69,11): " + java.lang.String.valueOf(_5_valueOrError1));
    }
    _4_res = (_5_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(70,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).PutCacheEntry(__default.MakePut(_1_abc, (long) 10000L));
    _6_valueOrError2 = _out2;
    if (!(!((_6_valueOrError2).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(71,16): " + java.lang.String.valueOf(_6_valueOrError2));
    }
    dafny.Tuple0 _7_res2;
    _7_res2 = (_6_valueOrError2).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).PutCacheEntry(__default.MakePut(_2_cde, (long) 10000L));
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(72,12): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    _7_res2 = (_8_valueOrError3).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_1_abc), (long) 11000L);
    _9_valueOrError4 = _out4;
    if (!(!((_9_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(78,11): " + java.lang.String.valueOf(_9_valueOrError4));
    }
    _4_res = (_9_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(79,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_1_abc), (long) 11000L);
    _10_valueOrError5 = _out5;
    if (!(!((_10_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(80,11): " + java.lang.String.valueOf(_10_valueOrError5));
    }
    _4_res = (_10_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_4_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(81,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_res3;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetCacheEntry(__default.MakeGet(_1_abc));
    _11_res3 = _out6;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_0_st).GetCacheEntry(__default.MakeGet(_1_abc));
    _11_res3 = _out7;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_res4;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_0_st).GetFromCache(__default.MakeGet(_1_abc));
    _12_res4 = _out8;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_0_st).GetFromCache(__default.MakeGet(_1_abc));
    _12_res4 = _out9;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_res5;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = (_0_st).DeleteCacheEntry(__default.MakeDel(_1_abc));
    _13_res5 = _out10;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out11;
    _out11 = (_0_st).DeleteCacheEntry(__default.MakeDel(_1_abc));
    _13_res5 = _out11;
  }
  public static void StormTrackerFanOut()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed8 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let4_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed8));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let4_0, boxed9 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed9));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed10 -> {
          int _pat_let5_0 = ((int)(java.lang.Object)(boxed10));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let5_0, boxed11 -> {
            int _2_dt__update_hfanOut_h0 = ((int)(java.lang.Object)(boxed11));
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
    dafny.DafnySequence<? extends java.lang.Byte> _3_one;
    _3_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    dafny.DafnySequence<? extends java.lang.Byte> _4_two;
    _4_two = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("two"));
    dafny.DafnySequence<? extends java.lang.Byte> _5_three;
    _5_three = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("three"));
    dafny.DafnySequence<? extends java.lang.Byte> _6_four;
    _6_four = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("four"));
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10000L);
    _7_valueOrError0 = _out0;
    if (!(!((_7_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(101,15): " + java.lang.String.valueOf(_7_valueOrError0));
    }
    StormTracker_Compile.CacheState _8_res;
    _8_res = (_7_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(102,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_4_two), (long) 10000L);
    _9_valueOrError1 = _out1;
    if (!(!((_9_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(103,11): " + java.lang.String.valueOf(_9_valueOrError1));
    }
    _8_res = (_9_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(104,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_5_three), (long) 10000L);
    _10_valueOrError2 = _out2;
    if (!(!((_10_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(105,11): " + java.lang.String.valueOf(_10_valueOrError2));
    }
    _8_res = (_10_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(106,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_6_four), (long) 10000L);
    _11_valueOrError3 = _out3;
    if (!(!((_11_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(107,11): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    _8_res = (_11_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_8_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(108,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void StormTrackerPruneTTL()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed12 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let6_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed12));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let6_0, boxed13 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed13));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(5, boxed14 -> {
          int _pat_let7_0 = ((int)(java.lang.Object)(boxed14));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let7_0, boxed15 -> {
            int _2_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed15));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed16 -> {
              int _pat_let8_0 = ((int)(java.lang.Object)(boxed16));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let8_0, boxed17 -> {
                int _3_dt__update_hfanOut_h0 = ((int)(java.lang.Object)(boxed17));
                return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed18 -> {
                  int _pat_let9_0 = ((int)(java.lang.Object)(boxed18));
                  return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let9_0, boxed19 -> {
                    int _4_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed19));
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
    dafny.DafnySequence<? extends java.lang.Byte> _5_one;
    _5_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    dafny.DafnySequence<? extends java.lang.Byte> _6_two;
    _6_two = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("two"));
    dafny.DafnySequence<? extends java.lang.Byte> _7_three;
    _7_three = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("three"));
    dafny.DafnySequence<? extends java.lang.Byte> _8_four;
    _8_four = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("four"));
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_5_one), (long) 10000L);
    _9_valueOrError0 = _out0;
    if (!(!((_9_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(120,15): " + java.lang.String.valueOf(_9_valueOrError0));
    }
    StormTracker_Compile.CacheState _10_res;
    _10_res = (_9_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(121,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_6_two), (long) 10000L);
    _11_valueOrError1 = _out1;
    if (!(!((_11_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(122,11): " + java.lang.String.valueOf(_11_valueOrError1));
    }
    _10_res = (_11_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(123,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_7_three), (long) 10000L);
    _12_valueOrError2 = _out2;
    if (!(!((_12_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(124,11): " + java.lang.String.valueOf(_12_valueOrError2));
    }
    _10_res = (_12_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(125,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_8_four), (long) 10000L);
    _13_valueOrError3 = _out3;
    if (!(!((_13_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(126,11): " + java.lang.String.valueOf(_13_valueOrError3));
    }
    _10_res = (_13_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(127,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_8_four), (long) 10001L);
    _14_valueOrError4 = _out4;
    if (!(!((_14_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(128,11): " + java.lang.String.valueOf(_14_valueOrError4));
    }
    _10_res = (_14_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(129,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_8_four), (long) 10003L);
    _15_valueOrError5 = _out5;
    if (!(!((_15_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(130,11): " + java.lang.String.valueOf(_15_valueOrError5));
    }
    _10_res = (_15_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(131,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError6 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_8_four), (long) 11000L);
    _16_valueOrError6 = _out6;
    if (!(!((_16_valueOrError6).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(135,11): " + java.lang.String.valueOf(_16_valueOrError6));
    }
    _10_res = (_16_valueOrError6).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_10_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(136,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void StormTrackerGraceInterval()
  {
    StormTracker_Compile.StormTracker _0_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed20 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let10_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed20));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let10_0, boxed21 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed21));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed22 -> {
          int _pat_let11_0 = ((int)(java.lang.Object)(boxed22));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let11_0, boxed23 -> {
            int _2_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed23));
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
    dafny.DafnySequence<? extends java.lang.Byte> _3_one;
    _3_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10000L);
    _4_valueOrError0 = _out0;
    if (!(!((_4_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(145,15): " + java.lang.String.valueOf(_4_valueOrError0));
    }
    StormTracker_Compile.CacheState _5_res;
    _5_res = (_4_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(146,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10000L);
    _6_valueOrError1 = _out1;
    if (!(!((_6_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(147,11): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    _5_res = (_6_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(148,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10001L);
    _7_valueOrError2 = _out2;
    if (!(!((_7_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(149,11): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    _5_res = (_7_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(150,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10002L);
    _8_valueOrError3 = _out3;
    if (!(!((_8_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(151,11): " + java.lang.String.valueOf(_8_valueOrError3));
    }
    _5_res = (_8_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(152,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetFromCacheWithTime(__default.MakeGet(_3_one), (long) 10003L);
    _9_valueOrError4 = _out4;
    if (!(!((_9_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(153,11): " + java.lang.String.valueOf(_9_valueOrError4));
    }
    _5_res = (_9_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_5_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(154,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void FullStormTrackerGraceInterval()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_one;
    _0_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    StormTracker_Compile.StormTracker _1_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed24 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let12_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed24));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let12_0, boxed25 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _2_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed25));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(5, boxed26 -> {
          int _pat_let13_0 = ((int)(java.lang.Object)(boxed26));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let13_0, boxed27 -> {
            int _3_dt__update_hgracePeriod_h0 = ((int)(java.lang.Object)(boxed27));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed28 -> {
              int _pat_let14_0 = ((int)(java.lang.Object)(boxed28));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let14_0, boxed29 -> {
                int _4_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed29));
                return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(2, boxed30 -> {
                  int _pat_let15_0 = ((int)(java.lang.Object)(boxed30));
                  return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let15_0, boxed31 -> {
                    int _5_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed31));
                    return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_2_dt__update__tmp_h0).dtor_entryCapacity(), (_2_dt__update__tmp_h0).dtor_entryPruningTailSize(), _3_dt__update_hgracePeriod_h0, _5_dt__update_hgraceInterval_h0, (_2_dt__update__tmp_h0).dtor_fanOut(), _4_dt__update_hinFlightTTL_h0, (_2_dt__update__tmp_h0).dtor_sleepMilli(), (_2_dt__update__tmp_h0).dtor_timeUnits());
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
    _1_st = _nw0;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_1_st).PutCacheEntry(__default.MakePut(_0_one, (long) 10000L));
    _6_valueOrError0 = _out0;
    if (!(!((_6_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(166,13): " + java.lang.String.valueOf(_6_valueOrError0));
    }
    dafny.Tuple0 _7___v0;
    _7___v0 = (_6_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 5L)));
    _8_valueOrError1 = _out1;
    if (!(!((_8_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(168,15): " + java.lang.String.valueOf(_8_valueOrError1));
    }
    StormTracker_Compile.CacheState _9_res;
    _9_res = (_8_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(169,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 5L)));
    _10_valueOrError2 = _out2;
    if (!(!((_10_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(170,11): " + java.lang.String.valueOf(_10_valueOrError2));
    }
    _9_res = (_10_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(171,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 4L)));
    _11_valueOrError3 = _out3;
    if (!(!((_11_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(172,11): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    _9_res = (_11_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(173,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 3L)));
    _12_valueOrError4 = _out4;
    if (!(!((_12_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(174,11): " + java.lang.String.valueOf(_12_valueOrError4));
    }
    _9_res = (_12_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(175,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 2L)));
    _13_valueOrError5 = _out5;
    if (!(!((_13_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(176,11): " + java.lang.String.valueOf(_13_valueOrError5));
    }
    _9_res = (_13_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(177,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError6 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 1L)));
    _14_valueOrError6 = _out6;
    if (!(!((_14_valueOrError6).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(178,11): " + java.lang.String.valueOf(_14_valueOrError6));
    }
    _9_res = (_14_valueOrError6).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(179,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError7 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 1L)));
    _15_valueOrError7 = _out7;
    if (!(!((_15_valueOrError7).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(180,11): " + java.lang.String.valueOf(_15_valueOrError7));
    }
    _9_res = (_15_valueOrError7).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(181,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _16_valueOrError8 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) - ((long) 0L)));
    _16_valueOrError8 = _out8;
    if (!(!((_16_valueOrError8).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(182,11): " + java.lang.String.valueOf(_16_valueOrError8));
    }
    _9_res = (_16_valueOrError8).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(184,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError9 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) (long) (((long) 11000L) + ((long) 1L)));
    _17_valueOrError9 = _out9;
    if (!(!((_17_valueOrError9).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(185,11): " + java.lang.String.valueOf(_17_valueOrError9));
    }
    _9_res = (_17_valueOrError9).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(187,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
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
    dafny.DafnySequence<? extends java.lang.Byte> _5_one;
    _5_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_4_st).PutCacheEntry(__default.MakePut(_5_one, _1_expiryTime));
    _6_valueOrError0 = _out0;
    if (!(!((_6_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(204,16): " + java.lang.String.valueOf(_6_valueOrError0));
    }
    dafny.Tuple0 _7_res2;
    _7_res2 = (_6_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_4_st).GetFromCacheWithTime(__default.MakeGet(_5_one), _2_beforeGracePeriod);
    _8_valueOrError1 = _out1;
    if (!(!((_8_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(206,15): " + java.lang.String.valueOf(_8_valueOrError1));
    }
    StormTracker_Compile.CacheState _9_res;
    _9_res = (_8_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(207,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_4_st).GetFromCacheWithTime(__default.MakeGet(_5_one), _3_insideGracePeriod);
    _10_valueOrError2 = _out2;
    if (!(!((_10_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(208,11): " + java.lang.String.valueOf(_10_valueOrError2));
    }
    _9_res = (_10_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(209,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_4_st).GetFromCacheWithTime(__default.MakeGet(_5_one), _3_insideGracePeriod);
    _11_valueOrError3 = _out3;
    if (!(!((_11_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(210,11): " + java.lang.String.valueOf(_11_valueOrError3));
    }
    _9_res = (_11_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_9_res).is_Full())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(211,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static void EmptyStormTrackerTLLAndInterval()
  {
    dafny.DafnySequence<? extends java.lang.Byte> _0_one;
    _0_one = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("one"));
    StormTracker_Compile.StormTracker _1_st;
    StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
    _nw0.__ctor(((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(StormTracker_Compile.__default.DefaultStorm(), boxed32 -> {
      software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _pat_let16_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed32));
      return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let16_0, boxed33 -> {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _2_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(boxed33));
        return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(3, boxed34 -> {
          int _pat_let17_0 = ((int)(java.lang.Object)(boxed34));
          return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let17_0, boxed35 -> {
            int _3_dt__update_hinFlightTTL_h0 = ((int)(java.lang.Object)(boxed35));
            return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(2, boxed36 -> {
              int _pat_let18_0 = ((int)(java.lang.Object)(boxed36));
              return ((software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache)(java.lang.Object)(dafny.Helpers.<java.lang.Integer, software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache>Let(_pat_let18_0, boxed37 -> {
                int _4_dt__update_hgraceInterval_h0 = ((int)(java.lang.Object)(boxed37));
                return software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_2_dt__update__tmp_h0).dtor_entryCapacity(), (_2_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_2_dt__update__tmp_h0).dtor_gracePeriod(), _4_dt__update_hgraceInterval_h0, (_2_dt__update__tmp_h0).dtor_fanOut(), _3_dt__update_hinFlightTTL_h0, (_2_dt__update__tmp_h0).dtor_sleepMilli(), (_2_dt__update__tmp_h0).dtor_timeUnits());
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
    _1_st = _nw0;
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError0 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10000L);
    _5_valueOrError0 = _out0;
    if (!(!((_5_valueOrError0).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(223,15): " + java.lang.String.valueOf(_5_valueOrError0));
    }
    StormTracker_Compile.CacheState _6_res;
    _6_res = (_5_valueOrError0).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(224,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10000L);
    _7_valueOrError1 = _out1;
    if (!(!((_7_valueOrError1).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(225,11): " + java.lang.String.valueOf(_7_valueOrError1));
    }
    _6_res = (_7_valueOrError1).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(226,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10001L);
    _8_valueOrError2 = _out2;
    if (!(!((_8_valueOrError2).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(227,11): " + java.lang.String.valueOf(_8_valueOrError2));
    }
    _6_res = (_8_valueOrError2).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(228,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10002L);
    _9_valueOrError3 = _out3;
    if (!(!((_9_valueOrError3).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(229,11): " + java.lang.String.valueOf(_9_valueOrError3));
    }
    _6_res = (_9_valueOrError3).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyFetch())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(230,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10002L);
    _10_valueOrError4 = _out4;
    if (!(!((_10_valueOrError4).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(231,11): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    _6_res = (_10_valueOrError4).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(232,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = Wrappers_Compile.Result.<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), StormTracker_Compile.CacheState.Default());
    Wrappers_Compile.Result<StormTracker_Compile.CacheState, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_1_st).GetFromCacheWithTime(__default.MakeGet(_0_one), (long) 10003L);
    _11_valueOrError5 = _out5;
    if (!(!((_11_valueOrError5).IsFailure(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(233,11): " + java.lang.String.valueOf(_11_valueOrError5));
    }
    _6_res = (_11_valueOrError5).Extract(StormTracker_Compile.CacheState._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if (!((_6_res).is_EmptyWait())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/StormTracker.dfy(234,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  @Override
  public java.lang.String toString() {
    return "TestStormTracker._default";
  }
}
