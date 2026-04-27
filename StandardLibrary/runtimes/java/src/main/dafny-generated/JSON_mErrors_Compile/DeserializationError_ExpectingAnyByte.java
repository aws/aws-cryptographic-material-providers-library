// Class DeserializationError_ExpectingAnyByte
// Dafny class DeserializationError_ExpectingAnyByte compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_ExpectingAnyByte extends DeserializationError {
  public dafny.DafnySequence<? extends java.lang.Byte> _expected__sq;
  public short _b;
  public DeserializationError_ExpectingAnyByte (dafny.DafnySequence<? extends java.lang.Byte> expected__sq, short b) {
    super();
    this._expected__sq = expected__sq;
    this._b = b;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_ExpectingAnyByte o = (DeserializationError_ExpectingAnyByte)other;
    return true && java.util.Objects.equals(this._expected__sq, o._expected__sq) && this._b == o._b;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._expected__sq);
    hash = ((hash << 5) + hash) + java.lang.Short.hashCode(this._b);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.ExpectingAnyByte");
    s.append("(");
    s.append(dafny.Helpers.toString(this._expected__sq));
    s.append(", ");
    s.append(this._b);
    s.append(")");
    return s.toString();
  }
}
