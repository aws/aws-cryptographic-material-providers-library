// Class EcdhWrapInfo
// Dafny class EcdhWrapInfo compiled into Java
package EcdhEdkWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class EcdhWrapInfo {
  public EcdhWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EcdhWrapInfo o = (EcdhWrapInfo)other;
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
    s.append("EcdhEdkWrapping.EcdhWrapInfo.EcdhWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EcdhWrapInfo> _TYPE = dafny.TypeDescriptor.<EcdhWrapInfo>referenceWithInitializer(EcdhWrapInfo.class, () -> EcdhWrapInfo.Default());
  public static dafny.TypeDescriptor<EcdhWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<EcdhWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EcdhWrapInfo theDefault = EcdhWrapInfo.create();
  public static EcdhWrapInfo Default() {
    return theDefault;
  }
  public static EcdhWrapInfo create() {
    return new EcdhWrapInfo();
  }
  public static EcdhWrapInfo create_EcdhWrapInfo() {
    return create();
  }
  public boolean is_EcdhWrapInfo() { return true; }
  public static java.util.ArrayList<EcdhWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<EcdhWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new EcdhWrapInfo());
    return singleton_iterator;
  }
}
