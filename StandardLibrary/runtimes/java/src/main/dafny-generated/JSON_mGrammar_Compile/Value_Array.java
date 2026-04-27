// Class Value_Array
// Dafny class Value_Array compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Value_Array extends Value {
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _arr;
  public Value_Array (Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, Value, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> arr) {
    super();
    this._arr = arr;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Value_Array o = (Value_Array)other;
    return true && java.util.Objects.equals(this._arr, o._arr);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._arr);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Value.Array");
    s.append("(");
    s.append(dafny.Helpers.toString(this._arr));
    s.append(")");
    return s.toString();
  }
}
