// Class ByteWriter
// Dafny class ByteWriter compiled into Java
package Streams_Compile;

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
  public long WriteByte(byte n)
  {
    long r = 0L;
    if(true) {
      long _out0;
      _out0 = ((this).writer()).WriteElements(dafny.DafnySequence.<java.lang.Byte> of(n));
      r = _out0;
    }
    return r;
  }
  public long WriteBytes(dafny.DafnySequence<? extends java.lang.Byte> s)
  {
    long r = 0L;
    if(true) {
      long _out0;
      _out0 = ((this).writer()).WriteElements(s);
      r = _out0;
    }
    return r;
  }
  public long WriteUInt16(short n)
  {
    long r = 0L;
    if(true) {
      long _out0;
      _out0 = ((this).writer()).WriteElements(StandardLibrary_mUInt_Compile.__default.UInt16ToSeq(n));
      r = _out0;
    }
    return r;
  }
  public long WriteUInt32(int n)
  {
    long r = 0L;
    if(true) {
      long _out0;
      _out0 = ((this).writer()).WriteElements(StandardLibrary_mUInt_Compile.__default.UInt32ToSeq(n));
      r = _out0;
    }
    return r;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> GetDataWritten() {
    return (this).writer().data;
  }
  public long GetSizeWritten() {
    return (long) ((this).writer().data).cardinalityInt();
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
