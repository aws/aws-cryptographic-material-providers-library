// Class __default
// Dafny class __default compiled into Java
package Digest_Compile;

import software.amazon.cryptography.primitives.internaldafny.types.*;
import ExternRandom.*;
import Random_Compile.*;
import AESEncryption.*;
import ExternDigest.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static java.math.BigInteger Length(software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm digestAlgorithm) {
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _source0 = digestAlgorithm;
    if (_source0.is_SHA__512()) {
      return java.math.BigInteger.valueOf(64L);
    } else if (_source0.is_SHA__384()) {
      return java.math.BigInteger.valueOf(48L);
    } else {
      return java.math.BigInteger.valueOf(32L);
    }
  }
  public static Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> Digest(software.amazon.cryptography.primitives.internaldafny.types.DigestInput input)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    software.amazon.cryptography.primitives.internaldafny.types.DigestInput _let_tmp_rhs0 = input;
    software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm _0_digestAlgorithm = ((software.amazon.cryptography.primitives.internaldafny.types.DigestInput)_let_tmp_rhs0)._digestAlgorithm;
    dafny.DafnySequence<? extends java.lang.Byte> _1_message = ((software.amazon.cryptography.primitives.internaldafny.types.DigestInput)_let_tmp_rhs0)._message;
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _2_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error> _out0;
    _out0 = ExternDigest.__default.Digest(_0_digestAlgorithm, _1_message);
    _2_valueOrError0 = _out0;
    if ((_2_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_2_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _3_value;
    _3_value = (_2_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    Wrappers_Compile.Outcome<software.amazon.cryptography.primitives.internaldafny.types.Error> _4_valueOrError1 = Wrappers_Compile.Outcome.<software.amazon.cryptography.primitives.internaldafny.types.Error>Default(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor());
    _4_valueOrError1 = Wrappers_Compile.__default.<software.amazon.cryptography.primitives.internaldafny.types.Error>Need(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), java.util.Objects.equals(java.math.BigInteger.valueOf((_3_value).length()), __default.Length(_0_digestAlgorithm)), software.amazon.cryptography.primitives.internaldafny.types.Error.create_AwsCryptographicPrimitivesError(dafny.DafnySequence.asString("Incorrect length digest from ExternDigest.")));
    if ((_4_valueOrError1).IsFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor())) {
      res = (_4_valueOrError1).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, software.amazon.cryptography.primitives.internaldafny.types.Error>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), software.amazon.cryptography.primitives.internaldafny.types.Error._typeDescriptor(), _3_value);
    return res;
  }
  @Override
  public java.lang.String toString() {
    return "Digest._default";
  }
}
