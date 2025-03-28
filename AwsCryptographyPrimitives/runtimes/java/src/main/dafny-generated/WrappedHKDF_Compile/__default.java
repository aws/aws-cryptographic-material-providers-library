// Class __default
// Dafny class __default compiled into Java
package WrappedHKDF_Compile;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;
import Digest_Compile.*;
import HMAC.*;
import WrappedHMAC_Compile.*;
import HKDF_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Extract(software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((input).dtor_salt()).is_None()) || ((java.math.BigInteger.valueOf((((input).dtor_salt()).dtor_value()).length())).signum() != 0)) && ((java.math.BigInteger.valueOf(((input).dtor_ikm()).length())).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("HKDF Extract needs a salt and reasonable ikm.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _1_digestAlgorithm = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput)_let_tmp_rhs0)._digestAlgorithm;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _2_salt = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput)_let_tmp_rhs0)._salt;
    dafny.DafnySequence<? extends java.lang.Byte> _3_ikm = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExtractInput)_let_tmp_rhs0)._ikm;
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _4_valueOrError1 = (Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = HMAC.HMac.Build(_1_digestAlgorithm);
    _4_valueOrError1 = _out0;
    if ((_4_valueOrError1).IsFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_4_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    HMAC.HMac _5_hmac;
    _5_hmac = (_4_valueOrError1).Extract(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _6_prk;
    dafny.DafnySequence<? extends java.lang.Byte> _out1;
    _out1 = HKDF_Compile.__default.Extract(_5_hmac, (_2_salt).UnwrapOr(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), StandardLibrary_Compile.__default.<java.lang.Byte>Fill(BoundedInts_Compile.uint8._typeDescriptor(), (byte) 0, Digest_Compile.__default.Length(_1_digestAlgorithm))), _3_ikm);
    _6_prk = _out1;
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _6_prk);
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Expand(software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), ((((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((input).dtor_expectedLength())) <= 0) && ((java.math.BigInteger.valueOf((input).dtor_expectedLength())).compareTo((java.math.BigInteger.valueOf(255L)).multiply(Digest_Compile.__default.Length((input).dtor_digestAlgorithm()))) <= 0)) && ((java.math.BigInteger.valueOf(((input).dtor_info()).length())).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0)) && (java.util.Objects.equals(Digest_Compile.__default.Length((input).dtor_digestAlgorithm()), java.math.BigInteger.valueOf(((input).dtor_prk()).length()))), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("HKDF Expand needs valid input.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _1_digestAlgorithm = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput)_let_tmp_rhs0)._digestAlgorithm;
    dafny.DafnySequence<? extends java.lang.Byte> _2_prk = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput)_let_tmp_rhs0)._prk;
    dafny.DafnySequence<? extends java.lang.Byte> _3_info = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput)_let_tmp_rhs0)._info;
    int _4_expectedLength = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfExpandInput)_let_tmp_rhs0)._expectedLength;
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _5_valueOrError1 = (Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
    Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = HMAC.HMac.Build(_1_digestAlgorithm);
    _5_valueOrError1 = _out0;
    if ((_5_valueOrError1).IsFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_5_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    HMAC.HMac _6_hmac;
    _6_hmac = (_5_valueOrError1).Extract(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    dafny.DafnySequence<? extends java.lang.Byte> _7_omk;
    dafny.DafnySequence<? extends java.lang.Byte> _out1;
    _out1 = HKDF_Compile.__default.Expand(_6_hmac, _2_prk, _3_info, java.math.BigInteger.valueOf(_4_expectedLength), _1_digestAlgorithm);
    _7_omk = _out1;
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _7_omk);
    return output;
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Hkdf(software.amazon.cryptography.primitives.internaldafny.types.HkdfInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _0_valueOrError0 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), (((((java.math.BigInteger.ONE).compareTo(java.math.BigInteger.valueOf((input).dtor_expectedLength())) <= 0) && ((java.math.BigInteger.valueOf((input).dtor_expectedLength())).compareTo((java.math.BigInteger.valueOf(255L)).multiply(Digest_Compile.__default.Length((input).dtor_digestAlgorithm()))) <= 0)) && ((((input).dtor_salt()).is_None()) || ((java.math.BigInteger.valueOf((((input).dtor_salt()).dtor_value()).length())).signum() != 0))) && ((java.math.BigInteger.valueOf(((input).dtor_info()).length())).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0)) && ((java.math.BigInteger.valueOf(((input).dtor_ikm()).length())).compareTo(StandardLibrary_mUInt_Compile.__default.INT32__MAX__LIMIT()) < 0), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Wrapped Hkdf input is invalid.")));
    if ((_0_valueOrError0).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      output = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return output;
    }
    software.amazon.cryptography.primitives.internaldafny.types.HkdfInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _1_digest = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfInput)_let_tmp_rhs0)._digestAlgorithm;
    Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _2_salt = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfInput)_let_tmp_rhs0)._salt;
    dafny.DafnySequence<? extends java.lang.Byte> _3_ikm = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfInput)_let_tmp_rhs0)._ikm;
    dafny.DafnySequence<? extends java.lang.Byte> _4_info = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfInput)_let_tmp_rhs0)._info;
    int _5_expectedLength = ((software.amazon.cryptography.primitives.internaldafny.types.HkdfInput)_let_tmp_rhs0)._expectedLength;
    dafny.DafnySequence<? extends java.lang.Byte> _6_okm;
    dafny.DafnySequence<? extends java.lang.Byte> _out0;
    _out0 = HKDF_Compile.__default.Hkdf(_1_digest, _2_salt, _3_ikm, _4_info, java.math.BigInteger.valueOf(_5_expectedLength));
    _6_okm = _out0;
    output = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _6_okm);
    return output;
  }
  @Override
  public java.lang.String toString() {
    return "WrappedHKDF._default";
  }
}
