// Class __default
// Dafny class __default compiled into Java
package AllRawAES_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> aesPersistentKeyNames()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("aes-128"), dafny.DafnySequence.asString("aes-256"), dafny.DafnySequence.asString("\uD835\uDfc1-nonascii-\uD800\uDC02-aes-256-\uD835\uDFC1-with-\uFFFD"));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptionsWithPsi()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.aesPersistentKeyNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.aesPersistentKeyNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(_0_key, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), _0_key), dafny.DafnySequence.asString("-\uD835\uDFC1")))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.aesPersistentKeyNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.aesPersistentKeyNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_AES(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawAES.create(_0_key, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), _0_key))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsNoEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES No Encryption Context "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                }
              }
            }
          }
        }
      }
      return new dafny.DafnySet<TestVectors_Compile.EncryptTestVector>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsWitPsiEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.encryptionContextWitPsi()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.encryptionContextWitPsi()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Encryption Context With Psi "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsWitReplacementCharEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.encryptionContextWitReplacementChar()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.encryptionContextWitReplacementChar()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Encryption Context With Psi "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestControlEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.encryptionContextControl()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.encryptionContextControl()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Control Encryption Context "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsBasicEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.encryptionContextBasic()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.encryptionContextBasic()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Basic Encryption Context "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsWithDiffUTF8Ec()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.variedUTF8EncryptionContext()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.variedUTF8EncryptionContext()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES UTF8 Representative values "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsWithOnePairOfHighCodePointUtf8ValuesInEc()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnySequence<? extends java.lang.Byte> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.representativeEncryptionContextUtf8Values()).Elements()) {
                    dafny.DafnySequence<? extends java.lang.Byte> _compr_3 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnySequence<? extends java.lang.Byte> _3_key = (dafny.DafnySequence<? extends java.lang.Byte>)_compr_3;
                      if (UTF8.ValidUTF8Bytes._Is(_3_key)) {
                        if ((EncryptionContextUtils_Compile.__default.representativeEncryptionContextUtf8Values()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_3_key)) {
                          for (dafny.DafnySequence<? extends java.lang.Byte> _compr_4_boxed0 : (EncryptionContextUtils_Compile.__default.representativeEncryptionContextUtf8Values()).Elements()) {
                            dafny.DafnySequence<? extends java.lang.Byte> _compr_4 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_compr_4_boxed0));
                            if (true) {
                              dafny.DafnySequence<? extends java.lang.Byte> _4_value = (dafny.DafnySequence<? extends java.lang.Byte>)_compr_4;
                              if (UTF8.ValidUTF8Bytes._Is(_4_value)) {
                                if ((EncryptionContextUtils_Compile.__default.representativeEncryptionContextUtf8Values()).<dafny.DafnySequence<? extends java.lang.Byte>>contains(_4_value)) {
                                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Mix and Match UTF8 Key Values "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(new dafny.Tuple2(_3_key, _4_value)), _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                                }
                              }
                            }
                          }
                        }
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> TestsWithMultipleUTF8Ec()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((dafny.DafnySet.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>union(__default.KeyDescriptions(), __default.KeyDescriptionsWithPsi())).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  for (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3_boxed0 : (EncryptionContextUtils_Compile.__default.multipleEntriesUTF8EncryptionContext()).Elements()) {
                    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _compr_3 = ((dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)(java.lang.Object)(_compr_3_boxed0));
                    if (true) {
                      dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _3_encryptionContext = (dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>)_compr_3;
                      if ((EncryptionContextUtils_Compile.__default.multipleEntriesUTF8EncryptionContext()).<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>contains(_3_encryptionContext)) {
                        _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawAES Multiple UTF8 Entries EC "), ((_0_keyDescription).dtor_AES()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _3_encryptionContext, _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
                      }
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector> empty(), __default.TestsNoEc()), __default.TestsWitPsiEc()), __default.TestsBasicEc()), __default.TestControlEc()), __default.TestsWitReplacementCharEc()), __default.TestsWithMultipleUTF8Ec());
  }
  @Override
  public java.lang.String toString() {
    return "AllRawAES._default";
  }
}
