// Class __default
// Dafny class __default compiled into Java
package TestManifests_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends Character> LogFileName() {
    if (((OsLang.__default.GetOsShort()).equals(dafny.DafnySequence.asString("Windows"))) && ((OsLang.__default.GetLanguageShort()).equals(dafny.DafnySequence.asString("Dotnet")))) {
      return dafny.DafnySequence.asString("..\\..\\PerfLog.txt");
    } else {
      return dafny.DafnySequence.asString("../../PerfLog.txt");
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> StartEncrypt(MplManifestOptions_Compile.ManifestOptions op)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    if(true) {
      Time.AbsoluteTime _0_time;
      Time.AbsoluteTime _out0;
      _out0 = Time.__default.GetAbsoluteTime();
      _0_time = _out0;
      Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = (Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>>)null;
      Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> _out1;
      _out1 = __default.GetManifest((op).dtor_manifestPath(), dafny.DafnySequence.asString("manifest.json"));
      _1_valueOrError0 = _out1;
      if ((_1_valueOrError0).IsFailure(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_1_valueOrError0).<dafny.Tuple0>PropagateFailure(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      ManifestData _2_encryptManifest;
      _2_encryptManifest = (_1_valueOrError0).Extract(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _3_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_2_encryptManifest).is_EncryptManifest(), dafny.DafnySequence.asString("Not a encrypt manifest"));
      if ((_3_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_3_valueOrError1).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.EncryptTestVector>_typeDescriptor(TestVectors_Compile.EncryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.EncryptTestVector> empty(TestVectors_Compile.EncryptTestVector._typeDescriptor()));
      _4_valueOrError2 = ParseJsonManifests_Compile.__default.BuildEncryptTestVector((_2_encryptManifest).dtor_keys(), (_2_encryptManifest).dtor_jsonTests());
      if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<TestVectors_Compile.EncryptTestVector>_typeDescriptor(TestVectors_Compile.EncryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_4_valueOrError2).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<TestVectors_Compile.EncryptTestVector>_typeDescriptor(TestVectors_Compile.EncryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector> _5_encryptVectors;
      _5_encryptVectors = (_4_valueOrError2).Extract(dafny.DafnySequence.<TestVectors_Compile.EncryptTestVector>_typeDescriptor(TestVectors_Compile.EncryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.EncryptTest> empty(TestVectors_Compile.EncryptTest._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>> _out2;
      _out2 = __default.ToEncryptTests((_2_encryptManifest).dtor_keys(), _5_encryptVectors);
      _6_valueOrError3 = _out2;
      if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_6_valueOrError3).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest> _7_encryptTests;
      _7_encryptTests = (_6_valueOrError3).Extract(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> _8_decryptVectors;
      dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> _out3;
      _out3 = __default.TestEncrypts(_7_encryptTests, (_2_encryptManifest).dtor_keys());
      _8_decryptVectors = _out3;
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _9_valueOrError4 = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out4;
      _out4 = CompleteVectors_Compile.__default.WriteDecryptManifest(op, (_2_encryptManifest).dtor_keys(), _8_decryptVectors);
      _9_valueOrError4 = _out4;
      if ((_9_valueOrError4).IsFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_9_valueOrError4).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.Tuple0 _10___v0;
      _10___v0 = (_9_valueOrError4).Extract(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Time.__default.PrintTimeSince(_0_time);
      output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return output;
  }
  public static dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> TestEncrypts(dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest> tests, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys)
  {
    dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> output = dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> empty(TestVectors_Compile.DecryptTestVector._typeDescriptor());
    if(true) {
      boolean _0_hasFailure;
      _0_hasFailure = false;
      System.out.print((dafny.DafnySequence.asString("\n=================== Starting ")).verbatimString());
      System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf((tests).length())));
      System.out.print((dafny.DafnySequence.asString(" Encrypt Tests =================== \n\n")).verbatimString());
      dafny.DafnySequence<? extends dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> _1_decryptableTests;
      _1_decryptableTests = dafny.DafnySequence.<dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> empty(dafny.Tuple2.<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor()));
      Time.AbsoluteTime _2_time;
      Time.AbsoluteTime _out0;
      _out0 = Time.__default.GetAbsoluteTime();
      _2_time = _out0;
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((tests).length());
      for (java.math.BigInteger _3_i = java.math.BigInteger.ZERO; _3_i.compareTo(_hi0) < 0; _3_i = _3_i.add(java.math.BigInteger.ONE)) {
        TestVectors_Compile.EncryptTest _4_test;
        _4_test = ((TestVectors_Compile.EncryptTest)(java.lang.Object)((tests).select(dafny.Helpers.toInt((_3_i)))));
        boolean _5_pass;
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> _6_maybeEncryptionMaterials;
        boolean _out1;
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> _out2;
        dafny.Tuple2<Boolean, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> _outcollector0 = TestVectors_Compile.__default.TestGetEncryptionMaterials(_4_test);
        _out1 = (boolean) (Object) _outcollector0.dtor__0();
        _out2 = (Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>) (Object) _outcollector0.dtor__1();
        _5_pass = _out1;
        _6_maybeEncryptionMaterials = _out2;
        if ((_5_pass) && (!(((_4_test).dtor_vector()).is_NegativeEncryptKeyringVector()))) {
          _1_decryptableTests = dafny.DafnySequence.<dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>>concatenate(_1_decryptableTests, dafny.DafnySequence.<dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> of(dafny.Tuple2.<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor()), dafny.Tuple2.<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>create(_4_test, (_6_maybeEncryptionMaterials).dtor_value())));
        } else if (!(_5_pass)) {
          _0_hasFailure = true;
        }
      }
      Time.RelativeTime _7_elapsed;
      Time.RelativeTime _out3;
      _out3 = Time.__default.TimeSince(_2_time);
      _7_elapsed = _out3;
      Time.__default.PrintTimeLong(_7_elapsed, dafny.DafnySequence.asString("TestEncrypts"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.LogFileName()));
      System.out.print((dafny.DafnySequence.asString("\n=================== Completed ")).verbatimString());
      System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf((tests).length())));
      System.out.print((dafny.DafnySequence.asString(" Encrypt Tests =================== \n\n")).verbatimString());
      if (!(!(_0_hasFailure))) {
        throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(90,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>> _8_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> empty(TestVectors_Compile.DecryptTestVector._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>> _out4;
      _out4 = __default.ToDecryptTestVectors(keys, _1_decryptableTests);
      _8_valueOrError0 = _out4;
      if (!(!((_8_valueOrError0).IsFailure(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))))) {
        throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(91,14): " + java.lang.String.valueOf(_8_valueOrError0));
      }
      output = (_8_valueOrError0).Extract(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> StartDecrypt(MplManifestOptions_Compile.ManifestOptions op)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    if(true) {
      Time.AbsoluteTime _0_time;
      Time.AbsoluteTime _out0;
      _out0 = Time.__default.GetAbsoluteTime();
      _0_time = _out0;
      Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> _1_valueOrError0 = (Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>>)null;
      Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> _out1;
      _out1 = __default.GetManifest((op).dtor_manifestPath(), dafny.DafnySequence.asString("manifest.json"));
      _1_valueOrError0 = _out1;
      if ((_1_valueOrError0).IsFailure(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_1_valueOrError0).<dafny.Tuple0>PropagateFailure(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      ManifestData _2_decryptManifest;
      _2_decryptManifest = (_1_valueOrError0).Extract(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _3_valueOrError1 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _3_valueOrError1 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_2_decryptManifest).is_DecryptManifest(), dafny.DafnySequence.asString("Not a encrypt manifest"));
      if ((_3_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_3_valueOrError1).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> empty(TestVectors_Compile.DecryptTestVector._typeDescriptor()));
      _4_valueOrError2 = ParseJsonManifests_Compile.__default.BuildDecryptTestVector((_2_decryptManifest).dtor_keys(), (_2_decryptManifest).dtor_jsonTests());
      if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_4_valueOrError2).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> _5_decryptVectors;
      _5_decryptVectors = (_4_valueOrError2).Extract(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTest> empty(TestVectors_Compile.DecryptTest._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>> _out2;
      _out2 = __default.ToDecryptTests((_2_decryptManifest).dtor_keys(), _5_decryptVectors);
      _6_valueOrError3 = _out2;
      if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_6_valueOrError3).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest> _7_decryptTests;
      _7_decryptTests = (_6_valueOrError3).Extract(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      __default.TestDecrypts(_7_decryptTests);
      Time.__default.PrintTimeSince(_0_time);
      output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return output;
  }
  public static void TestDecrypts(dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest> tests)
  {
    System.out.print((dafny.DafnySequence.asString("\n=================== Starting ")).verbatimString());
    System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf((tests).length())));
    System.out.print((dafny.DafnySequence.asString(" Decrypt Tests =================== \n\n")).verbatimString());
    boolean _0_hasFailure;
    _0_hasFailure = false;
    Time.AbsoluteTime _1_time;
    Time.AbsoluteTime _out0;
    _out0 = Time.__default.GetAbsoluteTime();
    _1_time = _out0;
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((tests).length());
    for (java.math.BigInteger _2_i = java.math.BigInteger.ZERO; _2_i.compareTo(_hi0) < 0; _2_i = _2_i.add(java.math.BigInteger.ONE)) {
      boolean _3_pass;
      boolean _out1;
      _out1 = TestVectors_Compile.__default.TestDecryptMaterials(((TestVectors_Compile.DecryptTest)(java.lang.Object)((tests).select(dafny.Helpers.toInt((_2_i))))));
      _3_pass = _out1;
      if (!(_3_pass)) {
        _0_hasFailure = true;
      }
    }
    Time.RelativeTime _4_elapsed;
    Time.RelativeTime _out2;
    _out2 = Time.__default.TimeSince(_1_time);
    _4_elapsed = _out2;
    Time.__default.PrintTimeLong(_4_elapsed, dafny.DafnySequence.asString("TestDecrypts"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default.LogFileName()));
    System.out.print((dafny.DafnySequence.asString("\n=================== Completed ")).verbatimString());
    System.out.print(java.lang.String.valueOf(java.math.BigInteger.valueOf((tests).length())));
    System.out.print((dafny.DafnySequence.asString(" Decrypt Tests =================== \n\n")).verbatimString());
    if (!(!(_0_hasFailure))) {
      throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(134,4): " + (dafny.DafnySequence.asString("expectation violation")).verbatimString());
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>> ToEncryptTests(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector> encryptVectors)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.EncryptTest> empty(TestVectors_Compile.EncryptTest._typeDescriptor()));
    dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest> _0_encryptTests;
    _0_encryptTests = dafny.DafnySequence.<TestVectors_Compile.EncryptTest> empty(TestVectors_Compile.EncryptTest._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((encryptVectors).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<TestVectors_Compile.EncryptTest, dafny.DafnySequence<? extends Character>> _2_valueOrError0 = (Wrappers_Compile.Result<TestVectors_Compile.EncryptTest, dafny.DafnySequence<? extends Character>>)null;
      Wrappers_Compile.Result<TestVectors_Compile.EncryptTest, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = TestVectors_Compile.__default.ToEncryptTest(keys, ((TestVectors_Compile.EncryptTestVector)(java.lang.Object)((encryptVectors).select(dafny.Helpers.toInt((_1_i))))));
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(TestVectors_Compile.EncryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_2_valueOrError0).<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>>PropagateFailure(TestVectors_Compile.EncryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()));
        return output;
      }
      TestVectors_Compile.EncryptTest _3_test;
      _3_test = (_2_valueOrError0).Extract(TestVectors_Compile.EncryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _0_encryptTests = dafny.DafnySequence.<TestVectors_Compile.EncryptTest>concatenate(_0_encryptTests, dafny.DafnySequence.<TestVectors_Compile.EncryptTest> of(TestVectors_Compile.EncryptTest._typeDescriptor(), _3_test));
    }
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.EncryptTest>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<TestVectors_Compile.EncryptTest>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_encryptTests);
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>> ToDecryptTestVectors(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, dafny.DafnySequence<? extends dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> tests)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> empty(TestVectors_Compile.DecryptTestVector._typeDescriptor()));
    if(true) {
      dafny.DafnySequence<? extends dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>> _0_successfulEncrypt;
      _0_successfulEncrypt = Seq_Compile.__default.<dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>>Filter(dafny.Tuple2.<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>_typeDescriptor(TestVectors_Compile.EncryptTest._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor()), ((java.util.function.Function<dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>, Boolean>)(_1_r_boxed0) -> {
        dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials> _1_r = ((dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>)(java.lang.Object)(_1_r_boxed0));
        return ((((_1_r).dtor__0()).dtor_vector()).is_PositiveEncryptKeyringVector()) || ((((_1_r).dtor__0()).dtor_vector()).is_PositiveEncryptNegativeDecryptKeyringVector());
      }), tests);
      dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> _2_decryptTestVectors;
      _2_decryptTestVectors = dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> empty(TestVectors_Compile.DecryptTestVector._typeDescriptor());
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_0_successfulEncrypt).length());
      for (java.math.BigInteger _3_i = java.math.BigInteger.ZERO; _3_i.compareTo(_hi0) < 0; _3_i = _3_i.add(java.math.BigInteger.ONE)) {
        TestVectors_Compile.DecryptTestVector _4_vector;
        _4_vector = TestVectors_Compile.__default.EncryptTestToDecryptVector((((dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>)(java.lang.Object)((_0_successfulEncrypt).select(dafny.Helpers.toInt((_3_i)))))).dtor__0(), (((dafny.Tuple2<TestVectors_Compile.EncryptTest, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials>)(java.lang.Object)((_0_successfulEncrypt).select(dafny.Helpers.toInt((_3_i)))))).dtor__1());
        _2_decryptTestVectors = dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>concatenate(_2_decryptTestVectors, dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector> of(TestVectors_Compile.DecryptTestVector._typeDescriptor(), _4_vector));
      }
      output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<TestVectors_Compile.DecryptTestVector>_typeDescriptor(TestVectors_Compile.DecryptTestVector._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_decryptTestVectors);
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>> ToDecryptTests(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> vectors)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTest> empty(TestVectors_Compile.DecryptTest._typeDescriptor()));
    dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest> _0_decryptTests;
    _0_decryptTests = dafny.DafnySequence.<TestVectors_Compile.DecryptTest> empty(TestVectors_Compile.DecryptTest._typeDescriptor());
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((vectors).length());
    for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
      Wrappers_Compile.Result<TestVectors_Compile.DecryptTest, dafny.DafnySequence<? extends Character>> _2_valueOrError0 = (Wrappers_Compile.Result<TestVectors_Compile.DecryptTest, dafny.DafnySequence<? extends Character>>)null;
      Wrappers_Compile.Result<TestVectors_Compile.DecryptTest, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = TestVectors_Compile.__default.DecryptVectorToDecryptTest(keys, ((TestVectors_Compile.DecryptTestVector)(java.lang.Object)((vectors).select(dafny.Helpers.toInt((_1_i))))));
      _2_valueOrError0 = _out0;
      if ((_2_valueOrError0).IsFailure(TestVectors_Compile.DecryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_2_valueOrError0).<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>>PropagateFailure(TestVectors_Compile.DecryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()));
        return output;
      }
      TestVectors_Compile.DecryptTest _3_test;
      _3_test = (_2_valueOrError0).Extract(TestVectors_Compile.DecryptTest._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _0_decryptTests = dafny.DafnySequence.<TestVectors_Compile.DecryptTest>concatenate(_0_decryptTests, dafny.DafnySequence.<TestVectors_Compile.DecryptTest> of(TestVectors_Compile.DecryptTest._typeDescriptor(), _3_test));
    }
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends TestVectors_Compile.DecryptTest>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<TestVectors_Compile.DecryptTest>_typeDescriptor(TestVectors_Compile.DecryptTest._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _0_decryptTests);
    return output;
  }
  public static Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> GetManifest(dafny.DafnySequence<? extends Character> manifestPath, dafny.DafnySequence<? extends Character> manifestFileName)
  {
    Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>> manifestData = (Wrappers_Compile.Result<ManifestData, dafny.DafnySequence<? extends Character>>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = FileIO_Compile.__default.ReadBytesFromFile(dafny.DafnySequence.<Character>concatenate(manifestPath, manifestFileName));
      _0_valueOrError0 = _out0;
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_0_valueOrError0).<ManifestData>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _1_decryptManifestBytes;
      _1_decryptManifestBytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _2_valueOrError1 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Default(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON.Default());
      _2_valueOrError1 = (JSON_mAPI_Compile.__default.Deserialize(_1_decryptManifestBytes)).<dafny.DafnySequence<? extends Character>>MapFailure(JSON_mValues_Compile.JSON._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<JSON_mErrors_Compile.DeserializationError, dafny.DafnySequence<? extends Character>>)(_3_e_boxed0) -> {
        JSON_mErrors_Compile.DeserializationError _3_e = ((JSON_mErrors_Compile.DeserializationError)(java.lang.Object)(_3_e_boxed0));
        return (_3_e).ToString();
      }));
      if ((_2_valueOrError1).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_2_valueOrError1).<ManifestData>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      JSON_mValues_Compile.JSON _4_manifestJson;
      _4_manifestJson = (_2_valueOrError1).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _5_valueOrError2 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _5_valueOrError2 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (_4_manifestJson).is_Object(), dafny.DafnySequence.asString("Not a JSON object"));
      if ((_5_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_5_valueOrError2).<ManifestData>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> empty(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())));
      _6_valueOrError3 = JSONHelpers_Compile.__default.GetObject(dafny.DafnySequence.asString("manifest"), (_4_manifestJson).dtor_obj());
      if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_6_valueOrError3).<ManifestData>PropagateFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _7_manifest;
      _7_manifest = (_6_valueOrError3).Extract(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<java.math.BigInteger, dafny.DafnySequence<? extends Character>> _8_valueOrError4 = Wrappers_Compile.Result.<java.math.BigInteger, dafny.DafnySequence<? extends Character>>Default(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), java.math.BigInteger.ZERO);
      _8_valueOrError4 = JSONHelpers_Compile.__default.GetNat(dafny.DafnySequence.asString("version"), _7_manifest);
      if ((_8_valueOrError4).IsFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_8_valueOrError4).<ManifestData>PropagateFailure(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      java.math.BigInteger _9_version = java.math.BigInteger.ZERO;
      _9_version = (_8_valueOrError4).Extract(_System.nat._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _10_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _10_valueOrError5 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("type"), _7_manifest);
      if ((_10_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_10_valueOrError5).<ManifestData>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends Character> _11_typ;
      _11_typ = (_10_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _12_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _12_valueOrError6 = JSONHelpers_Compile.__default.GetString(dafny.DafnySequence.asString("keys"), (_4_manifestJson).dtor_obj());
      if ((_12_valueOrError6).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_12_valueOrError6).<ManifestData>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends Character> _13_keyManifestUri;
      _13_keyManifestUri = (_12_valueOrError6).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Outcome<dafny.DafnySequence<? extends Character>> _14_valueOrError7 = Wrappers_Compile.Outcome.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      _14_valueOrError7 = Wrappers_Compile.__default.<dafny.DafnySequence<? extends Character>>Need(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (dafny.DafnySequence.asString("file://")).isProperPrefixOf(_13_keyManifestUri), dafny.DafnySequence.asString("Unexpected URI prefix"));
      if ((_14_valueOrError7).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_14_valueOrError7).<ManifestData>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends Character> _15_keyManifestPath;
      _15_keyManifestPath = dafny.DafnySequence.<Character>concatenate(manifestPath, (_13_keyManifestUri).drop(java.math.BigInteger.valueOf(7L)));
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _16_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error> _out1;
      _out1 = software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.__default.KeyVectors(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig.create(_15_keyManifestPath));
      _16_valueOrError8 = _out1;
      if (!(!((_16_valueOrError8).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(242,16): " + java.lang.String.valueOf(_16_valueOrError8));
      }
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient _17_keys;
      _17_keys = (_16_valueOrError8).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient.class)), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>> _18_valueOrError9 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> empty(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())));
      _18_valueOrError9 = JSONHelpers_Compile.__default.GetObject(dafny.DafnySequence.asString("tests"), (_4_manifestJson).dtor_obj());
      if ((_18_valueOrError9).IsFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        manifestData = (_18_valueOrError9).<ManifestData>PropagateFailure(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
        return manifestData;
      }
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _19_jsonTests;
      _19_jsonTests = (_18_valueOrError9).Extract(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>_typeDescriptor(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor())), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      if (java.util.Objects.equals(_11_typ, dafny.DafnySequence.asString("awses-mpl-decrypt"))) {
        Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _20_valueOrError10 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Default(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON.Default());
        _20_valueOrError10 = JSONHelpers_Compile.__default.Get(dafny.DafnySequence.asString("client"), (_4_manifestJson).dtor_obj());
        if ((_20_valueOrError10).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          manifestData = (_20_valueOrError10).<ManifestData>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData._typeDescriptor());
          return manifestData;
        }
        JSON_mValues_Compile.JSON _21_client;
        _21_client = (_20_valueOrError10).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        manifestData = Wrappers_Compile.Result.<ManifestData, dafny.DafnySequence<? extends Character>>create_Success(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData.create_DecryptManifest(_9_version, _17_keys, _21_client, _19_jsonTests));
      } else if (java.util.Objects.equals(_11_typ, dafny.DafnySequence.asString("awses-mpl-encrypt"))) {
        manifestData = Wrappers_Compile.Result.<ManifestData, dafny.DafnySequence<? extends Character>>create_Success(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ManifestData.create_EncryptManifest(_9_version, _17_keys, _19_jsonTests));
      } else {
        manifestData = Wrappers_Compile.Result.<ManifestData, dafny.DafnySequence<? extends Character>>create_Failure(ManifestData._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Unsupported manifest type:"), _11_typ));
      }
    }
    return manifestData;
  }
  @Override
  public java.lang.String toString() {
    return "TestManifests._default";
  }
}
