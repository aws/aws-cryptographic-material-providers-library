// Class UnescapeError
// Dafny class UnescapeError compiled into Java
package JSON_mUtils_mStr_mCharStrEscaping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class UnescapeError {
  public UnescapeError () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UnescapeError o = (UnescapeError)other;
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
    s.append("CharStrEscaping.UnescapeError.EscapeAtEOS");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UnescapeError> _TYPE = dafny.TypeDescriptor.<UnescapeError>referenceWithInitializer(UnescapeError.class, () -> UnescapeError.Default());
  public static dafny.TypeDescriptor<UnescapeError> _typeDescriptor() {
    return (dafny.TypeDescriptor<UnescapeError>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UnescapeError theDefault = UnescapeError.create();
  public static UnescapeError Default() {
    return theDefault;
  }
  public static UnescapeError create() {
    return new UnescapeError();
  }
  public static UnescapeError create_EscapeAtEOS() {
    return create();
  }
  public boolean is_EscapeAtEOS() { return true; }
  public static java.util.ArrayList<UnescapeError> AllSingletonConstructors() {
    java.util.ArrayList<UnescapeError> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new UnescapeError());
    return singleton_iterator;
  }
}
