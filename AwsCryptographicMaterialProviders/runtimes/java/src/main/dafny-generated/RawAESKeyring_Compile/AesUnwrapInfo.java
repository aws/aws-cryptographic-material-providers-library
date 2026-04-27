// Class AesUnwrapInfo
// Dafny class AesUnwrapInfo compiled into Java
package RawAESKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesUnwrapInfo {
  public AesUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesUnwrapInfo o = (AesUnwrapInfo)other;
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
    s.append("RawAESKeyring.AesUnwrapInfo.AesUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AesUnwrapInfo> _TYPE = dafny.TypeDescriptor.<AesUnwrapInfo>referenceWithInitializer(AesUnwrapInfo.class, () -> AesUnwrapInfo.Default());
  public static dafny.TypeDescriptor<AesUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesUnwrapInfo theDefault = AesUnwrapInfo.create();
  public static AesUnwrapInfo Default() {
    return theDefault;
  }
  public static AesUnwrapInfo create() {
    return new AesUnwrapInfo();
  }
  public static AesUnwrapInfo create_AesUnwrapInfo() {
    return create();
  }
  public boolean is_AesUnwrapInfo() { return true; }
  public static java.util.ArrayList<AesUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<AesUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new AesUnwrapInfo());
    return singleton_iterator;
  }
}
