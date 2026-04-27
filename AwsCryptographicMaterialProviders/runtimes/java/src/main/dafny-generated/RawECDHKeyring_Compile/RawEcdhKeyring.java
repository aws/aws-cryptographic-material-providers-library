// Class RawEcdhKeyring
// Dafny class RawEcdhKeyring compiled into Java
package RawECDHKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawEcdhKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public RawEcdhKeyring() {
    this._cryptoPrimitives = null;
    this._keyAgreementScheme = software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations.Default();
    this._curveSpec = software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default();
    this._recipientPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.Default();
    this._compressedRecipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._senderPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.Default();
    this._senderPrivateKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.Default();
    this._compressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out2;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out2;
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPrivateKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> compressedSenderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyAgreementScheme = keyAgreementScheme;
    (this)._curveSpec = curveSpec;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._recipientPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(recipientPublicKey);
    (this)._compressedRecipientPublicKey = compressedRecipientPublicKey;
    if ((((senderPublicKey).is_Some()) && ((senderPrivateKey).is_Some())) && ((compressedSenderPublicKey).is_Some())) {
      (this)._senderPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((senderPublicKey).dtor_value());
      (this)._senderPrivateKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create((senderPrivateKey).dtor_value());
      (this)._compressedSenderPublicKey = (compressedSenderPublicKey).dtor_value();
    } else {
      (this)._senderPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      (this)._senderPrivateKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      (this)._compressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    }
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      if (((this).keyAgreementScheme()).is_PublicKeyDiscovery()) {
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")));
        return res;
      }
      software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey _0_operationSenderPrivateKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.Default();
      software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey _1_operationSenderPublicKey = software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.Default();
      dafny.DafnySequence<? extends java.lang.Byte> _2_operationCompressedSenderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
      if (((this).keyAgreementScheme()).is_EphemeralPrivateKeyToStaticPublicKey()) {
        Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
        Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = __default.GenerateEphemeralEccKeyPair((this).curveSpec(), (this).cryptoPrimitives());
        _3_valueOrError0 = _out0;
        if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_3_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput _4_ephemeralKeyPair;
        _4_ephemeralKeyPair = (_3_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _0_operationSenderPrivateKey = (_4_ephemeralKeyPair).dtor_privateKey();
        _1_operationSenderPublicKey = (_4_ephemeralKeyPair).dtor_publicKey();
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
        Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
        _out1 = __default.CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((_1_operationSenderPublicKey).dtor_der()), (this).curveSpec(), (this).cryptoPrimitives());
        _5_valueOrError1 = _out1;
        if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        dafny.DafnySequence<? extends java.lang.Byte> _6_operationCompressedSenderPublicKey_q;
        _6_operationCompressedSenderPublicKey_q = (_5_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _2_operationCompressedSenderPublicKey = _6_operationCompressedSenderPublicKey_q;
      } else {
        _0_operationSenderPrivateKey = (this).senderPrivateKey();
        _1_operationSenderPublicKey = (this).senderPublicKey();
        _2_operationCompressedSenderPublicKey = (this).compressedSenderPublicKey();
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _7_materials;
      _7_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _8_suite;
      _8_suite = ((input).dtor_materials()).dtor_algorithmSuite();
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
      _out2 = __default.LocalDeriveSharedSecret(_0_operationSenderPrivateKey, (this).recipientPublicKey(), (this).curveSpec(), (this).cryptoPrimitives());
      _9_valueOrError2 = _out2;
      if ((_9_valueOrError2).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_9_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _10_sharedSecret;
      _10_sharedSecret = (_9_valueOrError2).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
      _11_valueOrError3 = (UTF8.__default.Encode(__default.CurveSpecTypeToString((this).curveSpec()))).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default::E);
      if ((_11_valueOrError3).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_11_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _12_curveSpecUtf8;
      _12_curveSpecUtf8 = (_11_valueOrError3).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _13_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _13_valueOrError4 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(((input).dtor_materials()).dtor_encryptionContext());
      if ((_13_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_13_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _14_canonicalizedEC;
      _14_canonicalizedEC = (_13_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Byte> _15_fixedInfo;
      _15_fixedInfo = EcdhEdkWrapping_Compile.__default.SerializeFixedInfo(Constants_Compile.__default.ECDH__KDF__UTF8(), _12_curveSpecUtf8, _2_operationCompressedSenderPublicKey, (this).compressedRecipientPublicKey(), _14_canonicalizedEC, __default.RAW__ECDH__KEYRING__VERSION());
      EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial _16_ecdhGenerateAndWrap;
      EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial _nw0 = new EcdhEdkWrapping_Compile.EcdhGenerateAndWrapKeyMaterial();
      _nw0.__ctor(_10_sharedSecret, _15_fixedInfo, (this).cryptoPrimitives());
      _16_ecdhGenerateAndWrap = _nw0;
      EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial _17_ecdhWrap;
      EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial _nw1 = new EcdhEdkWrapping_Compile.EcdhWrapKeyMaterial();
      _nw1.__ctor(_10_sharedSecret, _15_fixedInfo, (this).cryptoPrimitives());
      _17_ecdhWrap = _nw1;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _18_valueOrError5 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>Default(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor(), EcdhEdkWrapping_Compile.EcdhWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
      _out3 = EdkWrapping_Compile.__default.<EcdhEdkWrapping_Compile.EcdhWrapInfo>WrapEdkMaterial(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor(), _7_materials, _17_ecdhWrap, _16_ecdhGenerateAndWrap);
      _18_valueOrError5 = _out3;
      if ((_18_valueOrError5).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_18_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhWrapInfo> _19_wrapOutput;
      _19_wrapOutput = (_18_valueOrError5).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhWrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _20_symmetricSigningKeyList;
      if (((_19_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_19_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _20_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _21_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (__default.ValidCompressedPublicKeyLength(_2_operationCompressedSenderPublicKey)) && (__default.ValidCompressedPublicKeyLength((this).compressedRecipientPublicKey())), __default.E(dafny.DafnySequence.asString("Invalid compressed public key length.")));
      if ((_21_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_21_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return res;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _22_edk;
      _22_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create(Constants_Compile.__default.RAW__ECDH__PROVIDER__ID(), __default.SerializeProviderInfo(_2_operationCompressedSenderPublicKey, (this).compressedRecipientPublicKey()), (_19_wrapOutput).dtor_wrappedMaterial());
      if ((_19_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError7 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _23_valueOrError7 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_7_materials, (_19_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _22_edk), _20_symmetricSigningKeyList);
        if ((_23_valueOrError7).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_23_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _24_result;
        _24_result = (_23_valueOrError7).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_24_result));
        return res;
      } else if ((_19_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError8 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _25_valueOrError8 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_7_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _22_edk), _20_symmetricSigningKeyList);
        if ((_25_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_25_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return res;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _26_result;
        _26_result = (_25_valueOrError8).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_26_result));
        return res;
      }
    }
    return res;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if (((this).keyAgreementScheme()).is_EphemeralPrivateKeyToStaticPublicKey()) {
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.")));
      return res;
    }
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
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _3_operationCompressedSenderPublicKey;
    if (((this).compressedSenderPublicKey()).equals(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()))) {
      _3_operationCompressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_None(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    } else {
      _3_operationCompressedSenderPublicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>create_Some(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), (this).compressedSenderPublicKey());
    }
    OnDecryptEcdhDataKeyFilter _4_filter;
    OnDecryptEcdhDataKeyFilter _nw0 = new OnDecryptEcdhDataKeyFilter();
    _nw0.__ctor((this).keyAgreementScheme(), (this).compressedRecipientPublicKey(), _3_operationCompressedSenderPublicKey);
    _4_filter = _nw0;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> empty(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.Error>FilterWithResult(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _4_filter, (input).dtor_encryptedDataKeys());
    _5_valueOrError1 = _out0;
    if ((_5_valueOrError1).IsFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> _6_edksToAttempt;
    _6_edksToAttempt = (_5_valueOrError1).Extract(dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    if ((((long) (_6_edksToAttempt).cardinalityInt()) == 0 ? 0 : 1) == 0) {
      Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
      _7_valueOrError2 = ErrorMessages_Compile.__default.IncorrectDataKeys((input).dtor_encryptedDataKeys(), ((input).dtor_materials()).dtor_algorithmSuite(), dafny.DafnySequence.asString(""));
      if ((_7_valueOrError2).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
        return res;
      }
      dafny.DafnySequence<? extends Character> _8_errorMessage;
      _8_errorMessage = (_7_valueOrError2).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default.E(_8_errorMessage));
      return res;
    }
    Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_decryptClosure;
    DecryptSingleEncryptedDataKey _nw1 = new DecryptSingleEncryptedDataKey();
    _nw1.__ctor(_0_materials, (this).cryptoPrimitives(), (this).compressedSenderPublicKey(), (this).compressedRecipientPublicKey(), (this).keyAgreementScheme(), (this).curveSpec());
    _9_decryptClosure = _nw1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _10_outcome;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>> _out1;
    _out1 = Actions_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>ReduceToSuccess(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _9_decryptClosure, _6_edksToAttempt);
    _10_outcome = _out1;
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _11_valueOrError3 = (_10_outcome).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>_typeDescriptor(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_12_errors_boxed0) -> {
      dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_errors = ((dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(java.lang.Object)(_12_errors_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_12_errors, dafny.DafnySequence.asString("No Configured Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."));
    }));
    if ((_11_valueOrError3).IsFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_11_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _13_SealedDecryptionMaterials;
    _13_SealedDecryptionMaterials = (_11_valueOrError3).Extract(Materials_Compile.SealedDecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_13_SealedDecryptionMaterials));
    return res;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations _keyAgreementScheme;
  public software.amazon.cryptography.materialproviders.internaldafny.types.RawEcdhStaticConfigurations keyAgreementScheme()
  {
    return this._keyAgreementScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec()
  {
    return this._curveSpec;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey _recipientPublicKey;
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey recipientPublicKey()
  {
    return this._recipientPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedRecipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> compressedRecipientPublicKey()
  {
    return this._compressedRecipientPublicKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey _senderPublicKey;
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey senderPublicKey()
  {
    return this._senderPublicKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey _senderPrivateKey;
  public software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey senderPrivateKey()
  {
    return this._senderPrivateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedSenderPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> compressedSenderPublicKey()
  {
    return this._compressedSenderPublicKey;
  }
  private static final dafny.TypeDescriptor<RawEcdhKeyring> _TYPE = dafny.TypeDescriptor.<RawEcdhKeyring>referenceWithInitializer(RawEcdhKeyring.class, () -> (RawEcdhKeyring) null);
  public static dafny.TypeDescriptor<RawEcdhKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawEcdhKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawECDHKeyring.RawEcdhKeyring";
  }
}
