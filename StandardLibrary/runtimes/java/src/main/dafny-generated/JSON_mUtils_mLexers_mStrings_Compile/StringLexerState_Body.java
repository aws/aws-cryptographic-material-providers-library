// Class StringLexerState_Body
// Dafny class StringLexerState_Body compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StringLexerState_Body extends StringLexerState {
  public boolean _escaped;
  public StringLexerState_Body (boolean escaped) {
    super();
    this._escaped = escaped;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StringLexerState_Body o = (StringLexerState_Body)other;
    return true && this._escaped == o._escaped;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._escaped);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Strings.StringLexerState.Body");
    s.append("(");
    s.append(this._escaped);
    s.append(")");
    return s.toString();
  }
}
