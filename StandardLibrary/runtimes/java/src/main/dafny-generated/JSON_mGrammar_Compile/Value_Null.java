// Class Value_Null
// Dafny class Value_Null compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Value_Null extends Value {
  public JSON_mUtils_mViews_mCore_Compile.View__ _n;
  public Value_Null (JSON_mUtils_mViews_mCore_Compile.View__ n) {
    super();
    this._n = n;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Value_Null o = (Value_Null)other;
    return true && java.util.Objects.equals(this._n, o._n);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._n);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Value.Null");
    s.append("(");
    s.append(dafny.Helpers.toString(this._n));
    s.append(")");
    return s.toString();
  }
}
