// Class __default
// Dafny class __default compiled into Java
package AwsCryptographyMaterialProvidersOperations_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _0_valueOrError0 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((input).dtor_kmsKeyId());
    if ((_0_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.Tuple0 _1___v0;
    _1___v0 = (_0_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _2_valueOrError1 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _3_grantTokens;
    _3_grantTokens = (_2_valueOrError1).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsKeyring_Compile.AwsKmsKeyring _4_keyring;
    AwsKmsKeyring_Compile.AwsKmsKeyring _nw0 = new AwsKmsKeyring_Compile.AwsKmsKeyring();
    _nw0.__ctor((input).dtor_kmsClient(), (input).dtor_kmsKeyId(), _3_grantTokens);
    _4_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsKeyring_Compile.AwsKmsKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsKeyring_Compile.AwsKmsKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsKeyring_Compile.AwsKmsKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsDiscoveryKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if (((input).dtor_discoveryFilter()).is_Some()) {
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.ValidateDiscoveryFilter(((input).dtor_discoveryFilter()).dtor_value());
      if ((_0_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.Tuple0 _1___v1;
      _1___v1 = (_0_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _2_valueOrError1 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _3_grantTokens;
    _3_grantTokens = (_2_valueOrError1).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring _4_keyring;
    AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring _nw0 = new AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring();
    _nw0.__ctor((input).dtor_kmsClient(), (input).dtor_discoveryFilter(), _3_grantTokens);
    _4_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMultiKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_grantTokens;
      _1_grantTokens = (_0_valueOrError0).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      if (((input).dtor_clientSupplier()).is_Some()) {
        Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = StrictMultiKeyring_Compile.__default.StrictMultiKeyring((input).dtor_generator(), (input).dtor_kmsKeyIds(), ((input).dtor_clientSupplier()).dtor_value(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _1_grantTokens));
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_out0));
      } else {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = __default.CreateDefaultClientSupplier(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
        _2_valueOrError1 = _out1;
        if ((_2_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _3_clientSupplier;
        _3_clientSupplier = (_2_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
        _out2 = StrictMultiKeyring_Compile.__default.StrictMultiKeyring((input).dtor_generator(), (input).dtor_kmsKeyIds(), _3_clientSupplier, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _1_grantTokens));
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_out2));
      }
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsDiscoveryMultiKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_grantTokens;
      _1_grantTokens = (_0_valueOrError0).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _2_clientSupplier = null;
      if (((input).dtor_clientSupplier()).is_None()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = __default.CreateDefaultClientSupplier(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
        _3_valueOrError1 = _out0;
        if ((_3_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _2_clientSupplier = (_3_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else {
        _2_clientSupplier = ((input).dtor_clientSupplier()).dtor_value();
      }
      Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = DiscoveryMultiKeyring_Compile.__default.DiscoveryMultiKeyring((input).dtor_regions(), (input).dtor_discoveryFilter(), _2_clientSupplier, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _1_grantTokens));
      output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_out1));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _0_valueOrError0 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((input).dtor_kmsKeyId());
    if ((_0_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.Tuple0 _1___v2;
    _1___v2 = (_0_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _2_valueOrError1 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _3_grantTokens;
    _3_grantTokens = (_2_valueOrError1).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _4_keyring;
    AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _nw0 = new AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring();
    _nw0.__ctor((input).dtor_kmsClient(), (input).dtor_kmsKeyId(), _3_grantTokens);
    _4_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkMultiKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_grantTokens;
      _1_grantTokens = (_0_valueOrError0).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _2_clientSupplier = null;
      if (((input).dtor_clientSupplier()).is_None()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = __default.CreateDefaultClientSupplier(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
        _3_valueOrError1 = _out0;
        if ((_3_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _2_clientSupplier = (_3_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else {
        _2_clientSupplier = ((input).dtor_clientSupplier()).dtor_value();
      }
      Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = MrkAwareStrictMultiKeyring_Compile.__default.MrkAwareStrictMultiKeyring((input).dtor_generator(), (input).dtor_kmsKeyIds(), _2_clientSupplier, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _1_grantTokens));
      output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_out1));
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkDiscoveryKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if (((input).dtor_discoveryFilter()).is_Some()) {
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.ValidateDiscoveryFilter(((input).dtor_discoveryFilter()).dtor_value());
      if ((_0_valueOrError0).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.Tuple0 _1___v3;
      _1___v3 = (_0_valueOrError0).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    Wrappers_Compile.Option<Boolean> _2_regionMatch;
    _2_regionMatch = software.amazon.cryptography.services.kms.internaldafny.__default.RegionMatch((input).dtor_kmsClient(), (input).dtor_region());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), !java.util.Objects.equals(_2_regionMatch, Wrappers_Compile.Option.<Boolean>create_Some(dafny.TypeDescriptor.BOOLEAN, false)), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Provided client and region do not match")));
    if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _4_valueOrError2 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_4_valueOrError2).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_4_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _5_grantTokens;
    _5_grantTokens = (_4_valueOrError2).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring _6_keyring;
    AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring _nw0 = new AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring();
    _nw0.__ctor((input).dtor_kmsClient(), (input).dtor_region(), (input).dtor_discoveryFilter(), _5_grantTokens);
    _6_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _6_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkDiscoveryMultiKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
      _0_valueOrError0 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
      if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_grantTokens;
      _1_grantTokens = (_0_valueOrError0).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier _2_clientSupplier = null;
      if (((input).dtor_clientSupplier()).is_None()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = __default.CreateDefaultClientSupplier(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput.create());
        _3_valueOrError1 = _out0;
        if ((_3_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _2_clientSupplier = (_3_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else {
        _2_clientSupplier = ((input).dtor_clientSupplier()).dtor_value();
      }
      Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = MrkAwareDiscoveryMultiKeyring_Compile.__default.MrkAwareDiscoveryMultiKeyring((input).dtor_regions(), (input).dtor_discoveryFilter(), _2_clientSupplier, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _1_grantTokens));
      output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_out1));
    }
    return output;
  }
  public static dafny.DafnySequence<? extends Character> N(long n) {
    return StandardLibrary_mString_Compile.__default.Base10Int2String(java.math.BigInteger.valueOf(n));
  }
  public static Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> CheckCache(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType cache, long ttlSeconds)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if(true) {
      if ((cache).is_StormTracking()) {
        long _0_gracePeriod;
        if (((((cache).dtor_StormTracking()).dtor_timeUnits()).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.TimeUnits.create_Seconds())).is_Seconds()) {
          _0_gracePeriod = ((long) (((cache).dtor_StormTracking()).dtor_gracePeriod()));
        } else {
          _0_gracePeriod = dafny.DafnyEuclidean.EuclideanDivision(((long) (((cache).dtor_StormTracking()).dtor_gracePeriod())), (long) 1000L);
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _1_storm;
        _1_storm = (cache).dtor_StormTracking();
        if ((ttlSeconds) <= (_0_gracePeriod)) {
          dafny.DafnySequence<? extends Character> _2_msg;
          _2_msg = dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("When creating an AwsKmsHierarchicalKeyring with a StormCache, "), dafny.DafnySequence.asString("the ttlSeconds of the KeyRing must be greater than the gracePeriod of the StormCache ")), dafny.DafnySequence.asString("yet the ttlSeconds is ")), __default.N(ttlSeconds)), dafny.DafnySequence.asString(" and the gracePeriod is ")), __default.N(_0_gracePeriod)), dafny.DafnySequence.asString("."));
          output = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Fail(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_2_msg));
          return output;
        }
        output = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        return output;
      } else {
        output = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Pass(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        return output;
      }
    }
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsHierarchicalKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _0_cmc = null;
    if (((input).dtor_cache()).is_Some()) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = __default.CheckCache(((input).dtor_cache()).dtor_value(), (input).dtor_ttlSeconds());
      _1_valueOrError0 = _out0;
      if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_1_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _source0 = ((input).dtor_cache()).dtor_value();
      if (_source0.is_Default()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache _2___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_Default)_source0)._Default;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(((input).dtor_cache()).dtor_value()));
        _3_valueOrError1 = _out1;
        if ((_3_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_3_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _0_cmc = (_3_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else if (_source0.is_No()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.NoCache _4___mcc_h2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_No)_source0)._No;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
        _out2 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(((input).dtor_cache()).dtor_value()));
        _5_valueOrError1 = _out2;
        if ((_5_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _0_cmc = (_5_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else if (_source0.is_SingleThreaded()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache _6___mcc_h4 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_SingleThreaded)_source0)._SingleThreaded;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
        _out3 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(((input).dtor_cache()).dtor_value()));
        _7_valueOrError1 = _out3;
        if ((_7_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_7_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _0_cmc = (_7_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else if (_source0.is_MultiThreaded()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache _8___mcc_h6 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_MultiThreaded)_source0)._MultiThreaded;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
        _out4 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(((input).dtor_cache()).dtor_value()));
        _9_valueOrError1 = _out4;
        if ((_9_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_9_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _0_cmc = (_9_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else if (_source0.is_StormTracking()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _10___mcc_h8 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_StormTracking)_source0)._StormTracking;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
        _out5 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(((input).dtor_cache()).dtor_value()));
        _11_valueOrError1 = _out5;
        if ((_11_valueOrError1).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_11_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _0_cmc = (_11_valueOrError1).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _12___mcc_h10 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_Shared)_source0)._Shared;
        software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _13_c = _12___mcc_h10;
        _0_cmc = _13_c;
      }
    } else {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = __default.CheckCache(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_StormTracking(StormTracker_Compile.__default.DefaultStorm()), (input).dtor_ttlSeconds());
      _14_valueOrError2 = _out6;
      if ((_14_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_14_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out7;
      _out7 = __default.CreateCryptographicMaterialsCache(config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput.create(software.amazon.cryptography.materialproviders.internaldafny.types.CacheType.create_Default(software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache.create(1000))));
      _15_valueOrError3 = _out7;
      if ((_15_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_15_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      _0_cmc = (_15_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    dafny.DafnySequence<? extends java.lang.Byte> _16_partitionIdBytes = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    if (((input).dtor_partitionId()).is_Some()) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
      _17_valueOrError4 = (UTF8.__default.Encode(((input).dtor_partitionId()).dtor_value())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_18_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _18_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_18_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Could not UTF-8 Encode Partition ID: "), _18_e));
      }));
      if ((_17_valueOrError4).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_17_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      _16_partitionIdBytes = (_17_valueOrError4).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    } else {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _19_uuid_q;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>> _out8;
      _out8 = UUID.__default.GenerateUUID();
      _19_uuid_q = _out8;
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _20_valueOrError5 = (_19_uuid_q).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_21_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _21_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_21_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_21_e);
      }));
      if ((_20_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_20_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.DafnySequence<? extends Character> _22_uuid;
      _22_uuid = (_20_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _23_valueOrError6 = (UUID.__default.ToByteArray(_22_uuid)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_24_e_boxed0) -> {
        dafny.DafnySequence<? extends Character> _24_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_24_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_24_e);
      }));
      if ((_23_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_23_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      _16_partitionIdBytes = (_23_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _25_getKeyStoreInfoOutput_q;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.keystore.internaldafny.types.Error> _out9;
    _out9 = ((input).dtor_keyStore()).GetKeyStoreInfo();
    _25_getKeyStoreInfoOutput_q = _out9;
    Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _26_valueOrError7 = (_25_getKeyStoreInfoOutput_q).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.keystore.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.keystore.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_27_e_boxed0) -> {
      software.amazon.cryptography.keystore.internaldafny.types.Error _27_e = ((software.amazon.cryptography.keystore.internaldafny.types.Error)(java.lang.Object)(_27_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyKeyStore(_27_e);
    }));
    if ((_26_valueOrError7).IsFailure(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_26_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput _28_getKeyStoreInfoOutput;
    _28_getKeyStoreInfoOutput = (_26_valueOrError7).Extract(software.amazon.cryptography.keystore.internaldafny.types.GetKeyStoreInfoOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends Character> _29_logicalKeyStoreName;
    _29_logicalKeyStoreName = (_28_getKeyStoreInfoOutput).dtor_logicalKeyStoreName();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _30_valueOrError8 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
    _30_valueOrError8 = (UTF8.__default.Encode(_29_logicalKeyStoreName)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_31_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _31_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_31_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("Could not UTF-8 Encode Logical Key Store Name: "), _31_e));
    }));
    if ((_30_valueOrError8).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_30_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _32_logicalKeyStoreNameBytes;
    _32_logicalKeyStoreNameBytes = (_30_valueOrError8).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _33_valueOrError9 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _33_valueOrError9 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_branchKeyId()).is_None()) || (((input).dtor_branchKeyIdSupplier()).is_None()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Cannot initialize keyring with both a branchKeyId and BranchKeyIdSupplier.")));
    if ((_33_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_33_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _34_valueOrError10 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _34_valueOrError10 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_branchKeyId()).is_Some()) || (((input).dtor_branchKeyIdSupplier()).is_Some()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Must initialize keyring with either branchKeyId or BranchKeyIdSupplier.")));
    if ((_34_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_34_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring _35_keyring;
    AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring _nw0 = new AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring();
    _nw0.__ctor((input).dtor_keyStore(), (input).dtor_branchKeyId(), (input).dtor_branchKeyIdSupplier(), (input).dtor_ttlSeconds(), _0_cmc, _16_partitionIdBytes, _32_logicalKeyStoreNameBytes, (config).dtor_crypto());
    _35_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsHierarchicalKeyring_Compile.AwsKmsHierarchicalKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _35_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsEcdhKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _0_valueOrError0 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _1_grantTokens;
    _1_grantTokens = (_0_valueOrError0).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _2_recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _3_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor());
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _4_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _source0 = (input).dtor_KeyAgreementScheme();
    if (_source0.is_KmsPublicKeyDiscovery()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput _5___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery)_source0)._KmsPublicKeyDiscovery;
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput _6_kmsPublicKeyDiscovery = _5___mcc_h0;
      {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        _7_valueOrError1 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((_6_kmsPublicKeyDiscovery).dtor_recipientKmsIdentifier());
        if ((_7_valueOrError1).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_7_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        dafny.Tuple0 _8___v5;
        _8___v5 = (_7_valueOrError1).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = AwsKmsUtils_Compile.__default.GetEcdhPublicKey((input).dtor_kmsClient(), (_6_kmsPublicKeyDiscovery).dtor_recipientKmsIdentifier());
        _9_valueOrError2 = _out0;
        if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_9_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _2_recipientPublicKey = (_9_valueOrError2).Extract(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _3_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor());
        _4_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput _10___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey)_source0)._KmsPrivateKeyToStaticPublicKey;
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput _11_kmsPrivateKeyToStaticPublicKey = _10___mcc_h1;
      {
        if (((_11_kmsPrivateKeyToStaticPublicKey).dtor_senderPublicKey()).is_Some()) {
          Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          _12_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PublicKeyType(((_11_kmsPrivateKeyToStaticPublicKey).dtor_senderPublicKey()).dtor_value()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid SenderPublicKey length.")));
          if ((_12_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_12_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          _3_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_11_kmsPrivateKeyToStaticPublicKey).dtor_senderPublicKey()).dtor_value());
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
          _out1 = RawECDHKeyring_Compile.__default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((_3_senderPublicKey).dtor_value()), (input).dtor_curveSpec(), (config).dtor_crypto());
          _13_valueOrError4 = _out1;
          if ((_13_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_13_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          dafny.DafnySequence<? extends java.lang.Byte> _14_compressedPKU;
          _14_compressedPKU = (_13_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          _4_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _14_compressedPKU);
        } else {
          Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
          _15_valueOrError5 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((_11_kmsPrivateKeyToStaticPublicKey).dtor_senderKmsIdentifier());
          if ((_15_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_15_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          dafny.Tuple0 _16___v6;
          _16___v6 = (_15_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError6 = (Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
          _out2 = AwsKmsUtils_Compile.__default.GetEcdhPublicKey((input).dtor_kmsClient(), (_11_kmsPrivateKeyToStaticPublicKey).dtor_senderKmsIdentifier());
          _17_valueOrError6 = _out2;
          if ((_17_valueOrError6).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_17_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          dafny.DafnySequence<? extends java.lang.Byte> _18_senderPublicKeyResponse;
          _18_senderPublicKeyResponse = (_17_valueOrError6).Extract(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
          Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
          _out3 = RawECDHKeyring_Compile.__default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_18_senderPublicKeyResponse), (input).dtor_curveSpec(), (config).dtor_crypto());
          _19_valueOrError7 = _out3;
          if ((_19_valueOrError7).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_19_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
            return output;
          }
          dafny.DafnySequence<? extends java.lang.Byte> _20_compressedPKU;
          _20_compressedPKU = (_19_valueOrError7).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          _3_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor(), _18_senderPublicKeyResponse);
          _4_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _20_compressedPKU);
        }
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _21_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PublicKeyType((_11_kmsPrivateKeyToStaticPublicKey).dtor_recipientPublicKey()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid RecipientPublicKey length.")));
        if ((_21_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_21_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        _2_recipientPublicKey = (_11_kmsPrivateKeyToStaticPublicKey).dtor_recipientPublicKey();
      }
    }
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError9 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = RawECDHKeyring_Compile.__default.ValidatePublicKey((config).dtor_crypto(), (input).dtor_curveSpec(), _2_recipientPublicKey);
    _22_valueOrError9 = _out4;
    if ((_22_valueOrError9).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_22_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    boolean _23___v7;
    _23___v7 = (_22_valueOrError9).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError10 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = RawECDHKeyring_Compile.__default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_2_recipientPublicKey), (input).dtor_curveSpec(), (config).dtor_crypto());
    _24_valueOrError10 = _out5;
    if ((_24_valueOrError10).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_24_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _25_compressedRecipientPublicKey;
    _25_compressedRecipientPublicKey = (_24_valueOrError10).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _26_senderKmsKeyId;
    if (((input).dtor_KeyAgreementScheme()).is_KmsPublicKeyDiscovery()) {
      _26_senderKmsKeyId = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_None(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    } else {
      _26_senderKmsKeyId = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (((input).dtor_KeyAgreementScheme()).dtor_KmsPrivateKeyToStaticPublicKey()).dtor_senderKmsIdentifier());
    }
    if ((_26_senderKmsKeyId).is_Some()) {
      Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _27_valueOrError11 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
      _27_valueOrError11 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((_26_senderKmsKeyId).dtor_value());
      if ((_27_valueOrError11).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_27_valueOrError11).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      dafny.Tuple0 _28___v8;
      _28___v8 = (_27_valueOrError11).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    if ((_3_senderPublicKey).is_Some()) {
      Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _29_valueOrError12 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
      Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = RawECDHKeyring_Compile.__default.ValidatePublicKey((config).dtor_crypto(), (input).dtor_curveSpec(), (_3_senderPublicKey).dtor_value());
      _29_valueOrError12 = _out6;
      if ((_29_valueOrError12).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_29_valueOrError12).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      boolean _30___v9;
      _30___v9 = (_29_valueOrError12).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring _31_keyring;
    AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring _nw0 = new AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring();
    _nw0.__ctor((input).dtor_KeyAgreementScheme(), (input).dtor_curveSpec(), (input).dtor_kmsClient(), _1_grantTokens, _26_senderKmsKeyId, _3_senderPublicKey, _2_recipientPublicKey, _4_compressedSenderPublicKey, _25_compressedRecipientPublicKey, (config).dtor_crypto());
    _31_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsEcdhKeyring_Compile.AwsKmsEcdhKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _31_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateMultiKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_generator()).is_Some()) || ((((long) ((input).dtor_childKeyrings()).cardinalityInt()) == 0 ? 0 : 1) == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Must include a generator keyring and/or at least one child keyring")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    MultiKeyring_Compile.MultiKeyring _1_keyring;
    MultiKeyring_Compile.MultiKeyring _nw0 = new MultiKeyring_Compile.MultiKeyring();
    _nw0.__ctor((input).dtor_generator(), (input).dtor_childKeyrings());
    _1_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _1_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawAesKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), !((input).dtor_keyNamespace()).equals(dafny.DafnySequence.asString("aws-kms")), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("keyNamespace must not be `aws-kms`")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_wrappingAlg;
    software.amazon.cryptography.materialproviders.internaldafny.types.AesWrappingAlg _source0 = (input).dtor_wrappingAlg();
    if (_source0.is_ALG__AES128__GCM__IV12__TAG16()) {
      _1_wrappingAlg = software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(16, 16, 12);
    } else if (_source0.is_ALG__AES192__GCM__IV12__TAG16()) {
      _1_wrappingAlg = software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(24, 16, 12);
    } else {
      _1_wrappingAlg = software.amazon.cryptography.primitives.internaldafny.types.AES__GCM.create(32, 16, 12);
    }
    Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>Default(UTF8.ValidUTF8Bytes.defaultValue(), UTF8.ValidUTF8Bytes.defaultValue()));
    _2_valueOrError1 = AwsKmsUtils_Compile.__default.ParseKeyNamespaceAndName((input).dtor_keyNamespace(), (input).dtor_keyName());
    if ((_2_valueOrError1).IsFailure(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _3_namespaceAndName;
    _3_namespaceAndName = (_2_valueOrError1).Extract(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _let_tmp_rhs0 = _3_namespaceAndName;
    dafny.DafnySequence<? extends java.lang.Byte> _4_namespace = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>)_let_tmp_rhs0).dtor__0()));
    dafny.DafnySequence<? extends java.lang.Byte> _5_name = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>)_let_tmp_rhs0).dtor__1()));
    long _6_wrapping__key__size;
    _6_wrapping__key__size = (long) ((input).dtor_wrappingKey()).cardinalityInt();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_6_wrapping__key__size) == ((long) 16L)) || ((_6_wrapping__key__size) == ((long) 24L))) || ((_6_wrapping__key__size) == ((long) 32L)), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid wrapping key length")));
    if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_6_wrapping__key__size) == (((long) ((_1_wrappingAlg).dtor_keyLength()))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Wrapping key length does not match specified wrapping algorithm")));
    if ((_8_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_8_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    RawAESKeyring_Compile.RawAESKeyring _9_keyring;
    RawAESKeyring_Compile.RawAESKeyring _nw0 = new RawAESKeyring_Compile.RawAESKeyring();
    _nw0.__ctor(_4_namespace, _5_name, (input).dtor_wrappingKey(), _1_wrappingAlg, (config).dtor_crypto());
    _9_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<RawAESKeyring_Compile.RawAESKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<RawAESKeyring_Compile.RawAESKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(RawAESKeyring_Compile.RawAESKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _9_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawRsaKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), !((input).dtor_keyNamespace()).equals(dafny.DafnySequence.asString("aws-kms")), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("keyNamespace must not be `aws-kms`")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_publicKey()).is_Some()) || (((input).dtor_privateKey()).is_Some()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A publicKey or a privateKey is required")));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_1_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _2_padding;
    software.amazon.cryptography.materialproviders.internaldafny.types.PaddingScheme _source0 = (input).dtor_paddingScheme();
    if (_source0.is_PKCS1()) {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_PKCS1();
    } else if (_source0.is_OAEP__SHA1__MGF1()) {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA1();
    } else if (_source0.is_OAEP__SHA256__MGF1()) {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA256();
    } else if (_source0.is_OAEP__SHA384__MGF1()) {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA384();
    } else {
      _2_padding = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.create_OAEP__SHA512();
    }
    Wrappers_Compile.Result<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError2 = Wrappers_Compile.Result.<dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>Default(UTF8.ValidUTF8Bytes.defaultValue(), UTF8.ValidUTF8Bytes.defaultValue()));
    _3_valueOrError2 = AwsKmsUtils_Compile.__default.ParseKeyNamespaceAndName((input).dtor_keyNamespace(), (input).dtor_keyName());
    if ((_3_valueOrError2).IsFailure(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_3_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _4_namespaceAndName;
    _4_namespaceAndName = (_3_valueOrError2).Extract(dafny.Tuple2.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(UTF8.ValidUTF8Bytes._typeDescriptor(), UTF8.ValidUTF8Bytes._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _let_tmp_rhs0 = _4_namespaceAndName;
    dafny.DafnySequence<? extends java.lang.Byte> _5_namespace = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>)_let_tmp_rhs0).dtor__0()));
    dafny.DafnySequence<? extends java.lang.Byte> _6_name = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(((dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>>)_let_tmp_rhs0).dtor__1()));
    RawRSAKeyring_Compile.RawRSAKeyring _7_keyring;
    RawRSAKeyring_Compile.RawRSAKeyring _nw0 = new RawRSAKeyring_Compile.RawRSAKeyring();
    _nw0.__ctor(_5_namespace, _6_name, (input).dtor_publicKey(), (input).dtor_privateKey(), _2_padding, (config).dtor_crypto());
    _7_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<RawRSAKeyring_Compile.RawRSAKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<RawRSAKeyring_Compile.RawRSAKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(RawRSAKeyring_Compile.RawRSAKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawEcdhKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    dafny.DafnySequence<? extends java.lang.Byte> _0_recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _1_senderPrivateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _2_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _3_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _source0 = (input).dtor_KeyAgreementScheme();
    if (_source0.is_PublicKeyDiscovery()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput _4___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_PublicKeyDiscovery)_source0)._PublicKeyDiscovery;
      software.amazon.cryptography.materialproviders.internaldafny.types.PublicKeyDiscoveryInput _5_publicKeyDiscovery = _4___mcc_h0;
      {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = Utils_Compile.__default.GetPublicKey((input).dtor_curveSpec(), software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create((_5_publicKeyDiscovery).dtor_recipientStaticPrivateKey()), (config).dtor_crypto());
        _6_valueOrError3 = _out0;
        if ((_6_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_6_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        dafny.DafnySequence<? extends java.lang.Byte> _7_reproducedPublicKey;
        _7_reproducedPublicKey = (_6_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _0_recipientPublicKey = _7_reproducedPublicKey;
        _1_senderPrivateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        _2_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        _3_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      }
    } else if (_source0.is_RawPrivateKeyToStaticPublicKey()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput _8___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey)_source0)._RawPrivateKeyToStaticPublicKey;
      software.amazon.cryptography.materialproviders.internaldafny.types.RawPrivateKeyToStaticPublicKeyInput _9_rawPrivateKeyToStaticPublicKey = _8___mcc_h1;
      {
        _0_recipientPublicKey = (_9_rawPrivateKeyToStaticPublicKey).dtor_recipientPublicKey();
        _1_senderPrivateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (_9_rawPrivateKeyToStaticPublicKey).dtor_senderStaticPrivateKey());
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = Utils_Compile.__default.GetPublicKey((input).dtor_curveSpec(), software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create((_1_senderPrivateKey).dtor_value()), (config).dtor_crypto());
        _10_valueOrError0 = _out1;
        if ((_10_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_10_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        dafny.DafnySequence<? extends java.lang.Byte> _11_reproducedPublicKey;
        _11_reproducedPublicKey = (_10_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError1 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
        Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
        _out2 = RawECDHKeyring_Compile.__default.ValidatePublicKey((config).dtor_crypto(), (input).dtor_curveSpec(), _11_reproducedPublicKey);
        _12_valueOrError1 = _out2;
        if ((_12_valueOrError1).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_12_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        boolean _13___v10;
        _13___v10 = (_12_valueOrError1).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _2_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _11_reproducedPublicKey);
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
        _out3 = RawECDHKeyring_Compile.__default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_11_reproducedPublicKey), (input).dtor_curveSpec(), (config).dtor_crypto());
        _14_valueOrError2 = _out3;
        if ((_14_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_14_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
          return output;
        }
        dafny.DafnySequence<? extends java.lang.Byte> _15_compressedSenderPublicKey_q;
        _15_compressedSenderPublicKey_q = (_14_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _3_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), _15_compressedSenderPublicKey_q);
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput _16___mcc_h2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey)_source0)._EphemeralPrivateKeyToStaticPublicKey;
      software.amazon.cryptography.materialproviders.internaldafny.types.EphemeralPrivateKeyToStaticPublicKeyInput _17_ephemeralPrivateKeyToStaticPublicKey = _16___mcc_h2;
      {
        _0_recipientPublicKey = (_17_ephemeralPrivateKeyToStaticPublicKey).dtor_recipientPublicKey();
        _1_senderPrivateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        _2_senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        _3_compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      }
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = RawECDHKeyring_Compile.__default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_0_recipientPublicKey), (input).dtor_curveSpec(), (config).dtor_crypto());
    _18_valueOrError4 = _out4;
    if ((_18_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_18_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _19_compressedRecipientPublicKey;
    _19_compressedRecipientPublicKey = (_18_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError5 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = RawECDHKeyring_Compile.__default.ValidatePublicKey((config).dtor_crypto(), (input).dtor_curveSpec(), _0_recipientPublicKey);
    _20_valueOrError5 = _out5;
    if ((_20_valueOrError5).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_20_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    boolean _21___v11;
    _21___v11 = (_20_valueOrError5).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((_2_senderPublicKey).is_Some()) {
      Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError6 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
      Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
      _out6 = RawECDHKeyring_Compile.__default.ValidatePublicKey((config).dtor_crypto(), (input).dtor_curveSpec(), (_2_senderPublicKey).dtor_value());
      _22_valueOrError6 = _out6;
      if ((_22_valueOrError6).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_22_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      boolean _23___v12;
      _23___v12 = (_22_valueOrError6).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _24_valueOrError7 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _24_valueOrError7 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), RawECDHKeyring_Compile.__default.ValidPublicKeyLength((_2_senderPublicKey).dtor_value()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid sender public key length")));
      if ((_24_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_24_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _25_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), RawECDHKeyring_Compile.__default.ValidPublicKeyLength(_0_recipientPublicKey), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid recipient public key length")));
    if ((_25_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_25_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    RawECDHKeyring_Compile.RawEcdhKeyring _26_keyring;
    RawECDHKeyring_Compile.RawEcdhKeyring _nw0 = new RawECDHKeyring_Compile.RawEcdhKeyring();
    _nw0.__ctor((input).dtor_KeyAgreementScheme(), (input).dtor_curveSpec(), _1_senderPrivateKey, _2_senderPublicKey, _0_recipientPublicKey, _3_compressedSenderPublicKey, _19_compressedRecipientPublicKey, (config).dtor_crypto());
    _26_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<RawECDHKeyring_Compile.RawEcdhKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<RawECDHKeyring_Compile.RawEcdhKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(RawECDHKeyring_Compile.RawEcdhKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _26_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsRsaKeyring(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_publicKey()).is_Some()) || (((input).dtor_kmsClient()).is_Some()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A publicKey or a kmsClient is required")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_encryptionAlgorithm()).is_RSAES__OAEP__SHA__1()) || (((input).dtor_encryptionAlgorithm()).is_RSAES__OAEP__SHA__256()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Unsupported EncryptionAlgorithmSpec")));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_1_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__KeyIdType((input).dtor_kmsKeyId())) && ((AwsArnParsing_Compile.__default.ParseAwsKmsArn((input).dtor_kmsKeyId())).is_Success()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Kms Key ID must be a KMS Key ARN")));
    if ((_2_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    if (((input).dtor_publicKey()).is_Some()) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _3_lengthOutputRes;
      _3_lengthOutputRes = ((config).dtor_crypto()).GetRSAKeyModulusLength(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthInput.create(((input).dtor_publicKey()).dtor_value()));
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _4_valueOrError3 = (_3_lengthOutputRes).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _5_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_5_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_5_e);
      }));
      if ((_4_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_4_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
      software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput _6_lengthOutput;
      _6_lengthOutput = (_4_valueOrError3).Extract(software.amazon.cryptography.primitives.internaldafny.types.GetRSAKeyModulusLengthOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _7_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_6_lengthOutput).dtor_length()) >= (AwsKmsRsaKeyring_Compile.__default.MIN__KMS__RSA__KEY__LEN()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid public key length")));
      if ((_7_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_7_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
        return output;
      }
    }
    Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError5 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
    _8_valueOrError5 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((input).dtor_kmsKeyId());
    if ((_8_valueOrError5).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_8_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.Tuple0 _9___v13;
    _9___v13 = (_8_valueOrError5).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
    _10_valueOrError6 = AwsKmsUtils_Compile.__default.GetValidGrantTokens((input).dtor_grantTokens());
    if ((_10_valueOrError6).IsFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_10_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>PropagateFailure(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _11_grantTokens;
    _11_grantTokens = (_10_valueOrError6).Extract(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring _12_keyring;
    AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring _nw0 = new AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring();
    _nw0.__ctor((input).dtor_publicKey(), (input).dtor_kmsKeyId(), (input).dtor_encryptionAlgorithm(), (input).dtor_kmsClient(), (config).dtor_crypto(), _11_grantTokens);
    _12_keyring = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsRsaKeyring_Compile.AwsKmsRsaKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _12_keyring)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateDefaultCryptographicMaterialsManager(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    DefaultCMM_Compile.DefaultCMM _0_cmm;
    DefaultCMM_Compile.DefaultCMM _nw0 = new DefaultCMM_Compile.DefaultCMM();
    _nw0.OfKeyring((input).dtor_keyring(), (config).dtor_crypto());
    _0_cmm = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<DefaultCMM_Compile.DefaultCMM, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<DefaultCMM_Compile.DefaultCMM>)(java.lang.Object)dafny.TypeDescriptor.reference(DefaultCMM_Compile.DefaultCMM.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _0_cmm)));
    return output;
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Error CmpError(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(s);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRequiredEncryptionContextCMM(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((input).dtor_underlyingCMM()).is_Some()) && (((input).dtor_keyring()).is_None()), __default.CmpError(dafny.DafnySequence.asString("CreateRequiredEncryptionContextCMM currently only supports cmm.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)));
      return output;
    }
    dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>> _1_keySet;
    _1_keySet = ((java.util.function.Function<software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput, dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(_2_input) -> ((dafny.Function0<dafny.DafnySet<? extends dafny.DafnySequence<? extends java.lang.Byte>>>)(() -> {
      java.util.ArrayList<dafny.DafnySequence<? extends java.lang.Byte>> _coll0 = new java.util.ArrayList<>();
      for (dafny.DafnySequence<? extends java.lang.Byte> _compr_0_boxed0 : ((_2_input).dtor_requiredEncryptionContextKeys()).Elements()) {
        dafny.DafnySequence<? extends java.lang.Byte> _compr_0 = ((dafny.DafnySequence<? extends java.lang.Byte>)(java.lang.Object)(_compr_0_boxed0));
        dafny.DafnySequence<? extends java.lang.Byte> _3_k = (dafny.DafnySequence<? extends java.lang.Byte>)_compr_0;
        if (UTF8.ValidUTF8Bytes._Is(_3_k)) {
          if (((_2_input).dtor_requiredEncryptionContextKeys()).contains(_3_k)) {
            _coll0.add(_3_k);
          }
        }
      }
      return new dafny.DafnySet<dafny.DafnySequence<? extends java.lang.Byte>>(_coll0);
    })).apply()).apply(input);
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _4_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((long) (_1_keySet).cardinalityInt()) == 0 ? 0 : 1) == 1, __default.CmpError(dafny.DafnySequence.asString("RequiredEncryptionContextCMM needs at least one requiredEncryptionContextKey.")));
    if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_4_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager.class)));
      return output;
    }
    RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM _5_cmm;
    RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM _nw0 = new RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM();
    _nw0.__ctor(((input).dtor_underlyingCMM()).dtor_value(), _1_keySet);
    _5_cmm = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM>)(java.lang.Object)dafny.TypeDescriptor.reference(RequiredEncryptionContextCMM_Compile.RequiredEncryptionContextCMM.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _5_cmm)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateCryptographicMaterialsCache(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      software.amazon.cryptography.materialproviders.internaldafny.types.CacheType _source0 = (input).dtor_cache();
      if (_source0.is_Default()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache _0___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_Default)_source0)._Default;
        software.amazon.cryptography.materialproviders.internaldafny.types.DefaultCache _1_c = _0___mcc_h0;
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _2_cache;
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _3_dt__update__tmp_h0 = StormTracker_Compile.__default.DefaultStorm();
        int _4_dt__update_hentryCapacity_h0 = (_1_c).dtor_entryCapacity();
        _2_cache = software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create(_4_dt__update_hentryCapacity_h0, (_3_dt__update__tmp_h0).dtor_entryPruningTailSize(), (_3_dt__update__tmp_h0).dtor_gracePeriod(), (_3_dt__update__tmp_h0).dtor_graceInterval(), (_3_dt__update__tmp_h0).dtor_fanOut(), (_3_dt__update__tmp_h0).dtor_inFlightTTL(), (_3_dt__update__tmp_h0).dtor_sleepMilli(), (_3_dt__update__tmp_h0).dtor_timeUnits());
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _5_valueOrError0 = StormTracker_Compile.__default.CheckSettings(_2_cache);
        if ((_5_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_5_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)));
          return output;
        }
        StormTracker_Compile.StormTracker _6_cmc;
        StormTracker_Compile.StormTracker _nw0 = new StormTracker_Compile.StormTracker();
        _nw0.__ctor(_2_cache);
        _6_cmc = _nw0;
        software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC _7_synCmc;
        software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC _nw1 = new software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC(_6_cmc);
        _7_synCmc = _nw1;
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _7_synCmc)));
        return output;
      } else if (_source0.is_No()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.NoCache _8___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_No)_source0)._No;
        LocalCMC_Compile.LocalCMC _9_cmc;
        LocalCMC_Compile.LocalCMC _nw2 = new LocalCMC_Compile.LocalCMC();
        _nw2.__ctor((long) 0L, (long) 1L);
        _9_cmc = _nw2;
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<LocalCMC_Compile.LocalCMC, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<LocalCMC_Compile.LocalCMC>)(java.lang.Object)dafny.TypeDescriptor.reference(LocalCMC_Compile.LocalCMC.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _9_cmc)));
        return output;
      } else if (_source0.is_SingleThreaded()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache _10___mcc_h2 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_SingleThreaded)_source0)._SingleThreaded;
        software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache _11_c = _10___mcc_h2;
        LocalCMC_Compile.LocalCMC _12_cmc;
        LocalCMC_Compile.LocalCMC _nw3 = new LocalCMC_Compile.LocalCMC();
        _nw3.__ctor(((long) ((_11_c).dtor_entryCapacity())), ((long) ((__default.OptionalCountingNumber((_11_c).dtor_entryPruningTailSize())).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.CountingNumber._typeDescriptor(), 1))));
        _12_cmc = _nw3;
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<LocalCMC_Compile.LocalCMC, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<LocalCMC_Compile.LocalCMC>)(java.lang.Object)dafny.TypeDescriptor.reference(LocalCMC_Compile.LocalCMC.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _12_cmc)));
        return output;
      } else if (_source0.is_MultiThreaded()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache _13___mcc_h3 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_MultiThreaded)_source0)._MultiThreaded;
        software.amazon.cryptography.materialproviders.internaldafny.types.MultiThreadedCache _14_c = _13___mcc_h3;
        LocalCMC_Compile.LocalCMC _15_cmc;
        LocalCMC_Compile.LocalCMC _nw4 = new LocalCMC_Compile.LocalCMC();
        _nw4.__ctor(((long) ((_14_c).dtor_entryCapacity())), ((long) ((__default.OptionalCountingNumber((_14_c).dtor_entryPruningTailSize())).UnwrapOr(software.amazon.cryptography.materialproviders.internaldafny.types.CountingNumber._typeDescriptor(), 1))));
        _15_cmc = _nw4;
        software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC _16_synCmc;
        software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC _nw5 = new software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC(_15_cmc);
        _16_synCmc = _nw5;
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.internaldafny.SynchronizedLocalCMC.SynchronizedLocalCMC.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _16_synCmc)));
        return output;
      } else if (_source0.is_StormTracking()) {
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _17___mcc_h4 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_StormTracking)_source0)._StormTracking;
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _18_c = _17___mcc_h4;
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _19_cache;
        software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache _20_dt__update__tmp_h1 = _18_c;
        Wrappers_Compile.Option<java.lang.Integer> _21_dt__update_hentryPruningTailSize_h0 = __default.OptionalCountingNumber((_18_c).dtor_entryPruningTailSize());
        _19_cache = software.amazon.cryptography.materialproviders.internaldafny.types.StormTrackingCache.create((_20_dt__update__tmp_h1).dtor_entryCapacity(), _21_dt__update_hentryPruningTailSize_h0, (_20_dt__update__tmp_h1).dtor_gracePeriod(), (_20_dt__update__tmp_h1).dtor_graceInterval(), (_20_dt__update__tmp_h1).dtor_fanOut(), (_20_dt__update__tmp_h1).dtor_inFlightTTL(), (_20_dt__update__tmp_h1).dtor_sleepMilli(), (_20_dt__update__tmp_h1).dtor_timeUnits());
        Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _22_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _22_valueOrError1 = StormTracker_Compile.__default.CheckSettings(_19_cache);
        if ((_22_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_22_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)));
          return output;
        }
        StormTracker_Compile.StormTracker _23_cmc;
        StormTracker_Compile.StormTracker _nw6 = new StormTracker_Compile.StormTracker();
        _nw6.__ctor(_19_cache);
        _23_cmc = _nw6;
        software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC _24_synCmc;
        software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC _nw7 = new software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC(_23_cmc);
        _24_synCmc = _nw7;
        output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.internaldafny.StormTrackingCMC.StormTrackingCMC.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _24_synCmc)));
        return output;
      } else {
        software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _25___mcc_h5 = ((software.amazon.cryptography.materialproviders.internaldafny.types.CacheType_Shared)_source0)._Shared;
        software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache _26_c = _25___mcc_h5;
        software.amazon.cryptography.materialproviders.internaldafny.types.Error _27_exception;
        _27_exception = software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("CreateCryptographicMaterialsCache should never be called with Shared CacheType."));
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _27_exception);
        return output;
      }
    }
    return output;
  }
  public static Wrappers_Compile.Option<java.lang.Integer> OptionalCountingNumber(Wrappers_Compile.Option<java.lang.Integer> c) {
    if (((c).is_Some()) && (java.lang.Integer.signum(((c).dtor_value())) != 1)) {
      return Wrappers_Compile.Option.<java.lang.Integer>create_None(BoundedInts_Compile.int32._typeDescriptor());
    } else {
      return c;
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateDefaultClientSupplier(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    DefaultClientSupplier_Compile.DefaultClientSupplier _0_clientSupplier;
    DefaultClientSupplier_Compile.DefaultClientSupplier _nw0 = new DefaultClientSupplier_Compile.DefaultClientSupplier();
    _nw0.__ctor();
    _0_clientSupplier = _nw0;
    output = ((Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(Wrappers_Compile.Result.<DefaultClientSupplier_Compile.DefaultClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<DefaultClientSupplier_Compile.DefaultClientSupplier>)(java.lang.Object)dafny.TypeDescriptor.reference(DefaultClientSupplier_Compile.DefaultClientSupplier.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _0_clientSupplier)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> InitializeEncryptionMaterials(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput input)
  {
    return Materials_Compile.__default.InitializeEncryptionMaterials(input);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> InitializeDecryptionMaterials(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput input)
  {
    return Materials_Compile.__default.InitializeDecryptionMaterials(input);
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidEncryptionMaterialsTransition(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.ValidEncryptionMaterialsTransition((input).dtor_start(), (input).dtor_stop()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidEncryptionMaterialsTransition(dafny.DafnySequence.asString("Invalid Encryption Materials Transition")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidDecryptionMaterialsTransition(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsTransitionIsValid((input).dtor_start(), (input).dtor_stop()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidDecryptionMaterialsTransition(dafny.DafnySequence.asString("Invalid Decryption Materials Transition")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> EncryptionMaterialsHasPlaintextDataKey(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.EncryptionMaterialsHasPlaintextDataKey(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidDecryptionMaterials(dafny.DafnySequence.asString("Invalid Encryption Materials")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptionMaterialsWithPlaintextDataKey(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithPlaintextDataKey(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidDecryptionMaterials(dafny.DafnySequence.asString("Invalid Decryption Materials")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetAlgorithmSuiteInfo(Config config, dafny.DafnySequence<? extends java.lang.Byte> input)
  {
    return AlgorithmSuites_Compile.__default.GetAlgorithmSuiteInfo(input);
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidAlgorithmSuiteInfo(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AlgorithmSuites_Compile.__default.AlgorithmSuite_q(input), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_InvalidAlgorithmSuiteInfo(dafny.DafnySequence.asString("Invalid AlgorithmSuiteInfo")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnEncrypt(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Commitment_Compile.__default.ValidateCommitmentPolicyOnEncrypt((input).dtor_algorithm(), (input).dtor_commitmentPolicy());
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  public static Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnDecrypt(Config config, software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput input)
  {
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Commitment_Compile.__default.ValidateCommitmentPolicyOnDecrypt((input).dtor_algorithm(), (input).dtor_commitmentPolicy());
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<dafny.Tuple0>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0._typeDescriptor());
    } else {
      return Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.create());
    }
  }
  @Override
  public java.lang.String toString() {
    return "AwsCryptographyMaterialProvidersOperations._default";
  }
}
