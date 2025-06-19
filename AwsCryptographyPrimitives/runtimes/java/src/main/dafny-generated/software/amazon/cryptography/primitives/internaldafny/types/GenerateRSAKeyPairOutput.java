// Class GenerateRSAKeyPairOutput
// Dafny class GenerateRSAKeyPairOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateRSAKeyPairOutput {
  public RSAPublicKey _publicKey;
  public RSAPrivateKey _privateKey;
  public GenerateRSAKeyPairOutput (RSAPublicKey publicKey, RSAPrivateKey privateKey) {
    this._publicKey = publicKey;
    this._privateKey = privateKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateRSAKeyPairOutput o = (GenerateRSAKeyPairOutput)other;
    return true && java.util.Objects.equals(this._publicKey, o._publicKey) && java.util.Objects.equals(this._privateKey, o._privateKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput.GenerateRSAKeyPairOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateRSAKeyPairOutput> _TYPE = dafny.TypeDescriptor.<GenerateRSAKeyPairOutput>referenceWithInitializer(GenerateRSAKeyPairOutput.class, () -> GenerateRSAKeyPairOutput.Default());
  public static dafny.TypeDescriptor<GenerateRSAKeyPairOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateRSAKeyPairOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateRSAKeyPairOutput theDefault = GenerateRSAKeyPairOutput.create(RSAPublicKey.Default(), RSAPrivateKey.Default());
  public static GenerateRSAKeyPairOutput Default() {
    return theDefault;
  }
  public static GenerateRSAKeyPairOutput create(RSAPublicKey publicKey, RSAPrivateKey privateKey) {
    return new GenerateRSAKeyPairOutput(publicKey, privateKey);
  }
  public static GenerateRSAKeyPairOutput create_GenerateRSAKeyPairOutput(RSAPublicKey publicKey, RSAPrivateKey privateKey) {
    return create(publicKey, privateKey);
  }
  public boolean is_GenerateRSAKeyPairOutput() { return true; }
  public RSAPublicKey dtor_publicKey() {
    return this._publicKey;
  }
  public RSAPrivateKey dtor_privateKey() {
    return this._privateKey;
  }
}
