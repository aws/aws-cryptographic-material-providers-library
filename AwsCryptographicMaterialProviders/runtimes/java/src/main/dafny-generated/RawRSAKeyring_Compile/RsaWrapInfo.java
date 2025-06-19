// Class RsaWrapInfo
// Dafny class RsaWrapInfo compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaWrapInfo {
  public RsaWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RsaWrapInfo o = (RsaWrapInfo)other;
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
    s.append("RawRSAKeyring.RsaWrapInfo.RsaWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RsaWrapInfo> _TYPE = dafny.TypeDescriptor.<RsaWrapInfo>referenceWithInitializer(RsaWrapInfo.class, () -> RsaWrapInfo.Default());
  public static dafny.TypeDescriptor<RsaWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RsaWrapInfo theDefault = RsaWrapInfo.create();
  public static RsaWrapInfo Default() {
    return theDefault;
  }
  public static RsaWrapInfo create() {
    return new RsaWrapInfo();
  }
  public static RsaWrapInfo create_RsaWrapInfo() {
    return create();
  }
  public boolean is_RsaWrapInfo() { return true; }
  public static java.util.ArrayList<RsaWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<RsaWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RsaWrapInfo());
    return singleton_iterator;
  }
}
