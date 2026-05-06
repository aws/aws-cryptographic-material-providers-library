// Class __default
// Dafny class __default compiled into Java
package AllDefaultCmm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> SubSets(dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> ec, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>> keys)
  {
    if ((java.math.BigInteger.valueOf((ec).size())).signum() == 0) {
      return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(dafny.DafnyMap.fromElements());
    } else {
      dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _0_subsets = __default.SubSets(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>subtract(ec, dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>> of(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((keys).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))), (keys).drop(java.math.BigInteger.ONE));
      return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>union(_0_subsets, ((dafny.Function3<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>, dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_subsets, _2_keys, _3_ec) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
        java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll0 = new java.util.ArrayList<>();
        for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0_boxed0 : (_1_subsets).Elements()) {
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_0_boxed0));
          dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_0;
          if ((_1_subsets).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) {
            _coll0.add(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>merge(_4_s, dafny.DafnyMap.fromElements(new dafny.Tuple2(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_2_keys).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_3_ec).get(((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)((_2_keys).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))))))))));
          }
        }
        return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll0);
      })).apply()).apply(_0_subsets, keys, ec));
    }
  }
  public static dafny.DafnySequence<? extends Character> AesKey()
  {
    return ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((AllRawAES_Compile.__default.aesPersistentKeyNames()).select(dafny.Helpers.toInt(((java.math.BigInteger.valueOf((AllRawAES_Compile.__default.aesPersistentKeyNames()).length())).subtract(java.math.BigInteger.ONE))))));
  }
  public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription RawAesKeyring()
  {
    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(__default.AesKey(), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), __default.AesKey())));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> a()
  {
    return (UTF8.__default.Encode(dafny.DafnySequence.asString("a"))).dtor_value();
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> b()
  {
    return (UTF8.__default.Encode(dafny.DafnySequence.asString("b"))).dtor_value();
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> rootEncryptionContext()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.a(), __default.a()), new dafny.Tuple2(__default.b(), __default.b()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> encryptionContextsToTest()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.rootEncryptionContext());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> c()
  {
    return (UTF8.__default.Encode(dafny.DafnySequence.asString("c"))).dtor_value();
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> disjointEncryptionContext()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.a(), __default.c()), new dafny.Tuple2(__default.b(), __default.c()), new dafny.Tuple2(__default.c(), __default.c()));
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo StaticAlgorithmSuite()
  {
    return AlgorithmSuites_Compile.__default.GetESDKSuite(software.amazon.cryptography.materialproviders.internaldafny.types.ESDKAlgorithmSuiteId.create_ALG__AES__128__GCM__IV12__TAG16__NO__KDF());
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0_boxed0 : (__default.encryptionContextsToTest()).Elements()) {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_0;
        if ((__default.encryptionContextsToTest()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_0_encryptionContext)) {
          for (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
            java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll1 = new java.util.ArrayList<>();
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_b_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if ((__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_b_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_b_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if ((__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_b_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_8_encryptionContext, _9_requiredEncryptionContextKeys) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed0, _11_b_boxed0) -> {
                  byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed0));
                  byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed0));
                  return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed1, _11_b_boxed1) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed1));
                    byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed1));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                  })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_12_s)) && ((dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>>intersection((_12_s).keySet(), _9_requiredEncryptionContextKeys)).equals(_9_requiredEncryptionContextKeys))) {
                    _coll3.add(_12_s);
                  }
                }
                return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll3);
              })).apply()).apply(_0_encryptionContext, _5_requiredEncryptionContextKeys)).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_4_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _13_reproducedEncryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_4;
                if ((((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_14_encryptionContext, _15_requiredEncryptionContextKeys) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                  java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll4 = new java.util.ArrayList<>();
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed2, _11_b_boxed2) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed2));
                    byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed2));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed3, _11_b_boxed3) -> {
                      byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed3));
                      byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed3));
                      return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                    })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_16_s)) && ((dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>>intersection((_16_s).keySet(), _15_requiredEncryptionContextKeys)).equals(_15_requiredEncryptionContextKeys))) {
                      _coll4.add(_16_s);
                    }
                  }
                  return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll4);
                })).apply()).apply(_0_encryptionContext, _5_requiredEncryptionContextKeys)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_13_reproducedEncryptionContext)) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_17_a_boxed0, _18_b_boxed0) -> {
  byte _17_a = ((byte)(java.lang.Object)(_17_a_boxed0));
  byte _18_b = ((byte)(java.lang.Object)(_18_b_boxed0));
  return java.lang.Integer.compareUnsigned(_17_a, _18_b) < 0;
}))), __default.RawAesKeyring(), __default.RawAesKeyring(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _13_reproducedEncryptionContext)));
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> FailureBadReproducedEncryptionContext()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0_boxed0 : (__default.encryptionContextsToTest()).Elements()) {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_0;
        if ((__default.encryptionContextsToTest()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_0_encryptionContext)) {
          for (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
            java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll1 = new java.util.ArrayList<>();
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_b_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if ((__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_b_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_b_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if ((__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_b_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed0, _9_b_boxed0) -> {
                  byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed0));
                  byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed0));
                  return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _10_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed1, _9_b_boxed1) -> {
                    byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed1));
                    byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed1));
                    return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                  })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_10_s)) && (!(_10_s).equals(dafny.DafnyMap.fromElements()))) {
                    _coll3.add(_10_s);
                  }
                }
                return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll3);
              })).apply()).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_4_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _11_incorrectEncryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_4;
                if ((((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                  java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll4 = new java.util.ArrayList<>();
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed2, _9_b_boxed2) -> {
                    byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed2));
                    byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed2));
                    return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed3, _9_b_boxed3) -> {
                      byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed3));
                      byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed3));
                      return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                    })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_12_s)) && (!(_12_s).equals(dafny.DafnyMap.fromElements()))) {
                      _coll4.add(_12_s);
                    }
                  }
                  return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll4);
                })).apply()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_11_incorrectEncryptionContext)) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_7_boxed0 : (((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_13_encryptionContext, _14_incorrectEncryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                    java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll5 = new java.util.ArrayList<>();
                    for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_8_boxed0 : (__default.SubSets(_13_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_13_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed0, _16_b_boxed0) -> {
                      byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed0));
                      byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed0));
                      return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                    })))).Elements()) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_8 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_8_boxed0));
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _17_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_8;
                      if ((__default.SubSets(_13_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_13_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed1, _16_b_boxed1) -> {
                        byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed1));
                        byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed1));
                        return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                      })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_17_s)) {
                        _coll5.add(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>merge(_17_s, _14_incorrectEncryptionContext));
                      }
                    }
                    return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll5);
                  })).apply()).apply(_0_encryptionContext, _11_incorrectEncryptionContext)).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_7 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_7_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _18_reproducedEncryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_7;
                    if ((((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_19_encryptionContext, _20_incorrectEncryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                      java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll6 = new java.util.ArrayList<>();
                      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_9_boxed0 : (__default.SubSets(_19_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_19_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed2, _16_b_boxed2) -> {
                        byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed2));
                        byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed2));
                        return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                      })))).Elements()) {
                        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_9 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_9_boxed0));
                        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _21_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_9;
                        if ((__default.SubSets(_19_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_19_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed3, _16_b_boxed3) -> {
                          byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed3));
                          byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed3));
                          return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                        })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_21_s)) {
                          _coll6.add(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>merge(_21_s, _20_incorrectEncryptionContext));
                        }
                      }
                      return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll6);
                    })).apply()).apply(_0_encryptionContext, _11_incorrectEncryptionContext)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_18_reproducedEncryptionContext)) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptNegativeDecryptKeyringVector(dafny.DafnySequence.asString("Failure of reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_22_a_boxed0, _23_b_boxed0) -> {
  byte _22_a = ((byte)(java.lang.Object)(_22_a_boxed0));
  byte _23_b = ((byte)(java.lang.Object)(_23_b_boxed0));
  return java.lang.Integer.compareUnsigned(_22_a, _23_b) < 0;
}))), dafny.DafnySequence.asString("The reproducedEncryptionContext is not correct"), __default.RawAesKeyring(), __default.RawAesKeyring(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _18_reproducedEncryptionContext)));
                    }
                  }
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription StaticPlaintextDataKey()
  {
    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Static(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring.create(dafny.DafnySequence.asString("static-plaintext-data-key")));
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> d()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 144, (byte) 128, (byte) 130);
  }
  public static software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription StaticNotPlaintextDataKey()
  {
    return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Static(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.StaticKeyring.create(dafny.DafnySequence.asString("no-plaintext-data-key")));
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector> empty(), dafny.DafnySet.<TestVectors_Compile.EncryptTestVector> of(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("Simplest possible happy path"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), __default.StaticPlaintextDataKey(), __default.StaticPlaintextDataKey(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))), TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("SurrogatePair Encryption Context Test"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.d(), __default.d())), AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), __default.RawAesKeyring(), __default.RawAesKeyring(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))), TestVectors_Compile.EncryptTestVector.create_NegativeEncryptKeyringVector(dafny.DafnySequence.asString("Missing plaintext data key on decrypt"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), dafny.DafnySequence.asString("No plaintext data key on encrypt fails"), __default.StaticNotPlaintextDataKey()), TestVectors_Compile.EncryptTestVector.create_PositiveEncryptNegativeDecryptKeyringVector(dafny.DafnySequence.asString("Missing plaintext data key on decrypt"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(__default.StaticAlgorithmSuite()), __default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), dafny.DafnySequence.asString("No plaintext data key on encrypt fails"), __default.StaticPlaintextDataKey(), __default.StaticNotPlaintextDataKey(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))))), __default.FailureBadReproducedEncryptionContext()), __default.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext());
  }
  @Override
  public java.lang.String toString() {
    return "AllDefaultCmm._default";
  }
}
