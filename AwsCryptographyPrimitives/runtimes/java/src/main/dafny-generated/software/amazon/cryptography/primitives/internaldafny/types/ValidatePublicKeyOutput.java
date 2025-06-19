// Class ValidatePublicKeyOutput
// Dafny class ValidatePublicKeyOutput compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ValidatePublicKeyOutput {
  public boolean _success;
  public ValidatePublicKeyOutput (boolean success) {
    this._success = success;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ValidatePublicKeyOutput o = (ValidatePublicKeyOutput)other;
    return true && this._success == o._success;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + Boolean.hashCode(this._success);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.ValidatePublicKeyOutput");
    s.append("(");
    s.append(this._success);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ValidatePublicKeyOutput> _TYPE = dafny.TypeDescriptor.<ValidatePublicKeyOutput>referenceWithInitializer(ValidatePublicKeyOutput.class, () -> ValidatePublicKeyOutput.Default());
  public static dafny.TypeDescriptor<ValidatePublicKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ValidatePublicKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ValidatePublicKeyOutput theDefault = ValidatePublicKeyOutput.create(false);
  public static ValidatePublicKeyOutput Default() {
    return theDefault;
  }
  public static ValidatePublicKeyOutput create(boolean success) {
    return new ValidatePublicKeyOutput(success);
  }
  public static ValidatePublicKeyOutput create_ValidatePublicKeyOutput(boolean success) {
    return create(success);
  }
  public boolean is_ValidatePublicKeyOutput() { return true; }
  public boolean dtor_success() {
    return this._success;
  }
}
