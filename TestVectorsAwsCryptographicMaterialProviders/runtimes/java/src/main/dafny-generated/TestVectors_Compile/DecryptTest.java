// Class DecryptTest
// Dafny class DecryptTest compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptTest {
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput _input;
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager _cmm;
  public DecryptTestVector _vector;
  public DecryptTest (software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, DecryptTestVector vector) {
    this._input = input;
    this._cmm = cmm;
    this._vector = vector;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptTest o = (DecryptTest)other;
    return true && java.util.Objects.equals(this._input, o._input) && this._cmm == o._cmm && java.util.Objects.equals(this._vector, o._vector);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._input);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cmm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._vector);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("TestVectors.DecryptTest.DecryptTest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._input));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cmm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._vector));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptTest> _TYPE = dafny.TypeDescriptor.<DecryptTest>referenceWithInitializer(DecryptTest.class, () -> DecryptTest.Default());
  public static dafny.TypeDescriptor<DecryptTest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptTest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptTest theDefault = DecryptTest.create(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput.Default(), null, DecryptTestVector.Default());
  public static DecryptTest Default() {
    return theDefault;
  }
  public static DecryptTest create(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, DecryptTestVector vector) {
    return new DecryptTest(input, cmm, vector);
  }
  public static DecryptTest create_DecryptTest(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, DecryptTestVector vector) {
    return create(input, cmm, vector);
  }
  public boolean is_DecryptTest() { return true; }
  public software.amazon.cryptography.materialproviders.internaldafny.types.DecryptMaterialsInput dtor_input() {
    return this._input;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager dtor_cmm() {
    return this._cmm;
  }
  public DecryptTestVector dtor_vector() {
    return this._vector;
  }
}
