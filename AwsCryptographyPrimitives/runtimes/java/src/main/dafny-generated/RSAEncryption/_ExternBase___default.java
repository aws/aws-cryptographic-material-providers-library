// Class _ExternBase___default
// Dafny class __default compiled into Java
package RSAEncryption;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class _ExternBase___default {
  public _ExternBase___default() {
  }
  public static dafny.Tuple2 GenerateKeyPair(int lengthBits)
  {
    software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey publicKey = (software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey)null;
    software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey privateKey = (software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey)null;
    if(true) {
      dafny.DafnySequence<? extends java.lang.Byte> _0_pemPublic;
      dafny.DafnySequence<? extends java.lang.Byte> _1_pemPrivate;
      dafny.DafnySequence<? extends java.lang.Byte> _out0;
      dafny.DafnySequence<? extends java.lang.Byte> _out1;
      dafny.Tuple2<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends java.lang.Byte>> _outcollector0 = RSAEncryption.RSA.GenerateKeyPairExtern(lengthBits);
      _out0 = (dafny.DafnySequence<? extends java.lang.Byte>) (Object) _outcollector0.dtor__0();
      _out1 = (dafny.DafnySequence<? extends java.lang.Byte>) (Object) _outcollector0.dtor__1();
      _0_pemPublic = _out0;
      _1_pemPrivate = _out1;
      privateKey = software.amazon.cryptography.primitives.internaldafny.types.RSAPrivateKey.create(lengthBits, _1_pemPrivate);
      publicKey = software.amazon.cryptography.primitives.internaldafny.types.RSAPublicKey.create(lengthBits, _0_pemPublic);
    }
    return new dafny.Tuple2<>(publicKey, privateKey);
  }
  public static Wrappers_Compile.Result<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error> GetRSAKeyModulusLength(dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    Wrappers_Compile.Result<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = RSAEncryption.RSA.GetRSAKeyModulusLengthExtern(publicKey);
    if ((_0_valueOrError0).IsFailure(BoundedInts_Compile.uint32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      return (_0_valueOrError0).<java.lang.Integer>PropagateFailure(BoundedInts_Compile.uint32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), BoundedInts_Compile.int32._typeDescriptor());
    } else {
      int _1_length = (_0_valueOrError0).Extract(BoundedInts_Compile.uint32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (java.lang.Long.compareUnsigned((long) 81L, (long) java.lang.Integer.toUnsignedLong(_1_length)) <= 0) && (java.lang.Long.compareUnsigned((long) java.lang.Integer.toUnsignedLong(_1_length), (StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()).longValue()) < 0), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Unsupported length for RSA modulus.")));
      if ((_2_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
        return (_2_valueOrError1).<java.lang.Integer>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), BoundedInts_Compile.int32._typeDescriptor());
      } else {
        return Wrappers_Compile.Result.<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(BoundedInts_Compile.int32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (_1_length));
      }
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Decrypt(software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((long) ((input).dtor_privateKey()).cardinalityInt()) == 0 ? 0 : 1) == 1) && ((((long) ((input).dtor_cipherText()).cardinalityInt()) == 0 ? 0 : 1) == 1), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        return output;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = RSAEncryption.RSA.DecryptExtern((input).dtor_padding(), (input).dtor_privateKey(), (input).dtor_cipherText());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Encrypt(software.amazon.cryptography.primitives.internaldafny.types.RSAEncryptInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    if(true) {
      Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((long) ((input).dtor_publicKey()).cardinalityInt()) == 0 ? 0 : 1) == 1) && ((((long) ((input).dtor_plaintext()).cardinalityInt()) == 0 ? 0 : 1) == 1), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("")));
      if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
        output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        return output;
      }
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = RSAEncryption.RSA.EncryptExtern((input).dtor_padding(), (input).dtor_publicKey(), (input).dtor_plaintext());
      output = _out0;
    }
    return output;
  }
  public static Wrappers_Compile.Result<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetRSAKeyModulusLengthExternSuccess(int output) {
    return Wrappers_Compile.Result.<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(BoundedInts_Compile.uint32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), output);
  }
  public static Wrappers_Compile.Result<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateGetRSAKeyModulusLengthExternFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<java.lang.Integer, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(BoundedInts_Compile.uint32._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateBytesSuccess(dafny.DafnySequence<? extends java.lang.Byte> bytes) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), bytes);
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> CreateBytesFailure(software.amazon.cryptography.primitives.internaldafny.types.Error error) {
    return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), error);
  }
  @Override
  public java.lang.String toString() {
    return "RSAEncryption._default";
  }
}
