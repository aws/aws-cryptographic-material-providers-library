// Class __default
// Dafny class __default compiled into Java
package StrictMultiKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> StrictMultiKeyring(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> generator, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> awsKmsKeys, software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens)
  {
    Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _0_allStrings;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _source0 = generator;
    if (_source0.is_None()) {
      _0_allStrings = (awsKmsKeys).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    } else {
      dafny.DafnySequence<? extends Character> _1___mcc_h0 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends Character>>)_source0)._value;
      dafny.DafnySequence<? extends Character> _2_g = _1___mcc_h0;
      _0_allStrings = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>concatenate(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> of(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_g), (awsKmsKeys).UnwrapOr(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier>_typeDescriptor(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier> empty(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()));
    _3_valueOrError0 = (Seq_Compile.__default.<dafny.DafnySequence<? extends Character>, AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>>MapWithResult(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), AwsArnParsing_Compile.__default::IsAwsKmsIdentifierString, _0_allStrings)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier>_typeDescriptor(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_3_valueOrError0).IsFailure(dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier>_typeDescriptor(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_3_valueOrError0).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier>_typeDescriptor(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends AwsArnParsing_Compile.AwsKmsIdentifier> _4_allIdentifiers;
    _4_allIdentifiers = (_3_valueOrError0).Extract(dafny.DafnySequence.<AwsArnParsing_Compile.AwsKmsIdentifier>_typeDescriptor(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Option<AwsKmsKeyring_Compile.AwsKmsKeyring> _5_generatorKeyring = Wrappers_Compile.Option.<AwsKmsKeyring_Compile.AwsKmsKeyring>Default(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _source1 = generator;
    if (_source1.is_None()) {
      _5_generatorKeyring = Wrappers_Compile.Option.<AwsKmsKeyring_Compile.AwsKmsKeyring>create_None(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)));
    } else {
      dafny.DafnySequence<? extends Character> _6___mcc_h1 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends Character>>)_source1)._value;
      dafny.DafnySequence<? extends Character> _7_generatorIdentifier = _6___mcc_h1;
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError1 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _8_valueOrError1 = (AwsArnParsing_Compile.__default.IsAwsKmsIdentifierString(_7_generatorIdentifier)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_8_valueOrError1).IsFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_8_valueOrError1).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
        return output;
      }
      AwsArnParsing_Compile.AwsKmsIdentifier _9_arn;
      _9_arn = (_8_valueOrError1).Extract(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _10_region;
      _10_region = AwsArnParsing_Compile.__default.GetRegion(_9_arn);
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create((_10_region).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString(""))));
      _11_valueOrError2 = _out0;
      if ((_11_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_11_valueOrError2).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _12_client;
      _12_client = (_11_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      AwsKmsKeyring_Compile.AwsKmsKeyring _13_g;
      AwsKmsKeyring_Compile.AwsKmsKeyring _nw0 = new AwsKmsKeyring_Compile.AwsKmsKeyring();
      _nw0.__ctor(_12_client, _7_generatorIdentifier, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
      _13_g = _nw0;
      _5_generatorKeyring = Wrappers_Compile.Option.<AwsKmsKeyring_Compile.AwsKmsKeyring>create_Some(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)), _13_g);
    }
    dafny.DafnySequence<? extends AwsKmsKeyring_Compile.AwsKmsKeyring> _14_children;
    _14_children = dafny.DafnySequence.<AwsKmsKeyring_Compile.AwsKmsKeyring> empty(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _source2 = awsKmsKeys;
    if (_source2.is_None()) {
      _14_children = dafny.DafnySequence.<AwsKmsKeyring_Compile.AwsKmsKeyring> empty(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)));
    } else {
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _15___mcc_h2 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>)_source2)._value;
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _16_childIdentifiers = _15___mcc_h2;
      long _hi0 = (long) (_16_childIdentifiers).cardinalityInt();
      for (long _17_index = (long) 0L; java.lang.Long.compareUnsigned(_17_index, _hi0) < 0; _17_index++) {
        dafny.DafnySequence<? extends Character> _18_childIdentifier;
        _18_childIdentifier = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_16_childIdentifiers).select(dafny.Helpers.unsignedToInt(_17_index))));
        Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError3 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _19_valueOrError3 = (AwsArnParsing_Compile.__default.IsAwsKmsIdentifierString(_18_childIdentifier)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
        if ((_19_valueOrError3).IsFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_19_valueOrError3).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
          return output;
        }
        AwsArnParsing_Compile.AwsKmsIdentifier _20_info;
        _20_info = (_19_valueOrError3).Extract(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _21_region;
        _21_region = AwsArnParsing_Compile.__default.GetRegion(_20_info);
        Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create((_21_region).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString(""))));
        _22_valueOrError4 = _out1;
        if ((_22_valueOrError4).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_22_valueOrError4).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
          return output;
        }
        software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _23_client;
        _23_client = (_22_valueOrError4).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        AwsKmsKeyring_Compile.AwsKmsKeyring _24_keyring;
        AwsKmsKeyring_Compile.AwsKmsKeyring _nw1 = new AwsKmsKeyring_Compile.AwsKmsKeyring();
        _nw1.__ctor(_23_client, _18_childIdentifier, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
        _24_keyring = _nw1;
        _14_children = dafny.DafnySequence.<AwsKmsKeyring_Compile.AwsKmsKeyring>concatenate(_14_children, dafny.DafnySequence.<AwsKmsKeyring_Compile.AwsKmsKeyring> of(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)), _24_keyring));
      }
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _25_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_5_generatorKeyring).is_Some()) || ((((long) (_14_children).cardinalityInt()) == 0 ? 0 : 1) == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("generatorKeyring or child Keryings needed to create a multi keyring")));
    if ((_25_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_25_valueOrError5).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    MultiKeyring_Compile.MultiKeyring _26_keyring;
    MultiKeyring_Compile.MultiKeyring _nw2 = new MultiKeyring_Compile.MultiKeyring();
    _nw2.__ctor(((Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)(_5_generatorKeyring)), _14_children);
    _26_keyring = _nw2;
    output = Wrappers_Compile.Result.<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _26_keyring);
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "StrictMultiKeyring._default";
  }
}
