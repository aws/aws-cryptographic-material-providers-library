// Class KmsRsaUnwrapKeyMaterial
// Dafny class KmsRsaUnwrapKeyMaterial compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaUnwrapKeyMaterial implements MaterialWrapping_Compile.UnwrapMaterial<KmsRsaUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsRsaUnwrapKeyMaterial() {
    this._client = null;
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._paddingScheme = software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default();
    this._encryptionContextDigest = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends Character> awsKmsKey, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme, dafny.DafnySequence<? extends java.lang.Byte> encryptionContextDigest, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    (this)._client = client;
    (this)._awsKmsKey = awsKmsKey;
    (this)._paddingScheme = paddingScheme;
    (this)._encryptionContextDigest = encryptionContextDigest;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>Default(KmsRsaUnwrapInfo._typeDescriptor(), KmsRsaUnwrapInfo.Default()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType((input).dtor_wrappedMaterial()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Ciphertext length invalid")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest _1_decryptRequest;
    _1_decryptRequest = software.amazon.cryptography.services.kms.internaldafny.types.DecryptRequest.create((input).dtor_wrappedMaterial(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_None(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), (this).grantTokens()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>create_Some(AwsArnParsing_Compile.AwsKmsIdentifierString._typeDescriptor(), (this).awsKmsKey()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec._typeDescriptor(), (this).paddingScheme()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _2_maybeDecryptResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = ((this).client()).Decrypt(_1_decryptRequest);
    _2_maybeDecryptResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError1 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.Default());
    _3_valueOrError1 = (_2_maybeDecryptResponse).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_4_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _4_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_4_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_4_e);
    }));
    if ((_3_valueOrError1).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse _5_decryptResponse;
    _5_decryptResponse = (_3_valueOrError1).Extract(software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((_5_decryptResponse).dtor_KeyId()).is_Some()) && ((((_5_decryptResponse).dtor_KeyId()).dtor_value()).equals((this).awsKmsKey()))) && (((_5_decryptResponse).dtor_Plaintext()).is_Some()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from KMS Decrypt")));
    if ((_6_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError2).<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _7_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((this).encryptionContextDigest()).isPrefixOf(((_5_decryptResponse).dtor_Plaintext()).dtor_value())) && (((long) (long) ((((long) (AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())))) + ((long) ((this).encryptionContextDigest()).cardinalityInt()))) == ((long) (((_5_decryptResponse).dtor_Plaintext()).dtor_value()).cardinalityInt())), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Encryption context digest does not match expected value.")));
    if ((_7_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_7_valueOrError3).<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo> _8_output;
    _8_output = MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>create(KmsRsaUnwrapInfo._typeDescriptor(), (((_5_decryptResponse).dtor_Plaintext()).dtor_value()).drop((long) ((this).encryptionContextDigest()).cardinalityInt()), KmsRsaUnwrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<KmsRsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<KmsRsaUnwrapInfo>_typeDescriptor(KmsRsaUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_output);
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
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _paddingScheme;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme()
  {
    return this._paddingScheme;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _encryptionContextDigest;
  public dafny.DafnySequence<? extends java.lang.Byte> encryptionContextDigest()
  {
    return this._encryptionContextDigest;
  }
  private static final dafny.TypeDescriptor<KmsRsaUnwrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsRsaUnwrapKeyMaterial>referenceWithInitializer(KmsRsaUnwrapKeyMaterial.class, () -> (KmsRsaUnwrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsRsaUnwrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaUnwrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial";
  }
}
