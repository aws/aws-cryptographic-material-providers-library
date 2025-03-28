// Class HkdfInput
// Dafny class HkdfInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class HkdfInput {
  public DigestAlgorithm _digestAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _salt;
  public dafny.DafnySequence<? extends java.lang.Byte> _ikm;
  public dafny.DafnySequence<? extends java.lang.Byte> _info;
  public int _expectedLength;
  public HkdfInput (DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    this._digestAlgorithm = digestAlgorithm;
    this._salt = salt;
    this._ikm = ikm;
    this._info = info;
    this._expectedLength = expectedLength;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HkdfInput o = (HkdfInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._salt, o._salt) && java.util.Objects.equals(this._ikm, o._ikm) && java.util.Objects.equals(this._info, o._info) && this._expectedLength == o._expectedLength;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._salt);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ikm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._info);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._expectedLength);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.HkdfInput.HkdfInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._salt));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ikm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._info));
    s.append(", ");
    s.append(this._expectedLength);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HkdfInput> _TYPE = dafny.TypeDescriptor.<HkdfInput>referenceWithInitializer(HkdfInput.class, () -> HkdfInput.Default());
  public static dafny.TypeDescriptor<HkdfInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<HkdfInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HkdfInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.HkdfInput.create(DigestAlgorithm.Default(), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0);
  public static HkdfInput Default() {
    return theDefault;
  }
  public static HkdfInput create(DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    return new HkdfInput(digestAlgorithm, salt, ikm, info, expectedLength);
  }
  public static HkdfInput create_HkdfInput(DigestAlgorithm digestAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> salt, dafny.DafnySequence<? extends java.lang.Byte> ikm, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    return create(digestAlgorithm, salt, ikm, info, expectedLength);
  }
  public boolean is_HkdfInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_salt() {
    return this._salt;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_ikm() {
    return this._ikm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_info() {
    return this._info;
  }
  public int dtor_expectedLength() {
    return this._expectedLength;
  }
}
