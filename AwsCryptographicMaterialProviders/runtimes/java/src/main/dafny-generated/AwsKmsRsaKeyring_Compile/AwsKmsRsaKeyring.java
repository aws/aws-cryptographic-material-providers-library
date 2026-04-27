// Class AwsKmsRsaKeyring
// Dafny class AwsKmsRsaKeyring compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsRsaKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public AwsKmsRsaKeyring() {
    this._cryptoPrimitives = null;
    this._client = Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>Default(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class)));
    this._paddingScheme = software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default();
    this._awsKmsKey = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    this._publicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    this._awsKmsArn = (AwsArnParsing_Compile.AwsKmsIdentifier)null;
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out10;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out10;
    _out10 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out10;
  }
  public void __ctor(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, dafny.DafnySequence<? extends Character> awsKmsKey, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> client, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens)
  {
    Wrappers_Compile.Result<AwsArnParsing_Compile.AwsKmsIdentifier, dafny.DafnySequence<? extends Character>> _0_parsedAwsKmsId;
    _0_parsedAwsKmsId = AwsArnParsing_Compile.__default.ParseAwsKmsIdentifier(awsKmsKey);
    (this)._publicKey = publicKey;
    (this)._awsKmsKey = awsKmsKey;
    (this)._awsKmsArn = (_0_parsedAwsKmsId).dtor_value();
    (this)._paddingScheme = paddingScheme;
    (this)._client = client;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (((this).publicKey()).is_Some()) && ((((long) (((this).publicKey()).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()))).cardinalityInt()) == 0 ? 0 : 1) == 1), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((input).dtor_materials()).dtor_algorithmSuite()).dtor_signature()).is_None(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing."), dafny.DafnySequence.asString(" Please specify an algorithm suite without asymmetric signing."))));
    if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
      return res;
    }
    KmsRsaWrapKeyMaterial _2_wrap;
    KmsRsaWrapKeyMaterial _nw0 = new KmsRsaWrapKeyMaterial();
    _nw0.__ctor(((this).publicKey()).dtor_value(), (this).paddingScheme(), (this).cryptoPrimitives());
    _2_wrap = _nw0;
    KmsRsaGenerateAndWrapKeyMaterial _3_generateAndWrap;
    KmsRsaGenerateAndWrapKeyMaterial _nw1 = new KmsRsaGenerateAndWrapKeyMaterial();
    _nw1.__ctor(((this).publicKey()).dtor_value(), (this).paddingScheme(), (this).cryptoPrimitives());
    _3_generateAndWrap = _nw1;
    Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<KmsRsaWrapInfo>Default(KmsRsaWrapInfo._typeDescriptor(), KmsRsaWrapInfo.Default()));
    Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<KmsRsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = EdkWrapping_Compile.__default.<KmsRsaWrapInfo>WrapEdkMaterial(KmsRsaWrapInfo._typeDescriptor(), (input).dtor_materials(), _2_wrap, _3_generateAndWrap);
    _4_valueOrError2 = _out0;
    if ((_4_valueOrError2).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.WrapEdkMaterialOutput<KmsRsaWrapInfo> _5_wrapOutput;
    _5_wrapOutput = (_4_valueOrError2).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<KmsRsaWrapInfo>_typeDescriptor(KmsRsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _6_symmetricSigningKeyList;
    if (((_5_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
      _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_5_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
    } else {
      _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _7_edk;
    _7_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(Constants_Compile.__default.RSA__PROVIDER__ID(), (UTF8.__default.Encode((this).awsKmsKey())).dtor_value(), (_5_wrapOutput).dtor_wrappedMaterial());
    software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _8_returnMaterials = (software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials)null;
    if ((_5_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _9_valueOrError3 = Materials_Compile.__default.EncryptionMaterialAddDataKey((input).dtor_materials(), (_5_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
      if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_9_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      _8_returnMaterials = (_9_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    } else if ((_5_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError4 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
      _10_valueOrError4 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys((input).dtor_materials(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
      if ((_10_valueOrError4).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_10_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      _8_returnMaterials = (_10_valueOrError4).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_8_returnMaterials));
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).client()).is_Some(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _1_materials;
    _1_materials = (input).dtor_materials();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_1_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError2 = AwsKmsUtils_Compile.__default.OkForDecrypt((this).awsKmsArn(), (this).awsKmsKey());
    if ((_3_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _4_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((((input).dtor_materials()).dtor_algorithmSuite()).dtor_signature()).is_None(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.<Character>concatenate(dafny.DafnySequence.asString("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing."), dafny.DafnySequence.asString(" Please specify an algorithm suite without asymmetric signing."))));
    if ((_4_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    AwsKmsUtils_Compile.OnDecryptMrkAwareEncryptedDataKeyFilter _5_filter;
    AwsKmsUtils_Compile.OnDecryptMrkAwareEncryptedDataKeyFilter _nw0 = new AwsKmsUtils_Compile.OnDecryptMrkAwareEncryptedDataKeyFilter();
    _nw0.__ctor((this).awsKmsArn(), Constants_Compile.__default.RSA__PROVIDER__ID());
    _5_filter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _5_filter, (input).dtor_encryptedDataKeys());
    _6_valueOrError4 = _out0;
    if ((_6_valueOrError4).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _7_edksToAttempt;
    _7_edksToAttempt = (_6_valueOrError4).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((((long) (_7_edksToAttempt).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _8_valueOrError5 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_8_valueOrError5).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _9_errorMessage;
      _9_errorMessage = (_8_valueOrError5).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_9_errorMessage));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = __default.EncryptionContextDigest((this).cryptoPrimitives(), (_1_materials).dtor_encryptionContext());
    _10_valueOrError6 = _out1;
    if ((_10_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _11_encryptionContextDigest;
    _11_encryptionContextDigest = (_10_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_decryptClosure;
    DecryptSingleAWSRSAEncryptedDataKey _nw1 = new DecryptSingleAWSRSAEncryptedDataKey();
    _nw1.__ctor(_1_materials, ((this).client()).dtor_value(), (this).awsKmsKey(), (this).paddingScheme(), _11_encryptionContextDigest, (this).grantTokens());
    _12_decryptClosure = _nw1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _13_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out2;
    _out2 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _12_decryptClosure, _7_edksToAttempt);
    _13_outcome = _out2;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _14_valueOrError7 = (_13_outcome).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_15_errors_boxed0) -> {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_errors = ((dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_15_errors_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_15_errors, dafny.DafnySequence.asString("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."));
    }));
    if ((_14_valueOrError7).IsFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_14_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _16_SealedDecryptionMaterials;
    _16_SealedDecryptionMaterials = (_14_valueOrError7).Extract(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_16_SealedDecryptionMaterials));
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> _client;
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> client()
  {
    return this._client;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _paddingScheme;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec paddingScheme()
  {
    return this._paddingScheme;
  }
  public dafny.DafnySequence<? extends Character> _awsKmsKey;
  public dafny.DafnySequence<? extends Character> awsKmsKey()
  {
    return this._awsKmsKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _publicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey()
  {
    return this._publicKey;
  }
  public AwsArnParsing_Compile.AwsKmsIdentifier _awsKmsArn;
  public AwsArnParsing_Compile.AwsKmsIdentifier awsKmsArn()
  {
    return this._awsKmsArn;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  private static final dafny.TypeDescriptor<AwsKmsRsaKeyring> _TYPE = dafny.TypeDescriptor.<AwsKmsRsaKeyring>referenceWithInitializer(AwsKmsRsaKeyring.class, () -> (AwsKmsRsaKeyring) null);
  public static dafny.TypeDescriptor<AwsKmsRsaKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsRsaKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsRsaKeyring.AwsKmsRsaKeyring";
  }
}
