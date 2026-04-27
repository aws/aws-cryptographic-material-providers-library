// Class KmsGenerateAndWrapKeyMaterial
// Dafny class KmsGenerateAndWrapKeyMaterial compiled into Java
package AwsKmsKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsGenerateAndWrapKeyMaterial implements MaterialWrapping_Compile.GenerateAndWrapMaterial<KmsWrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.GenerateAndWrapInput, MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.GenerateAndWrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public KmsGenerateAndWrapKeyMaterial() {
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
  public Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.GenerateAndWrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>Default(KmsWrapInfo._typeDescriptor(), KmsWrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
    _1_valueOrError0 = AwsKmsUtils_Compile.__default.StringifyEncryptionContext((input).dtor_encryptionContext());
    if ((_1_valueOrError0).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _2_stringifiedEncCtx;
    _2_stringifiedEncCtx = (_1_valueOrError0).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyRequest _3_generatorRequest;
    _3_generatorRequest = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyRequest.create((this).awsKmsKey(), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>>create_Some(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), _2_stringifiedEncCtx), Wrappers_Compile.Option.<java.lang.Integer>create_Some(BoundedInts_Compile.int32._typeDescriptor(), AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite)), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec>create_None(software.amazon.cryptography.services.kms.internaldafny.types.DataKeySpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>create_Some(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenList._typeDescriptor(), (this).grantTokens()), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo>create_None(software.amazon.cryptography.services.kms.internaldafny.types.RecipientInfo._typeDescriptor()), Wrappers_Compile.Option.<Boolean>create_None(dafny.TypeDescriptor.BOOLEAN));
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _4_maybeGenerateResponse;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse, software.amazon.cryptography.services.kms.internaldafny.types.Error> _out0;
    _out0 = ((this).client()).GenerateDataKey(_3_generatorRequest);
    _4_maybeGenerateResponse = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse.Default());
    _5_valueOrError1 = (_4_maybeGenerateResponse).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.services.kms.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_6_e_boxed0) -> {
      software.amazon.cryptography.services.kms.internaldafny.types.Error _6_e = ((software.amazon.cryptography.services.kms.internaldafny.types.Error)(java.lang.Object)(_6_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_ComAmazonawsKms(_6_e);
    }));
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse _7_generateResponse;
    _7_generateResponse = (_5_valueOrError1).Extract(software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyResponse._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_7_generateResponse).dtor_KeyId()).is_Some()) && ((AwsArnParsing_Compile.__default.ParseAwsKmsIdentifier(((_7_generateResponse).dtor_KeyId()).dtor_value())).is_Success()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from KMS GenerateDataKey:: Invalid Key Id")));
    if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_7_generateResponse).dtor_Plaintext()).is_Some()) && ((((long) (AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite)))) == ((long) (((_7_generateResponse).dtor_Plaintext()).dtor_value()).cardinalityInt())), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from AWS KMS GenerateDataKey: Invalid data key")));
    if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError3).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _10_valueOrError4 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((_7_generateResponse).dtor_CiphertextBlob()).is_Some()) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__CiphertextType(((_7_generateResponse).dtor_CiphertextBlob()).dtor_value())), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")));
    if ((_10_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError4).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _11_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (true) && (((_7_generateResponse).dtor_CiphertextForRecipient()).is_None()), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Invalid response from AWS KMS GeneratedDataKey: Invalid CiphertextForRecipient")));
    if ((_11_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_11_valueOrError5).<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo> _12_output;
    _12_output = MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>create(KmsWrapInfo._typeDescriptor(), ((_7_generateResponse).dtor_Plaintext()).dtor_value(), ((_7_generateResponse).dtor_CiphertextBlob()).dtor_value(), KmsWrapInfo.create(((_7_generateResponse).dtor_KeyId()).dtor_value()));
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.GenerateAndWrapOutput<KmsWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.GenerateAndWrapOutput.<KmsWrapInfo>_typeDescriptor(KmsWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _12_output);
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
  private static final dafny.TypeDescriptor<KmsGenerateAndWrapKeyMaterial> _TYPE = dafny.TypeDescriptor.<KmsGenerateAndWrapKeyMaterial>referenceWithInitializer(KmsGenerateAndWrapKeyMaterial.class, () -> (KmsGenerateAndWrapKeyMaterial) null);
  public static dafny.TypeDescriptor<KmsGenerateAndWrapKeyMaterial> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsGenerateAndWrapKeyMaterial>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial";
  }
}
