// Class DeserializationError_ReachedEOF
// Dafny class DeserializationError_ReachedEOF compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_ReachedEOF extends DeserializationError {
  public DeserializationError_ReachedEOF () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_ReachedEOF o = (DeserializationError_ReachedEOF)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.ReachedEOF");
    return s.toString();
  }
}
