// Class HkdfExpandInput
// Dafny class HkdfExpandInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class HkdfExpandInput {
  public DigestAlgorithm _digestAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _prk;
  public dafny.DafnySequence<? extends java.lang.Byte> _info;
  public int _expectedLength;
  public HkdfExpandInput (DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> prk, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    this._digestAlgorithm = digestAlgorithm;
    this._prk = prk;
    this._info = info;
    this._expectedLength = expectedLength;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HkdfExpandInput o = (HkdfExpandInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._prk, o._prk) && java.util.Objects.equals(this._info, o._info) && this._expectedLength == o._expectedLength;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._prk);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._info);
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._expectedLength);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.HkdfExpandInput.HkdfExpandInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._prk));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._info));
    s.append(", ");
    s.append(this._expectedLength);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HkdfExpandInput> _TYPE = dafny.TypeDescriptor.<HkdfExpandInput>referenceWithInitializer(HkdfExpandInput.class, () -> HkdfExpandInput.Default());
  public static dafny.TypeDescriptor<HkdfExpandInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<HkdfExpandInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HkdfExpandInput theDefault = HkdfExpandInput.create(DigestAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), 0);
  public static HkdfExpandInput Default() {
    return theDefault;
  }
  public static HkdfExpandInput create(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> prk, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    return new HkdfExpandInput(digestAlgorithm, prk, info, expectedLength);
  }
  public static HkdfExpandInput create_HkdfExpandInput(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> prk, dafny.DafnySequence<? extends java.lang.Byte> info, int expectedLength) {
    return create(digestAlgorithm, prk, info, expectedLength);
  }
  public boolean is_HkdfExpandInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_prk() {
    return this._prk;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_info() {
    return this._info;
  }
  public int dtor_expectedLength() {
    return this._expectedLength;
  }
}
