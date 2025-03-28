// Class RSADecryptInput
// Dafny class RSADecryptInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RSADecryptInput {
  public RSAPaddingMode _padding;
  public dafny.DafnySequence<? extends java.lang.Byte> _privateKey;
  public dafny.DafnySequence<? extends java.lang.Byte> _cipherText;
  public RSADecryptInput (RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> cipherText) {
    this._padding = padding;
    this._privateKey = privateKey;
    this._cipherText = cipherText;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSADecryptInput o = (RSADecryptInput)other;
    return true && java.util.Objects.equals(this._padding, o._padding) && java.util.Objects.equals(this._privateKey, o._privateKey) && java.util.Objects.equals(this._cipherText, o._cipherText);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._padding);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._privateKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._cipherText);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.RSADecryptInput.RSADecryptInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._padding));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._privateKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._cipherText));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RSADecryptInput> _TYPE = dafny.TypeDescriptor.<RSADecryptInput>referenceWithInitializer(RSADecryptInput.class, () -> RSADecryptInput.Default());
  public static dafny.TypeDescriptor<RSADecryptInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RSADecryptInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RSADecryptInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.RSADecryptInput.create(RSAPaddingMode.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static RSADecryptInput Default() {
    return theDefault;
  }
  public static RSADecryptInput create(RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> cipherText) {
    return new RSADecryptInput(padding, privateKey, cipherText);
  }
  public static RSADecryptInput create_RSADecryptInput(RSAPaddingMode padding, dafny.DafnySequence<? extends java.lang.Byte> privateKey, dafny.DafnySequence<? extends java.lang.Byte> cipherText) {
    return create(padding, privateKey, cipherText);
  }
  public boolean is_RSADecryptInput() { return true; }
  public RSAPaddingMode dtor_padding() {
    return this._padding;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_privateKey() {
    return this._privateKey;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_cipherText() {
    return this._cipherText;
  }
}
