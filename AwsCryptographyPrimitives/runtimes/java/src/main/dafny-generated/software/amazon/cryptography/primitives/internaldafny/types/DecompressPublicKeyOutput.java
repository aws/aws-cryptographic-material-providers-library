// Class DecompressPublicKeyOutput
// Dafny class DecompressPublicKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecompressPublicKeyOutput {
  public ECCPublicKey _publicKey;
  public DecompressPublicKeyOutput (ECCPublicKey publicKey) {
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecompressPublicKeyOutput o = (DecompressPublicKeyOutput)other;
    return true && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.DecompressPublicKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecompressPublicKeyOutput> _TYPE = dafny.TypeDescriptor.<DecompressPublicKeyOutput>referenceWithInitializer(DecompressPublicKeyOutput.class, () -> DecompressPublicKeyOutput.Default());
  public static dafny.TypeDescriptor<DecompressPublicKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecompressPublicKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecompressPublicKeyOutput theDefault = DecompressPublicKeyOutput.create(ECCPublicKey.Default());
  public static DecompressPublicKeyOutput Default() {
    return theDefault;
  }
  public static DecompressPublicKeyOutput create(ECCPublicKey publicKey) {
    return new DecompressPublicKeyOutput(publicKey);
  }
  public static DecompressPublicKeyOutput create_DecompressPublicKeyOutput(ECCPublicKey publicKey) {
    return create(publicKey);
  }
  public boolean is_DecompressPublicKeyOutput() { return true; }
  public ECCPublicKey dtor_publicKey() {
    return this._publicKey;
  }
}
