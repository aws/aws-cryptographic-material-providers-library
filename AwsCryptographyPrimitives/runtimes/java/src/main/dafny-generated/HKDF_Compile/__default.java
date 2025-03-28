// Class __default
// Dafny class __default compiled into Java
package HKDF_Compile;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;
import Digest_Compile.*;
import HMAC.*;
import WrappedHMAC_Compile.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Extract(HMAC.HMac hmac, dafny.DafnySequence<? extends java.lang.Byte> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm)
  {
    dafny.DafnySequence<? extends java.lang.Byte> prk = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    (hmac).Init(salt);
    (hmac).BlockUpdate(ikm);
    dafny.DafnySequence<? extends java.lang.Byte> _out0;
    _out0 = (hmac).GetResult();
    prk = _out0;
    prk = prk;
    return prk;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Expand(HMAC.HMac hmac, dafny.DafnySequence<? extends java.lang.Byte> prk, dafny.DafnySequence<? extends java.lang.Byte> info, java.math.BigInteger expectedLength, software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm digest)
  {
    dafny.DafnySequence<? extends java.lang.Byte> okm = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    if(true) {
      java.math.BigInteger _0_hashLength = java.math.BigInteger.ZERO;
      _0_hashLength = Digest_Compile.__default.Length(digest);
      java.math.BigInteger _1_n = java.math.BigInteger.ZERO;
      _1_n = dafny.DafnyEuclidean.EuclideanDivision(((_0_hashLength).add(expectedLength)).subtract(java.math.BigInteger.ONE), _0_hashLength);
      (hmac).Init(prk);
      dafny.DafnySequence<? extends java.lang.Byte> _2_t__prev;
      _2_t__prev = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
      dafny.DafnySequence<? extends java.lang.Byte> _3_t__n;
      _3_t__n = _2_t__prev;
      java.math.BigInteger _4_i = java.math.BigInteger.ZERO;
      _4_i = java.math.BigInteger.ONE;
      while ((_4_i).compareTo(_1_n) <= 0) {
        (hmac).BlockUpdate(_2_t__prev);
        (hmac).BlockUpdate(info);
        (hmac).BlockUpdate(dafny.DafnySequence.<java.lang.Byte> of((_4_i).byteValue()));
        dafny.DafnySequence<? extends java.lang.Byte> _out0;
        _out0 = (hmac).GetResult();
        _2_t__prev = _out0;
        _3_t__n = dafny.DafnySequence.<java.lang.Byte>concatenate(_3_t__n, _2_t__prev);
        _4_i = (_4_i).add(java.math.BigInteger.ONE);
      }
      okm = _3_t__n;
      if ((expectedLength).compareTo(java.math.BigInteger.valueOf((okm).length())) < 0) {
        okm = (okm).take(expectedLength);
      }
    }
    return okm;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> Hkdf(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm digest, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm, dafny.DafnySequence<? extends java.lang.Byte> info, java.math.BigInteger L)
  {
    dafny.DafnySequence<? extends java.lang.Byte> okm = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    if(true) {
      if ((L).signum() == 0) {
        okm = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
        return okm;
      }
      Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _0_valueOrError0 = (Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error>)null;
      Wrappers_Compile.Result<HMAC.HMac, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
      _out0 = HMAC.HMac.Build(digest);
      _0_valueOrError0 = _out0;
      if (!(!((_0_valueOrError0).IsFailure(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())))) {
        throw new dafny.DafnyHaltException("src/HKDF/HKDF.dfy(222,16): " + java.lang.String.valueOf(_0_valueOrError0));
      }
      HMAC.HMac _1_hmac;
      _1_hmac = (_0_valueOrError0).Extract(((dafny.TypeDescriptor<HMAC.HMac>)(java.lang.Object)dafny.TypeDescriptor.reference(HMAC.HMac.class)), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
      java.math.BigInteger _2_hashLength = java.math.BigInteger.ZERO;
      _2_hashLength = Digest_Compile.__default.Length(digest);
      dafny.DafnySequence<? extends java.lang.Byte> _3_nonEmptySalt = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
      Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _source0 = salt;
      if (_source0.is_None()) {
        _3_nonEmptySalt = StandardLibrary_Compile.__default.<java.lang.Byte>Fill(BoundedInts_Compile.uint8._typeDescriptor(), (byte) 0, _2_hashLength);
      } else {
        dafny.DafnySequence<? extends java.lang.Byte> _4___mcc_h0 = ((Wrappers_Compile.Option_Some<dafny.DafnySequence<? extends java.lang.Byte>>)_source0)._value;
        dafny.DafnySequence<? extends java.lang.Byte> _5_s = _4___mcc_h0;
        _3_nonEmptySalt = _5_s;
      }
      dafny.DafnySequence<? extends java.lang.Byte> _6_prk;
      dafny.DafnySequence<? extends java.lang.Byte> _out1;
      _out1 = __default.Extract(_1_hmac, _3_nonEmptySalt, ikm);
      _6_prk = _out1;
      dafny.DafnySequence<? extends java.lang.Byte> _out2;
      _out2 = __default.Expand(_1_hmac, _6_prk, info, L, digest);
      okm = _out2;
    }
    return okm;
  }
  @Override
  public java.lang.String toString() {
    return "HKDF._default";
  }
}
