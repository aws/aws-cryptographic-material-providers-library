// Class SerializationError_IntTooLarge
// Dafny class SerializationError_IntTooLarge compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializationError_IntTooLarge extends SerializationError {
  public java.math.BigInteger _i;
  public SerializationError_IntTooLarge (java.math.BigInteger i) {
    super();
    this._i = i;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializationError_IntTooLarge o = (SerializationError_IntTooLarge)other;
    return true && java.util.Objects.equals(this._i, o._i);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._i);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.SerializationError.IntTooLarge");
    s.append("(");
    s.append(dafny.Helpers.toString(this._i));
    s.append(")");
    return s.toString();
  }
}
