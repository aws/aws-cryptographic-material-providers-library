// Class AwsKmsEncryptedDataKeyFilterTransform
// Dafny class AwsKmsEncryptedDataKeyFilterTransform compiled into Java
package AwsKmsMrkDiscoveryKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEncryptedDataKeyFilterTransform implements Actions_Compile.DeterministicActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.DeterministicAction<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public AwsKmsEncryptedDataKeyFilterTransform() {
    this._region = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._discoveryFilter = Wrappers_Compile.Option.<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter>Default(software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter._typeDescriptor());
  }
  public void __ctor(dafny.DafnySequence<? extends Character> region, Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter)
  {
    (this)._region = region;
    (this)._discoveryFilter = discoveryFilter;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> empty(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
    if (!((edk).dtor_keyProviderId()).equals(Constants_Compile.__default.PROVIDER__ID())) {
      res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> empty(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid AWS KMS encoding, provider info is not UTF8.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _1_valueOrError1 = (UTF8.__default.Decode((edk).dtor_keyProviderInfo())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _2_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_2_e);
    }));
    if ((_1_valueOrError1).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError1).<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends Character> _3_keyId;
    _3_keyId = (_1_valueOrError1).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _4_valueOrError2 = (AwsArnParsing_Compile.__default.ParseAwsKmsArn(_3_keyId)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_5_e_boxed0) -> {
      dafny.DafnySequence<? extends Character> _5_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_5_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_5_e);
    }));
    if ((_4_valueOrError2).IsFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError2).<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>>PropagateFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    AwsArnParsing_Compile.AwsArn _6_arn;
    _6_arn = (_4_valueOrError2).Extract(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_6_arn).dtor_resource()).dtor_resourceType()).equals(dafny.DafnySequence.asString("key")), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Only AWS KMS Keys supported")));
    if ((_7_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError3).<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    if (!(__default.DiscoveryMatch(_6_arn, (this).discoveryFilter(), (this).region()))) {
      res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> empty(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Constants_Compile.AwsKmsEdkHelper>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper>_typeDescriptor(Constants_Compile.AwsKmsEdkHelper._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Constants_Compile.AwsKmsEdkHelper> of(Constants_Compile.AwsKmsEdkHelper._typeDescriptor(), Constants_Compile.AwsKmsEdkHelper.create(edk, _6_arn)));
    return res;
  }
  public dafny.DafnySequence<? extends Character> _region;
  public dafny.DafnySequence<? extends Character> region()
  {
    return this._region;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> _discoveryFilter;
  public Wrappers_Compile.Option<software.amazon.cryptography.materialproviders.internaldafny.types.DiscoveryFilter> discoveryFilter()
  {
    return this._discoveryFilter;
  }
  private static final dafny.TypeDescriptor<AwsKmsEncryptedDataKeyFilterTransform> _TYPE = dafny.TypeDescriptor.<AwsKmsEncryptedDataKeyFilterTransform>referenceWithInitializer(AwsKmsEncryptedDataKeyFilterTransform.class, () -> (AwsKmsEncryptedDataKeyFilterTransform) null);
  public static dafny.TypeDescriptor<AwsKmsEncryptedDataKeyFilterTransform> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsEncryptedDataKeyFilterTransform>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform";
  }
}
