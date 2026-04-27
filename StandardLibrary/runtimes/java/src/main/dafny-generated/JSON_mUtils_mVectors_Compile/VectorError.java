// Class VectorError
// Dafny class VectorError compiled into Java
package JSON_mUtils_mVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class VectorError {
  public VectorError () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VectorError o = (VectorError)other;
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
    s.append("Vectors.VectorError.OutOfMemory");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VectorError> _TYPE = dafny.TypeDescriptor.<VectorError>referenceWithInitializer(VectorError.class, () -> VectorError.Default());
  public static dafny.TypeDescriptor<VectorError> _typeDescriptor() {
    return (dafny.TypeDescriptor<VectorError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VectorError theDefault = VectorError.create();
  public static VectorError Default() {
    return theDefault;
  }
  public static VectorError create() {
    return new VectorError();
  }
  public static VectorError create_OutOfMemory() {
    return create();
  }
  public boolean is_OutOfMemory() { return true; }
  public static java.util.ArrayList<VectorError> AllSingletonConstructors() {
    java.util.ArrayList<VectorError> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new VectorError());
    return singleton_iterator;
  }
}
