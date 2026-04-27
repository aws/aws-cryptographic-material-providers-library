// Class Value_Bool
// Dafny class Value_Bool compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Value_Bool extends Value {
  public JSON_mUtils_mViews_mCore_Compile.View__ _b;
  public Value_Bool (JSON_mUtils_mViews_mCore_Compile.View__ b) {
    super();
    this._b = b;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Value_Bool o = (Value_Bool)other;
    return true && java.util.Objects.equals(this._b, o._b);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._b);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Value.Bool");
    s.append("(");
    s.append(dafny.Helpers.toString(this._b));
    s.append(")");
    return s.toString();
  }
}
