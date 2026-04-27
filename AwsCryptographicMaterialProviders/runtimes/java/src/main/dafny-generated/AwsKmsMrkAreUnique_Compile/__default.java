// Class __default
// Dafny class __default compiled into Java
package AwsKmsMrkAreUnique_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> AwsKmsMrkAreUnique(dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier> identifiers) {
    dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier> _0_mrks = Seq_Compile.__default.<AwsArnParsing_Compile.AwsKmsIdentifier>Filter(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), AwsArnParsing_Compile.__default::IsMultiRegionAwsKmsIdentifier, identifiers);
    if ((((long) (_0_mrks).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    } else {
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_mrkKeyIds = Seq_Compile.__default.<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>Map(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), __default::GetKeyId, _0_mrks);
      dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _2_setMrks = Seq_Compile.__default.<dafny.DafnySequence<? extends Character>>ToSet(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_mrkKeyIds);
      if (((long) (_1_mrkKeyIds).cardinalityInt()) == ((long) (_2_setMrks).cardinalityInt())) {
        return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else {
        dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>> _3_duplicateMrkIds = ((java.util.function.Function<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>>)(_4_mrkKeyIds) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>>)(() -> {
          java.util.ArrayList<dafny.DafnySequence<? extends Character>> _coll0 = new java.util.ArrayList<>();
          for (dafny.DafnySequence<? extends Character> _compr_0_boxed0 : (_4_mrkKeyIds).Elements()) {
            dafny.DafnySequence<? extends Character> _compr_0 = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_compr_0_boxed0));
            dafny.DafnySequence<? extends Character> _5_x = (dafny.DafnySequence<? extends Character>)_compr_0;
            if (((_4_mrkKeyIds).contains(_5_x)) && ((dafny.DafnyMultiset.<dafny.DafnySequence<? extends Character>>multiplicity(((_4_mrkKeyIds).asDafnyMultiset()), _5_x)).compareTo(java.math.BigInteger.ONE) >= 0)) {
              _coll0.add(_5_x);
            }
          }
          return new dafny.DafnySet<dafny.DafnySequence<? extends Character>>(_coll0);
        })).apply()).apply(_1_mrkKeyIds);
        java.util.function.Function<AwsArnParsing_Compile.AwsKmsIdentifier, Boolean> _6_isDuplicate = ((java.util.function.Function<dafny.DafnySet<? extends dafny.DafnySequence<? extends Character>>, java.util.function.Function<AwsArnParsing_Compile.AwsKmsIdentifier, Boolean>>)(_7_duplicateMrkIds) -> ((java.util.function.Function<AwsArnParsing_Compile.AwsKmsIdentifier, Boolean>)(_8_identifier_boxed0) -> {
          AwsArnParsing_Compile.AwsKmsIdentifier _8_identifier = ((AwsArnParsing_Compile.AwsKmsIdentifier)(java.lang.Object)(_8_identifier_boxed0));
          return (_7_duplicateMrkIds).<dafny.DafnySequence<? extends Character>>contains(__default.GetKeyId(_8_identifier));
        })).apply(_3_duplicateMrkIds);
        java.util.function.Function<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>> _9_identifierToString = ((java.util.function.Function<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>)(_10_i_boxed0) -> {
          AwsArnParsing_Compile.AwsKmsIdentifier _10_i = ((AwsArnParsing_Compile.AwsKmsIdentifier)(java.lang.Object)(_10_i_boxed0));
          return (_10_i).ToString();
        });
        dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier> _11_duplicateIdentifiers = Seq_Compile.__default.<AwsArnParsing_Compile.AwsKmsIdentifier>Filter(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), _6_isDuplicate, identifiers);
        dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _12_duplicates = Seq_Compile.__default.<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>Map(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _9_identifierToString, _11_duplicateIdentifiers);
        if ((((long) (_12_duplicates).cardinalityInt()) == 0 ? 0 : 1) == 0) {
          return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Impossible")));
        } else {
          return Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Related multi-Region keys: "), StandardLibrary_Compile.__default.<Character>Join(dafny.TypeDescriptor.CHAR, _12_duplicates, dafny.DafnySequence.asString(","))), dafny.DafnySequence.asString("are not allowed."))));
        }
      }
    }
  }
  public static dafny.DafnySequence<? extends Character> GetKeyId(AwsArnParsing_Compile.AwsKmsIdentifier identifier) {
    AwsArnParsing_Compile.AwsKmsIdentifier _source0 = identifier;
    if (_source0.is_AwsKmsArnIdentifier()) {
      AwsArnParsing_Compile.AwsArn _0___mcc_h0 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsArnIdentifier)_source0)._a;
      AwsArnParsing_Compile.AwsArn _1_a = _0___mcc_h0;
      return ((_1_a).dtor_resource()).dtor_value();
    } else {
      AwsArnParsing_Compile.AwsResource _2___mcc_h1 = ((AwsArnParsing_Compile.AwsKmsIdentifier_AwsKmsRawResourceIdentifier)_source0)._r;
      AwsArnParsing_Compile.AwsResource _3_i = _2___mcc_h1;
      return (_3_i).dtor_value();
    }
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsMrkAreUnique._default";
  }
}
