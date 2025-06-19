// Class __default
// Dafny class __default compiled into Java
package JSON_mZeroCopy_mDeserializer_mArrayParams_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static dafny.DafnySequence<? extends java.lang.Byte> ElementSpec(JSON_mGrammar_Compile.Value t) {
    return JSON_mConcreteSyntax_mSpec_Compile.__default.Value(t);
  }
  public static Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>> Element(JSON_mUtils_mCursors_Compile.Cursor__ cs, JSON_mUtils_mParsers_Compile.SubParser__<JSON_mGrammar_Compile.Value, JSON_mErrors_Compile.DeserializationError> json)
  {
    return ((Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<JSON_mGrammar_Compile.Value>, JSON_mUtils_mCursors_Compile.CursorError<JSON_mErrors_Compile.DeserializationError>>)(java.lang.Object)(((json).dtor_fn()).apply(cs)));
  }
  public static byte OPEN()
  {
    return ((byte) ('['));
  }
  public static byte CLOSE()
  {
    return ((byte) (']'));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.ZeroCopy.Deserializer.ArrayParams._default";
  }
}
