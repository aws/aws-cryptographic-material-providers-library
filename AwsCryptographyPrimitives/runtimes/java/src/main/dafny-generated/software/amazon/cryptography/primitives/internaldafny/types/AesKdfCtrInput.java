// Class AesKdfCtrInput
// Dafny class AesKdfCtrInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AesKdfCtrInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _ikm;
  public int _expectedLength;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _nonce;
  public AesKdfCtrInput (dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    this._ikm = ikm;
    this._expectedLength = expectedLength;
    this._nonce = nonce;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AesKdfCtrInput o = (AesKdfCtrInput)other;
    return true && java.util.Objects.equals(this._ikm, o._ikm) && this._expectedLength == o._expectedLength && java.util.Objects.equals(this._nonce, o._nonce);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ikm);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._expectedLength);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._nonce);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.AesKdfCtrInput.AesKdfCtrInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ikm));
    s.append(", ");
    s.append(this._expectedLength);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._nonce));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<AesKdfCtrInput> _TYPE = dafny.TypeDescriptor.<AesKdfCtrInput>referenceWithInitializer(AesKdfCtrInput.class, () -> AesKdfCtrInput.Default());
  public static dafny.TypeDescriptor<AesKdfCtrInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<AesKdfCtrInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AesKdfCtrInput theDefault = AesKdfCtrInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
  public static AesKdfCtrInput Default() {
    return theDefault;
  }
  public static AesKdfCtrInput create(dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    return new AesKdfCtrInput(ikm, expectedLength, nonce);
  }
  public static AesKdfCtrInput create_AesKdfCtrInput(dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    return create(ikm, expectedLength, nonce);
  }
  public boolean is_AesKdfCtrInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ikm() {
    return this._ikm;
  }
  public int dtor_expectedLength() {
    return this._expectedLength;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_nonce() {
    return this._nonce;
  }
}
