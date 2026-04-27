// Class DeserializationError_UnterminatedSequence
// Dafny class DeserializationError_UnterminatedSequence compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeserializationError_UnterminatedSequence extends DeserializationError {
  public DeserializationError_UnterminatedSequence () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeserializationError_UnterminatedSequence o = (DeserializationError_UnterminatedSequence)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("Errors.DeserializationError.UnterminatedSequence");
    return s.toString();
  }
}
