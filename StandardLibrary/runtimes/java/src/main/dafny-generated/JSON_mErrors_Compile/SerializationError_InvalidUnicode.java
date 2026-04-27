// Class SerializationError_InvalidUnicode
// Dafny class SerializationError_InvalidUnicode compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializationError_InvalidUnicode extends SerializationError {
  public SerializationError_InvalidUnicode () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializationError_InvalidUnicode o = (SerializationError_InvalidUnicode)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.SerializationError.InvalidUnicode");
    return s.toString();
  }
}
