// Class TestVectorCmmInput
// Dafny class TestVectorCmmInput compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TestVectorCmmInput {
  public KeyDescription _keyDescription;
  public CmmOperation _forOperation;
  public TestVectorCmmInput (KeyDescription keyDescription, CmmOperation forOperation) {
    this._keyDescription = keyDescription;
    this._forOperation = forOperation;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TestVectorCmmInput o = (TestVectorCmmInput)other;
    return true && java.util.Objects.equals(this._keyDescription, o._keyDescription) && java.util.Objects.equals(this._forOperation, o._forOperation);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._keyDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._forOperation);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.TestVectorCmmInput.TestVectorCmmInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._keyDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._forOperation));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TestVectorCmmInput> _TYPE = dafny.TypeDescriptor.<TestVectorCmmInput>referenceWithInitializer(TestVectorCmmInput.class, () -> TestVectorCmmInput.Default());
  public static dafny.TypeDescriptor<TestVectorCmmInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<TestVectorCmmInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TestVectorCmmInput theDefault = TestVectorCmmInput.create(KeyDescription.Default(), CmmOperation.Default());
  public static TestVectorCmmInput Default() {
    return theDefault;
  }
  public static TestVectorCmmInput create(KeyDescription keyDescription, CmmOperation forOperation) {
    return new TestVectorCmmInput(keyDescription, forOperation);
  }
  public static TestVectorCmmInput create_TestVectorCmmInput(KeyDescription keyDescription, CmmOperation forOperation) {
    return create(keyDescription, forOperation);
  }
  public boolean is_TestVectorCmmInput() { return true; }
  public KeyDescription dtor_keyDescription() {
    return this._keyDescription;
  }
  public CmmOperation dtor_forOperation() {
    return this._forOperation;
  }
}
