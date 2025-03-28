// Class ByteWriter
// Dafny class ByteWriter compiled into Java
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
public class ByteWriter {
  public ByteWriter() {
    this._writer = null;
  }
  public void __ctor()
  {
    SeqWriter<java.lang.Byte> _0_mw;
    SeqWriter<java.lang.Byte> _nw0 = new SeqWriter<java.lang.Byte>(BoundedInts_Compile.uint8._typeDescriptor());
    _nw0.__ctor();
    _0_mw = _nw0;
    (this)._writer = _0_mw;
  }
  public java.math.BigInteger WriteByte(byte n)
  {
    java.math.BigInteger r = java.math.BigInteger.ZERO;
    if(true) {
      java.math.BigInteger _out0 = java.math.BigInteger.ZERO;
      _out0 = ((this).writer()).WriteElements(dafny.DafnySequence.<java.lang.Byte> of(n));
      r = _out0;
    }
    return r;
  }
  public java.math.BigInteger WriteBytes(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    java.math.BigInteger r = java.math.BigInteger.ZERO;
    if(true) {
      java.math.BigInteger _out0 = java.math.BigInteger.ZERO;
      _out0 = ((this).writer()).WriteElements(s);
      r = _out0;
    }
    return r;
  }
  public java.math.BigInteger WriteUInt16(short n)
  {
    java.math.BigInteger r = java.math.BigInteger.ZERO;
    if(true) {
      java.math.BigInteger _out0 = java.math.BigInteger.ZERO;
      _out0 = ((this).writer()).WriteElements(StandardLibrary_mUInt_Compile.__default.UInt16ToSeq(n));
      r = _out0;
    }
    return r;
  }
  public java.math.BigInteger WriteUInt32(int n)
  {
    java.math.BigInteger r = java.math.BigInteger.ZERO;
    if(true) {
      java.math.BigInteger _out0 = java.math.BigInteger.ZERO;
      _out0 = ((this).writer()).WriteElements(StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(n));
      r = _out0;
    }
    return r;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> GetDataWritten() {
    return (this).writer().data;
  }
  public java.math.BigInteger GetSizeWritten() {
    return java.math.BigInteger.valueOf(((this).writer().data).length());
  }
  public SeqWriter<java.lang.Byte> _writer;
  public SeqWriter<java.lang.Byte> writer()
  {
    return this._writer;
  }
  private static final dafny.TypeDescriptor<ByteWriter> _TYPE = dafny.TypeDescriptor.<ByteWriter>referenceWithInitializer(ByteWriter.class, () -> (ByteWriter) null);
  public static dafny.TypeDescriptor<ByteWriter> _typeDescriptor() {
    return (dafny.TypeDescriptor<ByteWriter>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "Streams.ByteWriter";
  }
}
