// Class __default
// Dafny class __default compiled into Java
package RawECDHKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static boolean ValidPublicKeyLength(dafny.DafnySequence<? extends java.lang.Byte> p) {
    long _0_len = (long) (p).cardinalityInt();
    return (true) && ((((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__LEN__ECC__NIST__256())) || ((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__LEN__ECC__NIST__384()))) || ((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__LEN__ECC__NIST__521())));
  }
  public static boolean ValidCompressedPublicKeyLength(dafny.DafnySequence<? extends java.lang.Byte> p) {
    long _0_len = (long) (p).cardinalityInt();
    return (true) && ((((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256())) || ((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384()))) || ((_0_len) == (Constants_Compile.__default.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521())));
  }
  public static boolean ValidProviderInfoLength(dafny.DafnySequence<? extends java.lang.Byte> p) {
    long _0_len = (long) (p).cardinalityInt();
    return (((_0_len) == ((long) java.lang.Integer.toUnsignedLong(Constants_Compile.__default.ECDH__PROVIDER__INFO__256__LEN()))) || ((_0_len) == ((long) java.lang.Integer.toUnsignedLong(Constants_Compile.__default.ECDH__PROVIDER__INFO__384__LEN())))) || ((_0_len) == ((long) java.lang.Integer.toUnsignedLong(Constants_Compile.__default.ECDH__PROVIDER__INFO__521__LEN())));
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> LocalDeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey senderPrivateKey, software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey recipientPublicKey, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeSharedSecret;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = (crypto).DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput.create(curveSpec, senderPrivateKey, recipientPublicKey));
    _0_maybeSharedSecret = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
    _1_valueOrError0 = (_0_maybeSharedSecret).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput _3_sharedSecretOutput;
    _3_sharedSecretOutput = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_3_sharedSecretOutput).dtor_sharedSecret());
    return res;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey publicKey, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeCompressedPublicKey;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = (crypto).CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput.create(publicKey, curveSpec));
    _0_maybeCompressedPublicKey = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.Default());
    _1_valueOrError0 = (_0_maybeCompressedPublicKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput _3_compressedPublicKey;
    _3_compressedPublicKey = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_3_compressedPublicKey).dtor_compressedPublicKey());
    return res;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecompressPublicKey(dafny.DafnySequence<? extends java.lang.Byte> publicKey, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybePublicKey;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = (crypto).DecompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput.create(publicKey, curveSpec));
    _0_maybePublicKey = _out0;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.Default());
    _1_valueOrError0 = (_0_maybePublicKey).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
      software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
      return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
    }));
    if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
      res = (_1_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput _3_publicKey;
    _3_publicKey = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((_3_publicKey).dtor_publicKey()).dtor_der());
    return res;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SerializeProviderInfo(dafny.DafnySequence<? extends java.lang.Byte> senderPublicKey, dafny.DafnySequence<? extends java.lang.Byte> recipientPublicKey)
  {
    return dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(__default.RAW__ECDH__KEYRING__VERSION(), StandardLibrary_mUInt_Compile.__default.UInt32ToSeq((recipientPublicKey).cardinalityInt())), recipientPublicKey), StandardLibrary_mUInt_Compile.__default.UInt32ToSeq((senderPublicKey).cardinalityInt())), senderPublicKey);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GenerateEphemeralEccKeyPair(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeKeyPair;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = (crypto).GenerateECCKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput.create(curveSpec));
      _0_maybeKeyPair = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
      _1_valueOrError0 = (_0_maybeKeyPair).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_1_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor());
        return res;
      }
      software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput _3_keyPair;
      _3_keyPair = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), _3_keyPair);
    }
    return res;
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidatePublicKey(software.amazon.cryptography.primitives.internaldafny.AtomicPrimitivesClient crypto, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, dafny.DafnySequence<? extends java.lang.Byte> publicKey)
  {
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error> res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), false);
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_maybeValidate;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = (crypto).ValidatePublicKey(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput.create(curveSpec, publicKey));
      _0_maybeValidate = _out0;
      Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _1_valueOrError0 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.materialproviders.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.Default());
      _1_valueOrError0 = (_0_maybeValidate).<software.amazon.cryptography.materialproviders.internaldafny.types.Error>MapFailure(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), ((java.util.function.Function<software.amazon.cryptography.primitives.internaldafny.types.Error, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)(_2_e_boxed0) -> {
        software.amazon.cryptography.primitives.internaldafny.types.Error _2_e = ((software.amazon.cryptography.primitives.internaldafny.types.Error)(java.lang.Object)(_2_e_boxed0));
        return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographyPrimitives(_2_e);
      }));
      if ((_1_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor())) {
        res = (_1_valueOrError0).<Boolean>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), dafny.TypeDescriptor.BOOLEAN);
        return res;
      }
      software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput _3_validate;
      _3_validate = (_1_valueOrError0).Extract(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor());
      res = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.materialproviders.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.materialproviders.internaldafny.types.Error._typeDescriptor(), (_3_validate).dtor_success());
    }
    return res;
  }
  public static dafny.DafnySequence<? extends Character> CurveSpecTypeToString(software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec c) {
    software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _source0 = c;
    if (_source0.is_ECC__NIST__P256()) {
      return dafny.DafnySequence.asString("p256");
    } else if (_source0.is_ECC__NIST__P384()) {
      return dafny.DafnySequence.asString("p384");
    } else if (_source0.is_ECC__NIST__P521()) {
      return dafny.DafnySequence.asString("p521");
    } else {
      return dafny.DafnySequence.asString("sm2");
    }
  }
  public static software.amazon.cryptography.materialproviders.internaldafny.types.Error E(dafny.DafnySequence<? extends Character> s) {
    return software.amazon.cryptography.materialproviders.internaldafny.types.Error.create_AwsCryptographicMaterialProvidersException(s);
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> RAW__ECDH__KEYRING__VERSION()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 1);
  }
  @Override
  public java.lang.String toString() {
    return "RawECDHKeyring._default";
  }
}
