// Class __default
// Dafny class __default compiled into Java
package CompleteVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> WriteStuff(MplManifestOptions_Compile.ManifestOptions op)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    if(true) {
      Time.AbsoluteTime _0_time;
      Time.AbsoluteTime _out0;
      _out0 = Time.__default.GetAbsoluteTime();
      _0_time = _out0;
      dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector> _1_tests;
      dafny.DafnySequence<? extends TestVectors_Compile.EncryptTestVector> _out1;
      _out1 = SortedSets.__default.<TestVectors_Compile.EncryptTestVector>SetToSequence(TestVectors_Compile.EncryptTestVector._typeDescriptor(), __default.AllPositiveKeyringTests());
      _1_tests = _out1;
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _2_testsJSON;
      _2_testsJSON = dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> empty(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()));
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_1_tests).length());
      for (java.math.BigInteger _3_i = java.math.BigInteger.ZERO; _3_i.compareTo(_hi0) < 0; _3_i = _3_i.add(java.math.BigInteger.ONE)) {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _4_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out2;
        _out2 = UUID.__default.GenerateUUID();
        _4_valueOrError0 = _out2;
        if ((_4_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          output = (_4_valueOrError0).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
          return output;
        }
        dafny.DafnySequence<? extends Character> _5_name;
        _5_name = (_4_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _6_valueOrError1 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Default(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON.Default());
        _6_valueOrError1 = WriteJsonManifests_Compile.__default.EncryptTestVectorToJson(((TestVectors_Compile.EncryptTestVector)(java.lang.Object)((_1_tests).select(dafny.Helpers.toInt((_3_i))))));
        if ((_6_valueOrError1).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          output = (_6_valueOrError1).<dafny.Tuple0>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
          return output;
        }
        JSON_mValues_Compile.JSON _7_test;
        _7_test = (_6_valueOrError1).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        _2_testsJSON = dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>concatenate(_2_testsJSON, dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(_5_name, _7_test)));
      }
      JSON_mValues_Compile.JSON _8_mplEncryptManifest;
      _8_mplEncryptManifest = JSON_mValues_Compile.JSON.create_Object(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("manifest"), JSON_mValues_Compile.JSON.create_Object(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("version"), JSON_mValues_Compile.JSON.create_Number(JSON_mValues_Compile.__default.Int(java.math.BigInteger.valueOf(4L)))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("type"), JSON_mValues_Compile.JSON.create_String(dafny.DafnySequence.asString("awses-mpl-encrypt")))))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("keys"), JSON_mValues_Compile.JSON.create_String(dafny.DafnySequence.asString("file://keys.json"))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("tests"), JSON_mValues_Compile.JSON.create_Object(_2_testsJSON))));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _9_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _9_valueOrError2 = (JSON_mAPI_Compile.__default.Serialize(_8_mplEncryptManifest)).<dafny.DafnySequence<? extends Character>>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<JSON_mErrors_Compile.SerializationError, dafny.DafnySequence<? extends Character>>)(_10_e_boxed0) -> {
        JSON_mErrors_Compile.SerializationError _10_e = ((JSON_mErrors_Compile.SerializationError)(java.lang.Object)(_10_e_boxed0));
        return (_10_e).ToString();
      }));
      if ((_9_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_9_valueOrError2).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _11_mplEncryptManifestBytes;
      _11_mplEncryptManifestBytes = (_9_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _12_valueOrError3 = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out3;
      _out3 = __default.WriteVectorsFile(dafny.DafnySequence.<Character>concatenate((op).dtor_encryptManifestOutput(), dafny.DafnySequence.asString("manifest.json")), _11_mplEncryptManifestBytes);
      _12_valueOrError3 = _out3;
      if ((_12_valueOrError3).IsFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_12_valueOrError3).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.Tuple0 _13___v0;
      _13___v0 = (_12_valueOrError3).Extract(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Time.__default.PrintTimeSince(_0_time);
      output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> WriteDecryptManifest(MplManifestOptions_Compile.ManifestOptions op, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.KeyVectorsClient keys, dafny.DafnySequence<? extends TestVectors_Compile.DecryptTestVector> tests)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    if(true) {
      dafny.DafnySequence<? extends dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> _0_testsJSON;
      _0_testsJSON = dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> empty(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()));
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((tests).length());
      for (java.math.BigInteger _1_i = java.math.BigInteger.ZERO; _1_i.compareTo(_hi0) < 0; _1_i = _1_i.add(java.math.BigInteger.ONE)) {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out0;
        _out0 = UUID.__default.GenerateUUID();
        _2_valueOrError0 = _out0;
        if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          output = (_2_valueOrError0).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
          return output;
        }
        dafny.DafnySequence<? extends Character> _3_name;
        _3_name = (_2_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        Wrappers_Compile.Result<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>> _4_valueOrError1 = Wrappers_Compile.Result.<JSON_mValues_Compile.JSON, dafny.DafnySequence<? extends Character>>Default(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON.Default());
        _4_valueOrError1 = WriteJsonManifests_Compile.__default.DecryptTestVectorToJson(((TestVectors_Compile.DecryptTestVector)(java.lang.Object)((tests).select(dafny.Helpers.toInt((_1_i))))));
        if ((_4_valueOrError1).IsFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
          output = (_4_valueOrError1).<dafny.Tuple0>PropagateFailure(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
          return output;
        }
        JSON_mValues_Compile.JSON _5_test;
        _5_test = (_4_valueOrError1).Extract(JSON_mValues_Compile.JSON._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
        _0_testsJSON = dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>>concatenate(_0_testsJSON, dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(_3_name, _5_test)));
      }
      JSON_mValues_Compile.JSON _6_mplDecryptManifest;
      _6_mplDecryptManifest = JSON_mValues_Compile.JSON.create_Object(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("manifest"), JSON_mValues_Compile.JSON.create_Object(dafny.DafnySequence.<dafny.Tuple2<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>> of(dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), JSON_mValues_Compile.JSON._typeDescriptor()), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("version"), JSON_mValues_Compile.JSON.create_Number(JSON_mValues_Compile.__default.Int(java.math.BigInteger.valueOf(4L)))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("type"), JSON_mValues_Compile.JSON.create_String(dafny.DafnySequence.asString("awses-mpl-decrypt")))))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("client"), JSON_mValues_Compile.JSON.create_String(dafny.DafnySequence.asString("mpl-dafny"))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("keys"), JSON_mValues_Compile.JSON.create_String(dafny.DafnySequence.asString("file://keys.json"))), dafny.Tuple2.<dafny.DafnySequence<? extends Character>, JSON_mValues_Compile.JSON>create(dafny.DafnySequence.asString("tests"), JSON_mValues_Compile.JSON.create_Object(_0_testsJSON))));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _7_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _7_valueOrError2 = (JSON_mAPI_Compile.__default.Serialize(_6_mplDecryptManifest)).<dafny.DafnySequence<? extends Character>>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<JSON_mErrors_Compile.SerializationError, dafny.DafnySequence<? extends Character>>)(_8_e_boxed0) -> {
        JSON_mErrors_Compile.SerializationError _8_e = ((JSON_mErrors_Compile.SerializationError)(java.lang.Object)(_8_e_boxed0));
        return (_8_e).ToString();
      }));
      if ((_7_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_7_valueOrError2).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _9_mplDecryptManifestBytes;
      _9_mplDecryptManifestBytes = (_7_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _10_valueOrError3 = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out1;
      _out1 = __default.WriteVectorsFile(dafny.DafnySequence.<Character>concatenate((op).dtor_decryptManifestOutput(), dafny.DafnySequence.asString("manifest.json")), _9_mplDecryptManifestBytes);
      _10_valueOrError3 = _out1;
      if ((_10_valueOrError3).IsFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_10_valueOrError3).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.Tuple0 _11___v1;
      _11___v1 = (_10_valueOrError3).Extract(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      dafny.DafnySequence<? extends Character> _12_keysJsonFileName;
      _12_keysJsonFileName = dafny.DafnySequence.asString("keys.json");
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _13_valueOrError4 = (JSON_mAPI_Compile.__default.Serialize(((keys).config()).dtor_keysJson())).<dafny.DafnySequence<? extends Character>>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), JSON_mErrors_Compile.SerializationError._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((java.util.function.Function<JSON_mErrors_Compile.SerializationError, dafny.DafnySequence<? extends Character>>)(_14_e_boxed0) -> {
        JSON_mErrors_Compile.SerializationError _14_e = ((JSON_mErrors_Compile.SerializationError)(java.lang.Object)(_14_e_boxed0));
        return (_14_e).ToString();
      }));
      if ((_13_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_13_valueOrError4).<dafny.Tuple0>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _15_keysJsonBytes;
      _15_keysJsonBytes = (_13_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _16_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out2;
      _out2 = __default.WriteVectorsFile(dafny.DafnySequence.<Character>concatenate((op).dtor_decryptManifestOutput(), _12_keysJsonFileName), _15_keysJsonBytes);
      _16_valueOrError5 = _out2;
      if ((_16_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
        output = (_16_valueOrError5).<dafny.Tuple0>PropagateFailure(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0._typeDescriptor());
        return output;
      }
      dafny.Tuple0 _17___v2;
      _17___v2 = (_16_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
      output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>create_Success(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.create());
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> WriteVectorsFile(dafny.DafnySequence<? extends Character> location, dafny.DafnySequence<? extends java.lang.Byte> bytes)
  {
    Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> output = Wrappers_Compile.Result.<dafny.Tuple0, dafny.DafnySequence<? extends Character>>Default(dafny.Tuple0._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.Tuple0.Default());
    if(true) {
      Wrappers_Compile.Result<dafny.Tuple0, dafny.DafnySequence<? extends Character>> _out0;
      _out0 = FileIO_Compile.__default.WriteBytesToFile(location, bytes);
      output = _out0;
    }
    return output;
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> AllPositiveKeyringTests()
  {
    return dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector> empty(), AllDefaultCmm_Compile.__default.Tests()), AllHierarchy_Compile.__default.Tests()), AllKms_Compile.__default.Tests()), AllKmsMrkAware_Compile.__default.Tests()), AllKmsMrkAwareDiscovery_Compile.__default.Tests()), AllKmsRsa_Compile.__default.Tests()), AllRawAES_Compile.__default.Tests()), AllRawRSA_Compile.__default.Tests()), AllMulti_Compile.__default.Tests()), AllRequiredEncryptionContextCmm_Compile.__default.Tests()), AllRawECDH_Compile.__default.Tests()), AllKmsEcdh_Compile.__default.Tests());
  }
  @Override
  public java.lang.String toString() {
    return "CompleteVectors._default";
  }
}
