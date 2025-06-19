// Class DeserializationError_EmptyNumber
// Dafny class DeserializationError_EmptyNumber compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_EmptyNumber extends DeserializationError {
  public DeserializationError_EmptyNumber () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_EmptyNumber o = (DeserializationError_EmptyNumber)other;
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
    s.append("Errors.DeserializationError.EmptyNumber");
    return s.toString();
  }
}
