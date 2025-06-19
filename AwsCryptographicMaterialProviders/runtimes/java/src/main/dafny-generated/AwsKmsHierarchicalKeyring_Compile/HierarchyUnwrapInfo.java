// Class HierarchyUnwrapInfo
// Dafny class HierarchyUnwrapInfo compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class HierarchyUnwrapInfo {
  public HierarchyUnwrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HierarchyUnwrapInfo o = (HierarchyUnwrapInfo)other;
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
    s.append("AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.HierarchyUnwrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HierarchyUnwrapInfo> _TYPE = dafny.TypeDescriptor.<HierarchyUnwrapInfo>referenceWithInitializer(HierarchyUnwrapInfo.class, () -> HierarchyUnwrapInfo.Default());
  public static dafny.TypeDescriptor<HierarchyUnwrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<HierarchyUnwrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HierarchyUnwrapInfo theDefault = HierarchyUnwrapInfo.create();
  public static HierarchyUnwrapInfo Default() {
    return theDefault;
  }
  public static HierarchyUnwrapInfo create() {
    return new HierarchyUnwrapInfo();
  }
  public static HierarchyUnwrapInfo create_HierarchyUnwrapInfo() {
    return create();
  }
  public boolean is_HierarchyUnwrapInfo() { return true; }
  public static java.util.ArrayList<HierarchyUnwrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<HierarchyUnwrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new HierarchyUnwrapInfo());
    return singleton_iterator;
  }
}
