// Class __default
// Dafny class __default compiled into Java
package AllRawECDH_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> ecdhCurveNames()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("ecc-256"), dafny.DafnySequence.asString("ecc-384"), dafny.DafnySequence.asString("ecc-521"));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> EphemeralKeyDescriptionsEncrypt()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.ecdhCurveNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.ecdhCurveNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_ECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh.create(dafny.DafnySequence.asString("ephemeral"), dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.asString("ephemeral"), dafny.DafnySequence.asString("recipient-material-public-key"), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-ephemeral "), _0_key), _0_key, dafny.DafnySequence.asString("ephemeral"))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> DiscoveryKeyDescriptionsDecrypt()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.ecdhCurveNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.ecdhCurveNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_ECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh.create(dafny.DafnySequence.asString("discovery"), dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.asString("discovery"), dafny.DafnySequence.asString("recipient-material-public-key"), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-discovery "), _0_key), _0_key, dafny.DafnySequence.asString("discovery"))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> SenderKeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.ecdhCurveNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.ecdhCurveNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_ECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh.create(dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.asString("sender-material-public-key"), dafny.DafnySequence.asString("recipient-material-public-key"), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-static "), _0_key), _0_key, dafny.DafnySequence.asString("static"))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> RecipientKeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.ecdhCurveNames()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.ecdhCurveNames()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_ECDH(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawEcdh.create(dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.<Character>concatenate(_0_key, dafny.DafnySequence.asString("-private")), dafny.DafnySequence.asString("sender-material-public-key"), dafny.DafnySequence.asString("recipient-material-public-key"), dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-static "), _0_key), _0_key, dafny.DafnySequence.asString("static"))));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> EphemeralDiscoveryTests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.EphemeralKeyDescriptionsEncrypt()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_encryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.EphemeralKeyDescriptionsEncrypt()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_encryptKeyDescription)) {
          for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1_boxed0 : (__default.DiscoveryKeyDescriptionsDecrypt()).Elements()) {
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _1_decryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_1;
            if (((__default.DiscoveryKeyDescriptionsDecrypt()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_1_decryptKeyDescription)) && ((((_1_decryptKeyDescription).dtor_ECDH()).dtor_curveSpec()).equals(((_0_encryptKeyDescription).dtor_ECDH()).dtor_curveSpec()))) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_2;
                if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_2_algorithmSuite)) {
                  for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_3_boxed0));
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _3_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_3;
                    if (java.util.Objects.equals(_3_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawECDH Ephemeral-Discovery "), ((_0_encryptKeyDescription).dtor_ECDH()).dtor_senderKeyId()), dafny.DafnySequence.asString(" ")), ((_1_decryptKeyDescription).dtor_ECDH()).dtor_recipientKeyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _3_commitmentPolicy, _2_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_encryptKeyDescription, _1_decryptKeyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> StaticSenderDiscoveryRecipientTests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.SenderKeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_encryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.SenderKeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_encryptKeyDescription)) {
          for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1_boxed0 : (__default.DiscoveryKeyDescriptionsDecrypt()).Elements()) {
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _1_decryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_1;
            if (((__default.DiscoveryKeyDescriptionsDecrypt()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_1_decryptKeyDescription)) && ((((_1_decryptKeyDescription).dtor_ECDH()).dtor_curveSpec()).equals(((_0_encryptKeyDescription).dtor_ECDH()).dtor_curveSpec()))) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_2;
                if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_2_algorithmSuite)) {
                  for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_3_boxed0));
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _3_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_3;
                    if (java.util.Objects.equals(_3_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawECDH Static "), ((_0_encryptKeyDescription).dtor_ECDH()).dtor_senderKeyId()), dafny.DafnySequence.asString(" Discovery ")), ((_1_decryptKeyDescription).dtor_ECDH()).dtor_recipientKeyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _3_commitmentPolicy, _2_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_encryptKeyDescription, _1_decryptKeyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> StaticSenderRecipientTests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.SenderKeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_encryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.SenderKeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_encryptKeyDescription)) {
          for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1_boxed0 : (__default.RecipientKeyDescriptions()).Elements()) {
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _1_decryptKeyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_1;
            if (((__default.RecipientKeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_1_decryptKeyDescription)) && ((((_1_decryptKeyDescription).dtor_ECDH()).dtor_curveSpec()).equals(((_0_encryptKeyDescription).dtor_ECDH()).dtor_curveSpec()))) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_2;
                if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_2_algorithmSuite)) {
                  for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_3_boxed0));
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _3_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_3;
                    if (java.util.Objects.equals(_3_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawECDH Static "), ((_0_encryptKeyDescription).dtor_ECDH()).dtor_senderKeyId()), dafny.DafnySequence.asString(" ")), ((_1_decryptKeyDescription).dtor_ECDH()).dtor_senderKeyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _3_commitmentPolicy, _2_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_encryptKeyDescription, _1_decryptKeyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
    return dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(dafny.DafnySet.<TestVectors_Compile.EncryptTestVector>union(__default.EphemeralDiscoveryTests(), __default.StaticSenderRecipientTests()), __default.StaticSenderDiscoveryRecipientTests());
  }
  @Override
  public java.lang.String toString() {
    return "AllRawECDH._default";
  }
}
