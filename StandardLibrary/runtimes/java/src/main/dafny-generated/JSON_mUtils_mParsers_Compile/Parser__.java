// Class Parser__<T, R>
// Dafny class Parser__<T, R> compiled into Java
package JSON_mUtils_mParsers_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Parser__<T, R> {
  public java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> _fn;
  protected dafny.TypeDescriptor<T> _td_T;
  protected dafny.TypeDescriptor<R> _td_R;
  public Parser__ (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    this._td_T = _td_T;
    this._td_R = _td_R;
    this._fn = fn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Parser__<T, R> o = (Parser__<T, R>)other;
    return true && java.util.Objects.equals(this._fn, o._fn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._fn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Parsers.Parser_.Parser");
    s.append("(");
    s.append(dafny.Helpers.toString(this._fn));
    s.append(")");
    return s.toString();
  }
  public static <T, R> dafny.TypeDescriptor<Parser__<T, R>> _typeDescriptor(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    return (dafny.TypeDescriptor<Parser__<T, R>>) (dafny.TypeDescriptor<?>) dafny.TypeDescriptor.<Parser__<T, R>>referenceWithInitializer(Parser__.class, () -> Parser__.<T, R>Default(_td_T, _td_R, _td_T.defaultValue()));
  }

  public static <T, R> Parser__<T, R> Default(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T _default_T) {
    return Parser__.<T, R>create(_td_T, _td_R, ((JSON_mUtils_mCursors_Compile.Cursor__ x0) -> Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>Default(JSON_mUtils_mCursors_Compile.Split.<T>_typeDescriptor(_td_T), JSON_mUtils_mCursors_Compile.CursorError.<R>_typeDescriptor(_td_R), JSON_mUtils_mCursors_Compile.Split.<T>Default(_td_T, _default_T))));
  }
  @Deprecated()
  public static <T, R> Parser__<T, R> Default(T _default_T) {
    dafny.TypeDescriptor<T> _td_T = null;
    dafny.TypeDescriptor<R> _td_R = null;
    return Parser__.<T, R>create(_td_T, _td_R, ((JSON_mUtils_mCursors_Compile.Cursor__ x0) -> Wrappers_Compile.Result.<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>Default(JSON_mUtils_mCursors_Compile.Split.<T>_typeDescriptor(_td_T), JSON_mUtils_mCursors_Compile.CursorError.<R>_typeDescriptor(_td_R), JSON_mUtils_mCursors_Compile.Split.<T>Default(_td_T, _default_T))));
  }
  public static <T, R> Parser__<T, R> create(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return new Parser__<T, R>(_td_T, _td_R, fn);
  }
  @Deprecated()
  public static <T, R> Parser__<T, R> create(java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return new Parser__<T, R>(null, null, fn);
  }
  public static <T, R> Parser__<T, R> create_Parser(dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return create(_td_T, _td_R, fn);
  }
  @Deprecated()
  public static <T, R> Parser__<T, R> create_Parser(java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> fn) {
    return create(null, null, fn);
  }
  public boolean is_Parser() { return true; }
  public java.util.function.Function<JSON_mUtils_mCursors_Compile.Cursor__, Wrappers_Compile.Result<JSON_mUtils_mCursors_Compile.Split<T>, JSON_mUtils_mCursors_Compile.CursorError<R>>> dtor_fn() {
    return this._fn;
  }
}
