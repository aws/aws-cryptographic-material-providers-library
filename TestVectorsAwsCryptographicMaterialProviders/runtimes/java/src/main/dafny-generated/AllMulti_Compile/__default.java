// Class __default
// Dafny class __default compiled into Java
package AllMulti_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> getChildKeyrings(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> keys, dafny.DafnySequence<? extends Character> key, java.math.BigInteger i)
  {
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _0___accumulator = dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> empty(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor());
    TAIL_CALL_START: while (true) {
      if (java.util.Objects.equals(i, java.math.BigInteger.valueOf((keys).length()))) {
        return dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>concatenate(_0___accumulator, dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> empty(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor()));
      } else if ((((dafny.DafnySequence<? extends Character>)(java.lang.Object)((keys).select(dafny.Helpers.toInt((i)))))).equals(key)) {
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in0 = keys;
        dafny.DafnySequence<? extends Character> _in1 = key;
        java.math.BigInteger _in2 = (i).add(java.math.BigInteger.ONE);
        keys = _in0;
        key = _in1;
        i = _in2;
        continue TAIL_CALL_START;
      } else {
        _0___accumulator = dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>concatenate(_0___accumulator, dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> of(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(((dafny.DafnySequence<? extends Character>)(java.lang.Object)((keys).select(dafny.Helpers.toInt((i))))), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((keys).select(dafny.Helpers.toInt((i))))))))));
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _in3 = keys;
        dafny.DafnySequence<? extends Character> _in4 = key;
        java.math.BigInteger _in5 = (i).add(java.math.BigInteger.ONE);
        keys = _in3;
        key = _in4;
        i = _in5;
        continue TAIL_CALL_START;
      }
    }
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptionsGeneratorAndChildren()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (AllRawAES_Compile.__default.aesPersistentKeyNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((AllRawAES_Compile.__default.aesPersistentKeyNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Multi(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring.create(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>create_Some(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(_0_key, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), _0_key)))), __default.getChildKeyrings(AllRawAES_Compile.__default.aesPersistentKeyNames(), _0_key, java.math.BigInteger.ZERO))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> OnlyGeneratorKeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (AllRawAES_Compile.__default.aesPersistentKeyNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((AllRawAES_Compile.__default.aesPersistentKeyNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_Multi(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.MultiKeyring.create(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>create_Some(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor(), software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(_0_key, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), _0_key)))), dafny.DafnySequence.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> empty(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription._typeDescriptor()))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.OnlyGeneratorKeyDescriptions(), __default.KeyDescriptionsGeneratorAndChildren());
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.KeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.KeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("MultiKeyring "), (((((_0_keyDescription).dtor_Multi()).dtor_generator()).dtor_value()).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  @Override
  public java.lang.String toString() {
    return "AllMulti._default";
  }
}
