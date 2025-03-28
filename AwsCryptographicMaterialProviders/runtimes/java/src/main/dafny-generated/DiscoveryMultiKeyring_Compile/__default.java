// Class __default
// Dafny class __default compiled into Java
package DiscoveryMultiKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DiscoveryMultiKeyring(dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> regions, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter, software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier clientSupplier, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens)
  {
    Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<MultiKeyring_Compile.MultiKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((regions).length())).signum() == 1, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("No regions passed.")));
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
    dafny.DafnySequence<? extends AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring> _2_children;
    _2_children = dafny.DafnySequence.<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring> empty(((dafny.TypeDescriptor<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring.class)));
    java.math.BigInteger _hi0 = java.math.BigInteger.valueOf((regions).length());
    for (java.math.BigInteger _3_i = java.math.BigInteger.ZERO; _3_i.compareTo(_hi0) < 0; _3_i = _3_i.add(java.math.BigInteger.ONE)) {
      dafny.DafnySequence<? extends Character> _4_region;
      _4_region = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)((regions).select(dafny.Helpers.toInt((_3_i)))));
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
      AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring _7_keyring;
      AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring _nw0 = new AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring();
      _nw0.__ctor(_6_client, discoveryFilter, (grantTokens).UnwrapOr(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor())));
      _7_keyring = _nw0;
      _2_children = dafny.DafnySequence.<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring>concatenate(_2_children, dafny.DafnySequence.<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring> of(((dafny.TypeDescriptor<AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring>)(java.lang.Object)dafny.TypeDescriptor.reference(AwsKmsDiscoveryKeyring_Compile.AwsKmsDiscoveryKeyring.class)), _7_keyring));
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
    return "DiscoveryMultiKeyring._default";
  }
}
