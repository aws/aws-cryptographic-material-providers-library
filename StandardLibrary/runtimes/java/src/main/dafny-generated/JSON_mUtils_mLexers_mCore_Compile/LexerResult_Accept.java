// Class LexerResult_Accept<T, R>
// Dafny class LexerResult_Accept<T, R> compiled into Java
package JSON_mUtils_mLexers_mCore_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class LexerResult_Accept<T, R> extends LexerResult<T, R> {
  public LexerResult_Accept (dafny.TypeDescriptor<T> _td_T, dafny.TypeDescriptor<R> _td_R) {
    super(_td_T, _td_R);
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LexerResult_Accept<T, R> o = (LexerResult_Accept<T, R>)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Core.LexerResult.Accept");
    return s.toString();
  }
}
