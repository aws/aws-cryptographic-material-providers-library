// Class RawRSAKeyring
// Dafny class RawRSAKeyring compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawRSAKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public RawRSAKeyring() {
    this._cryptoPrimitives = null;
    this._privateKeyMaterial = Wrappers_Compile.Option.<RsaUnwrapKeyMaterial>Default(((dafny.TypeDescriptor<RsaUnwrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaUnwrapKeyMaterial.class)));
    this._publicKeyMaterial = Wrappers_Compile.Option.<RsaWrapKeyMaterial>Default(((dafny.TypeDescriptor<RsaWrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaWrapKeyMaterial.class)));
    this._publicKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    this._privateKey = Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
    this._keyNamespace = UTF8.ValidUTF8Bytes.defaultValue();
    this._keyName = UTF8.ValidUTF8Bytes.defaultValue();
    this._paddingScheme = software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode.Default();
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out3;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out3;
    _out3 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out3;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> namespace, dafny.DafnySequence<? extends java.lang.Byte> name, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey, software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyNamespace = namespace;
    (this)._keyName = name;
    (this)._paddingScheme = paddingScheme;
    (this)._publicKey = publicKey;
    (this)._privateKey = privateKey;
    (this)._cryptoPrimitives = cryptoPrimitives;
    Wrappers_Compile.Option<RsaUnwrapKeyMaterial> _0_localPrivateKeyMaterial;
    _0_localPrivateKeyMaterial = Wrappers_Compile.Option.<RsaUnwrapKeyMaterial>create_None(((dafny.TypeDescriptor<RsaUnwrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaUnwrapKeyMaterial.class)));
    if ((privateKey).is_Some()) {
      dafny.DafnySequence<? extends java.lang.Byte> _1_extract;
      _1_extract = (privateKey).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      if ((((long) (_1_extract).cardinalityInt()) == 0 ? 0 : 1) == 1) {
        RsaUnwrapKeyMaterial _2_unwrap;
        RsaUnwrapKeyMaterial _nw0 = new RsaUnwrapKeyMaterial();
        _nw0.__ctor(_1_extract, paddingScheme, cryptoPrimitives);
        _2_unwrap = _nw0;
        _0_localPrivateKeyMaterial = Wrappers_Compile.Option.<RsaUnwrapKeyMaterial>create_Some(((dafny.TypeDescriptor<RsaUnwrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaUnwrapKeyMaterial.class)), _2_unwrap);
      }
    }
    Wrappers_Compile.Option<RsaWrapKeyMaterial> _3_localPublicKeyMaterial;
    _3_localPublicKeyMaterial = Wrappers_Compile.Option.<RsaWrapKeyMaterial>create_None(((dafny.TypeDescriptor<RsaWrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaWrapKeyMaterial.class)));
    if ((publicKey).is_Some()) {
      dafny.DafnySequence<? extends java.lang.Byte> _4_extract;
      _4_extract = (publicKey).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      if ((((long) (_4_extract).cardinalityInt()) == 0 ? 0 : 1) == 1) {
        RsaWrapKeyMaterial _5_wrap;
        RsaWrapKeyMaterial _nw1 = new RsaWrapKeyMaterial();
        _nw1.__ctor(_4_extract, paddingScheme, cryptoPrimitives);
        _5_wrap = _nw1;
        _3_localPublicKeyMaterial = Wrappers_Compile.Option.<RsaWrapKeyMaterial>create_Some(((dafny.TypeDescriptor<RsaWrapKeyMaterial>)(java.lang.Object)dafny.TypeDescriptor.reference(RsaWrapKeyMaterial.class)), _5_wrap);
      }
    }
    (this)._publicKeyMaterial = _3_localPublicKeyMaterial;
    (this)._privateKeyMaterial = _0_localPrivateKeyMaterial;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).publicKeyMaterial()).is_Some(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A RawRSAKeyring without a public key cannot provide OnEncrypt")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return output;
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _1_materials;
      _1_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _2_suite;
      _2_suite = (_1_materials).dtor_algorithmSuite();
      RsaGenerateAndWrapKeyMaterial _3_generateAndWrap;
      RsaGenerateAndWrapKeyMaterial _nw0 = new RsaGenerateAndWrapKeyMaterial();
      _nw0.__ctor(((this).publicKey()).dtor_value(), (this).paddingScheme(), (this).cryptoPrimitives());
      _3_generateAndWrap = _nw0;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>Default(RsaWrapInfo._typeDescriptor(), RsaWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = EdkWrapping_Compile.__default.<RsaWrapInfo>WrapEdkMaterial(RsaWrapInfo._typeDescriptor(), _1_materials, ((this).publicKeyMaterial()).dtor_value(), _3_generateAndWrap);
      _4_valueOrError1 = _out0;
      if ((_4_valueOrError1).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_4_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return output;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<RsaWrapInfo> _5_wrapOutput;
      _5_wrapOutput = (_4_valueOrError1).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<RsaWrapInfo>_typeDescriptor(RsaWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _6_symmetricSigningKeyList;
      if (((_5_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_5_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _7_edk;
      _7_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create((this).keyNamespace(), (this).keyName(), (_5_wrapOutput).dtor_wrappedMaterial());
      if ((_5_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _8_valueOrError2 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_1_materials, (_5_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
        if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_8_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _9_result;
        _9_result = (_8_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_9_result));
        return output;
      } else if ((_5_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _10_valueOrError3 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_1_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
        if ((_10_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_10_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _11_result;
        _11_result = (_10_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_11_result));
        return output;
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((this).privateKeyMaterial()).is_Some(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("A RawRSAKeyring without a private key cannot provide OnEncrypt")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _1_materials;
    _1_materials = (input).dtor_materials();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_1_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_errors;
    _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> empty(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    long _hi0 = (long) ((input).dtor_encryptedDataKeys()).cardinalityInt();
    for (long _4_i = (long) 0L; java.lang.Long.compareUnsigned(_4_i, _hi0) < 0; _4_i++) {
      if ((this).ShouldDecryptEDK(((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_4_i)))))) {
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _5_edk;
        _5_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_4_i))));
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _6_unwrapOutput;
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<RsaUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = EdkWrapping_Compile.__default.<RsaUnwrapInfo>UnwrapEdkMaterial(RsaUnwrapInfo._typeDescriptor(), (_5_edk).dtor_ciphertext(), _1_materials, ((this).privateKeyMaterial()).dtor_value());
        _6_unwrapOutput = _out0;
        if ((_6_unwrapOutput).is_Success()) {
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _7_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
          _7_valueOrError2 = Materials_Compile.__default.DecryptionMaterialsAddDataKey(_1_materials, ((_6_unwrapOutput).dtor_value()).dtor_plaintextDataKey(), ((_6_unwrapOutput).dtor_value()).dtor_symmetricSigningKey());
          if ((_7_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_7_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _8_returnMaterials;
          _8_returnMaterials = (_7_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_8_returnMaterials));
          return output;
        } else {
          _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_3_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_6_unwrapOutput).dtor_error()));
        }
      } else {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        _9_valueOrError3 = (UTF8.__default.Decode((((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_4_i))))).dtor_keyProviderId())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_10_e_boxed0) -> {
          dafny.DafnySequence<? extends Character> _10_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_10_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_10_e);
        }));
        if ((_9_valueOrError3).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_9_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
          return output;
        }
        dafny.DafnySequence<? extends Character> _11_extractedKeyProviderId;
        _11_extractedKeyProviderId = (_9_valueOrError3).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _3_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_3_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(ErrorMessages_Compile.__default.IncorrectRawDataKeys(StandardLibrary_mString_Compile.__default.Base10Int2String(dafny.Helpers.unsignedToBigInteger(_4_i)), dafny.DafnySequence.asString("RSAKeyring"), _11_extractedKeyProviderId))));
      }
    }
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_3_errors, dafny.DafnySequence.asString("Raw RSA Key was unable to decrypt any encrypted data key. The list of encountered Exceptions is available via `list`.")));
    return output;
  }
  public boolean ShouldDecryptEDK(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk) {
    return (((UTF8.__default.ValidUTF8Seq((edk).dtor_keyProviderInfo())) && (((edk).dtor_keyProviderInfo()).equals((this).keyName()))) && (((edk).dtor_keyProviderId()).equals((this).keyNamespace()))) && ((((long) ((edk).dtor_ciphertext()).cardinalityInt()) == 0 ? 0 : 1) == 1);
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public Wrappers_Compile.Option<RsaUnwrapKeyMaterial> _privateKeyMaterial;
  public Wrappers_Compile.Option<RsaUnwrapKeyMaterial> privateKeyMaterial()
  {
    return this._privateKeyMaterial;
  }
  public Wrappers_Compile.Option<RsaWrapKeyMaterial> _publicKeyMaterial;
  public Wrappers_Compile.Option<RsaWrapKeyMaterial> publicKeyMaterial()
  {
    return this._publicKeyMaterial;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _publicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey()
  {
    return this._publicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _privateKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> privateKey()
  {
    return this._privateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _keyNamespace;
  public dafny.DafnySequence<? extends java.lang.Byte> keyNamespace()
  {
    return this._keyNamespace;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _keyName;
  public dafny.DafnySequence<? extends java.lang.Byte> keyName()
  {
    return this._keyName;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode _paddingScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.RSAPaddingMode paddingScheme()
  {
    return this._paddingScheme;
  }
  private static final dafny.TypeDescriptor<RawRSAKeyring> _TYPE = dafny.TypeDescriptor.<RawRSAKeyring>referenceWithInitializer(RawRSAKeyring.class, () -> (RawRSAKeyring) null);
  public static dafny.TypeDescriptor<RawRSAKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawRSAKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawRSAKeyring.RawRSAKeyring";
  }
}
