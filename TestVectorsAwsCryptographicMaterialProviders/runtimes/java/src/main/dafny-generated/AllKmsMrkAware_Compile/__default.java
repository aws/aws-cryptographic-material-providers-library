// Class __default
// Dafny class __default compiled into Java
package AllKmsMrkAware_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> AllAwsKMSMrkKeys()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("us-west-2-mrk"), dafny.DafnySequence.asString("us-east-1-mrk"));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.AllAwsKMSMrkKeys()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.AllAwsKMSMrkKeys()).contains(_0_key)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsMrk(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAware.create(_0_key)));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (__default.KeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_encryptDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((__default.KeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_encryptDescription)) {
          for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1_boxed0 : (__default.KeyDescriptions()).Elements()) {
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _1_decryptDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_1;
            if ((__default.KeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_1_decryptDescription)) {
              for (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2_boxed0 : (AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).Elements()) {
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _compr_2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)(java.lang.Object)(_compr_2_boxed0));
                software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_algorithmSuite = (software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo)_compr_2;
                if ((AllAlgorithmSuites_Compile.__default.AllAlgorithmSuites()).<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo>contains(_2_algorithmSuite)) {
                  for (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3_boxed0 : java.util.Arrays.asList(AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _compr_3 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)(java.lang.Object)(_compr_3_boxed0));
                    software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy _3_commitmentPolicy = (software.amazon.cryptography.materialproviders.internaldafny.types.CommitmentPolicy)_compr_3;
                    if (java.util.Objects.equals(_3_commitmentPolicy, AllAlgorithmSuites_Compile.__default.GetCompatibleCommitmentPolicy(_2_algorithmSuite))) {
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated KMS MRK "), ((_0_encryptDescription).dtor_KmsMrk()).dtor_keyId()), dafny.DafnySequence.asString("->")), ((_1_decryptDescription).dtor_KmsMrk()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _3_commitmentPolicy, _2_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_encryptDescription, _1_decryptDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
  @Override
  public java.lang.String toString() {
    return "AllKmsMrkAware._default";
  }
}
