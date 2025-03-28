// Class HMacInput
// Dafny class HMacInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class HMacInput {
  public DigestAlgorithm _digestAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _key;
  public dafny.DafnySequence<? extends java.lang.Byte> _message;
  public HMacInput (DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> message) {
    this._digestAlgorithm = digestAlgorithm;
    this._key = key;
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    HMacInput o = (HMacInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._key, o._key) && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._key);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.HMacInput.HMacInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._key));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<HMacInput> _TYPE = dafny.TypeDescriptor.<HMacInput>referenceWithInitializer(HMacInput.class, () -> HMacInput.Default());
  public static dafny.TypeDescriptor<HMacInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<HMacInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final HMacInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.HMacInput.create(DigestAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static HMacInput Default() {
    return theDefault;
  }
  public static HMacInput create(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return new HMacInput(digestAlgorithm, key, message);
  }
  public static HMacInput create_HMacInput(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> key, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return create(digestAlgorithm, key, message);
  }
  public boolean is_HMacInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_key() {
    return this._key;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_message() {
    return this._message;
  }
}
