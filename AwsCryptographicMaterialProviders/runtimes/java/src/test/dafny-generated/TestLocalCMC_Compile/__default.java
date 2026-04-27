// Class __default
// Dafny class __default compiled into Java
package TestLocalCMC_Compile;

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
    return software.amazon.cryptography.materialproviders.internaldafny.types.PutCacheEntryInput.create(data, __default.MakeMat(data), (long) 123456789L, expiryTime, Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.PositiveInteger._typeDescriptor()));
  }
  public static void LocalCMCBasics()
  {
    LocalCMC_Compile.LocalCMC _0_st;
    LocalCMC_Compile.LocalCMC _nw0 = new LocalCMC_Compile.LocalCMC();
    _nw0.__ctor((long) 100L, (long) 1L);
    _0_st = _nw0;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_res;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.abc()), (long) 10000L);
    _1_res = _out0;
    if (!((_1_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(64,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_1_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).PutCacheEntry_k(__default.MakePut(__default.abc(), (long) 10000L));
    _2_valueOrError0 = _out1;
    if (!(!((_2_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(67,16): " + java.lang.String.valueOf(_2_valueOrError0));
    }
    dafny.Tuple0 _3_res2;
    _3_res2 = (_2_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).PutCacheEntry_k(__default.MakePut(__default.cde(), (long) 10000L));
    _4_valueOrError1 = _out2;
    if (!(!((_4_valueOrError1).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,12): " + java.lang.String.valueOf(_4_valueOrError1));
    }
    _3_res2 = (_4_valueOrError1).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.abc()), (long) 9999L);
    _5_valueOrError2 = _out3;
    if (!(!((_5_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(70,16): " + java.lang.String.valueOf(_5_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput _6_res3;
    _6_res3 = (_5_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.abc()), (long) 10000L);
    _7_valueOrError3 = _out4;
    if (!(!((_7_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,12): " + java.lang.String.valueOf(_7_valueOrError3));
    }
    _6_res3 = (_7_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.abc()), (long) 10001L);
    _1_res = _out5;
    if (!((_1_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_1_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(74,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.cde()), (long) 9999L);
    _8_valueOrError4 = _out6;
    if (!(!((_8_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(76,12): " + java.lang.String.valueOf(_8_valueOrError4));
    }
    _6_res3 = (_8_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_0_st).DeleteCacheEntry_k(__default.MakeDel(__default.cde()));
    _9_valueOrError5 = _out7;
    if (!(!((_9_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(77,16): " + java.lang.String.valueOf(_9_valueOrError5));
    }
    dafny.Tuple0 _10_res5;
    _10_res5 = (_9_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(__default.abc()), (long) 9999L);
    _1_res = _out8;
    if (!((_1_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(79,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_1_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(80,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError6 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_0_st).DeleteCacheEntry_k(__default.MakeDel(__default.cde()));
    _11_valueOrError6 = _out9;
    if (!(!((_11_valueOrError6).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(81,12): " + java.lang.String.valueOf(_11_valueOrError6));
    }
    _10_res5 = (_11_valueOrError6).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
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
  @Override
  public java.lang.String toString() {
    return "TestLocalCMC._default";
  }
}
