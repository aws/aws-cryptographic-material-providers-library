// Class KmsRsaWrapInfo
// Dafny class KmsRsaWrapInfo compiled into Java
package AwsKmsRsaKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsRsaWrapInfo {
  public KmsRsaWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsRsaWrapInfo o = (KmsRsaWrapInfo)other;
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
    s.append("AwsKmsRsaKeyring.KmsRsaWrapInfo.KmsRsaWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsRsaWrapInfo> _TYPE = dafny.TypeDescriptor.<KmsRsaWrapInfo>referenceWithInitializer(KmsRsaWrapInfo.class, () -> KmsRsaWrapInfo.Default());
  public static dafny.TypeDescriptor<KmsRsaWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsRsaWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsRsaWrapInfo theDefault = KmsRsaWrapInfo.create();
  public static KmsRsaWrapInfo Default() {
    return theDefault;
  }
  public static KmsRsaWrapInfo create() {
    return new KmsRsaWrapInfo();
  }
  public static KmsRsaWrapInfo create_KmsRsaWrapInfo() {
    return create();
  }
  public boolean is_KmsRsaWrapInfo() { return true; }
  public static java.util.ArrayList<KmsRsaWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<KmsRsaWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KmsRsaWrapInfo());
    return singleton_iterator;
  }
}
