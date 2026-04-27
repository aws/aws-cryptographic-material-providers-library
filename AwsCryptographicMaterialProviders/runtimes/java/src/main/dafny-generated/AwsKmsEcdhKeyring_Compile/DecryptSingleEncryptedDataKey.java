// Class DecryptSingleEncryptedDataKey
// Dafny class DecryptSingleEncryptedDataKey compiled into Java
package AwsKmsEcdhKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptSingleEncryptedDataKey implements Actions_Compile.ActionWithResult<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey, Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public DecryptSingleEncryptedDataKey() {
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials)null;
    this._cryptoPrimitives = null;
    this._recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._keyAgreementScheme = software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations.Default();
    this._client = null;
    this._curveSpec = software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default();
    this._grantTokens = dafny.DafnySequence.<dafny.DafnySequence<? extends Character>> empty(software.amazon.cryptography.services.kms.internaldafny.types.GrantTokenType._typeDescriptor());
  }
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client, dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>> grantTokens, software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations keyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec)
  {
    (this)._materials = materials;
    (this)._cryptoPrimitives = cryptoPrimitives;
    (this)._recipientPublicKey = recipientPublicKey;
    (this)._keyAgreementScheme = keyAgreementScheme;
    (this)._client = client;
    (this)._curveSpec = curveSpec;
    (this)._grantTokens = grantTokens;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = ((this).materials()).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _1_keyProviderId;
    _1_keyProviderId = (edk).dtor_keyProviderId();
    dafny.DafnySequence<? extends java.lang.Byte> _2_providerInfo;
    _2_providerInfo = (edk).dtor_keyProviderInfo();
    dafny.DafnySequence<? extends java.lang.Byte> _3_ciphertext;
    _3_ciphertext = (edk).dtor_ciphertext();
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _4_valueOrError0 = EdkWrapping_Compile.__default.GetProviderWrappedMaterial(_3_ciphertext, _0_suite);
    if ((_4_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _5_providerWrappedMaterial;
    _5_providerWrappedMaterial = (_4_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.lang.Long.compareUnsigned((long) (_2_providerInfo).cardinalityInt(), (long) java.lang.Integer.toUnsignedLong(Constants_Compile.__default.ECDH__PROVIDER__INFO__521__LEN())) <= 0) && (RawECDHKeyring_Compile.__default.ValidProviderInfoLength(_2_providerInfo)), __default.E(dafny.DafnySequence.asString("EDK ProviderInfo longer than expected")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_6_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    byte _7_keyringVersion;
    _7_keyringVersion = ((byte)(java.lang.Object)((_2_providerInfo).select(0)));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (dafny.DafnySequence.<java.lang.Byte> of(_7_keyringVersion)).equals(__default.AWS__KMS__ECDH__KEYRING__VERSION()), __default.E(dafny.DafnySequence.asString("Incorrect Keyring version found in provider info.")));
    if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    int _9_recipientPublicKeyLength;
    _9_recipientPublicKeyLength = StandardLibrary_mUInt_Compile.__default.SeqToUInt32((_2_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPL__INDEX(), Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX()));
    long _10_recipientPublicKeyLengthIndex;
    _10_recipientPublicKeyLengthIndex = (long) (long) (((long) java.lang.Integer.toUnsignedLong(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX())) + ((long) java.lang.Integer.toUnsignedLong(_9_recipientPublicKeyLength)));
    long _11_senderPublicKeyIndex;
    _11_senderPublicKeyIndex = (long) (long) ((_10_recipientPublicKeyLengthIndex) + (Constants_Compile.__default.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _12_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (long) ((_10_recipientPublicKeyLengthIndex) + ((long) 4L)), (long) (_2_providerInfo).cardinalityInt()) < 0, __default.E(dafny.DafnySequence.asString("Key Provider Info Serialization Error. Serialized length less than expected.")));
    if ((_12_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_12_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _13_providerInfoRecipientPublicKey;
    _13_providerInfoRecipientPublicKey = (_2_providerInfo).subsequence(Constants_Compile.__default.ECDH__PROVIDER__INFO__RPK__INDEX(), dafny.Helpers.unsignedToInt(_10_recipientPublicKeyLengthIndex));
    dafny.DafnySequence<? extends java.lang.Byte> _14_providerInfoSenderPublicKey;
    _14_providerInfoSenderPublicKey = (_2_providerInfo).drop(_11_senderPublicKeyIndex);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _15_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = RawECDHKeyring_Compile.__default.DecompressPublicKey(_14_providerInfoSenderPublicKey, (this).curveSpec(), (this).cryptoPrimitives());
    _15_valueOrError4 = _out0;
    if ((_15_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_15_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _16_senderPublicKey;
    _16_senderPublicKey = (_15_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError5 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = RawECDHKeyring_Compile.__default.DecompressPublicKey(_13_providerInfoRecipientPublicKey, (this).curveSpec(), (this).cryptoPrimitives());
    _17_valueOrError5 = _out1;
    if ((_17_valueOrError5).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_17_valueOrError5).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _18_recipientPublicKey;
    _18_recipientPublicKey = (_17_valueOrError5).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _19_valueOrError6 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out2;
    _out2 = RawECDHKeyring_Compile.__default.ValidatePublicKey((this).cryptoPrimitives(), (this).curveSpec(), _16_senderPublicKey);
    _19_valueOrError6 = _out2;
    if ((_19_valueOrError6).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_19_valueOrError6).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    boolean _20___v0;
    _20___v0 = (_19_valueOrError6).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError7 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = RawECDHKeyring_Compile.__default.ValidatePublicKey((this).cryptoPrimitives(), (this).curveSpec(), _18_recipientPublicKey);
    _21_valueOrError7 = _out3;
    if ((_21_valueOrError7).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_21_valueOrError7).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    boolean _22___v1;
    _22___v1 = (_21_valueOrError7).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _23_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PublicKeyType(_16_senderPublicKey)) && (software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PublicKeyType((this).recipientPublicKey())), __default.E(dafny.DafnySequence.asString("Received serialized sender public key of incorrect length")));
    if ((_23_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_23_valueOrError8).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _24_sharedSecretPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    dafny.DafnySequence<? extends Character> _25_sharedSecretKmsKeyId = dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR);
    software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _source0 = (this).keyAgreementScheme();
    if (_source0.is_KmsPublicKeyDiscovery()) {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput _26___mcc_h0 = ((software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery)_source0)._KmsPublicKeyDiscovery;
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPublicKeyDiscoveryInput _27_kmsPublicKeyDiscovery = _26___mcc_h0;
      {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError9 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        _28_valueOrError9 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((_27_kmsPublicKeyDiscovery).dtor_recipientKmsIdentifier());
        if ((_28_valueOrError9).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_28_valueOrError9).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
          return res;
        }
        dafny.Tuple0 _29___v2;
        _29___v2 = (_28_valueOrError9).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _24_sharedSecretPublicKey = _16_senderPublicKey;
        _25_sharedSecretKmsKeyId = (_27_kmsPublicKeyDiscovery).dtor_recipientKmsIdentifier();
      }
    } else {
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput _30___mcc_h1 = ((software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey)_source0)._KmsPrivateKeyToStaticPublicKey;
      software.amazon.cryptography.materialproviders.internaldafny.types.KmsPrivateKeyToStaticPublicKeyInput _31_kmsPrivateKeyToStaticPublicKey = _30___mcc_h1;
      {
        Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _32_valueOrError10 = Wrappers_Compile.Result.<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.Tuple0.Default());
        _32_valueOrError10 = AwsKmsUtils_Compile.__default.ValidateKmsKeyId((_31_kmsPrivateKeyToStaticPublicKey).dtor_senderKmsIdentifier());
        if ((_32_valueOrError10).IsFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          res = (_32_valueOrError10).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
          return res;
        }
        dafny.Tuple0 _33___v3;
        _33___v3 = (_32_valueOrError10).Extract(dafny.Tuple0._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _25_sharedSecretKmsKeyId = (_31_kmsPrivateKeyToStaticPublicKey).dtor_senderKmsIdentifier();
        if (((_31_kmsPrivateKeyToStaticPublicKey).dtor_recipientPublicKey()).equals(_18_recipientPublicKey)) {
          _24_sharedSecretPublicKey = _18_recipientPublicKey;
        } else {
          _24_sharedSecretPublicKey = _16_senderPublicKey;
        }
      }
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _34_valueOrError11 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _34_valueOrError11 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.services.kms.internaldafny.types.__default.IsValid__PublicKeyType(_24_sharedSecretPublicKey), __default.E(dafny.DafnySequence.asString("Received Recipient Public Key of incorrect expected length")));
    if ((_34_valueOrError11).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_34_valueOrError11).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _35_valueOrError12 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out4;
    _out4 = __default.DeriveSharedSecret((this).client(), _25_sharedSecretKmsKeyId, _24_sharedSecretPublicKey, (this).grantTokens());
    _35_valueOrError12 = _out4;
    if ((_35_valueOrError12).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_35_valueOrError12).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _36_sharedSecret;
    _36_sharedSecret = (_35_valueOrError12).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    EcdhEdkWrapping_Compile.EcdhUnwrap _37_ecdhUnwrap;
    EcdhEdkWrapping_Compile.EcdhUnwrap _nw0 = new EcdhEdkWrapping_Compile.EcdhUnwrap();
    _nw0.__ctor(_14_providerInfoSenderPublicKey, _13_providerInfoRecipientPublicKey, _36_sharedSecret, __default.AWS__KMS__ECDH__KEYRING__VERSION(), (this).curveSpec(), (this).cryptoPrimitives());
    _37_ecdhUnwrap = _nw0;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _38_unwrapOutputRes;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out5;
    _out5 = EdkWrapping_Compile.__default.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>UnwrapEdkMaterial(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor(), (edk).dtor_ciphertext(), (this).materials(), _37_ecdhUnwrap);
    _38_unwrapOutputRes = _out5;
    Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _39_valueOrError13 = Wrappers_Compile.Result.<EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>Default(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor(), EcdhEdkWrapping_Compile.EcdhUnwrapInfo.Default()));
    _39_valueOrError13 = _38_unwrapOutputRes;
    if ((_39_valueOrError13).IsFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_39_valueOrError13).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    EdkWrapping_Compile.UnwrapEdkMaterialOutput<EcdhEdkWrapping_Compile.EcdhUnwrapInfo> _40_unwrapOutput;
    _40_unwrapOutput = (_39_valueOrError13).Extract(EdkWrapping_Compile.UnwrapEdkMaterialOutput.<EcdhEdkWrapping_Compile.EcdhUnwrapInfo>_typeDescriptor(EcdhEdkWrapping_Compile.EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _41_valueOrError14 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    _41_valueOrError14 = Materials_Compile.__default.DecryptionMaterialsAddDataKey((this).materials(), (_40_unwrapOutput).dtor_plaintextDataKey(), (_40_unwrapOutput).dtor_symmetricSigningKey());
    if ((_41_valueOrError14).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_41_valueOrError14).<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.SealedDecryptionMaterials._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _42_result;
    _42_result = (_41_valueOrError14).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _42_result);
    return res;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials materials()
  {
    return this._materials;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey()
  {
    return this._recipientPublicKey;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations _keyAgreementScheme;
  public software.amazon.cryptography.materialproviders.internaldafny.types.KmsEcdhStaticConfigurations keyAgreementScheme()
  {
    return this._keyAgreementScheme;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _client;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient client()
  {
    return this._client;
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
  private static final dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _TYPE = dafny.TypeDescriptor.<DecryptSingleEncryptedDataKey>referenceWithInitializer(DecryptSingleEncryptedDataKey.class, () -> (DecryptSingleEncryptedDataKey) null);
  public static dafny.TypeDescriptor<DecryptSingleEncryptedDataKey> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptSingleEncryptedDataKey>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "AwsKmsEcdhKeyring.DecryptSingleEncryptedDataKey";
  }
}
