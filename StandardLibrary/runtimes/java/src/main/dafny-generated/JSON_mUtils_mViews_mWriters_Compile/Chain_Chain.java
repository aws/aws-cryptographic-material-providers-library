// Class Chain_Chain
// Dafny class Chain_Chain compiled into Java
package JSON_mUtils_mViews_mWriters_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class Chain_Chain extends Chain {
  public Chain _previous;
  public JSON_mUtils_mViews_mCore_Compile.View__ _v;
  public Chain_Chain (Chain previous, JSON_mUtils_mViews_mCore_Compile.View__ v) {
    super();
    this._previous = previous;
    this._v = v;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Chain_Chain o = (Chain_Chain)other;
    return true && java.util.Objects.equals(this._previous, o._previous) && java.util.Objects.equals(this._v, o._v);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._previous);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._v);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Writers.Chain.Chain");
    s.append("(");
    s.append(dafny.Helpers.toString(this._previous));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._v));
    s.append(")");
    return s.toString();
  }
}
