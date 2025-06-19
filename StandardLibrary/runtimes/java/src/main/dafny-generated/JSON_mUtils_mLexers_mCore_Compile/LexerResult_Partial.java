// Class LexerResult_Partial<T, R>
// Dafny class LexerResult_Partial<T, R> compiled into Java
package JSON_mUtils_mLexers_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class LexerResult_Partial<T, R> extends LexerResult<T, R> {
  public T _st;
  public LexerResult_Partial (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, T st) {
    super(_td_T, _td_R);
    this._st = st;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LexerResult_Partial<T, R> o = (LexerResult_Partial<T, R>)other;
    return true && java.util.Objects.equals(this._st, o._st);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._st);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Core.LexerResult.Partial");
    s.append("(");
    s.append(dafny.Helpers.toString(this._st));
    s.append(")");
    return s.toString();
  }
}
