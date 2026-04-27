// Class ParsePublicKeyInput
// Dafny class ParsePublicKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ParsePublicKeyInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public ParsePublicKeyInput (dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ParsePublicKeyInput o = (ParsePublicKeyInput)other;
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
    s.append("AwsCryptographyPrimitivesTypes.ParsePublicKeyInput.ParsePublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ParsePublicKeyInput> _TYPE = dafny.TypeDescriptor.<ParsePublicKeyInput>referenceWithInitializer(ParsePublicKeyInput.class, () -> ParsePublicKeyInput.Default());
  public static dafny.TypeDescriptor<ParsePublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ParsePublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ParsePublicKeyInput theDefault = ParsePublicKeyInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ParsePublicKeyInput Default() {
    return theDefault;
  }
  public static ParsePublicKeyInput create(dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new ParsePublicKeyInput(publicKey);
  }
  public static ParsePublicKeyInput create_ParsePublicKeyInput(dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return create(publicKey);
  }
  public boolean is_ParsePublicKeyInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
}
