// Class __default
// Dafny class __default compiled into Java
package AllRequiredEncryptionContextCmm_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
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
  public static dafny.DafnySequence<? extends java.lang.Byte> d()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 240, (byte) 144, (byte) 128, (byte) 130);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> psiECMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.a(), __default.a()), new dafny.Tuple2(__default.d(), __default.d()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> psiEC()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.psiECMap());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> replacementChar()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 239, (byte) 191, (byte) 189);
  }
  public static dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> replacementCharECMap()
  {
    return dafny.DafnyMap.fromElements(new dafny.Tuple2(__default.a(), __default.a()), new dafny.Tuple2(__default.replacementChar(), __default.replacementChar()));
  }
  public static dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> replacementCharEC()
  {
    return dafny.DafnySet.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> of(__default.replacementCharECMap());
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
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_b_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if (((AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_b_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) && ((java.math.BigInteger.valueOf((_4_s).size())).signum() != 0)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_b_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if (((AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_b_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) && ((java.math.BigInteger.valueOf((_7_s).size())).signum() != 0)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_8_encryptionContext, _9_requiredEncryptionContextKeys) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed0, _11_b_boxed0) -> {
                  byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed0));
                  byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed0));
                  return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed1, _11_b_boxed1) -> {
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
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed2, _11_b_boxed2) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed2));
                    byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed2));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed3, _11_b_boxed3) -> {
                      byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed3));
                      byte _11_b = ((byte)(java.lang.Object)(_11_b_boxed3));
                      return java.lang.Integer.compareUnsigned(_10_a, _11_b) < 0;
                    })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_16_s)) && ((dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>>intersection((_16_s).keySet(), _15_requiredEncryptionContextKeys)).equals(_15_requiredEncryptionContextKeys))) {
                      _coll4.add(_16_s);
                    }
                  }
                  return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll4);
                })).apply()).apply(_0_encryptionContext, _5_requiredEncryptionContextKeys)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_13_reproducedEncryptionContext)) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(AllDefaultCmm_Compile.__default.StaticAlgorithmSuite()), AllDefaultCmm_Compile.__default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_17_a_boxed0, _18_b_boxed0) -> {
  byte _17_a = ((byte)(java.lang.Object)(_17_a_boxed0));
  byte _18_b = ((byte)(java.lang.Object)(_18_b_boxed0));
  return java.lang.Integer.compareUnsigned(_17_a, _18_b) < 0;
}))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(AllDefaultCmm_Compile.__default.RawAesKeyring(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_19_a_boxed0, _20_b_boxed0) -> {
  byte _19_a = ((byte)(java.lang.Object)(_19_a_boxed0));
  byte _20_b = ((byte)(java.lang.Object)(_20_b_boxed0));
  return java.lang.Integer.compareUnsigned(_19_a, _20_b) < 0;
})))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(AllDefaultCmm_Compile.__default.RawAesKeyring(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_21_a_boxed0, _22_b_boxed0) -> {
  byte _21_a = ((byte)(java.lang.Object)(_21_a_boxed0));
  byte _22_b = ((byte)(java.lang.Object)(_22_b_boxed0));
  return java.lang.Integer.compareUnsigned(_21_a, _22_b) < 0;
})))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _13_reproducedEncryptionContext)));
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
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_b_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if (((AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_b_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) && ((java.math.BigInteger.valueOf((_4_s).size())).signum() != 0)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_b_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if (((AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_b_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_b = ((byte)(java.lang.Object)(_3_b_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_b) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) && ((java.math.BigInteger.valueOf((_7_s).size())).signum() != 0)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed0, _9_b_boxed0) -> {
                  byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed0));
                  byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed0));
                  return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _10_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((AllDefaultCmm_Compile.__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed1, _9_b_boxed1) -> {
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
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed2, _9_b_boxed2) -> {
                    byte _8_a = ((byte)(java.lang.Object)(_8_a_boxed2));
                    byte _9_b = ((byte)(java.lang.Object)(_9_b_boxed2));
                    return java.lang.Integer.compareUnsigned(_8_a, _9_b) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((AllDefaultCmm_Compile.__default.SubSets(__default.disjointEncryptionContext(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (__default.disjointEncryptionContext()).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_8_a_boxed3, _9_b_boxed3) -> {
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
                    for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_8_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_13_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_13_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed0, _16_b_boxed0) -> {
                      byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed0));
                      byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed0));
                      return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                    })))).Elements()) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_8 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_8_boxed0));
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _17_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_8;
                      if ((AllDefaultCmm_Compile.__default.SubSets(_13_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_13_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed1, _16_b_boxed1) -> {
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
                      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_9_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_19_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_19_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed2, _16_b_boxed2) -> {
                        byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed2));
                        byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed2));
                        return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                      })))).Elements()) {
                        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_9 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_9_boxed0));
                        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _21_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_9;
                        if ((AllDefaultCmm_Compile.__default.SubSets(_19_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_19_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_15_a_boxed3, _16_b_boxed3) -> {
                          byte _15_a = ((byte)(java.lang.Object)(_15_a_boxed3));
                          byte _16_b = ((byte)(java.lang.Object)(_16_b_boxed3));
                          return java.lang.Integer.compareUnsigned(_15_a, _16_b) < 0;
                        })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_21_s)) {
                          _coll6.add(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>merge(_21_s, _20_incorrectEncryptionContext));
                        }
                      }
                      return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll6);
                    })).apply()).apply(_0_encryptionContext, _11_incorrectEncryptionContext)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_18_reproducedEncryptionContext)) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptNegativeDecryptKeyringVector(dafny.DafnySequence.asString("Failure of reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(AllDefaultCmm_Compile.__default.StaticAlgorithmSuite()), AllDefaultCmm_Compile.__default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_22_a_boxed0, _23_b_boxed0) -> {
  byte _22_a = ((byte)(java.lang.Object)(_22_a_boxed0));
  byte _23_b = ((byte)(java.lang.Object)(_23_b_boxed0));
  return java.lang.Integer.compareUnsigned(_22_a, _23_b) < 0;
}))), dafny.DafnySequence.asString("The reproducedEncryptionContext is not correct"), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(AllDefaultCmm_Compile.__default.RawAesKeyring(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_24_a_boxed0, _25_b_boxed0) -> {
  byte _24_a = ((byte)(java.lang.Object)(_24_a_boxed0));
  byte _25_b = ((byte)(java.lang.Object)(_25_b_boxed0));
  return java.lang.Integer.compareUnsigned(_24_a, _25_b) < 0;
})))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(AllDefaultCmm_Compile.__default.RawAesKeyring(), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_26_a_boxed0, _27_b_boxed0) -> {
  byte _26_a = ((byte)(java.lang.Object)(_26_a_boxed0));
  byte _27_b = ((byte)(java.lang.Object)(_27_b_boxed0));
  return java.lang.Integer.compareUnsigned(_26_a, _27_b) < 0;
})))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _18_reproducedEncryptionContext)));
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContextPsi()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0_boxed0 : (__default.psiEC()).Elements()) {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_0;
        if ((__default.psiEC()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_0_encryptionContext)) {
          for (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
            java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll1 = new java.util.ArrayList<>();
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_d_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_d = ((byte)(java.lang.Object)(_3_d_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_d) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if (((AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_d_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_d = ((byte)(java.lang.Object)(_3_d_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_d) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) && ((java.math.BigInteger.valueOf((_4_s).size())).signum() != 0)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_d_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_d = ((byte)(java.lang.Object)(_3_d_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_d) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if (((AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_d_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_d = ((byte)(java.lang.Object)(_3_d_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_d) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) && ((java.math.BigInteger.valueOf((_7_s).size())).signum() != 0)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_8_encryptionContext, _9_requiredEncryptionContextKeys) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed0, _11_d_boxed0) -> {
                  byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed0));
                  byte _11_d = ((byte)(java.lang.Object)(_11_d_boxed0));
                  return java.lang.Integer.compareUnsigned(_10_a, _11_d) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed1, _11_d_boxed1) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed1));
                    byte _11_d = ((byte)(java.lang.Object)(_11_d_boxed1));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_d) < 0;
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
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed2, _11_d_boxed2) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed2));
                    byte _11_d = ((byte)(java.lang.Object)(_11_d_boxed2));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_d) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed3, _11_d_boxed3) -> {
                      byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed3));
                      byte _11_d = ((byte)(java.lang.Object)(_11_d_boxed3));
                      return java.lang.Integer.compareUnsigned(_10_a, _11_d) < 0;
                    })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_16_s)) && ((dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>>intersection((_16_s).keySet(), _15_requiredEncryptionContextKeys)).equals(_15_requiredEncryptionContextKeys))) {
                      _coll4.add(_16_s);
                    }
                  }
                  return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll4);
                })).apply()).apply(_0_encryptionContext, _5_requiredEncryptionContextKeys)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_13_reproducedEncryptionContext)) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(AllDefaultCmm_Compile.__default.StaticAlgorithmSuite()), AllDefaultCmm_Compile.__default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_17_a_boxed0, _18_d_boxed0) -> {
  byte _17_a = ((byte)(java.lang.Object)(_17_a_boxed0));
  byte _18_d = ((byte)(java.lang.Object)(_18_d_boxed0));
  return java.lang.Integer.compareUnsigned(_17_a, _18_d) < 0;
}))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo.create(dafny.DafnySequence.asString("us-west-2-decryptable"))), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_19_a_boxed0, _20_d_boxed0) -> {
  byte _19_a = ((byte)(java.lang.Object)(_19_a_boxed0));
  byte _20_d = ((byte)(java.lang.Object)(_20_d_boxed0));
  return java.lang.Integer.compareUnsigned(_19_a, _20_d) < 0;
})))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo.create(dafny.DafnySequence.asString("us-west-2-decryptable"))), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_21_a_boxed0, _22_d_boxed0) -> {
  byte _21_a = ((byte)(java.lang.Object)(_21_a_boxed0));
  byte _22_d = ((byte)(java.lang.Object)(_22_d_boxed0));
  return java.lang.Integer.compareUnsigned(_21_a, _22_d) < 0;
})))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _13_reproducedEncryptionContext)));
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContextReplacementChar()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0_boxed0 : (__default.replacementCharEC()).Elements()) {
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_0 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _0_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_0;
        if ((__default.replacementCharEC()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_0_encryptionContext)) {
          for (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1_boxed0 : (((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_1_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
            java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll1 = new java.util.ArrayList<>();
            for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed0, _3_replacementChar_boxed0) -> {
              byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed0));
              byte _3_replacementChar = ((byte)(java.lang.Object)(_3_replacementChar_boxed0));
              return java.lang.Integer.compareUnsigned(_2_a, _3_replacementChar) < 0;
            })))).Elements()) {
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_2 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_2_boxed0));
              dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _4_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_2;
              if (((AllDefaultCmm_Compile.__default.SubSets(_1_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_1_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed1, _3_replacementChar_boxed1) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed1));
                byte _3_replacementChar = ((byte)(java.lang.Object)(_3_replacementChar_boxed1));
                return java.lang.Integer.compareUnsigned(_2_a, _3_replacementChar) < 0;
              })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_4_s)) && ((java.math.BigInteger.valueOf((_4_s).size())).signum() != 0)) {
                _coll1.add((_4_s).keySet());
              }
            }
            return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll1);
          })).apply()).apply(_0_encryptionContext)).Elements()) {
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_1 = ((dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_1_boxed0));
            dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _5_requiredEncryptionContextKeys = (dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_1;
            if ((((java.util.function.Function<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_6_encryptionContext) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
              java.util.ArrayList<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll2 = new java.util.ArrayList<>();
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed2, _3_replacementChar_boxed2) -> {
                byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed2));
                byte _3_replacementChar = ((byte)(java.lang.Object)(_3_replacementChar_boxed2));
                return java.lang.Integer.compareUnsigned(_2_a, _3_replacementChar) < 0;
              })))).Elements()) {
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _7_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                if (((AllDefaultCmm_Compile.__default.SubSets(_6_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_6_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_2_a_boxed3, _3_replacementChar_boxed3) -> {
                  byte _2_a = ((byte)(java.lang.Object)(_2_a_boxed3));
                  byte _3_replacementChar = ((byte)(java.lang.Object)(_3_replacementChar_boxed3));
                  return java.lang.Integer.compareUnsigned(_2_a, _3_replacementChar) < 0;
                })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_7_s)) && ((java.math.BigInteger.valueOf((_7_s).size())).signum() != 0)) {
                  _coll2.add((_7_s).keySet());
                }
              }
              return new dafny.DafnySet<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll2);
            })).apply()).apply(_0_encryptionContext)).<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_5_requiredEncryptionContextKeys)) {
              for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_4_boxed0 : (((dafny.Function2<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>, dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(_8_encryptionContext, _9_requiredEncryptionContextKeys) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>>)(() -> {
                java.util.ArrayList<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>> _coll3 = new java.util.ArrayList<>();
                for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed0, _11_replacementChar_boxed0) -> {
                  byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed0));
                  byte _11_replacementChar = ((byte)(java.lang.Object)(_11_replacementChar_boxed0));
                  return java.lang.Integer.compareUnsigned(_10_a, _11_replacementChar) < 0;
                })))).Elements()) {
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_5 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_5_boxed0));
                  dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _12_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_5;
                  if (((AllDefaultCmm_Compile.__default.SubSets(_8_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_8_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed1, _11_replacementChar_boxed1) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed1));
                    byte _11_replacementChar = ((byte)(java.lang.Object)(_11_replacementChar_boxed1));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_replacementChar) < 0;
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
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6_boxed0 : (AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed2, _11_replacementChar_boxed2) -> {
                    byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed2));
                    byte _11_replacementChar = ((byte)(java.lang.Object)(_11_replacementChar_boxed2));
                    return java.lang.Integer.compareUnsigned(_10_a, _11_replacementChar) < 0;
                  })))).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_6 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_6_boxed0));
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _16_s = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_6;
                    if (((AllDefaultCmm_Compile.__default.SubSets(_14_encryptionContext, SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), (_14_encryptionContext).keySet(), ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_10_a_boxed3, _11_replacementChar_boxed3) -> {
                      byte _10_a = ((byte)(java.lang.Object)(_10_a_boxed3));
                      byte _11_replacementChar = ((byte)(java.lang.Object)(_11_replacementChar_boxed3));
                      return java.lang.Integer.compareUnsigned(_10_a, _11_replacementChar) < 0;
                    })))).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_16_s)) && ((dafny.DafnySet.<dafny.DafnySequence<? extends java.lang.Byte>>intersection((_16_s).keySet(), _15_requiredEncryptionContextKeys)).equals(_15_requiredEncryptionContextKeys))) {
                      _coll4.add(_16_s);
                    }
                  }
                  return new dafny.DafnySet<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>(_coll4);
                })).apply()).apply(_0_encryptionContext, _5_requiredEncryptionContextKeys)).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_13_reproducedEncryptionContext)) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.asString("Success testing requiredEncryptionContextKeys/reproducedEncryptionContext"), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _0_encryptionContext, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(AllDefaultCmm_Compile.__default.StaticAlgorithmSuite()), AllDefaultCmm_Compile.__default.StaticAlgorithmSuite(), Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_17_a_boxed0, _18_replacementChar_boxed0) -> {
  byte _17_a = ((byte)(java.lang.Object)(_17_a_boxed0));
  byte _18_replacementChar = ((byte)(java.lang.Object)(_18_replacementChar_boxed0));
  return java.lang.Integer.compareUnsigned(_17_a, _18_replacementChar) < 0;
}))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo.create(dafny.DafnySequence.asString("us-west-2-decryptable"))), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_19_a_boxed0, _20_replacementChar_boxed0) -> {
  byte _19_a = ((byte)(java.lang.Object)(_19_a_boxed0));
  byte _20_replacementChar = ((byte)(java.lang.Object)(_20_replacementChar_boxed0));
  return java.lang.Integer.compareUnsigned(_19_a, _20_replacementChar) < 0;
})))), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RequiredEncryptionContext(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RequiredEncryptionContextCMM.create(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Kms(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KMSInfo.create(dafny.DafnySequence.asString("us-west-2-decryptable"))), SortedSets.__default.<java.lang.Byte>SetToOrderedSequence2(BoundedInts_Compile.uint8._typeDescriptor(), _5_requiredEncryptionContextKeys, ((dafny.Function2<java.lang.Byte, java.lang.Byte, Boolean>)(_21_a_boxed0, _22_replacementChar_boxed0) -> {
  byte _21_a = ((byte)(java.lang.Object)(_21_a_boxed0));
  byte _22_replacementChar = ((byte)(java.lang.Object)(_22_replacementChar_boxed0));
  return java.lang.Integer.compareUnsigned(_21_a, _22_replacementChar) < 0;
})))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), _13_reproducedEncryptionContext)));
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector> empty(), __default.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContextPsi()), __default.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext()), __default.FailureBadReproducedEncryptionContext()), __default.SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContextReplacementChar());
  }
  @Override
  public java.lang.String toString() {
    return "AllRequiredEncryptionContextCmm._default";
  }
}
