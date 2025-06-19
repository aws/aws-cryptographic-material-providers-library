// Class View__
// Dafny class View__ compiled into Java
package JSON_mUtils_mViews_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class View__ {
  public dafny.DafnySequence<? extends java.lang.Byte> _s;
  public int _beg;
  public int _end;
  public View__ (dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int end) {
    this._s = s;
    this._beg = beg;
    this._end = end;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    View__ o = (View__)other;
    return true && java.util.Objects.equals(this._s, o._s) && this._beg == o._beg && this._end == o._end;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._s);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._beg);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._end);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder ss = new StringBuilder();
    ss.append("Core.View_.View");
    ss.append("(");
    ss.append(dafny.Helpers.toString(this._s));
    ss.append(", ");
    ss.append(this._beg);
    ss.append(", ");
    ss.append(this._end);
    ss.append(")");
    return ss.toString();
  }
  private static final dafny.TypeDescriptor<View__> _TYPE = dafny.TypeDescriptor.<View__>referenceWithInitializer(View__.class, () -> View__.Default());
  public static dafny.TypeDescriptor<View__> _typeDescriptor() {
    return (dafny.TypeDescriptor<View__>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final View__ theDefault = View__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0);
  public static View__ Default() {
    return theDefault;
  }
  public static View__ create(dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int end) {
    return new View__(s, beg, end);
  }
  public static View__ create_View(dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int end) {
    return create(s, beg, end);
  }
  public boolean is_View() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_s() {
    return this._s;
  }
  public int dtor_beg() {
    return this._beg;
  }
  public int dtor_end() {
    return this._end;
  }
  public int Length() {
    return (int) (((this).dtor_end()) - ((this).dtor_beg()));
  }
  public dafny.DafnySequence<? extends java.lang.Byte> Bytes() {
    return ((this).dtor_s()).subsequence((this).dtor_beg(), (this).dtor_end());
  }
  public static View__ OfBytes(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    return View__.create(bs, 0, (bs).cardinalityInt());
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> OfString(dafny.DafnySequence<? extends Character> s) {
    return dafny.DafnySequence.Create(BoundedInts_Compile.uint8._typeDescriptor(), java.math.BigInteger.valueOf((s).length()), ((java.util.function.Function<dafny.DafnySequence<? extends Character>, java.util.function.Function<java.math.BigInteger, java.lang.Byte>>)(_0_s) -> ((java.util.function.Function<java.math.BigInteger, java.lang.Byte>)(_1_i_boxed0) -> {
      java.math.BigInteger _1_i = ((java.math.BigInteger)(java.lang.Object)(_1_i_boxed0));
      return ((byte) (((char)(java.lang.Object)((_0_s).select(dafny.Helpers.toInt((_1_i)))))));
    })).apply(s));
  }
  public boolean Byte_q(byte c)
  {
    boolean _hresult = false;
    _hresult = (((this).Length()) == (1)) && (((this).At(0)) == (c));
    return _hresult;
  }
  public boolean Char_q(char c) {
    return (this).Byte_q(((byte) (c)));
  }
  public byte At(int idx) {
    return ((byte)(java.lang.Object)(((this).dtor_s()).select((int) (((this).dtor_beg()) + (idx)))));
  }
  public short Peek() {
    if ((this).Empty_q()) {
      return (short) -1;
    } else {
      return (short) java.lang.Byte.toUnsignedInt((this).At(0));
    }
  }
  public void CopyTo(byte[] dest, int start)
  {
    int _hi0 = (this).Length();
    for (int _0_idx = 0; java.lang.Integer.compareUnsigned(_0_idx, _hi0) < 0; _0_idx++) {
      int _index0 = (int) ((start) + (_0_idx));
      (dest)[dafny.Helpers.toInt(_index0)] = ((byte)(java.lang.Object)(((this).dtor_s()).select((int) (((this).dtor_beg()) + (_0_idx)))));
    }
  }
  public static View__ Empty()
  {
    return View__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0);
  }
  public boolean Empty_q()
  {
    return ((this).dtor_beg()) == ((this).dtor_end());
  }
}
