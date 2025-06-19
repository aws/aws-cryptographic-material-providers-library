// Class RawAESKeyring
// Dafny class RawAESKeyring compiled into Java
package RawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RawAESKeyring implements Keyring_Compile.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring {
  public RawAESKeyring() {
    this._wrappingKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._cryptoPrimitives = null;
    this._wrappingAlgorithm = (software.amazon.cryptography.primitives.internaldafny.types.AES__GCM)null;
    this._keyNamespace = UTF8.ValidUTF8Bytes.defaultValue();
    this._keyName = UTF8.ValidUTF8Bytes.defaultValue();
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnDecrypt(this, input);
    return _out1;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out1;
    _out1 = software.amazon.cryptography.materialproviders.internaldafny.types._Companion_IKeyring.OnEncrypt(this, input);
    return _out1;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> namespace, dafny.DafnySequence<? extends java.lang.Byte> name, dafny.DafnySequence<? extends java.lang.Byte> key, software.amazon.cryptography.primitives.internaldafny.types.AES__GCM wrappingAlgorithm, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives)
  {
    (this)._keyNamespace = namespace;
    (this)._keyName = name;
    (this)._wrappingKey = key;
    (this)._wrappingAlgorithm = wrappingAlgorithm;
    (this)._cryptoPrimitives = cryptoPrimitives;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnEncrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _0_materials;
      _0_materials = (input).dtor_materials();
      software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _1_suite;
      _1_suite = (_0_materials).dtor_algorithmSuite();
      AesWrapKeyMaterial _2_wrap;
      AesWrapKeyMaterial _nw0 = new AesWrapKeyMaterial();
      _nw0.__ctor((this).wrappingKey(), (this).wrappingAlgorithm(), (this).cryptoPrimitives());
      _2_wrap = _nw0;
      AesGenerateAndWrapKeyMaterial _3_generateAndWrap;
      AesGenerateAndWrapKeyMaterial _nw1 = new AesGenerateAndWrapKeyMaterial();
      _nw1.__ctor(_2_wrap);
      _3_generateAndWrap = _nw1;
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError0 = Wrappers_Compile.Result.<EdkWrapping_Compile.WrapEdkMaterialOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(EdkWrapping_Compile.WrapEdkMaterialOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), EdkWrapping_Compile.WrapEdkMaterialOutput.<AesWrapInfo>Default(AesWrapInfo._typeDescriptor(), AesWrapInfo.Default()));
      Wrappers_Compile.Result<EdkWrapping_Compile.WrapEdkMaterialOutput<AesWrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = EdkWrapping_Compile.__default.<AesWrapInfo>WrapEdkMaterial(AesWrapInfo._typeDescriptor(), _0_materials, _2_wrap, _3_generateAndWrap);
      _4_valueOrError0 = _out0;
      if ((_4_valueOrError0).IsFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        output = (_4_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(EdkWrapping_Compile.WrapEdkMaterialOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
        return output;
      }
      EdkWrapping_Compile.WrapEdkMaterialOutput<AesWrapInfo> _5_wrapOutput;
      _5_wrapOutput = (_4_valueOrError0).Extract(EdkWrapping_Compile.WrapEdkMaterialOutput.<AesWrapInfo>_typeDescriptor(AesWrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>> _6_symmetricSigningKeyList;
      if (((_5_wrapOutput).dtor_symmetricSigningKey()).is_Some()) {
        _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_Some(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>> of(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), ((_5_wrapOutput).dtor_symmetricSigningKey()).dtor_value()));
      } else {
        _6_symmetricSigningKeyList = Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends java.lang.Byte>>>create_None(dafny.DafnySequence.<dafny.DafnySequence<? extends java.lang.Byte>>_typeDescriptor(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
      }
      software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _7_edk;
      _7_edk = software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey.create((this).keyNamespace(), (this).SerializeProviderInfo(((_5_wrapOutput).dtor_wrapInfo()).dtor_iv()), (_5_wrapOutput).dtor_wrappedMaterial());
      if ((_5_wrapOutput).is_GenerateAndWrapEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _8_valueOrError1 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _8_valueOrError1 = Materials_Compile.__default.EncryptionMaterialAddDataKey(_0_materials, (_5_wrapOutput).dtor_plaintextDataKey(), dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
        if ((_8_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_8_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _9_result;
        _9_result = (_8_valueOrError1).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_9_result));
        return output;
      } else if ((_5_wrapOutput).is_WrapOnlyEdkMaterialOutput()) {
        Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_valueOrError2 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
        _10_valueOrError2 = Materials_Compile.__default.EncryptionMaterialAddEncryptedDataKeys(_0_materials, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey> of(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey._typeDescriptor(), _7_edk), _6_symmetricSigningKeyList);
        if ((_10_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_10_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor());
          return output;
        }
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials _11_result;
        _11_result = (_10_valueOrError2).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnEncryptOutput.create(_11_result));
        return output;
      }
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> OnDecrypt_k(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _0_materials;
    _0_materials = (input).dtor_materials();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _1_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), Materials_Compile.__default.DecryptionMaterialsWithoutPlaintextDataKey(_0_materials), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Keyring received decryption materials that already contain a plaintext data key.")));
    if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_1_valueOrError0).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _2_valueOrError1 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD(((input).dtor_materials()).dtor_encryptionContext());
    if ((_2_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_2_valueOrError1).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_aad;
    _3_aad = (_2_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _4_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _4_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((long) ((this).wrappingKey()).cardinalityInt()) == (((long) (((this).wrappingAlgorithm()).dtor_keyLength()))), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("The wrapping key does not match the wrapping algorithm")));
    if ((_4_valueOrError2).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      output = (_4_valueOrError2).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_errors;
    _5_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> empty(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    long _hi0 = (long) ((input).dtor_encryptedDataKeys()).cardinalityInt();
    for (long _6_i = (long) 0L; java.lang.Long.compareUnsigned(_6_i, _hi0) < 0; _6_i++) {
      if ((this).ShouldDecryptEDK(((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_6_i)))))) {
        software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey _7_edk;
        _7_edk = ((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_6_i))));
        dafny.DafnySequence<? extends java.lang.Byte> _8_iv;
        _8_iv = (this).GetIvFromProvInfo((_7_edk).dtor_keyProviderInfo());
        AesUnwrapKeyMaterial _9_unwrap;
        AesUnwrapKeyMaterial _nw0 = new AesUnwrapKeyMaterial();
        _nw0.__ctor((this).wrappingKey(), (this).wrappingAlgorithm(), _8_iv, (this).cryptoPrimitives());
        _9_unwrap = _nw0;
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _10_unwrapOutput;
        Wrappers_Compile.Result<EdkWrapping_Compile.UnwrapEdkMaterialOutput<AesUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
        _out0 = EdkWrapping_Compile.__default.<AesUnwrapInfo>UnwrapEdkMaterial(AesUnwrapInfo._typeDescriptor(), (_7_edk).dtor_ciphertext(), _0_materials, _9_unwrap);
        _10_unwrapOutput = _out0;
        if ((_10_unwrapOutput).is_Success()) {
          Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _11_valueOrError3 = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
          _11_valueOrError3 = Materials_Compile.__default.DecryptionMaterialsAddDataKey(_0_materials, ((_10_unwrapOutput).dtor_value()).dtor_plaintextDataKey(), ((_10_unwrapOutput).dtor_value()).dtor_symmetricSigningKey());
          if ((_11_valueOrError3).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
            output = (_11_valueOrError3).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
            return output;
          }
          software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials _12_result;
          _12_result = (_11_valueOrError3).Extract(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
          software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput _13_value;
          _13_value = software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput.create(_12_result);
          output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _13_value);
          return output;
        } else {
          _5_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_5_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_10_unwrapOutput).dtor_error()));
        }
      } else {
        Wrappers_Compile.Result<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
        _14_valueOrError4 = (UTF8.__default.Decode((((software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey)(java.lang.Object)(((input).dtor_encryptedDataKeys()).select(dafny.Helpers.unsignedToInt(_6_i))))).dtor_keyProviderId())).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_15_e_boxed0) -> {
          dafny.DafnySequence<? extends Character> _15_e = ((dafny.DafnySequence<? extends Character>)(java.lang.Object)(_15_e_boxed0));
          return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(_15_e);
        }));
        if ((_14_valueOrError4).IsFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
          output = (_14_valueOrError4).<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput>PropagateFailure(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor());
          return output;
        }
        dafny.DafnySequence<? extends Character> _16_extractedKeyProviderId;
        _16_extractedKeyProviderId = (_14_valueOrError4).Extract(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
        _5_errors = dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>concatenate(_5_errors, dafny.DafnySequence.<software.amazon.cryptography.materialproviders.internaldafny.types.Error> of(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(ErrorMessages_Compile.__default.IncorrectRawDataKeys(StandardLibrary_mString_Compile.__default.Base10Int2String(dafny.Helpers.unsignedToBigInteger(_6_i)), dafny.DafnySequence.asString("AESKeyring"), _16_extractedKeyProviderId))));
      }
    }
    output = Wrappers_Compile.Result.<software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_CollectionOfErrors(_5_errors, dafny.DafnySequence.asString("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")));
    return output;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> SerializeProviderInfo(dafny.DafnySequence<? extends java.lang.Byte> iv) {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate((this).keyName(), StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(((int) ((((this).wrappingAlgorithm()).dtor_tagLength()) * (8))))), StandardLibrary_mUInt_Compile.__default.UInt32ToSeq((((this).wrappingAlgorithm()).dtor_ivLength()))), iv);
  }
  public boolean ShouldDecryptEDK(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptedDataKey edk) {
    return (((edk).dtor_keyProviderId()).equals((this).keyNamespace())) && ((this).ValidProviderInfo((edk).dtor_keyProviderInfo()));
  }
  public boolean ValidProviderInfo(dafny.DafnySequence<? extends java.lang.Byte> info) {
    long _0_keyname__size = (long) ((this).keyName()).cardinalityInt();
    return (((((((long) (info).cardinalityInt()) == (StandardLibrary_mMemoryMath_Compile.__default.Add4(_0_keyname__size, __default.AUTH__TAG__LEN__LEN(), __default.IV__LEN__LEN(), ((long) (((this).wrappingAlgorithm()).dtor_ivLength()))))) && (((info).take(_0_keyname__size)).equals((this).keyName()))) && ((StandardLibrary_mUInt_Compile.__default.SeqToUInt32((info).subsequence(dafny.Helpers.unsignedToInt(_0_keyname__size), dafny.Helpers.unsignedToInt((long) (long) ((_0_keyname__size) + (__default.AUTH__TAG__LEN__LEN())))))) == (128))) && ((128) == ((int) (((((this).wrappingAlgorithm()).dtor_tagLength())) * (8))))) && ((StandardLibrary_mUInt_Compile.__default.SeqToUInt32((info).subsequence(dafny.Helpers.unsignedToInt((long) (long) ((_0_keyname__size) + (__default.AUTH__TAG__LEN__LEN()))), dafny.Helpers.unsignedToInt((long) (long) (((long) (long) ((_0_keyname__size) + (__default.AUTH__TAG__LEN__LEN()))) + (__default.IV__LEN__LEN())))))) == ((((this).wrappingAlgorithm()).dtor_ivLength())))) && ((StandardLibrary_mUInt_Compile.__default.SeqToUInt32((info).subsequence(dafny.Helpers.unsignedToInt((long) (long) ((_0_keyname__size) + (__default.AUTH__TAG__LEN__LEN()))), dafny.Helpers.unsignedToInt((long) (long) (((long) (long) ((_0_keyname__size) + (__default.AUTH__TAG__LEN__LEN()))) + (__default.IV__LEN__LEN())))))) == (12));
  }
  public dafny.DafnySequence<? extends java.lang.Byte> GetIvFromProvInfo(dafny.DafnySequence<? extends java.lang.Byte> info) {
    return (info).drop((long) (long) (((long) (long) (((long) ((this).keyName()).cardinalityInt()) + (__default.AUTH__TAG__LEN__LEN()))) + (__default.IV__LEN__LEN())));
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _wrappingKey;
  public dafny.DafnySequence<? extends java.lang.Byte> wrappingKey()
  {
    return this._wrappingKey;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _cryptoPrimitives;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient cryptoPrimitives()
  {
    return this._cryptoPrimitives;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _wrappingAlgorithm;
  public software.amazon.cryptography.primitives.internaldafny.types.AES__GCM wrappingAlgorithm()
  {
    return this._wrappingAlgorithm;
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
  private static final dafny.TypeDescriptor<RawAESKeyring> _TYPE = dafny.TypeDescriptor.<RawAESKeyring>referenceWithInitializer(RawAESKeyring.class, () -> (RawAESKeyring) null);
  public static dafny.TypeDescriptor<RawAESKeyring> _typeDescriptor() {
    return (dafny.TypeDescriptor<RawAESKeyring>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "RawAESKeyring.RawAESKeyring";
  }
}
