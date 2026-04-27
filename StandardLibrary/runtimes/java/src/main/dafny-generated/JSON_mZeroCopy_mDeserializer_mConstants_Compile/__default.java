// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mConstants_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Constant(JSON_mUtils_mCursors_Compile.Cursor__ cs, dafny.DafnySequence<? extends java.lang.Byte> expected)
  {
    Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Cursor__, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> _0_valueOrError0 = (cs).<JSON_mErrors_Compile.DeserializationError>AssertBytes(JSON_mErrors_Compile.DeserializationError._typeDescriptor(), expected, 0);
    if ((_0_valueOrError0).IsFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()))) {
      return (_0_valueOrError0).<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>>PropagateFailure(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()));
    } else {
      JSON_mUtils_mCursors_Compile.Cursor__ _1_cs = (_0_valueOrError0).Extract(JSON_mUtils_mCursors_Compile.Cursor._typeDescriptor(), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()));
      return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<JSON_mUtils_mViews_mCore_Compile.View__>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>create_Success(JSON_mUtils_mCursors_Compile.Split.<JSON_mUtils_mViews_mCore_Compile.View__>_typeDescriptor(JSON_mUtils_mViews_mCore_Compile.View._typeDescriptor()), JSON_mUtils_mCursors_Compile.CursorError.<JSON_mErrors_Compile.DeserializationError>_typeDescriptor(JSON_mErrors_Compile.DeserializationError._typeDescriptor()), (_1_cs).Split());
    }
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.Constants._default";
  }
}
