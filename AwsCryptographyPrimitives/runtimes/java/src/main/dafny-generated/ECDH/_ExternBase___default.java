// Class _ExternBase___default
// Dafny class __default compiled into Java
package ECDH;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GenerateEccKeyPair(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.Default());
    Wrappers_Compile.Result<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), EccKeyPair.Default());
    Wrappers_Compile.Result<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.KeyGeneration.GenerateKeyPair((input).dtor_eccCurve());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput>PropagateFailure(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor());
      return output;
    }
    EccKeyPair _1_keyPair;
    _1_keyPair = (_0_valueOrError0).Extract(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECCKeyPairOutput.create((input).dtor_eccCurve(), software.amazon.cryptography.primitives.internaldafny.types.ECCPrivateKey.create((_1_keyPair).dtor_privateKey()), software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create((_1_keyPair).dtor_publicKey())));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> GetPublicKeyFromPrivate(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.Default());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.ECCUtils.GetPublicKey((input).dtor_eccCurve(), (input).dtor_privateKey());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_publicKey;
    _1_publicKey = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GetPublicKeyFromPrivateKeyOutput.create((input).dtor_eccCurve(), (input).dtor_privateKey(), _1_publicKey));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ValidatePublicKey(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.Default());
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), false);
    Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.ECCUtils.ValidatePublicKey((input).dtor_eccCurve(), (input).dtor_publicKey());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput>PropagateFailure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor());
      return output;
    }
    boolean _1_result;
    _1_result = (_0_valueOrError0).Extract(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyOutput.create(_1_result));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DeriveSharedSecret(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.Default());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.DeriveSharedSecret.CalculateSharedSecret((input).dtor_eccCurve(), (input).dtor_privateKey(), (input).dtor_publicKey());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_derivedSharedSecret;
    _1_derivedSharedSecret = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DeriveSharedSecretOutput.create(_1_derivedSharedSecret));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> CompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.Default());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.ECCUtils.CompressPublicKey(((input).dtor_publicKey()).dtor_der(), (input).dtor_eccCurve());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_compressedPublicKey;
    _1_compressedPublicKey = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.CompressPublicKeyOutput.create(_1_compressedPublicKey));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> DecompressPublicKey(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.Default());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.ECCUtils.DecompressPublicKey((input).dtor_compressedPublicKey(), (input).dtor_eccCurve());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_decompressedPublicKey;
    _1_decompressedPublicKey = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.DecompressPublicKeyOutput.create(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_1_decompressedPublicKey)));
    return output;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> ParsePublicKey(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput.Default());
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ECDH.ECCUtils.ParsePublicKey((input).dtor_publicKey());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput._typeDescriptor());
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_derPublicKey;
    _1_derPublicKey = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.ParsePublicKeyOutput.create(software.amazon.cryptography.primitives.internaldafny.types.ECCPublicKey.create(_1_derPublicKey)));
    return output;
  }
  public static Wrappers_Compile.Result<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternEccKeyGenSuccess(EccKeyPair output) {
    return Wrappers_Compile.Result.<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternEccKeyGenFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<EccKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(EccKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternGetPublicKeyFromPrivateSuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternGetPublicKeyFromPrivateError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternValidatePublicKeySuccess(boolean output) {
    return Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternValidatePublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternDerivesharedSecretSuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternDerivesharedSecretError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternCompressPublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternCompressPublicKeySuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternDecompressPublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternDecompressPublicKeySuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternParsePublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternParsePublicKeySuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetInfinityPublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetInfinityPublicKeySuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetOutOfBoundsPublicKeyError(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetOutOfBoundsPublicKeySuccess(dafny.DafnySequence<? extends java.lang.Byte> output) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  @Override
  public java.lang.String toString() {
    return "ECDH._default";
  }
}
