// Class DeserializationError_IntOverflow
// Dafny class DeserializationError_IntOverflow compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_IntOverflow extends DeserializationError {
  public DeserializationError_IntOverflow () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_IntOverflow o = (DeserializationError_IntOverflow)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.IntOverflow");
    return s.toString();
  }
}
