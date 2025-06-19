// Class TestInfo
// Dafny class TestInfo compiled into Java
package TestIntermediateKeyWrapping_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class TestInfo {
  public TestInfo () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TestInfo o = (TestInfo)other;
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
    s.append("TestIntermediateKeyWrapping.TestInfo.TestInfo");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TestInfo> _TYPE = dafny.TypeDescriptor.<TestInfo>referenceWithInitializer(TestInfo.class, () -> TestInfo.Default());
  public static dafny.TypeDescriptor<TestInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<TestInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TestInfo theDefault = TestInfo.create();
  public static TestInfo Default() {
    return theDefault;
  }
  public static TestInfo create() {
    return new TestInfo();
  }
  public static TestInfo create_TestInfo() {
    return create();
  }
  public boolean is_TestInfo() { return true; }
  public static java.util.ArrayList<TestInfo> AllSingletonConstructors() {
    java.util.ArrayList<TestInfo> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new TestInfo());
    return singleton_iterator;
  }
}
