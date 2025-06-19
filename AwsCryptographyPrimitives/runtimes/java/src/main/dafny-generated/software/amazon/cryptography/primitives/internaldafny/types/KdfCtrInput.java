// Class KdfCtrInput
// Dafny class KdfCtrInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KdfCtrInput {
  public DigestAlgorithm _digestAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _ikm;
  public int _expectedLength;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _purpose;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _nonce;
  public KdfCtrInput (DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> purpose, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    this._digestAlgorithm = digestAlgorithm;
    this._ikm = ikm;
    this._expectedLength = expectedLength;
    this._purpose = purpose;
    this._nonce = nonce;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KdfCtrInput o = (KdfCtrInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._ikm, o._ikm) && this._expectedLength == o._expectedLength && java.util.Objects.equals(this._purpose, o._purpose) && java.util.Objects.equals(this._nonce, o._nonce);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ikm);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._expectedLength);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._purpose);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._nonce);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.KdfCtrInput.KdfCtrInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ikm));
    s.append(", ");
    s.append(this._expectedLength);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._purpose));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._nonce));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KdfCtrInput> _TYPE = dafny.TypeDescriptor.<KdfCtrInput>referenceWithInitializer(KdfCtrInput.class, () -> KdfCtrInput.Default());
  public static dafny.TypeDescriptor<KdfCtrInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<KdfCtrInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KdfCtrInput theDefault = KdfCtrInput.create(DigestAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0, Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())));
  public static KdfCtrInput Default() {
    return theDefault;
  }
  public static KdfCtrInput create(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> purpose, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    return new KdfCtrInput(digestAlgorithm, ikm, expectedLength, purpose, nonce);
  }
  public static KdfCtrInput create_KdfCtrInput(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> ikm, int expectedLength, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> purpose, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> nonce) {
    return create(digestAlgorithm, ikm, expectedLength, purpose, nonce);
  }
  public boolean is_KdfCtrInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ikm() {
    return this._ikm;
  }
  public int dtor_expectedLength() {
    return this._expectedLength;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_purpose() {
    return this._purpose;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_nonce() {
    return this._nonce;
  }
}
