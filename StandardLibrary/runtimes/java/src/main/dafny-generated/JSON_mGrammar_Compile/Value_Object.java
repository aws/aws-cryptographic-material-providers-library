// Class Value_Object
// Dafny class Value_Object compiled into Java
package JSON_mGrammar_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Value_Object extends Value {
  public Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> _obj;
  public Value_Object (Bracketed<JSON_mUtils_mViews_mCore_Compile.View__, jKeyValue, JSON_mUtils_mViews_mCore_Compile.View__, JSON_mUtils_mViews_mCore_Compile.View__> obj) {
    super();
    this._obj = obj;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Value_Object o = (Value_Object)other;
    return true && java.util.Objects.equals(this._obj, o._obj);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._obj);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Grammar.Value.Object");
    s.append("(");
    s.append(dafny.Helpers.toString(this._obj));
    s.append(")");
    return s.toString();
  }
}
