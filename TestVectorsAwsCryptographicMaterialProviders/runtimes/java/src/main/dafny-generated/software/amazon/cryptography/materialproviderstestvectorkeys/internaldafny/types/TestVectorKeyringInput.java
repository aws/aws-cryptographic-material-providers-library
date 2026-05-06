// Class TestVectorKeyringInput
// Dafny class TestVectorKeyringInput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TestVectorKeyringInput {
  public KeyDescription _keyDescription;
  public TestVectorKeyringInput (KeyDescription keyDescription) {
    this._keyDescription = keyDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TestVectorKeyringInput o = (TestVectorKeyringInput)other;
    return true && java.util.Objects.equals(this._keyDescription, o._keyDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorKeyringInput.TestVectorKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TestVectorKeyringInput> _TYPE = dafny.TypeDescriptor.<TestVectorKeyringInput>referenceWithInitializer(TestVectorKeyringInput.class, () -> TestVectorKeyringInput.Default());
  public static dafny.TypeDescriptor<TestVectorKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TestVectorKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TestVectorKeyringInput theDefault = TestVectorKeyringInput.create(KeyDescription.Default());
  public static TestVectorKeyringInput Default() {
    return theDefault;
  }
  public static TestVectorKeyringInput create(KeyDescription keyDescription) {
    return new TestVectorKeyringInput(keyDescription);
  }
  public static TestVectorKeyringInput create_TestVectorKeyringInput(KeyDescription keyDescription) {
    return create(keyDescription);
  }
  public boolean is_TestVectorKeyringInput() { return true; }
  public KeyDescription dtor_keyDescription() {
    return this._keyDescription;
  }
}
