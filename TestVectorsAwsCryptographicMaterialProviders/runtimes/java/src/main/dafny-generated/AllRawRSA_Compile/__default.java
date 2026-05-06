// Class __default
// Dafny class __default compiled into Java
package AllRawRSA_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> rsaPersistentKeyNamesWithoutPublicPrivate()
  {
    return dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString("rsa-4096"));
  }
  public static dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> KeyDescriptions()
  {
    return ((dafny.Function0<dafny.DafnySet<? extends software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>>)(() -> {
      java.util.ArrayList<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (__default.rsaPersistentKeyNamesWithoutPublicPrivate()).Elements()) {
        dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends Character> _0_key = (dafny.DafnySequence<? extends Character>)_compr_0;
        if ((__default.rsaPersistentKeyNamesWithoutPublicPrivate()).contains(_0_key)) {
          for (software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _compr_1_boxed0 : software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme.AllSingletonConstructors()) {
            software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _compr_1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme)(java.lang.Object)(_compr_1_boxed0));
            software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _1_padding = (software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme)_compr_1;
            _coll0.add(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RSA(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA.create(_0_key, dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("aws-raw-vectors-persistent-"), _0_key), _1_padding)));
          }
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
                  _coll0.add(TestVectors_Compile.EncryptTestVector.create_PositiveEncryptKeyringVector(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Generated RawRSA "), ((_0_keyDescription).dtor_RSA()).dtor_keyId()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnyMap.fromElements(), _2_commitmentPolicy, _1_algorithmSuite, Wrappers_Compile.Option.<java.lang.Long>create_None(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor())), ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_0_keyDescription, boxed16 -> {
  software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _pat_let8_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(boxed16));
  return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_pat_let8_0, boxed17 -> {
    software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _3_dt__update__tmp_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(boxed17));
    return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let((_0_keyDescription).dtor_RSA(), boxed19 -> {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _pat_let10_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed19));
      return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(_pat_let10_0, boxed20 -> {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _4_dt__update__tmp_h1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed20));
        return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(dafny.DafnySequence.<Character>concatenate(((_0_keyDescription).dtor_RSA()).dtor_keyId(), dafny.DafnySequence.asString("-public")), boxed21 -> {
          dafny.DafnySequence<? extends Character> _pat_let11_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed21));
          return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(_pat_let11_0, boxed22 -> {
            dafny.DafnySequence<? extends Character> _5_dt__update_hkeyId_h0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed22));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA.create(_5_dt__update_hkeyId_h0, (_4_dt__update__tmp_h1).dtor_providerId(), (_4_dt__update__tmp_h1).dtor_padding());
          }
          )));
        }
        )));
      }
      )));
    }
    ))), boxed18 -> {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _pat_let9_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed18));
      return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_pat_let9_0, boxed23 -> {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _6_dt__update_hRSA_h0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed23));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RSA(_6_dt__update_hRSA_h0);
      }
      )));
    }
    )));
  }
  )));
}
))), ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_0_keyDescription, boxed24 -> {
  software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _pat_let12_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(boxed24));
  return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_pat_let12_0, boxed25 -> {
    software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription _7_dt__update__tmp_h2 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(boxed25));
    return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let((_0_keyDescription).dtor_RSA(), boxed27 -> {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _pat_let14_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed27));
      return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(_pat_let14_0, boxed28 -> {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _8_dt__update__tmp_h3 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed28));
        return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(dafny.DafnySequence.<Character>concatenate(((_0_keyDescription).dtor_RSA()).dtor_keyId(), dafny.DafnySequence.asString("-private")), boxed29 -> {
          dafny.DafnySequence<? extends Character> _pat_let15_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed29));
          return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(dafny.Helpers.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA>Let(_pat_let15_0, boxed30 -> {
            dafny.DafnySequence<? extends Character> _9_dt__update_hkeyId_h1 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(boxed30));
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA.create(_9_dt__update_hkeyId_h1, (_8_dt__update__tmp_h3).dtor_providerId(), (_8_dt__update__tmp_h3).dtor_padding());
          }
          )));
        }
        )));
      }
      )));
    }
    ))), boxed26 -> {
      software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _pat_let13_0 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed26));
      return ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription)(java.lang.Object)(dafny.Helpers.<software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA, software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription>Let(_pat_let13_0, boxed31 -> {
        software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA _10_dt__update_hRSA_h1 = ((software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.RawRSA)(java.lang.Object)(boxed31));
        return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription.create_RSA(_10_dt__update_hRSA_h1);
      }
      )));
    }
    )));
  }
  )));
}
))), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()))));
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
    return "AllRawRSA._default";
  }
}
