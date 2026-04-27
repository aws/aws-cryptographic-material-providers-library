// Class KmsRsaUnwrapInfo
// Dafny class KmsRsaUnwrapInfo compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaUnwrapInfo {
  public KmsRsaUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsRsaUnwrapInfo o = (KmsRsaUnwrapInfo)other;
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
    s.append("AwsKmsRsaKeyring.KmsRsaUnwrapInfo.KmsRsaUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsRsaUnwrapInfo> _TYPE = dafny.TypeDescriptor.<KmsRsaUnwrapInfo>referenceWithInitializer(KmsRsaUnwrapInfo.class, () -> KmsRsaUnwrapInfo.Default());
  public static dafny.TypeDescriptor<KmsRsaUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsRsaUnwrapInfo theDefault = KmsRsaUnwrapInfo.create();
  public static KmsRsaUnwrapInfo Default() {
    return theDefault;
  }
  public static KmsRsaUnwrapInfo create() {
    return new KmsRsaUnwrapInfo();
  }
  public static KmsRsaUnwrapInfo create_KmsRsaUnwrapInfo() {
    return create();
  }
  public boolean is_KmsRsaUnwrapInfo() { return true; }
  public static java.util.ArrayList<KmsRsaUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<KmsRsaUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KmsRsaUnwrapInfo());
    return singleton_iterator;
  }
}
