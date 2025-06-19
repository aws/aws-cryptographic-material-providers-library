// Class KmsPublicKeyDiscoveryInput
// Dafny class KmsPublicKeyDiscoveryInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KmsPublicKeyDiscoveryInput {
  public dafny.DafnySequence<? extends Character> _recipientKmsIdentifier;
  public KmsPublicKeyDiscoveryInput (dafny.DafnySequence<? extends Character> recipientKmsIdentifier) {
    this._recipientKmsIdentifier = recipientKmsIdentifier;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KmsPublicKeyDiscoveryInput o = (KmsPublicKeyDiscoveryInput)other;
    return true && java.util.Objects.equals(this._recipientKmsIdentifier, o._recipientKmsIdentifier);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._recipientKmsIdentifier);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput.KmsPublicKeyDiscoveryInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._recipientKmsIdentifier));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KmsPublicKeyDiscoveryInput> _TYPE = dafny.TypeDescriptor.<KmsPublicKeyDiscoveryInput>referenceWithInitializer(KmsPublicKeyDiscoveryInput.class, () -> KmsPublicKeyDiscoveryInput.Default());
  public static dafny.TypeDescriptor<KmsPublicKeyDiscoveryInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<KmsPublicKeyDiscoveryInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KmsPublicKeyDiscoveryInput theDefault = KmsPublicKeyDiscoveryInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static KmsPublicKeyDiscoveryInput Default() {
    return theDefault;
  }
  public static KmsPublicKeyDiscoveryInput create(dafny.DafnySequence<? extends Character> recipientKmsIdentifier) {
    return new KmsPublicKeyDiscoveryInput(recipientKmsIdentifier);
  }
  public static KmsPublicKeyDiscoveryInput create_KmsPublicKeyDiscoveryInput(dafny.DafnySequence<? extends Character> recipientKmsIdentifier) {
    return create(recipientKmsIdentifier);
  }
  public boolean is_KmsPublicKeyDiscoveryInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_recipientKmsIdentifier() {
    return this._recipientKmsIdentifier;
  }
}
