// Class __default
// Dafny class __default compiled into Java
package TestLocalCMC_Compile;

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
    _nw0.__ctor(java.math.BigInteger.valueOf(100L), java.math.BigInteger.ONE);
    _0_st = _nw0;
    dafny.DafnySequence<? extends java.lang.Byte> _1_abc;
    _1_abc = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("abc"));
    dafny.DafnySequence<? extends java.lang.Byte> _2_cde;
    _2_cde = UTF8.__default.EncodeAscii(dafny.DafnySequence.asString("cde"));
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_res;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_1_abc), (long) 10000L);
    _3_res = _out0;
    if (!((_3_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(56,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_3_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(57,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = (_0_st).PutCacheEntry_k(__default.MakePut(_1_abc, (long) 10000L));
    _4_valueOrError0 = _out1;
    if (!(!((_4_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(59,16): " + java.lang.String.valueOf(_4_valueOrError0));
    }
    dafny.Tuple0 _5_res2;
    _5_res2 = (_4_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = (_0_st).PutCacheEntry_k(__default.MakePut(_2_cde, (long) 10000L));
    _6_valueOrError1 = _out2;
    if (!(!((_6_valueOrError1).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(60,12): " + java.lang.String.valueOf(_6_valueOrError1));
    }
    _5_res2 = (_6_valueOrError1).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_1_abc), (long) 9999L);
    _7_valueOrError2 = _out3;
    if (!(!((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(62,16): " + java.lang.String.valueOf(_7_valueOrError2));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput _8_res3;
    _8_res3 = (_7_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_1_abc), (long) 10000L);
    _9_valueOrError3 = _out4;
    if (!(!((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(63,12): " + java.lang.String.valueOf(_9_valueOrError3));
    }
    _8_res3 = (_9_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_1_abc), (long) 10001L);
    _3_res = _out5;
    if (!((_3_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(65,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_3_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(66,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_2_cde), (long) 9999L);
    _10_valueOrError4 = _out6;
    if (!(!((_10_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(68,12): " + java.lang.String.valueOf(_10_valueOrError4));
    }
    _8_res3 = (_10_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
    _out7 = (_0_st).DeleteCacheEntry_k(__default.MakeDel(_2_cde));
    _11_valueOrError5 = _out7;
    if (!(!((_11_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(69,16): " + java.lang.String.valueOf(_11_valueOrError5));
    }
    dafny.Tuple0 _12_res5;
    _12_res5 = (_11_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out8;
    _out8 = (_0_st).GetCacheEntryWithTime(__default.MakeGet(_1_abc), (long) 9999L);
    _3_res = _out8;
    if (!((_3_res).is_Failure())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(71,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    if (!(((_3_res).dtor_error()).is_EntryDoesNotExist())) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(72,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError6 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out9;
    _out9 = (_0_st).DeleteCacheEntry_k(__default.MakeDel(_2_cde));
    _13_valueOrError6 = _out9;
    if (!(!((_13_valueOrError6).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())))) {
      throw new dafny.DafnyHaltException("dafny/AwsCryptographicMaterialProviders/test/CMCs/LocalCMC.dfy(73,12): " + java.lang.String.valueOf(_13_valueOrError6));
    }
    _12_res5 = (_13_valueOrError6).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
  }
  @Override
  public java.lang.String toString() {
    return "TestLocalCMC._default";
  }
}
