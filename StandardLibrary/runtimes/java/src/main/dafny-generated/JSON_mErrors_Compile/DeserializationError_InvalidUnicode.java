// Class DeserializationError_InvalidUnicode
// Dafny class DeserializationError_InvalidUnicode compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_InvalidUnicode extends DeserializationError {
  public DeserializationError_InvalidUnicode () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_InvalidUnicode o = (DeserializationError_InvalidUnicode)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.InvalidUnicode");
    return s.toString();
  }
}
