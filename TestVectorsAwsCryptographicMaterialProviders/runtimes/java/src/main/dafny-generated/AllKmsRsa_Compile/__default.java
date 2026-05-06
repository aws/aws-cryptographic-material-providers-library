// Class __default
// Dafny class __default compiled into Java
package AllKmsRsa_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> AllKmsRsaKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("us-west-2-rsa-mrk"));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.AllKmsRsaKeys()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.AllKmsRsaKeys()).contains(_0_key)) {
          for (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_1_boxed0 : (((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>>)(() -> {
            java.util.ArrayList<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec> _coll1 = new java.util.ArrayList<>();
            for (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_2_boxed0 : software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.AllSingletonConstructors()) {
              software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_2 = ((software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)(java.lang.Object)(_compr_2_boxed0));
              software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _1_e = (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)_compr_2;
              if (!((_1_e).is_SYMMETRIC__DEFAULT())) {
                _coll1.add(_1_e);
              }
            }
            return new dafny.DafnySet<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>(_coll1);
          })).apply()).Elements()) {
            software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_1 = ((software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _2_encryptionAlgorithm = (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)_compr_1;
            if ((((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>>)(() -> {
              java.util.ArrayList<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec> _coll2 = new java.util.ArrayList<>();
              for (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_3_boxed0 : software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.AllSingletonConstructors()) {
                software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _compr_3 = ((software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)(java.lang.Object)(_compr_3_boxed0));
                software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _3_e = (software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec)_compr_3;
                if (!((_3_e).is_SYMMETRIC__DEFAULT())) {
                  _coll2.add(_3_e);
                }
              }
              return new dafny.DafnySet<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>(_coll2);
            })).apply()).<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>contains(_2_encryptionAlgorithm)) {
              _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsRsa(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsRsaKeyring.create(_0_key, _2_encryptionAlgorithm)));
            }
          }
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> algorithmSuites()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_0_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_0;
        if (AlgorithmSuites_Compile.AlgorithmSuite._Is(_0_suite)) {
          if (((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_0_suite)) && (!(((_0_suite).dtor_signature()).is_ECDSA()))) {
            _coll0.add(_0_suite);
          }
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.KeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_keyDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.KeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_keyDescription)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1_boxed0 : (__default.algorithmSuites()).Elements()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_1;
            if ((__default.algorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_1_algorithmSuite)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _2_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_2;
                if (java.util.Objects.equals(_2_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_1_algorithmSuite))) {
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated KMS RSA "), ((_0_keyDescription).dtor_KmsRsa()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_keyDescription, _0_keyDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
    return "AllKmsRsa._default";
  }
}
