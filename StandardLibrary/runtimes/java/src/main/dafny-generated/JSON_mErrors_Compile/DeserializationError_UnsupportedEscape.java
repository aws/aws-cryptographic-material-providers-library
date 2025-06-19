// Class DeserializationError_UnsupportedEscape
// Dafny class DeserializationError_UnsupportedEscape compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_UnsupportedEscape extends DeserializationError {
  public dafny.DafnySequence<? extends Character> _str;
  public DeserializationError_UnsupportedEscape (dafny.DafnySequence<? extends Character> str) {
    super();
    this._str = str;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_UnsupportedEscape o = (DeserializationError_UnsupportedEscape)other;
    return true && java.util.Objects.equals(this._str, o._str);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._str);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.UnsupportedEscape");
    s.append("(");
    s.append(dafny.Helpers.toString(this._str));
    s.append(")");
    return s.toString();
  }
}
