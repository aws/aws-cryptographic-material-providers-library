// Class JSON_Bool
// Dafny class JSON_Bool compiled into Java
package JSON_mValues_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class JSON_Bool extends JSON {
  public boolean _b;
  public JSON_Bool (boolean b) {
    super();
    this._b = b;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    JSON_Bool o = (JSON_Bool)other;
    return true && this._b == o._b;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._b);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Values.JSON.Bool");
    s.append("(");
    s.append(this._b);
    s.append(")");
    return s.toString();
  }
}
