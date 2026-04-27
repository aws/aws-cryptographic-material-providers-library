// Class RSAEncryptInput
// Dafny class RSAEncryptInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAEncryptInput {
  public RSAPaddingMode _padding;
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _plaintext;
  public RSAEncryptInput (RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> publicKey, dafny.DafnySequence<? extends java.lang.Byte> plaintext) {
    this._padding = padding;
    this._publicKey = publicKey;
    this._plaintext = plaintext;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSAEncryptInput o = (RSAEncryptInput)other;
    return true && java.util.Objects.equals(this._padding, o._padding) && java.util.Objects.equals(this._publicKey, o._publicKey) && java.util.Objects.equals(this._plaintext, o._plaintext);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._padding);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._plaintext);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.RSAEncryptInput.RSAEncryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._padding));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._plaintext));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RSAEncryptInput> _TYPE = dafny.TypeDescriptor.<RSAEncryptInput>referenceWithInitializer(RSAEncryptInput.class, () -> RSAEncryptInput.Default());
  public static dafny.TypeDescriptor<RSAEncryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RSAEncryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RSAEncryptInput theDefault = RSAEncryptInput.create(RSAPaddingMode.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static RSAEncryptInput Default() {
    return theDefault;
  }
  public static RSAEncryptInput create(RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> publicKey, dafny.DafnySequence<? extends java.lang.Byte> plaintext) {
    return new RSAEncryptInput(padding, publicKey, plaintext);
  }
  public static RSAEncryptInput create_RSAEncryptInput(RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> publicKey, dafny.DafnySequence<? extends java.lang.Byte> plaintext) {
    return create(padding, publicKey, plaintext);
  }
  public boolean is_RSAEncryptInput() { return true; }
  public RSAPaddingMode dtor_padding() {
    return this._padding;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_plaintext() {
    return this._plaintext;
  }
}
