// Class __default
// Dafny class __default compiled into Java
package KdfCtr_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> KdfCounterMode(software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((((java.util.Objects.equals((input).dtor_digestAlgorithm(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256())) || (java.util.Objects.equals((input).dtor_digestAlgorithm(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((((long) ((input).dtor_ikm()).cardinalityInt()) == ((long) 32L)) || (((long) ((input).dtor_ikm()).cardinalityInt()) == ((long) 48L))) || (((long) ((input).dtor_ikm()).cardinalityInt()) == ((long) 66L)))) && (((input).dtor_nonce()).is_Some())) && ((((long) (((input).dtor_nonce()).dtor_value()).cardinalityInt()) == ((long) 16L)) || (((long) (((input).dtor_nonce()).dtor_value()).cardinalityInt()) == ((long) 32L)))) && ((((input).dtor_expectedLength()) == (32)) || (((input).dtor_expectedLength()) == (64)))) && ((((((long) ((int) (((input).dtor_expectedLength()) * (8))))) == 0 ? 0 : 1) == 1) && (java.lang.Long.compareUnsigned(((long) ((int) (((input).dtor_expectedLength()) * (8)))), (StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()).longValue()) < 0)), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Kdf in Counter Mode input is invalid.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_ikm;
    _1_ikm = (input).dtor_ikm();
    dafny.DafnySequence<? extends java.lang.Byte> _2_label__;
    _2_label__ = ((input).dtor_purpose()).UnwrapOr(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    dafny.DafnySequence<? extends java.lang.Byte> _3_info;
    _3_info = ((input).dtor_nonce()).UnwrapOr(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    dafny.DafnySequence<? extends java.lang.Byte> _4_okm;
    _4_okm = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    int _5_internalLength;
    _5_internalLength = ((int) ((long) (long) (((long) (long) (((long) 4L) + ((long) (__default.SEPARATION__INDICATOR()).cardinalityInt()))) + ((long) 4L))));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (true) && (java.lang.Long.compareUnsigned(StandardLibrary_mMemoryMath_Compile.__default.Add3((long) java.lang.Integer.toUnsignedLong(_5_internalLength), (long) (_2_label__).cardinalityInt(), (long) (_3_info).cardinalityInt()), (StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()).longValue()) < 0), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Input Length exceeds INT32_MAX_LIMIT")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_6_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_lengthBits;
    _7_lengthBits = StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(((int) (((input).dtor_expectedLength()) * (8))));
    dafny.DafnySequence<? extends java.lang.Byte> _8_explicitInfo;
    _8_explicitInfo = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_2_label__, __default.SEPARATION__INDICATOR()), _3_info), _7_lengthBits);
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (long) (((long) 4L) + ((long) (_8_explicitInfo).cardinalityInt())), (StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()).longValue()) < 0, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("PRF input length exceeds INT32_MAX_LIMIT.")));
    if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_9_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _10_valueOrError3 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = __default.RawDerive(_1_ikm, _8_explicitInfo, (input).dtor_expectedLength(), 0, (input).dtor_digestAlgorithm());
    _10_valueOrError3 = _out0;
    if ((_10_valueOrError3).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_10_valueOrError3).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    _4_okm = (_10_valueOrError3).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _4_okm);
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> RawDerive(dafny.DafnySequence<? extends java.lang.Byte> ikm, dafny.DafnySequence<? extends java.lang.Byte> explicitInfo, int length, int offset, software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm digestAlgorithm)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = HMAC.HMac.Build(digestAlgorithm);
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    HMAC.HMac _1_hmac;
    _1_hmac = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    (_1_hmac).Init(ikm);
    int _2_macLengthBytes;
    _2_macLengthBytes = ((int) (Digest_Compile.__default.Length(digestAlgorithm)));
    int _3_iterations;
    _3_iterations = dafny.DafnyEuclidean.EuclideanDivision((int) (((int) ((length) + (_2_macLengthBytes))) - (1)), _2_macLengthBytes);
    dafny.DafnySequence<? extends java.lang.Byte> _4_buffer;
    _4_buffer = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _5_i;
    _5_i = StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(__default.COUNTER__START__VALUE());
    long _hi0 = StandardLibrary_mMemoryMath_Compile.__default.Add(((long) (_3_iterations)), (long) 1L);
    for (long _6_iteration = (long) 1L; java.lang.Long.compareUnsigned(_6_iteration, _hi0) < 0; _6_iteration++) {
      (_1_hmac).BlockUpdate(_5_i);
      (_1_hmac).BlockUpdate(explicitInfo);
      dafny.DafnySequence<? extends java.lang.Byte> _7_tmp;
      dafny.DafnySequence<? extends java.lang.Byte> _out1;
      _out1 = (_1_hmac).GetResult();
      _7_tmp = _out1;
      _4_buffer = dafny.DafnySequence.<java.lang.Byte>concatenate(_4_buffer, _7_tmp);
      Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _8_valueOrError1 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
      _8_valueOrError1 = __default.Increment(_5_i);
      if ((_8_valueOrError1).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
        output = (_8_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
        return output;
      }
      _5_i = (_8_valueOrError1).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    }
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), java.lang.Long.compareUnsigned((long) (_4_buffer).cardinalityInt(), ((long) (length))) >= 0, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Failed to derive key of requested length")));
    if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_9_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (_4_buffer).take(length));
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Increment(dafny.DafnySequence<? extends java.lang.Byte> x) {
    if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(3))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(0))), ((byte)(java.lang.Object)((x).select(1))), ((byte)(java.lang.Object)((x).select(2))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(3)))) + ((byte) 1)))));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(2))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(0))), ((byte)(java.lang.Object)((x).select(1))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(2)))) + ((byte) 1))), (byte) 0));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(1))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(0))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(1)))) + ((byte) 1))), (byte) 0, (byte) 0));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(0))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of((byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(0)))) + ((byte) 1))), (byte) 0, (byte) 0, (byte) 0));
    } else {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Failure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Unable to derive key material; may have exceeded limit.")));
    }
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> SEPARATION__INDICATOR()
  {
    return dafny.DafnySequence.<java.lang.Byte> of((byte) 0);
  }
  public static int COUNTER__START__VALUE()
  {
    return 1;
  }
  @Override
  public java.lang.String toString() {
    return "KdfCtr._default";
  }
}
