// Class GenerateECDSASignatureKeyInput
// Dafny class GenerateECDSASignatureKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateECDSASignatureKeyInput {
  public ECDSASignatureAlgorithm _signatureAlgorithm;
  public GenerateECDSASignatureKeyInput (ECDSASignatureAlgorithm signatureAlgorithm) {
    this._signatureAlgorithm = signatureAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateECDSASignatureKeyInput o = (GenerateECDSASignatureKeyInput)other;
    return true && java.util.Objects.equals(this._signatureAlgorithm, o._signatureAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._signatureAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyInput.GenerateECDSASignatureKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._signatureAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateECDSASignatureKeyInput> _TYPE = dafny.TypeDescriptor.<GenerateECDSASignatureKeyInput>referenceWithInitializer(GenerateECDSASignatureKeyInput.class, () -> GenerateECDSASignatureKeyInput.Default());
  public static dafny.TypeDescriptor<GenerateECDSASignatureKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateECDSASignatureKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateECDSASignatureKeyInput theDefault = GenerateECDSASignatureKeyInput.create(ECDSASignatureAlgorithm.Default());
  public static GenerateECDSASignatureKeyInput Default() {
    return theDefault;
  }
  public static GenerateECDSASignatureKeyInput create(ECDSASignatureAlgorithm signatureAlgorithm) {
    return new GenerateECDSASignatureKeyInput(signatureAlgorithm);
  }
  public static GenerateECDSASignatureKeyInput create_GenerateECDSASignatureKeyInput(ECDSASignatureAlgorithm signatureAlgorithm) {
    return create(signatureAlgorithm);
  }
  public boolean is_GenerateECDSASignatureKeyInput() { return true; }
  public ECDSASignatureAlgorithm dtor_signatureAlgorithm() {
    return this._signatureAlgorithm;
  }
}
