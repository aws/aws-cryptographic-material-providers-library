// Class __default
// Dafny class __default compiled into Java
package AllKmsMrkAwareDiscovery_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySet<? extends Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>> AllDiscoveryFilters()
  {
    return dafny.DafnySet.<Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>> of(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>create_Some(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter.create(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("658956600833")), dafny.DafnySequence.asString("aws"))), Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>create_None(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor()));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _compr_0_boxed0 : (__default.AllDiscoveryFilters()).Elements()) {
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _compr_0 = ((Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>)(java.lang.Object)(_compr_0_boxed0));
        Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _0_filter = (Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>)_compr_0;
        if ((__default.AllDiscoveryFilters()).<Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>>contains(_0_filter)) {
          _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_KmsMrkDiscovery(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KmsMrkAwareDiscovery.create(dafny.DafnySequence.asString(""), dafny.DafnySequence.asString("us-west-2"), _0_filter)));
        }
      }
      return new dafny.DafnySet<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>(_coll0);
    })).apply();
  }
  public static dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector> Tests()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends TestVectors_Compile.EncryptTestVector>>)(() -> {
      java.util.ArrayList<TestVectors_Compile.EncryptTestVector> _coll0 = new java.util.ArrayList<>();
      for (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0_boxed0 : (AllKmsMrkAware_Compile.__default.KeyDescriptions()).Elements()) {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _compr_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(_compr_0_boxed0));
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _0_encryptDescription = (software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)_compr_0;
        if ((AllKmsMrkAware_Compile.__default.KeyDescriptions()).<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>contains(_0_encryptDescription)) {
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
                      _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated Discovery KMS MRK "), ((_0_encryptDescription).dtor_KmsMrk()).dtor_keyId()), dafny.DafnySequence.asString("->")), (((((_1_decryptDescription).dtor_KmsMrkDiscovery()).dtor_awsKmsDiscoveryFilter()).is_Some()) ? (dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Filter "), ((((_1_decryptDescription).dtor_KmsMrkDiscovery()).dtor_awsKmsDiscoveryFilter()).dtor_value()).dtor_partition()), dafny.DafnySequence.asString(" ")), Seq_Compile.__default.<Character>Flatten(dafny.TypeDescriptor.CHAR, ((((_1_decryptDescription).dtor_KmsMrkDiscovery()).dtor_awsKmsDiscoveryFilter()).dtor_value()).dtor_accountIds()))) : (dafny.DafnySequence.asString("No Filter")))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _3_commitmentPolicy, _2_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), _0_encryptDescription, _1_decryptDescription, Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> AwsPartitions()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("aws"));
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> AWSAccounts()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("658956600833"));
  }
  @Override
  public java.lang.String toString() {
    return "AllKmsMrkAwareDiscovery._default";
  }
}
