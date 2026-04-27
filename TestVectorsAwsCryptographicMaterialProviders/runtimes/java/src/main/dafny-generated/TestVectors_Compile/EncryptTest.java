// Class EncryptTest
// Dafny class EncryptTest compiled into Java
package TestVectors_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptTest {
  public software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput _input;
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager _cmm;
  public EncryptTestVector _vector;
  public EncryptTest (software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, EncryptTestVector vector) {
    this._input = input;
    this._cmm = cmm;
    this._vector = vector;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptTest o = (EncryptTest)other;
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
    s.append("TestVectors.EncryptTest.EncryptTest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._input));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cmm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._vector));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EncryptTest> _TYPE = dafny.TypeDescriptor.<EncryptTest>referenceWithInitializer(EncryptTest.class, () -> EncryptTest.Default());
  public static dafny.TypeDescriptor<EncryptTest> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptTest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptTest theDefault = EncryptTest.create(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput.Default(), null, EncryptTestVector.Default());
  public static EncryptTest Default() {
    return theDefault;
  }
  public static EncryptTest create(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, EncryptTestVector vector) {
    return new EncryptTest(input, cmm, vector);
  }
  public static EncryptTest create_EncryptTest(software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput input, software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager cmm, EncryptTestVector vector) {
    return create(input, cmm, vector);
  }
  public boolean is_EncryptTest() { return true; }
  public software.amazon.cryptography.materialproviders.internaldafny.types.GetEncryptionMaterialsInput dtor_input() {
    return this._input;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager dtor_cmm() {
    return this._cmm;
  }
  public EncryptTestVector dtor_vector() {
    return this._vector;
  }
}
