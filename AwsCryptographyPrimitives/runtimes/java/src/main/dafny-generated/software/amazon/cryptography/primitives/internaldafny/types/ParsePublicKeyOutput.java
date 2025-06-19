// Class ParsePublicKeyOutput
// Dafny class ParsePublicKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ParsePublicKeyOutput {
  public ECCPublicKey _publicKey;
  public ParsePublicKeyOutput (ECCPublicKey publicKey) {
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ParsePublicKeyOutput o = (ParsePublicKeyOutput)other;
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
    s.append("AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.ParsePublicKeyOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ParsePublicKeyOutput> _TYPE = dafny.TypeDescriptor.<ParsePublicKeyOutput>referenceWithInitializer(ParsePublicKeyOutput.class, () -> ParsePublicKeyOutput.Default());
  public static dafny.TypeDescriptor<ParsePublicKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ParsePublicKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ParsePublicKeyOutput theDefault = ParsePublicKeyOutput.create(ECCPublicKey.Default());
  public static ParsePublicKeyOutput Default() {
    return theDefault;
  }
  public static ParsePublicKeyOutput create(ECCPublicKey publicKey) {
    return new ParsePublicKeyOutput(publicKey);
  }
  public static ParsePublicKeyOutput create_ParsePublicKeyOutput(ECCPublicKey publicKey) {
    return create(publicKey);
  }
  public boolean is_ParsePublicKeyOutput() { return true; }
  public ECCPublicKey dtor_publicKey() {
    return this._publicKey;
  }
}
