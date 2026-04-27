// Class AwsKmsEcdhKeyring
// Dafny class AwsKmsEcdhKeyring compiled into Java
package AwsKmsEcdhKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AwsKmsEcdhKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public AwsKmsEcdhKeyring() {
    this._client = null;
    this._cryptoPrimitives = null;
    this._keyAgreementScheme = software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.Default();
    this._curveSpec = software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default();
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
    this._recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._senderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(software.amazon.cryptography.services.kms.internaldafny.types.PublicKeyType._typeDescriptor());
    this._compressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    this._compressedRecipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._senderKmsKeyId = Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(AwsArnParsing_Compile.AwsKmsIdentifierString._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out6;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out6;
    _out6 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out6;
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> senderKmsKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> compressedSenderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyAgreementScheme = KeyAgreementScheme;
    (this)._curveSpec = curveSpec;
    (this)._client = client;
    (this)._grantTokens = grantTokens;
    (this)._recipientPublicKey = recipientPublicKey;
    (this)._senderPublicKey = senderPublicKey;
    (this)._compressedSenderPublicKey = compressedSenderPublicKey;
    (this)._compressedRecipientPublicKey = compressedRecipientPublicKey;
    (this)._senderKmsKeyId = senderKmsKeyId;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), !(((this).keyAgreementScheme()).is_KmsPublicKeyDiscovery()), __default.E(dafny.DafnySequence.asString("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _1_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).senderKmsKeyId()).is_Some(), __default.E(dafny.DafnySequence.asString("Keyring MUST be configured with a sender KMS Key ID")));
      if ((_1_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_1_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _2_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).senderPublicKey()).is_Some(), __default.E(dafny.DafnySequence.asString("Keyring MUST be configured with a senderPublicKey")));
      if ((_2_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_2_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _3_senderKmsKeyId;
      _3_senderKmsKeyId = ((this).senderKmsKeyId()).dtor_value();
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _4_materials;
      _4_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _5_suite;
      _5_suite = ((input).dtor_materials()).dtor_algorithmSuite();
      Wrappers_Compile.Result<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnyMap.<dafny.DafnySequence<? extends Character>,dafny.DafnySequence<? extends Character>> empty());
      _6_valueOrError3 = AwsKmsUtils_Compile.__default.StringifyEncryptionContext(((input).dtor_materials()).dtor_encryptionContext());
      if ((_6_valueOrError3).IsFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_6_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends dafny.DafnySequence<? extends Character>> _7_stringifiedEncCtx;
      _7_stringifiedEncCtx = (_6_valueOrError3).Extract(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = __default.DeriveSharedSecret((this).client(), _3_senderKmsKeyId, (this).recipientPublicKey(), (this).grantTokens());
      _8_valueOrError4 = _out0;
      if ((_8_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_8_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _9_sharedSecret;
      _9_sharedSecret = (_8_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Byte> _10_operationCompressedSenderPublicKey;
      if (((this).compressedSenderPublicKey()).is_None()) {
        _10_operationCompressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
      } else {
        _10_operationCompressedSenderPublicKey = ((this).compressedSenderPublicKey()).dtor_value();
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
      _11_valueOrError5 = (UTF8.__default.Encode(RawECDHKeyring_Compile.__default.CurveSpecTypeToString((this).curveSpec()))).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), AwsKmsUtils_Compile.__default::WrapStringToError);
      if ((_11_valueOrError5).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_11_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _12_curveSpecUtf8;
      _12_curveSpecUtf8 = (_11_valueOrError5).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError6 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _13_valueOrError6 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(((input).dtor_materials()).dtor_encryptionContext());
      if ((_13_valueOrError6).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_13_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _14_canonicalizedEC;
      _14_canonicalizedEC = (_13_valueOrError6).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Byte> _15_fixedInfo;
      _15_fixedInfo = EcdhEdkWrapping_Compile.__default.SerializeFixedInfo(Constants_Compile.__default.ECDH__KDF__UTF8(), _12_curveSpecUtf8, _10_operationCompressedSenderPublicKey, (this).compressedRecipientPublicKey(), _14_canonicalizedEC, __default.AWS__KMS__ECDH__KEYRING__VERSION());
      EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial _16_ecdhGenerateAndWrap;
      EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial _nw0 = new EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial();
      _nw0.__ctor(_9_sharedSecret, _15_fixedInfo, (this).cryptoPrimitives());
      _16_ecdhGenerateAndWrap = _nw0;
      EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial _17_ecdhWrap;
      EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial _nw1 = new EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial();
      _nw1.__ctor(_9_sharedSecret, _15_fixedInfo, (this).cryptoPrimitives());
      _17_ecdhWrap = _nw1;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError7 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>Default(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor(), EcdhEdkWrapping_Compile.EcdhWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
      _out1 = EdkWrapping_Compile.__default.<EcdhEdkWrapping_Compile.EcdhWrapInfo>WrapEdkMaterial(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor(), _4_materials, _17_ecdhWrap, _16_ecdhGenerateAndWrap);
      _18_valueOrError7 = _out1;
      if ((_18_valueOrError7).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_18_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo> _19_wrapOutput;
      _19_wrapOutput = (_18_valueOrError7).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _20_symmetricSigningKeyList;
      if (((_19_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_19_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _21_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (RawECDHKeyring_Compile.__default.ValidCompressedPublicKeyLength(_10_operationCompressedSenderPublicKey)) && (RawECDHKeyring_Compile.__default.ValidCompressedPublicKeyLength((this).compressedRecipientPublicKey())), __default.E(dafny.DafnySequence.asString("Invalid compressed public key length.")));
      if ((_21_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_21_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _22_edk;
      _22_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(Constants_Compile.__default.KMS__ECDH__PROVIDER__ID(), RawECDHKeyring_Compile.__default.SerializeProviderInfo(_10_operationCompressedSenderPublicKey, (this).compressedRecipientPublicKey()), (_19_wrapOutput).dtor_wrappedMaterial());
      if ((_19_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError9 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _23_valueOrError9 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_4_materials, (_19_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _22_edk), _20_symmetricSigningKeyList);
        if ((_23_valueOrError9).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_23_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _24_result;
        _24_result = (_23_valueOrError9).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_24_result));
        return res;
      } else if ((_19_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError10 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _25_valueOrError10 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_4_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _22_edk), _20_symmetricSigningKeyList);
        if ((_25_valueOrError10).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_25_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _26_result;
        _26_result = (_25_valueOrError10).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_26_result));
        return res;
      }
    }
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_materials;
    _0_materials = (input).dtor_materials();
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
    _1_suite = ((input).dtor_materials()).dtor_algorithmSuite();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_0_materials), __default.E(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_2_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    OnDecryptEcdhDataKeyFilter _3_filter;
    OnDecryptEcdhDataKeyFilter _nw0 = new OnDecryptEcdhDataKeyFilter();
    _nw0.__ctor((this).keyAgreementScheme(), (this).compressedRecipientPublicKey(), (this).compressedSenderPublicKey());
    _3_filter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _3_filter, (input).dtor_encryptedDataKeys());
    _4_valueOrError1 = _out0;
    if ((_4_valueOrError1).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _5_edksToAttempt;
    _5_edksToAttempt = (_4_valueOrError1).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((((long) (_5_edksToAttempt).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _6_valueOrError2 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_6_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_6_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _7_errorMessage;
      _7_errorMessage = (_6_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default.E(_7_errorMessage));
      return res;
    }
    Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_decryptClosure;
    DecryptSingleEncryptedDataKey _nw1 = new DecryptSingleEncryptedDataKey();
    _nw1.__ctor(_0_materials, (this).cryptoPrimitives(), (this).compressedRecipientPublicKey(), (this).client(), (this).grantTokens(), (this).keyAgreementScheme(), (this).curveSpec());
    _8_decryptClosure = _nw1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _9_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out1;
    _out1 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _8_decryptClosure, _5_edksToAttempt);
    _9_outcome = _out1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _10_valueOrError3 = (_9_outcome).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_11_errors_boxed0) -> {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_errors = ((dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_11_errors_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_11_errors, dafny.DafnySequence.asString("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."));
    }));
    if ((_10_valueOrError3).IsFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _12_SealedDecryptionMaterials;
    _12_SealedDecryptionMaterials = (_10_valueOrError3).Extract(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_12_SealedDecryptionMaterials));
    return res;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _keyAgreementScheme;
  public software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations keyAgreementScheme()
  {
    return this._keyAgreementScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec()
  {
    return this._curveSpec;
  }
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> _grantTokens;
  public dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens()
  {
    return this._grantTokens;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey()
  {
    return this._recipientPublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _senderPublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey()
  {
    return this._senderPublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _compressedSenderPublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> compressedSenderPublicKey()
  {
    return this._compressedSenderPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedRecipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey()
  {
    return this._compressedRecipientPublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _senderKmsKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> senderKmsKeyId()
  {
    return this._senderKmsKeyId;
  }
  private static final dafny.TypeDescriptor<AwsKmsEcdhKeyring> _TYPE = dafny.TypeDescriptor.<AwsKmsEcdhKeyring>referenceWithInitializer(AwsKmsEcdhKeyring.class, () -> (AwsKmsEcdhKeyring) null);
  public static dafny.TypeDescriptor<AwsKmsEcdhKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<AwsKmsEcdhKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsEcdhKeyring.AwsKmsEcdhKeyring";
  }
}
