// Class JSON_Number
// Dafny class JSON_Number compiled into Java
package JSON_mValues_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class JSON_Number extends JSON {
  public Decimal _num;
  public JSON_Number (Decimal num) {
    super();
    this._num = num;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    JSON_Number o = (JSON_Number)other;
    return true && java.util.Objects.equals(this._num, o._num);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._num);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Values.JSON.Number");
    s.append("(");
    s.append(dafny.Helpers.toString(this._num));
    s.append(")");
    return s.toString();
  }
}
