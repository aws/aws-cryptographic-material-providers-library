// Class LexerResult_Reject<T, R>
// Dafny class LexerResult_Reject<T, R> compiled into Java
package JSON_mUtils_mLexers_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class LexerResult_Reject<T, R> extends LexerResult<T, R> {
  public R _err;
  public LexerResult_Reject (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R, R err) {
    super(_td_T, _td_R);
    this._err = err;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LexerResult_Reject<T, R> o = (LexerResult_Reject<T, R>)other;
    return true && java.util.Objects.equals(this._err, o._err);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._err);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Core.LexerResult.Reject");
    s.append("(");
    s.append(dafny.Helpers.toString(this._err));
    s.append(")");
    return s.toString();
  }
}
