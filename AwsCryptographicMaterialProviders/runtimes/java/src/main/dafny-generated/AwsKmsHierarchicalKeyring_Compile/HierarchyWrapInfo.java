// Class HierarchyWrapInfo
// Dafny class HierarchyWrapInfo compiled into Java
package AwsKmsHierarchicalKeyring_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class HierarchyWrapInfo {
  public HierarchyWrapInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HierarchyWrapInfo o = (HierarchyWrapInfo)other;
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
    s.append("AwsKmsHierarchicalKeyring.HierarchyWrapInfo.HierarchyWrapInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HierarchyWrapInfo> _TYPE = dafny.TypeDescriptor.<HierarchyWrapInfo>referenceWithInitializer(HierarchyWrapInfo.class, () -> HierarchyWrapInfo.Default());
  public static dafny.TypeDescriptor<HierarchyWrapInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<HierarchyWrapInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HierarchyWrapInfo theDefault = HierarchyWrapInfo.create();
  public static HierarchyWrapInfo Default() {
    return theDefault;
  }
  public static HierarchyWrapInfo create() {
    return new HierarchyWrapInfo();
  }
  public static HierarchyWrapInfo create_HierarchyWrapInfo() {
    return create();
  }
  public boolean is_HierarchyWrapInfo() { return true; }
  public static java.util.ArrayList<HierarchyWrapInfo> AllSingletonConstructors() {
    java.util.ArrayList<HierarchyWrapInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new HierarchyWrapInfo());
    return singleton_iterator;
  }
}
