// Class Cursor__
// Dafny class Cursor__ compiled into Java
package JSON_mUtils_mCursors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Cursor__ {
  public dafny.DafnySequence<? extends java.lang.Byte> _s;
  public int _beg;
  public int _point;
  public int _end;
  public Cursor__ (dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int point, int end) {
    this._s = s;
    this._beg = beg;
    this._point = point;
    this._end = end;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Cursor__ o = (Cursor__)other;
    return true && java.util.Objects.equals(this._s, o._s) && this._beg == o._beg && this._point == o._point && this._end == o._end;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._s);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._beg);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._point);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._end);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder ss = new StringBuilder();
    ss.append("Cursors.Cursor_.Cursor");
    ss.append("(");
    ss.append(dafny.Helpers.toString(this._s));
    ss.append(", ");
    ss.append(this._beg);
    ss.append(", ");
    ss.append(this._point);
    ss.append(", ");
    ss.append(this._end);
    ss.append(")");
    return ss.toString();
  }
  private static final dafny.TypeDescriptor<Cursor__> _TYPE = dafny.TypeDescriptor.<Cursor__>referenceWithInitializer(Cursor__.class, () -> Cursor__.Default());
  public static dafny.TypeDescriptor<Cursor__> _typeDescriptor() {
    return (dafny.TypeDescriptor<Cursor__>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Cursor__ theDefault = Cursor__.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, 0, 0);
  public static Cursor__ Default() {
    return theDefault;
  }
  public static Cursor__ create(dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int point, int end) {
    return new Cursor__(s, beg, point, end);
  }
  public static Cursor__ create_Cursor(dafny.DafnySequence<? extends java.lang.Byte> s, int beg, int point, int end) {
    return create(s, beg, point, end);
  }
  public boolean is_Cursor() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_s() {
    return this._s;
  }
  public int dtor_beg() {
    return this._beg;
  }
  public int dtor_point() {
    return this._point;
  }
  public int dtor_end() {
    return this._end;
  }
  public static Cursor__ OfView(JSON_mUtils_mViews_mCore_Compile.View__ v) {
    return Cursor__.create((v).dtor_s(), (v).dtor_beg(), (v).dtor_beg(), (v).dtor_end());
  }
  public static Cursor__ OfBytes(dafny.DafnySequence<? extends java.lang.Byte> bs) {
    return Cursor__.create(bs, 0, 0, (bs).cardinalityInt());
  }
  public dafny.DafnySequence<? extends java.lang.Byte> Bytes() {
    return ((this).dtor_s()).subsequence((this).dtor_beg(), (this).dtor_end());
  }
  public JSON_mUtils_mViews_mCore_Compile.View__ Prefix() {
    return JSON_mUtils_mViews_mCore_Compile.View__.create((this).dtor_s(), (this).dtor_beg(), (this).dtor_point());
  }
  public Cursor__ Suffix() {
    Cursor__ _0_dt__update__tmp_h0 = this;
    int _1_dt__update_hbeg_h0 = (this).dtor_point();
    return Cursor__.create((_0_dt__update__tmp_h0).dtor_s(), _1_dt__update_hbeg_h0, (_0_dt__update__tmp_h0).dtor_point(), (_0_dt__update__tmp_h0).dtor_end());
  }
  public Split<JSON_mUtils_mViews_mCore_Compile.View__> Split() {
    return Split.<JSON_mUtils_mViews_mCore_Compile.View__>create(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), (this).Prefix(), (this).Suffix());
  }
  public int PrefixLength() {
    return (int) (((this).dtor_point()) - ((this).dtor_beg()));
  }
  public int SuffixLength() {
    return (int) (((this).dtor_end()) - ((this).dtor_point()));
  }
  public int Length() {
    return (int) (((this).dtor_end()) - ((this).dtor_beg()));
  }
  public byte At(int idx) {
    return ((byte)(java.lang.Object)(((this).dtor_s()).select((int) (((this).dtor_beg()) + (idx)))));
  }
  public byte SuffixAt(int idx) {
    return ((byte)(java.lang.Object)(((this).dtor_s()).select((int) (((this).dtor_point()) + (idx)))));
  }
  public short Peek() {
    if ((this).EOF_q()) {
      return (short) -1;
    } else {
      return (short) java.lang.Byte.toUnsignedInt((this).SuffixAt(0));
    }
  }
  public boolean LookingAt(char c) {
    return ((this).Peek()) == (((short) (c)));
  }
  public Cursor__ Skip(int n) {
    Cursor__ _0_dt__update__tmp_h0 = this;
    int _1_dt__update_hpoint_h0 = (int) (((this).dtor_point()) + (n));
    return Cursor__.create((_0_dt__update__tmp_h0).dtor_s(), (_0_dt__update__tmp_h0).dtor_beg(), _1_dt__update_hpoint_h0, (_0_dt__update__tmp_h0).dtor_end());
  }
  public Cursor__ Unskip(int n) {
    Cursor__ _0_dt__update__tmp_h0 = this;
    int _1_dt__update_hpoint_h0 = (int) (((this).dtor_point()) - (n));
    return Cursor__.create((_0_dt__update__tmp_h0).dtor_s(), (_0_dt__update__tmp_h0).dtor_beg(), _1_dt__update_hpoint_h0, (_0_dt__update__tmp_h0).dtor_end());
  }
  public <__R> Wrappers_Compile.Result<Cursor__, CursorError<__R>> Get(dafny.TypeDescriptor<__R> _td___R, __R err)
  {
    if ((this).EOF_q()) {
      return Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Failure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), CursorError.<__R>create_OtherError(_td___R, err));
    } else {
      return Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Success(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), (this).Skip(1));
    }
  }
  public <__R> Wrappers_Compile.Result<Cursor__, CursorError<__R>> AssertByte(dafny.TypeDescriptor<__R> _td___R, byte b)
  {
    short _0_nxt = (this).Peek();
    if ((_0_nxt) == ((short) java.lang.Byte.toUnsignedInt(b))) {
      return Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Success(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), (this).Skip(1));
    } else {
      return Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Failure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), CursorError.<__R>create_ExpectingByte(_td___R, b, _0_nxt));
    }
  }
  public <__R> Wrappers_Compile.Result<Cursor__, CursorError<__R>> AssertBytes(dafny.TypeDescriptor<__R> _td___R, dafny.DafnySequence<? extends java.lang.Byte> bs, int offset)
  {
    Cursor__ _this = this;
    TAIL_CALL_START: while (true) {
      if ((offset) == ((bs).cardinalityInt())) {
        return Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Success(Cursor__._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), _this);
      } else {
        Wrappers_Compile.Result<Cursor__, CursorError<__R>> _0_valueOrError0 = (_this).<__R>AssertByte(_td___R, ((byte)(java.lang.Object)((bs).select(offset))));
        if ((_0_valueOrError0).IsFailure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R))) {
          return (_0_valueOrError0).<Cursor__>PropagateFailure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), Cursor__._typeDescriptor());
        } else {
          Cursor__ _1_ps = (_0_valueOrError0).Extract(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R));
          Cursor__ _in0 = _1_ps;
          dafny.DafnySequence<? extends java.lang.Byte> _in1 = bs;
          int _in2 = (int) ((offset) + (1));
          _this = _in0;
          ;
          bs = _in1;
          offset = _in2;
          continue TAIL_CALL_START;
        }
      }
    }
  }
  public <__R> Wrappers_Compile.Result<Cursor__, CursorError<__R>> AssertChar(dafny.TypeDescriptor<__R> _td___R, char c0)
  {
    return (this).<__R>AssertByte(_td___R, ((byte) (c0)));
  }
  public Cursor__ SkipByte() {
    if ((this).EOF_q()) {
      return this;
    } else {
      return (this).Skip(1);
    }
  }
  public Cursor__ SkipIf(java.util.function.Function<java.lang.Byte, Boolean> p) {
    if (((this).EOF_q()) || (!(((boolean)(java.lang.Object)((p).apply((this).SuffixAt(0))))))) {
      return this;
    } else {
      return (this).Skip(1);
    }
  }
  public Cursor__ SkipWhile(java.util.function.Function<java.lang.Byte, Boolean> p)
  {
    Cursor__ ps = Cursor.defaultValue();
    int _0_point_k;
    _0_point_k = (this).dtor_point();
    int _1_end;
    _1_end = (this).dtor_end();
    while ((java.lang.Integer.compareUnsigned(_0_point_k, _1_end) < 0) && (((boolean)(java.lang.Object)((p).apply(((byte)(java.lang.Object)(((this).dtor_s()).select(_0_point_k)))))))) {
      _0_point_k = (int) ((_0_point_k) + (1));
    }
    ps = Cursor__.create((this).dtor_s(), (this).dtor_beg(), _0_point_k, (this).dtor_end());
    return ps;
  }
  public <__A, __R> Wrappers_Compile.Result<Cursor__, CursorError<__R>> SkipWhileLexer(dafny.TypeDescriptor<__A> _td___A, dafny.TypeDescriptor<__R> _td___R, dafny.Function2<__A, java.lang.Short, JSON_mUtils_mLexers_mCore_Compile.LexerResult<__A, __R>> step, __A st)
  {
    Wrappers_Compile.Result<Cursor__, CursorError<__R>> pr = Wrappers_Compile.Result.<Cursor__, CursorError<__R>>Default(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), Cursor.defaultValue());
    if(true) {
      int _0_point_k;
      _0_point_k = (this).dtor_point();
      int _1_end;
      _1_end = (this).dtor_end();
      @SuppressWarnings({"unchecked", "deprecation"})
      __A _2_st_k;
      _2_st_k = st;
      while (true) {
        boolean _3_eof;
        _3_eof = (_0_point_k) == (_1_end);
        short _4_minusone;
        _4_minusone = (short) -1;
        short _5_c;
        if (_3_eof) {
          _5_c = _4_minusone;
        } else {
          _5_c = (short) java.lang.Byte.toUnsignedInt(((byte)(java.lang.Object)(((this).dtor_s()).select(_0_point_k))));
        }
        JSON_mUtils_mLexers_mCore_Compile.LexerResult<__A, __R> _source0 = ((JSON_mUtils_mLexers_mCore_Compile.LexerResult<__A, __R>)(java.lang.Object)((step).apply(_2_st_k, _5_c)));
        if (_source0.is_Accept()) {
          pr = Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Success(Cursor__._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), Cursor__.create((this).dtor_s(), (this).dtor_beg(), _0_point_k, (this).dtor_end()));
          return pr;
        } else if (_source0.is_Reject()) {
          __R _6___mcc_h0 = ((JSON_mUtils_mLexers_mCore_Compile.LexerResult_Reject<__A, __R>)_source0)._err;
          __R _7_err = _6___mcc_h0;
          pr = Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Failure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), CursorError.<__R>create_OtherError(_td___R, _7_err));
          return pr;
        } else {
          __A _8___mcc_h1 = ((JSON_mUtils_mLexers_mCore_Compile.LexerResult_Partial<__A, __R>)_source0)._st;
          __A _9_st_k_k = _8___mcc_h1;
          if (_3_eof) {
            pr = Wrappers_Compile.Result.<Cursor__, CursorError<__R>>create_Failure(Cursor._typeDescriptor(), CursorError.<__R>_typeDescriptor(_td___R), CursorError.<__R>create_EOF(_td___R));
            return pr;
          } else {
            _2_st_k = _9_st_k_k;
            _0_point_k = (int) ((_0_point_k) + (1));
          }
        }
      }
    }
    return pr;
  }
  public boolean BOF_q()
  {
    return ((this).dtor_point()) == ((this).dtor_beg());
  }
  public boolean EOF_q()
  {
    return ((this).dtor_point()) == ((this).dtor_end());
  }
}
