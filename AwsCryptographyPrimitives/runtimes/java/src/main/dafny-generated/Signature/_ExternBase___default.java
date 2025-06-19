// Class _ExternBase___default
// Dafny class __default compiled into Java
package Signature;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static short SignatureLength(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm signatureAlgorithm) {
    software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm _source0 = signatureAlgorithm;
    if (_source0.is_ECDSA__P384()) {
      return (short) 103;
    } else {
      return (short) 71;
    }
  }
  public static long FieldSize(software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm signatureAlgorithm) {
    software.amazon.cryptography.primitives.internaldafny.types.ECDSASignatureAlgorithm _source0 = signatureAlgorithm;
    if (_source0.is_ECDSA__P384()) {
      return (long) 49L;
    } else {
      return (long) 33L;
    }
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> KeyGen(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.Default());
    Wrappers_Compile.Result<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Result.<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), SignatureKeyPair.Default());
    Wrappers_Compile.Result<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = Signature.ECDSA.ExternKeyGen((input).dtor_signatureAlgorithm());
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput>PropagateFailure(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor());
      return res;
    }
    SignatureKeyPair _1_sigKeyPair;
    _1_sigKeyPair = (_0_valueOrError0).Extract(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((long) ((_1_sigKeyPair).dtor_verificationKey()).cardinalityInt()) == (__default.FieldSize((input).dtor_signatureAlgorithm())), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Incorrect verification-key length from ExternKeyGen.")));
    if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError1).<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor());
      return res;
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.GenerateECDSASignatureKeyOutput.create((input).dtor_signatureAlgorithm(), (_1_sigKeyPair).dtor_verificationKey(), (_1_sigKeyPair).dtor_signingKey()));
    return res;
  }
  public static Wrappers_Compile.Result<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternKeyGenSuccess(SignatureKeyPair output) {
    return Wrappers_Compile.Result.<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateExternKeyGenFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<SignatureKeyPair, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(SignatureKeyPair._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateSignSuccess(dafny.DafnySequence<? extends java.lang.Byte> bytes) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), bytes);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateSignFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateVerifySuccess(boolean b) {
    return Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), b);
  }
  public static Wrappers_Compile.Result<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateVerifyFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<Boolean, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.TypeDescriptor.BOOLEAN, software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "Signature._default";
  }
}
