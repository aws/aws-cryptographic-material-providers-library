// Class KmsWrapKeyMaterial
// Dafny class KmsWrapKeyMaterial compiled into Java
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
public class KmsWrapKeyMaterial implements MaterialWrapping_Compile.WrapMaterial<KmsWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.WrapInput, MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.WrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsWrapKeyMaterial() {
    this._client = null;
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> awsKmsKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._client = client;
    (this)._awsKmsKey = awsKmsKey;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.WrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>Default(KmsWrapInfo._typeDescriptor(), KmsWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    _1_valueOrError0 = AwsKmsUtils_Compile.__default.StringifyEncryptionContext((input).dtor_encryptionContext());
    if ((_1_valueOrError0).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_stringifiedEncCtx;
    _2_stringifiedEncCtx = (_1_valueOrError0).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PlaintextType((input).dtor_plaintextMaterial()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid Plaintext on KMS Encrypt")));
    if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError1).<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest _4_encryptRequest;
    _4_encryptRequest = software.amazon.cryptography.services.kms.internaldafny.types.EncryptRequest.create((this).awsKmsKey(), (input).dtor_plaintextMaterial(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _2_stringifiedEncCtx), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), (this).grantTokens()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _5_maybeEncryptResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = ((this).client()).Encrypt(_4_encryptRequest);
    _5_maybeEncryptResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse.Default());
    _6_valueOrError2 = (_5_maybeEncryptResponse).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_7_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _7_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_7_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_7_e);
    }));
    if ((_6_valueOrError2).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError2).<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse _8_encryptResponse;
    _8_encryptResponse = (_6_valueOrError2).Extract(software.amazon.cryptography.services.kms.internaldafny.types.EncryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_8_encryptResponse).dtor_KeyId()).is_Some()) && ((AwsArnParsing_Compile.__default.ParseAwsKmsIdentifier(((_8_encryptResponse).dtor_KeyId()).dtor_value())).is_Success()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from AWS KMS Encrypt:: Invalid Key Id")));
    if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError3).<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _10_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_8_encryptResponse).dtor_CiphertextBlob()).is_Some(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")));
    if ((_10_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError4).<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.WrapOutput<KmsWrapInfo> _11_output;
    _11_output = MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>create(KmsWrapInfo._typeDescriptor(), ((_8_encryptResponse).dtor_CiphertextBlob()).dtor_value(), AwsKmsKeyring_Compile.KmsWrapInfo.create(((_8_encryptResponse).dtor_KeyId()).dtor_value()));
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.WrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.WrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _11_output);
    return res;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public dafny.DafnySequence<? extends Character> _awsKmsKey;
  public dafny.DafnySequence<? extends Character> awsKmsKey()
  {
    return this._awsKmsKey;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  private static final dafny.TypeDescriptor<KmsWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsWrapKeyMaterial>referenceWithInitializer(KmsWrapKeyMaterial.class, () -> (KmsWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsKeyring.KmsWrapKeyMaterial";
  }
}
