// Class StringLexerState_End
// Dafny class StringLexerState_End compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StringLexerState_End extends StringLexerState {
  public StringLexerState_End () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StringLexerState_End o = (StringLexerState_End)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Strings.StringLexerState.End");
    return s.toString();
  }
}
