// Class OnDecryptEncryptedDataKeyFilter
// Dafny class OnDecryptEncryptedDataKeyFilter compiled into Java
package AwsKmsKeyring_Compile;

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

@SuppressWarnings({"unchecked", "deprecation"})
public class OnDecryptEncryptedDataKeyFilter implements Actions_Compile.DeterministicActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.DeterministicAction<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public OnDecryptEncryptedDataKeyFilter() {
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
  }
  public void __ctor(dafny.DafnySequence<? extends Character> awsKmsKey)
  {
    (this)._awsKmsKey = awsKmsKey;
  }
  public Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    if (!((edk).dtor_keyProviderId()).equals(Constants_Compile.__default.PROVIDER__ID())) {
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
      return res;
    }
    if (!(UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo()))) {
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid AWS KMS encoding, provider info is not UTF8.")));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
    _0_valueOrError0 = (UTF8.__default.Decode((edk).dtor_keyProviderInfo())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<Boolean>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
      return res;
    }
    dafny.DafnySequence<? extends Character> _1_keyId;
    _1_keyId = (_0_valueOrError0).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = (Wrappers_Compile.Result<AwsArnParsing_Compile.AwsArn, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _2_valueOrError1 = (AwsArnParsing_Compile.__default.ParseAwsKmsArn(_1_keyId)).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
    if ((_2_valueOrError1).IsFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError1).<Boolean>PropagateFailure(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
      return res;
    }
    AwsArnParsing_Compile.AwsArn _3___v0;
    _3___v0 = (_2_valueOrError1).Extract(AwsArnParsing_Compile.AwsKmsArn._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).awsKmsKey()).equals(_1_keyId));
    return res;
  }
  public dafny.DafnySequence<? extends Character> _awsKmsKey;
  public dafny.DafnySequence<? extends Character> awsKmsKey()
  {
    return this._awsKmsKey;
  }
  private static final dafny.TypeDescriptor<OnDecryptEncryptedDataKeyFilter> _TYPE = dafny.TypeDescriptor.<OnDecryptEncryptedDataKeyFilter>referenceWithInitializer(OnDecryptEncryptedDataKeyFilter.class, () -> (OnDecryptEncryptedDataKeyFilter) null);
  public static dafny.TypeDescriptor<OnDecryptEncryptedDataKeyFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<OnDecryptEncryptedDataKeyFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsKeyring.OnDecryptEncryptedDataKeyFilter";
  }
}
