// Class __default
// Dafny class __default compiled into Java
package KdfCtr_Compile;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;
import Digest_Compile.*;
import HMAC.*;
import WrappedHMAC_Compile.*;
import HKDF_Compile.*;
import WrappedHKDF_Compile.*;
import Signature.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> KdfCounterMode(software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((((java.util.Objects.equals((input).dtor_digestAlgorithm(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__256())) || (java.util.Objects.equals((input).dtor_digestAlgorithm(), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.create_SHA__384()))) && (((java.util.Objects.equals(java.math.BigInteger.valueOf(((input).dtor_ikm()).length()), java.math.BigInteger.valueOf(32L))) || (java.util.Objects.equals(java.math.BigInteger.valueOf(((input).dtor_ikm()).length()), java.math.BigInteger.valueOf(48L)))) || (java.util.Objects.equals(java.math.BigInteger.valueOf(((input).dtor_ikm()).length()), java.math.BigInteger.valueOf(66L))))) && (((input).dtor_nonce()).is_Some())) && ((java.util.Objects.equals(java.math.BigInteger.valueOf((((input).dtor_nonce()).dtor_value()).length()), java.math.BigInteger.valueOf(16L))) || (java.util.Objects.equals(java.math.BigInteger.valueOf((((input).dtor_nonce()).dtor_value()).length()), java.math.BigInteger.valueOf(32L))))) && ((((input).dtor_expectedLength()) == (32)) || (((input).dtor_expectedLength()) == (64)))) && ((((java.math.BigInteger.valueOf((input).dtor_expectedLength())).multiply(java.math.BigInteger.valueOf(8L))).signum() == 1) && (((java.math.BigInteger.valueOf((input).dtor_expectedLength())).multiply(java.math.BigInteger.valueOf(8L))).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0)), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Kdf in Counter Mode input is invalid.")));
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
    _5_internalLength = (((java.math.BigInteger.valueOf(4L)).add(java.math.BigInteger.valueOf((__default.SEPARATION__INDICATOR()).length()))).add(java.math.BigInteger.valueOf(4L))).intValue();
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _6_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _6_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (true) && ((((dafny.Helpers.unsignedToBigInteger(_5_internalLength)).add(java.math.BigInteger.valueOf((_2_label__).length()))).add(java.math.BigInteger.valueOf((_3_info).length()))).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Input Length exceeds INT32_MAX_LIMIT")));
    if ((_6_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_6_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _7_lengthBits;
    _7_lengthBits = StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(((int) (((input).dtor_expectedLength()) * (8))));
    dafny.DafnySequence<? extends java.lang.Byte> _8_explicitInfo;
    _8_explicitInfo = dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(dafny.DafnySequence.<java.lang.Byte>concatenate(_2_label__, __default.SEPARATION__INDICATOR()), _3_info), _7_lengthBits);
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _9_valueOrError2 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _9_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((java.math.BigInteger.valueOf(4L)).add(java.math.BigInteger.valueOf((_8_explicitInfo).length()))).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("PRF input length exceeds INT32_MAX_LIMIT.")));
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
    _2_macLengthBytes = (Digest_Compile.__default.Length(digestAlgorithm)).intValue();
    int _3_iterations;
    _3_iterations = dafny.DafnyEuclidean.EuclideanDivision((int) (((int) ((length) + (_2_macLengthBytes))) - (1)), _2_macLengthBytes);
    dafny.DafnySequence<? extends java.lang.Byte> _4_buffer;
    _4_buffer = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _5_i;
    _5_i = StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(__default.COUNTER__START__VALUE());
    int _hi0 = (int) ((_3_iterations) + (1));
    for (int _6_iteration = 1; _6_iteration < _hi0; _6_iteration++) {
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
    _9_valueOrError2 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (java.math.BigInteger.valueOf((_4_buffer).length())).compareTo(java.math.BigInteger.valueOf(length)) >= 0, software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Failed to derive key of requested length")));
    if ((_9_valueOrError2).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_9_valueOrError2).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (_4_buffer).take(length));
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Increment(dafny.DafnySequence<? extends java.lang.Byte> x) {
    if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L)))))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), ((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(3L))))))) + ((byte) 1)))));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L)))))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), ((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.valueOf(2L))))))) + ((byte) 1))), (byte) 0));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ONE))))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ONE)))))) + ((byte) 1))), (byte) 0, (byte) 0));
    } else if (java.lang.Integer.compareUnsigned(((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))), (byte) 255) < 0) {
      return Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> of((byte) (byte) ((byte)((((byte)(java.lang.Object)((x).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO)))))) + ((byte) 1))), (byte) 0, (byte) 0, (byte) 0));
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
