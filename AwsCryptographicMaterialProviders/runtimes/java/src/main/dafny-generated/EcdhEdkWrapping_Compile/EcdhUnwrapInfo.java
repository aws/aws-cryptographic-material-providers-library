// Class EcdhUnwrapInfo
// Dafny class EcdhUnwrapInfo compiled into Java
package EcdhEdkWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class EcdhUnwrapInfo {
  public EcdhUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EcdhUnwrapInfo o = (EcdhUnwrapInfo)other;
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
    s.append("EcdhEdkWrapping.EcdhUnwrapInfo.EcdhUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EcdhUnwrapInfo> _TYPE = dafny.TypeDescriptor.<EcdhUnwrapInfo>referenceWithInitializer(EcdhUnwrapInfo.class, () -> EcdhUnwrapInfo.Default());
  public static dafny.TypeDescriptor<EcdhUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EcdhUnwrapInfo theDefault = EcdhUnwrapInfo.create();
  public static EcdhUnwrapInfo Default() {
    return theDefault;
  }
  public static EcdhUnwrapInfo create() {
    return new EcdhUnwrapInfo();
  }
  public static EcdhUnwrapInfo create_EcdhUnwrapInfo() {
    return create();
  }
  public boolean is_EcdhUnwrapInfo() { return true; }
  public static java.util.ArrayList<EcdhUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<EcdhUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new EcdhUnwrapInfo());
    return singleton_iterator;
  }
}
