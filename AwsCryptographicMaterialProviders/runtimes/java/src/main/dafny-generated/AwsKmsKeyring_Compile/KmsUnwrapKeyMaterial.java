// Class KmsUnwrapKeyMaterial
// Dafny class KmsUnwrapKeyMaterial compiled into Java
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
public class KmsUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<KmsUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsUnwrapKeyMaterial() {
    this._client = null;
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
  }
  public void __ctor(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> awsKmsKey, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._client = client;
    (this)._awsKmsKey = awsKmsKey;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>Default(KmsUnwrapInfo._typeDescriptor(), KmsUnwrapInfo.Default()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType((input).dtor_wrappedMaterial()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Ciphertext length invalid")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    _1_valueOrError1 = AwsKmsUtils_Compile.__default.StringifyEncryptionContext((input).dtor_encryptionContext());
    if ((_1_valueOrError1).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_stringifiedEncCtx;
    _2_stringifiedEncCtx = (_1_valueOrError1).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest _3_decryptRequest;
    _3_decryptRequest = software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest.create((input).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _2_stringifiedEncCtx), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), (this).grantTokens()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(AwsArnParsing_Compile.AwsKmsIdentifierString._typeDescriptor(), (this).awsKmsKey()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_maybeDecryptResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = ((this).client()).Decrypt(_3_decryptRequest);
    _4_maybeDecryptResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError2 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.Default());
    _5_valueOrError2 = (_4_maybeDecryptResponse).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_6_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _6_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_6_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_6_e);
    }));
    if ((_5_valueOrError2).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError2).<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse _7_decryptResponse;
    _7_decryptResponse = (_5_valueOrError2).Extract(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((((_7_decryptResponse).dtor_KeyId()).is_Some()) && ((((_7_decryptResponse).dtor_KeyId()).dtor_value()).equals((this).awsKmsKey()))) && (((_7_decryptResponse).dtor_Plaintext()).is_Some())) && (java.util.Objects.equals(java.math.BigInteger.valueOf(AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())), java.math.BigInteger.valueOf((((_7_decryptResponse).dtor_Plaintext()).dtor_value()).length()))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from KMS Decrypt")));
    if ((_8_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError3).<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo> _9_output;
    _9_output = MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>create(KmsUnwrapInfo._typeDescriptor(), ((_7_decryptResponse).dtor_Plaintext()).dtor_value(), AwsKmsKeyring_Compile.KmsUnwrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<KmsUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<KmsUnwrapInfo>_typeDescriptor(KmsUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _9_output);
    return res;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  public dafny.DafnySequence<? extends Character> _awsKmsKey;
  public dafny.DafnySequence<? extends Character> awsKmsKey()
  {
    return this._awsKmsKey;
  }
  private static final dafny.TypeDescriptor<KmsUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsUnwrapKeyMaterial>referenceWithInitializer(KmsUnwrapKeyMaterial.class, () -> (KmsUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsKeyring.KmsUnwrapKeyMaterial";
  }
}
