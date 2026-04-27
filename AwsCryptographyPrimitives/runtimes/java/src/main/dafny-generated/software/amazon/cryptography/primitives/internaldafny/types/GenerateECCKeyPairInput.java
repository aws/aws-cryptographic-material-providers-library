// Class GenerateECCKeyPairInput
// Dafny class GenerateECCKeyPairInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateECCKeyPairInput {
  public ECDHCurveSpec _eccCurve;
  public GenerateECCKeyPairInput (ECDHCurveSpec eccCurve) {
    this._eccCurve = eccCurve;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateECCKeyPairInput o = (GenerateECCKeyPairInput)other;
    return true && java.util.Objects.equals(this._eccCurve, o._eccCurve);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput.GenerateECCKeyPairInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateECCKeyPairInput> _TYPE = dafny.TypeDescriptor.<GenerateECCKeyPairInput>referenceWithInitializer(GenerateECCKeyPairInput.class, () -> GenerateECCKeyPairInput.Default());
  public static dafny.TypeDescriptor<GenerateECCKeyPairInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateECCKeyPairInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateECCKeyPairInput theDefault = GenerateECCKeyPairInput.create(ECDHCurveSpec.Default());
  public static GenerateECCKeyPairInput Default() {
    return theDefault;
  }
  public static GenerateECCKeyPairInput create(ECDHCurveSpec eccCurve) {
    return new GenerateECCKeyPairInput(eccCurve);
  }
  public static GenerateECCKeyPairInput create_GenerateECCKeyPairInput(ECDHCurveSpec eccCurve) {
    return create(eccCurve);
  }
  public boolean is_GenerateECCKeyPairInput() { return true; }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
}
