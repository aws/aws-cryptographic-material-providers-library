// Class __default
// Dafny class __default compiled into Java
package MrkAwareStrictMultiKeyring_Compile;

import software.amazon.cryptography.keystore.internaldafny.types.*;
import software.amazon.cryptography.materialproviders.internaldafny.types.*;
import AwsArnParsing_Compile.*;
import AwsKmsMrkMatchForDecrypt_Compile.*;
import AwsKmsUtils_Compile.*;
import KeyStoreErrorMessages_Compile.*;
import KmsArn_Compile.*;
import Structure_Compile.*;
import KMSKeystoreOperations_Compile.*;
import DDBKeystoreOperations_Compile.*;
import CreateKeys_Compile.*;
import CreateKeyStoreTable_Compile.*;
import GetKeys_Compile.*;
import AwsCryptographyKeyStoreOperations_Compile.*;
import software.amazon.cryptography.keystore.internaldafny.*;
import AlgorithmSuites_Compile.*;
import Materials_Compile.*;
import Keyring_Compile.*;
import MultiKeyring_Compile.*;
import AwsKmsMrkAreUnique_Compile.*;
import Constants_Compile.*;
import MaterialWrapping_Compile.*;
import CanonicalEncryptionContext_Compile.*;
import IntermediateKeyWrapping_Compile.*;
import EdkWrapping_Compile.*;
import ErrorMessages_Compile.*;
import AwsKmsKeyring_Compile.*;
import StrictMultiKeyring_Compile.*;
import AwsKmsDiscoveryKeyring_Compile.*;
import DiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkDiscoveryKeyring_Compile.*;
import MrkAwareDiscoveryMultiKeyring_Compile.*;
import AwsKmsMrkKeyring_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> MrkAwareStrictMultiKeyring(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> generator, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> awsKmsKeys, software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens)
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
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _5_valueOrError1 = AwsKmsMrkAreUnique_Compile.__default.AwsKmsMrkAreUnique(_4_allIdentifiers);
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_5_valueOrError1).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    Wrappers_Compile.Option<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring> _6_generatorKeyring = Wrappers_Compile.Option.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>Default(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _source1 = generator;
    if (_source1.is_None()) {
      _6_generatorKeyring = Wrappers_Compile.Option.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>create_None(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)));
    } else {
      dafny.DafnySequence<? extends Character> _7___mcc_h1 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends Character>>)_source1)._value;
      dafny.DafnySequence<? extends Character> _8_generatorIdentifier = _7___mcc_h1;
      Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _9_valueOrError2 = (AwsArnParsing_Compile.__default.IsAwsKmsIdentifierString(_8_generatorIdentifier)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_9_valueOrError2).IsFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_9_valueOrError2).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
        return output;
      }
      AwsArnParsing_Compile.AwsKmsIdentifier _10_arn;
      _10_arn = (_9_valueOrError2).Extract(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _11_region;
      _11_region = AwsArnParsing_Compile.__default.GetRegion(_10_arn);
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create((_11_region).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString(""))));
      _12_valueOrError3 = _out0;
      if ((_12_valueOrError3).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_12_valueOrError3).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
        return output;
      }
      software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _13_client;
      _13_client = (_12_valueOrError3).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _14_g;
      AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _nw0 = new AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring();
      _nw0.__ctor(_13_client, _8_generatorIdentifier, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
      _14_g = _nw0;
      _6_generatorKeyring = Wrappers_Compile.Option.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>create_Some(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)), _14_g);
    }
    dafny.DafnySequence<? extends AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring> _15_children;
    _15_children = dafny.DafnySequence.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring> empty(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)));
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _source2 = awsKmsKeys;
    if (_source2.is_None()) {
      _15_children = dafny.DafnySequence.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring> empty(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)));
    } else {
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _16___mcc_h2 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>)_source2)._value;
      dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _17_childIdentifiers = _16___mcc_h2;
      java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((_17_childIdentifiers).length());
      for (java.math.BigInteger _18_index = java.math.BigInteger.ZERO; _18_index.compareTo(_hi0) < 0; _18_index = _18_index.add(java.math.BigInteger.ONE)) {
        dafny.DafnySequence<? extends Character> _19_childIdentifier;
        _19_childIdentifier = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((_17_childIdentifiers).select(dafny.Helpers.toInt((_18_index)))));
        Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _20_valueOrError4 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _20_valueOrError4 = (AwsArnParsing_Compile.__default.IsAwsKmsIdentifierString(_19_childIdentifier)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
        if ((_20_valueOrError4).IsFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_20_valueOrError4).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
          return output;
        }
        AwsArnParsing_Compile.AwsKmsIdentifier _21_info;
        _21_info = (_20_valueOrError4).Extract(AwsArnParsing_Compile.AwsKmsIdentifier._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _22_region;
        _22_region = AwsArnParsing_Compile.__default.GetRegion(_21_info);
        Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError5 = (Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = (clientSupplier).GetClient(software.amazon.cryptography.materialproviders.internaldafny.types.GetClientInput.create((_22_region).UnwrapOr(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.asString(""))));
        _23_valueOrError5 = _out1;
        if ((_23_valueOrError5).IsFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_23_valueOrError5).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
          return output;
        }
        software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _24_client;
        _24_client = (_23_valueOrError5).Extract(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _25_keyring;
        AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring _nw1 = new AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring();
        _nw1.__ctor(_24_client, _19_childIdentifier, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
        _25_keyring = _nw1;
        _15_children = dafny.DafnySequence.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>concatenate(_15_children, dafny.DafnySequence.<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring> of(((dafny.TypeDescriptor<AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsMrkKeyring_Compile.AwsKmsMrkKeyring.class)), _25_keyring));
      }
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _26_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _26_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_6_generatorKeyring).is_Some()) || ((java.math.BigInteger.valueOf((_15_children).length())).signum() == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("generatorKeyring or child Keyrings needed to create a multi keyring")));
    if ((_26_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_26_valueOrError6).<MultiKeyring_Compile.MultiKeyring>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)));
      return output;
    }
    MultiKeyring_Compile.MultiKeyring _27_keyring;
    MultiKeyring_Compile.MultiKeyring _nw2 = new MultiKeyring_Compile.MultiKeyring();
    _nw2.__ctor(((Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring>)(java.lang.Object)(_6_generatorKeyring)), _15_children);
    _27_keyring = _nw2;
    output = Wrappers_Compile.Result.<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(((dafny.TypeDescriptor<MultiKeyring_Compile.MultiKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(MultiKeyring_Compile.MultiKeyring.class)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _27_keyring);
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "MrkAwareStrictMultiKeyring._default";
  }
}
