// Class SerializationError_OutOfMemory
// Dafny class SerializationError_OutOfMemory compiled into Java
package JSON_mErrors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class SerializationError_OutOfMemory extends SerializationError {
  public SerializationError_OutOfMemory () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SerializationError_OutOfMemory o = (SerializationError_OutOfMemory)other;
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
    s.append("Errors.SerializationError.OutOfMemory");
    return s.toString();
  }
}
