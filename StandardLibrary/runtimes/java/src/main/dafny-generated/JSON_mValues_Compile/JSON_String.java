// Class JSON_String
// Dafny class JSON_String compiled into Java
package JSON_mValues_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class JSON_String extends JSON {
  public dafny.DafnySequence<? extends Character> _str;
  public JSON_String (dafny.DafnySequence<? extends Character> str) {
    super();
    this._str = str;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    JSON_String o = (JSON_String)other;
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
    s.append("Values.JSON.String");
    s.append("(");
    s.append(dafny.Helpers.toString(this._str));
    s.append(")");
    return s.toString();
  }
}
