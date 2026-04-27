// Class GenerateRSAKeyPairInput
// Dafny class GenerateRSAKeyPairInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateRSAKeyPairInput {
  public int _lengthBits;
  public GenerateRSAKeyPairInput (int lengthBits) {
    this._lengthBits = lengthBits;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateRSAKeyPairInput o = (GenerateRSAKeyPairInput)other;
    return true && this._lengthBits == o._lengthBits;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._lengthBits);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput.GenerateRSAKeyPairInput");
    s.append("(");
    s.append(this._lengthBits);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateRSAKeyPairInput> _TYPE = dafny.TypeDescriptor.<GenerateRSAKeyPairInput>referenceWithInitializer(GenerateRSAKeyPairInput.class, () -> GenerateRSAKeyPairInput.Default());
  public static dafny.TypeDescriptor<GenerateRSAKeyPairInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateRSAKeyPairInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateRSAKeyPairInput theDefault = GenerateRSAKeyPairInput.create(0);
  public static GenerateRSAKeyPairInput Default() {
    return theDefault;
  }
  public static GenerateRSAKeyPairInput create(int lengthBits) {
    return new GenerateRSAKeyPairInput(lengthBits);
  }
  public static GenerateRSAKeyPairInput create_GenerateRSAKeyPairInput(int lengthBits) {
    return create(lengthBits);
  }
  public boolean is_GenerateRSAKeyPairInput() { return true; }
  public int dtor_lengthBits() {
    return this._lengthBits;
  }
}
