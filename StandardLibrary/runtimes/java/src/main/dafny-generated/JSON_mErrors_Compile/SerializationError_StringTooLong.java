// Class SerializationError_StringTooLong
// Dafny class SerializationError_StringTooLong compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializationError_StringTooLong extends SerializationError {
  public dafny.DafnySequence<? extends Character> _s;
  public SerializationError_StringTooLong (dafny.DafnySequence<? extends Character> s) {
    super();
    this._s = s;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializationError_StringTooLong o = (SerializationError_StringTooLong)other;
    return true && java.util.Objects.equals(this._s, o._s);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._s);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder ss = new StringBuilder();
    ss.append("Errors.SerializationError.StringTooLong");
    ss.append("(");
    ss.append(dafny.Helpers.toString(this._s));
    ss.append(")");
    return ss.toString();
  }
}
