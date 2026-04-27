// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Get(JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mErrors_Compile.DeserializationError err)
  {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = (cs).<JSON_mErrors_Compile.DeserializationError>Get(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), err);
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), (_1_cs).Split());
    }
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> WS(JSON_mUtils_mCursors_Compile.Cursor__ cs)
  {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> sp = JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>Default(JSON_mGrammar_Compile.jblanks._typeDescriptor(), JSON_mGrammar_Compile.jblanks.defaultValue());
    int _0_point_k;
    _0_point_k = (cs).dtor_point();
    int _1_end;
    _1_end = (cs).dtor_end();
    while ((java.lang.Integer.compareUnsigned(_0_point_k, _1_end) < 0) && (JSON_mGrammar_Compile.__default.Blank_q(((byte)(java.lang.Object)(((cs).dtor_s()).select(_0_point_k)))))) {
      _0_point_k = (int) ((_0_point_k) + (1));
    }
    sp = (JSON_mUtils_mCursors_Compile.Cursor__.create((cs).dtor_s(), (cs).dtor_beg(), _0_point_k, (cs).dtor_end())).Split();
    return sp;
  }
  public static <__T> Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<__T>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Structural(dafny.TypeDescriptor<__T> _td___T, JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mUtils_mParsers_Compile.Parser__<__T, JSON_mErrors_Compile.DeserializationError> parser)
  {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs0 = __default.WS(cs);
    JSON_mUtils_mViews_mCore_Compile.View__ _0_before = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._cs;
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _2_valueOrError0 = ((Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>)(java.lang.Object)(((parser).dtor_fn()).apply(_1_cs)));
    if ((_2_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_2_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<__T>>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<__T>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<__T>_typeDescriptor(_td___T)));
    } else {
      JSON_mUtils_mCursors_Compile.Split<__T> _let_tmp_rhs1 = (_2_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      __T _3_val = ((JSON_mUtils_mCursors_Compile.Split<__T>)_let_tmp_rhs1)._t;
      JSON_mUtils_mCursors_Compile.Cursor__ _4_cs = ((JSON_mUtils_mCursors_Compile.Split<__T>)_let_tmp_rhs1)._cs;
      JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs2 = __default.WS(_4_cs);
      JSON_mUtils_mViews_mCore_Compile.View__ _5_after = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._t;
      JSON_mUtils_mCursors_Compile.Cursor__ _6_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._cs;
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<__T>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<__T>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<__T>_typeDescriptor(_td___T)), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<__T>>create(JSON_mGrammar_Compile.Structural.<__T>_typeDescriptor(_td___T), JSON_mGrammar_Compile.Structural.<__T>create(_td___T, _0_before, _3_val, _5_after), _6_cs));
    }
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> TryStructural(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs0 = __default.WS(cs);
    JSON_mUtils_mViews_mCore_Compile.View__ _0_before = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._cs;
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs1 = ((_1_cs).SkipByte()).Split();
    JSON_mUtils_mViews_mCore_Compile.View__ _2_val = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _3_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._cs;
    JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs2 = __default.WS(_3_cs);
    JSON_mUtils_mViews_mCore_Compile.View__ _4_after = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._t;
    JSON_mUtils_mCursors_Compile.Cursor__ _5_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._cs;
    return JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>create(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>create(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor(), _0_before, _2_val, _4_after), _5_cs);
  }
  public static java.util.function.Function<JSON_mUtils_mViews_mCore_Compile.View__, dafny.DafnySequence<? extends java.lang.Byte>> SpecView()
  {
    return ((java.util.function.Function<JSON_mUtils_mViews_mCore_Compile.View__, dafny.DafnySequence<? extends java.lang.Byte>>)(_0_v_boxed0) -> {
      JSON_mUtils_mViews_mCore_Compile.View__ _0_v = ((JSON_mUtils_mViews_mCore_Compile.View__)(java.lang.Object)(_0_v_boxed0));
      return JSON_mConcreteSyntax_mSpec_Compile.__default.View(_0_v);
    });
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.Core._default";
  }
}
