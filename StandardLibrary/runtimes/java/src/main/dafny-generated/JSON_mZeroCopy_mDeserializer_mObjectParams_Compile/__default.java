// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mObjectParams_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Colon(JSON_mUtils_mCursors_Compile.Cursor__ cs) {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = (cs).<JSON_mErrors_Compile.DeserializationError>AssertChar(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), ':');
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), (_1_cs).Split());
    }
  }
  public static JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> KeyValueFromParts(JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring> k, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> colon, JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value> v)
  {
    JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> _0_sp = JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>create(JSON_mGrammar_Compile.jKeyValue._typeDescriptor(), JSON_mGrammar_Compile.jKeyValue.create((k).dtor_t(), (colon).dtor_t(), (v).dtor_t()), (v).dtor_cs());
    return _0_sp;
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ElementSpec(JSON_mGrammar_Compile.jKeyValue t) {
    return JSON_mConcreteSyntax_mSpec_Compile.__default.KeyValue(t);
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Element(JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mUtils_mParsers_Compile.SubParser__<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.DeserializationError> json)
  {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = JSON_mZeroCopy_mDeserializer_mStrings_Compile.__default.String(cs);
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jstring> _1_k = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jstring>_typeDescriptor(JSON_mGrammar_Compile.jstring._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      JSON_mUtils_mParsers_Compile.Parser__<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.DeserializationError> _2_p = JSON_mUtils_mParsers_Compile.Parser__.<JSON_mUtils_mViews_mCore_Compile.View__, JSON_mErrors_Compile.DeserializationError>create(JSON_mGrammar_Compile.jcolon._typeDescriptor(), JSON_mErrors_Compile.DeserializationError._typeDescriptor(), __default::Colon);
      Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _3_valueOrError1 = JSON_mZeroCopy_mDeserializer_mCore_Compile.__default.<JSON_mUtils_mViews_mCore_Compile.View__>Structural(JSON_mGrammar_Compile.jcolon._typeDescriptor(), (_1_k).dtor_cs(), _2_p);
      if ((_3_valueOrError1).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
        return (_3_valueOrError1).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
      } else {
        JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>> _4_colon = (_3_valueOrError1).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Structural<JSON_mUtils_mViews_mCore_Compile.View__>>_typeDescriptor(JSON_mGrammar_Compile.Structural.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mGrammar_Compile.jcolon._typeDescriptor())), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
        Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _5_valueOrError2 = ((Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>)(java.lang.Object)(((json).dtor_fn()).apply((_4_colon).dtor_cs())));
        if ((_5_valueOrError2).IsFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
          return (_5_valueOrError2).<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>>PropagateFailure(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()));
        } else {
          JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value> _6_v = (_5_valueOrError2).Extract(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.Value>_typeDescriptor(JSON_mGrammar_Compile.Value._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
          JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue> _7_kv = __default.KeyValueFromParts(_1_k, _4_colon, _6_v);
          return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.jKeyValue>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mGrammar_Compile.jKeyValue>_typeDescriptor(JSON_mGrammar_Compile.jKeyValue._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), _7_kv);
        }
      }
    }
  }
  public static byte OPEN()
  {
    return ((byte) ('{'));
  }
  public static byte CLOSE()
  {
    return ((byte) ('}'));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.ObjectParams._default";
  }
}
