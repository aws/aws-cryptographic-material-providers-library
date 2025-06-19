// Class Value_String
// Dafny class Value_String compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Value_String extends Value {
  public jstring _str;
  public Value_String (jstring str) {
    super();
    this._str = str;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Value_String o = (Value_String)other;
    return true && java.util.Objects.equals(this._str, o._str);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._str);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Value.String");
    s.append("(");
    s.append(dafny.Helpers.toString(this._str));
    s.append(")");
    return s.toString();
  }
}
