// Class _ExternBase___default
// Dafny class __default compiled into Java
package AESEncryption;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput EncryptionOutputFromByteSeq(dafny.DafnySequence<? extends java.lang.Byte> s, software.amazon.cryptography.primitives.internaldafny.types.AES__GCM encAlg)
  {
    long _0_pivot__point = (long) (long) (((long) (s).cardinalityInt()) - (((long) ((encAlg).dtor_tagLength()))));
    dafny.DafnySequence<? extends java.lang.Byte> _1_cipherText = (s).take(_0_pivot__point);
    dafny.DafnySequence<? extends java.lang.Byte> _2_authTag = (s).drop(_0_pivot__point);
    return software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.create(_1_cipherText, _2_authTag);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> AESEncrypt(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (((long) ((input).dtor_iv()).cardinalityInt()) == (((long) (((input).dtor_encAlg()).dtor_ivLength())))) && (((long) ((input).dtor_key()).cardinalityInt()) == (((long) (((input).dtor_encAlg()).dtor_keyLength())))), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Request does not match algorithm.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_encAlg = ((software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput)_let_tmp_rhs0)._encAlg;
    dafny.DafnySequence<? extends java.lang.Byte> _2_iv = ((software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput)_let_tmp_rhs0)._iv;
    dafny.DafnySequence<? extends java.lang.Byte> _3_key = ((software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput)_let_tmp_rhs0)._key;
    dafny.DafnySequence<? extends java.lang.Byte> _4_msg = ((software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput)_let_tmp_rhs0)._msg;
    dafny.DafnySequence<? extends java.lang.Byte> _5_aad = ((software.amazon.cryptography.primitives.internaldafny.types.AESEncryptInput)_let_tmp_rhs0)._aad;
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput.Default());
    Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = AESEncryption.AES_GCM.AESEncryptExtern(_1_encAlg, _2_iv, _3_key, _4_msg, _5_aad);
    _6_valueOrError1 = _out0;
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor())) {
      res = (_6_valueOrError1).<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor());
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput _7_value;
    _7_value = (_6_valueOrError1).Extract(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _8_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _8_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((long) ((_7_value).dtor_cipherText()).cardinalityInt()) == ((long) (_4_msg).cardinalityInt()), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("AESEncrypt did not return cipherText of expected length")));
    if ((_8_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_8_valueOrError2).<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor());
      return res;
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _9_valueOrError3 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError3 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((long) ((_7_value).dtor_authTag()).cardinalityInt()) == (((long) ((_1_encAlg).dtor_tagLength()))), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("AESEncryption did not return valid tag")));
    if ((_9_valueOrError3).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError3).<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor());
      return res;
    }
    res = Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _7_value);
    return res;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> AESDecrypt(software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((long) ((input).dtor_key()).cardinalityInt()) == (((long) (((input).dtor_encAlg()).dtor_keyLength())))) && (((long) ((input).dtor_iv()).cardinalityInt()) == (((long) (((input).dtor_encAlg()).dtor_ivLength()))))) && (((long) ((input).dtor_authTag()).cardinalityInt()) == (((long) (((input).dtor_encAlg()).dtor_tagLength())))), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Request does not match algorithm.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.AES__GCM _1_encAlg = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._encAlg;
    dafny.DafnySequence<? extends java.lang.Byte> _2_key = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._key;
    dafny.DafnySequence<? extends java.lang.Byte> _3_cipherTxt = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._cipherTxt;
    dafny.DafnySequence<? extends java.lang.Byte> _4_authTag = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._authTag;
    dafny.DafnySequence<? extends java.lang.Byte> _5_iv = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._iv;
    dafny.DafnySequence<? extends java.lang.Byte> _6_aad = ((software.amazon.cryptography.primitives.internaldafny.types.AESDecryptInput)_let_tmp_rhs0)._aad;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _7_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = AESEncryption.AES_GCM.AESDecryptExtern(_1_encAlg, _2_key, _3_cipherTxt, _4_authTag, _5_iv, _6_aad);
    _7_valueOrError1 = _out0;
    if ((_7_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor())) {
      res = (_7_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _8_value;
    _8_value = (_7_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((long) (_3_cipherTxt).cardinalityInt()) == ((long) (_8_value).cardinalityInt()), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("AESDecrypt did not return plaintext of expected length")));
    if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_9_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _8_value);
    return res;
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateAESEncryptExternSuccess(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput output) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateAESEncryptExternFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(software.amazon.cryptography.primitives.internaldafny.types.AESEncryptOutput._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateAESDecryptExternSuccess(dafny.DafnySequence<? extends java.lang.Byte> bytes) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), bytes);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateAESDecryptExternFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.OpaqueError._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "AESEncryption._default";
  }
}
