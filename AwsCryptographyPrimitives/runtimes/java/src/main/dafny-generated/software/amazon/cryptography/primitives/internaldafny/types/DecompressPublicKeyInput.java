// Class DecompressPublicKeyInput
// Dafny class DecompressPublicKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DecompressPublicKeyInput {
  public dafny.DafnySequence<? extends java.lang.Byte> _compressedPublicKey;
  public ECDHCurveSpec _eccCurve;
  public DecompressPublicKeyInput (dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey, ECDHCurveSpec eccCurve) {
    this._compressedPublicKey = compressedPublicKey;
    this._eccCurve = eccCurve;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecompressPublicKeyInput o = (DecompressPublicKeyInput)other;
    return true && java.util.Objects.equals(this._compressedPublicKey, o._compressedPublicKey) && java.util.Objects.equals(this._eccCurve, o._eccCurve);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._compressedPublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput.DecompressPublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._compressedPublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecompressPublicKeyInput> _TYPE = dafny.TypeDescriptor.<DecompressPublicKeyInput>referenceWithInitializer(DecompressPublicKeyInput.class, () -> DecompressPublicKeyInput.Default());
  public static dafny.TypeDescriptor<DecompressPublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecompressPublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecompressPublicKeyInput theDefault = DecompressPublicKeyInput.create(dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()), ECDHCurveSpec.Default());
  public static DecompressPublicKeyInput Default() {
    return theDefault;
  }
  public static DecompressPublicKeyInput create(dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey, ECDHCurveSpec eccCurve) {
    return new DecompressPublicKeyInput(compressedPublicKey, eccCurve);
  }
  public static DecompressPublicKeyInput create_DecompressPublicKeyInput(dafny.DafnySequence<? extends java.lang.Byte> compressedPublicKey, ECDHCurveSpec eccCurve) {
    return create(compressedPublicKey, eccCurve);
  }
  public boolean is_DecompressPublicKeyInput() { return true; }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_compressedPublicKey() {
    return this._compressedPublicKey;
  }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
}
