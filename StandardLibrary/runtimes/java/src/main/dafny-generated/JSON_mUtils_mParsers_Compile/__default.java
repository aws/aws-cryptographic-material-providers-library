// Class __default
// Dafny class __default compiled into Java
package JSON_mUtils_mParsers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__T, __R> Parser__<__T, __R> ParserWitness(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R)
  {
    return Parser__.<__T, __R>create(_td___T, _td___R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>>)(_0___v0_boxed0) -> {
  JSON_mUtils_mCursors_Compile.Cursor__ _0___v0 = ((JSON_mUtils_mCursors_Compile.Cursor__)(java.lang.Object)(_0___v0_boxed0));
  return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>create_Failure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<__R>_typeDescriptor(_td___R), JSON_mUtils_mCursors_Compile.CursorError.<__R>create_EOF(_td___R));
}));
  }
  public static <__T, __R> SubParser__<__T, __R> SubParserWitness(dafny.TypeDescriptor<__T> _td___T, dafny.TypeDescriptor<__R> _td___R)
  {
    return SubParser__.<__T, __R>create(_td___T, _td___R, ((java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>>)(_0_cs_boxed0) -> {
  JSON_mUtils_mCursors_Compile.Cursor__ _0_cs = ((JSON_mUtils_mCursors_Compile.Cursor__)(java.lang.Object)(_0_cs_boxed0));
  return Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<__T>, JSON_mUtils_mCursors_Compile.CursorError<__R>>create_Failure(JSON_mUtils_mCursors_Compile.Split.<__T>_typeDescriptor(_td___T), JSON_mUtils_mCursors_Compile.CursorError.<__R>_typeDescriptor(_td___R), JSON_mUtils_mCursors_Compile.CursorError.<__R>create_EOF(_td___R));
}));
  }
  @Override
  public java.lang.String toString() {
    return "JSON.Utils.Parsers._default";
  }
}
