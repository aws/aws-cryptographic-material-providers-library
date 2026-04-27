// Class DigestInput
// Dafny class DigestInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DigestInput {
  public DigestAlgorithm _digestAlgorithm;
  public dafny.DafnySequence<? extends java.lang.Byte> _message;
  public DigestInput (DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> message) {
    this._digestAlgorithm = digestAlgorithm;
    this._message = message;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DigestInput o = (DigestInput)other;
    return true && java.util.Objects.equals(this._digestAlgorithm, o._digestAlgorithm) && java.util.Objects.equals(this._message, o._message);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._digestAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._message);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DigestInput.DigestInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._digestAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._message));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DigestInput> _TYPE = dafny.TypeDescriptor.<DigestInput>referenceWithInitializer(DigestInput.class, () -> DigestInput.Default());
  public static dafny.TypeDescriptor<DigestInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DigestInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DigestInput theDefault = DigestInput.create(DigestAlgorithm.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static DigestInput Default() {
    return theDefault;
  }
  public static DigestInput create(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return new DigestInput(digestAlgorithm, message);
  }
  public static DigestInput create_DigestInput(DigestAlgorithm digestAlgorithm, dafny.DafnySequence<? extends java.lang.Byte> message) {
    return create(digestAlgorithm, message);
  }
  public boolean is_DigestInput() { return true; }
  public DigestAlgorithm dtor_digestAlgorithm() {
    return this._digestAlgorithm;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_message() {
    return this._message;
  }
}
