// Class ByteReader
// Dafny class ByteReader compiled into Java
package Streams_Compile;

import Wrappers_Compile.*;
import Seq_mMergeSort_Compile.*;
import Math_Compile.*;
import Seq_Compile.*;
import BoundedInts_Compile.*;
import Unicode_Compile.*;
import Utf8EncodingForm_Compile.*;
import Utf16EncodingForm_Compile.*;
import UnicodeStrings_Compile.*;
import FileIO_Compile.*;
import MulInternals_Compile.*;
import ModInternals_Compile.*;
import DivInternals_Compile.*;
import Power_Compile.*;
import Logarithm_Compile.*;
import StandardLibraryInterop_Compile.*;
import StandardLibrary_mUInt_Compile.*;
import StandardLibrary_mSequence_Compile.*;
import StandardLibrary_mString_Compile.*;
import StandardLibrary_Compile.*;
import UUID.*;
import UTF8.*;
import OsLang.*;
import Time.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class ByteReader {
  public ByteReader() {
    this._reader = null;
  }
  public void __ctor(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    SeqReader<java.lang.Byte> _0_mr;
    SeqReader<java.lang.Byte> _nw0 = new SeqReader<java.lang.Byte>(BoundedInts_Compile.uint8._typeDescriptor());
    _nw0.__ctor(s);
    _0_mr = _nw0;
    (this)._reader = _0_mr;
  }
  public Wrappers_Compile.Result<java.lang.Byte, dafny.DafnySequence<? extends Character>> ReadByte()
  {
    Wrappers_Compile.Result<java.lang.Byte, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<java.lang.Byte, dafny.DafnySequence<? extends Character>>Default(BoundedInts_Compile.uint8._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (byte) 0);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = ((this).reader()).ReadExact(java.math.BigInteger.ONE);
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      res = (_0_valueOrError0).<java.lang.Byte>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.uint8._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytes;
    _1_bytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    res = Wrappers_Compile.Result.<java.lang.Byte, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.uint8._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), ((byte)(java.lang.Object)((_1_bytes).select(dafny.Helpers.toInt((java.math.BigInteger.ZERO))))));
    return res;
  }
  public Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> ReadBytes(java.math.BigInteger n)
  {
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = ((this).reader()).ReadExact(n);
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      res = (_0_valueOrError0).<dafny.DafnySequence<? extends java.lang.Byte>>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()));
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytes;
    _1_bytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    res = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>create_Success(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _1_bytes);
    return res;
  }
  public Wrappers_Compile.Result<java.lang.Short, dafny.DafnySequence<? extends Character>> ReadUInt16()
  {
    Wrappers_Compile.Result<java.lang.Short, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<java.lang.Short, dafny.DafnySequence<? extends Character>>Default(BoundedInts_Compile.uint16._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), (short) 0);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = ((this).reader()).ReadExact(java.math.BigInteger.valueOf(2L));
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      res = (_0_valueOrError0).<java.lang.Short>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.uint16._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytes;
    _1_bytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    short _2_n;
    _2_n = StandardLibrary_mUInt_Compile.__default.SeqToUInt16(_1_bytes);
    res = Wrappers_Compile.Result.<java.lang.Short, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.uint16._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_n);
    return res;
  }
  public Wrappers_Compile.Result<java.lang.Integer, dafny.DafnySequence<? extends Character>> ReadUInt32()
  {
    Wrappers_Compile.Result<java.lang.Integer, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<java.lang.Integer, dafny.DafnySequence<? extends Character>>Default(BoundedInts_Compile.uint32._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), 0);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = ((this).reader()).ReadExact(java.math.BigInteger.valueOf(4L));
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      res = (_0_valueOrError0).<java.lang.Integer>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.uint32._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytes;
    _1_bytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    int _2_n;
    _2_n = StandardLibrary_mUInt_Compile.__default.SeqToUInt32(_1_bytes);
    res = Wrappers_Compile.Result.<java.lang.Integer, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.uint32._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_n);
    return res;
  }
  public Wrappers_Compile.Result<java.lang.Long, dafny.DafnySequence<? extends Character>> ReadUInt64()
  {
    Wrappers_Compile.Result<java.lang.Long, dafny.DafnySequence<? extends Character>> res = Wrappers_Compile.Result.<java.lang.Long, dafny.DafnySequence<? extends Character>>Default(BoundedInts_Compile.uint64._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), 0L);
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _0_valueOrError0 = Wrappers_Compile.Result.<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
    Wrappers_Compile.Result<dafny.DafnySequence<? extends java.lang.Byte>, dafny.DafnySequence<? extends Character>> _out0;
    _out0 = ((this).reader()).ReadExact(java.math.BigInteger.valueOf(8L));
    _0_valueOrError0 = _out0;
    if ((_0_valueOrError0).IsFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))) {
      res = (_0_valueOrError0).<java.lang.Long>PropagateFailure(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), BoundedInts_Compile.uint64._typeDescriptor());
      return res;
    }
    dafny.DafnySequence<? extends java.lang.Byte> _1_bytes;
    _1_bytes = (_0_valueOrError0).Extract(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR));
    long _2_n;
    _2_n = StandardLibrary_mUInt_Compile.__default.SeqToUInt64(_1_bytes);
    res = Wrappers_Compile.Result.<java.lang.Long, dafny.DafnySequence<? extends Character>>create_Success(BoundedInts_Compile.uint64._typeDescriptor(), dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR), _2_n);
    return res;
  }
  public boolean IsDoneReading()
  {
    boolean b = false;
    b = java.util.Objects.equals(java.math.BigInteger.valueOf((((this).reader()).data()).length()), (this).reader().pos);
    return b;
  }
  public java.math.BigInteger GetSizeRead()
  {
    java.math.BigInteger n = java.math.BigInteger.ZERO;
    n = (this).reader().pos;
    return n;
  }
  public SeqReader<java.lang.Byte> _reader;
  public SeqReader<java.lang.Byte> reader()
  {
    return this._reader;
  }
  private static final dafny.TypeDescriptor<ByteReader> _TYPE = dafny.TypeDescriptor.<ByteReader>referenceWithInitializer(ByteReader.class, () -> (ByteReader) null);
  public static dafny.TypeDescriptor<ByteReader> _typeDescriptor() {
    return (dafny.TypeDescriptor<ByteReader>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "Streams.ByteReader";
  }
}
