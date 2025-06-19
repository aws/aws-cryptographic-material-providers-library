// Class HkdfExtractInput
// Dafny class HkdfExtractInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class HkdfExtractInput {
  public DigestAlgorithm _digestAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _salt;
  public dafny.DafnySequence<? extends java.lang.Byte> _ikm;
  public HkdfExtractInput (DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm) {
    this._digestAlgorithm = digestAlgorithm;
    this._salt = salt;
    this._ikm = ikm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HkdfExtractInput o = (HkdfExtractInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._salt, o._salt) && java.util.Objects.equals(this._ikm, o._ikm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._salt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ikm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.HkdfExtractInput.HkdfExtractInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._salt));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ikm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HkdfExtractInput> _TYPE = dafny.TypeDescriptor.<HkdfExtractInput>referenceWithInitializer(HkdfExtractInput.class, () -> HkdfExtractInput.Default());
  public static dafny.TypeDescriptor<HkdfExtractInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<HkdfExtractInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HkdfExtractInput theDefault = HkdfExtractInput.create(DigestAlgorithm.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static HkdfExtractInput Default() {
    return theDefault;
  }
  public static HkdfExtractInput create(DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm) {
    return new HkdfExtractInput(digestAlgorithm, salt, ikm);
  }
  public static HkdfExtractInput create_HkdfExtractInput(DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm) {
    return create(digestAlgorithm, salt, ikm);
  }
  public boolean is_HkdfExtractInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_salt() {
    return this._salt;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ikm() {
    return this._ikm;
  }
}
