// Class __default
// Dafny class __default compiled into Java
package MrkAwareDiscoveryMultiKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> MrkAwareDiscoveryMultiKeyring(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> regions, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter, software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens)
  {
    Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((long) (regions).cardinalityInt()) == 0 ? 0 : 1) == 1, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("No regions passed.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (Seq_Compile.__default.<dafny.DafnySequence<? extends Character>>IndexOfOption(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), regions, dafny.DafnySequence.asString(""))).is_None(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Empty string is not a valid region.")));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_1_valueOrError1).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    dafny.DafnySequence<? extends AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring> _2_children;
    _2_children = dafny.DafnySequence.<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring> empty(((dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring.class)));
    long _hi0 = (long) (regions).cardinalityInt();
    for (long _3_i = (long) 0L; java.lang.Long.compareUnsigned(_3_i, _hi0) < 0; _3_i++) {
      dafny.DafnySequence<? extends Character> _4_region;
      _4_region = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((regions).select(dafny.Helpers.unsignedToInt(_3_i))));
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create(_4_region));
      _5_valueOrError2 = _out0;
      if ((_5_valueOrError2).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_5_valueOrError2).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _6_client;
      _6_client = (_5_valueOrError2).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring _7_keyring;
      AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring _nw0 = new AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring();
      _nw0.__ctor(_6_client, _4_region, discoveryFilter, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
      _7_keyring = _nw0;
      _2_children = dafny.DafnySequence.<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring>concatenate(_2_children, dafny.DafnySequence.<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring> of(((dafny.TypeDescriptor<AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkDiscoveryKeyring_Compile.AwsKmsMrkDiscoveryKeyring.class)), _7_keyring));
    }
    MultiKeyring_Compile.MultiKeyring _8_keyring;
    MultiKeyring_Compile.MultiKeyring _nw1 = new MultiKeyring_Compile.MultiKeyring();
    _nw1.__ctor(Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>create_None(((dafny.TypeDescriptor<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.class))), _2_children);
    _8_keyring = _nw1;
    output = Wrappers_Compile.Result.<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_keyring);
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "MrkAwareDiscoveryMultiKeyring._default";
  }
}
