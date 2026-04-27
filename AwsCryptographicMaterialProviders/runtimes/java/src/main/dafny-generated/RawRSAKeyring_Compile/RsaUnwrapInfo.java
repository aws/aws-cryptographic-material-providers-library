// Class RsaUnwrapInfo
// Dafny class RsaUnwrapInfo compiled into Java
package RawRSAKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class RsaUnwrapInfo {
  public RsaUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RsaUnwrapInfo o = (RsaUnwrapInfo)other;
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
    s.append("RawRSAKeyring.RsaUnwrapInfo.RsaUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RsaUnwrapInfo> _TYPE = dafny.TypeDescriptor.<RsaUnwrapInfo>referenceWithInitializer(RsaUnwrapInfo.class, () -> RsaUnwrapInfo.Default());
  public static dafny.TypeDescriptor<RsaUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<RsaUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RsaUnwrapInfo theDefault = RsaUnwrapInfo.create();
  public static RsaUnwrapInfo Default() {
    return theDefault;
  }
  public static RsaUnwrapInfo create() {
    return new RsaUnwrapInfo();
  }
  public static RsaUnwrapInfo create_RsaUnwrapInfo() {
    return create();
  }
  public boolean is_RsaUnwrapInfo() { return true; }
  public static java.util.ArrayList<RsaUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<RsaUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new RsaUnwrapInfo());
    return singleton_iterator;
  }
}
