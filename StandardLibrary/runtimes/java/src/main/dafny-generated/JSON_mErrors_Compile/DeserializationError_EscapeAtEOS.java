// Class DeserializationError_EscapeAtEOS
// Dafny class DeserializationError_EscapeAtEOS compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_EscapeAtEOS extends DeserializationError {
  public DeserializationError_EscapeAtEOS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_EscapeAtEOS o = (DeserializationError_EscapeAtEOS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.EscapeAtEOS");
    return s.toString();
  }
}
