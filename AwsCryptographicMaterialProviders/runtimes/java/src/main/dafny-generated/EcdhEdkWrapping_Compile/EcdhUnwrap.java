// Class EcdhUnwrap
// Dafny class EcdhUnwrap compiled into Java
package EcdhEdkWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class EcdhUnwrap implements MaterialWrapping_Compile.UnwrapMaterial<EcdhUnwrapInfo>, Actions_Compile.ActionWithResult<MaterialWrapping_Compile.UnwrapInput, MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>, Actions_Compile.Action<MaterialWrapping_Compile.UnwrapInput, Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>> {
  public EcdhUnwrap() {
    this._senderPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._recipientPublicKey = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._sharedSecret = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._keyringVersion = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._curveSpec = software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default();
    this._crypto = null;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey, dafny.DafnySequence<? extends java.lang.Byte> sharedSecret, dafny.DafnySequence<? extends java.lang.Byte> keyringVersion, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    (this)._senderPublicKey = senderPublicKey;
    (this)._recipientPublicKey = recipientPublicKey;
    (this)._sharedSecret = sharedSecret;
    (this)._keyringVersion = keyringVersion;
    (this)._curveSpec = curveSpec;
    (this)._crypto = crypto;
  }
  public Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> Invoke(MaterialWrapping_Compile.UnwrapInput input)
  {
    Wrappers_Compile.Result<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>Default(EcdhUnwrapInfo._typeDescriptor(), EcdhUnwrapInfo.Default()));
    software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo _0_suite;
    _0_suite = (input).dtor_algorithmSuite();
    dafny.DafnySequence<? extends java.lang.Byte> _1_wrappedMaterial;
    _1_wrappedMaterial = (input).dtor_wrappedMaterial();
    dafny.DafnyMap<? extends dafny.DafnySequence<? extends java.lang.Byte>, ? extends dafny.DafnySequence<? extends java.lang.Byte>> _2_aad;
    _2_aad = (input).dtor_encryptionContext();
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _3_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _3_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (_1_wrappedMaterial).cardinalityInt(), Constants_Compile.__default.CIPHERTEXT__WRAPPED__MATERIAL__INDEX()) > 0, __default.E(dafny.DafnySequence.asString("Received ciphertext is shorter than expected.")));
    if ((_3_valueOrError0).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_3_valueOrError0).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    int _4_KeyLength;
    _4_KeyLength = AlgorithmSuites_Compile.__default.GetEncryptKeyLength(_0_suite);
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _5_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _5_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((_1_wrappedMaterial).length())).compareTo((dafny.Helpers.unsignedToBigInteger(Constants_Compile.__default.ECDH__WRAPPED__KEY__MATERIAL__INDEX())).add(java.math.BigInteger.valueOf(_4_KeyLength))) > 0, software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(dafny.DafnySequence.asString("Received EDK Ciphertext of incorrect length3.")));
    if ((_5_valueOrError1).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_5_valueOrError1).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _6_kdfNonce;
    _6_kdfNonce = (_1_wrappedMaterial).take(Constants_Compile.__default.ECDH__COMMITMENT__KEY__INDEX());
    dafny.DafnySequence<? extends java.lang.Byte> _7_iv;
    _7_iv = dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf((Constants_Compile.__default.ECDH__AES__256__ENC__ALG()).dtor_ivLength()), ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_8___v0_boxed0) -> {
      java.math.BigInteger _8___v0 = ((java.math.BigInteger)(java.lang.Object)(_8___v0_boxed0));
      return (byte) 0;
    }));
    dafny.DafnySequence<? extends java.lang.Byte> _9_commitmentKey;
    _9_commitmentKey = (_1_wrappedMaterial).subsequence(dafny.Helpers.unsignedToInt(Constants_Compile.__default.ECDH__COMMITMENT__KEY__INDEX()), dafny.Helpers.unsignedToInt(Constants_Compile.__default.ECDH__WRAPPED__KEY__MATERIAL__INDEX()));
    dafny.DafnySequence<? extends java.lang.Byte> _10_wrappedKey;
    _10_wrappedKey = (_1_wrappedMaterial).subsequence(dafny.Helpers.unsignedToInt(Constants_Compile.__default.ECDH__WRAPPED__KEY__MATERIAL__INDEX()), dafny.Helpers.unsignedToInt((long) (long) ((Constants_Compile.__default.ECDH__WRAPPED__KEY__MATERIAL__INDEX()) + (((long) (_4_KeyLength))))));
    dafny.DafnySequence<? extends java.lang.Byte> _11_authTag;
    _11_authTag = (_1_wrappedMaterial).drop((long) (long) ((Constants_Compile.__default.ECDH__WRAPPED__KEY__MATERIAL__INDEX()) + (((long) (_4_KeyLength)))));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _12_valueOrError2 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), UTF8.ValidUTF8Bytes.defaultValue());
    _12_valueOrError2 = (UTF8.__default.Encode(__default.CurveSpecTypeToString((this).curveSpec()))).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), __default::E);
    if ((_12_valueOrError2).IsFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_12_valueOrError2).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _13_curveSpecUtf8;
    _13_curveSpecUtf8 = (_12_valueOrError2).Extract(UTF8.ValidUTF8Bytes._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _14_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _14_valueOrError3 = CanonicalEncryptionContext_Compile.__default.EncryptionContextToAAD((input).dtor_encryptionContext());
    if ((_14_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_14_valueOrError3).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _15_canonicalizedEC;
    _15_canonicalizedEC = (_14_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _16_fixedInfo;
    _16_fixedInfo = __default.SerializeFixedInfo(Constants_Compile.__default.ECDH__KDF__UTF8(), _13_curveSpecUtf8, (this).senderPublicKey(), (this).recipientPublicKey(), _15_canonicalizedEC, (this).keyringVersion());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _17_valueOrError4 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
    _out0 = __default.DeriveSharedKeyingMaterial((this).sharedSecret(), _16_fixedInfo, _6_kdfNonce, (this).crypto());
    _17_valueOrError4 = _out0;
    if ((_17_valueOrError4).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_17_valueOrError4).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _18_derivedKeyingMaterial;
    _18_derivedKeyingMaterial = (_17_valueOrError4).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _19_calculatedCommitmentKey;
    _19_calculatedCommitmentKey = (_18_derivedKeyingMaterial).take(32);
    dafny.DafnySequence<? extends java.lang.Byte> _20_sharedKeyingMaterial;
    _20_sharedKeyingMaterial = (_18_derivedKeyingMaterial).drop(32);
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _21_valueOrError5 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _21_valueOrError5 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((long) (_19_calculatedCommitmentKey).cardinalityInt()) == ((long) (_9_commitmentKey).cardinalityInt()), __default.E(dafny.DafnySequence.asString("Calculated commitment key length does NOT match expected commitment key length")));
    if ((_21_valueOrError5).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_21_valueOrError5).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    boolean _22_check_q;
    boolean _out1;
    _out1 = (this).commitmentKeyCheck(_19_calculatedCommitmentKey, _9_commitmentKey);
    _22_check_q = _out1;
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _23_valueOrError6 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _23_valueOrError6 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _22_check_q, __default.E(dafny.DafnySequence.asString("Commitment keys do not match")));
    if ((_23_valueOrError6).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_23_valueOrError6).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _24_maybeUnwrappedPdk;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out2;
    _out2 = ((this).crypto()).AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput.create(Constants_Compile.__default.ECDH__AES__256__ENC__ALG(), _20_sharedKeyingMaterial, _10_wrappedKey, _11_authTag, _7_iv, _16_fixedInfo));
    _24_maybeUnwrappedPdk = _out2;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _25_valueOrError7 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    _25_valueOrError7 = (_24_maybeUnwrappedPdk).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_26_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _26_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_26_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_26_e);
    }));
    if ((_25_valueOrError7).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_25_valueOrError7).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _27_unwrappedPdk;
    _27_unwrappedPdk = (_25_valueOrError7).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.materialproviders.internaldafny.types.Error> _28_valueOrError8 = Wrappers_Compile.Outcome.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    _28_valueOrError8 = Wrappers_Compile.__default.<software.amazon.cryptography.materialproviders.internaldafny.types.Error>Need(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((long) (_27_unwrappedPdk).cardinalityInt()) == (((long) (AlgorithmSuites_Compile.__default.GetEncryptKeyLength((input).dtor_algorithmSuite())))), __default.E(dafny.DafnySequence.asString("Invalid Key Length")));
    if ((_28_valueOrError8).IsFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_28_valueOrError8).<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>>PropagateFailure(software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()));
      return res;
    }
    MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo> _29_output;
    _29_output = MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>create(EcdhUnwrapInfo._typeDescriptor(), _27_unwrappedPdk, EcdhUnwrapInfo.create());
    res = Wrappers_Compile.Result.<MaterialWrapping_Compile.UnwrapOutput<EcdhUnwrapInfo>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(MaterialWrapping_Compile.UnwrapOutput.<EcdhUnwrapInfo>_typeDescriptor(EcdhUnwrapInfo._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _29_output);
    return res;
  }
  public boolean commitmentKeyCheck(dafny.DafnySequence<? extends java.lang.Byte> calculatedCommitmentKey, dafny.DafnySequence<? extends java.lang.Byte> serializedCommitmentKey)
  {
    boolean res = false;
    if(true) {
      byte _0_diff_q;
      _0_diff_q = (byte) 0;
      long _hi0 = (long) (serializedCommitmentKey).cardinalityInt();
      for (long _1_i = (long) 0L; java.lang.Long.compareUnsigned(_1_i, _hi0) < 0; _1_i++) {
        _0_diff_q = (byte) (byte) ((byte)((_0_diff_q) | ((byte) (byte) ((byte)(((((byte)(java.lang.Object)((calculatedCommitmentKey).select(dafny.Helpers.unsignedToInt(_1_i)))))) ^ ((((byte)(java.lang.Object)((serializedCommitmentKey).select(dafny.Helpers.unsignedToInt(_1_i)))))))))));
      }
      res = ((_0_diff_q) == 0 ? 0 : 1) == 0;
    }
    return res;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _senderPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> senderPublicKey()
  {
    return this._senderPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _recipientPublicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey()
  {
    return this._recipientPublicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _sharedSecret;
  public dafny.DafnySequence<? extends java.lang.Byte> sharedSecret()
  {
    return this._sharedSecret;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _keyringVersion;
  public dafny.DafnySequence<? extends java.lang.Byte> keyringVersion()
  {
    return this._keyringVersion;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec()
  {
    return this._curveSpec;
  }
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient _crypto;
  public software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto()
  {
    return this._crypto;
  }
  private static final dafny.TypeDescriptor<EcdhUnwrap> _TYPE = dafny.TypeDescriptor.<EcdhUnwrap>referenceWithInitializer(EcdhUnwrap.class, () -> (EcdhUnwrap) null);
  public static dafny.TypeDescriptor<EcdhUnwrap> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhUnwrap>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "EcdhEdkWrapping.EcdhUnwrap";
  }
}
