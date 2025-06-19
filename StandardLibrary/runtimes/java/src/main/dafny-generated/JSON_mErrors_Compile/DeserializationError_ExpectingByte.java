// Class DeserializationError_ExpectingByte
// Dafny class DeserializationError_ExpectingByte compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_ExpectingByte extends DeserializationError {
  public byte _expected;
  public short _b;
  public DeserializationError_ExpectingByte (byte expected, short b) {
    super();
    this._expected = expected;
    this._b = b;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_ExpectingByte o = (DeserializationError_ExpectingByte)other;
    return true && this._expected == o._expected && this._b == o._b;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    hash = ((hash << 5) + hash) + java.lang.Byte.hashCode(this._expected);
    hash = ((hash << 5) + hash) + java.lang.Short.hashCode(this._b);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.ExpectingByte");
    s.append("(");
    s.append(this._expected);
    s.append(", ");
    s.append(this._b);
    s.append(")");
    return s.toString();
  }
}
