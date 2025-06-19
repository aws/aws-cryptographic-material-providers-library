// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> StringBody(JSON_mUtils_mCursors_Compile.Cursor__ cs)
  {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> pr = Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>Default(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Cursor.defaultValue());
    boolean _0_escaped;
    _0_escaped = false;
    int _hi0 = (cs).dtor_end();
    for (int _1_point_k = (cs).dtor_point(); java.lang.Integer.compareUnsigned(_1_point_k, _hi0) < 0; _1_point_k++) {
      byte _2_byte;
      _2_byte = ((byte)(java.lang.Object)(((cs).dtor_s()).select(_1_point_k)));
      if (((_2_byte) == (((byte) ('\"')))) && (!(_0_escaped))) {
        pr = Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Cursor__._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Cursor__.create((cs).dtor_s(), (cs).dtor_beg(), _1_point_k, (cs).dtor_end()));
        return pr;
      } else if ((_2_byte) == (((byte) ('\\')))) {
        _0_escaped = !(_0_escaped);
      } else {
        _0_escaped = false;
      }
    }
    pr = Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Failure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>create_EOF(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
    return pr;
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Quote(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = (cs).<JSON_mErrors_Compile.DeserializationError>AssertChar(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), '\"');
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), (_1_cs).Split());
    }
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> String(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = __default.Quote(cs);
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs0 = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      JSON_mUtils_mViews_mCore_Compile.View__ _1_lq = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._t;
      JSON_mUtils_mCursors_Compile.Cursor__ _2_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs0)._cs;
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _3_valueOrError1 = __default.StringBody(_2_cs);
      if ((_3_valueOrError1).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_3_valueOrError1).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()));
      } else {
        JSON_mUtils_mCursors_Compile.Cursor__ _4_contents = (_3_valueOrError1).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs1 = (_4_contents).Split();
        JSON_mUtils_mViews_mCore_Compile.View__ _5_contents = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._t;
        JSON_mUtils_mCursors_Compile.Cursor__ _6_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs1)._cs;
        Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _7_valueOrError2 = __default.Quote(_6_cs);
        if ((_7_valueOrError2).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
          return (_7_valueOrError2).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()));
        } else {
          JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__> _let_tmp_rhs2 = (_7_valueOrError2).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jquote._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
          JSON_mUtils_mViews_mCore_Compile.View__ _8_rq = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._t;
          JSON_mUtils_mCursors_Compile.Cursor__ _9_cs = ((JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>)_let_tmp_rhs2)._cs;
          return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>create(JSON_mGrammar_Compile.jstring._typeDescriptor(), JSON_mGrammar_Compile.jstring.create(_1_lq, _5_contents, _8_rq), _9_cs));
        }
      }
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.Strings._default";
  }
}
