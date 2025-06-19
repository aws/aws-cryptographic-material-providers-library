// Class KmsUnwrapInfo
// Dafny class KmsUnwrapInfo compiled into Java
package AwsKmsKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsUnwrapInfo {
  public KmsUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsUnwrapInfo o = (KmsUnwrapInfo)other;
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
    s.append("AwsKmsKeyring.KmsUnwrapInfo.KmsUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsUnwrapInfo> _TYPE = dafny.TypeDescriptor.<KmsUnwrapInfo>referenceWithInitializer(KmsUnwrapInfo.class, () -> KmsUnwrapInfo.Default());
  public static dafny.TypeDescriptor<KmsUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsUnwrapInfo theDefault = KmsUnwrapInfo.create();
  public static KmsUnwrapInfo Default() {
    return theDefault;
  }
  public static KmsUnwrapInfo create() {
    return new KmsUnwrapInfo();
  }
  public static KmsUnwrapInfo create_KmsUnwrapInfo() {
    return create();
  }
  public boolean is_KmsUnwrapInfo() { return true; }
  public static java.util.ArrayList<KmsUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<KmsUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KmsUnwrapInfo());
    return singleton_iterator;
  }
}
