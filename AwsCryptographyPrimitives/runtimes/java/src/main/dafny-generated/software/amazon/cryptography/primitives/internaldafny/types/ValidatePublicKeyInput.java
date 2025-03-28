// Class ValidatePublicKeyInput
// Dafny class ValidatePublicKeyInput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ValidatePublicKeyInput {
  public ECDHCurveSpec _eccCurve;
  public dafny.DafnySequence<? extends java.lang.Byte> _publicKey;
  public ValidatePublicKeyInput (ECDHCurveSpec eccCurve, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    this._eccCurve = eccCurve;
    this._publicKey = publicKey;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ValidatePublicKeyInput o = (ValidatePublicKeyInput)other;
    return true && java.util.Objects.equals(this._eccCurve, o._eccCurve) && java.util.Objects.equals(this._publicKey, o._publicKey);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._eccCurve);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput.ValidatePublicKeyInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._eccCurve));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ValidatePublicKeyInput> _TYPE = dafny.TypeDescriptor.<ValidatePublicKeyInput>referenceWithInitializer(ValidatePublicKeyInput.class, () -> ValidatePublicKeyInput.Default());
  public static dafny.TypeDescriptor<ValidatePublicKeyInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ValidatePublicKeyInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ValidatePublicKeyInput theDefault = software.amazon.cryptography.primitives.internaldafny.types.ValidatePublicKeyInput.create(ECDHCurveSpec.Default(), dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor()));
  public static ValidatePublicKeyInput Default() {
    return theDefault;
  }
  public static ValidatePublicKeyInput create(ECDHCurveSpec eccCurve, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return new ValidatePublicKeyInput(eccCurve, publicKey);
  }
  public static ValidatePublicKeyInput create_ValidatePublicKeyInput(ECDHCurveSpec eccCurve, dafny.DafnySequence<? extends java.lang.Byte> publicKey) {
    return create(eccCurve, publicKey);
  }
  public boolean is_ValidatePublicKeyInput() { return true; }
  public ECDHCurveSpec dtor_eccCurve() {
    return this._eccCurve;
  }
  public dafny.DafnySequence<? extends java.lang.Byte> dtor_publicKey() {
    return this._publicKey;
  }
}
