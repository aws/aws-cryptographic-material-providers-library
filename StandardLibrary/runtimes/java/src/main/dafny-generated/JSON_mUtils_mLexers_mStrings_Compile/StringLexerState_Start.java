// Class StringLexerState_Start
// Dafny class StringLexerState_Start compiled into Java
package JSON_mUtils_mLexers_mStrings_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class StringLexerState_Start extends StringLexerState {
  public StringLexerState_Start () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    StringLexerState_Start o = (StringLexerState_Start)other;
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
    s.append("Strings.StringLexerState.Start");
    return s.toString();
  }
}
